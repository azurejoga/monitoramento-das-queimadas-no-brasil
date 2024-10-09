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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cbc68f3-e511-3150-88e9-3a7d991e77c6 | -16.89203 | -56.71953 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4c6762a4-a31d-3a60-80b9-6c0b3d1baa38 | -16.8892 | -56.73262 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4d474f84-f0f9-3749-aa9f-13554b96c529 | -16.88526 | -56.72254 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f90d7b45-b7d7-3656-ab4b-6275f39b6072 | -16.88432 | -56.72691 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 08e5fabb-ce97-3756-bd19-bcbdc3523e40 | -16.88337 | -56.73127 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a6b6c133-3248-3144-b5f3-76c31adaf80e | -16.88243 | -56.73564 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| be8b690a-9e11-3c66-b3fb-e20ae5ff7e87 | -16.87944 | -56.72117 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b37dc2ce-41d5-389b-91a1-4f3ef540b360 | -16.8785 | -56.72554 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 40e37e5d-3c65-3e93-9724-5013ef302bf5 | -16.87754 | -56.72992 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 43214222-032c-3d06-a875-652cf74170b6 | -16.8774 | -56.70243 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 40cdbcc8-b730-35da-88d4-21987799a9c0 | -16.87659 | -56.73432 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cb472b56-2ef6-3598-af12-b51d2afa70a6 | -16.87563 | -56.73872 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 99ac2c75-54f9-302d-969c-8e22890fecbd | -16.87551 | -56.71112 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d715bf43-2fe0-3e8b-8a6e-695aac9545ca | -16.87456 | -56.71548 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e0e894f8-11b8-3d47-9f33-aec4a8c921ad | -16.87171 | -56.72861 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7aa452fc-181b-34af-b3bf-355447178be4 | -16.86884 | -56.74179 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 91375a1e-9b94-3cc7-b15b-4f0a4368b1b6 | -16.86788 | -56.7462 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c08cf74-6f2c-3f94-9e40-baccc0d4adda | -16.86364 | -56.74453 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 25d7fbbd-3008-37ec-8d64-cc26683f5f9a | -16.86204 | -56.74486 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| eea1b176-5bf4-353e-bc8d-5556f61d09e6 | -16.85687 | -56.74761 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3330e586-89d1-3b86-b4c5-e05184b9e1a7 | -16.85523 | -56.74796 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0229bccf-6e3f-3ae7-baf2-4fb417c4fb88 | -15.70868 | -59.37525 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1657a862-d40f-3f7c-a9bc-5b00a1bef12b | -15.70731 | -59.38132 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e6166526-60a0-38a1-b1ce-fef400ac3a3c | -15.70724 | -59.37539 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1509502c-e3fd-35a5-a731-a83a22b56444 | -15.70584 | -59.38143 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9283d5e6-ba1a-3e45-b6db-f2d0ed2e5978 | -15.70035 | -59.37985 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4b9d2a20-6475-31d5-a788-6ded686d4237 | -15.69878 | -59.38039 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ce57fc0e-7fa2-3913-8e5d-5760a414efad | -15.69179 | -59.38546 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 297d22ee-2c0d-3185-9ec9-0d9bba3ae8b0 | -15.6904 | -59.39159 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 827b74bb-0405-33d9-b9b8-1f9a3a5caa26 | -15.69017 | -59.38602 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf3ec218-885c-3902-9fa1-76d067d53b1a | -15.68876 | -59.39207 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb286c64-dbb2-37eb-ba24-88ac81a74719 | -15.68181 | -59.39732 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c54c8ec-5d3d-3080-9b6b-a0d56700bcc6 | -15.67188 | -59.40888 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7204d687-ce7e-3554-8f4a-ffe386b4c0da | -15.66505 | -59.40679 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c345a9d1-e08f-36e4-a503-0b8d57f9b8ff | -15.66363 | -59.41301 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5ccac3a5-fd83-3945-ba56-40e77819ff27 | -15.65666 | -59.41153 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d9facb8-cfe5-3570-818c-2800c2b1ac3d | -15.65519 | -59.41798 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a93d3a9-fea6-36b8-a756-54c34bc55476 | -15.65368 | -59.42457 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24be0caa-1a44-36fd-9f4c-d5e4e3c59465 | -15.6521 | -59.43153 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e83718f-f7ad-360e-8109-46a043477db5 | -15.65031 | -59.43937 | 2024-10-09 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5cb8fd49-9445-33e6-80eb-ce5683fccc35 | -1.11 | -53.6173 | 2024-10-09 04:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3d9958cf-895d-363f-bb1e-8d29a87f64f7 | -3.9023 | -46.4467 | 2024-10-09 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ef08a6a6-bee6-33fa-af92-52005c0f54a4 | -3.9208 | -46.4459 | 2024-10-09 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fd169e18-872e-36d0-803c-2fc121d9f942 | -3.9394 | -46.445 | 2024-10-09 04:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 85388f52-0652-32aa-804a-46097efaf4c4 | -5.5905 | -44.8687 | 2024-10-09 04:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 4a82aa58-4e60-3d44-a864-6bbd12188c3a | -6.7614 | -60.0559 | 2024-10-09 04:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 2aed18ef-afbc-391e-a56c-ac65faef2097 | -6.7615 | -60.0367 | 2024-10-09 04:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 3a3eb646-a546-3db9-901a-9ebee1b91107 | -6.7798 | -60.0552 | 2024-10-09 04:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 95de2340-381e-32ac-8e61-d45a457c26e9 | -6.7799 | -60.036 | 2024-10-09 04:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a7f1d0f7-02e5-3a51-8b7b-092f868a62d7 | -8.4921 | -48.6259 | 2024-10-09 04:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0a92562a-4151-33a2-904a-08ad2a90d821 | -10.3656 | -64.8262 | 2024-10-09 04:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8b4f8b24-7bc4-34fa-ab8c-d2dea03ee3da | -10.3843 | -64.8255 | 2024-10-09 04:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b6c6dfa0-95c1-389a-9a89-f76f749455ac | -10.4287 | -60.9979 | 2024-10-09 04:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| fefe1b3f-6c35-3fa6-9ecb-146806020d98 | -10.6256 | -55.9154 | 2024-10-09 04:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| beae0aa6-cb07-3a49-82cf-0c5f08492ccf | -10.6258 | -55.8953 | 2024-10-09 04:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e7bc1fa9-68e8-3640-97e5-6a25984cfa9e | -10.8754 | -63.9169 | 2024-10-09 04:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7b4159ab-ab30-3b4e-83f3-46b4ccc4a067 | -10.8755 | -63.8979 | 2024-10-09 04:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 137aec57-60d6-36e5-a2ff-c4bd67c9f600 | -11.2583 | -60.3885 | 2024-10-09 04:26:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 2a6fc078-3798-34f3-b408-fa62e81e7011 | -11.2771 | -60.3873 | 2024-10-09 04:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c2c66915-6e25-342c-9670-67a6cf348a55 | -11.5233 | -65.137 | 2024-10-09 04:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 09c930f4-2f83-33e2-85c0-1b937a837e8e | -11.693 | -65.0163 | 2024-10-09 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6ed9099b-4ddc-3597-a351-7872aaa06668 | -11.6931 | -64.9974 | 2024-10-09 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 125.3 |
| b29c8c9e-178b-3e26-beca-c842adec4c17 | -11.7117 | -65.0155 | 2024-10-09 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 5132dcbc-7076-358a-9bef-0d083e069140 | -11.7119 | -64.9966 | 2024-10-09 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 271.4 |
| 776aec19-6e3a-3399-86cf-bed5b91b74cc | -11.712 | -64.9777 | 2024-10-09 04:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 83f5e74d-d5c0-3e98-b9ca-b496bae6b9fe | -11.9729 | -51.0575 | 2024-10-09 04:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3c37d8a3-f425-3277-bce9-77d0d80a9ef5 | -13.288 | -53.6832 | 2024-10-09 04:26:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b98d45dc-5763-363d-86ce-e4b78736c3d1 | -13.3786 | -61.9582 | 2024-10-09 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9d40a8af-598c-3627-bcae-974fcaa77f7e | -13.379 | -61.9194 | 2024-10-09 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 671034c7-61eb-3f83-83bc-09c39e054348 | -13.3976 | -61.957 | 2024-10-09 04:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 325a70e9-4d15-327b-9d8a-c65d0d6394e8 | -13.398 | -61.9182 | 2024-10-09 04:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 0ebf50e5-1c42-3d08-bf5a-516422c71d57 | -13.417 | -61.9169 | 2024-10-09 04:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ee853c00-2a74-3fbb-a3e1-5587e76e0768 | -14.0975 | -51.0918 | 2024-10-09 04:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e592feb6-b4c3-399a-982d-d8b41e0dc4cb | -14.0979 | -51.0703 | 2024-10-09 04:26:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c474bcbd-e52d-398a-b75c-696ce4fa080b | -15.6795 | -52.4993 | 2024-10-09 04:26:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 181070b1-bc7d-3203-9be7-8f05e25e7dd4 | -16.8048 | -57.4197 | 2024-10-09 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.2 |
| de56b943-3007-3c08-9c09-8c33711a1a7d | -16.8244 | -57.4175 | 2024-10-09 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 2d5bd07c-27f8-3565-8ae8-245c39dbbc21 | -16.8898 | -55.8039 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| c5275527-bd79-3c45-b2ef-df4c4203d815 | -16.8901 | -55.7831 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| a9388762-e6f1-3248-a66a-714d5c69308b | -16.9094 | -55.8014 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 179.0 |
| 3c2de4b9-6e20-32db-98af-7275b13f2ba6 | -16.9098 | -55.7806 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 200.2 |
| 6c07a442-a040-3ece-a408-9086485030b5 | -16.929 | -55.7989 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 2c1b0fa4-68f1-3151-aacc-5783add1a4c1 | -16.9294 | -55.7781 | 2024-10-09 04:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| ca8b375e-9041-306e-a20a-3192849374cd | -17.0995 | -57.3446 | 2024-10-09 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| c1d3d2fd-6e1a-33c5-8847-01fa0976de28 | -17.0799 | -57.3469 | 2024-10-09 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 0da09c28-5904-352d-afdb-d62361c0bb7a | -17.0795 | -57.3674 | 2024-10-09 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 07cd966f-9e7b-305b-b320-3ab6b120ea18 | -17.0599 | -57.3697 | 2024-10-09 04:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| e40d1e95-4319-39fa-8750-c6050abc053f | -17.1188 | -57.3628 | 2024-10-09 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| c903ffb8-7129-3d87-85d2-2856059519f2 | -17.1591 | -56.1014 | 2024-10-09 04:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 43b7963d-81ca-3fb3-8d5b-3d2d6b502873 | -17.1471 | -56.8256 | 2024-10-09 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| cc114a47-d89d-3c91-b034-bfb682c77949 | -17.1384 | -57.3605 | 2024-10-09 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 2c5786b0-661b-3e35-859e-3a49b436b6ad | -18.1193 | -56.3921 | 2024-10-09 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| ba4c212e-7b7b-3cda-88c6-9684f75c0288 | -18.1196 | -56.3713 | 2024-10-09 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 01e94f3c-d80f-3235-8b8b-2ec330445c73 | -18.5996 | -57.2422 | 2024-10-09 04:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.4 |
| 54f13857-3814-388e-8dbd-bd86a6a1dde0 | -19.7927 | -45.6252 | 2024-10-09 04:26:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 9d96f7be-169f-39c2-9f1f-862e49ab70bb | -19.7934 | -45.6012 | 2024-10-09 04:26:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 4a33d1f4-e7b3-38d6-b938-bd5b677617e7 | -19.7941 | -45.5771 | 2024-10-09 04:26:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ea874322-5d61-318f-b142-8c98d043969f | -19.8138 | -45.5961 | 2024-10-09 04:26:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 4b10e142-d53c-3526-833c-1a2afdfcf865 | -20.1035 | -55.9434 | 2024-10-09 04:26:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 48d72df9-095c-33c1-8336-b699a1f074fa | -20.3346 | -48.7307 | 2024-10-09 04:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 286.2 |


[Clique aqui para ver as próximas entradas](README109.md)
