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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e0d4e74-4338-3b50-8b86-42ae9c2d2d58 | -14.8926 | -57.98029 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e89915f-933e-3354-9d1e-de56e7352bc2 | -14.88981 | -57.97607 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a22c35e-6642-305b-90af-e712aa5851a6 | -14.88925 | -57.97973 | 2024-09-28 05:10:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1adc3ca9-c85a-3a04-9686-567e1c7763fc | -15.36793 | -58.17517 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 703b00f8-c1ee-3be1-9e51-ef8bb6e5905e | -15.36738 | -58.17876 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08a1c79b-c4a4-3af8-91ae-cb37f7684912 | -15.36403 | -58.17829 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c065085-0530-39d5-b6fd-c10b3726ceaf | -15.36348 | -58.18186 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d63d704-3194-36e0-b40b-7a885615dcdb | -15.35282 | -58.16168 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bef523b-eac0-323a-8549-e80064056cda | -15.35227 | -58.16535 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d9b0f83-726c-36fc-891b-c249b704b00f | -15.35003 | -58.15743 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dda5816-7d31-3abf-9a02-7c8761626e4a | -15.33723 | -58.15904 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d8e15d-aa35-3c66-8c3d-ecf89e318d90 | -15.33501 | -58.15116 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b162a26-4823-3a95-88fc-2fc952204f53 | -15.33445 | -58.15481 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad51de7b-cd39-331c-96c8-4bdc5169ec11 | -15.33167 | -58.15059 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b3e3efa-3980-3474-906b-a6f0ac4f9d5b | -15.32497 | -58.14948 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33ebbd47-9f18-3626-8bd7-89f24fb006ce | -15.32107 | -58.1526 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10bf15ac-052a-318a-b7ca-d38693cb9531 | -15.31438 | -58.15148 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65335744-aeb4-31f2-8b19-6828235d2216 | -15.31325 | -58.15882 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1226267-299b-38bc-b83b-9233e8e2c1f4 | -15.31269 | -58.16249 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf817684-4352-38e9-9d09-18a0a6ed5cdd | -15.31103 | -58.15092 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01b0550c-c6fa-321c-8d7c-938f8a472316 | -15.31047 | -58.15461 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b21f15c-4895-38e5-a776-e1b8fc49194a | -15.30935 | -58.16195 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e86832a4-19f1-3f99-83d2-bc4d7e2df3b9 | -15.30544 | -58.16508 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca104cde-09a4-32b4-806f-82f4899b06b3 | -15.30488 | -58.16877 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a9aae71-3efd-3f24-aa63-20b3314496c8 | -15.30432 | -58.17244 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19714741-1558-393f-bee4-9c482792e32a | -15.30153 | -58.1682 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ffb377-6998-330d-8f62-5f1c5b874ba3 | -15.30097 | -58.17187 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 603a34ca-12b1-332f-a9a0-c5f0f40d73b1 | -15.30041 | -58.17554 | 2024-09-28 05:10:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5dc763f-502f-3413-a3a3-341ce2fb4bfe | -8.79985 | -58.19379 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2830e602-de01-3539-b4e9-6fd458fbbb14 | -8.79764 | -58.18629 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed41387a-0627-330b-ad14-0e48968a8038 | -8.79709 | -58.18978 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c48e4ade-86a5-399a-9e0c-21e586d3c6ef | -8.79654 | -58.19326 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08831b32-ad7c-3d2c-99b5-02ac5e73f5eb | -8.79599 | -58.19674 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cf189b6-79b5-3650-8e14-bb7cdbb1b13f | -8.79544 | -58.20023 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6fcf3da-32b7-3437-8a99-19944d738c92 | -8.79488 | -58.18229 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 82a6db9b-3231-3db4-aeb9-be49680b7a74 | -8.79268 | -58.19621 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b347583-79d7-3093-bf0d-ee9b63c6395c | -8.79266 | -58.17479 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9d7d4c1-7642-3db4-b029-7861896d1ce2 | -8.79212 | -58.19969 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8085744-4d8f-3830-af0f-2e3ab8a002f4 | -8.79211 | -58.17827 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa6989cf-855c-3e13-838c-a1858f72bcb3 | -8.79045 | -58.16729 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d296de3c-9ce9-3e93-9599-71eed2afc65b | -8.7899 | -58.17077 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d821da7-d5e6-3c00-a1d7-a7c5116d648a | -8.78935 | -58.17425 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b6f734-6412-3a6f-b12b-91d571d40fae | -8.7888 | -58.17773 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 192e905d-e099-3027-89f7-057c90339fcf | -8.78714 | -58.16675 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fe4a7fd-14fb-3a81-9f79-2060fe827de9 | -8.78659 | -58.17023 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4ed811-6848-326e-9cae-d797dd585cf6 | -8.78604 | -58.17371 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e9e2e4-d1ee-3ae1-b1b0-e024d7b96f09 | -8.78383 | -58.16622 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b89e7fe5-ed9e-3ffb-8d37-fb3d60290b69 | -8.78328 | -58.1697 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3f466f2-6176-3b41-8d76-8b3564f5becc | -8.78052 | -58.16569 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b6dfec5-82fc-3d0f-b7b4-b4542d742b6c | -8.77776 | -58.16168 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b9c32c1-006d-32c5-943e-2fb54c0f5017 | -8.77445 | -58.16114 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 444bba63-552c-392a-a86a-baae1e2605bc | -8.7739 | -58.16463 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 723078ec-b863-32ba-aa76-8669ddbc697f | -8.77169 | -58.15714 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2648bf05-68c0-356a-9ed1-363842f46cc9 | -8.77114 | -58.16061 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d43cab32-6d91-3b57-9c57-13982bf65034 | -8.76838 | -58.15659 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd91a07c-104d-34ce-9448-5c0048a03a6b | -8.76783 | -58.16008 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731ae1f1-2dbf-38bc-9d0a-1ac405d63e94 | -8.76617 | -58.17051 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9888f9fb-4b18-3096-ab0b-ca258eeff397 | -8.76451 | -58.15955 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b82ed80c-2669-3037-8eee-03f57b753bf5 | -8.76341 | -58.1665 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c17e6a-130f-3b03-8d8a-efb2eca9def0 | -8.76286 | -58.16998 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6eebd2b-98e7-31a0-9519-30fe2967185f | -8.7612 | -58.15902 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41345f21-fd7f-3ae6-b21c-1335801b8eef | -8.76065 | -58.1625 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 793a7273-b285-3dee-bb0c-e2c1549227e6 | -8.7601 | -58.16599 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c17f313-7e4b-3ae9-a648-dc6cc171fa86 | -8.75955 | -58.16946 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81731609-6063-32e1-88c3-a48381a386be | -8.759 | -58.17293 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0923bb7b-edde-3c15-9349-688d3e878c0a | -8.75845 | -58.1764 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 632746ed-1388-3db1-bd9e-3dd5663aa186 | -8.75679 | -58.16545 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ee7253c-6c74-38a0-b350-3130a8d9bf2c | -8.75018 | -58.18577 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42a28c12-7121-3579-b614-c48b6e80f2e5 | -8.72589 | -58.16765 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a11e2402-bd41-3221-9062-e607e39f0223 | -8.72258 | -58.16712 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 382ea98d-0dd3-3530-b371-f72b03e2844b | -8.66292 | -58.00774 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4375d73-90d2-3a18-b695-bb250aa0dc0c | -8.66182 | -58.0147 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03680d7e-2e31-3702-a3f7-32191999e360 | -8.66071 | -58.00026 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f4c79bc-7ecc-3e5e-a95f-afc5d0164268 | -8.66016 | -58.00374 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f00c06cd-f630-3203-999d-d5b5a3ba071f | -8.65906 | -58.01069 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b575eb8-fa35-308d-9cdf-deb3c1874d8e | -8.65851 | -58.01418 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72362eca-8dac-3c2a-82a4-b4b16fdcf03f | -8.65685 | -58.00321 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4c09d0a-8e87-3792-86c6-146aadf10811 | -8.6563 | -58.00669 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd01e1ca-914f-3df5-aa39-53e6714ad54a | -8.65299 | -58.00615 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71f3d06c-11ac-332b-9067-e92fa4a75cc6 | -8.65244 | -58.00964 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e47ac9-1873-3bf3-8dd2-5636863d0c7d | -9.1579 | -58.88956 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbb9a8e0-9881-39c6-9646-52a6136fbbf3 | -9.15456 | -58.88902 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40f0f683-6e72-3309-84d3-4e68d36e4b12 | -9.15399 | -58.89257 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8777b5c9-4873-3691-a53a-b7b8f8311fca | -9.15342 | -58.89613 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5a3c8b8-51a2-3a21-beae-5506ac873a9e | -9.15285 | -58.89967 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e010b71-ae60-3274-81bb-9af16dbe87be | -9.12539 | -59.52137 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c3fdf35-6449-37a3-906a-83b97ff29d99 | -9.122 | -59.52081 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5fc8dfc-560b-3939-974a-240994b5d322 | -9.1218 | -58.94932 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3411322-5bd4-3e58-94cb-6f0174ff6a0a | -9.09348 | -59.39591 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f865752-be06-39d7-8fc8-04ca23881a4b | -9.0901 | -59.39535 | 2024-09-28 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 100f54c7-18ea-321a-904d-5fbb222d47d5 | -9.02828 | -58.87588 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d494242a-db4e-3221-ba7c-26237e0d7595 | -9.00779 | -58.5752 | 2024-09-28 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cd3d20d-eeb5-3d5c-9006-7ce5fe3137bb | -9.00623 | -58.99298 | 2024-09-28 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34e54a7e-e2d6-37d9-a57c-7336802184c7 | -8.82312 | -58.21919 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1be0ff44-ad7d-3db1-889f-0f81fce2d2bb | -8.82257 | -58.22266 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1e1ff53-a507-3d61-accd-fb300345be30 | -8.82202 | -58.22615 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8da279f-2bcc-3360-b2e7-a4513bcb9746 | -8.82036 | -58.21518 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e2ed1fe-0a0f-3d73-9e90-e6833b47792f | -8.81981 | -58.21867 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd626bdf-3885-326c-8003-673d24f892e4 | -8.81926 | -58.22214 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6884e45b-e4a8-3b84-becf-fe32a2cda7bd | -8.81871 | -58.22561 | 2024-09-28 05:10:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README86.md)
