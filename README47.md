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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b53d398-fb68-32d0-969a-49a44bdc1cda | -2.43352 | -48.96324 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1df4623-99fa-3c64-a308-297e3ab5a8b9 | -2.43298 | -48.96677 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6092db21-cdd1-3c93-8bf2-a0dfb05b3ac8 | -2.43243 | -48.9703 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3401f30c-6131-31df-b98d-4e125ab69cd5 | -2.42785 | -49.08846 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 523cc757-805c-3765-a121-291457699b9c | -2.4273 | -48.93697 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9be37329-b865-35aa-b0dc-c8b58146705c | -2.42395 | -48.93646 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc33096-d677-3658-9af6-8f70d2588d8b | -2.41834 | -48.92836 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2718d776-7982-347d-9cca-64041fdaf149 | -2.40676 | -49.0924 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a243d0de-bf3a-3d41-a850-7e29135173ec | -2.39138 | -48.9749 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3551f0b0-152c-31c3-9ccf-5fc625db69f3 | -2.3762 | -49.13792 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a159b8-07b4-3ecc-ad32-2bc86e644b2b | -2.37565 | -49.14143 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec263289-86c0-3555-9cf5-9c4ef6ebfea6 | -2.82869 | -49.31138 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83ec1efa-33dc-3b86-924c-bd9fb537e907 | -2.82644 | -49.30389 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b98f51e-10dc-3ece-a146-37813050498f | -2.8259 | -49.30738 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 631398bb-59aa-35c1-a699-eb69468a0168 | -2.82429 | -49.31785 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2151db7f-474b-34cb-bb1c-4fa32db4698b | -2.82312 | -49.30338 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c9fb790-3acb-325d-bedd-1be987e2e55a | -2.82096 | -49.31734 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac9488f-7dde-3dff-a2f4-99d661e983b4 | -2.81979 | -49.30286 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7999b185-3f23-3ba1-8176-5e7c0991527e | -2.81807 | -49.42387 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56524255-9eb6-381c-bb2c-f739471e367c | -2.81655 | -49.3238 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96698073-08bf-3967-943d-d35f327d8edc | -2.81475 | -49.42337 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d4cb801-612b-39a9-982b-32b92e4f2ad6 | -2.81215 | -49.33027 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1e1e635-8653-3844-bf42-1a823b9da675 | -2.80882 | -49.32976 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 517cfe2b-f838-31af-becb-7508960f1674 | -2.80838 | -49.35468 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 084f642f-30aa-31a3-9131-3d97b6eab0a2 | -2.80496 | -49.33274 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31f49f6b-78a1-3de3-b095-8906c13d81e1 | -2.80442 | -49.33622 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9390fa0-756f-395e-aaf9-ccfab04ddc68 | -2.80388 | -49.33971 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8b49438-fda5-3976-95c7-a010a64970e3 | -2.80227 | -49.35017 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 142bdafe-0960-3f96-8abc-7dcf5407b024 | -2.8011 | -49.33571 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b938ae8-9daf-318a-94af-219bfbe2c27d | -2.80056 | -49.3392 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324c523c-5178-3388-be0b-f9fad8a1c86c | -2.80002 | -49.34269 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b13f958-f965-33e6-a57b-895a29912207 | -2.79616 | -49.34566 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02b1cafe-9a16-3578-aa7f-a12d3b1ee627 | -2.79009 | -49.47292 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f961c0-0191-382b-a6e1-343f310e4d4f | -2.78939 | -49.2588 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e57bbba3-7dd8-3d60-93be-43d0a39fec24 | -2.78677 | -49.4724 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8025bb-f015-39d9-b048-45a059f4b15b | -2.78292 | -49.47536 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 863874d7-46d3-36cc-a715-0b187e36a382 | -2.76502 | -49.43696 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5be808a6-7294-32b3-ad60-fe907f430e5b | -2.76418 | -49.17965 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd74812-c889-3c2c-8668-c6213386e8c5 | -2.76364 | -49.18316 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6f4d922-fd20-3213-98d0-34fc63f2248a | -2.76194 | -49.17212 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 567306d5-d4b1-39bd-808a-c95cc6be3fa0 | -2.76139 | -49.17563 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3119dafb-4ec7-34ae-b217-eea4105281b1 | -2.76085 | -49.17913 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15389b37-f0e1-37d5-ba48-b29a2c7ef7da | -2.76031 | -49.18264 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae931e4-b37c-37f9-9b05-2b9c65b9bbf9 | -2.7586 | -49.17161 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42e99dda-5afa-37c0-9804-1c900e57173c | -2.75806 | -49.17511 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a226780a-83d7-3309-93cd-dc0eeaee6ff8 | -2.75473 | -49.1746 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 773e06a4-4a36-39de-b1c0-9e91f79b26d0 | -2.74906 | -49.29909 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81faccfd-32be-3a3d-84a3-139d8e5e6991 | -2.72697 | -49.17752 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c47f67ac-bf52-3047-bd84-88670baff9ab | -2.71983 | -49.33387 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5e4d1976-d046-3b25-8af5-af3d12ad4ee6 | -2.71759 | -49.32639 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 75dc7c01-c651-3105-b906-a79e3eb5a144 | -2.71687 | -49.28699 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44a33b9a-80da-3a1d-b04c-3c0db9e786b5 | -2.71651 | -49.33335 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ea7a0c57-682f-33ae-aa66-4ec8769060d4 | -2.71426 | -49.32587 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fc42406-e0d6-353a-983c-fd008df1bb5d | -2.71319 | -49.33284 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b400a34-e7c8-33ea-a5b6-b222efdc7bc1 | -2.71193 | -49.29696 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a8535c2-e4ce-3230-be6b-48bd69f304b8 | -2.71094 | -49.32537 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b8ba3604-3c15-36b7-862e-d97bc02e2b78 | -2.70986 | -49.33233 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a91352-7857-3fde-b74d-e4682fd97bfe | -2.70914 | -49.29296 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5582969c-92f8-321b-9840-d49f90b982ab | -2.70582 | -49.29244 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10b6a57f-ee1f-3452-bb08-066f7877ed2e | -2.70303 | -49.28844 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ca2e50c-187b-3e20-a13e-78efb55dad5b | -2.68659 | -49.32876 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b91102f-3f6e-3b7f-8318-d3ceba0ed1c4 | -2.88675 | -49.26664 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76f2224f-7bcd-30b1-b3b6-42ca2eb96a57 | -2.88621 | -49.27013 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcb40a5b-4f4b-3b61-a5c6-327f7c5bb834 | -2.88499 | -49.23411 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a10de9b-9748-31f2-8200-586bf599bf20 | -2.88396 | -49.26263 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d9036a2-d32a-3987-842a-c11a84de1708 | -2.88342 | -49.26612 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 982daac1-13f9-36ae-b4c3-5c9cdb7fe85f | -2.88288 | -49.26962 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4147e86c-feaa-3e63-a556-788aac9340b5 | -2.88166 | -49.2336 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 323ccb65-f5ce-39fb-8eb1-c12745780968 | -2.88063 | -49.26212 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f99e04f5-85e6-3345-aed2-dd18d505fa48 | -2.87955 | -49.26911 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b597b0ab-e15d-3068-bb12-b79d2d030a4f | -2.879 | -49.27261 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f53ef38-6bec-3e49-9969-2841cda05a83 | -2.87833 | -49.23308 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54cce34-358a-3ad5-aeee-a5348a7968f3 | -2.87778 | -49.23659 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88465ca5-5380-371a-a46f-f78d8b2c8f2f | -2.87676 | -49.2651 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a0f88f2-0a25-3f2b-b1d4-a38afecd6537 | -2.87567 | -49.2721 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd75f8c-e4d2-3b13-848e-bc6c540216d3 | -2.87499 | -49.23257 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f75c4c20-9376-3dc4-b9df-840be5c34bc5 | -2.87289 | -49.26809 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0a6ed10-288f-3ddc-a59b-b7952d210920 | -2.87166 | -49.23206 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0ac0db9-07bb-304c-9e42-76e2d00f031b | -2.8701 | -49.26408 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 011141ed-b032-3da6-87cc-9ec73d745108 | -2.86833 | -49.23154 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7d23121-fceb-3230-9ad4-7e0f9474e2a2 | -2.86677 | -49.26357 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ae15f1f-437b-34f0-92aa-0f1478c50a5c | -2.865 | -49.23103 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17076748-2e83-3d4a-a21e-0dd847c92421 | -2.86167 | -49.23052 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b858673-ce78-3c87-9c69-d49c643d8e8c | -2.85833 | -49.23001 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8057a8-44a7-326d-8bba-ef1b16aba6d4 | -2.85779 | -49.23351 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a07264e-3196-379c-91d5-1e110ab7c225 | -2.85624 | -49.26553 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cc850d6-ab85-3320-a80c-7d2277f64b28 | -2.85291 | -49.26502 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6b2f3f-ca35-35b9-818d-a755d643ae0c | -2.84958 | -49.2645 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36036738-de9c-3b87-92e6-658afd3da8f5 | -2.84904 | -49.268 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56e68d84-87d5-3c91-b101-b299fc24fbb1 | -2.84517 | -49.27099 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcea4c95-41b5-398c-9266-46e5f3e0eddb | -2.83464 | -49.27295 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd49aa9-cb4e-3695-9634-5cab1fa1bd35 | -3.33288 | -50.27041 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b7f404c-5908-3dfd-b7dd-12b9fab96090 | -3.33181 | -50.27726 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4646d954-b31f-373d-bd32-d5eda797b8db | -3.32958 | -50.2699 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32384fe2-4941-31f9-a350-1c0aebd2d3d8 | -3.32521 | -50.27625 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 244c93dd-7196-3cbf-bc2a-c97c51691525 | -3.32468 | -50.27968 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bfa84c4-9400-3f1d-9361-d43dac3ae8ba | -3.2749 | -50.35614 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e726c67-2e64-3399-838b-5319ff828b68 | -3.27437 | -50.35957 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8e0a62d-2a29-34e1-b9c3-2b01b73dd228 | -3.27428 | -50.33849 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0b8a493-4ea7-3077-8b27-b2536fbe2d9d | -3.2716 | -50.35563 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README48.md)
