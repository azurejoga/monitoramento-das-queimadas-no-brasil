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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0952d8be-8aa7-3f52-bdde-c25703177337 | -13.09563 | -52.28949 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c54a701-896a-39fa-bf41-042d0b2a7756 | -8.11255 | -45.90004 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf9c6cc8-ffb7-3c44-8290-b0851ee1a584 | -11.37564 | -55.11418 | 2025-06-13 04:10:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df1db46-549e-3457-b38a-09cecfabae0d | -7.20212 | -45.35161 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 442bfe88-0b9f-30ee-813d-b1673cd2b6a7 | -11.57797 | -44.84977 | 2025-06-13 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0c17658-71b9-364f-89e0-9889fbe8abed | -13.09536 | -52.28458 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bae1fcd-1438-337d-896d-d5df1efd35ca | -7.45797 | -45.51544 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a96954b9-7795-334a-b46c-98ba7b121d5d | -10.86059 | -54.30331 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb56f9d3-9360-30d3-8e65-8af9c63c3a95 | -10.93177 | -56.84377 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 027bfd60-5bf1-3837-8c03-51fbc9ffee89 | -11.74603 | -54.71787 | 2025-06-13 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fe02fd4-756e-3229-85ef-c9ae62d8f87c | -10.65485 | -44.49156 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea761aa-97bb-3a9d-910a-16e52ac75824 | -9.67044 | -48.76838 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ce23fc7-455a-3030-ba20-ab02cd903f55 | -7.6994 | -45.78207 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc69cd1c-37d2-3309-8663-a83154584944 | -10.35313 | -51.98998 | 2025-06-13 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a12f4256-43bc-34a3-885c-9007420def94 | -10.92252 | -56.84214 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4880eee3-f89b-3d0c-af96-ac3e2203b47c | -9.88171 | -46.27897 | 2025-06-13 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acc006f6-dd90-398b-bcdf-57bcf8f67386 | -9.40763 | -48.42145 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b102ddb5-0532-3a0e-9197-5eccdd79b2d3 | -13.45511 | -48.21735 | 2025-06-13 04:10:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dc0e187-b6e6-341c-90d4-03872ab81a69 | -10.23188 | -52.23709 | 2025-06-13 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83f28794-1a54-3cef-a399-b7e77c22322d | -11.12422 | -53.95511 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51183141-1dc9-3d09-89b8-37c27da5cf68 | -9.40041 | -48.41166 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c29f75d-959d-3dad-aec7-4e4b7ea2b8a3 | -7.45423 | -45.51484 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33650447-ce74-35d7-b41b-24593fddd0c6 | -8.81118 | -45.09762 | 2025-06-13 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d4293a3-6ce9-376f-949a-b483527b0ea5 | -11.56832 | -54.56979 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a89fee03-3946-376c-bf7c-3a0caa430da3 | -11.57661 | -54.57486 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c0a6b865-f5db-3149-884f-5c4effc38644 | -13.09101 | -52.28507 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4defe8f4-997e-3fcb-b279-f15c751f19ae | -9.84253 | -44.71097 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20b8a0af-041b-33d2-98ad-6db62ac0f6be | -13.22871 | -47.20305 | 2025-06-13 04:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a7ddd06-8ee7-3d42-8b47-8b9f8338a16d | -13.0947 | -52.28791 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4661683-104f-325e-bdf2-f1a1fc912f36 | -12.00032 | -45.13294 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| de4ae8c0-aa15-3b80-96ba-5c2e6b765edc | -10.18644 | -49.50294 | 2025-06-13 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f0be382-59b4-3e91-bd2f-30954125c277 | -12.12947 | -54.6714 | 2025-06-13 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47eb1e8e-f72b-3071-961d-dcb4b70b51c7 | -11.57453 | -54.57117 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08c459bc-6494-3fe5-8652-b8a8771f70a0 | -10.70057 | -49.49532 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b9b2bf6b-adda-3875-9878-e013ab06c093 | -10.18271 | -49.49729 | 2025-06-13 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc57b50a-ef46-3f75-9bbf-033e0236d61a | -9.39819 | -48.42409 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5eea4b0-3dd9-343b-a7e4-e20e876b56ed | -9.40689 | -48.42562 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5550861-ebfe-3c44-96ff-bd9c4eee0488 | -12.00169 | -45.1322 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1dde1b41-6da4-3581-a807-16a54a278d19 | -11.57349 | -54.57623 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa384182-b948-30c2-97ee-93c3d7bef979 | -10.86584 | -54.30944 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f99bc01c-2da9-36d9-8aa5-6c905af079da | -11.78296 | -47.32333 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59279d17-ca27-3e9b-89a5-b201e586267b | -8.07317 | -43.11095 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 2e731c23-19ed-3a9d-8fbb-1c0826d8cfe2 | -11.17473 | -46.8783 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 58824ae6-1a0c-34e1-af82-dbc4fa7047a8 | -10.91838 | -56.82578 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53945021-f64c-33d5-8cd6-677f8d26c364 | -11.56108 | -54.57342 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6f5cc906-1106-3c14-9e1d-55bb6fe7c2ea | -10.64859 | -44.48664 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 7723c06e-2772-3e8f-b760-f6af23100655 | -10.64577 | -44.48231 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5ff3f8d-9fa8-349d-8c53-849584409aba | -10.60141 | -52.83043 | 2025-06-13 04:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34735f86-9ffa-3ed5-a159-c088dd4b1c00 | -9.3931 | -48.42754 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 206c1a1f-3732-390c-9618-1be45deb602a | -9.36115 | -40.42051 | 2025-06-13 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e3956f20-34c3-3db8-b371-25ec2dbdcd4e | -10.69853 | -49.50293 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b261b744-2951-388f-bc29-0bb5e8b5625a | -10.64234 | -49.42614 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d9fdb951-e384-3e98-920b-bd045e212cf7 | -9.88548 | -46.27963 | 2025-06-13 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 391c60b9-de82-3530-aeac-86b83be5d436 | -8.08326 | -43.1126 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bc83d718-ecc7-32ec-b1d2-c69f24a06282 | -9.11991 | -46.92872 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66569113-d96c-3553-b7cd-4c2f3287fafe | -12.86222 | -44.49837 | 2025-06-13 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dad8ad64-080a-3d78-85c6-a86d18fb3752 | -11.13807 | -53.94863 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 469b3772-f42d-3d4f-80a2-1b4fb390ac1c | -6.73778 | -47.4225 | 2025-06-13 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3275d7e3-a18a-3a69-988b-5c0a723cabd1 | -9.39385 | -48.42332 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efd67669-3a01-3ab3-b9d7-552a3d26fc2e | -9.12292 | -46.93486 | 2025-06-13 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15617108-a577-3140-8a6b-cec7687dfe6f | -10.7334 | -47.61042 | 2025-06-13 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0b75cb2-3258-3a41-ae22-de1cda4d7086 | -11.12511 | -53.95059 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7048f221-acb5-3c79-a827-8a327ecbb8bf | -8.07875 | -43.1192 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 51615212-a56e-3e8d-8bfc-8518e037b838 | -12.76781 | -44.41095 | 2025-06-13 04:10:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3689c1e8-cf0b-357f-909f-67d2ea06cc73 | -10.86153 | -54.29848 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c9a5ac3-31e1-32b2-a250-d9c2ec7757e9 | -7.4505 | -45.51423 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5909c4bd-0da0-39bb-b0d9-0fbe497f5a47 | -7.46096 | -45.52054 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 569a78ad-dd2a-3e9f-b5ba-7773bf701a84 | -7.72785 | -46.61523 | 2025-06-13 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 730fc087-d030-344b-bc51-b49358eaa22f | -8.07596 | -43.11508 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| fbe73b21-b7f4-3dfa-ab79-995984149913 | -10.65265 | -44.48345 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 48295255-d13e-3d1f-9093-5ab63f63dc79 | -11.20999 | -49.0059 | 2025-06-13 04:10:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 365f7d4b-e874-36b1-ab34-0429225fd14d | -9.84574 | -44.69153 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f9e8bc0-7951-3857-b8e7-043c5ec5ce0a | -10.64515 | -44.48607 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23a74e0c-fa9a-30b7-a3da-36ed0357e30d | -10.80383 | -54.04062 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd32dcec-9dd3-338a-8453-767b48e8d613 | -13.89944 | -54.64978 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23961b54-ccdd-3903-8c8d-47acf79ca9a7 | -14.84802 | -48.30903 | 2025-06-13 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 83b6eaaa-a975-3927-be64-2d4d60bfe8be | -14.03739 | -55.13511 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d2e4d2-4add-3229-9166-b49e30ce72e3 | -14.19582 | -57.40337 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 868655a5-5770-3731-a44a-c38d6284f73b | -14.19189 | -57.40879 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72ecbc3a-3663-3453-b192-d75b6a1a97a5 | -17.0463 | -48.93364 | 2025-06-13 04:12:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a27f0ce9-0b55-36c5-a7e9-1fe021fbfd49 | -15.3694 | -47.86543 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee4e31e2-0a96-3933-a6f9-c6042d2ce01e | -14.19443 | -57.40979 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bad49982-9a40-3f8a-8635-f62db1ebc2db | -14.03841 | -55.13036 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0196a428-526b-393e-8043-01617c111649 | -13.35598 | -52.28049 | 2025-06-13 04:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3733f213-d045-3b6a-8bb8-cb24a3c38ce4 | -13.89538 | -54.63229 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29d9d27b-30ca-39f0-ab65-d290db367057 | -18.3793 | -44.50816 | 2025-06-13 04:12:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f111394-e598-33a6-9eb8-90aff4d6e2e9 | -14.20281 | -57.40497 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da4e91d7-f9b2-3e63-b869-2323be9b1670 | -15.38768 | -47.87339 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2a3fe4-faf6-3aaf-9c21-8247b940c979 | -13.89442 | -54.63694 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05e0f62a-e9ff-321b-a599-500b4ac1a473 | -15.36218 | -47.88389 | 2025-06-13 04:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf0422c-253e-37ea-a226-455cf6374451 | -13.89631 | -54.62773 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 907d7fd8-e305-310c-9dee-3bb2ebb53402 | -13.90133 | -54.6338 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 81d37eb2-8767-320d-b846-297a85818a46 | -12.5228 | -57.23507 | 2025-06-13 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01a58d3-1419-3e3c-83ec-6e8e705cd1d7 | -17.37547 | -53.82107 | 2025-06-13 04:12:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74731640-8de3-394f-9e88-3a6d33b58b04 | -13.90039 | -54.64528 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28777095-098c-3db8-a83b-33c50434abd6 | -15.56815 | -47.85719 | 2025-06-13 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac9636e7-af27-3221-94a0-9218b435fd15 | -17.65271 | -47.45686 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a858b457-bcad-3e20-a0a4-ef2b2edd91aa | -14.03328 | -55.12415 | 2025-06-13 04:12:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2036aaac-391c-39bf-bab0-6018969f9fca | -17.66429 | -47.45464 | 2025-06-13 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60437cbc-3bbe-35aa-9e5e-ac8655f082f9 | -13.88843 | -54.63559 | 2025-06-13 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README12.md)
