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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecc46918-d5da-3f26-af81-64bd8ab733f7 | -6.7129 | -59.13333 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e136590-702d-33c0-b10c-8f32888593e5 | -8.57374 | -55.27619 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed27ed3c-e8ac-31da-b605-66382e5f2b0f | -6.28052 | -53.36454 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bb749c8-be6e-3c97-aa92-06cfd2734439 | -2.852 | -50.46602 | 2026-08-26 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8efaa47-f740-3bce-bcfc-538d4e253761 | -7.26238 | -49.85407 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d64542ef-99bc-3c8c-8a68-936b088eb686 | -7.45809 | -46.01833 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a09b1ca4-c84b-317d-a0f4-4bdb12f71436 | -7.86138 | -46.11414 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2cd84a14-d17c-3d1f-bc70-6cb636b18f5d | -7.29226 | -43.02688 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b169116f-43f2-3f2f-aa76-1dc355e89d5c | -6.32582 | -54.75582 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dbd6449-a436-30b8-b7a5-ee036af01e71 | -8.01586 | -51.80405 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d46911e-7657-3680-a046-db50af389989 | -6.60303 | -56.37152 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e81fa3-b4bf-369b-a5b0-b5e883b509c2 | -8.17898 | -54.96025 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85ca5d1d-f5e8-3fc8-a6b8-70ebae139474 | -6.80165 | -59.59504 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f682a7da-78d6-35ff-8da0-c92f9be41ccd | -6.17173 | -53.49406 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2583527-53cb-3415-ade6-f343fbe3cb60 | -9.4623 | -50.30748 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3506587b-cd2e-3ae9-9e4f-d2d395428e9d | -6.12395 | -57.81923 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87929fac-93ef-38f0-ba8c-1975f9809702 | -6.99086 | -59.28208 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9442d985-2b6e-3487-b187-8b87b9a15413 | -6.73202 | -59.669 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caee2c22-8ecf-325c-831c-9021bdfb8a8e | -6.33566 | -54.73819 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d03d5ddd-c15f-34be-b897-43c03a7da92a | -6.83771 | -52.49838 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3413bb5-6923-307f-a3ee-27a62cda0241 | -6.94048 | -52.77716 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a1bd425-ec4c-3c13-a48d-61c5230143cf | -2.79077 | -49.5245 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb558499-62f7-3d2c-b180-e12e43a35524 | -6.87036 | -59.40734 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89498f9f-10ca-3e17-81a6-846ae7a6b88c | -9.56637 | -49.26095 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c77fd0a0-c54a-3213-94dc-7287611132fe | -6.14449 | -59.91499 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bd0f815-6fa8-3b92-adfc-4a37c1b04e65 | -6.64215 | -58.51463 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a8fd7f0-1ea4-3835-9705-7f8071261d41 | -9.71455 | -49.33002 | 2026-08-26 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed4e9532-d2e3-389d-9b77-66b3932d8bc2 | -7.03612 | -59.22768 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a3e1e6a-3a84-3493-a7af-70807ba7583e | -9.41709 | -51.65503 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 613fc0cb-3e29-34ad-ab6e-6fdaf1004f42 | -8.54533 | -55.30231 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89cb254f-144e-3578-9c07-a716e6dee9ec | -7.28235 | -44.08002 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08c36901-4ded-3731-a304-e0320a16277f | -8.01416 | -51.79277 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6237e1-50ae-3337-a9d5-6f754433d5a6 | -6.89161 | -59.40915 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b304bf4a-1544-373a-a065-e7ef651c5082 | -6.88333 | -43.75024 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a76bb2df-b674-3a9a-ab91-5cd518c544bc | -5.81241 | -57.63238 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d713d016-7ca3-3f09-a421-a6e7ba1c44c1 | -10.0226 | -46.42456 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fedb850-c289-3870-a63e-1ad0e3de5927 | -9.02363 | -50.78083 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ba5a740-4803-3d19-a1bd-461224278fdc | -8.16753 | -46.20235 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 885a77b5-b21e-3895-87e5-3125cbc1d695 | -6.69094 | -58.71783 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf17a958-02fb-3f46-8cbf-fa0ad1997a4a | -6.98938 | -59.26399 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa0cdb11-123b-301a-9242-a76a68dc7ecf | -6.69159 | -58.71386 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6684b934-c188-3d1d-8cba-37da328dc64e | -6.275 | -53.37795 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf2757b8-ec72-316c-8070-4cd227f7dc94 | -3.49837 | -57.02089 | 2026-08-26 04:51:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4fe4af8-75f0-3eff-9db8-f8924ff833c8 | -6.42354 | -54.93712 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a01f30b8-f331-3222-b37a-738eacfc61bf | -6.33103 | -54.74514 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2763e24a-4fb7-3f8e-b619-827ad0c049e9 | -8.64903 | -50.33507 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adb3daec-d505-3aa9-a0db-e51ca509adb2 | -7.38379 | -55.18417 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdd626d1-445a-3a4e-85ee-c37c2153d02d | -7.03577 | -59.23064 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c86066dc-f65f-3988-af1e-b413fb96f74b | -8.00803 | -51.81026 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee05284d-2a90-369e-8b31-9c18d3d4e9b3 | -6.82299 | -58.6521 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cd879a5-d6d5-3456-897f-9b28b9906a0b | -7.5418 | -61.3611 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cbf7d80-739b-3f99-a552-3706d3124dca | -6.64899 | -58.49978 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f19165af-addf-36ba-9e6a-e3a9eaf75651 | -6.69428 | -58.71774 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8faccea0-847d-3748-a92c-e079ad6bbb7b | -3.10067 | -53.16862 | 2026-08-26 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c0ca587-a560-3fbd-8d6d-c56dcb07bde7 | -6.14974 | -59.92837 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01328657-f8a9-3ded-aa47-4e5ffc5580c1 | -9.1698 | -49.97854 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1d922a6-4d58-3d71-ad82-8b2e5fa0618a | -9.44883 | -51.67522 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71f6c49c-36e1-3bb4-81db-865b146ddeb6 | -8.56748 | -54.81496 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfedd537-67e6-3021-b693-ecbd8a68b5db | -6.77011 | -59.44113 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf7ffed-cef7-3f21-82aa-dcf0a18e3448 | -6.14534 | -57.841 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc4a922-0196-3a0a-aed8-e12ed3c90b17 | -6.62473 | -53.18779 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 671895c2-fdba-3e0c-a76a-13b568177a56 | -3.54019 | -48.18429 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a7101f6a-e2da-3048-9213-226e81147962 | -7.25948 | -49.84878 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c42b85e-4144-3862-a39f-25d9008b8827 | -6.26473 | -55.41257 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 863de3e3-090d-3e34-a9a9-c37e3e9d0477 | -6.82778 | -52.49686 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 352a0455-c302-37fe-b39e-17800b29e7a7 | -4.10707 | -50.99018 | 2026-08-26 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16941f3e-130c-3bee-8a9a-f3893a599240 | -6.10938 | -53.84516 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d613c8e6-1207-32e3-9850-9fd89163a898 | -8.94822 | -50.70887 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16d1c2b4-de74-381d-b74f-3fbf6342fd78 | -6.30179 | -53.57547 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52145d3d-df79-33d8-bc9a-25c78c43c72c | -6.999 | -59.31454 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b623962b-8160-38b3-8ad1-9de9c534dcb7 | -3.09229 | -61.19719 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afd887a9-2df0-39fe-aea3-31e5b2969e67 | -6.30955 | -53.5695 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a664f1-72fa-3bcd-8b23-b4e8eb342f08 | -7.54127 | -61.36408 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51e06068-fdb3-3f98-9367-d3c502662021 | -3.09709 | -61.20144 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59fe90ee-85f2-3286-b86b-0d29a47e9900 | -7.16337 | -42.80367 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0fbc80e0-aaeb-32b9-a24d-a79f2d1ef729 | -6.51698 | -55.22291 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25676749-158c-3f67-b822-a7700267c952 | -6.28162 | -53.35757 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2769b685-75f3-3612-b11d-8671feae30ad | -7.47189 | -61.3792 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd2d485-eef1-31a2-b712-c0e548bb9261 | -6.9444 | -52.79548 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5d50715-277a-31cb-8700-d7156a253c4e | -5.77917 | -57.55033 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 987a3e02-0de7-38a8-a6f5-935316cb3286 | -7.29793 | -44.08802 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e672b73-e44d-3086-ba44-0493538dde71 | -6.6164 | -58.37908 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5fb14957-a69a-3f68-bb98-8752bbd4a9d3 | -9.01788 | -50.77142 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d848bd0-b4ef-3b59-9cd1-90e45541834d | -10.33536 | -48.21688 | 2026-08-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa3c718-92b5-30b9-ab80-799519298e09 | -7.07161 | -59.23219 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5c5daa91-5378-3352-89e3-37302dc14b2c | -8.03128 | -51.80687 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715f23b4-64ef-35c8-8d7e-f584dfdab32e | -6.09542 | -53.3955 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b383b27d-b831-373f-a219-b2f7ce00d9fa | -6.75567 | -51.131 | 2026-08-26 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a0b18e-3be5-379c-ab8d-32f740c4b94a | -6.25619 | -53.36788 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c7128a-64d3-302c-8753-0998642ff0d8 | -9.41362 | -51.63195 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ca14f5c-c655-3677-a869-7aec5f802aab | -8.60506 | -54.86224 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe840cae-b62c-330c-aaf8-d7810862d600 | -5.95675 | -53.58533 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c34d78b-425d-3fc5-9a1d-1c19f27db2ce | -6.63506 | -58.50547 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f5aad13-1b8b-3670-8a49-4f0a63038dc1 | -7.28157 | -59.62276 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1804bf8b-4663-3f6e-ab8f-7e0e2977cd3b | -8.57595 | -55.28427 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ff6edd0-8fdd-3135-8174-8c0bd982871e | -6.26782 | -53.38039 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63b3aad2-eef2-3b18-af23-c2ad195859f1 | -6.772 | -59.44564 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e366518-a672-3f21-a03f-7c40a233e776 | -9.65687 | -48.31654 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a20d8b7a-5265-340d-9e02-b3920485e2f0 | -6.64059 | -58.49836 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b50e3ae-4e97-32ee-aa1f-0202ac3644c3 | -7.68597 | -50.75003 | 2026-08-26 04:51:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README39.md)
