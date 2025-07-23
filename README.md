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
| e1ac9a86-652e-3774-b29a-332d817087fd | -7.7381 | -44.0202 | 2025-07-23 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f6c6212a-d06a-3f17-b75d-a4c3033cca06 | -9.0642 | -45.0749 | 2025-07-23 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| f20fb21c-c70d-37a7-b467-aa263c31f9b6 | -3.1833 | -49.4429 | 2025-07-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 184.1 |
| e1b007f9-51f5-30d5-aa66-d7ab1daaf96e | -9.0646 | -45.052 | 2025-07-23 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2977e314-496a-32cb-9393-eb69929ead7d | -3.1648 | -49.4648 | 2025-07-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 295.7 |
| 8eb8392a-de53-3e47-8535-32e05236c936 | -13.7169 | -45.6833 | 2025-07-23 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2a2a1b1d-9d1b-32c4-af0a-71aa0445c0e2 | -3.1649 | -49.4435 | 2025-07-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| d9d50048-918d-3524-9bfa-7cc162fe28bb | -7.7569 | -44.0183 | 2025-07-23 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 1db8f6d5-7905-3e6e-a8df-801bde58ac3d | -7.2283 | -49.5897 | 2025-07-23 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 44f66140-3287-3674-a2ea-95dc698fa604 | -13.6582 | -45.7161 | 2025-07-23 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 816f1b1c-fb18-3334-9835-a4bff165e22e | -3.1832 | -49.4642 | 2025-07-23 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 280.5 |
| 4d44ff44-986a-3a82-90c8-205dbe6cff00 | -7.2281 | -49.611 | 2025-07-23 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f4506488-ce32-386d-81e8-3448e384263f | -13.5451 | -43.7001 | 2025-07-23 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0e20266a-6d88-3ec5-956f-39823cec68a4 | -7.1966 | -45.3313 | 2025-07-23 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| bbebfa4e-2013-373c-aba4-9ea541335672 | -7.2096 | -49.5911 | 2025-07-23 00:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bceb32d0-10c2-32f5-bc98-1a591b3ff283 | -13.7169 | -45.6833 | 2025-07-23 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8cdef075-4f55-3a72-ac44-5cfcdb21cc5e | -7.2096 | -49.5911 | 2025-07-23 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8445519a-2ee4-3848-8e42-0bc034252d73 | -7.2283 | -49.5897 | 2025-07-23 00:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| dfd7d96b-d997-3160-bf98-1f7e87e82132 | -7.1966 | -45.3313 | 2025-07-23 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| f7714775-7645-3cc8-b063-1afb8cf7d986 | -21.4004 | -54.1425 | 2025-07-23 00:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7d8cee06-086e-3414-a30c-ab7606e785ff | -3.1833 | -49.4429 | 2025-07-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 83bb91db-3d7f-370f-9be8-3d2d89945d1d | -7.7569 | -44.0183 | 2025-07-23 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 197.9 |
| c4befc07-7622-3147-84a3-ac21c2fcf648 | -7.7381 | -44.0202 | 2025-07-23 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 61899487-d8fb-3403-abd7-44ae144372d2 | -9.0453 | -45.077 | 2025-07-23 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 5fbe9571-8995-3589-bec2-fcbc1a7d254a | -9.0456 | -45.0541 | 2025-07-23 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 967d0d17-e01d-3081-b5eb-371154e2b3ab | -3.1648 | -49.4648 | 2025-07-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 249.3 |
| 08026fef-7f90-3ec2-9714-e80b1764809b | -7.7567 | -44.0415 | 2025-07-23 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 54858183-0f72-33d4-9170-ff35d2586375 | -3.1832 | -49.4642 | 2025-07-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 212.8 |
| bc21a98a-32b1-3bad-b173-7b780c413a58 | -9.0646 | -45.052 | 2025-07-23 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 6b02a093-57f0-3eb6-a862-42aa179e1ce5 | -9.0642 | -45.0749 | 2025-07-23 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c388c5e3-50a3-3acd-9ef2-aad5fff1ad07 | -9.342 | -49.8394 | 2025-07-23 00:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5bbf234f-f3ac-3f1a-abc5-0d6a595ce50b | -13.5451 | -43.7001 | 2025-07-23 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 606fa01b-ded5-3320-b7c1-ccfa650f56b6 | -3.1649 | -49.4435 | 2025-07-23 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 235.3 |
| 67676383-d578-3ce8-9aa7-74fec8a97e7b | -7.7569 | -44.0183 | 2025-07-23 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| be2176e7-d8db-3ca6-ae74-d31cf1c609d2 | -13.5451 | -43.7001 | 2025-07-23 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ea5ffe3f-ffd5-3943-a798-995800c74212 | -7.7567 | -44.0415 | 2025-07-23 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ec1e5835-4d92-346d-8b81-7af527a79808 | -7.2283 | -49.5897 | 2025-07-23 00:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1f5b3952-8a4e-3dc6-815f-cac7df69bbe7 | -3.1649 | -49.4435 | 2025-07-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 228.4 |
| 963cdea2-2d7d-3141-b2d4-6ce31e971719 | -21.4004 | -54.1425 | 2025-07-23 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 51.9 |
| f4622f88-093b-3d47-8b67-908074b208b2 | -7.7381 | -44.0202 | 2025-07-23 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4202cd42-bc0a-3f50-853d-a936609e0cef | -3.1832 | -49.4642 | 2025-07-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 220.2 |
| f3dbc8f3-7149-3794-9098-fceee911776b | -13.7169 | -45.6833 | 2025-07-23 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 85b0d2d9-0db9-3269-84e8-3d5866e4b08c | -3.1833 | -49.4429 | 2025-07-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| f78bd3be-8d6c-3242-b595-56319cd4fbc4 | -9.3232 | -49.8412 | 2025-07-23 00:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 03b5a4ec-310a-3444-9a36-2651e07a6a70 | -7.1966 | -45.3313 | 2025-07-23 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 391bbe96-34d8-342a-836b-774c9dc234c3 | -9.0646 | -45.052 | 2025-07-23 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| ecd0e3da-c655-315b-9835-96ea2a5ebf3e | -3.1648 | -49.4648 | 2025-07-23 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 273.0 |
| 34accebe-dd07-3cc2-b214-8ee319d21909 | -7.2154 | -45.3297 | 2025-07-23 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| be37fcb9-7a55-3a41-ae5d-4ea92cc4d767 | -3.1648 | -49.4648 | 2025-07-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 6dd0888f-33d3-3be0-b3f2-96c15bbf3477 | -9.0646 | -45.052 | 2025-07-23 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 54bd5871-9942-3a48-8d4e-af72632e3e37 | -7.7381 | -44.0202 | 2025-07-23 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7e052167-79cf-3909-9b5f-c5368fabc912 | -3.1832 | -49.4642 | 2025-07-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 301.4 |
| e204fac5-cfda-3cc1-b1d8-d9c132cacf3e | -3.1649 | -49.4435 | 2025-07-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 7f610280-9faa-3825-9bed-51c37335abbf | -7.7569 | -44.0183 | 2025-07-23 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a7d3fc9d-2fcb-3ecc-8192-7d9ecda44e77 | -13.7169 | -45.6833 | 2025-07-23 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b80135fc-b1c7-3bf3-9cd9-4e605388019b | -3.1833 | -49.4429 | 2025-07-23 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 273.2 |
| 3caa2d6e-7a39-32e5-b0b4-c5cb4562d427 | -9.0642 | -45.0749 | 2025-07-23 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d5d28113-4fab-3f04-bfba-523085250e01 | -7.1966 | -45.3313 | 2025-07-23 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 11ae90a3-de43-36e2-aad8-a3278ae2afa2 | -7.2283 | -49.5897 | 2025-07-23 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 84c9f5f4-0b3b-3bab-919e-9ca0b6daacc9 | -9.342 | -49.8394 | 2025-07-23 00:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4c117b5a-7361-3658-8ff0-b395af09371d | -3.1649 | -49.4435 | 2025-07-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 269477a4-fc2e-36cb-885d-0a0a58c2f330 | -9.0453 | -45.077 | 2025-07-23 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 67444fc8-b217-3e37-a522-efbecb8a8bab | -9.0456 | -45.0541 | 2025-07-23 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a94392a0-6cfd-3d58-8867-69ebbfdf2c98 | -7.7569 | -44.0183 | 2025-07-23 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0e2a7f9d-8c21-347c-a31b-a124d515e3b4 | -23.7209 | -51.7182 | 2025-07-23 00:40:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 52cdeb78-2c4a-3c8e-b6dd-fc6f2ac9d2f9 | -9.0646 | -45.052 | 2025-07-23 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 160.1 |
| e58d4bc7-0758-3e0c-957b-b8a53233e054 | -7.2283 | -49.5897 | 2025-07-23 00:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6f76b0ec-f066-379f-8e2e-f10db35145b6 | -7.7381 | -44.0202 | 2025-07-23 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 72ff747d-8446-343d-a4ae-b354731b0b46 | -3.1648 | -49.4648 | 2025-07-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 398cc487-1ba0-37d5-a067-2fee076e26b4 | -7.1966 | -45.3313 | 2025-07-23 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5eb84269-e35d-3d0a-a5b4-6cfcf31e8ac2 | -9.0642 | -45.0749 | 2025-07-23 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 13fc0dc7-7a70-32b4-a092-9ebc9e8157d0 | -9.342 | -49.8394 | 2025-07-23 00:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 96c9d836-d24c-31b5-b56c-ef1c80b69e77 | -3.1833 | -49.4429 | 2025-07-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 194.8 |
| cf57c555-7e35-3c3a-b12b-f1e585b6a927 | -13.7169 | -45.6833 | 2025-07-23 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 584e85f2-e27e-3b77-a5e5-52fc06b580f2 | -3.1832 | -49.4642 | 2025-07-23 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| ce977085-e361-3629-9826-3b9867376356 | -9.3232 | -49.8412 | 2025-07-23 00:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8b0fadb7-6b15-3b83-8026-203e8fa52d4b | -16.1193 | -49.9645 | 2025-07-23 00:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 2f468ab8-545c-33e2-9105-40f87f716878 | -9.342 | -49.8394 | 2025-07-23 00:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 8005ddb1-57d7-332c-ae9a-a89cf8233a80 | -9.3232 | -49.8412 | 2025-07-23 00:50:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 76070200-cbbc-36c6-80a7-bda99f578918 | -9.0646 | -45.052 | 2025-07-23 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 26a16716-a9ef-3300-8ccd-85b890df567c | -3.1832 | -49.4642 | 2025-07-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 295.5 |
| 48aa473b-d267-3bd4-adec-cee288281df7 | -3.1649 | -49.4435 | 2025-07-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| cfa0ad7c-4ef1-3d3a-9359-a34a1bd614e9 | -7.7569 | -44.0183 | 2025-07-23 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 1fab4cbc-4e45-3688-952a-c5f10e4f5644 | -3.1648 | -49.4648 | 2025-07-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 9be93d09-ff3b-3173-9d90-2a7606af55ac | -7.1966 | -45.3313 | 2025-07-23 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ea85a4b1-fa5f-32a9-99b6-d1041ad977b6 | -3.1833 | -49.4429 | 2025-07-23 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 209.3 |
| 09f05b48-e317-30fa-8a9f-82d33887e19d | -7.7381 | -44.0202 | 2025-07-23 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 88f09615-f21d-3dcf-80a6-09195a5a60c0 | -9.0642 | -45.0749 | 2025-07-23 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 6585022f-4489-3674-bb0a-abec20426c03 | -3.1832 | -49.4642 | 2025-07-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 246.7 |
| fe40f8fc-685b-312a-ae88-4df6eb0f6ce8 | -3.1649 | -49.4435 | 2025-07-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2e8fc7c4-b407-394f-872c-82d4215fbb47 | -9.0642 | -45.0749 | 2025-07-23 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| a95b9ae2-6fc0-38ef-ac9f-e6c5dc423b4b | -16.1001 | -49.9457 | 2025-07-23 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 25ea4e16-0316-32ea-ab7e-a3a54b6cb0c3 | -7.1966 | -45.3313 | 2025-07-23 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e981e305-56f9-374a-836e-6fa2650a64fd | -16.1198 | -49.9424 | 2025-07-23 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| ec48f3f4-5415-3ebc-b6af-f9130c53d020 | -3.1833 | -49.4429 | 2025-07-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 57cae7b9-5757-32b1-aa9d-9ae26bfaacf6 | -16.1193 | -49.9645 | 2025-07-23 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 113e7465-ddfc-3eaa-b272-cb41745e46b1 | -7.7569 | -44.0183 | 2025-07-23 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| fdc5acd2-041d-346c-b792-66d19f00e0d9 | -3.1648 | -49.4648 | 2025-07-23 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| cde041bd-3ae7-3f51-a78f-d3a27a825568 | -9.0646 | -45.052 | 2025-07-23 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 84943de9-704f-3395-a6cb-1524412d9e6a | -9.342 | -49.8394 | 2025-07-23 01:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |


[Clique aqui para ver as próximas entradas](README2.md)
