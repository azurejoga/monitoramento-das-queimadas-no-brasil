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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997d048d-b5c6-3da8-92fc-121726208cd4 | -6.67109 | -42.82206 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ae1c0363-7825-38ac-8495-344f7dffe2b7 | -8.04382 | -54.89751 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0cfd2ea0-b014-3ddf-8dd4-6c2355b5e5ef | -7.74377 | -42.52531 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 20fe3d00-0487-3291-8877-ad78b216015a | -9.8888 | -47.81459 | 2025-10-04 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d1b4b9f-6048-3676-bcf2-5ade23e6e653 | -7.75707 | -42.51823 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 71d81b2d-d3bc-30ee-b87b-2bf142bd7fb6 | -3.78247 | -52.33463 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0333aff7-2d50-3fa3-92b6-ef3360b8c6af | -6.04847 | -42.52035 | 2025-10-04 05:04:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 52b8d8d4-401e-312e-ab46-7519808643dc | -9.32585 | -54.52333 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60f59441-6dab-3e8f-998b-f107fb2f4ff3 | -8.61494 | -54.95944 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c6270fc-6aa2-312a-a2d0-e9ef4a38c8ba | -10.0704 | -48.18399 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c84c115-a60b-3204-b9ca-461b8a885fe3 | -4.33004 | -53.8347 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b019a7-c684-3619-ad30-5368be2121cf | -8.52312 | -50.02806 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75dbe889-4d75-35df-95aa-29ba6b958ee0 | -3.78323 | -52.33209 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b17d9705-aab6-39e7-89bf-2282eac5eb68 | -8.85167 | -46.82717 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ed57849-a887-3dc1-8d6a-bb31e9a46bc8 | -6.72772 | -45.96725 | 2025-10-04 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bd1db8b-1342-3233-b795-1fffd4927147 | -6.88386 | -47.23528 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58d47cb4-a748-3899-ba7f-a509e2546753 | -8.62626 | -54.99793 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6dce727-3daf-3baf-b7d9-4ca897e5a135 | -9.63427 | -54.31356 | 2025-10-04 05:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5a8b59a-83bf-31c7-a065-f8fb3352dd9a | -8.85261 | -46.82003 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64f93a96-0471-3e54-a1d4-368617628761 | -8.85086 | -46.79094 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65d48580-2274-3e24-8179-9f48cf5b2ec4 | -4.95832 | -45.07158 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a8473df5-e9cd-3561-9ea6-671bd3518e98 | -8.22303 | -46.81113 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5889f0a4-0674-3213-97ba-5c846907ee33 | -8.89086 | -45.02436 | 2025-10-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7752a39a-5560-37d8-ba78-f048c6f43223 | -7.73903 | -46.30892 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe36c060-3a10-3ec9-a676-b76d320c34ac | -9.4507 | -50.89803 | 2025-10-04 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef995032-c885-38e9-8aae-9c4b83c77f5b | -5.84897 | -42.80014 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0a6b1fff-2a7f-39d5-bc08-c9bf0039ea4f | -8.89125 | -45.02126 | 2025-10-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c945e30b-27fc-39c3-8bb2-082e91d06ef9 | -3.69086 | -50.893 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b57d249-4482-3d05-bda6-0d13b3d284e5 | -7.46811 | -46.85101 | 2025-10-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 687e6df7-dbcc-306d-b75f-5e0296857786 | -7.78402 | -61.36161 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0756201-3abb-3fe5-a398-5b2db31b4f1d | -4.61598 | -43.1442 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6b8f2254-09e2-393b-aae6-76de7763fabf | -9.99625 | -48.27925 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4688458-561f-3c8e-bae3-f87ca323f390 | -4.44396 | -43.23445 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 0a47cdb4-86ea-3f66-ae9a-500f42854667 | -6.06938 | -42.51908 | 2025-10-04 05:04:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 103a5200-2597-30a9-98f3-bed200660053 | -9.02571 | -50.66179 | 2025-10-04 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d06ab30-77a0-3919-88b1-310485ac5cd0 | -9.9372 | -50.23497 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e9eed92-2adf-34fb-815e-c7168fc7efa4 | -8.6659 | -50.69687 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e59106c-53c6-38e7-965a-000302a78020 | -7.05577 | -42.78848 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a0d93e16-b215-3e87-b01d-a20512a00bd5 | -7.7562 | -42.52526 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 97ee5432-40b7-3c46-9532-29c97623d14a | -5.2732 | -46.1749 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcf3a89b-34d2-3978-9fdf-faaae78371c6 | -5.84973 | -42.79445 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d34c3e0d-3ac5-303e-ae07-2361deb25bc2 | -3.79155 | -52.06519 | 2025-10-04 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6335e5f8-ca9c-393b-a0b0-478849b852bb | -8.91978 | -46.61016 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f1bf04f-8975-32be-bda3-05db83561cfb | -5.485 | -44.1064 | 2025-10-04 05:04:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1a44ee2c-03c9-34df-8b43-fb3f6e0f8402 | -4.60868 | -43.15195 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e77bb673-9f44-3199-9851-cf7889aad671 | -8.62064 | -54.98975 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12aa2985-899b-341b-9939-b64615abfba6 | -7.72329 | -46.29919 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec0a7b2b-0166-37fa-a944-dc76cbdaee50 | -9.34095 | -45.78943 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9a4e6ec9-b881-3fd2-896a-72f14d61c24f | -8.91955 | -46.60843 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a40ea47-4b24-3bde-b1e9-5239273f0cd4 | -4.315 | -48.09505 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f55b1e1-7310-35cc-ba98-3a9d27c2b9db | -4.49591 | -42.869 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a569331-0d36-3eda-9099-69e2d32c18e1 | -9.91513 | -43.80206 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3ef02b5f-804d-380a-9fbc-4b409488c832 | -9.32131 | -54.53035 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66aada79-4b5f-338b-a8fe-4d9ab6bee406 | -7.6553 | -45.47012 | 2025-10-04 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c336d53c-5742-3602-a584-5b0cf04d5610 | -9.90857 | -43.74071 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4af90e9a-d56a-3708-8eaa-7d8e3dcc41af | -7.77077 | -46.27333 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 233389bf-c631-3d47-816d-0ae312b2f4cc | -10.5383 | -44.51589 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec86a47b-3424-35b8-887b-30b2643aed23 | -9.76759 | -48.5843 | 2025-10-04 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78eb79ce-eb41-3ab5-b2a4-83dd4162332f | -7.04958 | -42.7766 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| abaf7d8e-b4ec-3eb3-8fd5-f02f4d9812b7 | -10.21358 | -48.18596 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d449722d-40e6-328e-af46-b02b70ce70df | -4.43594 | -43.24435 | 2025-10-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb3a9e65-c303-3607-82e0-f6b81e4b8950 | -8.6229 | -54.99742 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c39ca65-3228-3fd5-8b72-ebc9e3ff4010 | -9.11104 | -44.39845 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b64b42c1-b1f8-3493-b7fd-305d67390dac | -6.22423 | -44.27504 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f7a84ca-6efa-33b0-9290-3abcf19aaab5 | -6.36483 | -43.89313 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89d33d3d-263c-3273-b978-f84daac53940 | -6.37251 | -43.89904 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6a04ca10-be62-3f6a-9cfa-43f57de09acc | -8.90374 | -46.59925 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a82f321a-9b34-3471-a978-ce5a516f69f5 | -4.31571 | -48.09008 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa1bce66-3f2b-357c-b9bf-35af247a55cc | -6.2434 | -45.34528 | 2025-10-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73c4c612-8fa8-30b7-ace6-2f5f03c58d80 | -8.5266 | -47.21584 | 2025-10-04 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b246ed-6971-3866-89a4-9c71edf13cec | -9.34845 | -45.78951 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 002d01fc-c2b4-36bd-81c9-de4292b63f4f | -7.0556 | -42.78409 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9d664b24-5eca-3f93-ba56-45effc0b2371 | -9.91444 | -43.80803 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 46a71e8a-7965-3478-b51e-7c22e4746f51 | -10.34194 | -48.16889 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6825fd66-e6b9-33c3-b216-25ba61e3a2a9 | -3.4972 | -49.56077 | 2025-10-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aafc2c9e-c014-3d36-bc14-6408ef691ac2 | -6.46515 | -44.58468 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d40a841f-3239-3e16-95bc-ab4b1a0b1b03 | -3.86553 | -53.3845 | 2025-10-04 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2944aae-bc30-3141-82f6-d073cbf50595 | -7.05558 | -45.78593 | 2025-10-04 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 566f1e36-f111-341d-b806-829ca6bbb12b | -3.73007 | -51.35844 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8fc2266-b353-35cb-b952-ea77805aeba2 | -8.89769 | -45.01987 | 2025-10-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 803b2566-2ef2-3196-acbc-cb58550aa2b8 | -10.77656 | -45.32956 | 2025-10-04 05:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4694ca06-f5cb-39d8-97c3-b623abf1a8b7 | -4.3176 | -48.09411 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 00b1b98c-1081-3230-b49e-8cc4264260a9 | -6.24359 | -44.22409 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea175e25-3d77-306a-be06-78359ebd1411 | -4.60796 | -43.15409 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f325bf38-468c-3bc1-8897-efb624f3f0f2 | -4.25643 | -48.56817 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0059074-1ba3-3dcb-8641-fa1966999f74 | -8.62111 | -54.96407 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8076e99-80df-3d45-ac48-9a63d66e07fa | -8.85214 | -46.82358 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afff2689-005d-39c2-940e-8ef57fb4a507 | -6.71311 | -42.8201 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8185702f-f78c-3311-8aa6-e8a80010f129 | -8.17144 | -44.12954 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73fc1ebd-bbf1-36d4-a27f-975fe59907c9 | -6.20471 | -44.33496 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b8468c41-e595-3a95-9876-c5335ac45a36 | -5.69764 | -49.30601 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b038f504-aee2-3c1d-a8ab-e583983e757a | -8.46795 | -47.41721 | 2025-10-04 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de9f610c-6e6a-3041-ac9b-170d85be3f81 | -6.30665 | -44.27551 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 379f7cfe-ac66-3208-9447-38c4a30d7978 | -9.93984 | -50.24677 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d068320c-7012-3029-b135-725192708c00 | -8.87642 | -47.82079 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5bd8b30-9baf-33bd-954f-82006d181f11 | -7.74558 | -46.30243 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1f5caef3-3486-3bb6-97a2-8592b9b124bd | -8.13701 | -44.0813 | 2025-10-04 05:04:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faa301c4-e83d-3b27-bff0-31776d6c27e1 | -8.7136 | -47.97723 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf521312-5d0c-3f23-911d-55e235a055e4 | -9.91161 | -45.96188 | 2025-10-04 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b1b58b9-f574-3485-8fa5-cfc0d19a9899 | -6.1804 | -43.92495 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README104.md)
