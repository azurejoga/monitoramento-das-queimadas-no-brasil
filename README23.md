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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b31bcf1-fa3a-3462-9529-c965cfe014b2 | -3.04655 | -53.01027 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56cae56f-02b7-399f-9bd2-db15d70b2b9e | -1.37555 | -55.38751 | 2025-12-12 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72dfe328-ae4c-38f6-8b05-feb941747cbc | -3.34752 | -53.07294 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764bc811-a5e1-3329-9956-19323f66a728 | -3.61059 | -55.40034 | 2025-12-12 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c8e6db2-72ab-3efb-933a-e396cb510746 | -2.65671 | -51.64304 | 2025-12-12 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02009dd5-ee03-361a-afd2-4e38eb80204a | -3.19316 | -52.91241 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ca82137-43ea-373b-8b1a-148fae37d6a9 | -2.94301 | -53.02715 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a562d678-e56c-358b-8411-2c8c680e7577 | -1.79226 | -45.76176 | 2025-12-12 05:10:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab1e0a21-669f-3d88-9a11-ed01e0903be2 | -2.66392 | -47.78303 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b28d204-078e-392d-a068-8ea3ff17daf9 | -2.77686 | -54.52687 | 2025-12-12 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10ffbb49-3ede-3f0a-a79a-8eff4a6f866b | -2.54307 | -47.79989 | 2025-12-12 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24cdb7ae-a2a0-3504-9f0b-0c02553c97aa | -2.66793 | -46.89723 | 2025-12-12 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f9d0daf-530b-3c92-ad13-35e5a91b4ff2 | -6.03033 | -43.7091 | 2025-12-12 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7bb3025b-eced-31f0-b58f-6f105eb02197 | -2.43905 | -47.19205 | 2025-12-12 05:10:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3270d46b-8814-3941-92cb-5863d686eea0 | -2.8634 | -53.03472 | 2025-12-12 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d95f5d1-7ab3-3577-bf47-989a2438437f | -2.97094 | -52.72136 | 2025-12-12 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d48ec64d-fa9f-3463-884d-8a16ab98d431 | -3.0255 | -51.86557 | 2025-12-12 05:10:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8eeda212-7e75-3db2-a507-6e6a6d2f6c6c | -1.05712 | -53.6719 | 2025-12-12 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c22bf34-0dfb-3cdc-b2af-94c3e3f3e1f6 | -4.84899 | -45.51834 | 2025-12-12 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4577c9d-b9dc-30a1-9eb3-a7756dff2d42 | -1.34349 | -54.60933 | 2025-12-12 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 891fc5d6-ffaa-3309-92ee-454e053e34b0 | 1.1283 | -60.52896 | 2025-12-12 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 331e0be5-f487-3cf7-b49b-cab1961bd9cb | -12.43165 | -58.03417 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 83c80618-b51d-3857-b615-9eb44e504e66 | -12.20892 | -49.54575 | 2025-12-12 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecaa280e-82b7-3d0c-a320-de4ae89f166e | -12.3872 | -58.03758 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8899309-5c09-32dc-ba95-097ed5e8232e | -11.88092 | -57.01373 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28cc40f3-147b-3f41-8195-9e469a1d87c0 | -12.62383 | -58.09016 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c47e9c0e-0b11-3868-bac2-48b9932ff3b5 | -12.50532 | -58.35085 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42ad1817-47bb-38c5-9d39-ba56b448372c | -12.62493 | -58.08305 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b25fe783-9537-3ba4-b786-fc8a2b2fc69d | -12.50809 | -58.35491 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11cc4086-7a2c-3d0e-8b75-23f556aba841 | -8.09885 | -55.00865 | 2025-12-12 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a91dc2f-d5fb-3cb5-a7ef-7969a720bc1a | -12.63213 | -58.08055 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09229eea-4bb9-34fd-8bd6-83a9b36f50a3 | -12.63268 | -58.077 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32edc11e-289e-3b47-a566-3f319e6500f3 | -10.23731 | -52.22613 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e00ed4c-652a-3577-8429-0984b692b4a1 | -12.29924 | -57.37194 | 2025-12-12 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0bf5395-e453-31d3-9fb2-d1b9868a7d8a | -10.73764 | -52.44146 | 2025-12-12 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f0e1ca-24ec-36b3-8588-5a8f1af21d10 | -11.95476 | -58.76296 | 2025-12-12 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fcd23a7-a89d-3936-bb23-55b09be04e8b | -12.39386 | -58.03865 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 261edfb1-2706-3fae-af17-1f6be072d5f6 | -12.62548 | -58.0795 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a162ebbe-64e0-3e2d-adfb-9fadb62546f5 | -11.87697 | -57.01692 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a74d1567-60e7-3a68-ad39-9b674c5cbc5f | -12.2036 | -49.54505 | 2025-12-12 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16f82781-16df-303f-900d-47c3f6949bdf | -12.3944 | -58.03509 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f922488-146e-30a9-b33a-4d5767dead02 | -10.24043 | -52.2204 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f60ed00-edad-345c-8e2e-377ff465d753 | -8.09894 | -55.00994 | 2025-12-12 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f0b04d1-c1c3-3466-9ff9-29e7444075cb | -12.41381 | -58.04183 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9f638c3-769f-35c8-b338-eb3448706aaa | -10.23987 | -52.22459 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7971e560-2abc-3ae3-bd62-84269db63611 | -12.51526 | -58.35244 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f63052-92e1-306d-b6bb-35002c8a07e9 | -7.56613 | -55.35082 | 2025-12-12 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45236246-7428-3a41-8382-feeb2ca2b340 | -11.88036 | -57.01744 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77b9e2db-6a6b-36b9-9736-6558d8b66ea0 | -12.90613 | -52.51619 | 2025-12-12 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb11053b-c53b-3415-8a77-fce3984e003b | -12.41326 | -58.04538 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae84fcf7-42b4-3563-8f1c-aaf08b9c16b3 | -12.51472 | -58.35598 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67001e28-b399-3608-84a6-e5f5e89cc4ad | -11.01065 | -59.05609 | 2025-12-12 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13f5d336-465b-3771-ab41-89775ae4f48f | -12.62881 | -58.08001 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7e6f82c-b7ef-338e-bb95-29275968ad98 | -10.98916 | -53.99964 | 2025-12-12 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e405719-e52e-3c36-b720-4ef982e69e6e | -11.32354 | -49.19606 | 2025-12-12 05:12:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef1083ef-c057-3b74-a74c-120079226450 | -12.40438 | -58.03669 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f413a441-4bed-3ddc-a476-b7261fd8b7a2 | -12.51363 | -58.36303 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7819d4cc-7d34-30c2-b031-3f67a17cb95e | -12.40993 | -58.04485 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c24eba6c-644b-30b1-81bb-837b33178373 | -11.87753 | -57.0132 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dabf8860-659e-318d-895d-6446f9b34432 | -12.51636 | -58.34538 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6981e47-9843-3992-82f9-4025ed922300 | -11.31814 | -49.19547 | 2025-12-12 05:12:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d7a77a-f56c-3cde-ad6b-c0c8eb36fadf | -10.73707 | -52.4455 | 2025-12-12 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a346510-65d5-3502-84b4-a292262c98ab | -12.39053 | -58.03811 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dca2eb2-e507-3fd6-993d-b6e5178c4c02 | -12.89735 | -52.51498 | 2025-12-12 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12630ccd-90f3-3917-adba-87b35a9891c7 | -10.74057 | -52.44392 | 2025-12-12 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541bfe20-0e52-3cf8-9a64-ba0fce36d923 | -12.62771 | -58.08712 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b03d6af1-b2af-38af-aec8-53ee4f294461 | -8.09826 | -55.01271 | 2025-12-12 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2203c879-7910-348f-9219-784a458d6480 | -12.50754 | -58.35844 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17e41667-c073-37b9-a3de-4eaadae9d69d | -12.39773 | -58.03563 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e11bac15-cec5-39b6-b9cb-34b3c6d9d1e3 | -10.73629 | -52.44331 | 2025-12-12 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eff2ab1-7966-365e-97fe-a0daf23d0825 | -12.5114 | -58.35545 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20127d45-c8c3-39ab-8b63-293c545c9319 | -12.41158 | -58.03419 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57f9ece4-a880-3e13-8088-6ff3fc1d8453 | -12.2032 | -49.54839 | 2025-12-12 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81dd6853-b723-397a-bb29-8cd208d1608a | -12.41713 | -58.04236 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 712a182e-a6d7-3116-a5c8-7078159a7ca7 | -12.25428 | -58.30327 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafc8ec9-e3c3-390c-909f-948de0579f23 | -12.39108 | -58.03456 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d982b287-ce18-32ef-b629-6b8b8e781967 | -12.62826 | -58.08357 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 418f4827-a259-37f2-92d1-727fbcac4559 | -12.38388 | -58.03704 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a0b7dfa-bb48-30f8-bdc1-14c2e6ea333e | -12.51195 | -58.35192 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06cc1328-870d-30c0-9efc-6182dc428b21 | -12.39718 | -58.03918 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3be30fd-668c-301d-a57b-f22d448a1905 | -10.23612 | -52.21978 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5537b2b-20a8-3b57-8c4c-7cad1ca2926f | -8.10249 | -55.01047 | 2025-12-12 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5df09140-c7f7-3b50-8ab0-ba8f5f35c283 | -12.51086 | -58.35897 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7315bebc-3e0e-3725-8309-f814a8399a7c | -12.51581 | -58.34892 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9776f043-f440-3b99-bff6-feecea8bf78d | -12.38775 | -58.03403 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e3463ad-22b5-3465-a570-0a11ed57c6e9 | -12.62438 | -58.08661 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6981fa2-2b5e-348e-910c-f27ad3802ed0 | -12.41103 | -58.03775 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0777bc7-1887-3b85-b505-71a32ccf9551 | -10.98597 | -53.99416 | 2025-12-12 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8214441-af99-3b46-881d-146302a2078a | -11.02767 | -50.52805 | 2025-12-12 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cc697fbe-3fc5-3177-9357-d1d3e862c239 | -12.51417 | -58.3595 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a294048b-f65f-3818-aab2-888e72846fa7 | -13.28531 | -55.97662 | 2025-12-12 05:12:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f68a00a9-9356-3a7c-9f7e-b542da43f12c | -10.23557 | -52.22395 | 2025-12-12 05:12:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab6ea0ac-2b53-3ded-a29c-7c5871ae61ea | -10.88837 | -54.14227 | 2025-12-12 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5352c4df-3f79-3e29-8555-84df214f8089 | -12.43497 | -58.03471 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 46665f72-48b3-34b1-a8f9-b44ee157edaf | -11.80738 | -56.96508 | 2025-12-12 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edf06734-1504-347e-b5a3-00b6286c8788 | -12.25483 | -58.29974 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 811f509c-b92b-335d-b632-2dc13521e475 | -12.20852 | -49.54908 | 2025-12-12 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5fa902d-18b8-374f-807c-07d4c174efdf | -10.7328 | -52.44485 | 2025-12-12 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e95c90-21d1-33d1-8780-1d6301d63290 | -12.43443 | -58.03826 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 42788b56-74b9-36ba-8233-ff132635144f | -12.502 | -58.35032 | 2025-12-12 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README24.md)
