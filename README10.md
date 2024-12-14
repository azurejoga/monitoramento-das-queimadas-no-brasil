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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a950a35-9087-3606-9a94-cca22ebaa9a8 | -4.66891 | -44.03951 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53130521-9083-3ee7-833c-b88a219468d7 | -5.50915 | -45.49012 | 2024-12-14 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67a5dff6-e26f-3be6-8dcd-2e56e0515145 | -5.05226 | -42.61639 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a28703e4-5449-342b-bd88-3731d92768ee | -6.73436 | -42.53294 | 2024-12-14 04:25:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aed26f83-6193-3280-8a5f-d1ee19d0863f | -12.56606 | -57.75913 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| da4f8c3f-a751-3997-b76d-d6273ee2abce | -4.41075 | -45.82284 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbbd4d36-878f-31e1-8ca8-ee6672528269 | -3.98634 | -46.89311 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0820492c-2c3d-316d-b6cc-11838a94e0f8 | -11.49696 | -52.91026 | 2024-12-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cf016a9-f503-37fe-8a31-ec734d175ddd | -4.0453 | -46.67355 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1506625f-83b9-3af7-a59d-c7307142d895 | -12.54482 | -57.71888 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e0517d61-eb3c-37cc-bcd0-0cf255f1d28d | -11.49426 | -52.92559 | 2024-12-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff7f3e38-7a7b-3d99-be62-690aeed538e0 | -6.51929 | -41.28022 | 2024-12-14 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4ad626a-03f8-374e-9a0b-f37cadde804b | -6.52327 | -41.28084 | 2024-12-14 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6019f3e3-9c8a-34a6-92b9-d4404baa9251 | -4.41905 | -45.83472 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 024b0649-3f73-3a18-af7f-65a7af22f425 | -13.64141 | -48.4486 | 2024-12-14 04:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9e18dc2-7b50-3292-a717-da6befd0fffa | -11.82601 | -57.82953 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 461568aa-fa98-335d-9b56-98052fd77670 | -4.10209 | -46.61762 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cd3e1a28-d63b-3a10-a62c-a7eb64b0defc | -4.07483 | -46.7253 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40da1daf-44ba-3a7b-93f9-6df9838ca409 | -12.99082 | -54.15052 | 2024-12-14 04:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f55415b5-4b7f-37e3-ae9d-b2ba56015864 | -14.69204 | -52.63068 | 2024-12-14 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e97fcb6-0e1d-373d-b543-b9ea53f6f9c9 | -4.41737 | -45.82387 | 2024-12-14 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98fdfe7f-fd23-3dca-9350-ef3840ae508b | -4.40636 | -45.82921 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9376fe77-eac3-3954-a333-00c98d6dfa81 | -14.97134 | -44.41022 | 2024-12-14 04:25:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a98a3b3-08bf-3b77-93f7-473b8ea27876 | -12.55268 | -57.70845 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3608bcd2-9923-32d9-88d7-99fee3506119 | -4.02666 | -46.89951 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdcaff77-11c1-37a6-8d37-ed19b69a8d74 | -11.82756 | -57.82142 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7f5d6e5-c360-3085-a6c6-02f5790dd2f5 | -4.41021 | -45.82628 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e22b7ab4-94cd-33fe-b5b6-135e2b9ae2db | -4.41243 | -45.83369 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1b8463e-de0a-3ae5-b8e9-cc8ced543f57 | -6.04476 | -44.042 | 2024-12-14 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3df685de-d9eb-3fdc-ac67-3b4de3c555ad | -12.56457 | -57.76675 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74102078-cbb4-3bcb-a93d-418bc47ad966 | -6.09801 | -44.76233 | 2024-12-14 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd6a9c3b-e163-3c13-9a82-cc853596e25e | -5.04165 | -43.21484 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 020e6477-70fc-3f3a-8ae9-84fb1ab0fb9b | -13.53627 | -55.38454 | 2024-12-14 04:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc8ce486-73b6-3be4-8e30-da3beb2b57af | -13.17365 | -53.28596 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f50ed3da-83d9-3b80-b735-424d63db9a4d | -4.0997 | -46.67096 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24d8fe07-e9a6-3fe2-90d2-e6c8825a964b | -4.4229 | -45.83179 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90b042bf-ff20-3d47-90f9-02a0dac940db | -6.51029 | -41.28589 | 2024-12-14 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65710881-a88a-3491-8cec-ed08de422579 | -11.78294 | -55.13278 | 2024-12-14 04:25:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82d6b52f-1b03-3490-97af-33ead0d97d66 | -4.00831 | -46.54522 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4081c01-efa2-328c-9d04-fb8d57711747 | -4.40528 | -45.8361 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f5a8bc-8355-322c-8448-1acb8725b74d | -4.71908 | -43.19615 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 629dfd40-4479-395a-91a2-7a050ccbaff3 | -4.07817 | -46.66074 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 896ab6d4-daf5-3d0a-af20-8a4551573b7d | -4.40414 | -45.8218 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acf68fe9-dadd-39cd-bc27-4fa816e4f6ba | -17.96435 | -44.57606 | 2024-12-14 04:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a92b25b-0402-332c-9f3c-b800fd659412 | -4.09686 | -46.71019 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d55e68b-41db-3684-be8a-91dda1226f5f | -4.66022 | -43.82378 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 904c25b3-53d9-326a-b7de-05eaa7fd289e | -14.82958 | -52.87604 | 2024-12-14 04:25:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3ac6cae-72b5-3fbb-9428-4a3fa63d9082 | -5.05474 | -42.61817 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e80def78-b005-3550-8105-c80c223e1802 | -13.16951 | -53.28518 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7339d026-b851-3c9c-a89a-a63612930ce0 | -5.94307 | -43.77276 | 2024-12-14 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6edcfc54-ecdb-3101-85a7-de5b46e355bc | -4.10264 | -46.6141 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 45e7a004-7efb-3798-a404-0b9a2239d275 | -13.64531 | -48.44558 | 2024-12-14 04:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d6ec665-4620-37b5-a340-e16203ff5ce8 | -4.41628 | -45.83076 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1ad8a288-6da6-349e-9d92-4c3b8eaa0ebd | -5.26491 | -41.39077 | 2024-12-14 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a8d264cc-f34c-3b85-8bbd-365b1c9f4ca1 | -6.92162 | -35.71704 | 2024-12-14 04:25:00 | NOAA-20 | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc45e11d-df88-318e-8faf-de720751faa9 | -3.57998 | -51.04975 | 2024-12-14 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b483130f-9fce-33e5-9faa-ba3bb8ceffef | -11.82108 | -57.82434 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c986d94d-9ad7-3b74-bff8-7c198aa513f5 | -4.09432 | -46.66693 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30fae95-d2a0-37b9-b4dd-5310b528b8d5 | -4.4152 | -45.83765 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d30bb05e-278a-3847-8d13-0a81e0900a75 | -13.17297 | -53.28977 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0fa0b72-65bc-32ca-9efe-74f42b0bfe1e | -4.71848 | -43.20005 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73d6b509-80b1-309c-8264-4ac1d2c796b3 | -4.80663 | -43.30803 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2db2c328-7c29-3f02-99c5-1468b622c82a | -3.58059 | -51.04598 | 2024-12-14 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0c63462-be0d-3a61-ae52-7d06e411f06c | -5.53842 | -42.8541 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78626e50-710c-3d63-bbed-3a3943d83cf5 | -4.09656 | -46.67445 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a5e8cd-c7ae-32fe-8da8-6b5560cdfca6 | -5.6489 | -37.259 | 2024-12-14 04:25:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd2e4230-3615-3fe1-bf27-4b64e8842316 | -14.8442 | -53.67325 | 2024-12-14 04:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dfa155c-2d0b-3f66-a904-01d2cc2c9568 | -5.53716 | -42.86227 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52a70474-95df-32bb-b083-915706811fab | -5.96496 | -40.44563 | 2024-12-14 04:25:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4810c19a-14f4-3720-b9f4-614893bf6457 | -4.30097 | -47.88688 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03d17668-03bd-35e1-876d-7d4d0b0504de | -16.91932 | -43.59825 | 2024-12-14 04:25:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77c05b16-c9ed-3819-b3cf-7648a614f159 | -4.41135 | -45.84058 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b616be62-dbc4-3ef2-b077-e5ea53c36ab1 | -4.65396 | -43.81951 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3079eadd-2b75-3e2d-af27-5d9fef3301e9 | -4.13695 | -46.11596 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15d19ff8-15de-33d1-9075-21099634d8a8 | -4.23064 | -46.78914 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03827f18-8bfa-3d53-938a-af55e34e47c2 | -6.62115 | -39.17922 | 2024-12-14 04:25:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c27152b-0f1f-38e5-be7d-4ff66d373c75 | -11.49629 | -52.91408 | 2024-12-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c7af05c-b2a0-39a6-8225-1b96823c7a2c | -4.66495 | -44.04264 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c76c71d-3afa-348c-bee9-9acc55b82167 | -4.4742 | -43.87184 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43a4d86a-2229-3f14-846a-b9586f610d2b | -14.95873 | -46.90153 | 2024-12-14 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23ba1aed-2b1f-3815-8ccc-3789bb6211bd | -17.15784 | -53.43178 | 2024-12-14 04:27:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7874401c-359d-3d3b-b8f9-7a1f6a7979d8 | -20.41496 | -43.55222 | 2024-12-14 04:27:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 679944e7-d7bd-349e-bb8e-fae00b24ce34 | -4.1057 | -46.6142 | 2024-12-14 04:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7f04e100-ffda-3860-b8dc-063a6901434f | -12.5499 | -57.6996 | 2024-12-14 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| da8afb9d-21d9-3ca0-8d1f-2e98aa5df5d5 | -12.5682 | -57.7579 | 2024-12-14 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 19cd9adc-aba3-33aa-8678-c8608a782b0d | -12.5497 | -57.7196 | 2024-12-14 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 83e53a64-e8d5-3512-abef-25330601b3bb | -4.1057 | -46.6142 | 2024-12-14 04:40:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f5db6c3b-90de-3eaa-a70d-e0ade9528867 | -12.5497 | -57.7196 | 2024-12-14 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 90f02f41-dc84-3212-80d9-3820724bd4df | -12.5499 | -57.6996 | 2024-12-14 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c27307ec-7f90-3a10-a4b6-ba5266cdf2b8 | -12.5497 | -57.7196 | 2024-12-14 04:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3701d269-7f6c-3189-944f-0dd15a70229a | -4.1696 | -42.4346 | 2024-12-14 04:50:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| b51bfeb3-e857-3685-a7b5-b4cc4e32d693 | -2.58115 | -51.92169 | 2024-12-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a90b35-5881-34ca-bedf-98709b32429f | 2.73996 | -60.38284 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 912ec126-cbfe-3652-b520-30a388255b85 | 3.20262 | -60.26788 | 2024-12-14 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46cbda48-367c-3ecc-ba48-8ae38de6e757 | -1.71483 | -52.56469 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f85a603-6e89-3100-8ee7-5d6dd5cda98a | -1.81556 | -52.72676 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d740debd-cc37-3c70-9f25-03619e6348b9 | 2.52591 | -60.64734 | 2024-12-14 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47fe274a-a6f3-3651-9f8f-bc8eef5a293e | -1.72015 | -52.5577 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3f4b3ac4-43bd-310a-a059-8c6aab4a1d05 | -1.81651 | -52.69248 | 2024-12-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88cdbd85-1a15-3123-a851-6fb79339ca39 | -2.67926 | -53.07692 | 2024-12-14 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
