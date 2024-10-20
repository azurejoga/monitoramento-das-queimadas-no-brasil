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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd3b7298-9100-33c7-87f9-5516544bbd18 | -5.3926 | -46.9007 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc12f901-dfbb-3c62-8459-c811d9b2da92 | -5.3957 | -46.9147 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed11902-27f1-3c58-8b5b-333fbc9487a2 | -5.3798 | -46.888802 | 2024-10-20 00:13:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dadda565-9eac-3eac-849f-eb4e77a4f6e5 | -5.386 | -46.916801 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2c5bb6-1a9a-3389-a4d7-eb1c508627c5 | -5.1947 | -46.0914 | 2024-10-20 00:13:55 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e152f9a5-1785-3333-8f3b-fc65cd1a93cb | -5.1974 | -46.103699 | 2024-10-20 00:13:55 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90ea6f07-0885-3c6c-a126-b738b698bcce | -5.37 | -46.8909 | 2024-10-20 00:13:55 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4f87a3e-e8b2-31cb-968a-ccab5ab43b4a | -5.3731 | -46.9049 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6540a0d3-127c-34c3-bfd9-1729cb9f0d60 | -5.3762 | -46.9189 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a21b743-c79f-3a87-bd46-c0540f3b2943 | -5.1849 | -46.093498 | 2024-10-20 00:13:55 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdd6fda4-d61e-3ffa-bf36-71674fba8a2f | -5.1876 | -46.105801 | 2024-10-20 00:13:55 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a23bcdd-e509-35ae-9d92-077bbe415918 | -5.3634 | -46.906898 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c0b34a6-19de-389f-8ff9-41f12c893033 | -5.3665 | -46.920898 | 2024-10-20 00:13:55 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9a36181-44c7-3d51-a2ea-e2882a94aa37 | -4.4428 | -42.9025 | 2024-10-20 00:13:56 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 823760e6-d1ff-3692-8df7-5c4590486f77 | -4.4312 | -42.896702 | 2024-10-20 00:13:56 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dba159a5-e84d-3017-9ca9-96f612bc4f94 | -4.433 | -42.904598 | 2024-10-20 00:13:56 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be9c61df-5baa-3b2e-9619-5a1e2fd59157 | -4.4348 | -42.912399 | 2024-10-20 00:13:56 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a13f7484-53ed-3264-ab32-cc3d4325001b | -3.8445 | -40.632301 | 2024-10-20 00:13:57 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c93c5ab2-3d2b-3760-863b-4f9c849f9b5b | -3.8461 | -40.639099 | 2024-10-20 00:13:57 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4db59550-e558-3aa6-a638-cc521566e287 | -3.8476 | -40.645901 | 2024-10-20 00:13:57 | METOP-C | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3b77fe83-4c32-3be9-8a66-ea15c9d63ba1 | -4.393 | -43.046299 | 2024-10-20 00:13:57 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83a02864-fa0a-3b3c-a100-e7854ddff892 | -4.3832 | -43.0485 | 2024-10-20 00:13:57 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b11c004-30cd-34c4-a5f9-e37ce5aed4be | -4.385 | -43.056499 | 2024-10-20 00:13:57 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c5911be-03ed-39d0-a883-69e875830fe3 | -5.1166 | -46.1082 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 045f1f79-7a50-3dd5-b304-31099b586402 | -5.1193 | -46.120499 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 533df418-3d5a-31d4-986f-1dc7a506113d | -5.1068 | -46.110298 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d72e465e-94ce-33c2-b4a6-af58b0680022 | -5.1095 | -46.122601 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a10e4c38-d262-3b1b-8529-592c34fbc89c | -5.1051 | -46.149399 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9c674a-c5ab-36bb-932c-14a46ad27dc8 | -5.1079 | -46.161701 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c30d56dd-b98f-3772-8fd6-20df455811f0 | -5.0953 | -46.151501 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b37632f2-06cc-3172-a813-06acc7e1571f | -5.0981 | -46.163799 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5de4840f-a150-3566-b7f1-fc8fd9fe3e2f | -5.0677 | -46.118698 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e646ee4-d4e0-38bb-8b83-be1db5318c57 | -5.0704 | -46.131001 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3407f73e-3f7e-397e-95fa-8871ec52d437 | -5.0731 | -46.143299 | 2024-10-20 00:13:57 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bad0278-5250-3103-b5f3-34172c06c47c | -3.8577 | -40.9604 | 2024-10-20 00:13:58 | METOP-C | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a5ccf27c-66d3-3a28-a2d4-a0016ec6488c | -4.5616 | -43.979801 | 2024-10-20 00:13:58 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2c2a988-eb1e-3038-b6cb-36f23ffb704c | -4.5636 | -43.988701 | 2024-10-20 00:13:58 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f9df9e0-75d1-3af2-b40c-75bc978c34c2 | -4.5538 | -43.990799 | 2024-10-20 00:13:58 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4d47f3d-6559-3bab-b04b-5d34882c6ea1 | -4.8889 | -45.818699 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e162e8d-1747-3599-a7de-a295030990d3 | -4.8915 | -45.830399 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4f7cc2e-18df-34fa-a3db-351098428794 | -4.8941 | -45.842098 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23b5eb4e-f037-368c-821f-9b72a2eff53a | -4.8766 | -45.8092 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5122d7ea-64c9-3309-b624-2d34433d18cd | -4.8792 | -45.8209 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 333f26fe-3337-34b3-8f47-6f4b984660e8 | -4.8817 | -45.8325 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62d23eab-9776-32fd-9fb8-45696adaba9e | -4.8843 | -45.8442 | 2024-10-20 00:13:59 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3a58d2d-9686-3276-ba76-ee29f546e131 | -4.8694 | -45.823002 | 2024-10-20 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08677bb3-6233-347a-b523-8e2e1fad327d | -4.8719 | -45.834599 | 2024-10-20 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1c85ac-07f1-3239-b36b-af6e4a676d46 | -4.712 | -45.205601 | 2024-10-20 00:14:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f08a94b9-d699-3682-ba2d-179fdcbb0ff0 | -4.8478 | -45.8643 | 2024-10-20 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce839a0c-6f79-3de1-b9e7-cfb9dc5e7ad4 | -4.838 | -45.866402 | 2024-10-20 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58e0e4ec-94f8-3319-b7f8-2ad9f838a18f | -4.8406 | -45.878201 | 2024-10-20 00:14:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d72fb5b-f4df-3cab-85ad-3b2dcdfdf761 | -4.5562 | -44.736599 | 2024-10-20 00:14:01 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47a17304-7173-3d67-aacc-01cb4442428d | -4.2502 | -43.691299 | 2024-10-20 00:14:02 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a7ba299-7d87-36f6-8020-3812fb7533f3 | -4.1033 | -43.084999 | 2024-10-20 00:14:02 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e54a699-842f-35b8-81fa-87a122496abc | -4.1051 | -43.092899 | 2024-10-20 00:14:02 | METOP-C | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23f9b357-8c60-39e7-8fa0-c9fb0f3789e5 | -4.1438 | -43.3554 | 2024-10-20 00:14:02 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd75e4e8-df03-3654-ad9b-897faaf7458a | -4.1456 | -43.363602 | 2024-10-20 00:14:02 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbc2195-125f-37ab-bbe9-56e5fd0eda17 | -4.4627 | -44.593498 | 2024-10-20 00:14:02 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cad067e9-931a-3c64-9672-1caba7cdf8ec | -4.4779 | -44.753601 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3be0868a-6c32-33cd-875f-e11f3588368d | -4.4801 | -44.7635 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28061aaa-4ff4-3cd5-82a9-45f0a1857f72 | -4.4659 | -44.745899 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5952f97-6feb-389e-95a2-c7b2d61e7760 | -4.4681 | -44.755699 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c34d5797-2ae8-3c1a-92ac-4aa5cc7487b0 | -4.4703 | -44.765598 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91dd2424-d97d-3727-a180-a88f75dd413c | -4.4584 | -44.7579 | 2024-10-20 00:14:02 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac7f9559-f46e-3d25-9b82-d1cab75696a9 | -4.134 | -43.357498 | 2024-10-20 00:14:03 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75d4885a-f8a9-31f1-b775-2524efb23796 | -4.1358 | -43.3657 | 2024-10-20 00:14:03 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9815d02e-389f-387b-a526-c47ed8f14106 | -4.6883 | -45.837601 | 2024-10-20 00:14:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 815f4de2-5871-3c30-bff1-4b591352d13f | -4.6759 | -45.828098 | 2024-10-20 00:14:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32dd26e8-9161-3687-a6ba-5e2c44c9c43e | -4.6785 | -45.839699 | 2024-10-20 00:14:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8e6f32d-6822-3c6f-8416-d6aaa637af15 | -4.681 | -45.851299 | 2024-10-20 00:14:03 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16c2535c-1bd0-34b8-90a9-32e6e37f00a1 | -3.7611 | -42.482399 | 2024-10-20 00:14:05 | METOP-C | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f055baaf-d6f5-36e2-bcb3-fb16d00dee66 | -4.2608 | -44.517399 | 2024-10-20 00:14:05 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1f407d5-82d4-37b0-a20a-2889c12d1693 | -4.2629 | -44.526798 | 2024-10-20 00:14:05 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6f4d91-0c84-3bba-a423-c4b54b629a73 | -4.5284 | -45.7635 | 2024-10-20 00:14:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd27b26a-4de8-3948-85c5-e67878a07eaa | -4.5187 | -45.765598 | 2024-10-20 00:14:05 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed0e415-6ca8-328e-8e1f-51fab3035e70 | -5.4773 | -50.5797 | 2024-10-20 00:14:07 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1638663b-0f20-3597-a9ba-98178f6a4870 | -4.0707 | -44.218899 | 2024-10-20 00:14:07 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb4423bb-5853-342d-9ae8-59fb73ea7680 | -4.0727 | -44.228001 | 2024-10-20 00:14:07 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88ff95c2-df5c-3eb3-9cc9-5815a6037041 | -3.5127 | -42.205002 | 2024-10-20 00:14:08 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a38c01ba-6ebd-3191-bf79-147fb187d4f9 | -3.5143 | -42.212299 | 2024-10-20 00:14:08 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06bf2ae5-1f69-3fa3-91c5-f95a5e6d97ae | -4.3222 | -45.619202 | 2024-10-20 00:14:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc6c6602-bd35-344d-a774-2e01c50181e7 | -4.3247 | -45.630299 | 2024-10-20 00:14:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 753a9519-b3c1-35fa-be2d-a0ae96d939c3 | -4.3124 | -45.621399 | 2024-10-20 00:14:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01163071-a1a4-3c67-9119-fb0fc14c29b3 | -4.3149 | -45.6325 | 2024-10-20 00:14:08 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba95843-dc8c-3f35-876a-8e85db64a820 | -4.3576 | -45.824402 | 2024-10-20 00:14:08 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7934c303-01e8-338c-97bc-74b5a891fb2d | -4.3602 | -45.8358 | 2024-10-20 00:14:08 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85e968a7-21e1-3268-9841-3c683f14fe90 | -4.3504 | -45.837898 | 2024-10-20 00:14:08 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc44054f-1bcf-32a1-b5d1-25f8e5fb8107 | -4.5816 | -47.530201 | 2024-10-20 00:14:10 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 65607bda-583c-313a-bf1c-edaabc09cf17 | -4.1734 | -45.733398 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc89c0a6-f757-3408-81b4-83ea821dc623 | -4.1637 | -45.7356 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e73a81ee-1d88-3452-83b2-5a5b667d8f92 | -4.1662 | -45.746799 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c679eb17-e91c-36c8-9ed5-969757f9f346 | -4.1542 | -45.784901 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa7dce2-e849-3be0-a297-bc54546feb86 | -4.152 | -45.820999 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b200c89-5772-3354-964c-3c82a9862039 | -4.1545 | -45.832401 | 2024-10-20 00:14:11 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8148c20-0694-3515-b19d-70ab16e3a446 | -3.6552 | -43.697601 | 2024-10-20 00:14:12 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c23c7bb-43ac-32df-aeef-0ad881ab0822 | -3.6571 | -43.706001 | 2024-10-20 00:14:12 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3399fce2-c271-3970-a6f1-3d1af277c32b | -4.4495 | -47.718201 | 2024-10-20 00:14:13 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d38414b0-b926-3b94-b686-e4cb3ff738e4 | -4.4529 | -47.7337 | 2024-10-20 00:14:13 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6312504e-94c5-3dd6-ade6-60d000ce82dd | -4.4398 | -47.720299 | 2024-10-20 00:14:13 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54bd7424-1c74-38f3-afc7-43899779fdd9 | -4.4432 | -47.735802 | 2024-10-20 00:14:13 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
