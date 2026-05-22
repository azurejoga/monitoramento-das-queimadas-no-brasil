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
| 7d09f3a2-c510-3ec6-bcf1-bb4364d14d9d | -5.95354 | -43.49028 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2c54b760-1729-315f-8f9e-693ade436584 | -5.95285 | -43.49406 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed7387cf-a8b1-351b-9442-e70a3ebc4892 | -5.02795 | -37.56533 | 2026-05-22 03:45:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b92c5c37-c660-3c24-bc8c-653358b782e0 | -4.65824 | -42.42077 | 2026-05-22 03:45:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2f84bd3-de42-3445-8d57-6e6ac4db00e7 | -4.66355 | -42.42168 | 2026-05-22 03:45:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d28a9c0e-5dbe-3fcd-846b-eb4c7ff96c9c | -5.92358 | -43.47844 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca19da8b-1066-3f6a-a395-a746a7a2e0d8 | -5.95076 | -43.48748 | 2026-05-22 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 865ea362-02da-3647-af3a-188d96de6a7c | -5.77124 | -45.13691 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63806a4f-8125-3954-8f67-459530d49aba | -5.77319 | -45.13738 | 2026-05-22 03:45:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5e2f835-8277-3f9c-a48b-af65a6e13596 | -8.73645 | -47.9875 | 2026-05-22 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8aa25f4-5fb4-3668-8996-e248a7fa15da | -7.63947 | -45.30728 | 2026-05-22 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bf5bf0b-5510-30ae-9a5d-97d3e9bb5ada | -8.73783 | -47.98044 | 2026-05-22 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 177c1e5b-c2d5-3174-b1fc-78b0a5247957 | -12.26606 | -43.50858 | 2026-05-22 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb202f5a-55d5-309c-9d4b-3b9ce454b5b1 | -11.05534 | -46.71385 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccaccea1-2e27-3207-bdc6-a7edca75da1c | -12.59643 | -44.51516 | 2026-05-22 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6c6da8-9aa8-33eb-bc71-d788e04d6109 | -11.99488 | -45.14693 | 2026-05-22 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffd7a9ae-0283-3047-bc04-c4b5d426a02f | -11.04261 | -46.79313 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40304abf-3829-3951-9ddf-a69cb371d611 | -9.72491 | -47.05342 | 2026-05-22 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91b2815b-8ac7-3e1a-9d92-6ae2d9828278 | -9.29359 | -45.48937 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 127a7211-8b6a-3cec-b20b-d09fcb5f6e7a | -9.72606 | -47.04766 | 2026-05-22 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4cc4af-84f3-3060-afa7-08d4ff46b486 | -11.61087 | -47.90969 | 2026-05-22 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 518227e9-e287-3935-a417-f4a8c99e9a5e | -9.3992 | -47.37157 | 2026-05-22 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e48bdbb1-bacd-37af-97b5-ecf91425e566 | -9.40042 | -47.36554 | 2026-05-22 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8abd0a79-3198-3a4d-97f6-c7488afa8d9e | -9.28847 | -45.48368 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1e3ad12-c14d-3aca-a440-6f7b611c2a67 | -12.24028 | -44.26761 | 2026-05-22 03:47:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc43407-10c2-3dc0-900d-afdb33b22fb8 | -7.64557 | -45.30834 | 2026-05-22 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d24f5af7-551b-3e1d-8ff7-2b7d5a400b1a | -11.99713 | -45.14788 | 2026-05-22 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbd2bff5-6f43-3e22-a18c-ec84db1a7142 | -12.00046 | -45.14808 | 2026-05-22 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4188d8c0-0c0f-3ea0-a1e0-a2438f247ccc | -6.56813 | -47.91211 | 2026-05-22 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 148e175f-444f-3057-a70e-f561602cd56a | -9.29871 | -45.49508 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b7ab676c-286f-3756-a72b-b07a38136014 | -6.56952 | -47.90485 | 2026-05-22 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf07dc60-2656-3ba4-977f-5d6eb3ae851e | -12.26495 | -43.51442 | 2026-05-22 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b94b94c-71a6-388f-a5ed-0528a7d58b2e | -9.29786 | -45.49952 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1eba3942-7cdc-3afb-b1ef-78c6a1b4cb3d | -12.23566 | -44.26319 | 2026-05-22 03:47:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf154de5-b57f-3f87-95e8-e7d5d6aca62f | -12.26995 | -43.51545 | 2026-05-22 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11072c56-821a-3830-88b9-1a68bb0b57c9 | -8.55593 | -45.98598 | 2026-05-22 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 627d22cb-dacf-3bc1-bfdf-d496a561585f | -11.0394 | -46.79519 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6fb7178-6356-3a9f-b5ab-e5f21f999fb8 | -11.0674 | -46.70298 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 282afe7b-6218-3291-86b2-966e871fc21c | -8.72109 | -48.32976 | 2026-05-22 03:47:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b224e7c-93aa-3e9c-bea3-3b5be857e170 | -11.04034 | -46.79041 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7a7b61f-50c8-35ae-bf52-b9d1cdc727fe | -8.72348 | -48.32793 | 2026-05-22 03:47:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48a3bf11-4bce-3817-ad97-fb1c56d82527 | -12.00121 | -45.14429 | 2026-05-22 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c14d3c29-7f64-326e-985f-eafd2ebd9cf4 | -12.27495 | -43.51648 | 2026-05-22 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 481f8d6d-c874-3384-a3a3-ba211229db6d | -9.28762 | -45.48809 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed670699-78cb-3ff0-bb2e-925e65f0e3c3 | -11.04164 | -46.79791 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b2ffa07-0657-3aad-b8cb-1a6c1281e272 | -9.29443 | -45.48496 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83c597d0-8a8e-31da-ac40-f7273a23149d | -6.56644 | -47.91211 | 2026-05-22 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b53c4c7-5d65-3104-8494-f167e231a6aa | -9.30467 | -45.49638 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f7032fdc-111b-37a6-992e-6a5bd516890c | -6.56777 | -47.9049 | 2026-05-22 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 41b06e65-4bd2-3f3e-ae5c-4223e885c42e | -11.03636 | -46.79164 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70b3e948-681d-32da-8565-a2153a1a62da | -9.30382 | -45.50082 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e168e1a0-3051-3543-89f0-ed171765ba9e | -11.05913 | -46.71168 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c7482d-a1da-3b3e-9d46-7048925357c2 | -7.64644 | -45.30366 | 2026-05-22 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a932e8ba-73f3-38a7-bd09-51a192dc6fbd | -11.06011 | -46.70684 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afd6fcc0-7b4b-3ab1-8720-97805be37deb | -8.92477 | -46.91504 | 2026-05-22 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 623c1205-cb0e-3bb8-97b8-8062daf11fdd | -8.93021 | -46.92215 | 2026-05-22 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6731ff44-3851-30ab-b7f3-607501546f73 | -11.99786 | -45.14407 | 2026-05-22 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dc1330d-7c57-31af-9ab5-140f55bd80d0 | -8.72243 | -48.32287 | 2026-05-22 03:47:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a8280f2-448c-31cc-bc14-810f751c521d | -8.71632 | -48.32665 | 2026-05-22 03:47:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5c46ba3-7ebd-3e35-8087-fba9be298149 | -6.56086 | -47.91107 | 2026-05-22 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f7668a1-824d-3a3a-9e3d-9d18c2042da2 | -12.23502 | -44.26654 | 2026-05-22 03:47:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b94d5f-f589-3e7b-9411-031929cf7ced | -8.55063 | -45.97984 | 2026-05-22 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 595fb504-d485-364e-9ca5-27b0c9fe3adf | -8.56212 | -45.98755 | 2026-05-22 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ced236b9-0780-32b2-987b-7d7cacafb55f | -7.64032 | -45.30265 | 2026-05-22 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd2c989e-effb-39b3-ba2a-45cd9bba17e4 | -12.23437 | -44.26991 | 2026-05-22 03:47:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a958b78-6bc7-3850-8c79-910f0f347c04 | -8.71395 | -48.32838 | 2026-05-22 03:47:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a745093-acde-3fc2-94a6-379eb455d31f | -11.05182 | -46.71562 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e185bdb-661d-33a6-a703-b6294cd68675 | -11.61211 | -47.90364 | 2026-05-22 03:47:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8c72740-a307-33cc-9705-d2f8bbfc9671 | -11.0626 | -46.70995 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a36c851a-a3e2-3135-8e4c-3500f100c03b | -16.35393 | -43.87918 | 2026-05-22 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48afc34a-939f-3a35-ab81-a6969744d122 | -8.92369 | -46.92058 | 2026-05-22 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67165398-614d-3ad9-8b2f-3d781b068c47 | -11.06355 | -46.70514 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c77c1b42-4d84-3d0d-9799-fc9dad807e44 | -14.08144 | -42.11517 | 2026-05-22 03:47:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdf9af89-9775-3eb0-aee9-f2b6338d093b | -12.59709 | -44.51178 | 2026-05-22 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8f0ab44-96ad-3a1e-983c-56f55f4b403e | -9.29955 | -45.49067 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f6c82fa3-7eaf-3fed-ab23-aad104dfa634 | -12.27384 | -43.52232 | 2026-05-22 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0188db29-32de-399f-be06-3a177b6bd381 | -11.04807 | -46.71773 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a4722c6-5df7-3223-89fd-91d5d99b5391 | -8.73383 | -47.9853 | 2026-05-22 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2f91896-ae45-3b0a-8e30-83d6d98ddfa2 | -8.22164 | -36.11423 | 2026-05-22 03:47:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46e3a141-e1f0-3714-8f3e-272f0dc1a132 | -12.2363 | -44.25988 | 2026-05-22 03:47:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0ac9995-0e83-3cff-b283-0c6d38eeacb7 | -8.55501 | -45.99083 | 2026-05-22 03:47:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d67ad77-6a43-3d02-afa4-e7b6e97447fb | -11.04452 | -46.71947 | 2026-05-22 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7466a25f-9cfd-3d8e-90c1-02170dfc97f4 | -9.29274 | -45.49381 | 2026-05-22 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c1e12c93-f193-3d1e-9787-7b0c20552e06 | -14.75371 | -41.70684 | 2026-05-22 03:49:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1940b455-99d4-3d45-8876-1f256b4b33d8 | -29.07415 | -50.73626 | 2026-05-22 03:51:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4efde210-a2af-38a5-b875-8014503af043 | -27.68495 | -48.75331 | 2026-05-22 03:51:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cb461f30-95bf-3540-ae47-62443f922eab | -3.41874 | -43.16439 | 2026-05-22 04:02:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6741ea3c-ade4-33cd-ab13-354ba13183d9 | -4.19058 | -41.00606 | 2026-05-22 04:02:00 | NOAA-20 | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e1afd873-7071-31cf-85f5-ae39c991e7cd | -3.42251 | -43.165 | 2026-05-22 04:02:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1afc7f74-1187-34db-b50f-017fd64c7074 | -9.3011 | -45.48958 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30f1f6ad-eeef-3d02-ba9a-dce2fa112c6a | -8.55717 | -45.98864 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d639dafd-9045-3cfd-9c71-52218a561c32 | -5.76903 | -45.12817 | 2026-05-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50e715ad-fcee-3302-9052-e4613c0cba8b | -8.71844 | -48.32517 | 2026-05-22 04:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 753ba108-cbeb-323e-b342-ec15d553c37a | -8.93192 | -46.91573 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb08f673-cc91-33aa-9230-06c0c7605c89 | -5.92692 | -43.47648 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2fcd26a6-6399-352c-8c1d-f620e76aad46 | -9.29253 | -45.49161 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 758144fc-de8a-38ae-9317-cdb5753193d1 | -9.94025 | -52.46904 | 2026-05-22 04:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea596568-d386-3cd6-a797-7c30d2c111d3 | -9.40175 | -47.36521 | 2026-05-22 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2512f01b-2e1f-3edc-b0f1-4ce4c15f0830 | -8.55365 | -45.98405 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ebf66c2b-1a28-36f3-93bb-647ac0a8e835 | -9.28913 | -45.48737 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README3.md)
