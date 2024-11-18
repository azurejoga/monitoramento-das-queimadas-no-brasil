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
| 9b28526b-6b46-3432-ad2d-d4ec51ac2e04 | -1.3148 | -51.7408 | 2024-11-18 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| dfd811e6-9bd8-31c9-bba8-cb67536c0fd1 | -3.3152 | -53.3744 | 2024-11-18 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| bf77727e-8e98-3874-981e-cfc690854c21 | 0.9845 | -51.145 | 2024-11-18 00:00:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3874254e-51eb-328c-8c36-f640a297d40c | -3.6593 | -50.439 | 2024-11-18 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0a1fa73f-0126-312e-b22d-043547e4182d | -1.4408 | -53.3917 | 2024-11-18 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f6af5f98-857b-3a25-8cac-c203cb68dec2 | -1.6962 | -45.8311 | 2024-11-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 132fb89e-2db8-334e-a01b-6cc983f7746a | -1.7147 | -45.8307 | 2024-11-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 2dcbc19c-ff20-34b9-a034-ef2051744d8a | -5.9556 | -48.0642 | 2024-11-18 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a66de5b7-8403-3b28-acea-a226ed1ccc5e | -1.4408 | -53.3715 | 2024-11-18 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| a6498b8e-4512-3bba-84e9-28948f7813cf | -2.1766 | -46.3975 | 2024-11-18 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7e14c7b3-779d-3670-be79-518d0f064db5 | -2.7843 | -52.6158 | 2024-11-18 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| af784b42-4127-3215-9ce5-a4b007af98fc | -4.7946 | -46.4899 | 2024-11-18 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| fee2a884-90dd-310f-9357-64bd9c36f721 | -4.7945 | -46.5121 | 2024-11-18 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6d420d20-55d7-3095-b139-9b34ccb9b9a5 | -14.2857 | -57.6442 | 2024-11-18 00:00:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9f979cbc-35a6-3689-af1b-b2bc5149360d | -2.6801 | -45.6934 | 2024-11-18 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 980293b5-ee56-3a6c-84be-f3c9523fb871 | -3.0542 | -54.4081 | 2024-11-18 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 6de41502-6b04-31d5-ba59-a75fee5fd25d | -4.5771 | -45.6325 | 2024-11-18 00:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ed8570d0-0b23-3fb3-91ab-d9617c172eaf | -5.5481 | -43.2824 | 2024-11-18 00:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6a7e514a-adc2-359a-83f3-ecfc7024c906 | -3.5678 | -50.2534 | 2024-11-18 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e4f41231-9084-343a-b20f-a1d9235b508a | -13.021 | -56.4544 | 2024-11-18 00:00:00 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4618335f-533d-38f0-bc67-d6047efff45e | -14.286 | -57.624 | 2024-11-18 00:00:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| ed8abee5-67bf-3873-b139-46ce452b166e | -2.5847 | -51.7181 | 2024-11-18 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| e7ca13d1-3666-36c0-8f8d-0a9fbd92126e | -4.7761 | -46.4688 | 2024-11-18 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6a99aec8-ba32-3d83-b82c-4a490e61c04d | -2.5846 | -51.7387 | 2024-11-18 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c535ad2c-ce9e-342c-a164-1c040efa0f28 | -2.6583 | -51.7163 | 2024-11-18 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4f6950f1-b93e-3721-ae17-295ef40b4c1c | -2.8607 | -51.7937 | 2024-11-18 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 1311a4ac-dd50-34af-b513-1629396c3396 | -2.7475 | -52.6167 | 2024-11-18 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ddeb068f-8ea0-383b-99a7-389406282b0e | -4.776 | -46.491 | 2024-11-18 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bdce2cbb-97d4-32a4-8436-848db56c1797 | -2.8608 | -51.7731 | 2024-11-18 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 25b05f8f-35d4-3d9a-bf5a-89a2cb1884f7 | -3.0764 | -53.2796 | 2024-11-18 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fdbb4b1c-c0ed-3b71-9e27-e37645b15eda | -2.68 | -45.7158 | 2024-11-18 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7893c62f-4c13-3d88-9bce-fba0988faea1 | -2.6028 | -51.8001 | 2024-11-18 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6d292b1b-9b32-379a-99c4-a8079e867cd4 | -3.3287 | -46.0048 | 2024-11-18 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| d3e81307-2c25-36cd-ba95-5005642e815e | -1.2964 | -51.7204 | 2024-11-18 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 7e64a83b-cb28-340a-b674-66be6eeaba26 | -2.6986 | -45.6928 | 2024-11-18 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 35afa743-bcee-3367-86c2-74b7608fd8ac | -3.6778 | -50.4384 | 2024-11-18 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9d878c54-fbd9-3dd0-afbf-a8be455a4de0 | -1.2964 | -51.741 | 2024-11-18 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 194.6 |
| e2a68402-071a-3a0d-8c7b-a94d517ddae0 | -2.7659 | -52.6163 | 2024-11-18 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 205.0 |
| dc6c27fc-bbc4-3f46-a14e-3dd6d7d2272d | -2.8791 | -51.7932 | 2024-11-18 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 3e97a13d-820e-31ad-8801-0a0fe8a62a52 | 0.966 | -51.1452 | 2024-11-18 00:00:00 | GOES-16 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 91ac47ee-9d04-3964-bc43-657e56f38fb3 | -2.6986 | -45.7152 | 2024-11-18 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 130.4 |
| d5192836-fccc-3cf0-85e7-8fe09c3e1a57 | -2.766 | -52.5959 | 2024-11-18 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 7dd21703-c94e-3355-8a36-bb59c907d6e2 | -2.9814 | -49.1091 | 2024-11-18 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 843ea1c4-7314-34bb-8012-9ea72bdada72 | -2.8792 | -51.7726 | 2024-11-18 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 0f731755-430c-310b-8def-c62191c708d3 | -3.77 | -45.96 | 2024-11-18 00:00:00 | MSG-03 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6c6fcec-3028-3258-878d-32344ee02a44 | -3.77 | -45.91 | 2024-11-18 00:00:00 | MSG-03 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a937f459-0f01-3eeb-b730-71b28ac294e8 | -3.75 | -45.96 | 2024-11-18 00:00:00 | MSG-03 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f49e3561-d7cd-3e0c-aade-1c66fdf1555c | -3.74 | -45.91 | 2024-11-18 00:00:00 | MSG-03 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3a8e116-e7f0-3e05-bfeb-e5be3ce0263e | -3.3384 | -46.03247 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 38d5f7d4-50b0-35f9-ad58-aad49d66b505 | -9.40011 | -40.31239 | 2024-11-18 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 480f3a91-6028-3452-8a14-fd7a17d43a94 | -3.7527 | -45.98341 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| db82d087-544f-3331-af81-085a99027c31 | -3.76908 | -45.98113 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 97b138d9-97cb-3aa5-b72d-aa201945bceb | -7.40125 | -38.99659 | 2024-11-18 00:05:00 | TERRA_M-M | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 152c11e6-6935-3ac8-bab1-ba3492ce7806 | -6.21674 | -43.28662 | 2024-11-18 00:05:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| f78535fd-e546-3dbd-b80f-bdc1a6de0061 | -5.66296 | -35.47085 | 2024-11-18 00:05:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4aedac9b-0159-31f5-b809-61b232a61fcf | -5.56639 | -46.43639 | 2024-11-18 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 77bf3827-f9e6-3240-ac17-c844f7c726e0 | -3.75334 | -45.91968 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 57599be8-059f-3d1b-bcb7-811156c4f5a7 | -10.52399 | -36.74144 | 2024-11-18 00:05:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 3b26aeb5-ee61-31fa-8832-a767d79c49e9 | -6.96922 | -34.93371 | 2024-11-18 00:05:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f9f2f606-6f7b-34ef-9f77-51307c9552e3 | -10.03876 | -36.41521 | 2024-11-18 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ffab8237-69bc-324f-853e-3c6dba6c7fda | -7.65235 | -35.33245 | 2024-11-18 00:05:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 2590584d-7c6a-3aab-b3dc-db94b965d7c1 | -6.33974 | -39.68692 | 2024-11-18 00:05:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5d4b691a-6ee1-3fa6-ac38-df54ef8e0f26 | -4.90924 | -44.0227 | 2024-11-18 00:05:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fd731200-cce1-352a-b019-c0bbae0d1c31 | -5.3415 | -40.89548 | 2024-11-18 00:05:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| f3aab116-69d4-331d-aca0-18a281458ff0 | -3.76457 | -45.94648 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1131.2 |
| 6680536d-e806-3a65-abed-4e72a554b01e | -7.40774 | -42.77687 | 2024-11-18 00:05:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 22fcca8f-a31e-3813-9272-40afce20923c | -6.21052 | -43.29269 | 2024-11-18 00:05:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8bace20c-4cf2-3f6f-b81c-c18f1728377a | -9.40221 | -40.31847 | 2024-11-18 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 186a4a4b-e3c5-3c2a-a758-44ee2252de35 | -3.18732 | -45.45941 | 2024-11-18 00:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| adede0a2-b950-3906-b623-984c96a91aa0 | -3.33178 | -46.03832 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| c6dbd70f-efa2-31a5-be05-8a742d489519 | -7.18313 | -39.12165 | 2024-11-18 00:05:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 889f3870-606e-39c9-a553-44d5e49fa354 | -5.56489 | -46.44188 | 2024-11-18 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| baaf8f3c-caab-3e87-b83a-64b73df50831 | -10.02973 | -36.41647 | 2024-11-18 00:05:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 8c4cf31b-d02a-3826-b18f-4b42e7847ddb | -10.49744 | -36.74103 | 2024-11-18 00:05:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| af04f577-cf1e-3d8e-92b2-cec54d29f7c1 | -3.75804 | -45.95404 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1016.7 |
| 5933b1d4-5b66-358c-8f40-4e76bdefe6be | -6.86696 | -38.89157 | 2024-11-18 00:05:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 9dc3a7ce-48ad-3068-9352-9ec1db8e5260 | -5.5451 | -43.30346 | 2024-11-18 00:05:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7545c1a7-ea24-3330-818e-1136753248db | -4.95698 | -44.50336 | 2024-11-18 00:05:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| eed75da9-813c-343f-8341-ebc595c5f841 | -6.52716 | -35.19395 | 2024-11-18 00:05:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a2ca1f2d-5d3a-3697-9d66-ad39cab7ec6d | -7.6536 | -35.34137 | 2024-11-18 00:05:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bb079800-997b-356d-bade-d9d25624f452 | -6.96027 | -34.935 | 2024-11-18 00:05:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c2ce3300-84c6-381e-914e-10f443ddd4af | -5.26381 | -44.05711 | 2024-11-18 00:05:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 78c0beb0-6e91-3d57-96f6-1e29245f4112 | -9.402 | -40.32777 | 2024-11-18 00:05:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 107dd7c2-396b-3c96-9dcb-e9d017fa3ea1 | -10.1129 | -36.35152 | 2024-11-18 00:05:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| 3a0df5f5-eb52-3ecb-8221-e632ec9de634 | -5.51415 | -41.0726 | 2024-11-18 00:05:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| e0dce877-9eb9-3676-9561-e0cb1367b2cd | -5.50291 | -35.57883 | 2024-11-18 00:05:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bcb5d255-9349-30eb-b03e-64a7133e86d5 | -4.79708 | -37.39238 | 2024-11-18 00:05:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7c2658ff-75f0-3817-ae96-f3ffeed07ad9 | -4.7681 | -46.42787 | 2024-11-18 00:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 785781dc-c9c1-3d74-b399-3ecb92ab088d | -9.81664 | -39.1523 | 2024-11-18 00:05:00 | TERRA_M-M | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 8d8ebdcc-da92-3e9d-aa2f-b3663b9e1508 | -4.4959 | -46.39602 | 2024-11-18 00:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| db207598-9f0b-3ad5-9c71-6b774dfc43bb | -3.7744 | -45.95195 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| ffa762f5-0ee2-39ed-8970-2c5b02eb93fe | -10.11543 | -36.37016 | 2024-11-18 00:05:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| cb4a4601-ac13-3c0c-ac01-7b16186ac309 | -7.53389 | -35.21017 | 2024-11-18 00:05:00 | TERRA_M-M | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2f47925e-0ae0-38db-ad23-40ad0a9265dc | -7.53814 | -35.31577 | 2024-11-18 00:05:00 | TERRA_M-M | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 0375429c-8934-3775-a4e8-e0b7635e97bd | -3.32704 | -46.00428 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f1428ac5-5c24-3872-94c6-addd1ee804f3 | -3.33384 | -45.9981 | 2024-11-18 00:05:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ffad5909-c618-3fd0-a8d4-6dc310e8a9bb | -3.76279 | -45.98873 | 2024-11-18 00:05:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| fa708a7d-bec8-38c6-98f7-ad87c67bccb7 | -7.40056 | -38.99038 | 2024-11-18 00:05:00 | TERRA_M-M | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 583ca7b6-074d-3d39-accf-49dba47c5bb1 | -6.32938 | -39.68835 | 2024-11-18 00:05:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 57062db1-9277-31f3-9962-69d1f2ca5d00 | -6.86548 | -38.88037 | 2024-11-18 00:05:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |


[Clique aqui para ver as próximas entradas](README2.md)
