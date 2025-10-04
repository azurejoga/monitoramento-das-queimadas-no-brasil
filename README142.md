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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81a036bc-7bda-314d-b4b9-ecc3145fcf82 | -13.45653 | -47.27245 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 6e655d43-1545-3fcc-8a2e-d8e114582c10 | -16.95044 | -48.16977 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d94ac72a-68e7-37e4-9f99-295b3d82fa56 | -13.19701 | -51.00474 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f3b8893f-e372-31d2-8b35-adffbfd9bb99 | -16.01954 | -50.95296 | 2025-10-04 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 42012d23-182a-397b-a00e-e48cfbe400fb | -12.02841 | -45.20626 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| f49a5626-89f1-3cf0-88b3-df905b08142e | -14.93229 | -46.84996 | 2025-10-04 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53942d39-4ca2-3df2-a78f-b0a0e67747e4 | -15.53804 | -46.85217 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| da5e1901-8c9c-32d7-91b5-ea2a27c14a0d | -13.10903 | -47.84573 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| db33bee0-259b-31ef-b8d7-27cc7974abab | -11.92771 | -46.40991 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9d11759b-3a31-31d7-b7d7-06a9a6156eff | -9.35217 | -45.72696 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cd80aaf1-8f80-36fe-aad0-a8f61332b58b | -12.8914 | -47.16491 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| aba6ce6e-1f12-31c5-8706-8e7fac5b5f45 | -18.89121 | -44.67773 | 2025-10-04 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ca746793-6e59-3ed1-975c-1e39a1ab56da | -14.9899 | -49.9507 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97504403-a39c-3d04-9204-becad25545d3 | -8.96833 | -46.75438 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 42d45a32-adad-3507-886d-8e28690ef9b4 | -11.79524 | -46.83506 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 643936a2-f4f0-37f6-a153-ea6655b74766 | -9.93776 | -50.23816 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| cd9c0a7f-eebf-38dc-99f5-0eb5d9f46fa4 | -13.24923 | -47.24031 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c0d90755-5dae-34d2-922a-5d9c384c66b2 | -9.10412 | -46.71186 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 012dbd31-daf7-39a5-8640-f8081707f7c0 | -13.11256 | -47.94847 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6c0f1886-a8b2-3ce7-b9b6-feeaa8d5437d | -15.61857 | -49.11803 | 2025-10-04 12:19:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 91bcf40c-c3ad-34bc-bd71-3609110165c2 | -11.13977 | -47.89177 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| b7b59918-f828-3004-8128-a1475bf91fc2 | -13.31999 | -48.11682 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1d0bdba5-afb7-36ad-b609-17d4b3b9aada | -13.9359 | -48.19468 | 2025-10-04 12:19:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 80acc108-71ad-3589-a95f-98c05bb32442 | -11.55629 | -47.68344 | 2025-10-04 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| b2c26d37-d0da-3f31-a91f-552a86acdae0 | -16.30334 | -47.78939 | 2025-10-04 12:19:00 | TERRA_M-T | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4d5a3cdd-b5c6-3c80-bbb4-26cb926198ae | -14.93988 | -49.97537 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ef394507-08e2-33cc-83a8-bfdba7851659 | -9.68532 | -45.7063 | 2025-10-04 12:19:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e40760e4-e074-3add-b99d-dbfe15088e08 | -11.02203 | -44.63897 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 22e14aa6-9094-391c-b9ca-feffcb3f7082 | -8.48044 | -49.59716 | 2025-10-04 12:19:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 70440670-bba8-3410-a6c6-a4f8094df762 | -9.36388 | -45.77843 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 338dca7b-99eb-3337-be81-c04e7131518e | -14.56558 | -48.94806 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3fb3f13f-fb4d-3356-8fd4-eb0aa359d32e | -12.71348 | -48.55267 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1a0decc1-ee44-372a-b5f0-c0e37248b6c5 | -10.35214 | -48.17545 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ddf2652c-16d5-3c05-a2f6-b01e0c0c6f4a | -12.65916 | -46.97915 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 0273a8b2-4f38-393d-af34-6dfc0c0c64e7 | -17.9873 | -49.82653 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 328.2 |
| 6ac2716c-ceaa-34ae-b367-ebacf022e322 | -15.35086 | -47.95705 | 2025-10-04 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ad532112-7ddc-31b1-9380-538a51cfb176 | -12.79456 | -47.71975 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3196a67e-6fd1-307e-b2bb-67b7112a2599 | -16.04251 | -51.04942 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f938dbee-236c-39ae-8b3f-30655f574f39 | -11.78882 | -46.81495 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e0278750-f07c-3158-bc64-dfbf0167d7bf | -17.99615 | -49.82791 | 2025-10-04 12:19:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 6ce4466d-35cd-3925-af63-c3e4df99baed | -16.08718 | -47.55295 | 2025-10-04 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2f8ebc24-28b6-3b39-b188-89afe2b5e643 | -11.0808 | -47.72201 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3837b2df-062a-37b5-8c59-c65c057f89a2 | -11.78492 | -46.84296 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75d5f8e4-e36e-3665-9e52-87f990c71b70 | -9.3362 | -45.77428 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8e86a8c9-b51a-358f-9531-9f4f5f07c255 | -11.93174 | -46.38053 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cf48628e-434c-3817-86ed-b78ec1a337bf | -14.05043 | -53.91387 | 2025-10-04 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d758f752-a7d1-31ef-8c5e-da1cae6e2399 | -8.96704 | -46.76343 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4d9092a9-f741-3177-945e-3b420e0ce64f | -13.98454 | -45.0809 | 2025-10-04 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 11a4117b-6916-3086-bc2b-c33deba8c70d | -11.14733 | -47.90198 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a41f32b6-482f-3da5-b5a1-c03eff0927af | -12.39393 | -45.22213 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f9745278-67ac-3712-bb06-b795b8f0b97d | -9.17397 | -49.95722 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9b7eecba-0f2d-370c-a85f-ce55ebe249f6 | -14.59524 | -52.4906 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c90f2559-efbc-39c5-934b-c0eb18b8e0e0 | -11.96062 | -49.34663 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 54d2bb13-8902-33c5-9091-4167c03281c9 | -10.99275 | -46.5131 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f3df734f-c0a4-3858-a959-abab4640245e | -13.24047 | -47.82452 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| e78d6fcf-f44a-31a1-a73d-9fbe117eed5d | -12.29315 | -45.36215 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| db034170-3aaf-3b95-acd2-014a23ea3b2c | -10.33971 | -50.30932 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f089fae0-bbc6-3396-8b55-073b1c3920dd | -16.03026 | -50.94455 | 2025-10-04 12:19:00 | TERRA_M-T | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6d52465e-143b-3bae-beac-1ece42d9c5a2 | -13.5111 | -47.27732 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 255bd76e-a6e1-34d2-aa8d-e10de3fa9932 | -10.34462 | -48.16513 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c80698e5-ef8b-3550-8a65-ecd6c0e55eb0 | -10.87313 | -46.64436 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b43a5473-156d-3714-b237-41816c76461e | -18.55 | -45.04632 | 2025-10-04 12:19:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6557cd08-a644-35bb-85c5-ba67eb38903f | -17.86019 | -44.6989 | 2025-10-04 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f559383b-78b1-39f5-a3b4-cf317438fd3a | -10.99754 | -46.67733 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6efd9189-f4ab-3b02-8b66-b6b19e80b9c7 | -13.10015 | -47.84443 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5f3cd79d-f7a6-3e5a-b28d-47a4bb03eda0 | -10.7187 | -47.8644 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9ca75c7-c3f6-3d4a-8937-ede214e363b1 | -8.95813 | -46.76218 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| f5f38079-b0c4-3ee8-8cea-f8679724123d | -10.02278 | -48.27626 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d79c9e6f-46b0-364f-b48e-f53850ebcbb5 | -14.67304 | -48.25851 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 66f0e32f-ffd4-35d7-8a32-1f4e4262d8a6 | -11.84026 | -44.93612 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7a93d35b-748f-3a10-a39c-f90eaa14bba1 | -11.24708 | -47.78581 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cef30b93-85d8-3c1f-80b4-0393729edd7e | -12.53856 | -45.9781 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1fddd2ef-6a34-32d3-9d30-6757de16b6a1 | -8.92511 | -46.60955 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a58d5814-53c7-3bb8-9264-9698d43095bb | -14.94885 | -49.97678 | 2025-10-04 12:19:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e416f6da-2f36-3c3a-b320-5a8feab7c607 | -14.68062 | -48.269 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0c86a706-73ac-3429-8bde-834a79c474cb | -9.9099 | -45.95991 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 7abbceb9-0f2e-3ba0-9310-f52f5f229c79 | -12.39366 | -42.53753 | 2025-10-04 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 5dfc3978-e480-3f71-8824-b8eeaf7f8e50 | -14.94157 | -46.85131 | 2025-10-04 12:19:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c67b8e4c-f908-3229-be79-67bb04cfe1d8 | -19.00327 | -48.09941 | 2025-10-04 12:19:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| eb5cb7f2-4d7f-3610-ace3-317c3fe7fb90 | -12.5438 | -46.01048 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 34ace67d-ed71-3a74-8f5b-7a0c8067d06e | -14.16663 | -49.21658 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e5d3a23e-611b-340b-a22c-ba62eee8d632 | -13.74861 | -51.30008 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fbe758f9-c186-308b-a876-bc7bcfb7cccb | -9.08274 | -48.02408 | 2025-10-04 12:19:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0985447a-57d6-3573-9b95-9ec13b1991da | -13.35429 | -48.06631 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7d2c4904-55b3-3122-a21f-dd4330d32b5e | -9.67118 | -48.21911 | 2025-10-04 12:19:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5daa2e0d-62e8-394e-b6b2-0af64f3ad7db | -11.68533 | -47.48704 | 2025-10-04 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 25cfc805-bbeb-3027-bfbc-eae53c3af0f1 | -15.99141 | -50.90245 | 2025-10-04 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b81a55e0-5371-396f-b34c-d0204f1164a1 | -13.21386 | -47.82046 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 93ebc514-b72f-383d-97f2-3f71923876d2 | -12.58683 | -54.73251 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d24e1201-3a34-3d22-945f-9ee487cf90b9 | -17.46008 | -49.89658 | 2025-10-04 12:19:00 | TERRA_M-T | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 10112e2e-2e48-3c72-9bdf-87db106260c7 | -11.31512 | -47.82893 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7c9924b2-5eee-32b4-9af7-e5f844ffcdfe | -12.38907 | -42.53115 | 2025-10-04 12:19:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| ea37f020-cba0-3c40-82e6-4a915c4be15a | -15.4529 | -45.87014 | 2025-10-04 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 543ff1a3-8ff1-3807-9927-11b2f992da14 | -12.02994 | -45.19494 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 998f3325-690e-30fa-8c22-f8badd4e4a68 | -17.58743 | -44.4952 | 2025-10-04 12:19:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 790431d7-2538-360d-9cce-5a52f3a02ee2 | -15.96553 | -43.32578 | 2025-10-04 12:19:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 06fca3d6-3378-36b2-a114-1215662b512d | -12.93655 | -46.36473 | 2025-10-04 12:19:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f7c71486-af1f-3ae9-8360-2b1be28d147a | -12.87332 | -47.29576 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| cdca461a-fe70-3321-8b97-8f360ec12ca3 | -14.21179 | -46.05862 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 636b9445-d927-3b42-a651-af4dc92af543 | -11.13849 | -47.90071 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 208.8 |


[Clique aqui para ver as próximas entradas](README143.md)
