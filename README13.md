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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bfa4402-5175-3d63-8238-d6a1b65b9a2c | -4.9605 | -55.8226 | 2025-08-24 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 0da2cc4e-9fa9-30a4-b030-28aa523b2467 | -17.6176 | -44.298 | 2025-08-24 01:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| cd80fcd5-1789-37a0-9fa9-22b8c38773d6 | -5.4182 | -60.1593 | 2025-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 94962c3d-093d-30fe-b397-080a55edc929 | -20.3396 | -51.6839 | 2025-08-24 01:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 905af817-4eda-35d1-9dac-d1ad492b085f | -5.4026 | -44.9952 | 2025-08-24 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9b589dfb-8850-3d77-abf3-9c511f4776f5 | -3.5083 | -47.212 | 2025-08-24 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3e5eea83-4d98-31e3-8b79-9681347ea836 | -9.1533 | -59.5027 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ec0eda38-c6ac-3941-ae83-353ec9cda878 | -5.4365 | -60.1588 | 2025-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c3aba59f-2150-3990-80f4-8b90546fdec6 | -11.9867 | -61.0214 | 2025-08-24 01:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3cc56635-2f92-32c4-a399-85aeb147e27e | -17.6183 | -44.2738 | 2025-08-24 01:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 29c258c7-1a76-3519-a793-fbea45989f5f | -5.4364 | -60.1779 | 2025-08-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f4b8f391-6d80-3d29-a2ec-f20ce78ebd7d | -9.0061 | -65.3813 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4fae29f9-1f6d-347d-9775-0304edcfcb89 | -17.4045 | -42.6186 | 2025-08-24 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a06682b9-dd0e-3166-8983-12caae02de03 | -10.8082 | -46.3857 | 2025-08-24 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 8b75fb96-83c2-31a0-abf3-0775e79d3b8e | -9.0231 | -65.7169 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 07bf7580-c940-39b4-be19-3be990d93179 | -9.1536 | -59.464 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 231.1 |
| 7926b1f3-0ea8-378c-a600-c3e1f8fdbdf6 | -9.1441 | -60.7765 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7803c1e0-f64a-3792-9a90-4f3bec0608ea | -9.0246 | -65.3807 | 2025-08-24 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b7263444-9017-3e97-87ad-a17406cf5d48 | -20.3599 | -51.68 | 2025-08-24 01:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 157.2 |
| f0b63e4c-134e-304a-9a93-0e8bc61d9306 | -22.8253 | -53.9872 | 2025-08-24 01:10:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| f4cec375-b8d2-387d-9f60-8c841b6f41dc | -3.5995 | -47.5142 | 2025-08-24 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a6eb82d2-6c8e-3b63-8d52-9f86625272c9 | -22.8248 | -54.0094 | 2025-08-24 01:10:00 | GOES-19 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 3b549ff3-fe32-37e7-bf54-1b4e4d13f228 | -9.1998 | -60.793 | 2025-08-24 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 82ebf8f4-0c59-3ab9-83f7-9227342d508a | -14.8157 | -47.9118 | 2025-08-24 01:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 6e1244f2-68f8-38e4-a667-536e1278baf6 | -8.9106 | -62.4289 | 2025-08-24 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| ebe1214e-65fd-3847-be2f-64311a50c10e | -11.5055 | -51.8705 | 2025-08-24 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 07aed4cd-10d9-3830-96c8-3f7144b3e479 | -17.4045 | -42.6186 | 2025-08-24 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8e373415-b9ab-31d4-a467-9d76675f1009 | -10.4164 | -47.1732 | 2025-08-24 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ba7901e1-0e15-3a64-ac7d-53a2c88e2a9e | -9.1535 | -59.4834 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 224fe291-e3ad-3f92-acef-e27c972e7425 | -9.0045 | -65.7174 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b97de22a-c3c2-3a38-83e3-933064bbd809 | -20.3396 | -51.6839 | 2025-08-24 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 924860e4-e4fc-37cb-b8e6-91ce255f35eb | -9.0416 | -65.7163 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 743d1cf4-31a4-3bfe-8abf-9246469780a4 | -17.6176 | -44.298 | 2025-08-24 01:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 108.2 |
| edabf4d4-f86a-35ec-aab2-39b6c23f9088 | -20.3701 | -46.7433 | 2025-08-24 01:20:00 | GOES-19 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 712e5cce-f2ee-3fd2-b10a-9081e87d7654 | -10.6128 | -44.3284 | 2025-08-24 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 789b21a5-e944-302c-abcb-8340778e08e8 | -20.3594 | -51.7023 | 2025-08-24 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5a1858df-d7ac-3ea2-82dc-09bef0fdc29d | -11.9867 | -61.0214 | 2025-08-24 01:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ac323195-b2fb-3df8-8f11-5668b6e47bf6 | -5.4364 | -60.1779 | 2025-08-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 677a0f77-2a01-3c45-b4de-c09cce056a5f | -9.1722 | -59.4629 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 9f5d07f4-eb1d-305c-a925-14da7311e567 | -8.6131 | -62.5929 | 2025-08-24 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 38e997f3-b265-35a6-af32-62ad5c463cf5 | -9.1533 | -59.5027 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7ffa70ba-6ce4-32b8-b894-d4dde7292376 | -3.5994 | -47.5359 | 2025-08-24 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f9919d7e-25f1-3053-b216-58b05a0d6f6f | -17.6183 | -44.2738 | 2025-08-24 01:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 58e4c4d3-8573-3d65-90c0-7cc16c9c3063 | -9.0231 | -65.7169 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 5f0c6671-85d0-3673-b856-dc0f396078aa | -9.0245 | -65.3994 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c2036bd4-f001-3bbe-9a6d-7fc7afcdfa92 | -9.1998 | -60.793 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 4f672ba1-79bd-3002-8bd7-8290e29b6b12 | -16.797 | -51.3419 | 2025-08-24 01:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cc19014f-ef13-3d4e-aea8-b00b4f2a2868 | -5.4365 | -60.1588 | 2025-08-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1899e9c7-24fd-315b-ba82-6228682904c1 | -9.0246 | -65.3807 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e31112c9-e5f5-30a7-88c5-72c04fd28a73 | -10.5937 | -44.331 | 2025-08-24 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e60e66cb-f960-3eb5-b31d-9d025a5fabea | -9.1538 | -59.4446 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89f2bb0c-15fb-35fe-85fa-5cf92b341c43 | -10.6009 | -50.1843 | 2025-08-24 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 97b8ca5d-4666-350d-bd90-37a4232c5a54 | -9.1441 | -60.7765 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e9e97998-00e5-3d0d-899d-3da8e54497bb | -5.4181 | -60.1784 | 2025-08-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6bc3c124-67d1-35bf-9ecb-74740d5a97ed | -3.5995 | -47.5142 | 2025-08-24 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 96a56319-c8e2-3dd9-97d3-08812c01bbef | -9.0046 | -65.6988 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ad358597-2fd8-318d-bda4-128a6ed6fec9 | -10.8078 | -46.4083 | 2025-08-24 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 48596bef-4613-3921-adb7-d0d4913b6509 | -20.3599 | -51.68 | 2025-08-24 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 135.8 |
| ffcc6ec4-49b9-36b6-bc40-d9c2ecee08f3 | -9.0232 | -65.6982 | 2025-08-24 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 378f7d13-635d-3287-bfb7-7f2966a89b91 | -10.416 | -47.1955 | 2025-08-24 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 666a60bf-c262-3e40-b1ca-246a2f5fdf04 | -9.1536 | -59.464 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 228.3 |
| 3a5306e2-33aa-3cea-b3cb-7080d9914e24 | -11.5247 | -51.8474 | 2025-08-24 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8fcca01d-89ee-3683-b0aa-bca7a17094c7 | -16.7965 | -51.3637 | 2025-08-24 01:20:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| d81f04a8-201c-3ad7-996c-8bf49426a5b8 | -20.339 | -51.7062 | 2025-08-24 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e929bf01-045f-32ff-81af-ce074db3c6a2 | -4.9605 | -55.8226 | 2025-08-24 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2681eafb-cdf0-3479-8311-3cd0bc025147 | -5.4026 | -44.9952 | 2025-08-24 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e0d478bb-312e-3878-b735-aba0b06015b4 | -2.9279 | -53.7078 | 2025-08-24 01:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 8f777dc5-8a62-323c-9dd2-2c2f15352e22 | -11.5245 | -51.8685 | 2025-08-24 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 263.2 |
| 79405485-db63-3759-9ba8-1fce6a39f254 | -9.1721 | -59.4823 | 2025-08-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| c2b10265-2bd5-3f29-ad95-8861965e1710 | -17.5975 | -44.3027 | 2025-08-24 01:20:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 317f3ff9-83b9-3c0e-a8fe-d378459d4609 | -11.5055 | -51.8705 | 2025-08-24 01:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 155.9 |
| 39ec9742-4774-35c6-8679-f5ead5a1f85a | -5.4182 | -60.1593 | 2025-08-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a6e2b2f0-fcfb-3f02-adaf-0d952dc5f631 | -8.5801 | -62.603298 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f49e4dcf-1806-319c-be78-aff8120b24a8 | -9.1509 | -59.507999 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f29048f-0a2d-30a4-9ca2-6fb761d01f64 | -9.0222 | -65.699997 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d63b60b8-7315-367f-899b-80474b81ec13 | -5.4126 | -60.1828 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4329310e-2a4a-3a78-ae78-9edf22f60769 | -8.9132 | -62.439999 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd9d3533-6753-34d5-8021-169b0c6098d1 | -9.0191 | -65.686096 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6056501c-f77b-3d17-9a3b-8ae7661a3c8a | -8.4378 | -63.856499 | 2025-08-24 01:24:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea90e69b-b5f2-35b6-8149-0cc72460db68 | -9.1604 | -59.4627 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42d8a619-bd3f-3d7c-b02d-b77da06a62b3 | -9.0238 | -65.706902 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5f478f-fe8d-3c9f-9e6f-107e08a873da | -12.587 | -60.352901 | 2025-08-24 01:24:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c05a327b-ed6f-3a41-b26f-b5975f3ce50b | -11.6988 | -60.1833 | 2025-08-24 01:24:00 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fe6c9a6e-329a-368a-8341-f784410ddb75 | -9.0201 | -65.370697 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55a54f91-9c78-35da-9dac-441e3d89dca0 | -9.327 | -63.196899 | 2025-08-24 01:24:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f67ab8f9-2495-342a-bd50-4591ce9302af | -6.6782 | -58.8634 | 2025-08-24 01:24:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a88e804c-8f2e-3c51-aa65-19451405a937 | -8.8831 | -62.3997 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e37f9269-6c19-3113-819c-ec1ea5f9e254 | -7.7306 | -67.0625 | 2025-08-24 01:24:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0c3773-e151-3727-ac45-c3b64970c849 | -6.3069 | -59.881001 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3169087f-d1de-35e5-bcaf-d3dcf0ea045a | -7.5689 | -63.442902 | 2025-08-24 01:24:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb3b0399-dc7c-3e28-a63f-dfd1cf3532f6 | -8.9048 | -62.404099 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 84ff9378-4b59-34d8-94db-2e390973625e | -8.9112 | -62.431099 | 2025-08-24 01:24:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6200ad0-8311-3e4b-a5ca-172061819917 | -5.6073 | -60.223801 | 2025-08-24 01:24:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf9251e-cc32-3520-a436-f179d30e023a | -9.1637 | -59.4762 | 2025-08-24 01:24:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec61aa4-3803-308f-adca-d2687bde327f | -9.0034 | -63.6264 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f81a993-0f34-3058-8e20-bd369af92493 | -9.0217 | -65.377701 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3335b2ef-efae-31c0-be4d-afd2fdead47c | -9.0053 | -63.634201 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e5ca1ba-b294-32f0-a8a5-32db2f0d05a2 | -8.6822 | -62.864101 | 2025-08-24 01:24:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7b9198-14a7-38e1-9221-394952466c7f | -9.0175 | -65.6791 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 990fdebf-6f42-3ecd-88c5-2816bd58656b | -9.0304 | -65.690697 | 2025-08-24 01:24:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
