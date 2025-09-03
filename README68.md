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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9acb6b22-56fc-3dff-b67a-673ee3fefe57 | -11.63412 | -52.05276 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe75b63-c933-3b41-bd61-1773b58283f5 | -7.78455 | -50.95838 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c805e5d9-5e40-3f53-821d-0c5f4f849964 | -11.68809 | -52.14451 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b3bc143-e590-37c3-883b-6009fe003826 | -11.59405 | -52.13618 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 21cddbf2-af53-318a-8c58-80175920b1b6 | -6.85634 | -52.81801 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a817b327-b770-38b8-94d3-d30f76080e9f | -11.53303 | -54.41095 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd44ee55-6455-3616-aacd-1966e10a25ee | -13.27193 | -43.42702 | 2025-09-03 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3718772-65c9-32ba-bdb1-fed5e75a0897 | -13.31203 | -51.77521 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7e4557d-eb81-38c9-945b-24422f5429ae | -11.86218 | -52.42373 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e21b0e4-2352-3904-803c-cbe32affc279 | -14.56176 | -49.1562 | 2025-09-03 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de16a392-d9a0-3636-b624-5e77653b627b | -12.94778 | -56.99426 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7462e85d-b2a1-3aad-a23a-670a8db66dfb | -12.91882 | -56.94107 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fe1802c-1a86-37a6-9dbe-722918b77123 | -13.52545 | -51.80181 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c247d82-06b9-3b9e-a006-2c12785ba31f | -12.63934 | -57.00124 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08f00a23-4666-3ccb-80f0-eea7f3ae2a00 | -13.98964 | -49.5539 | 2025-09-03 04:49:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06729e7b-8971-3b7d-95f8-2f1111a7016b | -12.17969 | -53.89311 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ad67281-856d-3493-ab34-46c2c5208ee2 | -12.93549 | -56.99704 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c8711b5-0a70-3eb7-b359-71bc0610b6dc | -18.06436 | -45.99367 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e0c3f9ec-bcee-3d4c-9239-a48bb8206c45 | -13.3519 | -51.73339 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e41f207e-bb5d-3fa0-8cc5-a5c5da09a923 | -12.89048 | -48.04449 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c1f99e2-be43-38e9-ac2f-2b133d6158a4 | -15.5525 | -48.38231 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fa0cc588-4b71-3ce9-968c-96c566ab4a0a | -12.89729 | -56.95222 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd4f6ada-a669-3523-b6a9-45749d688702 | -12.62868 | -56.99432 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6d28c9-36cc-34a0-a3c7-4b7cb231af5b | -11.66004 | -57.35983 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db61910c-103f-3564-84dc-a2f85aeac2bd | -12.44235 | -50.17048 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26364363-87af-382b-a143-b879e79675d4 | -14.81015 | -48.23114 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75168184-5203-3d21-bbe9-f809c28a79a1 | -16.30823 | -52.95675 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b16d10dc-2330-3029-bc5d-a0c65a26beed | -13.01206 | -48.09503 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 50bc6d26-fd12-37b3-a36b-39a91746e8db | -17.54065 | -46.60689 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98bed2c5-8e87-3893-a1f5-6f5efb5fdbd0 | -11.85387 | -51.53084 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35a8a3c3-96b5-347f-8eb1-cefec234d641 | -13.48654 | -46.82247 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5caea3a-3ce5-37ee-b2c8-0af2e4dc7348 | -14.61319 | -48.09184 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e319b8fe-9aa5-3e77-8043-1c3e28553c7e | -12.91875 | -57.01073 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2a7dd62-19a5-315e-bff5-ba075aed719a | -14.77021 | -48.13727 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9759cfea-7c43-3911-8f81-b9a13522b05e | -15.10836 | -48.12174 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1da90afd-ebbb-3bcb-8659-48c6baeac072 | -11.86426 | -51.48497 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1197eaa0-5d8e-3871-bd53-244d8d214cc0 | -14.3543 | -51.93587 | 2025-09-03 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fc5a8ff-35bb-3b5b-bfa3-cca97f525686 | -11.86835 | -51.54773 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b571596-6632-3156-a1f3-10e0c02a4838 | -14.60524 | -48.03082 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aa619f5-1562-31c5-a761-b982cf79f7f5 | -12.92524 | -48.08601 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 144c2df3-3b35-376f-bb30-c56c47335b83 | -14.61548 | -48.10481 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ae191d3-fd15-3bdd-bd80-e4d1e4a46c84 | -13.27032 | -46.89053 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5ad723f-548a-3005-b287-6a5b9bbe0766 | -14.06378 | -54.01274 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35ed09ac-58af-3adc-af96-bc1c3e5ef6e7 | -15.01913 | -50.04633 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1638831-76f2-341f-9a3f-a95de6c278f5 | -13.28628 | -46.83457 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12fe31b0-f3ed-3c74-a0a3-cb80746f32fd | -13.5781 | -48.13967 | 2025-09-03 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5f0d7268-b715-37aa-8999-eceaba79107d | -14.5713 | -54.53345 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 629783c4-6563-3514-ae0e-e33d568221e3 | -13.3004 | -46.925 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61622ddc-3286-35e2-abef-d09dc5b6367a | -12.97607 | -54.76304 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ffe40c5-5beb-36fa-b7ae-7fc57882845f | -11.47413 | -54.61728 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2470f46-9d40-3a3c-a576-69f61472b661 | -13.31258 | -51.77161 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93e3f478-c9a5-325c-bd41-ea83ad905c24 | -13.28212 | -46.83553 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b40efe3c-de28-39c3-8e6f-c0fddbd376d2 | -17.43757 | -47.20668 | 2025-09-03 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5286e08e-e88f-364b-8fee-88009689b8ae | -15.57312 | -48.3172 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 988dd54e-de9f-3d59-a00d-8612716ff14a | -15.01735 | -50.05899 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 980e3725-6ea0-3e56-8544-639e8817ce13 | -12.60995 | -57.01095 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af6e8611-add6-323b-b6f7-448305ff0804 | -14.33168 | -60.34009 | 2025-09-03 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34ef826e-5a5e-3922-aa3a-541b1adf7f9e | -14.34435 | -52.79579 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57cf9a6b-1445-3dd4-980c-1bc482330bc7 | -14.4024 | -51.66341 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 820db38c-866e-3a52-aecb-fe289fb02127 | -12.87305 | -48.02666 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 062d881f-fecc-382a-b438-96e54aa724d4 | -16.29112 | -52.95755 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c607668f-6b7d-377c-ba0f-a5e64ee9b531 | -15.72115 | -53.64712 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b66e1d19-abfe-351a-a96a-d706bd7b178f | -12.44465 | -48.70856 | 2025-09-03 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3644f39c-01f9-3622-b63e-97069cb02b54 | -16.30051 | -52.94072 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80011b99-912e-3bd7-bcb5-93c9b66db43e | -12.48551 | -53.83186 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66e1c1ac-5e6d-3ce2-8192-87fb8131e6e4 | -17.53435 | -47.58564 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e0c6b29-e8e7-3340-ba12-51bfa59cdbe8 | -16.29493 | -45.6896 | 2025-09-03 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c7d8fef8-5eb0-323d-bf37-5ed2c0c0938a | -13.50975 | -47.03723 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dfe5065-23ea-3c79-aae4-88fc4d39c6fe | -12.86268 | -48.1856 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 978f0675-cb34-301b-8bc6-531c1e0e70e1 | -11.8631 | -51.47017 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba0ee21-cae5-32de-bd5c-292eeafe8e44 | -14.98123 | -50.21642 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67b138bf-772c-3f17-8639-0cab763154f8 | -13.48592 | -46.82708 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0cb0de8-61c6-3ced-b986-bd0d099bda23 | -12.91963 | -56.9363 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dd2faad-85b8-31b1-9b18-6580884a9d9a | -15.58167 | -54.32879 | 2025-09-03 04:49:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c8180a3-ee07-39d9-8cf6-cf0071c8b5ac | -13.70803 | -46.93733 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c865e436-c42c-3870-aa08-ce6f15db3dcc | -16.71982 | -49.07682 | 2025-09-03 04:49:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e088875-67ef-36a5-bfdf-9315ad885495 | -15.55644 | -48.38307 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67a046e7-14c5-33a0-a23e-87546d66504d | -11.83105 | -51.57112 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85515d7e-cadf-3e59-b605-270d6e069239 | -11.66985 | -57.35073 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 662c8de3-7cf7-3d0f-ac8d-6d028ebae1bf | -15.72558 | -53.64055 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 188e6816-8212-3d09-a316-275175392f34 | -14.38347 | -53.26345 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01032b93-6630-3c59-8511-60b4ca57003d | -16.29333 | -52.96528 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8ed8dea-243a-37c9-b46e-9a44c8349e63 | -12.49182 | -47.48132 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9afaaa22-e360-334c-9411-3ea0438f832e | -15.21659 | -53.78267 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 431fabd5-859b-388f-9e5b-a3e6f3bf5fea | -15.6004 | -52.67527 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3bb93a4-5838-32bb-b1dd-a154b012923b | -15.55466 | -48.37542 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7ef8e9b4-17ed-3219-bcc7-97c53af77831 | -12.88017 | -48.03279 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66eb2924-a296-3587-bd6c-3a994eed5942 | -13.50045 | -46.81595 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab682deb-eac7-3a4c-b4d3-b690bfd444d3 | -11.86163 | -52.42723 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f55789a9-cf14-3253-897f-f3e46b0c3ddd | -12.49104 | -53.84022 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159946ea-46ad-3792-9672-4e20b7b96d73 | -14.99884 | -50.06043 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4d27a80-471b-3070-8565-fa0ff7172f61 | -13.09975 | -57.1337 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f8f3782-0e78-3862-b866-fce791fa1c7b | -15.14995 | -52.35526 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d7c11a-e4e1-35d5-ac0e-c310dc18944f | -14.38733 | -53.26045 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 037e6b9e-26d5-3b3b-ab90-ffb9f1669b0e | -15.54568 | -48.35221 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4531e8cc-f67f-3652-a0ad-2bea1e644726 | -13.00681 | -48.10445 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d6b0dc1-612c-3fbf-a171-1a420ead56d6 | -15.58283 | -54.32158 | 2025-09-03 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6881bf8d-139a-31c9-ad1e-2321ffab53da | -17.62272 | -46.70303 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4131ba08-5b61-3f75-9115-513e1952acf5 | -13.50609 | -46.93391 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55d4d4b4-82a0-3b18-9ded-3a0ae27eabaf | -15.26846 | -52.73518 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README69.md)
