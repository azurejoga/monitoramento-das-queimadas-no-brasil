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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eed8b0dd-17ec-31cb-988b-38e78be93684 | -13.29665 | -43.55294 | 2026-07-02 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 610735c8-972c-309a-9db7-f56ec9985a25 | -9.18946 | -45.32026 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 738cb1db-67be-322e-a9a0-8fdfdfa149d6 | -12.51508 | -48.29133 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 35c6e01f-e937-3009-b673-1a2ee6f5efc5 | -12.7644 | -44.48057 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f528bc1-5384-3f05-8eae-74d20f6e140b | -11.00385 | -47.18515 | 2026-07-02 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7d244d05-3dff-3e73-b0d3-a89bbda01564 | -10.37718 | -46.69259 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80e78ce5-5cad-33ca-8b6c-147f62507242 | -11.87316 | -45.60912 | 2026-07-02 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b49464c3-b692-34a3-ad9f-bd84d2628649 | -10.37797 | -46.68849 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c3aac3f-fe0a-3fcf-a430-fdd9924e9334 | -12.86851 | -44.34652 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 0b83acb7-5ceb-3b81-a240-d1e505b310f9 | -11.00157 | -47.18307 | 2026-07-02 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d04181d6-5afd-38d2-b400-3f3aaf5f75ca | -8.71816 | -48.34169 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d4b894af-7060-335c-89d5-2bd176b51a8a | -12.76237 | -44.4915 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b282ba0a-e171-385d-8a38-d460a83ff746 | -12.75374 | -44.48416 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 705.9 |
| 681e6a32-a9db-376e-9c18-7674f97a3acc | -12.85421 | -44.34367 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5a0775c8-b588-3eb0-baca-749db4c80c03 | -9.16253 | -47.23679 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fdd8d6e-0c8f-32e7-93d7-80722540818f | -12.50829 | -48.28695 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 731180fe-9bd0-30e1-bb22-4b3af95168b4 | -11.91569 | -43.38717 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af754680-f7ec-3ddc-8084-b0efffb222b7 | -12.86652 | -44.3571 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 9f1b8ad2-6feb-34a0-9fdb-1d45d818cc24 | -8.50319 | -47.20164 | 2026-07-02 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ab3819-552d-3db0-8131-83b4067c3b0a | -12.77481 | -44.50532 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b6b57e8-ce19-3625-a719-55c71003155a | -12.78751 | -44.49072 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 79979ce7-52f9-3bb4-8914-2d5d6c8d50c8 | -9.74864 | -49.03011 | 2026-07-02 03:45:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f77b8bb-0a9a-3f4a-b618-09dbd8809975 | -10.38041 | -46.67582 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79d75eda-db30-3d6d-84ae-21c72b304006 | -11.85606 | -48.24262 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f681972-94ae-3d6e-8b4b-5dba569e14eb | -8.95662 | -37.99435 | 2026-07-02 03:45:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9efe6a0c-92f6-3661-bce8-274cf68e0d93 | -11.92024 | -43.38807 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcf04e89-e395-35e8-82c7-e5eefce9d310 | -12.74891 | -44.48325 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 142a5bed-a38e-37da-b35e-1e879715cef9 | -12.74028 | -44.47591 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de8ff7f8-9ffe-3a82-ba48-a92f64850fda | -8.71266 | -48.33486 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0b644a1-6c22-3f91-a796-c35513b79899 | -9.24612 | -46.42555 | 2026-07-02 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b1004cb-fe78-3a86-ab2e-1115530d4eaf | -12.86375 | -44.34554 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 976ac3c6-1fc8-3f25-993e-6532db8c28a0 | -10.94235 | -43.04541 | 2026-07-02 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 19314dec-84f7-3d72-bc44-64987eeeb653 | -9.74555 | -49.03484 | 2026-07-02 03:45:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 037b8296-44e8-3e76-9cee-a3e6c164d84d | -12.86949 | -44.3413 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f8de17ab-d343-3e16-828e-7b3018359721 | -10.37136 | -46.69153 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d17787a6-ad83-3ba9-8f70-ba0be9d0afa9 | -12.77684 | -44.49434 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de5ba467-e96e-3acf-8b83-51e9c04744a1 | -12.74787 | -44.48875 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b8d3c73e-2f3d-31cb-97f2-7d4fc185673d | -10.94688 | -43.04625 | 2026-07-02 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 18743b67-18db-3af3-9991-e750f115cd0f | -12.87327 | -44.34749 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 61e874dd-a1aa-38f1-8cb0-600aa4e58a36 | -10.84368 | -45.05799 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a218fbc-7383-31a2-a66f-d74aa7bfdaee | -9.2125 | -45.32487 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe5c4510-a6c2-3410-aa81-697f4b628764 | -12.52164 | -48.28455 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 816ea939-fc39-361c-a110-5860dbd63627 | -8.49702 | -47.20041 | 2026-07-02 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0676ba0-04ba-31db-9e93-795676b23eb0 | -9.15639 | -47.23562 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67b92f2b-6c17-35e6-b3bf-7813f27b7a97 | -12.75578 | -44.47323 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 994766b2-1940-3500-a4b8-97bff2fa2350 | -12.87229 | -44.35274 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| bdd5210b-5188-31b3-93a5-0e027ccac174 | -12.8522 | -44.35431 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| fa4709d4-118a-3daf-82b8-8593907d4fb9 | -11.91558 | -43.39074 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40ad9f9f-5d28-3390-8b66-66c37623a02b | -12.5268 | -48.29074 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2d195f22-cbdd-33d9-9b93-766e918447bc | -12.76617 | -44.49794 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d3614683-6006-302a-9f71-db494d025044 | -10.80467 | -48.56744 | 2026-07-02 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36eb3592-4495-32b5-a52d-a4445e73f293 | -8.71339 | -48.34268 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 42fb67dc-ade4-351f-8e7c-29903f5c12e2 | -9.21315 | -45.3214 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80630509-435c-3386-b9d6-de15ef8753d2 | -11.84985 | -48.2413 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e9989731-41ae-3710-9ecb-40c4aa8780a4 | -10.84368 | -45.06257 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0a8d809-c1a5-3c44-a3c5-eeb8bc9eeeb7 | -12.85522 | -44.33836 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e9dbabb5-97e4-3558-bb05-96991e43094e | -12.51548 | -48.28324 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d4070c6-1d1b-3510-876d-9adcc13feb0a | -7.90545 | -48.24648 | 2026-07-02 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99933b24-b8d2-3e39-937e-d31c6dec8338 | -8.71924 | -48.33619 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| b6da296e-f89c-3f8e-a817-55495dd9f68e | -10.79817 | -48.56635 | 2026-07-02 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abf61df9-f661-3711-b762-ae5855995511 | -10.37543 | -46.67038 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ddc541-dbcb-3461-88a7-ad6b72c3706b | -12.86474 | -44.3403 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4fb1e016-cf47-3baf-9048-ae34edb06b0a | -9.20164 | -45.32286 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7223858-5e6a-3217-a865-c2fdea5f49fb | -12.78269 | -44.48979 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ada7317a-6c85-3e88-8147-aef7de08ac03 | -9.20771 | -45.3204 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a29ffba-c267-3367-925e-04d440f4112c | -12.7606 | -44.47417 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cf45211-513e-32e0-b32f-f403a337ec5e | -8.49807 | -47.20225 | 2026-07-02 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0caea9a3-13f2-3521-8a23-ac6a0364be9b | -10.69642 | -49.61166 | 2026-07-02 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93b6774a-d9a0-32e8-91af-53c4cbd94384 | -12.85798 | -44.34991 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f8049d2d-50db-39d4-8663-9f813438f2ae | -11.92013 | -43.39161 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1a6a83e-a852-39f1-a854-004ff0eb8f6b | -12.86175 | -44.35616 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c0ec62df-0814-3a96-a5bc-0445d9d40c8e | -12.52781 | -48.28584 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d061bb7-61ec-3f5b-b857-fe8fda883195 | -12.84742 | -44.3534 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 6269af7a-3d42-3a60-87a2-fd7b1a858c5e | -12.86275 | -44.35084 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8b8c56c7-1045-33ea-b4d5-1735f8071814 | -12.74304 | -44.48783 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f761ebd9-92a6-3cd7-bb93-bf02bb7a3098 | -9.7468 | -49.0285 | 2026-07-02 03:45:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abe83a5e-7a42-3a67-8463-a70d4a5033bf | -12.771 | -44.49889 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f0dde49-407f-3425-9df4-944d2927e4ac | -9.15624 | -47.23366 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 753a140d-f58d-3804-9036-82995721fbce | -10.69557 | -49.61485 | 2026-07-02 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5f0e55e-a4c5-3bbf-9fe5-5a77df7c5d38 | -12.62173 | -44.66269 | 2026-07-02 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bebf9b3-d77a-3e79-9015-4b27294bbfb8 | -12.76821 | -44.48698 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ca97a232-23da-3021-89be-7a8830e19ff9 | -13.56246 | -44.10244 | 2026-07-02 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad6993c7-3863-3d65-9684-1ef3f57285da | -8.71157 | -48.3404 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a656477f-1dce-3c15-bd31-0471a368d23f | -8.72101 | -48.33855 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| bdd89e8b-1afe-30ee-b1ae-ffe26178d876 | -12.51605 | -48.28645 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 495d16c8-925f-3e5f-9405-3b813027d561 | -10.79901 | -48.56286 | 2026-07-02 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 671c27f8-cd30-34ca-aead-90852f14872d | -12.61683 | -44.66178 | 2026-07-02 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b45d9ea-88a9-3fbd-b7d9-74dca3fc15da | -9.19686 | -45.31833 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b2f88e0-a185-3e6f-b282-34315f3a26b9 | -13.30115 | -43.5538 | 2026-07-02 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8561052-7228-3043-97fe-7a98ef158617 | -11.40762 | -49.01203 | 2026-07-02 03:45:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e8c9fe5-1d99-3635-83e8-6d51c87ca21c | -11.49132 | -47.39342 | 2026-07-02 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 264bd0fd-6c2e-3cf5-84b2-9ef97ef5023b | -10.84428 | -45.05941 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c8f5312-972c-3435-909e-3fdbd19c3926 | -12.74408 | -44.48232 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| edfbd88c-b94f-323f-b788-039cf14cfd36 | -10.37877 | -46.68431 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e313fa8-b326-3642-9231-fee0107b518a | -9.21793 | -45.32592 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 752a535d-dbe4-34fc-bb6d-b426a65247a8 | -9.20707 | -45.32386 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec593153-eaae-36ed-981f-64307e3371b5 | -11.00298 | -47.18975 | 2026-07-02 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aff284bd-c70c-3aab-9ccd-0f3f8003e8c5 | -10.95057 | -43.05175 | 2026-07-02 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 1cff5062-abfd-36a6-b0de-ea6642c4eacb | -13.2991 | -43.55523 | 2026-07-02 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93b3bcce-eafc-3b79-8348-01619786541c | -9.19143 | -45.3173 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README9.md)
