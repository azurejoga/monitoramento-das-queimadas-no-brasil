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
| 82f635a1-893a-3f49-9813-8c2cd2091b3f | -3.26965 | -50.36007 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3cc1e559-d44b-3af7-8890-359eaf15cc85 | -3.26161 | -50.35468 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 228.5 |
| 15aa79ca-ef1b-3e48-8ea6-4745242314d5 | -3.25859 | -50.33131 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| cbfe1698-eb25-372c-ab53-168fad02bf8f | -3.2558 | -50.36193 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 1b4d4f6e-8e6a-34ee-87c2-786e6a9e1649 | -3.25262 | -50.33859 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| a43a33e0-e88c-397f-8bab-73be9ec28d14 | -3.23853 | -50.58917 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 2576d18b-5c2d-34c6-9641-82b8ceefd34e | -3.23585 | -44.4139 | 2024-10-30 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 218f3257-5aaf-3e24-8e8d-935580fb7153 | -3.22883 | -50.58501 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 64c28f02-a90a-3984-b176-1aeb11839874 | -3.22443 | -50.59105 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d3de74b6-7ca0-36af-9ee7-a0d355015209 | -3.18387 | -50.40103 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 45e31edf-1a04-3e8a-b332-d01d971120c0 | -3.18214 | -50.59678 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 70136dc9-f7e1-3366-bf9d-04d724e5165f | -3.18063 | -50.37757 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 16a01b58-5db6-3af4-80ba-f3c827692c44 | -3.17578 | -50.39676 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e45540c0-a7b9-38e4-88bd-0dbcad0cd512 | -3.16805 | -50.59871 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 3c804088-d151-3a9b-81a2-d437a8e8c54f | -3.13627 | -44.96096 | 2024-10-30 00:33:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00c82323-625f-3177-8ff9-45f374e24216 | -3.13493 | -44.95128 | 2024-10-30 00:33:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 10547392-d1f4-3755-b441-476b55ebaddd | -3.11513 | -51.10741 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| ebd6d048-5057-31fc-b628-8cfd228d9c7b | -3.11446 | -51.11282 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 4e859790-a670-3c43-b396-05c0e5c32d6f | -3.10048 | -51.10962 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f27fec38-6741-3734-952a-e867278f9b3b | -3.05214 | -45.08817 | 2024-10-30 00:33:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 80b501d0-a11f-3142-9e2d-73391b75d92d | -3.04284 | -45.08946 | 2024-10-30 00:33:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5043a2ae-9f16-37b3-846d-2b428592ae5d | -3.00655 | -49.59022 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 54906037-b2f6-337c-a73a-6568c1de1e16 | -3.00501 | -49.58394 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0959a071-684a-3fd8-a158-880537dfe01f | -2.91251 | -52.58775 | 2024-10-30 00:33:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| a7dd2335-a0a6-3fd8-9480-7209e56d0de0 | -2.90575 | -52.59327 | 2024-10-30 00:33:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 17c9742a-0a47-3b55-bc6c-83e4939b2d97 | -2.84415 | -49.25559 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| bf4f7687-c99c-361e-ba3c-44c94c23c684 | -2.84169 | -49.23682 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 00371856-4b4d-3a33-9173-570b5e364a2c | -2.84046 | -49.24254 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 85156579-a641-36b0-883c-a05c74b7bf50 | -2.83785 | -49.22377 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 97b40b7e-a4b8-3495-8a02-5c1169d13ff2 | -2.82791 | -49.24424 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5d600f73-46d0-3881-8be0-fae5de4bdc83 | -2.82533 | -49.22552 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| aec7f0ac-e7e5-31ab-b87d-f77e4775c089 | -2.81281 | -49.22725 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 2217ac06-e7ae-3a22-a6cb-3a9162625d28 | -2.81026 | -49.20859 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b25dcee5-5d7e-3877-b2cd-b4045c0335eb | -2.75817 | -44.75546 | 2024-10-30 00:33:00 | TERRA_M-M | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 907a5557-d214-32f7-9abe-98204749d98a | -2.7212 | -46.70687 | 2024-10-30 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20847a7c-9b96-30dc-93ad-aec499dfc72c | -2.71957 | -46.69485 | 2024-10-30 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4207448e-bf9a-3fb3-833b-f7b530b01bbd | -2.71793 | -46.68284 | 2024-10-30 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f32a84b-d473-3278-b9a0-e4c447da4704 | -2.61121 | -48.2562 | 2024-10-30 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ccda2344-418f-308d-b54e-04608f8b684c | -2.58432 | -48.40415 | 2024-10-30 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8212808b-0774-3896-87fc-1aa9deca07a7 | -2.53744 | -45.15663 | 2024-10-30 00:33:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02f880c7-f8b1-3ce4-b7cd-55b7cafa3aa4 | -2.51991 | -47.44456 | 2024-10-30 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5d35f51a-ca9a-3bbb-ad7a-b6b133b096a2 | -2.51414 | -47.45274 | 2024-10-30 00:33:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 526185b9-3c70-3cb3-af91-fe7e307bd56c | -2.48584 | -50.4911 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 66d71d03-5cc4-3634-a014-5c34f1fc4d00 | -2.47978 | -50.49732 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1171674d-d6c9-3279-9d31-fa7d82bce728 | -2.47652 | -50.47415 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d0309df7-3f8f-3060-b42a-bd05a0ba5b0e | -2.44756 | -48.48394 | 2024-10-30 00:33:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 239505ff-5d8b-3749-947c-55960c4d0c87 | -2.41644 | -46.7123 | 2024-10-30 00:33:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f0737c0f-9b67-3496-ab63-b81a3772c785 | -2.41475 | -46.70038 | 2024-10-30 00:33:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eac9746e-9640-30ba-9433-a06275970fdb | -2.39439 | -48.94081 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 29f8445f-72c3-398d-9fec-831c33896f15 | -2.38562 | -44.8608 | 2024-10-30 00:33:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d070c10e-49b6-3eb3-a4c5-6066c8d44a1c | -2.38226 | -48.94253 | 2024-10-30 00:33:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 43926065-d288-3008-8ebb-695716ee7bdd | -2.36507 | -50.33264 | 2024-10-30 00:33:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| fe907ff1-1179-3064-85aa-27fde8ee3f24 | -2.3619 | -50.31018 | 2024-10-30 00:33:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d7a3ec5a-2231-3afb-87e2-e043cfbf819a | -2.35874 | -50.32705 | 2024-10-30 00:33:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d97fd4e3-9d6f-3fb5-a76c-071295a47f99 | -2.34178 | -46.47266 | 2024-10-30 00:33:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9d341cfb-3c9b-317f-b7df-98a8fa50dbd8 | -2.29009 | -48.50127 | 2024-10-30 00:33:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7d27dc08-d397-3ae1-af5d-4f5f153be6be | -2.20588 | -50.60115 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 310fca54-6bd2-39e6-a2e8-419491f69951 | -2.20258 | -50.57766 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a783bc1e-92df-3818-87d6-a1265960415b | -2.19769 | -46.98959 | 2024-10-30 00:33:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 95008af8-7446-339f-9fd2-f6b4e5394cb1 | -2.19761 | -50.59569 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d2d6d48e-f260-30b7-9adb-5ef39069db9a | -2.19452 | -50.57224 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 1c72ec2a-c8bc-32e9-acab-c1d546f41401 | -2.18875 | -50.57958 | 2024-10-30 00:33:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 07383335-198e-3a62-8d9d-300fa84462b6 | -1.84504 | -47.10057 | 2024-10-30 00:33:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da3284bc-559a-3d97-b2e8-88ce6d9882db | -5.31632 | -41.03559 | 2024-10-30 00:33:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e339f896-5f3f-324f-8fb1-6a48e71eb197 | -5.30718 | -43.07466 | 2024-10-30 00:33:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34fbe342-ebc9-3063-8dec-76203dd4c177 | -5.2717 | -41.23891 | 2024-10-30 00:33:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6adca3bb-91d9-33c5-b3e2-fe082f8871d0 | -5.07957 | -43.3612 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 78e130e0-307a-31ec-b96e-a9d05ff6fba1 | -4.98721 | -42.29524 | 2024-10-30 00:33:00 | TERRA_M-M | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 115a24c0-fc2d-36a1-a0dc-9ce01b0232e1 | -4.93623 | -43.18768 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77a907d3-ddea-3b37-9b5b-3828c6efdfea | -5.43577 | -41.03159 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7727326c-3764-368b-b8a1-9dba2fc29ce9 | -5.43711 | -41.04097 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 59e1d4e1-f691-3630-be31-fcadf717abfa | -5.45155 | -43.17794 | 2024-10-30 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25dbd742-692d-3efd-a733-8e0099a00382 | -5.45278 | -43.18684 | 2024-10-30 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 20c96450-870c-3e88-8921-c2374acccbe4 | -5.46042 | -43.17667 | 2024-10-30 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f45385a-ca50-36b1-8222-3485e3a97b3e | -5.46165 | -43.18557 | 2024-10-30 00:33:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| abe65ad4-51b4-3b81-b57b-98e1873f89ba | -5.49231 | -41.36439 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| a77b5520-001b-38b4-af86-24781f545807 | -5.49361 | -41.37359 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4c824868-5402-32fa-80be-2519f89bbc5e | -5.57086 | -43.71268 | 2024-10-30 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e72dae6e-8651-38ac-8b07-3e6d5ed1452d | -5.67211 | -39.90731 | 2024-10-30 00:33:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 72363211-0894-3c34-9cb0-760281d345e1 | -5.67357 | -39.91751 | 2024-10-30 00:33:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ec1a2c7b-5940-3442-add8-9d37dbff9f44 | -5.82543 | -43.2831 | 2024-10-30 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 153ef6ac-90f9-32dd-81d8-a0890d69241e | -5.92634 | -43.68529 | 2024-10-30 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7df9c4d5-b57e-37d3-8c2a-decb91e2c3a2 | -5.93534 | -43.68401 | 2024-10-30 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| aba6c006-1a6e-327d-b8ba-78394c7e7193 | -4.85565 | -42.47932 | 2024-10-30 00:33:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 59394702-0f80-348a-ab20-f23fa9b71c3f | -4.85442 | -42.4705 | 2024-10-30 00:33:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| b599ddf9-69a3-3dc8-9046-480663e61a82 | -4.66407 | -43.81712 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 834ff2f4-d10a-3c90-b03b-cc0f6957314a | -4.6551 | -43.81838 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 673cd33c-641d-365a-a720-712e29671213 | -7.3333 | -41.87263 | 2024-10-30 00:33:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 42b55eab-0850-3a52-be5c-41539e6a8717 | -7.33206 | -41.86377 | 2024-10-30 00:33:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 61839681-a328-3e77-9534-924655ac6183 | -6.992 | -41.34683 | 2024-10-30 00:33:00 | TERRA_M-M | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9165d27d-e827-3694-9bc0-2e526c293270 | -6.0915 | -43.54706 | 2024-10-30 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a56b8505-de7b-3b9c-85e8-68c157f21c79 | -4.51416 | -43.12725 | 2024-10-30 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 5b17f5f5-5ced-3d51-9098-abfce21ed3e0 | -3.94999 | -41.47264 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| bab1906a-7add-34dd-a7d3-c37f9ddebb1b | -8.28035 | -43.66597 | 2024-10-30 00:33:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 94744a18-83dd-32d5-8562-44d15a041576 | -7.91897 | -42.83823 | 2024-10-30 00:33:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| d3ec367c-edc1-3e6d-ab9c-a1c68cd8f55a | -7.81433 | -43.21743 | 2024-10-30 00:33:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6cfb2722-e9e5-32f2-883c-e6d5ee1f62fa | -7.69795 | -39.52901 | 2024-10-30 00:33:00 | TERRA_M-M | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| a17ade1f-ec45-371b-967d-02d220e5524b | -7.56241 | -38.75526 | 2024-10-30 00:33:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7a585f8c-e159-3764-a648-7f057bb3da2d | -7.3257 | -41.88277 | 2024-10-30 00:33:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c8f7a507-bb06-3e84-91fc-9a25b61f58d2 | -7.32445 | -41.87391 | 2024-10-30 00:33:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |


[Clique aqui para ver as próximas entradas](README10.md)
