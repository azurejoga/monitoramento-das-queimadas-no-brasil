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
| a58f2f64-c5a7-3073-aa51-8315b32a122c | -0.04342 | -53.25174 | 2024-11-17 04:04:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de7db5e-a2ee-3116-a4aa-2c00595db4e5 | 0.51608 | -50.74276 | 2024-11-17 04:04:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8edec6af-7bab-3b49-b4f8-22d6aafb9273 | 0.51503 | -50.74216 | 2024-11-17 04:04:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16a6f8d9-8c5d-332d-a959-ca330db9f1be | -0.83891 | -47.4725 | 2024-11-17 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6ddfe3e-301c-3551-9f41-9d9a93d52260 | -0.02622 | -51.66797 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17bcbf4d-2d9d-3747-a8f7-6fc98ffd0f8d | -1.23425 | -47.35579 | 2024-11-17 04:04:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bc20aceb-5bba-3820-a035-5f1a6aefacb8 | -0.11963 | -51.62824 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24199129-8be6-3d1b-8827-fdfca3d027f8 | -1.01596 | -47.7655 | 2024-11-17 04:04:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8feb80fe-84e8-3331-9ba7-bcf63fdf561b | -0.40387 | -51.62298 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dfdccec-a045-32db-85cf-bb58921db670 | -0.3138 | -51.5018 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebba494-de4f-33dc-88c7-d2bd4188859a | -1.23348 | -47.3606 | 2024-11-17 04:04:00 | NPP-375D | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 91ec1670-2cd6-3ad3-b2d3-1c4b1afb33f0 | -0.11104 | -51.60102 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e3c58f-80fd-3c78-8054-1861aae9d949 | -1.52386 | -47.4695 | 2024-11-17 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05ef0b96-90b5-3a5f-8b74-823924a0ad63 | -0.31624 | -51.50268 | 2024-11-17 04:04:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90885024-bff5-3b0d-aaf6-c872c0dc1b57 | -2.65951 | -46.21841 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ff67684-13a4-3dfb-a783-4ef7a581eac2 | -2.81777 | -46.66269 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00956031-f47f-3f65-80d6-32a4770945fb | -3.52795 | -50.23853 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d81af94-798c-3b00-8048-5168ff81f6b9 | -2.63385 | -48.56688 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 68d426dc-bd70-364c-9931-6da8c2e30372 | -3.24098 | -48.00227 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2ef1053-f89e-3ece-b5f7-84c437c7405d | -3.58316 | -50.52066 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2db15e93-ba97-3cec-93a8-1018485d655c | -2.62402 | -48.56458 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c5c196f-891e-3256-9fd7-fbd6984d5342 | -1.83274 | -46.59414 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23e75686-e551-32f2-9df9-bdd65dd4a381 | -5.33802 | -40.89988 | 2024-11-17 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9f540988-16be-3e4c-88d7-23ed2dbdeffa | -3.73824 | -44.52894 | 2024-11-17 04:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20230887-a3f0-3b67-969e-703e5b04ce04 | -2.67165 | -46.19652 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4268f6e-2c9e-35cd-bae8-b42b8f20dd39 | -3.61562 | -50.1521 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e69f6d22-2aa6-3031-b141-96923798d214 | -3.12473 | -45.89952 | 2024-11-17 04:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 385f2621-1861-31ec-afa8-50ad9ff2fbae | -3.55905 | -50.25491 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24ad2b5-cd8a-3065-a459-31fcdf888b64 | -2.29822 | -49.13178 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b56a4c-9955-3b96-b233-9a0063b94a12 | -2.6823 | -46.20935 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12da316f-0fe5-3fc7-87fb-6773d686df08 | -3.53587 | -50.2583 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2c9297c-d073-3ebb-9be3-13289c7c21da | -3.24127 | -48.0058 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ace684-bf24-3178-894e-51853b25c8bb | -2.40209 | -48.45091 | 2024-11-17 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4aa1963d-b4cb-3095-989e-15f70917ff03 | -0.94698 | -51.72858 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7b13b6d-a636-377e-b4a5-a9d7a61c7906 | -2.60965 | -46.2583 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d825e4b5-156b-396f-bfd5-304e7b607cfd | -3.52243 | -50.23774 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8358b4ee-9229-3a6d-a7f6-e815184283f2 | -7.31481 | -45.27255 | 2024-11-17 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91e988ca-b0ba-3b59-aaec-904f30c9e2bc | -3.17086 | -46.59747 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b04d8b21-457a-3b7e-ab92-a5825cd8f5d8 | -3.14124 | -45.98166 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 624f02b9-813a-31ed-b6cd-8ad8e7e03996 | -2.67843 | -46.85644 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f22a5b2-4a32-3fec-99f9-043f90e56585 | -2.71882 | -47.90789 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7d8c43c-8fee-3d11-81b3-0675dfae9429 | -4.8127 | -44.48216 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 7225d449-fa94-3a1e-b922-215fcfb5efee | -4.57807 | -48.02938 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 196982b3-1077-3230-b405-6a87f94e5874 | -2.81825 | -46.66569 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 952e0b71-bc06-31e3-ac8f-58221b5eaa73 | -6.38874 | -45.68575 | 2024-11-17 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0eb6253-e0e1-3c29-965a-7eba30327a27 | -2.66558 | -46.20752 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7827ae5-eaf6-3a25-b1b0-a0c7d6e9b051 | -3.69577 | -50.11119 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99a201b9-6d73-3939-9e7a-3f40adda3f65 | -6.2016 | -39.77705 | 2024-11-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f41bbe8-19d1-317f-ac8c-0b147ae556f1 | -4.65038 | -45.0027 | 2024-11-17 04:06:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a29e41ed-1f21-3813-b7d9-c159bb08bbf8 | -2.67464 | -46.20501 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c675e574-698d-31b2-a9cd-54dd998ebb4d | -1.91181 | -46.57437 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6a3a989d-e530-30ba-8f09-0835ccca7b79 | -3.66197 | -50.60551 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8147654e-83b7-3e59-a6ee-79c7b0c94259 | -3.68978 | -50.11362 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7066334b-98a3-3aec-b67f-558d16477493 | -2.68001 | -46.197 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4dd9981-288d-30b9-8036-fa28c322fc5c | -4.72984 | -46.83895 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f52c22-1080-3116-9cf6-90d07001a228 | -3.49619 | -43.7836 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88a5cb32-ee3a-34d2-8b97-3a297cbca13a | -3.91653 | -46.52907 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8671df5e-851f-3965-b4a9-3d3e204647d6 | -5.51685 | -37.87889 | 2024-11-17 04:06:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 729cd729-9d46-3f36-bad2-dfab3b0ff613 | -3.044 | -45.75692 | 2024-11-17 04:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b66ca66-70bf-3077-a690-ed64562affa7 | -3.57059 | -50.25341 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e186e02a-ee43-3368-8c16-84e52ad4b392 | -4.47505 | -48.11474 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3daaa56b-3bfb-303d-b9cb-a6b9ceacae0a | -3.95525 | -46.71816 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8991d0-c638-34e1-b6ff-3895c6f04572 | -3.52487 | -50.25654 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 31c0e61e-9960-3d28-80a4-d83c6263c4e2 | -3.07581 | -45.37908 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f0da24-829b-390e-b31a-56d30a46ff41 | -4.55896 | -48.00132 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e02ef9e2-0735-3c17-ae3c-969d046964d1 | -2.07084 | -48.53762 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14ee7305-8282-329b-b9c6-d74ce82848e3 | -7.2991 | -39.1688 | 2024-11-17 04:06:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4ff5620f-c37b-3932-9762-d635a2025fc2 | -7.35649 | -46.37189 | 2024-11-17 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fae17e7d-9ae5-3a2a-a302-77a5b1d7aa41 | -4.44057 | -46.57122 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d20d6129-2cdb-3bb6-973a-58a0ad638ec9 | -3.14742 | -45.98312 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bd70e03-74c3-3a41-94b6-0eba6fae62a4 | -2.66349 | -46.21814 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 993cb882-9237-3d22-b71a-1f44114f38e2 | -2.86735 | -46.72072 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| fc22d744-1077-3cfa-a2ff-5dbc7a6858df | -4.11787 | -40.5423 | 2024-11-17 04:06:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 559ef8d0-c238-35af-beb5-89187db758d5 | -4.28885 | -46.90962 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f69a15af-c6e5-37e9-bf4a-712b959db391 | -5.42503 | -45.34061 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af1cee00-e898-3b03-b26b-688a4079c1af | -4.28721 | -48.2121 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2325da17-b485-360d-958f-79160ee44e64 | -4.03762 | -45.47012 | 2024-11-17 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2aad8ae4-65cd-392e-993e-4cdb7bbf5222 | -2.67708 | -46.18851 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba626872-8b7a-3a24-a60f-cbfb6ebd6d3a | -3.57698 | -50.52334 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a90c1fe5-382c-3a8d-b03a-267c43783ac1 | -3.67518 | -50.10091 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a6eb77ee-7d83-3d49-bd23-0737bbff99ca | -4.47924 | -44.00937 | 2024-11-17 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3f57906-510c-35fa-9e79-7a1f8e18f18c | -7.3125 | -39.17485 | 2024-11-17 04:06:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0cf5aa3e-7dd2-3d81-90e3-a5fb2921a39d | -3.52121 | -50.24487 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5ff498b-ab07-391d-9d91-f42a9bc85ec8 | -2.61031 | -46.25428 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f484e41-5ea6-3fc5-95c3-3c490e011aac | -7.709 | -43.74311 | 2024-11-17 04:06:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a42e656e-1a03-382e-a14c-65c3698d7325 | -1.7934 | -48.07145 | 2024-11-17 04:06:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3de8faff-82da-3fa1-89b9-323528db9fd1 | -5.27244 | -44.90889 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 32837465-2f02-332a-b274-9ae5a429c3d9 | -2.07594 | -46.47466 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0520b615-09e8-3a0f-bbb4-a7fff6787b99 | -4.84586 | -44.48734 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b7e16d2-468a-3e7f-9b92-03e7d2ca50d7 | -3.52611 | -50.24924 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0414a25a-c3ef-3de0-a6d7-d811ca8963ea | -2.67579 | -46.19631 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5c2b4d0-eacb-3b2c-8d72-b26d54cc8038 | -3.36414 | -46.08174 | 2024-11-17 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ce55f20-6c10-3c80-a12c-9567b620114b | -2.20252 | -46.29861 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f21fc99-dadd-3104-ba11-3c73b5a243c0 | -2.29837 | -49.13182 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5722420b-7e45-363f-8937-8ca985dce288 | -4.54158 | -45.24889 | 2024-11-17 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29a9babf-9727-37b5-b22b-1914c4e9abce | -3.89112 | -43.13444 | 2024-11-17 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 163389d7-1304-3ee9-8888-271b4b6046fe | -3.83874 | -51.30525 | 2024-11-17 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73f6306-ea80-34f9-8753-0893e5c24d9b | -5.64493 | -43.29872 | 2024-11-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a5e89c-c8e1-325b-a909-1a2cbab2949f | -4.02589 | -46.54521 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6be8496d-e694-3140-bcbd-6efe8924b19d | -3.91296 | -46.5244 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
