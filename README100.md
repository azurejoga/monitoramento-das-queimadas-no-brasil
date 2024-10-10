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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff8c8675-cc07-3960-bb93-3ec03eabac60 | -12.19431 | -46.73224 | 2024-10-10 04:44:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64023b6e-4986-3bc4-a174-28c4f701b149 | -12.17413 | -47.57225 | 2024-10-10 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6f1b21d-fe14-3774-b509-b4d01c729cd9 | -12.17019 | -47.57167 | 2024-10-10 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75bbcd7c-a4a3-3da5-b7f7-dc61f2bfe949 | -11.79544 | -47.39435 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa0cd531-7e1b-36cf-93b5-bdda05ead066 | -11.7922 | -47.38864 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecb077eb-01a7-33cb-9753-b858bee07cea | -11.79147 | -47.39379 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33b650e0-1fb8-385a-92f1-e8cbba341e5f | -11.78824 | -47.38804 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7058a9b-20f4-3af3-bf05-8669bb499378 | -11.42354 | -47.1716 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7a2704f-1f2a-3ba2-8a02-54109268ea23 | -11.41955 | -47.17098 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 414d75af-2a9e-3b49-a899-81dcabd988dd | -11.41157 | -47.16972 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa32a240-5277-3d2a-84ca-a2cae3787294 | -11.40759 | -47.16908 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1feeebd3-0702-38eb-9dd9-0613e3be6a3a | -11.40162 | -47.18245 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68dad5ed-0a76-39fb-b04d-357f4f19d723 | -11.39763 | -47.18179 | 2024-10-10 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ec33952-fea9-3932-98b8-409cdf861230 | -12.34376 | -47.67615 | 2024-10-10 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 491d8246-52c5-3d93-b889-429e95759994 | -12.28451 | -47.64199 | 2024-10-10 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b069e073-953a-3cdf-b61f-c25350000491 | -4.92681 | -46.73927 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99ae6fa4-f2a0-35d9-9892-6a3e065febbe | -4.83845 | -46.86164 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a368cb-177f-3e0c-9c28-be4c3e5b4b41 | -4.83434 | -46.50753 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 580bed4e-bf19-37ba-b7ef-1b3684ce44e0 | -4.77818 | -47.05957 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f95d24-e7bf-3a5b-8065-f9ac64a0ce54 | -4.92303 | -46.73879 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e07811a7-077a-38ff-a745-cfcccf8d1865 | -4.85012 | -47.52002 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3a13216d-6156-3ef0-9a98-302f21547baf | -4.84652 | -47.51947 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 941ce9a3-10ff-369a-bbb2-66430988ea8d | -4.8354 | -46.8566 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da5e931d-734e-3ba4-ab29-50fab7f7b068 | -4.83333 | -46.51016 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da2f6630-acd2-3620-8c44-03586fbd9780 | -4.83052 | -46.50699 | 2024-10-10 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d35d520-28ac-359b-883d-e3e7fff7b6d9 | -4.77449 | -47.05902 | 2024-10-10 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 667086b3-ad23-3470-9a21-b1d2796a6b22 | -6.53747 | -47.11489 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1249c05-6b8e-3acd-9c71-7ebd83c47575 | -6.53679 | -47.1194 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72dd4f62-abab-3868-a430-248a4e9ee768 | -6.29206 | -46.99837 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d932ee-cb50-3b09-9737-48ab7505dc0c | -6.0766 | -47.27276 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1951d1b4-7cdb-39e0-a99b-2126e691b88f | -6.04999 | -46.5969 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84667a44-b72d-3b36-9e88-bad4b566874a | -6.04928 | -46.60168 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96d380e9-a593-3ca6-829b-519b3e9372f6 | -6.04858 | -46.60643 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87cad297-31cb-3f06-b2ec-4b421a1b657e | -6.04543 | -46.60115 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf8d045a-7e77-3c15-9fd9-70fb9ba28e12 | -6.04158 | -46.60056 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d0cdf17-4e56-3530-92a5-c47e3638fd12 | -5.91901 | -47.71933 | 2024-10-10 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 733d9ce9-d6df-37ed-9237-8df599436bc1 | -5.27236 | -47.69213 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2174a4c-0a59-3eb3-87ad-2c423698c762 | -5.85493 | -46.6114 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ecd30f9-3af6-3194-b21e-7102c2101d8f | -5.84087 | -47.42337 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45ebc385-43f5-3f33-aced-f8660a2fc1d6 | -5.84022 | -47.42764 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bda894ed-6da5-39fd-bb5a-3cd3a7cebf19 | -5.83957 | -47.43189 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ffa8f59-414a-3ca1-a6c7-d2f48a531a16 | -5.83785 | -47.41855 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a26f7971-b30b-39a4-a77a-0fc593bf2206 | -5.8372 | -47.42282 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0a84146-fe25-37dd-b64e-1135fd0fa60e | -5.83656 | -47.42709 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6fcfa88b-fcff-3b33-a66d-40c5bf9c7d2c | -5.83592 | -47.43134 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aeb721ee-de5d-37f1-9a01-d9dc9fcf8eb0 | -5.83355 | -47.42226 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef8878c3-ff4e-33e9-ab74-ffee18439870 | -5.8329 | -47.42652 | 2024-10-10 04:44:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99a00a90-9c58-3c23-a8b8-d5b9c2d0506c | -5.83226 | -47.43077 | 2024-10-10 04:44:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebc6f35e-9d23-3dfb-a696-b810191aa85c | -5.78094 | -46.51508 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5404b751-d4c6-39be-8203-4e81a8550648 | -5.76314 | -46.58073 | 2024-10-10 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a04cda3a-0f96-3ffe-9441-787cbe60ce7c | -5.57425 | -47.25984 | 2024-10-10 04:44:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 085c7991-2d7c-3140-ba7c-55f0b4642515 | -5.54812 | -46.69862 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91cf31a8-570a-3588-bea5-bdefe6ff2868 | -5.54051 | -46.69751 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73677ef2-dc05-39c9-a934-47dfc1236b11 | -5.53741 | -46.69233 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6528d43e-462d-39d8-901a-ad959aadae6a | -5.52278 | -47.10038 | 2024-10-10 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfcfcacb-5366-3c2c-93a7-90532ac09298 | -5.51839 | -47.10437 | 2024-10-10 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8f15cbd-390d-3589-b164-215397c7b407 | -5.49575 | -46.91565 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aa817d9-b017-3531-9a11-c53c538c624b | -5.492 | -46.9151 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c12f7873-1ae5-3418-bd8f-63e077cf3207 | -5.4746 | -46.85217 | 2024-10-10 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2964c599-50b3-3925-a145-fcbf0081eaeb | -5.4394 | -47.82718 | 2024-10-10 04:44:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e9fdb4b-a1d7-33e3-b0b2-f7c011ce48b3 | -5.43537 | -47.6842 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 275ceb53-3b4d-36d7-8222-a728a0828e77 | -5.43475 | -47.68833 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad409148-c1ca-35d2-a67a-4822dbc737b7 | -5.43178 | -47.68362 | 2024-10-10 04:44:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff0eb117-7901-34ff-aeb3-af01e08318d3 | -5.4076 | -47.68608 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c4130e3-ca9c-347f-858d-10aaf1d545ee | -5.40601 | -47.68392 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10375d2f-3123-3bdd-b32c-36d567968ab7 | -5.4054 | -47.68804 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7fa9ca25-b464-3ac2-b85c-98e8df4782d0 | -5.40401 | -47.68555 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9386bfe-5543-39dc-9217-19bab138d378 | -5.40338 | -47.68966 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 096f4a09-bb06-362f-bb81-470213a15928 | -5.39682 | -47.68447 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71433b61-c3b7-3db1-81af-e5e9ef9e22f9 | -5.273 | -47.688 | 2024-10-10 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd604b98-402f-3029-a923-ca139b88bd67 | -5.15535 | -47.60452 | 2024-10-10 04:44:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 249969c1-53f0-3620-9c28-72b845dd1a82 | -6.29273 | -46.9938 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824071dd-f6df-31da-9fac-3f65772f11e7 | -6.28896 | -46.99323 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52db3bb8-bd27-39ab-ac08-64916930fb78 | -7.13742 | -47.7471 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f3cea32-38bc-3617-ad7d-9c70cd1767a3 | -7.13584 | -47.83321 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a70eedf-d1f6-3d53-aa50-e305d5e23886 | -7.13329 | -47.74916 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eca1aa99-35a1-3ecd-aafe-c86c054dabbf | -7.13224 | -47.83242 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb1e5c7d-d7b9-3541-b5a4-2ffa5b74eb65 | -7.09067 | -47.85855 | 2024-10-10 04:44:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 309a5d8d-6e97-3778-be93-a38fab5fb383 | -7.02526 | -47.37146 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0c5753e-e8ee-3060-a55e-931b5c386a2b | -7.02396 | -47.38023 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3f37961-3140-3b13-a64f-ee962a631742 | -7.0218 | -47.21372 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11370867-9b24-34b3-a3de-bee02b47cf66 | -7.01186 | -47.20287 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f075971-f58e-35cb-92e9-e4be460c6ef4 | -7.00986 | -47.21659 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20a8149b-85c0-3caf-97bc-65b7a8db9f26 | -7.0092 | -47.22107 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbcfd90a-0cf8-3657-94b7-b8b08151959b | -7.00723 | -47.23457 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbae95af-2144-3962-ad2c-6521186a01f9 | -7.00413 | -47.22949 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 344df964-ef2f-3803-b7ff-b6172c1d7a8d | -7.00039 | -47.22888 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a51dc173-918a-3a56-80d4-86d226106ef0 | -7.00005 | -47.22637 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e00b1520-b529-3f63-82a8-11aec866ce8a | -6.99936 | -47.23091 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c4aeb09-5203-337f-8084-e681f4a69b51 | -6.98348 | -47.39679 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48bf57e7-13e5-3c22-bdce-22523f98cb78 | -6.9824 | -47.37822 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ebe4be7-9163-374c-8aad-33c9b492ee3d | -6.98174 | -47.3827 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06ef78f2-fb7b-33c4-a46b-eb99c13ab9d8 | -6.97869 | -47.37757 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e84b1aa3-3262-3c82-9a16-7621e80bd7cb | -6.97848 | -47.40498 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2075311-e177-392e-b7f4-4f7b619ead05 | -6.97738 | -47.38652 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 676e6d1c-947a-3995-bc26-9c7f1b7256ad | -6.97673 | -47.39101 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16699d84-2606-3064-8e37-7246f8eefb19 | -6.97607 | -47.38377 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31f5536e-4be7-3795-96f2-5be0d8d679b8 | -6.96425 | -47.38649 | 2024-10-10 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ba4e7d1-db38-3bb4-8e7c-2be997ab2a00 | -6.93472 | -48.17102 | 2024-10-10 04:44:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c345e52d-8e58-3432-8731-da87b216ed80 | -6.84357 | -46.92662 | 2024-10-10 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README101.md)
