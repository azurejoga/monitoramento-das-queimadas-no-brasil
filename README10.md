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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd05e7a-c6cc-3845-a6ce-4feede2c6863 | -3.7439 | -61.744202 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9e7a2d1-a358-3247-bb0c-803957b3638b | -10.89 | -47.793701 | 2026-09-13 00:43:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc4277f5-0279-39bf-9ccd-81915132be09 | -8.5458 | -54.694599 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfdf8b47-c844-3c67-a575-cb194aab050b | -6.0989 | -57.646599 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b599c8-428d-38a2-a1fd-12916f134c25 | -3.4075 | -59.233101 | 2026-09-13 00:43:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0f1838c-f7a7-3d13-8734-9e7d4d526926 | -8.536 | -54.696899 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99fba7b3-1f9b-378f-9687-b15a3bde0c51 | -6.175 | -57.709301 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d56972f-346a-3b7d-821c-5353f4f0d332 | -6.7641 | -59.416302 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4e4625-9702-3a99-8bd5-64e52c9831a4 | -6.1326 | -57.7043 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b90bbf-6d06-3861-b901-634d575dcb01 | -5.311 | -57.127602 | 2026-09-13 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f8623f-da2c-3fc4-9b2a-9de057d8a14f | -6.3445 | -57.866299 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8786a1f-0717-3272-8122-f089c6ff8dcf | -6.0107 | -57.6665 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 453cac2d-95db-30c0-83f3-7c3f14eb759e | -8.6051 | -55.216599 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcff6946-9f1e-3f98-ba84-5307abd032d2 | -3.7403 | -61.7281 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4de7f233-5ffa-3f2a-a960-365a0b738c07 | -6.7552 | -58.960602 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08741e0c-d913-35d0-8cbb-ea3746f82775 | -3.7243 | -61.748501 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16c94f94-6774-3da3-8a8d-b9dbb7c8d41b | -3.907 | -55.722801 | 2026-09-13 00:43:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6379124-70e0-3478-a1c2-dbffd546c3ab | -6.3399 | -55.8134 | 2026-09-13 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb3c94ca-9a76-32be-baa1-f43d3ea0f96c | -6.5723 | -55.613899 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2507d8-1cd4-3d74-add9-ec432600986e | -14.8119 | -48.139301 | 2026-09-13 00:43:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b10d473-a1f2-33c5-8982-37ee853481fa | -10.5227 | -51.340698 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe5121a0-dd8d-35d4-9092-2365869ed9ba | -10.6933 | -54.168701 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a38b3f4-f96e-3f68-8701-dacad41f91f6 | -8.5379 | -54.705002 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9850511-ce13-3088-96ef-a91b1e64ec12 | -2.7163 | -57.591702 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a08ced57-2344-3d13-8786-a1bfaabbf544 | -7.8676 | -54.7062 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d74548a9-525c-308d-ba0d-a0024b201f8a | -10.9464 | -57.166901 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20e27f27-1365-3807-8e76-730f612de1de | -6.3045 | -59.9403 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f6e15fa-563d-3c0a-ac26-845a31925eba | -6.1024 | -57.616798 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf0db462-96f9-3914-b0c6-3ceb343c8fca | -6.6616 | -58.864601 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaf79406-99e7-3a27-935c-40eb6b404e30 | -6.2883 | -59.9133 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28d12cb1-30de-3766-9428-bbdad2183828 | -6.5935 | -58.836102 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 506dc695-bb82-33fe-9434-81ffe7ad60e6 | -6.7963 | -58.776402 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0bdbfbd6-afca-3ca7-b34d-f4feea2c8701 | -13.4044 | -57.0173 | 2026-09-13 00:43:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd2a0e7f-a605-34ba-b1a3-7b37bfd7ef60 | -6.1652 | -57.711498 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1df37f2-9960-34a5-b3f9-ddd8c6be4901 | -6.8519 | -55.5741 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2271c8be-9e46-303e-885d-60d16c556f5f | -6.0724 | -57.848099 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036adfbe-90e6-39aa-b39a-3fc7976c7f72 | -6.8581 | -55.556301 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7c8fed8-5f07-3d6a-ab91-2fce53e9ded1 | -3.3538 | -58.175098 | 2026-09-13 00:43:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 133dae03-29ae-3147-8e5a-1dcc83bd029c | -2.926 | -50.376701 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32f80606-6ede-34e8-bf4e-c3d585df1413 | -6.2267 | -51.690899 | 2026-09-13 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e79d96f-77ac-3e45-9829-aa4d729446fe | -6.7537 | -58.953701 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6ffc2b-0b9e-3d2b-aa3c-df1be999c306 | -10.6796 | -54.154499 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 236420b3-2d33-3fc3-9a1c-d69be2a21b5d | -3.1593 | -58.636101 | 2026-09-13 00:43:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d5ce443-6535-3bb2-8232-cacc398a334a | -6.3429 | -57.859501 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df95074-c6e6-311d-8215-039a56f2df21 | -1.1854 | -55.710701 | 2026-09-13 00:43:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 977cea60-bef5-35bd-b1e5-b20de367b3fa | -10.9582 | -58.9454 | 2026-09-13 00:43:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df6f7a00-62bb-31e1-a34c-8c1d370146fc | -2.6785 | -57.5115 | 2026-09-13 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ba83f8fa-8d49-33d8-b04c-459b166dc438 | -6.1111 | -57.6645 | 2026-09-13 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 185362fd-07b1-330c-9960-f549089a0580 | -3.728 | -61.7555 | 2026-09-13 00:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5acba9f9-c1e4-3182-9a94-e6311a0ae216 | -2.6602 | -57.5313 | 2026-09-13 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1587658a-0df9-3258-b86d-e89fea38b211 | -6.0915 | -57.8602 | 2026-09-13 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ff4180ee-b7b1-3cdd-8f7d-b4bc0a007849 | -2.9579 | -50.3988 | 2026-09-13 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 51ee9667-b49b-36ba-bab7-a3cfa3dfe610 | -6.6757 | -58.8847 | 2026-09-13 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f119a0e7-8523-379c-9ea6-6a450ee3da1c | -3.3293 | -42.2893 | 2026-09-13 00:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 88d42a0f-0e51-3936-abb8-45c8779c08eb | -10.7018 | -54.1458 | 2026-09-13 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f60b1b7d-9136-35d7-a00f-1ccc5c38e821 | -10.6824 | -54.1884 | 2026-09-13 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ddfea9b2-e0c1-3cc0-8de3-ffbef9a92e4e | -15.5595 | -53.7845 | 2026-09-13 00:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b590b233-5a25-3ade-9e27-10f537490bf8 | -6.8446 | -55.5611 | 2026-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 157cbfe9-9f1e-377c-80d8-0c1e9e31f8a1 | -2.6785 | -57.531 | 2026-09-13 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 64f89337-0f6f-38eb-9461-bfeaad7b4ad1 | -6.8445 | -55.581 | 2026-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b4fdf71e-0927-336d-9628-67bda7d80437 | -6.6021 | -58.849 | 2026-09-13 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5d66fbd7-e851-30e6-bac4-bc46eecfb165 | -10.6829 | -54.1475 | 2026-09-13 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 3a545d1e-24e5-35c4-b434-7e82b77385ee | -15.579 | -53.782 | 2026-09-13 00:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c46b3a33-f026-3c26-9538-9439e4720cc7 | -8.5417 | -54.6985 | 2026-09-13 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 92553d64-30ff-3145-8c9b-e602cab4208a | -6.8632 | -55.5601 | 2026-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f82f2cf0-29bd-32bd-8da3-b5e5c53d9ad2 | -6.0731 | -57.861 | 2026-09-13 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 1b9befd4-5993-39a4-b93f-cab2194bace2 | -10.7015 | -54.1663 | 2026-09-13 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| fd2df7ef-9aae-349a-9ae2-20621fb1349d | -3.3292 | -42.3129 | 2026-09-13 00:50:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 043a8372-8e87-39ec-a7ca-9d7823b6b6d4 | -6.863 | -55.5801 | 2026-09-13 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6c7cc202-3965-3714-9f57-6b4a9d50c6e4 | -2.6784 | -57.5504 | 2026-09-13 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 7e0eb1d7-308c-31ac-995c-577621dacad8 | -5.8206 | -53.8052 | 2026-09-13 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6caca173-ce90-394e-acb6-98e2dcfdc8da | -3.5743 | -53.0015 | 2026-09-13 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6c0534dd-09ff-3fdf-9fa2-9293513cb1c2 | -12.8543 | -44.386 | 2026-09-13 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 379933f7-cea2-32b9-80ad-ef0e0133719e | -10.6827 | -54.1679 | 2026-09-13 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 287.7 |
| d30d952f-675a-361d-9e88-1db2b81e40ae | -8.5415 | -54.7187 | 2026-09-13 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cf6c9345-8bbc-3015-b71b-21e8bdcf0427 | -6.8565 | -47.4547 | 2026-09-13 00:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 4033c1fd-ee8f-3ed4-bfef-bd15568c5569 | -6.8567 | -47.4328 | 2026-09-13 00:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 360634a5-d2fe-327b-9a4f-861aaf52fa06 | -10.6824 | -54.1884 | 2026-09-13 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 1af0df92-3835-3e60-b5f4-50905e214739 | -10.6829 | -54.1475 | 2026-09-13 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 210.8 |
| 60c0279e-aa52-39f9-b7ec-8ab295269060 | -5.8206 | -53.8052 | 2026-09-13 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4cd9e782-26b5-3d73-84c1-097e484e24ca | -3.3293 | -42.2893 | 2026-09-13 01:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 9cf46ed3-72d0-3fd6-86cd-758f5ff5a0f9 | -2.9579 | -50.3988 | 2026-09-13 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f2a4ec79-4b1f-3a59-9145-f90e056a0f69 | -6.863 | -55.5801 | 2026-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 23233d8e-cc11-3e6a-ab37-4dc067e9cafa | -6.166 | -57.7208 | 2026-09-13 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| fc166f5b-d7ce-301a-86ae-086a70ab975a | -6.0731 | -57.861 | 2026-09-13 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6cf05aef-42b7-378c-bb65-05e3abd18683 | -10.7015 | -54.1663 | 2026-09-13 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 083a9b1e-80ee-3099-b8cd-4239a10d6981 | -8.5417 | -54.6985 | 2026-09-13 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| eb274aa0-e37e-381f-9fa5-d11c3f82b24b | -6.6021 | -58.849 | 2026-09-13 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a20a4710-cc82-34f7-b07a-3e6ff9e355ae | -6.8446 | -55.5611 | 2026-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d436889d-ebfc-3ae1-9200-e2548b76d614 | -10.7018 | -54.1458 | 2026-09-13 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5dab7428-1116-3ea8-b0ca-4c02b800984c | -6.1845 | -57.72 | 2026-09-13 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 420a5dd0-e46a-30c6-990e-d49f378cc742 | -10.6827 | -54.1679 | 2026-09-13 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 383.7 |
| e0924ffa-5c33-35a4-88c9-988c4f6b2e54 | -10.5286 | -51.3597 | 2026-09-13 01:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 604e2df9-eb9b-3a41-9614-9d53713400c2 | -8.5415 | -54.7187 | 2026-09-13 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 822194fd-9790-3607-b59d-6d30a1e41357 | -15.2629 | -42.7872 | 2026-09-13 01:00:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7bd55b2d-c808-339e-bacf-7138d411642b | -12.8543 | -44.386 | 2026-09-13 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 17ecdd98-1182-3cdc-b4cd-bcadf2dec5e4 | -2.6784 | -57.5504 | 2026-09-13 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c9d9adc8-6cea-3121-8365-49df5d466f8e | -2.6602 | -57.5313 | 2026-09-13 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 90276ed2-bea1-3771-a90d-cbc764c53aa5 | -6.8632 | -55.5601 | 2026-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| ef76c3b5-0a4d-3b38-b362-44c9771e7e47 | -2.6785 | -57.5115 | 2026-09-13 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |


[Clique aqui para ver as próximas entradas](README11.md)
