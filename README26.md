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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1769e284-dcad-361c-9786-233e133d8658 | -11.4393 | -45.1154 | 2025-07-15 06:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7a6ec47a-d1a1-37a0-852c-13745be6e794 | -11.478 | -45.0868 | 2025-07-15 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 7880642e-798a-3997-891f-059f1494ca07 | -11.4588 | -45.0895 | 2025-07-15 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 3bbe02c4-4329-3fdf-8381-a0097a37817a | -11.4584 | -45.1126 | 2025-07-15 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f1df0fe7-dbeb-3ba8-ae67-2353277c08a9 | -11.4397 | -45.0923 | 2025-07-15 06:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 875b2c96-e73d-37f7-884e-48019dffcb02 | -10.5586 | -49.1337 | 2025-07-15 06:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 8dd7aeab-3762-36aa-8c6b-a1613fb78fbf | -11.4588 | -45.0895 | 2025-07-15 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 92d9eff8-e43b-36b9-85f3-1619a72bac1f | -11.478 | -45.0868 | 2025-07-15 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 27215e93-bcf2-3242-8dae-96e8237890dd | -11.4397 | -45.0923 | 2025-07-15 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 73aa0ade-47f1-34b4-a39c-f21f326902ff | -11.4393 | -45.1154 | 2025-07-15 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| e752275e-9b70-30af-a335-15f026cb5ce1 | -11.4584 | -45.1126 | 2025-07-15 07:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cfe09f1d-f7b9-3500-846c-5dd65057ca6c | -11.4588 | -45.0895 | 2025-07-15 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 47826618-4ee4-36f5-af69-419b6848357b | -11.4584 | -45.1126 | 2025-07-15 07:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dee4595f-fa22-302a-a710-d2e56db41c8f | -11.4588 | -45.0895 | 2025-07-15 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 1efc7f9b-cdc8-317a-9bfc-ed1cbe32a338 | -10.5586 | -49.1337 | 2025-07-15 07:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 2f15e1d8-cac3-33e1-a68b-e869b092b6cc | -11.478 | -45.0868 | 2025-07-15 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ef80789d-019b-3b8e-8b77-e40ba9f25ad2 | -11.4397 | -45.0923 | 2025-07-15 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c973e7a1-eb67-31c0-9fcd-5db7b7001d5d | -11.4584 | -45.1126 | 2025-07-15 07:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3f217c46-f10a-3699-bc8c-620015457b53 | -11.4588 | -45.0895 | 2025-07-15 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5712aa98-139c-34bc-b6c1-ee830355e15d | -11.4397 | -45.0923 | 2025-07-15 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| a7417fbf-6046-34e0-b14a-8d3ad2d0527a | -11.4584 | -45.1126 | 2025-07-15 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d182f0c7-3a51-39f3-95d6-d468738a0fca | -11.478 | -45.0868 | 2025-07-15 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 65265cec-ddb1-3d13-8c50-9b363b69b0a2 | -16.2368 | -49.9673 | 2025-07-15 07:40:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 144.2 |
| a2906a8b-2d53-3d86-8455-3d935d1215e7 | -16.2171 | -49.9705 | 2025-07-15 07:40:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 2fc48f03-ec80-32c4-9737-728492552b15 | -11.4397 | -45.0923 | 2025-07-15 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 31813b12-d61a-3e7a-a872-596ea543817a | -12.8813 | -49.1758 | 2025-07-15 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1a073385-541c-301b-8873-50ae4e9a3a11 | -16.2372 | -49.9452 | 2025-07-15 07:40:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e96df3f4-3fec-30fd-858b-bb3f7c866539 | -11.4588 | -45.0895 | 2025-07-15 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| c8c24dcb-06ef-3728-b278-d2cf9083fc70 | -16.2176 | -49.9484 | 2025-07-15 07:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9a1f6208-1899-3ff9-b7a6-7813086414d0 | -12.8809 | -49.1977 | 2025-07-15 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c38d90c8-04dc-3ed2-90f2-5f879631efb8 | -11.4584 | -45.1126 | 2025-07-15 07:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d8deb4f5-f5c3-3900-b306-65285473cd90 | -11.4588 | -45.0895 | 2025-07-15 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| e1bebea0-78be-36a2-a495-8d5aa0cc564d | -12.8813 | -49.1758 | 2025-07-15 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 8365c032-01b0-3c79-8037-6e3ea11ea70e | -11.4584 | -45.1126 | 2025-07-15 07:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 76e62d51-17c9-3e24-89ef-dd5e11a885fa | -12.8809 | -49.1977 | 2025-07-15 07:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7dc971e3-ffe0-3274-a3e5-cbefc6c8510d | -12.8809 | -49.1977 | 2025-07-15 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| b0d579dc-88cb-38bd-a450-6acb854fff91 | -12.8813 | -49.1758 | 2025-07-15 08:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| bb3b04c7-58a1-3742-85c5-fe5faed56ce6 | -11.4584 | -45.1126 | 2025-07-15 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b5fc7ed8-0bd8-36d7-ab8b-59ac5476ab2f | -11.4588 | -45.0895 | 2025-07-15 08:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 3cda2a7a-f6b0-3412-87a4-b4f5541bb756 | -12.8809 | -49.1977 | 2025-07-15 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c9846ccb-d3ff-34fc-9d9a-8b28528ee7cb | -11.4584 | -45.1126 | 2025-07-15 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 426b5095-b368-3764-a50b-a9ebbd08ca3c | -11.4588 | -45.0895 | 2025-07-15 08:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 06554b4b-02fe-3a11-aaa9-b050c127a9a3 | -12.8813 | -49.1758 | 2025-07-15 08:10:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| eac53950-1d1a-32ee-a8c1-4e1486809bf0 | -12.8813 | -49.1758 | 2025-07-15 08:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9c6a192d-242c-37fd-a677-eed6a7a9f272 | -11.4584 | -45.1126 | 2025-07-15 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| cb4f0dd3-8cd2-3d6b-8631-ba268555c5de | -12.8809 | -49.1977 | 2025-07-15 08:20:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e927bd16-f3d1-302a-aa72-1916708dd248 | -11.4588 | -45.0895 | 2025-07-15 08:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 12263991-e2b6-3892-860b-bcdbcd0f5f3b | -11.4588 | -45.0895 | 2025-07-15 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 410adc83-0b93-34b3-84f6-c49a8adb3e75 | -12.8813 | -49.1758 | 2025-07-15 08:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c918ebe9-60e4-3b93-8a4b-d3b8e2fb61d7 | -12.8809 | -49.1977 | 2025-07-15 08:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7eaf00df-12ad-3d3f-8aec-68360b1c1833 | -11.4584 | -45.1126 | 2025-07-15 08:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0c86470a-d24d-3d26-89c0-90f2f76f8f9a | -12.8813 | -49.1758 | 2025-07-15 08:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d9da6812-7a81-36e1-9d9b-d859af4a245c | -11.4588 | -45.0895 | 2025-07-15 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 32e510b0-9f02-3851-8c89-3e461c58b6d7 | -11.4584 | -45.1126 | 2025-07-15 08:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| d9b170c2-f1b1-3030-8b26-fbc7bb371552 | -12.8809 | -49.1977 | 2025-07-15 08:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 53df3c44-ba35-3947-849a-5461c39fe9c3 | -12.8813 | -49.1758 | 2025-07-15 08:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 2766a2ea-79f1-36b3-bb79-185112a8e169 | -12.8809 | -49.1977 | 2025-07-15 08:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2f87c5a7-1dee-308d-b1ef-40cefdce4918 | -12.8813 | -49.1758 | 2025-07-15 09:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cdcf0999-b9f6-36b2-ab74-2b9290cc4976 | -12.8809 | -49.1977 | 2025-07-15 09:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f0ef4edd-641f-31d8-aff0-1b51aaccfbe0 | -11.4588 | -45.0895 | 2025-07-15 09:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| a40961df-6973-38b8-8110-d29009d85fdd | -12.8813 | -49.1758 | 2025-07-15 09:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6927b1c7-02f2-3f10-9e38-64142cc5bb7a | -12.8809 | -49.1977 | 2025-07-15 09:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 96f27637-bdf7-3032-8147-8b6cdff4c4a4 | -12.8809 | -49.1977 | 2025-07-15 10:30:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 84dadac5-7b54-34c4-bde9-00604e810caf | -11.4588 | -45.0895 | 2025-07-15 10:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ad88175c-6cd3-3c46-a978-01cd7cba337f | -11.4588 | -45.0895 | 2025-07-15 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8f3c3a17-f7ee-38e7-a011-68b0c840ee28 | -5.3741 | -43.9216 | 2025-07-15 11:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6342fdbb-1cbf-3be8-9313-ab40f5c5e95c | -11.4588 | -45.0895 | 2025-07-15 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 10cb0832-d7dc-39df-a9b0-f6fa12b5cf0a | -5.3741 | -43.9216 | 2025-07-15 11:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 7223d6c8-e304-3566-b9dc-72e2aa01a1b4 | -3.04565 | -40.81489 | 2025-07-15 11:30:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 71341412-7b35-3437-9976-a2253f517384 | -5.61844 | -38.89976 | 2025-07-15 11:30:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 9fb4d9f8-1c4e-3b19-b966-c44c1658e1c4 | -14.15165 | -42.11927 | 2025-07-15 11:32:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 593e455a-68b5-3f14-8b3a-acc483e6fc89 | -14.14158 | -42.11027 | 2025-07-15 11:32:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 7659d095-6764-3ff7-9009-f6bbfb29b414 | -19.41239 | -40.50412 | 2025-07-15 11:34:00 | TERRA_M-M | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| fdc56c3b-337e-3ad3-bb53-537c61526483 | -11.4588 | -45.0895 | 2025-07-15 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ba774ec8-067c-38a8-a415-da1f6b6d3013 | -11.4588 | -45.0895 | 2025-07-15 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 63852593-3d67-3cdf-bacb-b6fd77334f12 | -11.4598 | -47.3107 | 2025-07-15 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a7da7950-97fa-3ab5-b1b6-dede503b8b1c | -11.4588 | -45.0895 | 2025-07-15 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7e020217-10a0-364d-a2ba-7652868d22bb | -11.4588 | -45.0895 | 2025-07-15 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 09899ea3-a667-3593-a0f9-f89b173eca0e | -11.4598 | -47.3107 | 2025-07-15 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 97d825d4-66e5-3762-8a85-2c23ffb0a20c | -7.658 | -44.4207 | 2025-07-15 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1c5abb77-26f7-3be0-b544-39c9a232ad2b | -7.6583 | -44.3976 | 2025-07-15 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c4ac293a-2670-37c4-ab90-7729ccc38b34 | -11.4588 | -45.0895 | 2025-07-15 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 540eb6f8-cca7-3043-8078-57f8eb14be84 | -7.658 | -44.4207 | 2025-07-15 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 0abdb029-bf21-377c-8dfd-a5e4994650fb | -12.4797 | -46.9243 | 2025-07-15 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e875c0ae-2a16-3307-a66e-9e14bbc5ba06 | -11.4598 | -47.3107 | 2025-07-15 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a27d60ad-7cf6-3897-9182-6b6cbdd5e50c | -5.3741 | -43.9216 | 2025-07-15 12:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 311ba626-186d-391b-92c2-4c9c41946a17 | -12.4797 | -46.9243 | 2025-07-15 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 35378b34-9c81-384c-866c-dc1a363a5f94 | -11.4598 | -47.3107 | 2025-07-15 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 64169fab-ef76-3729-a180-d0459721f18e | -11.4598 | -47.3107 | 2025-07-15 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2ea03eea-265d-35c1-8c20-929fde0debfc | -11.4598 | -47.3107 | 2025-07-15 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1481bf3e-b124-36af-9879-420e58676e14 | -12.4797 | -46.9243 | 2025-07-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 4c21c404-273d-3aff-ac05-cdb464ca596e | -12.4801 | -46.9017 | 2025-07-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 527c6dd2-b070-3490-8b6a-d4c5416ed38e | -11.4588 | -45.0895 | 2025-07-15 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e8111823-a4ea-3d36-a868-8db2b5ab901c | -12.4797 | -46.9243 | 2025-07-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 6546770d-4a59-3d0f-aeee-36db21437c7b | -6.6678 | -45.7147 | 2025-07-15 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 8321da11-0911-30ce-92bc-ca244d68f935 | -12.4801 | -46.9017 | 2025-07-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 72a5a35d-bdcb-3023-bf16-a0f41dece77d | -11.4598 | -47.3107 | 2025-07-15 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 35b8499a-7706-33b3-a9ed-bbd0176b2233 | -11.4789 | -47.3082 | 2025-07-15 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b75c736f-1ef5-3bcd-afdb-4be0a5cb7975 | -14.1441 | -42.115 | 2025-07-15 13:20:00 | GOES-19 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 5500d218-0877-36fd-95ce-f0b21ade21f1 | -6.6678 | -45.7147 | 2025-07-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |


[Clique aqui para ver as próximas entradas](README27.md)
