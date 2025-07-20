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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6864ad4e-71bc-310a-b9fb-afd5b273fd51 | -7.7005 | -47.2976 | 2025-07-20 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 36cba33c-e948-3c4b-b5a1-744ea8e3bb04 | -10.9811 | -45.1104 | 2025-07-20 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 362.4 |
| b3f32d5e-b19f-3416-b7e5-8eed01378cea | -7.7007 | -47.2755 | 2025-07-20 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 5fcf3199-63c6-3da3-a136-2e68aa8fd9a8 | -10.962 | -45.113 | 2025-07-20 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 432.0 |
| 8ca79b2e-9620-3113-a519-64933cc1cfc0 | -10.7404 | -52.5123 | 2025-07-20 00:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 6c8591ca-d692-3268-a05d-7ae9be238a09 | -10.9624 | -45.09 | 2025-07-20 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 93e78a66-9272-3316-9c43-5c9dd5bb282f | -3.1198 | -47.0075 | 2025-07-20 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ce046f85-f45c-3b47-859c-7bd0f574768c | -10.3785 | -62.7622 | 2025-07-20 00:00:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 38c44782-5a8b-3982-a889-f5e5c144f81f | -10.9815 | -45.0874 | 2025-07-20 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 5636a981-a7a1-3251-ba89-0608e58d3e0b | -10.9624 | -45.09 | 2025-07-20 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| db9fa6dd-cae8-3b4f-94d3-3bbb4ef84157 | -10.7067 | -46.803 | 2025-07-20 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 43c1e6d0-169f-3145-9b8a-1e8de11f8485 | -10.3785 | -62.7622 | 2025-07-20 00:10:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fcfce906-7b2f-3a4f-9db8-2f457dafd7cf | -10.9815 | -45.0874 | 2025-07-20 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 313.2 |
| 9b1d5a82-c8ac-30ca-9dce-cc64857e8477 | -10.9811 | -45.1104 | 2025-07-20 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 410.6 |
| f6dadf74-8cea-3967-a13e-5a10aa1ec623 | -7.7005 | -47.2976 | 2025-07-20 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0bc43959-c1b7-3a30-8438-966198f98795 | -10.962 | -45.113 | 2025-07-20 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.6 |
| 2b520226-e12b-3327-b0d8-a32e0fc7e686 | -10.707 | -46.7805 | 2025-07-20 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 384176fc-b6d3-378b-87fd-9f69ae34a018 | -7.7005 | -47.2976 | 2025-07-20 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 1b80a83a-0652-3531-b260-6d9accfc34de | -10.9811 | -45.1104 | 2025-07-20 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 367.7 |
| 6c122ca2-fc76-3996-b424-e5bb768d2fee | -6.9145 | -45.4011 | 2025-07-20 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a10a250d-3e1c-366d-9714-f940cb7a2c56 | -3.042 | -47.8607 | 2025-07-20 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| eac063ee-20cf-3cb9-8468-dddfbda1cdf9 | -10.3785 | -62.7622 | 2025-07-20 00:20:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 6b83481f-46ad-336c-9317-9691d9752ac7 | -10.6876 | -46.8053 | 2025-07-20 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 486.6 |
| cbbcfcd3-9638-3d35-b50f-703eec24a857 | -7.7007 | -47.2755 | 2025-07-20 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e104c37f-2ab3-329d-a25a-81ac44657d47 | -10.707 | -46.7805 | 2025-07-20 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 2efe1ce7-be29-32e3-aa28-98d2aebba5db | -10.7067 | -46.803 | 2025-07-20 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 243.7 |
| 2b15b781-ef78-39bb-a4ef-daf54a39f46e | -10.9624 | -45.09 | 2025-07-20 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| b6781653-9d90-337b-8cc9-6e28b6f73af6 | -10.962 | -45.113 | 2025-07-20 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| ad37183e-f4fe-38a4-b3e6-f52177a62c4a | -10.9815 | -45.0874 | 2025-07-20 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 8f5f1d80-fc08-37a1-8710-5c16d4e8f61c | -10.688 | -46.7829 | 2025-07-20 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 259.7 |
| a72ced2f-1143-3742-9e09-72d1fe35900a | -10.7067 | -46.803 | 2025-07-20 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9c8abacb-7d3b-3aaa-ab07-3c9c82b222b2 | -7.7005 | -47.2976 | 2025-07-20 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 80e208ea-8d33-3ee4-bacc-1bb1c48b2317 | -7.7007 | -47.2755 | 2025-07-20 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 536737f0-ed5b-324c-af9d-2b2730465749 | -10.688 | -46.7829 | 2025-07-20 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 234.1 |
| 234911c0-2978-30a4-9f1f-84db2b256121 | -10.3785 | -62.7622 | 2025-07-20 00:30:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 627cfbd3-75c8-331b-86ec-6a9b2fb491b5 | -10.962 | -45.113 | 2025-07-20 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 337e4afb-8ce3-341b-9f66-fda5b0c8c8ff | -3.0235 | -47.8613 | 2025-07-20 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a02433ab-403a-3f4d-9c04-3585d3f4cb71 | -10.707 | -46.7805 | 2025-07-20 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 7152dad2-2378-33cb-86be-992eab3bbb0f | -10.6876 | -46.8053 | 2025-07-20 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 437.6 |
| fffd9cc0-7681-3f9d-a312-4a7a2cddb50a | -10.9811 | -45.1104 | 2025-07-20 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 294.3 |
| ea69a732-7f92-3fb1-a8e6-a36c071b3eaf | -10.9815 | -45.0874 | 2025-07-20 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 885ad059-e279-3230-a51c-1e75474f131f | -10.9624 | -45.09 | 2025-07-20 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| eb25e3ce-e851-3a2f-bc19-9dd90f5e2145 | -3.042 | -47.8607 | 2025-07-20 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8f458691-856a-3a83-9d16-4772a3e4db27 | -10.707 | -46.7805 | 2025-07-20 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cb4c5f34-247e-32ee-8a2e-84923428ff6b | -10.7067 | -46.803 | 2025-07-20 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 96c3d193-04ae-3e5f-b07e-7f27f0c27bb6 | -7.2773 | -50.3293 | 2025-07-20 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 14e0ba86-553b-3faa-acd9-102009b28018 | -7.7005 | -47.2976 | 2025-07-20 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d15e5200-51de-3399-9656-3168f6ed063c | -3.0419 | -47.8824 | 2025-07-20 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1f54ccb4-4929-3769-a47a-5f4699eaf5e1 | -10.688 | -46.7829 | 2025-07-20 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| fca0b2bf-a83f-36cd-980b-59df8c1f9a7d | -9.6158 | -49.0166 | 2025-07-20 00:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f2f29a82-4a56-3a1a-bfab-a5d9e8d68449 | -3.042 | -47.8607 | 2025-07-20 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5a4f369e-fdd0-3635-8e77-3859f77594e3 | -10.962 | -45.113 | 2025-07-20 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| ce6bd7d8-b1af-39c3-9cba-bceed9a59b1a | -10.6686 | -46.8077 | 2025-07-20 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5161da33-edb7-3aed-b0a1-2eb19e2f4045 | -10.6876 | -46.8053 | 2025-07-20 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 5bfc43cb-d415-337f-b704-957f715ee992 | -10.9624 | -45.09 | 2025-07-20 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| d01c37c0-5d9b-32a5-8407-98ae5e831bdd | -10.9815 | -45.0874 | 2025-07-20 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 195ba84e-83cf-37a7-b743-de03e15ca0f3 | -10.9811 | -45.1104 | 2025-07-20 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.8 |
| 1c3b850b-757d-3b11-8619-6a8200d91293 | -10.3785 | -62.7622 | 2025-07-20 00:40:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 68c4bda0-defe-3fb8-b4e9-a02c711e2fef | -23.33788 | -51.91008 | 2025-07-20 00:41:00 | TERRA_M-M | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 973e5d65-bc96-3d86-b5b1-5b76215e8db0 | -19.89922 | -45.03881 | 2025-07-20 00:41:00 | TERRA_M-M | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c70b5fce-8321-307f-8c1a-a54e13277795 | -23.24979 | -47.11515 | 2025-07-20 00:41:00 | TERRA_M-M | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b371f7fc-0568-33db-94e0-36b1892baf30 | -20.02895 | -47.7161 | 2025-07-20 00:41:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 21bb9feb-8fff-3596-93d0-8e098278dbe3 | -20.02764 | -47.70674 | 2025-07-20 00:41:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 1124f65f-b7ca-324d-93a6-4a1d3234fa21 | -22.43559 | -48.99404 | 2025-07-20 00:41:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fd665646-6d09-39c4-ac60-74776843933e | -11.45982 | -48.158 | 2025-07-20 00:43:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 97aee962-b48a-31b0-a78e-02f0cc047bd0 | -11.83523 | -47.50106 | 2025-07-20 00:43:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 67d6a4fd-d4ca-330f-b51e-7bc0f7bb347b | -11.49352 | -48.07723 | 2025-07-20 00:43:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 31dad487-1599-31f7-ad3d-5e00a851c264 | -11.48368 | -47.32008 | 2025-07-20 00:43:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b2e9e62a-d084-37b9-936c-174c3c0056ac | -11.82583 | -47.50255 | 2025-07-20 00:43:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b1bee97f-ba5f-33ca-aebd-808a78bc6ea1 | -16.08546 | -45.17194 | 2025-07-20 00:43:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8e105d0a-822e-3298-b557-c2590d8d6c59 | -14.48464 | -46.35954 | 2025-07-20 00:43:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5c2ca340-2f27-302d-bb00-5674e3edff98 | -13.89748 | -50.65593 | 2025-07-20 00:43:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 00757e21-bbcf-3165-b64c-b81f1b6802c6 | -12.35435 | -50.32954 | 2025-07-20 00:43:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 48cf7adf-ee45-33a5-8e24-1ec0c6c1726c | -11.56213 | -47.0947 | 2025-07-20 00:43:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cb129a15-d439-3ac9-94c1-100be93f50b5 | -12.65928 | -47.09899 | 2025-07-20 00:43:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| d1ac0264-24ed-3501-b725-6644cd0061d8 | -12.36402 | -46.42803 | 2025-07-20 00:43:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b15b386c-0337-301f-8a8a-ef740c257053 | -13.71033 | -42.51669 | 2025-07-20 00:43:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 9afcd2c7-d4ba-39a6-b48e-4d0cd43c36a3 | -10.9699 | -45.09237 | 2025-07-20 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e7e53fec-55ac-3256-9528-b285e5600f46 | -10.96101 | -45.10886 | 2025-07-20 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 70f2db8b-c9b1-321e-8527-d443829cba9f | -10.97453 | -45.12202 | 2025-07-20 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 64937ac6-30f2-3024-8481-95316747a8a4 | -11.57176 | -47.09316 | 2025-07-20 00:43:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 368014cb-efba-3d87-a88d-782bef1b177b | -10.97222 | -45.10719 | 2025-07-20 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 698.2 |
| 90bb830c-ed48-309a-b5e1-c67291b4f24e | -13.89876 | -50.66549 | 2025-07-20 00:43:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dd2dfcfe-97c4-3381-b974-7e633a165f32 | -11.46121 | -48.16766 | 2025-07-20 00:43:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ad241c19-fe55-3d7e-9d7d-ee3074d68001 | -11.55248 | -47.09619 | 2025-07-20 00:43:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 70c38623-5666-35da-8b03-760f21864dc3 | -9.80407 | -48.56734 | 2025-07-20 00:45:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7b22b41e-d2dd-34d8-83d8-272b03415b4b | -10.70009 | -46.80776 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d54baf64-1d7f-38a0-a950-bfc6e5c947d1 | -7.7027 | -47.3048 | 2025-07-20 00:45:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 60be85c5-7ff9-3073-b27b-ec3080393179 | -10.67849 | -46.79929 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ec809593-dd89-3e52-b505-18203cb9df66 | -10.63187 | -48.09996 | 2025-07-20 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5aba8e81-02c2-3342-b9e3-bd1b24f8d95b | -10.73177 | -52.51078 | 2025-07-20 00:45:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1303c7d4-3876-3217-a3b7-2c284157c96c | -9.5248 | -40.35325 | 2025-07-20 00:45:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| f8ce0fc5-6870-343d-8f23-a554936d2f3c | -10.69837 | -46.79619 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| f351fec6-4887-3fae-b240-f5b7dde37c1d | -10.63477 | -45.23247 | 2025-07-20 00:45:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0aa58001-32b0-3245-b56b-df451ddbc999 | -9.91059 | -55.53533 | 2025-07-20 00:45:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 54835b16-9096-34a9-8d0d-1e0be5a2559c | -7.71105 | -47.29182 | 2025-07-20 00:45:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3beba68d-6dac-3da2-8fe8-6aee9540a4e5 | -7.69926 | -47.28164 | 2025-07-20 00:45:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f17566d-a306-3479-849b-c5591af71eb0 | -10.68844 | -46.79777 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| eb88efd7-a963-313d-a500-56fdc6221139 | -10.63046 | -48.09011 | 2025-07-20 00:45:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9ff7eefb-2bc7-3640-b5c1-a86de94f86ea | -9.80268 | -48.55778 | 2025-07-20 00:45:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README2.md)
