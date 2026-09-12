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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7de8431-0285-3d9e-a30f-3010383a41f3 | -6.11148 | -52.24498 | 2026-09-12 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e30435a1-7fc4-311c-8c12-511a7891e704 | -3.2157 | -56.83947 | 2026-09-12 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee29d36b-a17f-3d4b-984e-48915fc6e8d1 | -4.53417 | -54.96398 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dd67495-243d-3446-862e-4bb2ecf7cf45 | -2.67298 | -57.50832 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2760693f-43ba-3f35-986f-8e8156c139e3 | -4.87124 | -56.00058 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1ad6a5a-bdeb-3a3c-95f6-a07ca8df192a | -3.23245 | -46.9548 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f545a611-438f-3f58-aadd-f3ed3c47a9f4 | -2.93194 | -57.91079 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6930103e-27ad-3815-b638-2c4fb8a0fc18 | -2.94838 | -50.4064 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| fd9d2454-6078-3228-a15e-9b3bf55be696 | -3.07301 | -51.33507 | 2026-09-12 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb39da9-5c16-3831-b292-5a0966ad5f21 | -2.47008 | -48.04512 | 2026-09-12 05:27:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b6e0104-212c-3734-a5ce-505c56e41865 | -2.66889 | -57.51163 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd61c968-e451-38d9-9115-e47b78b70693 | -4.53828 | -54.96467 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ab14098-9607-378a-9930-19753a877f33 | -4.53005 | -54.96329 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878a915a-7577-3b68-b9a9-20d74a56ae81 | -3.86235 | -49.22319 | 2026-09-12 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38a7ef05-9cda-3481-9a44-c97c1c60fdbe | -4.53472 | -54.96024 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 056e088b-75cd-3116-839d-946fbd21a3d5 | -6.501 | -47.59887 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 504d301e-5569-3745-822c-32f6d180835d | -2.95883 | -50.41175 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 32dbd8e8-3052-38cc-a1c7-eaf045367545 | -4.53884 | -54.96089 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cf00786-de92-30b1-b960-d5452cc37a22 | -3.19574 | -51.0192 | 2026-09-12 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e6b28eb-b7e4-3688-8579-4b72aa128b33 | -2.95777 | -50.4189 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 22013968-644b-3eff-8abd-e0b7fb155a94 | -2.94182 | -50.41272 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 8478dbcc-4746-39de-8b18-3f558b473265 | -2.9386 | -50.39623 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cddfc8a4-a699-34f1-ad62-4e2c47332dca | -3.11112 | -61.48001 | 2026-09-12 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae15fc02-f52c-37f1-a9d2-812801bc74e4 | -2.94135 | -50.4148 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7cfc6bce-7540-33a1-8d24-fca28c691b31 | -2.72452 | -57.64479 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 470a46e6-5299-3ee0-9bd0-ad6b8c0de58d | -3.16325 | -58.6448 | 2026-09-12 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 604c5ae8-8030-3aac-9258-80bdef674454 | -5.81968 | -53.80426 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02e3f48d-c7b3-3550-a73f-ba842968b2eb | -2.83943 | -53.98939 | 2026-09-12 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7055da3-4a4c-3cbe-a063-a2512ca4d58d | -1.77379 | -54.94429 | 2026-09-12 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3f5dd1d-6640-3daa-b737-9abd783a02c0 | -3.22459 | -46.96042 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a8c251d-ae2f-3a52-a20b-22c14043ac83 | -2.94551 | -50.38773 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba939d9e-5725-3827-9daf-7db0a913cc68 | -5.28229 | -56.04076 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2865609d-d4ef-30c8-ac63-ed888168da81 | -2.71766 | -57.62034 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 565231c2-8795-3aeb-a518-fa6945d2820e | -4.35496 | -54.77351 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ec330dc-72b4-3b30-8c04-7edf6558887a | -2.9528 | -50.41449 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d246a1e0-b4e4-35fb-a8a0-faa16ce8f5fc | -2.96096 | -50.39741 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| e6bf5ee6-d45a-3ff4-bfa5-90871cf4ee3b | -2.66949 | -57.50778 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 443de029-a606-3cc0-b270-e321a523b3de | -2.93838 | -50.47407 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1b3f18c-9e68-33eb-afec-2a933042b78e | -2.96311 | -50.38294 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0278c789-4631-3a19-9c46-791c2700aa26 | -5.82035 | -53.79972 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58eb1acb-c6bb-3a77-97c9-7be9be4bba30 | -5.0979 | -56.12517 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6020c2c8-40d5-358f-8c29-6be17f995234 | -2.96204 | -50.39016 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8d897a97-1554-3494-b08a-81cae95bc997 | -2.72003 | -57.60508 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03888b1f-793e-3d84-892e-87dfbf1687e4 | -2.67237 | -57.51216 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ea95927-93b1-31a7-aa20-051fa61e123f | -3.15637 | -48.60963 | 2026-09-12 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4f0d0ea-3a9e-3979-8500-32478eee1b86 | -2.67426 | -54.59062 | 2026-09-12 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df59f430-8f57-3560-bf3d-47689f3efcb7 | -3.22597 | -46.95424 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0a669917-c507-3c58-b789-7bfea3595660 | -2.94301 | -50.40408 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 40272403-ddcf-3dec-8255-de2d83738117 | -5.78966 | -53.81901 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 92e9ab80-0971-319c-b6b4-d9c693f5978a | -2.9654 | -50.40541 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 043f095b-abf8-371d-a542-d298e2a60591 | -4.36477 | -47.78076 | 2026-09-12 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4490875e-fb18-3a1d-9faf-1c42eb74a304 | -2.91507 | -54.11822 | 2026-09-12 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bab3979-e314-34d0-b167-4e3bcf979c2d | -2.83018 | -57.64129 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8491092-0c47-3fef-856d-3c00ce47d76d | -2.94577 | -50.38625 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8fbc064-33ee-33c2-a0e5-2251b7baa944 | -2.95228 | -50.41805 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1a6266c7-476f-3f52-9e5c-7c28483a6407 | -4.5336 | -54.9678 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00dbd021-be25-3b97-8f26-de7f7a48e8b5 | -3.19622 | -51.01593 | 2026-09-12 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9859953-9b98-3ddc-8ca0-eaf4a2835c07 | -6.11107 | -52.24791 | 2026-09-12 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e24db0d-2607-328e-83d8-c05ca3cf0d64 | -2.95102 | -50.3885 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93de693a-9a52-3b9c-b162-94196386e40c | -5.85636 | -53.87743 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bdf7915-13d3-385f-8d87-6e57487ddb40 | -5.79488 | -53.81502 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe3ea3c0-a485-3422-937f-b82e22d8658a | -2.9576 | -50.3821 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb6a1973-7b5b-33d7-8c5d-4bfd169fdd65 | -3.89278 | -55.81805 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e6e23ff-74a6-30f1-83de-67307eea7bba | -1.77857 | -55.50287 | 2026-09-12 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835bc22e-b763-3612-b8c3-359e35e7d012 | -2.94943 | -50.39927 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b2553197-ab92-3793-975e-7956a2d6e86a | -5.79355 | -53.82425 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc7141b2-cb8f-38c7-b8db-ddcf6120b5e9 | -5.82423 | -53.80494 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0f3c6b1-4c29-3ea6-b670-c10ec052d652 | -2.9434 | -50.40203 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 56d61607-52fd-39d6-8526-4cc42013b3a3 | -4.98121 | -56.13013 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f57377a-95cc-3059-a7c4-6e2d1aaacd06 | -3.86077 | -49.21948 | 2026-09-12 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01e007e8-d430-3ac7-ba6f-18d070e298d1 | -3.3741 | -50.7616 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 316e240b-e8e2-36a1-8ded-9621a7ae0430 | -2.58214 | -54.6217 | 2026-09-12 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4716e59d-03f1-3444-ba21-ed8a4b2137bb | 1.03447 | -51.0565 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 394345c1-6ffe-35e2-a948-f154c0605c10 | -5.124 | -55.976 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63b815be-77e3-3e8b-b323-15768ca4893b | -3.36278 | -50.76336 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17fe0ab8-8a92-3863-bd5d-a9e1d3544859 | -2.94392 | -50.39849 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5fe47151-0e60-362a-8947-97cc5b09b9ba | -3.23186 | -46.96198 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 204ebef1-56d6-36dd-be70-9c21fd3dfddc | -2.72977 | -57.63391 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| dd4a6139-9b9a-3d41-bbd2-e44a550a78f5 | -3.81012 | -59.32248 | 2026-09-12 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a6c4f7b-2c06-3b9d-9fb0-e664b18eaff1 | -2.96487 | -50.40897 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0b59a8fb-00d6-3a5c-89f2-70156f86e07e | -2.91194 | -54.11522 | 2026-09-12 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd865da4-4ca9-31d2-b09f-0ff4211a4c8c | -2.93915 | -50.39263 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595b295e-c449-3bb4-a044-6bc63184a5a8 | -3.07254 | -51.33817 | 2026-09-12 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d403e80a-b63f-37e0-86ae-48db0a22cb66 | -4.35854 | -54.77804 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a517e0a-bb75-3728-b649-df96723e7368 | -2.73205 | -57.64206 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 301c4813-dbbb-31ac-8c5e-51fcd772c597 | -2.9441 | -50.39702 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 47aabf91-4443-318e-a280-be0a32d7cf4e | -6.51985 | -47.61488 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 882b8019-a190-32b2-a245-7c38f31aa79c | -6.50789 | -47.59972 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e1bc137-b843-3dfa-be92-22b00c5bb651 | 1.23098 | -50.72213 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1527037-e023-3679-8883-7045dd851aaa | -2.74196 | -57.62408 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb2ab61-e223-34f6-8a7f-bdbbd64f6076 | -2.95936 | -50.40817 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 04b9be8e-0a21-386e-8d7d-0c173dac5b74 | -4.82661 | -55.76749 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6555544b-1b65-33ec-a0cf-528f800f4c4c | -3.15932 | -58.64783 | 2026-09-12 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44303b12-d780-39a2-9000-e5c2a6f098ec | -2.72223 | -57.63665 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dce5544f-9e8d-36cf-baa8-25b69d81ee10 | -4.82706 | -55.76601 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bad39ace-e1cd-3191-be2f-45ff0bf24b36 | -4.81919 | -55.76485 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98420a89-e9ba-39e9-ba04-5ae71f05a025 | -4.30261 | -49.11632 | 2026-09-12 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1731da11-5313-3ef0-b788-8c71bbbb9f15 | 1.23213 | -50.7607 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89c115dd-8e90-3746-9b91-2b9dc1f93747 | -2.94334 | -50.47839 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a3715b-cc9e-3d71-b680-d10c5ec44b33 | -4.81842 | -55.76981 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README46.md)
