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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c409b6b-61a7-39ae-a013-706c2b8f82a8 | -3.7316 | -40.7092 | 2024-10-13 00:45:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 940f1ea8-c35b-37c0-a7f1-469194f08f7f | -3.6066 | -54.1325 | 2024-10-13 00:45:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ad0fe125-4d7a-3f34-873b-691dff5a725d | -3.625 | -54.132 | 2024-10-13 00:45:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 793bf1cc-ffb7-3656-ba94-752b38482c9f | -4.1148 | -48.2515 | 2024-10-13 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 32919dff-c43f-3af1-88c0-872d970791fb | -4.1149 | -48.2299 | 2024-10-13 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 7b35264d-6b74-3857-bc66-fe332bc60342 | -4.1334 | -48.2291 | 2024-10-13 00:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 56ed06fd-5cec-32df-aa89-d701cea43683 | -4.4026 | -49.7563 | 2024-10-13 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 0b31e74b-258f-3894-a721-fc815476136b | -4.7006 | -60.7507 | 2024-10-13 00:45:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1a07033d-0672-3529-9668-2bc6a3367d70 | -5.0713 | -46.8499 | 2024-10-13 00:45:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 05f40577-e841-3320-9e21-ba3cee8c9b0c | -5.1381 | -45.3969 | 2024-10-13 00:45:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1bfc4cf0-cc3b-3ffb-b5bf-e7fdf68313bd | -6.1299 | -47.2884 | 2024-10-13 00:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 339e6ebe-1496-376d-882f-32d3d116dc73 | -6.1301 | -47.2664 | 2024-10-13 00:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4d0c0f38-3226-309f-bb27-2d2973825267 | -6.1487 | -47.2651 | 2024-10-13 00:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0ce33967-772b-3fb7-a5a8-acd06a6081d6 | -6.6925 | -62.8493 | 2024-10-13 00:45:45 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| da71fe09-d42f-3296-a051-28732520bf2c | -7.3823 | -47.2586 | 2024-10-13 00:45:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a866c625-fc78-3f9a-b4c4-318d0f0cd0ea | -7.3657 | -64.6656 | 2024-10-13 00:45:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f13c22bf-ba9f-30cf-9df2-93de09f75809 | -7.3841 | -64.665 | 2024-10-13 00:45:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| b7aee084-b06e-3ce7-8908-bfa88638ee43 | -7.3842 | -64.6464 | 2024-10-13 00:45:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 1b387dfa-e653-3323-a283-2be9e0860f8f | -7.6627 | -47.3229 | 2024-10-13 00:45:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1942e43e-fcb9-3cbd-939d-40b93b5728a3 | -7.6629 | -47.3009 | 2024-10-13 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 71c850da-5bd2-310c-9b1d-797056dd4ab2 | -7.6815 | -47.3213 | 2024-10-13 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 475aca5b-00a1-3865-82b9-da31a0cda9af | -7.6817 | -47.2992 | 2024-10-13 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 875985bb-7414-33b6-a39f-078f51f42ffa | -8.0675 | -44.8158 | 2024-10-13 00:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ba92c337-40be-30a0-8e2a-060f256675af | -8.2352 | -64.0961 | 2024-10-13 00:45:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 36a48f63-f9ce-3878-b7f9-4c1a7a4f1bfd | -8.2352 | -64.0773 | 2024-10-13 00:45:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| de3a1b41-4ee7-34ca-b9b7-a949da75d48d | -8.7045 | -46.6042 | 2024-10-13 00:45:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b06dc35e-5a66-381f-8d2a-69713949a371 | -9.7359 | -64.2295 | 2024-10-13 00:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 586abfb4-07c9-303a-aa7b-94c63aff97b3 | -10.9311 | -44.6789 | 2024-10-13 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 61169fa3-1653-382a-9800-31860df52c2c | -10.9315 | -44.6557 | 2024-10-13 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b448091b-0da0-3bd0-8276-ae30e6de720f | -10.9502 | -44.6762 | 2024-10-13 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 316e8f05-eea3-3e2e-8772-194bdf30cec8 | -10.9506 | -44.653 | 2024-10-13 00:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2f790526-18e0-33d3-97f9-c58768f3d9a2 | -10.8567 | -63.9177 | 2024-10-13 00:46:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| e8d48012-2c94-3774-b006-e323c4f156ee | -11.2535 | -50.9036 | 2024-10-13 00:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 25a285f1-0ee3-33b2-9ad6-d3dc4eeed8da | -11.2722 | -50.9228 | 2024-10-13 00:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 14362c2c-2a80-3efd-9d99-f2d0516db463 | -11.2725 | -50.9016 | 2024-10-13 00:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 41fad1f3-7d95-367b-b95a-0f542c02239f | -11.6334 | -48.3736 | 2024-10-13 00:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e6fde4f6-8944-3955-89fc-da287ce58868 | -11.7479 | -48.3591 | 2024-10-13 00:46:13 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d4454d3d-14ea-3077-b461-33912183ddb0 | -11.712 | -64.9777 | 2024-10-13 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d171c44c-eea7-36ec-baa7-1ff52e2917fa | -11.7308 | -64.9769 | 2024-10-13 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 56e4e7cf-20d6-354c-89b9-7009103ffd70 | -11.7309 | -64.9579 | 2024-10-13 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 746959ff-acd4-3709-825a-3f414604fc50 | -12.2754 | -47.6473 | 2024-10-13 00:46:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 837435d3-84e3-3554-8cf9-00bfac768773 | -12.3067 | -59.1641 | 2024-10-13 00:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| add2a886-8afa-3ef3-8482-1a3860465c22 | -12.3793 | -63.7294 | 2024-10-13 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5d65a1b1-7dff-3b71-8187-ee3284a525b0 | -12.398 | -63.7475 | 2024-10-13 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2a38e662-dd8c-304d-9b51-b47bd7d7b893 | -12.3982 | -63.7284 | 2024-10-13 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 143.9 |
| cb442bd1-06c0-3fa7-8e4c-dd871f2b4643 | -12.9182 | -62.5287 | 2024-10-13 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.0 |
| faea3327-7255-383f-acf4-a27ff7a33798 | -12.9372 | -62.5275 | 2024-10-13 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 97b6a671-6240-3dcd-b67c-f71b059f7193 | -13.1475 | -62.3215 | 2024-10-13 00:46:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 72062f00-d176-3a5c-914d-4e8081945e5d | -13.7346 | -60.6079 | 2024-10-13 00:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 17ff5f8e-8b16-3727-a54a-236d32354be2 | -13.7348 | -60.5883 | 2024-10-13 00:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 95f3f093-1b76-3e53-8482-8e2e615a4450 | -14.7638 | -57.799 | 2024-10-13 00:46:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c02098ed-7ee9-3bb0-95bf-25729f50ee73 | -14.7831 | -57.7971 | 2024-10-13 00:46:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 532c84ec-343c-3bbc-8194-508711aecd14 | -15.6419 | -59.9767 | 2024-10-13 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 360d784f-c66e-3404-a7d4-369f3a4d8296 | -15.6421 | -59.9568 | 2024-10-13 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3a3e9226-485e-30cd-8491-d43dcf91100c | -15.6612 | -59.975 | 2024-10-13 00:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6df089de-a785-3b5d-926a-e6d35fc45754 | -16.9998 | -57.4586 | 2024-10-13 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 8bce9556-bab1-3f3b-87e0-ecfabb6d003d | -17.0001 | -57.4381 | 2024-10-13 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| b43303ef-932c-3535-af22-18883afc43de | -17.1758 | -57.479 | 2024-10-13 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.1 |
| e119974b-893b-3d35-bed5-a163c811a2ed | -17.1761 | -57.4585 | 2024-10-13 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 190.0 |
| fd662ddb-56d8-34bd-910d-9348f058f081 | -17.1764 | -57.438 | 2024-10-13 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 4a9ffe25-9c68-3570-ae3f-835eb8251c5f | -17.1954 | -57.4767 | 2024-10-13 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 7d09004f-e1ef-3b7d-8c72-2faff8b9c1f5 | -17.1957 | -57.4562 | 2024-10-13 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.2 |
| 5f5fcf72-0201-31b8-b5c2-97a868247725 | -17.964 | -57.3843 | 2024-10-13 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| f2aba931-fa52-3abb-8e93-4b5437380518 | -17.9643 | -57.3637 | 2024-10-13 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.2 |
| 55144a52-0dea-3f35-af70-e72cf470743b | -17.9837 | -57.3819 | 2024-10-13 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 7c9eda40-74df-3427-96ab-49154f9b33ca | -17.9841 | -57.3612 | 2024-10-13 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 29bb6058-0932-34aa-a606-cbfb4131d110 | -18.1953 | -56.5691 | 2024-10-13 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| c13e3ce4-6772-38e1-a83e-7ac668813b08 | -18.2147 | -56.5873 | 2024-10-13 00:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.9 |
| ce65ebbd-51ab-3de2-ab7e-c4e3a481f47d | -18.2151 | -56.5665 | 2024-10-13 00:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 233.3 |
| 9f5fa37e-1f68-312c-a73d-19d45a37dba1 | -18.2155 | -56.5457 | 2024-10-13 00:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 89bc00f3-934c-316d-89ee-ed6bda654db5 | -20.9426 | -45.995602 | 2024-10-13 00:54:59 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b599cd43-c76b-3e1e-b3a5-2bbef41c4036 | -20.9443 | -46.0033 | 2024-10-13 00:54:59 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed44084-fbec-3c9e-a257-4e9a653c51f9 | -1.9486 | -56.4692 | 2024-10-13 00:55:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7d16ef5f-a7cf-3763-bcd9-6ff8e88c8a08 | -1.9486 | -56.4496 | 2024-10-13 00:55:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e72c4373-dca5-3672-aaf1-3452c2e50c6d | -2.1693 | -48.8108 | 2024-10-13 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 7f9a26b9-0ec8-357d-8478-80d5efcaca09 | -3.0731 | -54.2473 | 2024-10-13 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b1cdca26-49d9-3707-bca3-e3fb7d100851 | -3.0773 | -53.036 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 05d99cee-307a-3394-85d5-088b9c94197f | -3.0915 | -54.2469 | 2024-10-13 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 32e80ec2-40b6-30f2-b151-84efaf088b8d | -3.0956 | -53.0559 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| a2168012-b0cc-3ad9-b251-7daae3531b66 | -3.0957 | -53.0355 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 230.5 |
| 1dd1ac8f-ba2d-33e8-a7ac-0a20cd6032fc | -3.0957 | -53.0152 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| dee314f9-f6d9-33c4-9f12-fc36f94c5ec0 | -3.114 | -53.0554 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 3bf5e16c-bc2a-37fd-95a6-4b8e33d02753 | -3.1141 | -53.0351 | 2024-10-13 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 3aa0e321-6143-3925-bad1-416963b9f668 | -3.1791 | -50.476 | 2024-10-13 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 127c61f9-8c5b-3686-96f8-664ffc5f7df3 | -3.1792 | -50.4551 | 2024-10-13 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| d98b8b73-bb33-3a81-848c-a938aec08246 | -3.7127 | -40.7346 | 2024-10-13 00:55:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 57.5 |
| ba21a6c5-6e3a-3c62-b774-d27f0f335f17 | -3.7128 | -40.7102 | 2024-10-13 00:55:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 3e4000b8-269f-396a-adb2-4bb2ecccc926 | -4.1148 | -48.2515 | 2024-10-13 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 8bd04f4a-9d91-3b84-b73f-450f7d797d62 | -4.1149 | -48.2299 | 2024-10-13 00:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 0ad0f624-55a7-3fcc-87e0-f682eeb0c3d8 | -4.4026 | -49.7563 | 2024-10-13 00:55:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ca41f415-ec11-3790-b92d-9e328615ae64 | -5.0713 | -46.8499 | 2024-10-13 00:55:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| aeca07a4-2395-35e6-9a10-ca77cebf0d90 | -5.1381 | -45.3969 | 2024-10-13 00:55:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| cdb89715-533c-3ba2-9297-d0cec9efe9f6 | -6.1299 | -47.2884 | 2024-10-13 00:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 9b7639e7-c6ad-347b-bbe0-ebfdeb0103af | -6.1301 | -47.2664 | 2024-10-13 00:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| bccbc798-c5f6-3ae3-9bc0-905df491b231 | -6.1487 | -47.2651 | 2024-10-13 00:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 66ee434a-d456-3248-b495-4bea57872f9d | -7.3823 | -47.2586 | 2024-10-13 00:55:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a97fecaa-1275-39c5-a7f1-f2e83b8b0e1e | -7.3657 | -64.6656 | 2024-10-13 00:55:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| ef104501-325b-39cb-9dc9-f59318e4da2f | -7.3841 | -64.665 | 2024-10-13 00:55:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| fd98000d-56ef-3190-be9e-b2f9ed879d83 | -8.2352 | -64.0961 | 2024-10-13 00:55:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 26fb1955-1633-38b9-a160-b4071ea09771 | -8.7045 | -46.6042 | 2024-10-13 00:55:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |


[Clique aqui para ver as próximas entradas](README12.md)
