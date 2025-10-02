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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 370db04c-e413-3db1-a6c0-592bcc0ded88 | -5.9856 | -44.6118 | 2025-10-02 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ba6dbefa-e38a-3271-81d3-1836d743c3f7 | -7.7752 | -42.539 | 2025-10-02 02:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| 354992c0-d815-3342-9d70-45461f80900d | -13.0119 | -45.1988 | 2025-10-02 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 01503201-4a35-32aa-8c67-d56d64166c6b | -14.3119 | -45.9736 | 2025-10-02 02:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 7ace3bc4-d99c-33ea-9438-5a2826a38286 | -13.1546 | -47.8345 | 2025-10-02 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 810b7d47-d146-3f15-b5fc-8deb239ce8a8 | -7.7755 | -42.5152 | 2025-10-02 02:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 2067f228-077c-378b-8446-1726af3dd1d1 | -11.0144 | -46.5844 | 2025-10-02 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 67fcde50-8f41-38dc-8417-4242c62561b3 | -12.9024 | -46.9073 | 2025-10-02 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3581270a-cadd-34fb-8f84-a8ee69cc0246 | -13.3081 | -47.8565 | 2025-10-02 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b8a54dbd-24db-347e-9866-c66212d36718 | -10.8424 | -46.6289 | 2025-10-02 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 87996df5-3a55-3598-92d2-3779551399da | -10.8234 | -46.6313 | 2025-10-02 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 66a67ece-cb5f-35f1-b224-22f88c0dd9e1 | -6.6955 | -48.7062 | 2025-10-02 02:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 109.1 |
| aacd14b4-0fb8-360e-b751-0b482589b177 | -10.8237 | -46.6088 | 2025-10-02 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0a211838-2b2c-31ee-87d2-509beaa97724 | -5.986 | -44.5661 | 2025-10-02 02:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f5fb7b43-bd73-3694-83f5-c538ee08ea60 | -6.7213 | -44.1387 | 2025-10-02 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f8580630-cd47-307c-8bb6-50fa73994099 | -13.3085 | -47.8341 | 2025-10-02 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 51219427-2747-3f82-a6a5-1292e6b053fa | -13.155 | -47.8121 | 2025-10-02 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fe1af210-60e4-3a7b-8292-95f220a1735f | -13.1739 | -47.8317 | 2025-10-02 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| bad348bb-f4d8-3648-a9df-7ebc5ecd2918 | -5.9858 | -44.589 | 2025-10-02 02:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 50aec977-b1a3-33ca-88a6-edec485ee910 | -7.7563 | -42.541 | 2025-10-02 02:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 128014b2-c24b-303c-950d-dab587a44b62 | -15.1839 | -43.625 | 2025-10-02 02:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 683bb573-d46e-38cb-af96-3396c533b2df | -14.3114 | -45.9967 | 2025-10-02 02:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 5bb8f405-ff47-3df9-8c13-c04dd070407a | -7.7752 | -42.539 | 2025-10-02 02:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 163.4 |
| 8863c441-5bcc-3975-849f-79897d03baf7 | -15.2542 | -49.3104 | 2025-10-02 02:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 8d070e5e-6610-3bc5-a483-2551535019a9 | -15.2738 | -49.3073 | 2025-10-02 02:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3d937435-f3ef-396b-bf45-5020188d0eaf | -9.9567 | -43.6927 | 2025-10-02 02:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1115ccba-20e7-398a-98a1-b35da7d5d5d6 | -7.7941 | -42.5369 | 2025-10-02 02:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| a51035bb-2565-3805-b1ab-b67320b2d0e7 | -10.8429 | -45.4044 | 2025-10-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| be9cf540-f18f-328d-96e9-9d05f23781cd | -7.7563 | -42.541 | 2025-10-02 02:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 40c0894d-746a-31cf-bc13-23866c6e0d31 | -7.7752 | -42.539 | 2025-10-02 02:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 289.4 |
| 80a3bda7-93e4-32ea-aef5-8de06416bd15 | -9.9365 | -43.7657 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 210.2 |
| eef7fbc5-514b-3733-88c3-a8fb6b8fed23 | -14.407 | -46.0722 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1156b692-0c6e-3c44-b514-db1d786d9076 | -10.862 | -45.4019 | 2025-10-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cf24585c-128e-3097-af69-629b60e8d388 | -14.3114 | -45.9967 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 3f9f46b6-5f2c-318b-b49d-27fb5a2a4a43 | -14.426 | -46.0919 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a955d7e0-aab0-3a95-80da-e02ccd433c54 | -14.4255 | -46.115 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 208.5 |
| aaaf6096-a498-3b69-8b09-ffd08212f24b | -9.9559 | -43.7397 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 139.9 |
| 4d0d2060-11e2-3884-aa2f-ac4af7553e33 | -14.425 | -46.1381 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5bb5f150-55b6-3045-b8ad-f4c328bf7498 | -10.8424 | -46.6289 | 2025-10-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 39ef1dcb-df01-3582-9a0d-17c688f74417 | -6.6955 | -48.7062 | 2025-10-02 02:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 0e7de0f3-eaf7-313b-8cf5-9218ca7f2b7a | -9.9372 | -43.7187 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| 1d6c1b68-c631-364e-a769-84635d505f8c | -10.8433 | -45.3815 | 2025-10-02 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 0e39f180-2625-3ea7-81ec-e2415c83f426 | -15.2738 | -49.3073 | 2025-10-02 02:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b3d36393-0131-37ce-b22a-bf357fced9c6 | -10.8237 | -46.6088 | 2025-10-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a1ea0479-2a7c-3f6f-8291-7adfb4c007f3 | -10.8234 | -46.6313 | 2025-10-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| b9bf07ee-fa67-3e5b-b3f3-bac3b35ea0eb | -14.3119 | -45.9736 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 65dc4e8d-4ae4-3bb7-95f3-56e5aea2c3b1 | -15.2542 | -49.3104 | 2025-10-02 02:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b3dac825-cac4-354e-ac5a-6769f5412bb8 | -10.8428 | -46.6064 | 2025-10-02 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a6a82835-7845-3c2b-a260-31160c95f4c9 | -9.9563 | -43.7162 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| e9f3a910-b3f8-3faa-9656-956c669f9bd6 | -9.9556 | -43.7632 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| bf586a8e-73f1-3777-b15f-46f3ea130b87 | -7.7749 | -42.5628 | 2025-10-02 02:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 98e6a495-9610-31f4-a918-355bf0ce08a5 | -14.4065 | -46.0953 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 63645919-e394-35c1-a25c-61e0ef9f430d | -9.9369 | -43.7422 | 2025-10-02 02:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 274.8 |
| 1de26f69-1eb1-3d4a-86b5-1f188964bf27 | -7.7755 | -42.5152 | 2025-10-02 02:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 4d45a01b-dc91-3e87-b91f-158886e04926 | -14.406 | -46.1184 | 2025-10-02 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 275e7ab0-268a-30fe-a5e3-1440d5af0443 | -10.8234 | -46.6313 | 2025-10-02 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 00f4491d-4354-3ecf-86d7-8f02a3a2bcbe | -9.9372 | -43.7187 | 2025-10-02 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 144.3 |
| ab53b25c-98c8-3fa7-8169-e55cfdcb661b | -16.0426 | -50.8522 | 2025-10-02 02:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| e3d5dd4f-101d-337a-bb59-3eac50cd31d6 | -7.7752 | -42.539 | 2025-10-02 02:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 199.6 |
| 7b280fc3-49cf-3715-8df3-1dd9e1662738 | -14.426 | -46.0919 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 33881511-cfed-3764-b805-57d75f36e9f8 | -10.862 | -45.4019 | 2025-10-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 591ca400-0fa8-3cba-98ba-53163c9dfc56 | -17.8614 | -57.623 | 2025-10-02 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 42550f66-5d4e-367f-94de-98726ccca6df | -14.425 | -46.1381 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| fc7cfede-87f1-3f5f-ba9c-5bf4a02e86c5 | -7.7941 | -42.5369 | 2025-10-02 02:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| a4c22742-044a-3497-b814-4b8067d5f100 | -14.406 | -46.1184 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d2d08ff6-4b57-3c18-842c-1e2ecee2cbdb | -14.3119 | -45.9736 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7748a607-c435-3c8a-b3ee-c613faeb2ee5 | -10.8424 | -46.6289 | 2025-10-02 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| da54c3ab-ffc3-32ac-9406-644a9169168a | -10.8429 | -45.4044 | 2025-10-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 58eca72f-dd98-3f88-8c7d-dd6bc1a65e17 | -13.1739 | -47.8317 | 2025-10-02 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 12e59578-d17e-3f95-9db3-d8bef586c075 | -9.9563 | -43.7162 | 2025-10-02 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e4046973-cf63-3ae0-a1bf-bd01e8861427 | -6.6953 | -48.7277 | 2025-10-02 02:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 1bcf8c85-124e-3ae2-a10e-d66c8f3cf93c | -14.3114 | -45.9967 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 9db25067-4095-367e-907d-81ff2963c9fa | -9.9559 | -43.7397 | 2025-10-02 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 033a907d-a6ae-3a2c-852b-e8801df74b7f | -10.8616 | -45.4248 | 2025-10-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 47665d3b-05fe-3599-98b9-2ec839cb3d54 | -14.4255 | -46.115 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 154.9 |
| d1afe0ed-0c5c-309d-8b85-68e4d2cc38eb | -9.9365 | -43.7657 | 2025-10-02 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 227.6 |
| 7172499c-e28f-3c2f-ac20-4ab7c581eb92 | -6.6955 | -48.7062 | 2025-10-02 02:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d61e1a21-0c70-32d3-b136-84ac2877caf1 | -16.0217 | -50.9207 | 2025-10-02 02:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 566ef377-9d50-3524-b423-9b0c845e437d | -17.8812 | -57.6206 | 2025-10-02 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| acd1b461-7920-35fa-ab87-f7c772781e79 | -14.4065 | -46.0953 | 2025-10-02 02:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 765a05ce-0476-376c-9888-79ac21ffd833 | -7.7563 | -42.541 | 2025-10-02 02:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 9554d616-1b56-34d5-9795-5f0e627f1045 | -10.8433 | -45.3815 | 2025-10-02 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 129eaa8a-8529-3152-b615-e0b6383868f7 | -6.7213 | -44.1387 | 2025-10-02 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 521ea32a-bb36-3f4c-a814-d5d038ebc633 | -9.9369 | -43.7422 | 2025-10-02 02:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 226.5 |
| e5f9e8a0-8ef6-3151-943e-278f0aff6354 | -14.4255 | -46.115 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 6f8d018f-a7c5-3f57-b702-14b5a156b156 | -7.7755 | -42.5152 | 2025-10-02 02:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| d2a708fa-4ffa-3341-bb32-4c859550ba9a | -9.9365 | -43.7657 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 277.0 |
| f059f257-682d-3208-845d-ce7e50ce4958 | -9.9372 | -43.7187 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 157.9 |
| 313c0a93-9825-39f7-b876-a5a2aac4a5cf | -6.7213 | -44.1387 | 2025-10-02 02:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c35a7fe3-d458-37d1-953e-fd025fd012c1 | -10.8234 | -46.6313 | 2025-10-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8bafad39-1e13-3261-8588-324d5205d8b3 | -14.3114 | -45.9967 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| fd4eb8c7-3887-319b-91d9-16ec61197729 | -10.8237 | -46.6088 | 2025-10-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9837d2a6-0c80-35b5-b56f-0854d1499d75 | -16.0217 | -50.9207 | 2025-10-02 02:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e99b5c51-ad31-354d-be86-e51e1a99faed | -7.7752 | -42.539 | 2025-10-02 02:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 172.0 |
| fa8f29b2-5111-375b-a66c-78ea11882ab4 | -14.4065 | -46.0953 | 2025-10-02 02:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e9e9c61f-d79c-39b8-9e66-f7f1f020d565 | -9.9361 | -43.7891 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 2c1dc189-8334-316c-98e3-2e474038df7f | -11.1746 | -47.2805 | 2025-10-02 02:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8c75b8a3-1de1-373b-a926-061ea4aa8d05 | -9.9559 | -43.7397 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 2c4228a3-0794-3caa-8b05-1c8c991d93de | -13.1739 | -47.8317 | 2025-10-02 02:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 42e7048b-110b-3adf-ba30-ec5d61a8f874 | -9.9369 | -43.7422 | 2025-10-02 02:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 263.1 |


[Clique aqui para ver as próximas entradas](README15.md)
