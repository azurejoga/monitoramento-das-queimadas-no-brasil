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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e91b4da-4a35-3084-8d63-b200f2d387f8 | -3.34345 | -50.19999 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7308d80b-4121-3380-a188-d085b1576e45 | -4.73681 | -45.71224 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0256815f-74a4-35e3-af2d-e6806b762174 | -4.50056 | -43.85615 | 2025-11-08 04:06:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de47e400-3063-39a3-9d7b-62c3eeae6c02 | -3.69005 | -52.13527 | 2025-11-08 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed6c54de-142c-3022-92d0-94adc1f51f33 | -7.27429 | -40.95679 | 2025-11-08 04:06:00 | NOAA-21 | VILA NOVA DO PIAUÍ | PIAUÍ | Brasil | 2211605 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dedc4349-6ba4-39a7-b0c3-f80678ae6d96 | -3.83684 | -49.81641 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5bc3d6c-732b-385a-952b-cef84584fe28 | -4.28666 | -45.88718 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7839c430-56a5-3460-8cfe-5888bba956fd | -5.84496 | -43.41299 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d5e5b964-7509-3e2e-a7b0-5cdf91465e24 | -4.35667 | -45.8452 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e81a559-aaef-3577-826c-c411c6cd8b9e | -5.91358 | -44.52511 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 96c926aa-6cd6-3ed4-bf5a-5b513eb80cc9 | -4.59607 | -45.9962 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 06a1a820-8673-3d53-819a-6af4b9d085f6 | -4.75705 | -45.78109 | 2025-11-08 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c893450-e26f-3297-b262-5cd46bcfbe02 | -4.32972 | -45.98527 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c25560c-8a5c-343b-bc75-09450291bd20 | -7.5488 | -41.65974 | 2025-11-08 04:06:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4fb23e3b-4ef1-302b-8b1d-8cf8b477d12d | -6.65538 | -44.48844 | 2025-11-08 04:06:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e8b79c3-32f1-334e-b5fc-33e02532cbf6 | -3.84559 | -45.8525 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 315dd97f-bcaa-3896-bb5b-4d69a04cac56 | -5.43448 | -41.5607 | 2025-11-08 04:06:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c2e437a-5918-3133-b957-cd054c0e72e2 | -3.76436 | -43.04346 | 2025-11-08 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 937b0c01-32d7-3930-b9cf-ba5e5d16c7b2 | -5.75196 | -40.79158 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00b9273e-080b-31de-b777-f97788c98816 | -4.71128 | -45.8965 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fada2c4-c8c1-302c-a0cc-bdec6684d99e | -5.42816 | -44.6276 | 2025-11-08 04:06:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fd4b8d0-db89-395f-b6ab-827cd7f34f1c | -4.4773 | -45.33214 | 2025-11-08 04:06:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a2241d9-04fe-359f-90c7-6d6ca972a723 | -3.15104 | -50.29602 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2b5d1e-b29a-3a84-b19d-30883b2081d1 | -7.3854 | -43.53222 | 2025-11-08 04:06:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f068533f-da99-3cc0-9abf-33a26365b8c1 | -3.59473 | -51.23441 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f8e234b-17bc-3579-846d-c8de41ac59e3 | -5.83172 | -43.27575 | 2025-11-08 04:06:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d42024d-d3a7-374d-8a66-cc1faea6dff2 | -7.58943 | -42.31023 | 2025-11-08 04:06:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1b0dae6d-7792-3367-bec2-a818ff8f9cd6 | -3.15002 | -50.61001 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07b8934b-d01c-3b37-98cd-6ed76f0e24f3 | -3.91568 | -50.04323 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bce2ad7-63d7-32ba-8ba4-9d4076ee9ec2 | -6.48599 | -48.36812 | 2025-11-08 04:06:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0131514-d9ba-395a-ad5d-f43844701d63 | -6.33518 | -41.69623 | 2025-11-08 04:06:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92d9a124-dbd9-306a-8636-52fa88b5a382 | -3.31656 | -49.12811 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00ef0247-9427-3693-8ab0-aed3a4a3cbd9 | -3.31589 | -50.1244 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdfc9177-fa11-384b-972e-a05a70f505ec | -3.78096 | -45.84224 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e6905ee-b296-33d9-ae9e-ecb1f5cb6c9c | -5.04111 | -45.92224 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 445af6b8-bcb5-3443-bfc0-2238e2d95143 | -5.23379 | -45.53066 | 2025-11-08 04:06:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4ec76f7e-f8b1-3472-b6a8-27b4b7bf8b13 | -5.94998 | -46.6515 | 2025-11-08 04:06:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4e3b332-23ff-3049-bf71-a0bb80a38c18 | -3.43611 | -45.59452 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ce37466-d264-3582-afdf-5d222f2cc522 | -5.09894 | -43.99187 | 2025-11-08 04:06:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dc23079-9e40-36d1-b03d-52f9dfee3c98 | -3.43667 | -45.59106 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a585040-d0ac-3e79-85f8-b18cf0dded3a | -5.93773 | -38.19136 | 2025-11-08 04:06:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4b296810-df95-32b8-b9a8-6be8f7e08b0e | -3.8335 | -43.35494 | 2025-11-08 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa2119c8-2e34-31f4-98e7-1f3d66d2bd7c | -3.41263 | -45.43707 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5fcad906-6a8d-3a47-ae6a-7c3ffb40628d | -4.47184 | -43.21506 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc7292d2-f442-38df-998e-6c96e547a378 | -4.2855 | -45.89444 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e81bb85-455d-3d09-9195-1a112a254452 | -4.28088 | -46.41493 | 2025-11-08 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4a79f73-3376-327b-8539-3d7aa41dcb82 | -3.43325 | -51.52361 | 2025-11-08 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7d12277-fccf-3345-999e-084e0ace6c81 | -3.24416 | -48.76202 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f682b4-b76a-30e8-8ed8-2fffeadad166 | -3.44898 | -46.19035 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 681f3a50-6912-37e1-9fad-21657deee385 | -5.08327 | -45.10193 | 2025-11-08 04:06:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48f4cf76-30b6-35f5-8e4f-de0663503c10 | -4.59205 | -45.99549 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 7d73f773-454d-37b5-a795-3fb089f86a76 | -5.23374 | -42.79963 | 2025-11-08 04:06:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40969aa5-4253-37e2-a3bf-acccbfa85b90 | -6.10454 | -42.68458 | 2025-11-08 04:06:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5539cc2e-e572-3fc6-afd7-3a93d7a155b6 | -4.53138 | -41.91241 | 2025-11-08 04:06:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7dd14682-d6e1-3e03-8ed7-041e07b982b7 | -3.15165 | -50.29242 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a7538ca-b769-332d-9de1-c10bb107f6b1 | -3.65353 | -50.2724 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 66924c13-739f-3193-9679-bbfe3738a3cf | -3.34666 | -50.20946 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| aa9e22a7-8ce3-3ffb-82ba-0d93d9439ae8 | -3.32064 | -49.13489 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f4ad707-7a2a-3264-a0f6-18cad3305004 | -5.49883 | -40.77984 | 2025-11-08 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| f69d0a59-ec4d-307c-97f2-51aabbab271f | -3.52859 | -47.53856 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90274470-4fcb-3902-9628-9d9d65404527 | -3.45335 | -48.83543 | 2025-11-08 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3b22880-9f29-3b75-b657-c347e55b472f | -3.94729 | -49.02263 | 2025-11-08 04:06:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eace7c43-5131-3636-b856-adafde45701a | -3.1011 | -50.32534 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e520d628-f3de-32ed-8c2b-563623223f94 | -4.59664 | -45.99277 | 2025-11-08 04:06:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b079bfa-e507-3eab-ab13-377264dfaa67 | -3.15067 | -50.60611 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 852988ca-3d86-3b77-8ea8-9e63752c008c | -7.42041 | -35.18034 | 2025-11-08 04:06:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5bf9fa9c-1c7e-37c5-a0cd-da893bcf75a1 | -2.79186 | -50.31208 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94090a4a-2b33-3baf-ac11-7077b8aab603 | -3.35156 | -50.21388 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5fcac323-d241-3d7f-90d4-4c03f7112cf8 | -6.63811 | -44.54951 | 2025-11-08 04:06:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08ef6fff-bb9e-390f-8cdc-caf01459c473 | -5.67791 | -40.85432 | 2025-11-08 04:06:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2afadb64-5f0d-3eaa-a56b-eb3f1a037da9 | -5.5881 | -39.59217 | 2025-11-08 04:06:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4203f702-b50f-3bd2-9e1d-a3e31b75c4d0 | -5.10251 | -43.99242 | 2025-11-08 04:06:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5344b11-1887-355e-8410-4fd82bcb8e69 | -3.83737 | -49.81322 | 2025-11-08 04:06:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3c6124b-d4fc-3881-bb7d-9bd716b4dcd2 | -3.46632 | -48.97481 | 2025-11-08 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2360973-1451-3e90-b7a8-d41d788244c3 | -3.14552 | -50.29511 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84651f91-cee1-37b4-b317-17c4a8a7f63d | -3.40159 | -45.43013 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26f4ab28-48b0-3e4b-b2aa-9d2222d92a70 | -3.43722 | -45.5876 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192e98f6-7094-38e1-a1e3-0e46d73797f4 | -4.60546 | -41.72349 | 2025-11-08 04:06:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8cb9d0ab-9aa4-3a8b-8b94-fa490e28f1b5 | -3.14939 | -49.21233 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 258f8087-f680-39af-8d01-68fa33ca2d93 | -4.40485 | -42.32811 | 2025-11-08 04:06:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf57f423-9862-3cb5-aaea-c02cc44b516a | -3.48489 | -46.11503 | 2025-11-08 04:06:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddd317a4-9e98-3e05-a5f3-6036e60c8436 | -4.46145 | -43.21343 | 2025-11-08 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030ed057-1cb0-3f05-8ece-9380ac86e5d4 | -3.11926 | -50.14671 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9a01009-94eb-3157-8b40-29a9874ef966 | -5.77613 | -40.79194 | 2025-11-08 04:06:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| afbc1987-b91a-3489-8f7a-07106067ff28 | -5.97686 | -44.17505 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb509006-95fd-34ce-99be-e41d69d88386 | -3.36411 | -49.51459 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cc34ad0-1b83-3e9b-89a5-486e52980a5c | -3.35056 | -53.22856 | 2025-11-08 04:06:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d850ab41-1055-3a91-a4ad-eba604050fba | -5.00938 | -45.81636 | 2025-11-08 04:06:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9f66ae-c83e-3791-9da7-821c6db41381 | -3.40867 | -45.43642 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5d2058cf-dc59-30ad-8a81-214f464f687d | -3.65483 | -50.27073 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d12ddae7-3898-38f5-8e39-f36c0dfee030 | -3.91965 | -51.01163 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cfe03243-1e9d-328b-98fd-0aec33c94a20 | -7.53446 | -39.24828 | 2025-11-08 04:06:00 | NOAA-21 | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbbab9df-27e6-3aee-9a26-b20e9664eb18 | -5.88312 | -43.92197 | 2025-11-08 04:06:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d221bf-5952-3abc-8ef2-61d52b6b5b5b | -2.71094 | -49.54725 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d3cf08b3-0a82-3331-b0a7-7b25810d0094 | -5.98042 | -44.17563 | 2025-11-08 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fab90672-7d30-3dd1-935e-c81d488a522d | -3.65545 | -50.26715 | 2025-11-08 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0ae9b082-9157-32d9-9a08-64be4c777f14 | -3.36466 | -49.51141 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03072047-9a07-370e-a32f-cd026cef4ae9 | -3.84155 | -45.85187 | 2025-11-08 04:06:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 418a621c-c2d1-32e7-b17f-a309d95f1b09 | -3.11985 | -50.14312 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71da02cb-70e3-3403-b0db-0f1718e6867d | -6.04997 | -39.14462 | 2025-11-08 04:06:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README10.md)
