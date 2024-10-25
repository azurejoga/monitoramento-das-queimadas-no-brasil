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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2b5f67-d92b-3189-80db-7bc0d189dc61 | -3.5792 | -46.06111 | 2024-10-25 16:52:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 28827b70-05b9-3cb8-8837-248630685e36 | -3.56181 | -46.18652 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9e2667d6-1a1a-3fe2-8f48-dfdfa01edf7a | -3.49546 | -46.1578 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cea1746b-a7c7-3273-9d1e-38bdfeed7b0c | -3.49145 | -46.15846 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 20c8460a-cc7f-3c5c-99da-c186d99ad436 | -3.48741 | -46.37703 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d9bde2d5-ce2c-355c-9e17-d5be8ee6f4e5 | -3.4866 | -46.37191 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1b32b1d8-4b47-3efe-9d10-db4558215895 | -3.3341 | -46.27448 | 2024-10-25 16:52:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a8fa9634-ad78-3f53-9eb4-9ba7ea8cf6e1 | -3.28376 | -46.33218 | 2024-10-25 16:52:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b6dbc27-7555-36d5-9c20-eef0dfd5d098 | -3.18957 | -46.17893 | 2024-10-25 16:52:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8cd3ffe0-64cc-3ae8-927d-b10bbb08110b | -3.03622 | -46.39787 | 2024-10-25 16:52:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ec612bdb-ce79-3eb1-9a99-780e0adebf97 | -2.56331 | -46.07334 | 2024-10-25 16:52:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 795df8fd-50f8-314e-a7f9-c3053702f95c | -2.32486 | -46.04382 | 2024-10-25 16:52:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a94c2f2e-23ee-3e05-9214-28f96ad3cb0f | -2.31778 | -45.9185 | 2024-10-25 16:52:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3131a605-3abc-3b19-8958-b3679b81a250 | -2.31719 | -45.91474 | 2024-10-25 16:52:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 05851060-0915-3d32-9d18-186e9d1aa673 | -2.31362 | -45.91917 | 2024-10-25 16:52:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4caf9808-6908-355a-af66-84dd9bebdaa1 | -2.31303 | -45.91541 | 2024-10-25 16:52:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8fdc1451-ab82-3f50-9f19-6da34b11da8d | -2.30947 | -45.91987 | 2024-10-25 16:52:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8aab57d8-c24c-302e-a7e5-ec239898974c | -4.11723 | -46.24144 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed9bde23-53ca-3e85-b5b4-5cfc0099088e | -3.99092 | -46.18057 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ee8dea4-0285-3507-bf6b-fa95261daef8 | -3.9352 | -46.16468 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a1a613c7-9725-3442-a42f-2b2b677bef90 | -3.93177 | -46.16874 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 57a9415f-71f0-32ef-a46f-f1e16fc863a7 | -3.93121 | -46.16529 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 085a8fb8-ab54-3156-9a46-92624661dd6d | -3.92895 | -46.15148 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e660874b-f6a5-3046-a48f-dcb448ebe123 | -5.00992 | -46.90016 | 2024-10-25 16:52:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1495d4f6-6271-3336-b412-d4d30b7f8129 | -5.00879 | -46.89807 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 645e2028-6295-3f94-aab3-6e37f2e131c5 | -4.96464 | -46.74093 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e5d28bd9-b125-377e-a301-2482365a85a8 | -4.84867 | -46.89002 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01f40fc8-dce8-3966-a57b-3349c5849344 | -6.35345 | -47.8478 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 153adf96-70bb-3cce-9669-4bfa8e56972a | -6.34931 | -47.84437 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3a7b2f1a-dfa1-338b-bf36-a0e28d126a78 | -6.31562 | -47.88227 | 2024-10-25 16:52:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a0fae0d4-fc90-334e-a5cc-447f313a778c | -6.12486 | -47.98391 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1ab8de04-38ef-3205-b37f-71d9b88f2084 | -5.97261 | -47.95931 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4a16a908-5475-36a5-82b3-219c9d9b7676 | -5.9691 | -47.95986 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 94c236ad-5ecb-3016-93e6-d89f19ca20ab | -5.96882 | -47.93553 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1a11a67e-f7c1-35c6-a890-2c9a4c487e78 | -5.96819 | -47.9316 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 17e0cd5b-4c3e-3c87-aba8-d8b9b661f38d | -5.96558 | -47.96042 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 624988ce-725d-327f-b8f3-f01dd16fec6f | -5.96207 | -47.96098 | 2024-10-25 16:52:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c3d7c4f-8ec4-37ab-b47f-3940c7a8ac56 | -5.91365 | -47.68203 | 2024-10-25 16:52:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1bb50ee2-eb53-3814-bf78-fab16309355c | -5.85668 | -47.68666 | 2024-10-25 16:52:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ac907e17-ff91-33ac-808f-4809104e8dab | -5.45587 | -47.12178 | 2024-10-25 16:52:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9bddc0c7-3bcb-310f-b959-47c4daaa405c | -5.45518 | -47.11741 | 2024-10-25 16:52:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| adfdd738-3b23-3c11-a294-ad7f7d768d91 | -5.43008 | -46.49793 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8a382711-1680-3cc6-941d-88ac9fcb91d1 | -5.41417 | -46.5687 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3f6e53ec-a5f1-3e51-8a4c-e3119915db35 | -5.41035 | -46.56929 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 15961818-6625-38e2-92e0-3846dab2ca6d | -5.40654 | -46.56985 | 2024-10-25 16:52:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 534f63eb-4117-3e06-9788-a1d7066a67f2 | -6.5263 | -47.27155 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 615bfe7b-66f7-316b-9cb8-4daa0836bc72 | -6.52269 | -47.27216 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0157bada-54c7-3cbf-a664-c65f64e8bf9f | -6.51841 | -46.78519 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 472facfe-133b-390b-8a4c-580772e4b27e | -6.51774 | -47.26442 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69cb4ee2-ccbb-3ff9-8ce0-6295c089701e | -6.5147 | -46.78573 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 3c1b4ba5-0076-364b-a31f-786d1b742ffa | -6.50725 | -46.68059 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5babae1e-6f45-339d-b1e2-3be1802196a0 | -6.50532 | -46.68244 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f7b6af89-c123-3e50-9c88-9810c54faa7e | -6.3977 | -47.55267 | 2024-10-25 16:52:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dccaaa99-7255-3322-9f24-0aec4334c7de | -6.38973 | -47.14607 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0aabd0dc-6187-3be7-9c4a-82334a0cee1a | -6.38904 | -47.14183 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e98abf01-4891-3938-96c0-270e9e4770b4 | -6.38541 | -47.14243 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf66af47-9027-38cb-b86c-17195276139e | -6.38472 | -47.13821 | 2024-10-25 16:52:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ea2de447-d2a6-3115-933d-915518f7b878 | -6.15951 | -46.71317 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 10a6ee4d-3aa8-3f68-a0b7-b0a1f89165c4 | -6.15578 | -46.71379 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f6719568-0aeb-377c-a19f-9cb09795cdd2 | -6.12731 | -47.00897 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 88a76d97-7528-3751-acce-d9706298d92e | -6.12485 | -47.0128 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c6571de-deb3-36a2-ad6a-bd5657ff71cc | -6.1113 | -47.2351 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b76e18e-5da6-34b2-8dba-578c9c1adb59 | -6.10766 | -47.23569 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e1135d1-dab6-31b5-a494-fc010b03da09 | -6.0625 | -46.90598 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 20d01aa7-4924-38f7-ace4-7594140d0721 | -6.05951 | -46.91102 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 139a41b2-b2c3-37c4-a087-c081a30de840 | -6.04628 | -46.89959 | 2024-10-25 16:52:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fecf17cc-940d-39b1-bf18-4cccda594e48 | -5.9351 | -47.0728 | 2024-10-25 16:52:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| e0bc1d9c-a961-3a35-a6f3-161d142bf8e3 | -5.81075 | -46.61909 | 2024-10-25 16:52:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f764670-2b48-3452-819b-433102989a1b | -5.70169 | -47.18232 | 2024-10-25 16:52:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| be8c85f5-3168-3d12-bb07-5f73ddd5bb71 | -6.69363 | -48.20778 | 2024-10-25 16:52:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ea1086af-744c-3870-9e13-57aae8ea8762 | -6.61475 | -47.66441 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0797e5b2-c641-3333-b9e0-8f60b3a80ff5 | -6.49234 | -47.85157 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e91b0037-f09e-35fb-8176-046882b958f2 | -6.48946 | -47.85609 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7845c51d-f4c3-3375-b18a-ccc44bd52552 | -6.48883 | -47.85215 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6810438a-f25a-3670-beb1-028a831fe5df | -6.48531 | -47.8527 | 2024-10-25 16:52:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa52233e-7540-3aef-9343-e825164cd21e | -7.81193 | -47.64399 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 093a86fc-5781-3ad0-803e-dca6fc07379e | -7.79756 | -48.10647 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e05a7851-0852-3b0e-941f-2b44c0bb40dd | -7.74556 | -47.82125 | 2024-10-25 16:52:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 404be2c3-7681-3d78-bb53-88d7985a5901 | -7.70573 | -48.25989 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 34b26b4f-7a68-38dd-bdc5-0ebef3fdf317 | -7.69583 | -47.95545 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17784962-9bfe-3ae3-8abd-b966830787b5 | -7.57485 | -47.88061 | 2024-10-25 16:52:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9420a8c0-f4b0-3969-9149-7bdfabe5c366 | -7.40177 | -48.35803 | 2024-10-25 16:52:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cb97a4dc-c5cd-3d38-b9f2-93280a68d2a6 | -7.32288 | -47.62347 | 2024-10-25 16:52:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5325f696-924c-31de-bb4f-e5d4a157039a | -7.31936 | -47.62402 | 2024-10-25 16:52:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 74792226-6eee-3c36-9037-027dd07c2a43 | -7.30522 | -47.67474 | 2024-10-25 16:52:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 637572a2-8725-3cfa-8e4d-418138c360fe | -7.28041 | -47.83549 | 2024-10-25 16:52:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8071e8f3-17f4-3b6e-9e6d-52a051e665da | -7.25172 | -47.76804 | 2024-10-25 16:52:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 727f736a-f0d7-3e61-9756-d233df9a8cc5 | -7.02766 | -47.79552 | 2024-10-25 16:52:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f0d2027-3d12-37ce-9397-584196aa1777 | -6.9897 | -47.78969 | 2024-10-25 16:52:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a30e42f-5dfe-3e40-8b0e-3aa4bfe16739 | -6.97443 | -47.91982 | 2024-10-25 16:52:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b753b093-2947-322b-ad4c-bd802a181409 | -6.94462 | -48.1726 | 2024-10-25 16:52:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 635ff64c-c234-3d1b-b686-729278fd3155 | -6.7919 | -47.24812 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 729de031-b77a-30e1-8b12-af7051b98f8e | -6.7752 | -47.25934 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ebe81979-518b-319f-8f5d-3b5eaa4ee073 | -6.76485 | -47.17111 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f957e025-2f43-32d4-90b6-e989d04a7549 | -6.75322 | -47.23746 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c5abaa26-7761-35d8-b263-5269da31591f | -6.74493 | -47.20887 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a86bdfe-63ce-3023-8c5d-0e98e06cfe00 | -6.6833 | -46.96598 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 9329662e-aeef-3032-b7a3-35cea7e41abd | -6.67011 | -47.06886 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08309d06-7bed-323c-96b3-0f9d49015eb0 | -6.66939 | -47.06731 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72e8ae30-c303-3e73-b677-2bd9779540d2 | -6.64563 | -46.91692 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README178.md)
