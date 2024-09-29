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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d5575f6-7496-3773-9ac3-8e026d54635c | -18.35011 | -42.76643 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 866b39e0-252d-3e2f-8f56-123c1f0b424f | -18.34879 | -42.77221 | 2024-09-29 03:13:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 050887fd-fd66-3e10-8f7b-9aad2fbba286 | -18.33092 | -43.05972 | 2024-09-29 03:13:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 25d63373-d640-39b2-b9bc-c643bb95a58a | -18.33084 | -43.0535 | 2024-09-29 03:13:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 04bd6d06-9e93-3dad-b8af-b6616588bc08 | -18.32944 | -43.05947 | 2024-09-29 03:13:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ddb981f-3a35-3505-8c6e-147e8816b05a | -18.29434 | -42.16991 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d04a5396-fc5f-3e2c-b268-3897847f0102 | -18.29347 | -42.17381 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e622db49-3ed5-3b39-ac0c-0bb99476350f | -18.29194 | -42.16981 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 56753d2f-4fe6-34b8-bf97-dfb23ecd6173 | -18.29106 | -42.17361 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 97803974-14fc-37e9-8c8f-82a5ba2ae96a | -18.28762 | -42.17081 | 2024-09-29 03:13:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0537c799-c4a5-38b4-a102-62fb6a15d6b0 | -18.22942 | -42.4693 | 2024-09-29 03:13:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| afc94dfd-282d-3061-a9b8-2a7440b098a4 | -18.22774 | -42.46769 | 2024-09-29 03:13:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a61d1fce-1f2d-3442-afb0-27f7eeacc42d | -18.22653 | -42.47306 | 2024-09-29 03:13:00 | NOAA-20 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b375052-a719-3188-a30d-9eb756486468 | -16.92162 | -40.24485 | 2024-09-29 03:13:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 96f20d0b-c5c6-3d96-8a52-3b79d03aa443 | -16.92083 | -40.24855 | 2024-09-29 03:13:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5c95e71e-148b-3c49-aa24-ef1faab08b5c | -15.83406 | -42.16387 | 2024-09-29 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 340fc457-64e2-399d-8634-8ad4bb79f4f4 | -15.83296 | -42.16597 | 2024-09-29 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 7e832a8a-8390-3505-a7f5-6d1ecec2b72a | -15.83286 | -42.16945 | 2024-09-29 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 4d0b0f23-6d22-3a54-8a09-da2609472e68 | -15.83171 | -42.17162 | 2024-09-29 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 69fabcb3-f4ab-3a7a-abb3-d0322a80fc5f | -15.83162 | -42.17519 | 2024-09-29 03:13:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 16bfff5c-a13f-3a5e-a3b7-208ab96c71b4 | -4.14401 | -43.72366 | 2024-09-29 04:00:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5f2b89c-b307-3a0d-9ee1-80c1f7032962 | -2.33098 | -45.52236 | 2024-09-29 04:00:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 536ef2c4-299a-3cac-9b74-593ac1f67b57 | -4.30142 | -44.71317 | 2024-09-29 04:00:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10b65ec6-c833-3af6-ac37-0b5a776dc948 | -1.1773 | -46.71555 | 2024-09-29 04:00:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 299ac24d-e360-393a-abe9-16b00c45a823 | -1.17237 | -46.71476 | 2024-09-29 04:00:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2e943b51-fbdd-397d-9b8a-4a03a777d471 | -3.47178 | -47.53462 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22f667b7-f46f-35d6-a0af-13e4b0a53822 | -3.47131 | -47.53739 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08279d40-9a63-3197-a26a-e38205cbc556 | -2.72266 | -46.72395 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17298d79-2e38-333a-b341-1cfc2518e33a | -2.72167 | -46.72694 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2aeed3d3-d8fe-396c-9537-ac32590f08ea | -2.71784 | -46.72316 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3482e3df-d1d0-309c-93da-a0dbce9192db | -2.71701 | -46.72838 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d7ccb63-bd0c-3fa6-bb46-29dc813b2c9c | -2.71686 | -46.72614 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0ef4c3c3-f752-3a89-a830-d6911cc1dda9 | -3.70131 | -47.60877 | 2024-09-29 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa00b55b-c7b5-30ca-8603-019d08f176d5 | -3.70083 | -47.61165 | 2024-09-29 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a855c6bb-8f7f-3277-996e-cc641c88afaf | -3.92066 | -46.46221 | 2024-09-29 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ea7d2e2-271b-3b59-9546-39483b3e1fb3 | -3.91603 | -46.46137 | 2024-09-29 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b247d69-0aa7-360b-ab61-4a1e8ae207cc | -3.91519 | -46.4665 | 2024-09-29 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3eded0da-109f-3a85-9cea-ba07c0a88804 | -3.9114 | -46.46062 | 2024-09-29 04:00:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe954de0-1145-3c51-9a48-a867e4936ccc | -2.02638 | -47.65471 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2185ee7-7e3a-34eb-be17-0bb03a3dd0bf | -2.02585 | -47.65786 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 968abea2-1870-3e19-8b5e-17e3b9343104 | -2.02483 | -47.65666 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| db27f508-4ee9-3360-b424-eaa41a0a07a9 | -1.872 | -47.90629 | 2024-09-29 04:00:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21ce9bf-270b-3d6c-8fa5-1acb9d832dad | -1.63617 | -48.67784 | 2024-09-29 04:00:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be01aed4-35ac-30b4-8eb3-9bd4b44c67a0 | -1.63465 | -48.67735 | 2024-09-29 04:00:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02adc28b-750c-3051-aded-0d1285dccbe0 | -3.70034 | -47.61457 | 2024-09-29 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bc13986-44b2-3be1-a3b9-8ec7f52bc4da | -3.69985 | -47.61749 | 2024-09-29 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a38459f-ee86-385b-9db1-1da52d8e6e29 | -3.69937 | -47.6204 | 2024-09-29 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e72107a3-6a04-31a5-bb46-ac068873665d | -3.47124 | -47.66162 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| beabe567-a16a-34ac-8093-90e85f68e1d9 | -3.47075 | -47.66451 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e9ca8e0-c28e-378b-8f6c-f0881efeaf21 | -3.41151 | -47.5895 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97baa7e6-2b52-3f98-92b8-33078c604103 | -3.41103 | -47.59246 | 2024-09-29 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54b0e1ec-b023-35a2-8034-442043acb7b0 | -2.63936 | -48.25338 | 2024-09-29 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c08ab29a-4e42-3645-b4ba-784749d19996 | -2.59276 | -47.65439 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4d4a7f-085a-3750-a0d6-92cb441d43d3 | -2.59224 | -47.65747 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1cd5d5-ec91-3091-8c29-06ae183b17d0 | -2.59174 | -47.66052 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ede1370-764e-3ac2-922a-2e86fe016609 | -2.4658 | -47.83311 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba4dcad4-2e4b-399d-9bdb-881b79448051 | -2.46527 | -47.8363 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e9e4035-030a-353a-b6ed-9d8a616db354 | -2.41931 | -48.45209 | 2024-09-29 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39f6c16d-9ec8-3064-9e5e-182fc6129826 | -2.36453 | -47.60124 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 9c75ed1f-6938-38d3-8e39-8e625cb56dbc | -2.36402 | -47.60431 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 9c3594bd-ffb3-3ddb-978a-71e7d90b4794 | -2.3635 | -47.60742 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 06123c56-148e-335b-ae3c-c028539f6fca | -2.36298 | -47.61054 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| bd4f3787-c862-3ef0-832f-3577ef8eb5d9 | -2.35887 | -47.60349 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 43c3da5b-0196-3a60-b0f9-d7ad1496a859 | -2.35835 | -47.6066 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7b06806e-2ab4-3184-a60a-febc8320cbdf | -2.35783 | -47.60972 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 231bc5bf-2838-3e5a-8650-26d3701ce7ea | -2.35623 | -47.60528 | 2024-09-29 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c6aaabb-0ca1-381c-97a8-1c0791d70a1d | -2.35572 | -47.60841 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b328362-06b7-34c3-bc6b-912fc2878880 | -2.35523 | -47.61155 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 31bcc587-7f37-352e-879f-3d900aaae881 | -2.35268 | -47.60889 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 749b0015-2043-3560-a821-850a62e77915 | -2.35216 | -47.61201 | 2024-09-29 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 058526a7-abba-3281-8b2d-e91a16ec1312 | -3.14487 | -50.2748 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f71b7937-5516-3aa3-a4fd-8c14d418c6b6 | -1.38009 | -49.34729 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9fabb45-5852-3247-8be5-b59822ba18a3 | -1.37422 | -49.34636 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68aa8357-da23-3966-84dd-76093a6eff69 | -1.36454 | -49.33192 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9082a3c-5c00-318f-92e7-cbaff0cdb51f | -1.35936 | -49.3268 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4aa135f5-6260-3f26-aad6-f97097d1fe7c | -1.34592 | -49.2989 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65dcdaa7-be7e-347f-85a8-3ab1deb7a3c4 | -1.34076 | -49.29381 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2611d5fe-5501-36b6-90b2-5f997b8f1798 | -1.33649 | -49.28788 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c27ab95f-770e-34f5-b4f9-2da116675dfd | -1.33582 | -49.29209 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40670a8b-a875-3f25-8f38-17c788eb8fe4 | -1.33561 | -49.28868 | 2024-09-29 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c873f27-1131-36cf-822f-4aa5377a4b22 | -3.33535 | -50.30656 | 2024-09-29 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d0c0e2b-bce3-3ad7-b13c-2c25d70896cb | -3.3293 | -50.30559 | 2024-09-29 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cae6cd7e-5f85-30c3-a9e9-c448efa033b2 | -3.32242 | -50.30942 | 2024-09-29 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2673d31e-c645-3f19-b6a2-91bdffcc5141 | -3.24079 | -50.0179 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7f97041-b1b3-3381-ab57-444d4acf5498 | -3.23784 | -50.01472 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d407d60-7558-3a2e-ac35-1e3903d4449c | -3.23709 | -50.01927 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0071a56-8997-30be-9aa4-176a73dd26ba | -3.23562 | -50.01244 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6debaca-1edb-3a3b-92b1-ecad831c0af1 | -3.23484 | -50.01692 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b23e094e-111f-39f7-bece-0ae5c4ee2a52 | -3.19319 | -50.43725 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1ac9070-e5dd-3aba-9f3e-23c943884d63 | -3.19233 | -50.44224 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39769ed7-9d42-3663-928f-588c8dc0737c | -3.19149 | -50.44711 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffb4d736-aae9-366c-b62b-7496330b116b | -3.14564 | -50.27028 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffc534b6-f977-344d-b624-d98713bfc9e2 | -3.13883 | -50.27373 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c61dc46a-fef5-3c35-b663-6f090668b964 | -3.10943 | -50.48376 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0bb8aac4-7631-3b79-b6ea-78f8aad58014 | -3.10864 | -50.48842 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b34e0a6-e7bb-3bf1-8c41-6db0a9f35502 | -3.10328 | -50.4828 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7ba1230-4ad2-3d9c-96f6-b15822828488 | -3.1025 | -50.48738 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1499b072-a200-3b0e-ae23-75b349e8e283 | -3.09182 | -50.476 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4d04fb17-6498-3dce-827b-b4162b8ce9ab | -3.09102 | -50.4807 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d80707f5-283b-3ddc-845a-d0a2f27d00e1 | -3.09023 | -50.48532 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |


[Clique aqui para ver as próximas entradas](README20.md)
