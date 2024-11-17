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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc6fd51c-db52-3990-85d3-dd504d0c765d | -2.66257 | -46.20885 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d5d9d54-ddd6-3573-9c58-2a68f8890683 | -2.30275 | -48.48781 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b12d24dc-4b94-351f-a7a9-4eccc64e376f | -2.07868 | -50.34751 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abdf3cf0-0804-3e9e-afc5-31b63aa33012 | -3.22921 | -45.40142 | 2024-11-17 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0f1eaf0-f42b-3e5c-8633-a792824dff88 | -2.66799 | -46.17407 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dae345b7-766b-3ed6-8627-8df648dd7c03 | -2.85247 | -46.66646 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39b826b8-c238-3355-8058-efd3ffea2b30 | -4.74072 | -48.11746 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e75a4b9-d09d-3dd5-9fa0-de076961dc39 | -2.3686 | -48.53146 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8974aef0-fb32-3ec6-b7da-fe34f2148f20 | -1.13641 | -51.69535 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9835321-6167-3a05-b24d-bd62e3c8de0f | -4.81875 | -47.32049 | 2024-11-17 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd202091-bbea-3b38-a70c-11b8eeacaf92 | -3.87172 | -51.16607 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9023539-e61c-3318-8930-6449a547cfd6 | -4.6664 | -49.51952 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3b9ef9d-853c-34f8-b0de-ba521246d8bb | -3.23883 | -53.52335 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec48b7e8-69e2-349e-8bc0-aa3e0e6a73f5 | -2.13858 | -46.49516 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96830855-c7fc-3b61-9114-acea29b7a40a | -2.17626 | -49.10709 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d78d2c52-b0c4-3d69-a44c-3cba15de5f07 | -0.04645 | -53.25593 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8671eccd-14bc-3666-b38e-2e395010a926 | -3.52552 | -50.8077 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abb1c2b8-59db-3b12-91e9-49d8d8c7a2be | -2.94534 | -48.32012 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60775dec-531d-3b5b-bdf3-645de379cbed | -2.34978 | -47.46452 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 926550a7-3dda-30d0-b369-e531f7ffb062 | -2.05999 | -46.54285 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31e51244-173a-3a01-9ee8-f44426f63bd8 | -3.81132 | -46.50826 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62bef826-8da4-37cb-ba48-79b18e0176a4 | -2.10846 | -48.29926 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5dbdb3c-6e53-3ea0-a4b7-d8ffa6fd2fa4 | -2.62094 | -54.15845 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7453ab9d-a979-3aaa-a27c-b503d73e5ae2 | -3.52829 | -50.26986 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddecb417-587b-33e9-b3e3-091dec24bfa8 | -4.68395 | -49.63035 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7273d6c9-b9a3-3522-bc1c-6b13a61b420d | -2.64534 | -54.66867 | 2024-11-17 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 316eebc6-43db-3afd-8a00-ba43ee976db6 | -3.53447 | -50.254 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2be78d73-19cd-3f37-99c5-702b5215616c | -2.41911 | -48.78929 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abd2b68c-d51b-362c-8145-5885a456d23f | -4.44446 | -50.70404 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11273ece-5935-3062-95a7-3accc97620a1 | -4.56124 | -45.10424 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b51ea7e-2dab-3c20-a2f4-cf10d8464490 | -0.15475 | -51.50167 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ceb2ea-c8b6-33e3-94db-0ab2993d518b | -3.808 | -46.50774 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a203f457-6e94-3655-930c-25a896ddeb52 | -2.02838 | -46.37574 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1838723-25bd-30da-b844-dcf68a480967 | -2.06718 | -48.52894 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37fef594-97fa-32fb-bc82-e8647477ac0e | -2.09638 | -48.3966 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1009d2b5-6a85-320a-a77d-e13a83b593a6 | -2.6543 | -48.54559 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea63600-c886-3e85-8133-2e6546b77440 | -2.28905 | -47.48336 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a47fbc9-7b27-3bef-827d-633d4e3fe74d | -2.57035 | -47.57372 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9c71e47-0ff7-302b-a1e2-068d29040982 | -3.16867 | -46.59959 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2531912-ad61-3300-b979-58ae69cd5c46 | -2.21869 | -47.21791 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 318458e7-5508-3e90-ac58-88ea7f2a7c11 | -2.16765 | -48.76154 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6a73de9-da48-3938-bd86-80dc28c269b8 | -4.64828 | -46.86937 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44c6e983-634a-3313-920c-f9577f179fe4 | -4.41443 | -50.49775 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f65695c-c2b7-32cf-a7f9-5cf6d2bd5174 | -4.10759 | -46.87363 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e562554-a1d6-3b4b-b4bb-1c29e26159f1 | -2.6669 | -46.18104 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c94436b7-2d92-36be-b565-b36be95a35cb | -2.03205 | -51.17926 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd3e0e10-3f9e-3cc6-bd76-5f439d6c41b3 | -2.52604 | -46.36486 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89dee80d-4eed-3053-97e0-d85ac2c24099 | -4.19569 | -46.17677 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00f0737c-1734-3aea-aeca-6c09785a3af7 | -2.06276 | -46.54679 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d8d3bec-6dfc-36d9-bd4c-ab3076ebead6 | -2.23901 | -46.83083 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bfc0d26-817d-354b-a97d-201cd2f34a9f | -2.56605 | -54.7365 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e468474-0a4b-3140-af03-4aeac3e83060 | -2.1815 | -50.33568 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4d2185-5946-3b6d-bbbd-06665848d30c | -2.19849 | -46.35311 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 002ea48a-c507-301a-988d-c297271d89ac | -5.62662 | -46.36675 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 094fed65-4934-3ae3-a20c-d7f4160763cf | -4.10834 | -46.10512 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3af2e856-b91c-3ef7-a1d2-ec4a017a3e25 | -3.17311 | -46.44087 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d4bdf21-b6a6-30bb-96b7-def7b742c1e8 | -4.67271 | -46.73462 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b8f35b7-d01d-32dc-8b6e-0ef72245090c | -2.62576 | -46.03152 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 146a9ec3-4f7e-33aa-9c17-fdae3417ffd6 | -2.62827 | -48.08944 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c043dd-2945-34c3-b164-647a9c0a5f5a | -2.59681 | -47.5566 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892c898a-c31f-3667-8d35-abe17a12df56 | -6.93842 | -42.82227 | 2024-11-17 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5ec4eae-0243-309a-a137-ee18d0e6e456 | -3.34734 | -46.06427 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6e9a8737-9213-3696-a55e-d1fa86478be3 | -4.03637 | -50.88955 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af8ea549-7886-3a43-bda3-ae0e117450c7 | -3.36127 | -54.64488 | 2024-11-17 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aa536a5-5325-36d2-a4d1-474cbf1b343a | -5.11948 | -45.15446 | 2024-11-17 04:29:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5350b812-4c44-3fca-be91-abdf21be75f3 | -5.40539 | -46.34785 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27aa02c8-71bd-32d7-bf01-a23c62d169a9 | -3.61317 | -47.53258 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a20f1c-78fc-3a6c-b2a9-f10c8dd0670f | -2.66311 | -46.20537 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54d3d587-c435-3e74-a88d-bc08584de703 | -2.19457 | -49.54444 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7749439b-5d64-37a1-8b47-72ab7fd078f3 | -7.65847 | -38.83943 | 2024-11-17 04:29:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97677414-b8ea-3869-b1e3-61e353e6c810 | -1.79456 | -48.43877 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83d606d6-4a1d-36ad-bede-faaf2864b19f | -3.66048 | -50.20482 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59ef30d9-d2ba-3dd0-aff6-281375892dcf | -3.90885 | -50.46976 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78593c9-d770-3416-9394-2f64d8c7134d | -2.81887 | -46.66478 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 573abc47-0ef9-3fa7-a6fb-ca26d5c1ba38 | -2.20385 | -49.28296 | 2024-11-17 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdcfdd38-d411-308e-8076-bed2f29ec50c | -2.65459 | -46.84356 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d0b1c6f-765f-3051-b137-6f7c6549ee3b | -5.76603 | -46.5374 | 2024-11-17 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40188bf8-7687-3a94-9eb0-9d23519957a4 | -1.10499 | -52.3196 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2940605-e67e-3bbc-8fad-cc80fd9b66a5 | -1.13838 | -51.68882 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41f6f777-f3f7-3cfd-80c6-dd0d6c34c5bd | -2.09715 | -46.45702 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13512f62-da60-341b-9bd1-b5181342afea | -1.86893 | -50.96394 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee148ec3-5170-39d7-8b44-1db05c965007 | -2.67917 | -46.21141 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f4ffc17-4518-3bd2-b7cc-4a41ccf5d16c | -4.58159 | -48.02838 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e7a9bade-7abc-3348-a09f-b62ecd447eb5 | -4.536 | -43.29427 | 2024-11-17 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeb543e9-88d2-395a-b5b4-00621fb5029d | -2.34363 | -48.6018 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26c4a21c-578f-3589-a187-36b84bb20f69 | -3.14668 | -45.979 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c17e6670-ba95-305a-bdc2-bf93dafd69fb | -2.6397 | -46.8307 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80affa4a-dccf-3f5c-a009-eafba8a7f6d0 | -1.37352 | -47.25488 | 2024-11-17 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67d01a7-da8f-3f6a-be4b-d34190657fe8 | -2.31943 | -49.19475 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53a0a726-52ee-3d51-844d-0ee0c64399f3 | -4.33284 | -43.0462 | 2024-11-17 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e065cb37-991d-39a6-9bc0-3e02dc77622e | -2.17595 | -48.55685 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6b8ff76-154f-393d-b2f3-d7d29236309c | -1.63839 | -48.5189 | 2024-11-17 04:29:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eb9b6d8-eca2-33f6-97b4-cab22a8b15d3 | -1.4002 | -51.08495 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 008599ef-0761-36ac-9d49-25d5d3b99dbe | -2.59627 | -47.56005 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f22b781-2581-3062-9f2d-9f617db38dcf | -4.13363 | -49.36428 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc98875d-0f4a-381f-9905-2ad92165ff56 | -2.70595 | -47.9829 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54fb288d-125a-3b4a-8de9-4f1420901b1e | -2.67199 | -46.21387 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce99acea-cfc1-322d-b306-6abcd9b5fb41 | -2.17738 | -48.40931 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159c820f-7a7e-37a9-bc48-072cd5ca73ec | -3.15604 | -46.61531 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abfaadbc-5f1c-3833-b1c5-5bf47d8e21cd | -5.49453 | -46.25214 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
