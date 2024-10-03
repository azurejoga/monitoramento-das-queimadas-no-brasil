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

## Dados Diários - Página 220

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97dc6bff-946d-3570-a1ed-10df1ce13f31 | -8.649 | -66.6767 | 2024-10-03 14:45:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| e6ff452c-bc94-3abb-acb3-da89d162988e | -8.8312 | -67.3951 | 2024-10-03 14:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 47566d00-c7d9-3ee1-9019-2fdb339c9d14 | -8.7892 | -68.929 | 2024-10-03 14:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e87c058e-344e-3b9e-bf4e-0241a2fce9d9 | -8.7892 | -68.9474 | 2024-10-03 14:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 94284729-b029-390b-a389-fbc62179062e | -8.9674 | -45.2456 | 2024-10-03 14:45:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f3a7889b-d7a7-3ca4-950c-d289e774430d | -8.8497 | -67.3946 | 2024-10-03 14:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 5c8ac2ef-fb8a-341e-b49b-e365d62fdca6 | -8.9791 | -67.4099 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1eea2d88-5344-3569-b05e-052b5f5b59af | -9.0149 | -67.7423 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 6fd6a92d-473e-3cc1-b86f-0d7a2d9d9a94 | -9.0516 | -67.8525 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 8db17475-ff20-3038-b78c-48e3e1e486ca | -8.9976 | -67.4094 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6b77a402-09c1-39bc-bbe2-2213d12199e1 | -9.015 | -67.7238 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7aa06120-aa3c-3948-8a92-d5ea32b4566d | -9.2576 | -43.4535 | 2024-10-03 14:45:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 9eb8aea2-3b94-3a87-bb98-daaf4463ccdc | -9.033 | -67.8714 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6f1ef5c7-939c-3c47-8040-856040d61bf7 | -9.2573 | -43.4771 | 2024-10-03 14:45:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| a818f353-65ab-3589-8487-a60ca7c2cac9 | -9.0515 | -67.871 | 2024-10-03 14:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 09357672-61a6-348b-a950-ff79bacd8f06 | -9.3832 | -68.3441 | 2024-10-03 14:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d03f19ff-5786-3fb3-801c-2466b9b3abba | -9.4018 | -68.3252 | 2024-10-03 14:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 659c2730-a1ea-3267-9b43-8c008590bde2 | -9.5821 | -50.2011 | 2024-10-03 14:46:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 5fcd45c1-14cb-3df2-8f9f-6026043ba3a3 | -9.3834 | -68.3071 | 2024-10-03 14:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 729c6438-eae6-3807-ac27-7fdd42a6374d | -9.4368 | -64.5419 | 2024-10-03 14:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e9b78a7f-6a65-3c0c-b646-67cdbd05322e | -9.5824 | -50.1797 | 2024-10-03 14:46:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 796bff17-1eb6-352d-8b68-483fc9645895 | -9.3445 | -68.8808 | 2024-10-03 14:46:00 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7f51af44-e9ef-302c-8706-1e83078c9bc4 | -9.3833 | -68.3256 | 2024-10-03 14:46:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 198.2 |
| dfbdfe8a-b18c-3843-94fc-be0a739c4557 | -9.4753 | -68.5454 | 2024-10-03 14:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 32b7e9f7-7350-35b4-b5a2-6bc76c245cc3 | -9.494 | -68.4895 | 2024-10-03 14:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 3307c817-4dd9-3f85-85ef-bb3d3d3c5953 | -9.4752 | -68.5639 | 2024-10-03 14:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7542a2b4-a523-3394-83bb-8c13d7bde692 | -9.6012 | -50.1779 | 2024-10-03 14:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9a75e594-8a6b-3a19-b9d2-ac20a6b809a1 | -9.4566 | -68.5643 | 2024-10-03 14:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 94.0 |
| aab62978-f108-3908-be9a-134d4188a019 | -9.4567 | -68.5458 | 2024-10-03 14:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b407ca4e-c945-3315-9a97-b119c0d2b366 | -9.9747 | -64.7661 | 2024-10-03 14:46:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 967035f7-92f1-373a-a6c4-fe779f3e5e6f | -10.0226 | -48.2337 | 2024-10-03 14:46:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5379514f-50c8-3a31-a612-2fc466ba7909 | -10.0229 | -48.2117 | 2024-10-03 14:46:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 59bec316-b7c0-3b3c-92f5-e9dad5e0dd1d | -10.0418 | -48.2097 | 2024-10-03 14:46:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| dc2971e2-62b3-3cd5-82a9-bd71700dd82c | -9.888 | -67.3485 | 2024-10-03 14:46:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 268c74ee-2eb5-3cee-8b2f-04c9a6fd54b5 | -10.2384 | -47.6817 | 2024-10-03 14:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 086155a8-935f-3cb1-a42b-78ba9d223575 | -9.9933 | -64.7654 | 2024-10-03 14:46:04 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cee8a239-2b9f-303c-aa2c-fc5cc8f574c3 | -10.2195 | -47.6839 | 2024-10-03 14:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 33e6fdbb-8235-350b-8863-aaab72957a36 | -10.5056 | -46.2885 | 2024-10-03 14:46:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 8a8ab968-e8f9-3161-b5be-ef334730382a | -10.4287 | -56.7904 | 2024-10-03 14:46:06 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 6a1af330-75d1-3654-849e-dfd0b005ba44 | -10.4475 | -56.789 | 2024-10-03 14:46:06 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 465858fe-c71b-3a39-913a-7de0ea537f53 | -10.6981 | -46.1287 | 2024-10-03 14:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.1 |
| e2bde6dc-090e-3ebf-b10c-cee87ee1c46d | -10.4473 | -56.809 | 2024-10-03 14:46:06 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| acf61c24-0290-3882-833b-3014726d3585 | -10.7158 | -46.2169 | 2024-10-03 14:46:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| c36217db-39a4-3975-a56d-2754f67cd077 | -10.5929 | -48.0597 | 2024-10-03 14:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a75005e6-9645-34a5-bba1-5ca953e0f18d | -10.5926 | -48.0817 | 2024-10-03 14:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b63b5233-9210-3483-b19e-68041e5c42ad | -10.6317 | -53.7011 | 2024-10-03 14:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 28b16e2f-a572-38a3-bfde-9d70ee6fd942 | -10.7319 | -47.6461 | 2024-10-03 14:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 5f0e246c-9821-34f7-b9c0-034a74bc945f | -10.6505 | -53.6994 | 2024-10-03 14:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9482bbb2-9d03-3ebd-b802-89f2c8c68f4b | -10.7348 | -46.2145 | 2024-10-03 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 05e3b9ab-89a3-3b62-843a-b14db7620fae | -10.7315 | -47.6683 | 2024-10-03 14:46:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 3f727cac-802d-385d-b581-c63ee83cd797 | -10.7352 | -46.1918 | 2024-10-03 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| dc9bf7e3-0514-30e4-beef-cd646a78685f | -10.7366 | -69.4238 | 2024-10-03 14:46:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 13709438-abe8-372d-9526-5bb96d905141 | -10.8335 | -51.16 | 2024-10-03 14:46:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 202213fe-6da5-35c9-ac4e-5e109499c103 | -11.1579 | -45.9551 | 2024-10-03 14:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| db0a9899-5a16-3a4d-b517-ed5afb5fb1a2 | -11.2959 | -46.8399 | 2024-10-03 14:46:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 198.8 |
| af0d9bd6-ec0f-319f-b143-4a260b3e2d14 | -11.6822 | -47.7045 | 2024-10-03 14:46:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 466c5e2e-88e7-327e-be21-3d2ce43b2c3c | -11.5695 | -63.8084 | 2024-10-03 14:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 5e881c9f-93d4-3dfd-be0c-58735ffa9cbb | -11.5694 | -63.8274 | 2024-10-03 14:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f3c237f9-9a13-384d-b272-c505dfcd8325 | -11.6051 | -64.0918 | 2024-10-03 14:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 40a7a3af-ce3d-3955-a5ab-ec7ff5632f29 | -11.6052 | -64.0728 | 2024-10-03 14:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c8dbf375-ef73-39e5-ad5d-b1b412f190f2 | -12.0131 | -47.3263 | 2024-10-03 14:46:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| af8cc60c-b409-3583-92d5-ab32b6f45afd | -11.9483 | -50.1618 | 2024-10-03 14:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 54968a75-a617-3a76-b737-7e5c0cc7a53e | -12.3934 | -50.9658 | 2024-10-03 14:46:16 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6ea27d45-af22-3dbc-b7a2-0a76581dec13 | -12.3101 | -54.0973 | 2024-10-03 14:46:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5478754a-3707-3b57-9191-a49fafee29b6 | -12.9831 | -51.129 | 2024-10-03 14:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 5dfe5237-1203-3d72-9769-5724487e380d | -13.0406 | -51.1218 | 2024-10-03 14:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6f831be4-683e-3bf9-bf39-d46ae3419342 | -13.1805 | -45.4489 | 2024-10-03 14:46:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 496.5 |
| bf225c81-2e61-3d23-85b2-be7acb384d90 | -13.1924 | -51.2097 | 2024-10-03 14:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f2feac17-8894-3a10-8e1b-d5b34bad2240 | -13.1927 | -51.1883 | 2024-10-03 14:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d861308a-aa18-3013-ab27-2b994c32066b | -13.5198 | -51.1252 | 2024-10-03 14:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 8d7c1a0d-63a3-3e2c-8c82-978055b12db9 | -13.6342 | -51.1746 | 2024-10-03 14:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 73986dd7-b068-3bde-bbcd-d263c22a9102 | -13.5957 | -51.1796 | 2024-10-03 14:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 4176b1b2-c296-3bc0-8b75-4a797d75026d | -13.5954 | -51.2011 | 2024-10-03 14:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 23b8b784-c751-35fb-a5bb-4eec6c5f4675 | -13.615 | -51.1771 | 2024-10-03 14:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 181.7 |
| c81ea3d3-d817-334b-bfa4-46ce5ffea913 | -14.0202 | -45.0747 | 2024-10-03 14:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 361.8 |
| 0734e038-17b8-3fc7-b7d7-6eb514228b76 | -14.7017 | -48.7559 | 2024-10-03 14:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c2a8f7a3-c3fc-3139-be7d-fd25f625ceea | -15.1426 | -48.1044 | 2024-10-03 14:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 79e02d07-6868-3e86-80b5-3f7271f3668a | -20.4928 | -40.9323 | 2024-10-03 14:46:58 | GOES-16 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 98.7 |


