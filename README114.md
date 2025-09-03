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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 725bfdb3-2abe-36f3-81f1-40c61b002200 | -5.8895 | -57.7513 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0451c84d-3462-3f48-92e5-46ddca93aff2 | -7.7039 | -48.7371 | 2025-09-03 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b693fdb4-1f36-398a-9e64-f9d157b3ccbc | -9.7427 | -49.414 | 2025-09-03 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c7f3e193-2ffe-3bd4-884b-17e6dcce3545 | -5.9079 | -57.7506 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| b02b631a-786b-3877-bd11-0f1dfd13da7c | -11.9439 | -45.7998 | 2025-09-03 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4e022cbc-ced8-309b-a67f-c0e68549b92c | -7.4969 | -45.3495 | 2025-09-03 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 9db47a7a-d3fb-39e8-aa37-95ac568b3dd9 | -11.9635 | -45.7741 | 2025-09-03 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 259.1 |
| f1a656de-242e-3937-8ede-96b4550529c5 | -6.7595 | -45.9095 | 2025-09-03 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 861d77ac-1d2c-3ac2-baa9-19b547adf1bf | -15.0258 | -50.0491 | 2025-09-03 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f0d68f41-b272-319b-bf11-27bd221ba509 | -10.0932 | -54.7667 | 2025-09-03 13:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| f3ca4649-d9c3-3fae-a3bc-853a5b284af7 | -10.9524 | -50.7658 | 2025-09-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a5517a02-8bbd-37f1-af9c-9a9c105ed265 | -11.6836 | -57.3518 | 2025-09-03 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b31165d2-d0f1-3512-9de9-0e4a702aa54f | -9.6229 | -47.0638 | 2025-09-03 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 5a6b1aac-0555-3c0a-a90c-5db9fd26c89e | -7.53 | -47.4662 | 2025-09-03 13:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3ce67135-a5e6-34c9-9189-3bf8b28d725b | -8.0796 | -45.3617 | 2025-09-03 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 7ff319ab-9a70-3221-934e-94edfd06e143 | -10.9323 | -50.8529 | 2025-09-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| dd7f2a20-0598-3908-98c8-2c18bec34941 | -11.9606 | -50.6108 | 2025-09-03 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6af172ab-43ef-3860-8694-ae5c4b32bdda | -11.3893 | -43.6075 | 2025-09-03 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| b55cb026-afa1-3629-9981-0b4c526b9321 | -9.402 | -48.0585 | 2025-09-03 13:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| d6c05c6b-d432-3eb9-8f28-c9f6a83e0209 | -11.6165 | -52.0689 | 2025-09-03 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5482f448-ccde-374f-afa0-a94d70c30cc3 | -5.8455 | -45.6421 | 2025-09-03 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 16dea6e0-d2e5-36c5-83ca-0cafcc086885 | -10.9326 | -50.8316 | 2025-09-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 35e3c23d-0fab-3ecb-9745-d471ca54ae3f | -6.6982 | -48.4035 | 2025-09-03 13:00:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e9c9da02-52eb-32d8-bc94-f4abd166407d | -8.8653 | -45.824 | 2025-09-03 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 06b7b508-9fb2-3529-9067-c5e4723350d0 | -8.4604 | -45.0495 | 2025-09-03 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 253d44fe-248c-3ea4-9aff-7682a7226704 | -6.4646 | -49.5364 | 2025-09-03 13:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8dfcdf83-303a-3cdb-9a2d-4e81226e60d8 | -6.3689 | -45.6483 | 2025-09-03 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| f912ae19-dcaf-3d32-9c24-4b4b3734a114 | -5.9265 | -57.7108 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| d1d1b4e7-648a-3990-af27-87a27927edc8 | -15.0254 | -50.071 | 2025-09-03 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a1ba1bf9-434a-356a-949b-726d0d3a7cce | -5.8896 | -57.7318 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9f134732-7673-36a5-bc58-e8eb63f688d5 | -15.1771 | -52.356 | 2025-09-03 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 61125d7d-42a1-3e0f-a23a-394ba64f04cf | -7.9828 | -44.0415 | 2025-09-03 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 789bb71e-7401-344e-b1af-c014f16368af | -7.7224 | -48.7572 | 2025-09-03 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 301.2 |
| 17b6174a-f2d3-3b38-b414-14419ec3dfcc | -16.8532 | -49.6196 | 2025-09-03 13:00:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d6109042-5158-3d6f-96b3-54087b546590 | -11.3897 | -43.5839 | 2025-09-03 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 7792c3e0-6919-3871-9c32-77964852429a | -6.3502 | -45.6498 | 2025-09-03 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 12666a99-1a4f-38b8-8592-93a648026d9d | -6.9942 | -43.2308 | 2025-09-03 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 4442335b-f6c2-3f43-822e-35ed677d4b1e | -10.9136 | -50.8336 | 2025-09-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 635919c1-7644-3f5e-af34-6b9df64b0b9b | -7.0128 | -43.2525 | 2025-09-03 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 93e7ad2e-fe46-35eb-af6d-45d26bd17456 | -8.0608 | -45.3636 | 2025-09-03 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 421.8 |
| b399871a-c2f8-3b61-9935-f0c602ff6218 | -11.3897 | -43.5839 | 2025-09-03 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 54c7914e-daa9-38f4-bc94-8704201a20e8 | -12.793 | -47.6415 | 2025-09-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| a055a32b-885b-370c-8b21-228978e59c92 | -14.0502 | -44.5779 | 2025-09-03 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 440dfaa4-0cfd-3109-aeef-bf5cee690ea4 | -7.4969 | -45.3495 | 2025-09-03 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 0d869118-6879-3288-988d-bddb1292fd38 | -9.7613 | -49.4337 | 2025-09-03 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 8fffe899-1767-3058-9561-9aed813de3b2 | -8.3644 | -48.3116 | 2025-09-03 13:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 66a44e0c-39a6-3b4a-969c-ed7078ccba62 | -6.35 | -45.6723 | 2025-09-03 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| d8770daa-c3c5-374b-9b48-45ef6d36a62f | -16.8532 | -49.6196 | 2025-09-03 13:10:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 4ccc6ebf-d707-342d-a767-3ebe1632923c | -11.3901 | -43.5602 | 2025-09-03 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 6437251a-7993-396d-867b-b04fc8d971e6 | -6.3502 | -45.6498 | 2025-09-03 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| ce4544d0-646b-32b3-93f0-35a606b186ad | -10.5045 | -50.3226 | 2025-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b4ade4d4-47ff-3af4-b990-dce829084ea9 | -8.8839 | -45.8446 | 2025-09-03 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c14656b1-ff51-337a-9fba-2ecac37d0822 | -9.6499 | -47.8569 | 2025-09-03 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 507cf196-949b-3b7c-94fa-31a7a3429c62 | -6.6847 | -44.0496 | 2025-09-03 13:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3d8f7b29-e0cd-3571-ba93-168b92b9a879 | -8.0608 | -45.3636 | 2025-09-03 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 82368cc0-0fb3-35ab-80ed-1f19d979b9d4 | -8.0794 | -45.3844 | 2025-09-03 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ab253308-2bc9-30ae-a8eb-a334c86ed71d | -6.3687 | -45.6709 | 2025-09-03 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 7d8a2ef2-90d2-35d9-8bfa-f7ac831697e3 | -11.8843 | -50.6197 | 2025-09-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d7f7cd43-a4dd-3313-ae23-8a7af8b4ce72 | -10.5004 | -53.651 | 2025-09-03 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d91825f8-5910-34db-a8bd-18038ac34091 | -9.402 | -48.0585 | 2025-09-03 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| aca06ad3-8879-313e-85ca-1b2137dddb97 | -6.1234 | -45.9139 | 2025-09-03 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| b72db8e4-5dae-3edf-bfdb-7a19a86501ff | -7.4842 | -44.8043 | 2025-09-03 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a0203af9-41d0-3389-82e2-420640202130 | -6.0699 | -45.6259 | 2025-09-03 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 141.7 |
| ab64a7d8-b2b1-387d-aeba-40b5b6a6df8a | -7.484 | -44.8272 | 2025-09-03 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0c1f384d-29da-35f4-aa39-d73ebf74459d | -9.7615 | -49.4121 | 2025-09-03 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8a83ca98-785c-34d6-97ac-130b3e004b46 | -11.9635 | -45.7741 | 2025-09-03 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ddc1d5b2-77f8-3c39-8d1e-0e7c373ef515 | -10.4853 | -50.346 | 2025-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 07b4cbb6-a9fe-3b9e-8184-ff7313e3c734 | -10.0932 | -54.7667 | 2025-09-03 13:10:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| b63859ed-a58f-364f-81ff-a6204c7a75db | -13.5162 | -47.0393 | 2025-09-03 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fa124c09-41b8-36a2-b291-1bf3fdae7e30 | -9.7429 | -49.3925 | 2025-09-03 13:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 65732537-ee80-3725-a3e3-4a706137e884 | -7.6646 | -43.8653 | 2025-09-03 13:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| bba63648-b686-30ce-a0f9-75016a76bb72 | -11.9034 | -50.6175 | 2025-09-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| a029f01a-108b-3fdf-92fb-1966e916adbc | -10.0411 | -45.6212 | 2025-09-03 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 87e2c84c-ea25-3e7b-a0c5-d2b0da966132 | -11.0181 | -51.5001 | 2025-09-03 13:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 16ede203-6d94-3c63-b948-24f5c248b0ab | -6.7597 | -45.8871 | 2025-09-03 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2dfdab5e-4c04-3648-8c4b-ec169c2b9088 | -6.7595 | -45.9095 | 2025-09-03 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 28098924-1dd7-35c1-b91a-14c3c55ebe5b | -5.8455 | -45.6421 | 2025-09-03 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5834c8a7-93c3-36fb-8b80-8dace7cc29c0 | -7.4966 | -45.3722 | 2025-09-03 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 87bd0787-17cd-3bc2-af9d-9b21f46e2b71 | -8.8653 | -45.824 | 2025-09-03 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3979753e-8898-3bf5-b0bc-ce1174d93668 | -9.1373 | -49.6659 | 2025-09-03 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 13c5abb6-afa0-3cff-a293-971731e163dc | -5.908 | -57.7311 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 195.4 |
| b0ea2004-7342-301a-bf2a-f202e2fe6c10 | -9.6229 | -47.0638 | 2025-09-03 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1587d6df-b1e4-3496-b138-11699402760c | -11.3893 | -43.6075 | 2025-09-03 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 0dc69773-4698-3fe5-bb3b-b4c2f6e4d5d8 | -11.6647 | -57.3533 | 2025-09-03 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 3bf4c18f-272f-33be-84f5-c03c5f72eba5 | -6.3689 | -45.6483 | 2025-09-03 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 1498574a-d183-3ecb-937f-c71520164519 | -15.0258 | -50.0491 | 2025-09-03 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e11d2959-9050-35dc-a94f-7c9c38bc1ed0 | -6.6982 | -48.4035 | 2025-09-03 13:10:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 279e44fb-5b78-3657-a8ca-50e01231cee1 | -5.9265 | -57.7108 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 8e42c065-b382-31de-a92e-0292e9179cb1 | -12.7926 | -47.6638 | 2025-09-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 86507bbd-7705-328b-af87-b3cadf941bb6 | -5.8895 | -57.7513 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| ee448283-e97c-3488-b4f9-0f45a67883a8 | -5.9264 | -57.7303 | 2025-09-03 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 79c218c0-9add-3a2f-bc14-f662d3a8ec9a | -9.6226 | -47.0861 | 2025-09-03 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| a1677a50-59f8-36ae-9265-e3c46067b419 | -11.3709 | -43.5631 | 2025-09-03 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1c3561fc-c771-3bb4-9a44-17418de7ffab | -3.1962 | -42.743 | 2025-09-03 13:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 929ad5c3-1c48-36f1-9c3e-294d3b2feabc | -8.8842 | -45.822 | 2025-09-03 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2ad8a10e-76df-30c1-a3db-ad76f1a976fa | -10.0221 | -45.6235 | 2025-09-03 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6e8f5d4d-2023-381b-9ee6-44471dac1b7e | -8.0796 | -45.3617 | 2025-09-03 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 273.6 |
| e4f04d50-705c-3c20-9907-51382f40e960 | -11.1224 | -44.6521 | 2025-09-03 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| be6524ec-d321-3b33-9690-263179b70224 | -5.7154 | -45.5613 | 2025-09-03 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1d767d24-fd94-312b-ac30-d0aa11a70c6a | -6.4648 | -45.4154 | 2025-09-03 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |


[Clique aqui para ver as próximas entradas](README115.md)
