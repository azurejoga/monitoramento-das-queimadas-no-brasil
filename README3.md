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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ccb6867-6329-3e5f-b418-57da9e853bc4 | -21.0051 | -47.3904 | 2025-06-18 00:40:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ffa9aa89-e0bf-3716-910e-ff4ffaf8a3e8 | -8.7314 | -49.0367 | 2025-06-18 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 8f0b3488-29b8-3bcd-8d27-d19d9672de6a | -8.7317 | -49.0151 | 2025-06-18 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 2bc4b1fd-f565-3048-9d6b-f36aadb85958 | -14.4273 | -48.9093 | 2025-06-18 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 762f5e4f-af32-3332-919a-8e000541251c | -20.9845 | -47.3955 | 2025-06-18 00:40:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b306fe66-43fd-3a15-969b-a8dcd744e82e | -11.952 | -58.7376 | 2025-06-18 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| b055e7d3-de51-3b3f-9304-d2de06fc2016 | -8.7314 | -49.0367 | 2025-06-18 00:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 06442c44-fd14-30c7-9ff1-b069443702b7 | -21.0051 | -47.3904 | 2025-06-18 00:50:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b4205779-11b1-3a50-9723-371de36e0ad6 | -6.118 | -42.5323 | 2025-06-18 00:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 40687ea2-4dc1-369f-a71c-11ef74ab79f7 | -11.1379 | -53.9429 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 395.8 |
| ead744ac-62d3-3922-b256-2cbd616d96c3 | -20.9845 | -47.3955 | 2025-06-18 00:50:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 825883f7-cf77-3d59-860f-a1df4e7b0dc8 | -10.9164 | -56.8536 | 2025-06-18 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f519d875-42bd-353f-8288-b348f54fc7d4 | -14.4467 | -48.9063 | 2025-06-18 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4a92f235-ef17-3a37-a9cd-8d39e0e1c78e | -11.1382 | -53.9223 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 273.7 |
| 3bd6295a-dd21-3759-bf7d-4c0063348eed | -11.1568 | -53.9411 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 6960635a-10ee-3768-a058-3e78aee73b12 | -11.119 | -53.9446 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 2fe17356-ac7d-3c27-a959-a7bab0ee359b | -14.4273 | -48.9093 | 2025-06-18 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9f873f41-fc5d-338f-805a-cf7d9501d190 | -8.7129 | -49.0168 | 2025-06-18 00:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| eae57316-7a48-33e3-9e38-2ef84e0f338e | -8.7317 | -49.0151 | 2025-06-18 00:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9fe271e1-6f29-3084-9c14-1d57c9d8344d | -5.9028 | -43.4418 | 2025-06-18 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a7b53e77-1c77-318f-ade6-39f23b031eb1 | -11.1571 | -53.9206 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 6804309b-6512-3dfd-aa76-89dd22b654d8 | -9.4807 | -56.0801 | 2025-06-18 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 696e6709-2f6f-3b99-9aba-88411563ff9b | -10.9167 | -56.8336 | 2025-06-18 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 26c0655e-c7e0-3ea0-965b-482a0674e992 | -11.1193 | -53.9241 | 2025-06-18 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| a33c07a4-ad15-344b-9bf1-32934bb0f010 | -10.669 | -49.3597 | 2025-06-18 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a07e2a15-7e75-3eec-b906-21951955cbe7 | -9.4993 | -56.0988 | 2025-06-18 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| c1921f90-1be7-3a3e-ab2e-440c6905253a | -9.4994 | -56.0788 | 2025-06-18 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 60c3d88e-2524-3bdd-8a6d-466077b66134 | -20.92891 | -49.09459 | 2025-06-18 00:56:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3d8beb57-fea3-36e1-a2b5-7a0e52286f2a | -20.99314 | -47.40213 | 2025-06-18 00:56:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c9a292ca-a00f-38bc-82ed-001e33499342 | -19.48086 | -49.28556 | 2025-06-18 00:56:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c007ab1-c81b-33d9-a48a-a49c2d958aee | -22.77988 | -49.32096 | 2025-06-18 00:56:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c6ea9643-aaf8-334f-a8b7-423687e68614 | -18.99475 | -52.09069 | 2025-06-18 00:56:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ea2f4756-3e79-3f4c-8534-421c80f7cfb7 | -21.37105 | -48.96644 | 2025-06-18 00:56:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a55422df-2122-3116-b538-754322df4850 | -20.99122 | -47.39003 | 2025-06-18 00:56:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 2ce02507-ce2c-389c-9a07-fe31c6a21d10 | -19.48239 | -49.29573 | 2025-06-18 00:56:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d81b4cee-3ff1-39e7-b318-59f5aa3e5c93 | -11.78364 | -48.32502 | 2025-06-18 00:58:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0d033c4d-d165-3073-8c38-63abd0684978 | -14.06949 | -53.37458 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 26f4e11a-ad02-3f72-8dac-8c2032c38788 | -13.942 | -54.50104 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cd1db682-f214-3495-9b26-5d555a265cb6 | -12.65855 | -54.10961 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 07b888ae-871b-3610-820e-4366e155cd5c | -12.65206 | -54.12994 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| d4b50fae-25c8-35bf-827f-521edfc9d510 | -13.58172 | -59.23699 | 2025-06-18 00:58:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 12e6b7fb-78e5-359c-9a00-a0ee29a138fb | -14.19665 | -45.51072 | 2025-06-18 00:58:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6d5387a5-f290-3a43-b35d-17fa123d8d9c | -14.03214 | -55.1289 | 2025-06-18 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8e1e626a-551b-3792-9eb4-d3b3bcb27f2e | -14.07198 | -53.39315 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f608b120-0951-32a4-b40f-9f62d6ce2df8 | -14.0225 | -55.13025 | 2025-06-18 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ce59945-e67d-3547-9673-5d992652c1d6 | -12.52457 | -57.7688 | 2025-06-18 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 68932ffe-2d89-388e-b314-db57c62ad294 | -12.34502 | -49.30231 | 2025-06-18 00:58:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f2c9052d-69e1-3163-9804-a7b88faf3c77 | -12.65983 | -54.11913 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 88b3edd1-0cce-37ec-bc2d-190980785df7 | -12.52777 | -57.22068 | 2025-06-18 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5faed22b-8419-3e01-9a55-a98f12df4847 | -14.43798 | -48.91169 | 2025-06-18 00:58:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 163.6 |
| a0ba510e-6686-380f-a089-553dafdd9422 | -14.07074 | -53.38386 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| bd25b38a-65fe-3a0f-969d-f9912ee0b5a6 | -14.43982 | -48.92346 | 2025-06-18 00:58:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 621c4f25-bf59-36f8-a24f-72e81cc49aaf | -12.34682 | -49.31429 | 2025-06-18 00:58:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7ddb8be6-cdb3-3479-a7ef-ad7418e0677d | -12.52374 | -57.2127 | 2025-06-18 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5ff85329-4238-3f8a-8d12-b1d4a8e464f1 | -13.80546 | -54.30221 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e3dc01b7-3690-32c9-bf20-c9a430ea3124 | -14.43612 | -48.89975 | 2025-06-18 00:58:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 79bc4f59-c677-380a-85e7-1cfaee8ae93b | -12.57972 | -56.98222 | 2025-06-18 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1ad846b8-11b6-3eed-a4f0-1d8b8eb44e5e | -13.79755 | -54.29906 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 955da8ad-7907-31ac-9b31-a1bc7ce1b679 | -12.65078 | -54.12041 | 2025-06-18 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b223bcb9-d5c3-30ca-9416-7c00b06d1299 | -12.212 | -49.64733 | 2025-06-18 00:58:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2c002ab0-35b1-3e1b-829d-5e7550d0f608 | -14.03077 | -55.1181 | 2025-06-18 00:58:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ee043c67-4687-3be8-a698-799c22326378 | -13.64827 | -53.94097 | 2025-06-18 00:58:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b387afa9-f601-3a54-bba4-e65adda65385 | -16.31129 | -58.25793 | 2025-06-18 00:58:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 1e1fb7a0-ce54-312c-ab8d-fee76f37402b | -10.9164 | -56.8536 | 2025-06-18 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 7efd421e-ddb6-3a5e-a9c8-38536c829adf | -14.4467 | -48.9063 | 2025-06-18 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| c34db814-84db-32b2-8b10-f3eb0082b576 | -11.1571 | -53.9206 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ecd490ff-cbe0-36b6-bcea-337bf3722fd9 | -11.952 | -58.7376 | 2025-06-18 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| c128bc64-8539-3ffc-93e8-b6873571bd71 | -9.4993 | -56.0988 | 2025-06-18 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 38d6cf85-437d-3b71-9315-f5a9a770371d | -8.7314 | -49.0367 | 2025-06-18 01:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c8f9bfb3-a321-3927-bfa5-88765ca7c5d9 | -14.4273 | -48.9093 | 2025-06-18 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 718e35d4-efd4-31d7-bcdb-74454bae076f | -20.9845 | -47.3955 | 2025-06-18 01:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b654b982-8fae-3b0f-83e6-6fde7adb096c | -11.1379 | -53.9429 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 401.5 |
| 8dd64f64-4e10-3953-9695-e9d4a50aea4f | -21.0051 | -47.3904 | 2025-06-18 01:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 00b39336-6a57-3f5c-a757-90cbb2e4caf2 | -8.7317 | -49.0151 | 2025-06-18 01:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 4ffb4c88-f8c0-3074-a8b3-10933cbd9245 | -5.9028 | -43.4418 | 2025-06-18 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1474d60c-ebbe-37a1-80cd-9c06f21af8c6 | -11.1193 | -53.9241 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a931334e-816a-3baa-a256-0fae3fd028ba | -11.119 | -53.9446 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 45200860-462e-30d8-aff5-1493cca5d581 | -9.4994 | -56.0788 | 2025-06-18 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9e92ab3d-f9f8-3926-82ba-a0b2da957a29 | -10.9167 | -56.8336 | 2025-06-18 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d21c92da-a6a8-32b3-9f3f-54cd354fc032 | -11.1382 | -53.9223 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 218.4 |
| cbbb672e-6108-3cd2-8782-8aff437c3408 | -11.1568 | -53.9411 | 2025-06-18 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 954f0cf0-ade9-31b6-a53a-64917a4fd581 | -6.118 | -42.5323 | 2025-06-18 01:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 690d63c8-a08c-3d5b-9069-5b97c4f3ac7a | -7.54016 | -45.6661 | 2025-06-18 01:00:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 0e465bce-1f8a-3014-a0cf-57a1897b2a5d | -9.85935 | -47.8861 | 2025-06-18 01:00:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 92409299-f63a-3b47-994c-8550ceccee19 | -11.64205 | -54.14833 | 2025-06-18 01:00:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08cfbcf2-333b-32f0-8592-0d22acc9cd21 | -11.13646 | -53.94917 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| af7e9006-d960-3e8a-b406-d754a91bc157 | -10.93423 | -56.84137 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 415355a4-299e-3e0b-9456-5ab9aa4e65df | -11.96426 | -58.74793 | 2025-06-18 01:00:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| c6a57f79-96f6-35c3-b419-5a88aacd4648 | -10.2828 | -60.54171 | 2025-06-18 01:00:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5e6f0053-3ecc-3f95-94de-cdc735d799ee | -10.72427 | -49.56073 | 2025-06-18 01:00:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 6b9829d6-7e0a-3dd0-8e38-8ba0ef46b859 | -11.91644 | -54.82129 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d119408a-0e14-3cb7-8716-4bf72c320e05 | -8.59643 | -48.05685 | 2025-06-18 01:00:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 096422ba-be98-3cd1-a5f3-5891734ef4b5 | -11.08288 | -55.06229 | 2025-06-18 01:00:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6dcc0bad-aa93-3532-898b-74a4fa4a2631 | -10.8623 | -53.76582 | 2025-06-18 01:00:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f5b33700-8ded-3d13-a02f-cb10a484a02a | -11.64979 | -54.13776 | 2025-06-18 01:00:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4a7cdf29-6828-35e1-9100-abe8ab9f4b82 | -11.64079 | -54.139 | 2025-06-18 01:00:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ab57c344-93c4-3eb9-8177-d57868abdca4 | -9.15969 | -49.64603 | 2025-06-18 01:00:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e21c48fd-015e-3871-b7f0-0d957e839be6 | -10.6622 | -49.35638 | 2025-06-18 01:00:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8fbdff6c-e518-3a9b-a82f-3a2079f425a9 | -10.24256 | -52.22219 | 2025-06-18 01:00:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 37e3789e-cc19-3ef6-8a9f-9dee4bfb84f3 | -10.91568 | -56.8375 | 2025-06-18 01:00:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README4.md)
