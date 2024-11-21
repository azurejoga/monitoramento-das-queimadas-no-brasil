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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6e9cea0-282b-343e-9541-5176efc8589f | -3.11867 | -48.66505 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6867b5a9-14e1-391f-bbd9-242ae568dc1f | -1.19605 | -51.77471 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75d9bb40-2805-3a7e-b198-f04cc1910c76 | -3.7979 | -47.79435 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a24f4c1d-6aa3-34f1-96d0-2e2da1497954 | -0.03943 | -51.24176 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3bebb64-6983-3031-b8d5-1aa92d3523ae | -1.9775 | -53.32821 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc6ac207-f502-3f85-8b5b-7a34430108f6 | -2.9008 | -48.32294 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 866c13d2-2579-328a-ac55-68fa4b0c41c8 | -2.75243 | -52.11233 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e725925-eb4b-3f56-a0f8-88d2302841e3 | -3.2519 | -46.42609 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84287f1e-0460-38b3-adb8-d76d850fc139 | -3.88517 | -46.66011 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb1bd0c-e3e2-3d28-ad89-b0615f449cda | -2.39471 | -46.7985 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a3f51d5-8cf5-388a-a903-08a47d896d31 | -2.14864 | -53.77835 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e427b8ae-6e68-3ffe-9da8-d20563a7d74e | -2.19726 | -53.65418 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce2e30dd-9c87-31ed-80c8-7cc8afa41fc9 | -2.12612 | -50.12619 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39b04027-ba58-3ba7-852f-4e64ac95001c | -1.96099 | -53.00137 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae123d04-109c-3fe1-80e4-04875e271b5f | -1.61094 | -52.60781 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8eebf08e-1863-3d9e-90fc-dda18c625a7e | -1.3916 | -46.50763 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50b0a806-13fd-30a2-83ec-31638e2e8fe3 | -3.26804 | -50.62539 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af70e74d-f312-3a34-91c6-b33b51ec3455 | -3.19198 | -48.57917 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc44ee1c-ab3a-36fe-998f-fd5a457f0ef7 | -3.227 | -43.26458 | 2024-11-21 04:29:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e7fb7a4-df79-3a63-8154-ec0a969465d9 | -2.61266 | -48.24563 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef14ea28-5ad7-3889-8d44-a024ffef137d | -1.6476 | -55.25863 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deee5061-8eb0-3f2a-8fed-c4724db40c72 | -2.51985 | -46.28408 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5b843f5-64d9-300a-8017-896eb7f34140 | -2.60414 | -46.2615 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26987ba6-b9cf-3a5b-8b52-bce4934fc1f3 | -3.53806 | -50.53074 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4f830fe-b3b8-3529-aad0-002494e70ac3 | -1.72864 | -53.02069 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e066931b-6633-34d4-883a-a632f1f3c414 | -2.10417 | -48.89788 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24c94f68-24ff-34e7-ac3b-66be5a87c109 | -2.62955 | -51.92369 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 364090e2-a1b7-3b90-843c-a851e2a69af5 | -1.75869 | -52.67166 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b486a314-2e27-3041-a675-8c338fcc3209 | -2.09799 | -49.55021 | 2024-11-21 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a948e5-dc02-3b71-8cce-59feb8e56bee | -1.36121 | -55.50735 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f4734bb-c4be-3990-80c6-2caba12ad87a | -2.84396 | -46.67469 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e848ed07-6c6a-30c2-a7c4-e6d248babeac | -0.42373 | -51.56452 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccc6227c-fac9-3d2f-b7ad-e56b582d0d11 | -1.1852 | -53.71473 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 855140f6-a822-3e28-8f5c-3b6f6e65a8ce | -3.79986 | -46.51545 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12d45a36-b793-32d0-8858-ebddd9258655 | -2.93628 | -48.33955 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db9cc7c8-1dcf-3d3b-b312-8f1d2e66dc60 | -2.69717 | -46.22966 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8db05af-acf2-366b-8ce2-524f291cdddd | -3.80582 | -42.54612 | 2024-11-21 04:29:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72548487-3487-397d-a0fc-6ab048a25bef | -1.47255 | -51.11921 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 749ba1d1-dde0-3c65-b3d3-83870c5b25a4 | -3.23285 | -47.47458 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12be9671-d45e-3be8-bfd4-d2de4021bb72 | -4.06435 | -46.83313 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19d059e-17b4-3312-b61a-34d519cdde0d | -3.329 | -50.25317 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb75d67f-be4e-3a28-9325-89c90283f385 | -2.28848 | -49.19176 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cff099da-0df7-3487-b593-1b3d5f91f036 | -3.39553 | -50.25789 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3db9a6a7-a24b-3b58-b7e5-a7f1652d1bd2 | -3.56758 | -49.90398 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ec09e55-100b-3d24-a67d-d25af7966663 | -2.58391 | -51.71797 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 302749ab-13ee-3714-a7be-b2777feb98f0 | -0.77444 | -51.76583 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3ee9f2-8409-3ec9-872a-0c540a55b13e | -2.61664 | -48.22058 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db03a105-3c55-3906-a591-8d984275d02d | -1.12053 | -53.39202 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 55c15ed6-60ae-3ea4-b966-ff859139169b | -2.00985 | -46.85811 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45b7c1f9-99ba-3440-a2df-7a2c721bff26 | -2.68446 | -46.24548 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0399298e-769d-34e5-8882-fce8ccf1da3b | -3.00398 | -51.30167 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5ba973a8-999f-3ffd-84cd-afedfd26ba0f | -4.24395 | -46.11708 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65c3c5ca-7831-3639-a73d-49e23519376d | -2.85283 | -46.68314 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34c0f104-5312-312e-914c-2ab7f0b6613b | -3.88904 | -46.65715 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13ca8d07-bc20-32ec-b4ff-fd0d554d6c9e | -2.7886 | -52.5546 | 2024-11-21 04:29:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a855e658-3fb9-3af5-a01d-93dd58a1c248 | -3.26688 | -50.62264 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76754168-4e54-3d18-99c7-3da2797af8e8 | -3.79636 | -46.9437 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0a5b27a-b0a5-354e-9c37-2cdc2231511a | -1.54336 | -51.22948 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc0d2de5-2789-3289-9c03-de25f3dfcea8 | -3.51648 | -50.22401 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aefdde52-12a8-3a11-9119-64bd98b31efa | -2.15306 | -50.49177 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71c49219-d376-39c5-804b-e0f79b5be50e | -3.78302 | -49.36729 | 2024-11-21 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc6d6781-e5f3-3e49-82db-ea69f10c87a7 | -2.76064 | -52.11361 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| d8e0c777-7444-3901-ad88-8f43a60b5e22 | -2.73917 | -49.16949 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef6bc07-4c4b-3838-be77-f3a6d4c3cfc4 | -2.78175 | -51.72241 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d60a17d-0931-39f3-8584-3c03b441b07d | -3.53368 | -50.44179 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f722381-23ca-392f-864f-a5d676b81785 | -4.08211 | -46.85007 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d880ff4f-af10-3545-80ec-fa4d01601eec | -2.84619 | -46.68211 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f8b6efb-a55b-3551-b9c0-939d13e58b3d | -0.95102 | -51.64302 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e9948bb-9ac3-3c3c-9a24-b9e60f9030e2 | -2.8506 | -46.67572 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a10ea3bc-2482-367e-bf44-82aaeeaa0cdc | -2.23879 | -46.82305 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d334c662-b807-3487-8a90-6e9487febb2a | -3.88794 | -46.6641 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a68914ec-6ce5-366c-a186-594c1dc4a851 | -2.65557 | -46.56005 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fad9319-f31b-38a8-ac3a-b1f33017b3d2 | -2.75247 | -48.57457 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb41229d-614f-3b2c-9e2d-4ade1e65b470 | -2.75594 | -52.11663 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a60048fa-c1ce-3fdf-8c9c-efad614b3127 | -2.43978 | -46.53364 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ae035c-1909-311f-9803-8b3db702ff31 | -1.10055 | -51.74878 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de7b266a-b95b-314d-ae0c-489a0ced9ff2 | -1.23429 | -47.35425 | 2024-11-21 04:29:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfca40fa-964e-3943-b0a0-a187b97cb3ab | -1.58937 | -50.44391 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4307ae47-c673-3897-aafd-d06968c60dbf | 0.40883 | -50.82401 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a783b52f-3c1f-3baf-afc7-cd51433817e3 | -2.61407 | -49.2529 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80df697d-56f6-3528-81ef-46c8183d7e10 | -3.49923 | -48.22672 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9496bbd-92d0-3038-8e6c-441a33b662d9 | -2.71854 | -49.34705 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36f688b9-8d55-333a-9ecd-54456caa6838 | -2.61046 | -48.21592 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f8c5715-18f9-3070-9fe0-e12082a24fbe | -2.55926 | -46.05511 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89d46bc4-b864-377b-b28f-98a83a53a6e8 | -2.65178 | -46.24043 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8004695-f903-3557-9aed-80e204031cb2 | -1.2304 | -47.35722 | 2024-11-21 04:29:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 400156ad-bfc7-3826-a5f2-1c1cc92d1f88 | -2.24689 | -49.20503 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08c021d2-0de8-3388-8fcf-0466a6b9827a | -2.76813 | -49.86898 | 2024-11-21 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f7eb90c-2e9b-3d7d-8058-0de7941d687a | -1.46165 | -52.67398 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8691e800-8cc3-39ce-b376-bb11e79eb8a5 | -2.70259 | -47.98253 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faa196a5-e593-324c-8d6c-9d9f6960e63b | -2.84683 | -53.96955 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b29b671d-30f5-3851-a70d-0f7b29ab1708 | -1.89337 | -53.33303 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbbcfbba-38b3-3f5d-9bcd-55981888fdc9 | -2.29279 | -47.48722 | 2024-11-21 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f50d37c-1944-30d8-a254-124805451bd5 | -3.10651 | -50.19866 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b43e4d79-df06-3a2e-b3d3-22fd63222eae | -2.2609 | -46.87285 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcfcf4a3-9f10-372b-8343-86caff9f47bf | -0.9201 | -52.68844 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bdfa115-f754-37d1-8a18-291c320ececb | -2.68942 | -46.23558 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2783e13-133c-3f17-91d1-60e5e7cad6a1 | -2.84117 | -51.81965 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb5379b1-eb13-3bec-8ab5-cb69d3d4233a | -3.59767 | -43.6357 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67e413d2-2a9f-3e13-81ee-550d5603c4d5 | -1.464 | -52.68704 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
