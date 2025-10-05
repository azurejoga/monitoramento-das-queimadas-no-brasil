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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a088ef9-9d0f-398b-8f4c-2f509795e76b | -6.36935 | -47.92905 | 2025-10-05 04:46:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6096343b-3e2e-3ff3-a7fc-65347a495c24 | -13.26695 | -47.6107 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95e397fa-ad0c-3b01-9946-0efc0ce5fb08 | -13.30995 | -48.11948 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 267683c7-2708-340d-9eda-8f278e6ba67b | -11.07151 | -47.90766 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfc13406-a02d-32cd-b22f-da0dd988ca5f | -13.25122 | -47.23307 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3861974c-bbeb-3409-bae5-3f75bc7784f4 | -8.62241 | -50.01768 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5b54c47-659f-368b-bd49-a44fb22b1755 | -12.38394 | -44.45079 | 2025-10-05 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3b57645-8edc-3d8d-8d08-95cf0855d261 | -6.43125 | -46.02407 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6037d5d-1d54-3a70-950f-276633a28652 | -8.53725 | -47.6895 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83d72a02-954c-3c9c-9cba-53b77f270c8c | -13.34787 | -47.19318 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 355146f7-8a53-3467-a4eb-25908620f75f | -10.99806 | -57.04595 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 550a081f-ca05-3f6f-9ca9-c1aba251f82e | -13.26036 | -47.22733 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6711e2d7-d892-331a-8252-1919d1832bd0 | -13.24572 | -48.47376 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48b8ee50-442b-3df5-812b-949880a5bb2a | -13.2959 | -47.81431 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2d5ebd5-cea1-3679-bfb5-f126293fc89d | -8.58489 | -46.33091 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 449df6a1-b1e5-3334-84c5-61f03515c9b0 | -12.94047 | -46.36847 | 2025-10-05 04:46:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d4fa92-5927-38e4-9561-715e5c85a553 | -5.60819 | -51.80809 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca037db3-d8c8-321b-b5ed-00059f34e3a3 | -10.39106 | -45.39748 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff67ddb4-dce8-3b79-84a2-6bba70301635 | -11.81573 | -45.07433 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3764007-bc0e-3a42-a6d2-002eb31740b3 | -13.096 | -47.8382 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e745324b-c45a-3efd-ab03-f108747eb07b | -10.01552 | -45.51387 | 2025-10-05 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e61632d0-08ef-3b75-ac61-d7cd7f442209 | -8.33713 | -49.49546 | 2025-10-05 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e9fa4895-f968-3771-8411-99b39253fafa | -8.58901 | -46.30169 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 373e0865-c4d3-3bcf-9e80-229238788d95 | -10.63099 | -49.16363 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecae5a8d-3afd-3090-a8bf-d3b4c19b2737 | -10.11094 | -55.96447 | 2025-10-05 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dca7bbd5-aea4-3f68-b816-a000b93a6595 | -13.09864 | -47.84844 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7290b628-806d-32d4-85c8-6bc23cff762c | -11.30431 | -53.96404 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4775435a-2941-3946-b7ac-69fb7c0a2364 | -12.97312 | -51.03361 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0534c2a-f066-3019-818b-47701264f4d1 | -8.87623 | -50.88876 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d682b35e-9ed1-3088-9b66-9b116703562d | -8.6253 | -54.99676 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 213d7ba1-37eb-35a0-8582-f84966989445 | -13.27966 | -47.17809 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6548f542-43d5-3de1-be59-9ec8ee690652 | -10.99747 | -57.04942 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7629dff2-0c99-340e-b51a-150cdf27705b | -10.80281 | -48.82257 | 2025-10-05 04:46:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be3e9cef-9104-352d-8602-ab481ef4ec6d | -11.86492 | -44.95431 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42305272-0857-3668-bc29-e29408cd321a | -9.33704 | -54.52242 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab8157ea-9e4f-3e87-8eda-ce041238e7af | -11.10158 | -47.7499 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a09b378-8bd7-331d-baf5-408ea9a8d81b | -9.26724 | -51.80939 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3af10d0d-5a17-3f34-9dd3-ee5cfc998a12 | -5.54082 | -51.43769 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64e9f0cc-15c6-3610-8680-dd23a5566678 | -8.62578 | -50.0182 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a50cf63-696c-3e62-bc81-f9393466b22e | -12.24593 | -47.84987 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 64730037-7a92-35a7-88ea-e075c266470c | -10.84205 | -47.97195 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70f0503-f422-3ab5-bfba-2f1c8354fdc4 | -13.26298 | -47.60983 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ce3146db-1ac1-3ada-b1b6-de2af6e87341 | -13.08084 | -47.92188 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36eb6546-7cc5-3463-9147-55f9d5db8d8c | -11.83186 | -45.05975 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e0d40b1-3a91-35a6-a398-9c8fcd09f39c | -13.14643 | -50.92455 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07837a33-7075-3448-8e54-8af9283fc70d | -13.26296 | -47.8195 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 49bb83b9-f577-3c71-b460-b632ff9d47b9 | -13.09666 | -47.83329 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe72303d-0bf5-3041-8b3d-339a1454f40d | -13.15823 | -50.89211 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c60cf0c-d708-34b7-a47d-ee73f8d2afa1 | -12.30789 | -55.1419 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fb4f073-eec3-3c0b-80b2-e56364efdb0e | -10.23741 | -48.00468 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 523c766d-cb49-3f2a-91cf-adcfed743ad1 | -12.31151 | -55.12509 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0847e4b-dffd-3321-b7c7-982f23f5074c | -8.62523 | -50.02184 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b11c1224-3ab0-338d-a054-26566dd449fd | -10.83087 | -57.19414 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72464dcf-df90-3a5b-88b3-00b205a9f62c | -12.32215 | -55.1476 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffdbebae-6306-3f72-ad77-6ab524d23331 | -8.62603 | -54.99245 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5853c9bd-07ab-3f21-9b4a-10bb0d0a2702 | -13.08909 | -47.88995 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| da0e4fca-5456-3166-ac60-2d0cc414be35 | -7.42733 | -46.50156 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb9d72a2-ced3-39d1-85f4-038538c6e5a1 | -7.70158 | -42.87289 | 2025-10-05 04:46:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d9b15613-92e7-32df-960b-fb69146a185e | -12.23257 | -43.77245 | 2025-10-05 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d03067fe-8b43-3c72-aaa1-96e6a220c017 | -13.48589 | -47.27983 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 25dc6c30-c54e-370d-bae0-f233f344affa | -12.27056 | -55.12737 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4004f4-66e7-3cf9-a4d9-d3ce2e5568c5 | -8.26851 | -48.81349 | 2025-10-05 04:46:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 9a4db0a9-a217-3820-8080-0fc8a0f4573b | -12.30987 | -55.12983 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0fc0418-4a21-3a13-9b6c-b51c3cb96c1c | -13.35509 | -47.20189 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19083283-a0b7-355f-9e77-a9574995bdef | -10.70003 | -47.99184 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 774d4ff7-b494-3ed4-b129-b2ceb1e697ed | -9.3835 | -45.87162 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a69cf02-b447-33ed-aaa7-4f1c046780dd | -11.93122 | -46.43208 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a475bd9-54cf-39dc-8cdf-f4baea7a8d28 | -12.56277 | -48.16174 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b99f7c4-9131-3dc3-9f85-c509a388ea42 | -7.52132 | -43.85867 | 2025-10-05 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d8b7cd5-e7fc-3e16-9831-af707019718c | -13.12629 | -43.84457 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9c8daab2-124f-386d-8c46-6d0ab1c9ac65 | -11.101 | -49.85649 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c2a98d9-6ec9-3e1f-8cb0-bd68cfe2fba7 | -6.94741 | -47.04499 | 2025-10-05 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebd673aa-0540-3cff-8926-bde28b0855af | -11.80629 | -46.83719 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2c90f16-b334-3bb4-b7ef-b1d8302773b9 | -10.0358 | -62.45945 | 2025-10-05 04:46:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00d7637c-4742-317b-8a31-9ef861773903 | -13.3284 | -47.18178 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecdc2dc9-dba9-37bd-a118-52dbfc1444c8 | -12.38702 | -51.09685 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff595c32-9858-3922-90ce-3633b52bc1f2 | -13.29408 | -47.62127 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 43c13f8e-9793-3628-b2f6-3200fec637d7 | -10.3576 | -48.1712 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| b5150c11-000c-37de-91b2-2f70a48b32c7 | -6.43295 | -46.02022 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66db088c-4dd4-32b3-a33c-78e68a86d348 | -11.49357 | -46.78661 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07df1f24-3ddd-3599-82e1-482dcba10f2f | -8.58387 | -46.33813 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 97c1825a-8750-367f-a91a-7c57bc4d19ae | -7.43913 | -46.96714 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb5ae130-9130-30a8-a368-d90c354d8175 | -11.04478 | -47.79123 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee9b49bc-27a7-356c-b462-2b19e81bf7b5 | -12.13259 | -49.43081 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa525a60-7c5e-34c6-8363-948c7d57a224 | -10.04954 | -49.20419 | 2025-10-05 04:46:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2f16a6b3-13b6-33cb-9a75-1e08a3ddc8e1 | -9.27193 | -46.29566 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4752142e-ccd4-3541-8001-3bf4410c3931 | -7.79186 | -44.13554 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 117a3225-3637-3b15-8186-ce554d74d650 | -10.39798 | -45.41304 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66d55168-d98d-3272-8748-a23458d303c8 | -12.45913 | -45.51944 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be92b99d-d763-397c-9069-bdf019bfada4 | -12.30879 | -55.14113 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b918c3b5-c6fa-34e2-92a9-b3b1ce808fba | -13.14851 | -47.98089 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43329f19-32fe-33e4-a0e2-7c560f457d73 | -8.86438 | -46.84988 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56769557-8426-36ad-af8b-e2555d38d64b | -10.83673 | -57.18415 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28466231-8d44-38b1-bdf9-c7e246c48e50 | -8.41108 | -45.66151 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a92d9406-39b6-3746-b9f8-21f21baba68a | -9.27713 | -46.01606 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ff72210-8fbd-354d-9867-2bf3d375c303 | -12.59099 | -48.15582 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43318992-9686-300e-a05c-0056c44338ff | -12.31403 | -55.12643 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b29a34fd-e0d7-3573-ad62-3aafc85710b1 | -11.76155 | -44.74296 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 14d29ac2-5bb2-3a24-ad2b-5ceb3a919505 | -11.01915 | -46.69793 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99c659cd-935e-3e06-be43-11ebd5e8b40f | -9.20307 | -46.92021 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README96.md)
