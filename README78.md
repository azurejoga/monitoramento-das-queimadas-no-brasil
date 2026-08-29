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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 724996c2-bd8d-372f-a465-7b436b711508 | -8.3205 | -45.6773 | 2026-08-29 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 78ea863d-4a1e-37c1-b78b-6c7f803f6ec3 | -6.7884 | -55.6635 | 2026-08-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a9ba28c0-19cd-3e4e-a5f7-fa1b0f783545 | -10.8804 | -50.4965 | 2026-08-29 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c8d1c981-50f9-3634-91aa-fad43a0019d7 | -7.5137 | -55.3051 | 2026-08-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| f868feb0-1cb7-382a-875e-addbd0a4697a | -6.7885 | -55.6436 | 2026-08-29 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3b71a9f5-161f-3772-a586-15c01636d18e | -14.2027 | -52.8432 | 2026-08-29 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 295.1 |
| 6047e3a8-314a-34ee-9fbd-03b27f533315 | -13.3061 | -46.9363 | 2026-08-29 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 34f673e6-2d5f-3117-89de-2d2547f215af | -14.1642 | -52.848 | 2026-08-29 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9eaf5744-dee7-33a6-accc-68bab4690ae3 | -10.8235 | -50.5026 | 2026-08-29 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9a31fdd7-f2ee-32ef-8f94-900d769504d1 | -6.6129 | -43.7317 | 2026-08-29 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| b5f2df71-766c-3a87-8724-be5d24e591cb | -12.2093 | -50.5386 | 2026-08-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b84bdc8b-8990-39e2-ad60-ee629fdaed9b | -11.7024 | -47.6352 | 2026-08-29 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 381fe3dc-e7d9-310a-af56-6b865298ef88 | -6.6315 | -43.7533 | 2026-08-29 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 70c94b59-1679-3871-b75c-af6c75dcf260 | -12.9221 | -45.8582 | 2026-08-29 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4dad580c-2bf7-3e13-890f-81b7e77a9934 | -9.621 | -55.1266 | 2026-08-29 13:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 662aaef8-79e4-3a4c-9348-37751f309e66 | -9.9708 | -53.9419 | 2026-08-29 13:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| e4cd9bfa-bc32-38fb-8f77-4167f8715c31 | -14.4057 | -50.0537 | 2026-08-29 13:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 18269535-6cad-31f7-845d-b291a5080b1a | -14.1835 | -52.8456 | 2026-08-29 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 316.1 |
| f165bfd2-3341-34a6-a12f-6ba777e32c32 | -8.5968 | -54.7957 | 2026-08-29 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a7f158e6-77ea-3acb-b558-f5af51e277a7 | -6.7885 | -55.6436 | 2026-08-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 14116e61-1677-3c40-8f4a-f3a59b97b848 | -8.6154 | -54.7945 | 2026-08-29 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| e01d8c91-245d-3855-b50f-d187eadac6ac | -8.5968 | -54.7957 | 2026-08-29 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| e323d110-a998-3107-be8c-9c00a27e2b80 | -7.2993 | -49.9676 | 2026-08-29 13:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1bf9116f-6f05-3111-ac80-073e1202c868 | -14.4193 | -52.5625 | 2026-08-29 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4ff84d4a-336f-33da-b1cb-f95cbea184c4 | -11.2317 | -53.9958 | 2026-08-29 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 66a48c1a-f6e7-3142-b419-8bbe32153da6 | -7.5661 | -61.3239 | 2026-08-29 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fa277a8e-5bb5-31fb-837a-468f1b4cb494 | -15.3849 | -52.6677 | 2026-08-29 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c3efde91-9e08-3231-b6ba-8d769333f0f3 | -12.2093 | -50.5386 | 2026-08-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0041e48c-3363-3bdc-8cfa-9f1581dac249 | -9.9708 | -53.9419 | 2026-08-29 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 228.5 |
| d38b2277-1aef-3994-8d56-852e9e2fd0d4 | -8.9428 | -63.2797 | 2026-08-29 13:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 115.4 |
| ad308929-dce3-35c4-a854-ffd78c794a31 | -8.5966 | -54.8159 | 2026-08-29 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 91eda81f-a794-3773-a3d7-bc2cc609fcbb | -10.8235 | -50.5026 | 2026-08-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 837bc6ed-4a89-3351-8ad6-30067592e1ec | -12.3811 | -48.1877 | 2026-08-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 03428263-24e6-34dc-a3aa-6c27febb033c | -6.6129 | -43.7317 | 2026-08-29 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 258.0 |
| fa2d7245-cd8e-3920-99ce-da586ad27b9d | -11.1639 | -45.5897 | 2026-08-29 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 47200515-76c8-318a-a34a-1dafcb718517 | -14.2027 | -52.8432 | 2026-08-29 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a46527de-4323-3ad6-ad7b-b8f6395872cc | -5.8895 | -57.7513 | 2026-08-29 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2b491c79-e3ba-3602-9a94-8f6058ec1147 | -6.7884 | -55.6635 | 2026-08-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 54f781ea-c566-3642-bd31-79698c044235 | -9.971 | -53.9214 | 2026-08-29 13:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 270.6 |
| bf123507-3e67-3404-895c-6a25b28b7141 | -7.5137 | -55.3051 | 2026-08-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 914e6fb3-d1ab-3be0-9b39-0085d32bde18 | -12.9221 | -45.8582 | 2026-08-29 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 288d4214-9361-3dd0-a502-9f472fb3fe27 | -9.6022 | -55.128 | 2026-08-29 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 3f9bb282-d8be-30ac-9d86-c043e6d056c6 | -7.5662 | -61.3049 | 2026-08-29 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2df33a4a-2686-349e-b633-52742d4078b5 | -8.9613 | -63.279 | 2026-08-29 13:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 58026eba-ded3-3266-9f0a-f337aafee1c8 | -14.1835 | -52.8456 | 2026-08-29 13:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 917c5421-48c2-3078-a85d-354d7a2f02ab | -10.7043 | -48.2226 | 2026-08-29 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f5218d14-f2f3-30ac-89f8-95497e5b30a5 | -9.621 | -55.1266 | 2026-08-29 13:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fa924c5b-3ced-3536-8d2c-f48810c1998b | -6.6317 | -43.73 | 2026-08-29 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 922.7 |
| 06ab266f-e734-3150-8032-a29fae1dd34e | -8.5969 | -54.7755 | 2026-08-29 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 71146ab2-0fbd-383f-96bd-68ba9a8543de | -11.5039 | -46.9471 | 2026-08-29 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d763e8d0-0741-3a8e-9a30-4791bcb49eee | -10.8804 | -50.4965 | 2026-08-29 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d6fa0275-93b1-3aa4-88af-528d16b23503 | -13.3061 | -46.9363 | 2026-08-29 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 793d5735-15a5-3f1d-a55e-19145ed522b9 | -14.419 | -52.5837 | 2026-08-29 13:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 76695dce-b460-3364-aaae-5c811d5fc0fd | -6.77 | -55.6445 | 2026-08-29 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| f5d5ab82-d0a1-35c8-b550-d19e01578d7a | -10.8422 | -50.5219 | 2026-08-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7f27ed5a-4169-3974-83e0-954a6d90db9b | -14.4057 | -50.0537 | 2026-08-29 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0126f416-0b80-3c51-accf-8f355ba3a91d | -8.9428 | -63.2797 | 2026-08-29 13:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 1bf1fead-d6b8-34c6-b160-b6629a9a655a | -9.971 | -53.9214 | 2026-08-29 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 242.4 |
| caaf2846-641a-3751-ba8c-f630a21ceff6 | -9.2282 | -51.5428 | 2026-08-29 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9b0ffc05-151c-3128-8e75-873ce6cf29da | -14.1835 | -52.8456 | 2026-08-29 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 171.8 |
| dc79a8fb-9a71-32ba-91d8-1fd0837353af | -9.621 | -55.1266 | 2026-08-29 13:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 87b8c1bc-1614-33ae-95c5-2d31032a16d2 | -8.3205 | -45.6773 | 2026-08-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ce3e74c2-ce3b-3051-9c02-737b40a52dc9 | -15.3849 | -52.6677 | 2026-08-29 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| bcddea07-bc3c-30f9-b606-c8df2ba99262 | -11.5039 | -46.9471 | 2026-08-29 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b3a13c11-f55c-38f6-b778-6f9026badbe9 | -12.2093 | -50.5386 | 2026-08-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 276419bf-6f21-360e-ae5c-439693d26d0b | -14.4142 | -51.7345 | 2026-08-29 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f2f0a6b0-ae78-305a-a774-4983b5628ef6 | -10.8235 | -50.5026 | 2026-08-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| ed07966d-0a37-3a74-b08c-5e5edd0df6cf | -11.2489 | -45.0732 | 2026-08-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 99b62d08-32a9-3871-9c26-5f349f95da02 | -7.5661 | -61.3239 | 2026-08-29 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 191.5 |
| df93db26-3faf-37e8-b68e-7059654a4ed8 | -10.7791 | -53.9752 | 2026-08-29 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1d63f933-36dd-30de-8c97-dc46f34c0638 | -12.1902 | -50.5409 | 2026-08-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b0efd2dc-2c3c-3a3b-a15b-6fb84f4afe1d | -10.4794 | -64.5012 | 2026-08-29 13:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 469b95f3-0117-3ab4-97d6-5d008077f9d2 | -10.8804 | -50.4965 | 2026-08-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| d8d0c45b-0c7c-3b4a-a28d-a04f4b294286 | -2.7948 | -49.582 | 2026-08-29 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4dddb60e-c67c-3c31-b157-bdcffe9f6a94 | -13.3254 | -46.9333 | 2026-08-29 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ac84c929-8046-36d7-8735-a437488553bf | -9.9896 | -53.9404 | 2026-08-29 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 0beb676b-9453-346f-b23e-6e63f6490e97 | -10.8425 | -50.5005 | 2026-08-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 2283805e-a867-3d5d-84a3-6b3a87b67c33 | -6.6315 | -43.7533 | 2026-08-29 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 322.8 |
| 42ba312b-abfb-3ee7-8a35-aa60ef6b645c | -8.5968 | -54.7957 | 2026-08-29 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ff114447-f3d8-37bf-bb3c-e8aea674e680 | -10.8232 | -50.5239 | 2026-08-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 99f3da19-c053-36e9-8329-0958a9588aae | -6.77 | -55.6445 | 2026-08-29 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 130c3904-e67f-3394-82e5-c0118ecd4460 | -14.2027 | -52.8432 | 2026-08-29 13:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 68b9f53d-6516-3e6c-8159-ffba3452e1b6 | -6.7885 | -55.6436 | 2026-08-29 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 4a9542a8-ba33-3c56-b3e4-009721bad26b | -9.2094 | -51.5444 | 2026-08-29 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fa6e3090-da1b-3495-9a0c-99493f775bfb | -14.419 | -52.5837 | 2026-08-29 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b5f6f888-2a5f-37d7-a02c-643954276d95 | -11.269 | -54.0334 | 2026-08-29 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5d58a0e4-3ef3-3792-ad33-99868acbcda8 | -5.8895 | -57.7513 | 2026-08-29 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b157753f-2974-37b9-bb12-f7c093d49002 | -6.6129 | -43.7317 | 2026-08-29 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 337.3 |
| 4ab32bc3-c1e0-39a2-8e05-793fa47607cb | -5.1426 | -49.9324 | 2026-08-29 13:50:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| d1f9ca4c-987b-3c98-b206-b3e8478bc512 | -9.9708 | -53.9419 | 2026-08-29 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 6cd3db59-c38b-324b-8016-ed7641b5c1c3 | -12.9221 | -45.8582 | 2026-08-29 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ebcff040-7f89-335d-b6c9-312330edc873 | -14.4 | -52.565 | 2026-08-29 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 519645e1-9413-381e-a428-444c7814979a | -14.4193 | -52.5625 | 2026-08-29 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 646cd0c0-fd6b-3d27-b3d0-bfb03eb471be | -7.5662 | -61.3049 | 2026-08-29 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |
| d926ab89-4589-3607-9102-309fb00e0e5b | -10.8215 | -50.6519 | 2026-08-29 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 142f5af1-521f-3761-b0f0-603be963cdd1 | -11.7024 | -47.6352 | 2026-08-29 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 28e9e111-1ce8-30e6-a930-a0f12e06c5fa | -11.7028 | -47.6129 | 2026-08-29 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 03513e62-e0c3-3af5-8e8c-adc7b852838b | -8.9613 | -63.279 | 2026-08-29 13:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 119.9 |
| fb308940-bf23-3813-af76-7803100f5588 | -10.8425 | -50.5005 | 2026-08-29 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9e879c13-c29f-3240-9b71-1c3878112ac9 | -7.9838 | -45.5072 | 2026-08-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |


[Clique aqui para ver as próximas entradas](README79.md)
