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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e6ed464-b2b1-37ba-a1fb-732881eeadc8 | 1.7905 | -55.91372 | 2025-10-17 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| bcac68cf-09b5-38a3-bec9-8bfa01dd8443 | 2.234 | -55.88845 | 2025-10-17 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 36653a96-681f-3ded-943c-d329cb4dc59e | 0.88676 | -51.11709 | 2025-10-17 12:34:00 | TERRA_M-T | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 410fe657-b6f0-3cff-a857-048a37f115d1 | 1.822 | -55.71509 | 2025-10-17 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| adab1e09-dda7-3157-850a-a1548b675cd6 | 1.78099 | -55.93153 | 2025-10-17 12:34:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| d1a46c9d-604e-3b87-8485-3684a45c80ae | 1.03192 | -51.21877 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 6d3f334f-05c2-37b7-8968-238310fe31ad | 1.10252 | -51.14629 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 28df10cb-2857-31e8-9aa3-b78423a5cc9c | 1.04201 | -51.22634 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 892e60cf-dc08-3795-b03e-45d1d7ecfcd0 | 1.0962 | -51.10244 | 2025-10-17 12:34:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 54f386b6-d643-356c-bf57-5be1040cad5f | -0.90306 | -47.55018 | 2025-10-17 12:34:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 553976a2-9d75-3f54-b375-a95638b1290d | 2.0752 | -55.80728 | 2025-10-17 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| b6cfff5f-0827-3969-9db3-b615d49a99d2 | 1.72806 | -55.78282 | 2025-10-17 12:34:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 740bdd1f-1a88-3505-9a63-37481a1a9ee1 | -8.19497 | -43.31898 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.9 |
| b1067542-45b2-3125-bbd3-55535626b45d | -5.82918 | -42.24278 | 2025-10-17 12:36:00 | TERRA_M-T | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 69a373e7-430c-39e7-8536-3ad5d5f4e036 | -6.58859 | -43.92229 | 2025-10-17 12:36:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1023e2fe-8a16-3456-b575-814bb03f661f | -3.98487 | -42.47514 | 2025-10-17 12:36:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| bcd1b3c7-2343-3fc6-9c23-c9717e11ca6d | -8.27323 | -47.12722 | 2025-10-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 4d6e1900-20ab-3497-a16f-4d8ed7eb8ff9 | -7.35505 | -43.85448 | 2025-10-17 12:36:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| d30875ba-1dc1-3030-9378-a654c91c7e92 | -8.52488 | -44.5807 | 2025-10-17 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 86f4a9d6-01dc-35c9-aa10-a91acebabf5f | -8.52465 | -44.57517 | 2025-10-17 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 4185edae-db20-375f-91fe-b5e1e949afb1 | -7.838 | -44.1263 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 540a538c-cf05-3d21-872c-41afc4171c08 | -8.18063 | -47.04111 | 2025-10-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 79309219-c1dd-31f0-bc9c-796f7888b891 | -8.82407 | -47.30359 | 2025-10-17 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7bc60061-7834-3a74-98f8-f98fdd22a65e | -8.23107 | -43.99313 | 2025-10-17 12:36:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| eafc8156-d181-31ec-bd1e-592d0397f862 | -4.4127 | -43.39714 | 2025-10-17 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 6d2ef520-f1e0-37e2-8bac-a0f54891ef95 | -8.3971 | -46.27866 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 403ae0bd-a5ef-3202-97a4-dff49b9f75d1 | -8.409 | -46.28684 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 6b0c5fbe-8c09-3943-a8d6-bc19ca195dcf | -5.85762 | -42.32799 | 2025-10-17 12:36:00 | TERRA_M-T | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| f7dfef71-cbad-3aaf-a3c2-dd7dca9a4229 | -8.12073 | -45.59261 | 2025-10-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a29e2775-1002-32dc-9563-412e493721e3 | -8.99224 | -45.35968 | 2025-10-17 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1e039fc8-fa1a-3abd-b6fb-2446009caffb | -8.27862 | -47.1344 | 2025-10-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 507e5ad8-3877-37f6-b474-d34ee0ea37c5 | -3.20213 | -52.57712 | 2025-10-17 12:36:00 | TERRA_M-T | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 43fc22cc-cff8-33bc-a152-fa689a560322 | -7.37185 | -44.21346 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b79f02fe-91e5-388b-97a3-7a9f4284900e | -8.30309 | -43.44288 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| 04b2d437-e4a9-3597-8f40-ca2667be1f26 | -3.23421 | -45.96714 | 2025-10-17 12:36:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 42b40216-4991-3138-ab1b-db995b7c6f45 | -8.58204 | -45.44715 | 2025-10-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5acbf9b0-f26b-343c-ac46-ca7292200563 | -6.03627 | -46.34713 | 2025-10-17 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b290ae74-ba30-36a9-aced-3f402a385fdc | -8.30737 | -43.40852 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.5 |
| 50a021fd-e0a9-39d3-9f6a-f997e6152d5d | -9.10357 | -46.68327 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c70cfb2e-d3a2-385f-b4bd-3f9e0172a463 | -4.01249 | -44.2051 | 2025-10-17 12:36:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f2320de3-353c-35c2-8c8c-04b6162ad744 | -9.08311 | -48.0248 | 2025-10-17 12:36:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8d5692c8-3831-3bbc-a86b-fd8b50573352 | -7.38951 | -45.38424 | 2025-10-17 12:36:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 421117fc-6413-3adc-bb25-e9e5a9a933ad | -7.12525 | -44.71386 | 2025-10-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 99d7e1ec-81d6-31e9-a6c7-b037d74f6458 | -8.16367 | -46.06676 | 2025-10-17 12:36:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cbf2f0e5-c525-3730-9a7a-c131d173e768 | -9.03719 | -46.68783 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 1434475e-8a33-3afd-bfe3-8742b03be052 | -7.67558 | -50.49934 | 2025-10-17 12:36:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8aec0e87-085b-3da3-84cf-54115e4c65df | -8.28076 | -47.11719 | 2025-10-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8a555205-b81b-311f-bb92-1f293a9a54aa | -2.70754 | -49.85394 | 2025-10-17 12:36:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07f9323a-0d93-3db2-ba00-201417fc0b4a | -7.45467 | -45.69144 | 2025-10-17 12:36:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4526ded8-05fb-3de5-b281-da6fc0bec3a1 | -8.98704 | -45.35351 | 2025-10-17 12:36:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 640ecb94-e7af-3aa1-b35a-b860383b800c | -9.14628 | -46.64951 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| dceac562-1daa-3238-8f54-13941a4bc572 | -7.4864 | -47.02387 | 2025-10-17 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 307450a9-9cf8-3170-827a-05a02100c0a7 | -4.42526 | -43.40526 | 2025-10-17 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d78d1d13-4f1b-3717-96b7-2136bac6738a | -8.37632 | -46.23661 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 547f7517-ca96-3ffe-b7ad-a0580359a4ea | -8.45206 | -44.18452 | 2025-10-17 12:36:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 39e1a69b-9ab5-3ef9-9ceb-fda242e07070 | -8.26632 | -44.08915 | 2025-10-17 12:36:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3e88de57-7826-3378-96b6-8e123180a7e8 | -6.08407 | -44.67017 | 2025-10-17 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e0e0f065-363d-36aa-b3f4-fb3985956659 | -4.8855 | -45.94964 | 2025-10-17 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| c9849c1e-d199-39bb-a18b-ff32b43f64ae | -8.57714 | -45.42823 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 83a5040a-8e73-3a95-93cd-f2953645c127 | -7.98151 | -44.1871 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 649f13d5-9ffa-3724-85b8-59bc228e92df | -7.12197 | -44.73919 | 2025-10-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| ccdf2497-30ad-3e80-a686-6a1bba439063 | -2.615 | -52.04318 | 2025-10-17 12:36:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a25d1b61-726d-35d6-8e39-8254c9e59bb3 | -3.98042 | -42.50935 | 2025-10-17 12:36:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| e9443c4d-7382-3c06-b2db-e15051d14539 | -8.5396 | -44.58322 | 2025-10-17 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2e6b67a6-d230-3797-b096-e87690dfab21 | -8.53936 | -44.57766 | 2025-10-17 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 59ea6998-502a-3463-b427-9018127753c8 | -8.16248 | -43.31529 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| 224a2304-fac3-34f4-806d-f1f4a9f120a4 | -3.5023 | -52.48901 | 2025-10-17 12:36:00 | TERRA_M-T | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bb43e33b-461b-3b5f-95c9-2b3a52b509ef | -6.53467 | -55.04528 | 2025-10-17 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e5ddba53-050a-3b9b-a5d3-3a56f7eda9aa | -3.97324 | -42.50124 | 2025-10-17 12:36:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 003bac6a-4c61-37c5-84f8-0d734622f11e | -6.08089 | -44.69493 | 2025-10-17 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d2947b2e-8346-33b8-8b45-3f381bf66266 | -8.33775 | -46.23032 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f67f28f3-74c1-3f51-863b-97034d771e86 | -7.83589 | -44.13137 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.1 |
| ef202b3c-19f7-3077-ae2d-f5aca0d784ae | -7.12807 | -44.72073 | 2025-10-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 93b092bb-5d09-37a6-b044-8cae32d820db | -8.45578 | -44.15436 | 2025-10-17 12:36:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 43a24038-e8e2-3f34-9a10-011ada918159 | -7.39821 | -44.74683 | 2025-10-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 0a557589-e6f0-3526-a1a3-ead66568d695 | -8.3154 | -43.41497 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| 1b1642bf-4d46-324f-811b-27229f85cec5 | -9.02162 | -46.60756 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c91db801-2d37-3a4b-ab36-8ec75f2bdea8 | -8.2755 | -47.10999 | 2025-10-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e5cf2d7a-a538-38ea-80cb-0a4da45ec912 | -8.0862 | -45.42815 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 09ca1564-2f24-367e-bb69-0fc9edf557a6 | -8.40997 | -46.28033 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e7002b88-8548-3783-8755-12746faabf05 | -7.98178 | -49.96444 | 2025-10-17 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a13b1814-be9f-3cd7-836f-7a5ba53e6b97 | -7.0795 | -44.24869 | 2025-10-17 12:36:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 6c35ad70-9bf3-3d1e-acf4-6befcfaec36b | -7.98326 | -49.95373 | 2025-10-17 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 99a1605c-3582-398f-b40e-1533ba126de3 | -6.58254 | -48.76945 | 2025-10-17 12:36:00 | TERRA_M-T | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| b9426ae4-735d-3b3a-9aea-420df97093a3 | -5.82561 | -42.23522 | 2025-10-17 12:36:00 | TERRA_M-T | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 0e2c80af-f23c-3c91-b7c2-2c00e4d25ba3 | -5.61196 | -45.17883 | 2025-10-17 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 2ef3c1e2-89a0-3ad9-9db5-d47c78f7f2f5 | -4.42911 | -43.37594 | 2025-10-17 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 32ab22e1-5fc3-3805-adb5-5e20a2c55c86 | -6.58662 | -43.94643 | 2025-10-17 12:36:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| be9775f4-a404-3c44-9c5e-26cc1405f21b | -2.94864 | -47.31152 | 2025-10-17 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2243e74f-ff50-378b-81f8-7f9a84da44f5 | -7.98511 | -44.1579 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 443.7 |
| 58b5cc25-a768-3bc0-bca7-9b8c1ef2cbe8 | -8.82985 | -47.31093 | 2025-10-17 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8dbb5005-d19a-3198-9b9c-299fd17516ba | -6.93405 | -43.70996 | 2025-10-17 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e5c27444-9aa5-3a19-844b-fc2e0648ebcb | -2.87903 | -50.72137 | 2025-10-17 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ca3ee924-39bf-3b51-aaf9-7600fc1af678 | -8.1237 | -45.56978 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 9b367b25-931f-3bff-8f92-c334aa2db50f | -8.40335 | -46.22636 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| bc3513a7-428d-37cb-b193-c6c45770a497 | -5.9995 | -44.15208 | 2025-10-17 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 291ab192-e56a-3d45-868a-c89b6ef31ef6 | -4.41002 | -43.40341 | 2025-10-17 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| d54242d3-5469-37a9-ada8-ccbcdaf0c689 | -7.39528 | -44.74046 | 2025-10-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 907baf7a-1a9f-3629-ad0f-961db22ca32e | -7.99292 | -49.95501 | 2025-10-17 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c6235245-55fd-3154-997d-9a0d3c1e31df | -4.01957 | -44.18603 | 2025-10-17 12:36:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |


[Clique aqui para ver as próximas entradas](README119.md)
