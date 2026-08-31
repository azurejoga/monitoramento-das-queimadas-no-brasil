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
| e2c7a7b3-c673-3c49-8cbb-d622d69e7725 | -8.2564 | -62.75257 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| badfcb56-923b-38b2-9f83-77f2a2f3b0ff | -7.52907 | -55.3307 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69895d6e-164f-33b4-9759-b56a789e680d | -9.01151 | -60.60254 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be0a4739-89f1-3595-9983-6a4892a3b8d4 | -9.17645 | -59.63671 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8ed433b-54a8-3244-a7e5-bb07b565f34a | -7.57269 | -61.35746 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19eec548-afcc-3ad0-ab2f-1b2807db47da | -7.5849 | -61.3451 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 124a4a3a-d92c-3cf4-8312-7a714bb549bc | -6.88851 | -59.45099 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef2a26da-3e94-373d-9d7b-592c8618254f | -7.31025 | -60.57713 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 387653f7-6030-32b6-8257-4df67ba2f5eb | -8.14495 | -63.9992 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df5af39-6c80-306a-94c1-67858788dc18 | -7.06826 | -59.70861 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5918f660-10c5-3545-83d1-a58a007e9049 | -7.5243 | -55.33404 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8ea57f6-dd4b-30eb-8923-cc314cd30989 | -7.3097 | -60.58061 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 96f7d44b-717d-36f1-8955-f4bd9eacd086 | -9.18937 | -51.54938 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f841c493-6016-39e6-9811-e24457139a03 | -7.52598 | -55.32258 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a35bf4de-8f64-35b0-b898-ff3b5ae2f047 | -6.77352 | -59.47393 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8842ab43-6b73-3a59-ae9b-d253799f704a | -9.15891 | -59.54714 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22de4ab0-57b8-339b-9e63-98ba7ecefda6 | -7.34793 | -60.59736 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5d06203-c389-38f1-afd9-3a86beacf14a | -9.1538 | -59.53497 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7abc579f-b084-3f3f-b359-38762cbc1ce9 | -6.90426 | -59.48284 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91ab8d04-6864-333b-a0ce-92ea1518166d | -6.86381 | -59.47651 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2588cd9b-5521-349c-bcb4-6920cd4b0899 | -6.86829 | -59.46989 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55c8bf03-b079-3316-84c8-403098dfce7d | -7.62115 | -55.29212 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7a91c2d-1596-306f-bf97-0884fe206294 | -7.58767 | -61.34912 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87f7b3a3-fc27-3d11-ae46-1a9a325756b1 | -7.39831 | -60.58039 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e37ec83e-0498-3942-84df-a23bcba13add | -7.69597 | -63.3229 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c2f7f6-2467-3620-9c25-98d82d7e4134 | -6.90594 | -59.49411 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 677c3069-f279-3d9a-8e0c-ebdff9c5d83a | -7.29619 | -60.58577 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f81b20-9f9d-3495-8c46-eee690cc1986 | -7.52164 | -61.37791 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cddc5b0f-b523-31b8-aba9-8cfe253bc509 | -7.33741 | -60.59926 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbbff2f-fa6c-3cb8-bfa8-776694a5ce7b | -9.17931 | -59.61832 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfd2a27c-c3c0-3347-87a5-34eb2b0fca71 | -7.6212 | -57.61969 | 2026-08-31 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 303f872e-1a9a-38a1-8d99-5205be5d7898 | -7.79306 | -61.5826 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a332e365-627f-32e8-bfe0-89960c84de4c | -7.31247 | -60.58461 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32f8e463-b15c-3a38-a3c8-7f3731069bf1 | -9.00873 | -60.59849 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b1a164-fb69-33f6-9de1-b80350df19b3 | -7.43579 | -61.42873 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| befc1275-5505-3424-aed9-5362cd617868 | -7.53214 | -55.33893 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a76dca5-ad6f-3237-8aae-21e483bcfd76 | -7.30805 | -60.59105 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ef72d2-6df6-3877-94fd-501b8bd47097 | -7.52725 | -61.32153 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98cb6371-b636-3362-b6bd-35576310f13b | -7.61274 | -55.29079 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9bf48a7-0c45-3384-8a7c-0dc9c479401d | -9.1709 | -56.98754 | 2026-08-31 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae3da8a5-27b0-3e03-8119-1d0f62856fc7 | -7.9215 | -61.33435 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09438c3c-717d-3055-bfb5-f9c37075b6bf | -8.25921 | -62.75684 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5090e8bb-6a8b-3dcc-ac92-2ddc1df17520 | -8.62073 | -54.69612 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf6fb4f-3e6c-3e55-b121-661fd2938651 | -15.23744 | -56.38864 | 2026-08-31 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9471c415-1df1-3bff-ad06-c02b682acc07 | -15.03202 | -48.1676 | 2026-08-31 05:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d6bdfff-022d-3664-b2e9-aa4e55c01a1d | -13.46832 | -57.03813 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 625d9aab-0b72-3bad-b2f5-3b80da3be901 | -15.63888 | -56.38833 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 155d2313-a96d-3319-83ef-22630b1073d3 | -15.67861 | -56.27945 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ea74e48-449c-320d-ada3-026c3d1ada4d | -15.23494 | -53.87211 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba5f2dd5-7669-3f4d-b895-2fb108bcfce0 | -14.60811 | -54.10344 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a5ad2589-f917-3243-9997-34ffbda35a0b | -14.39574 | -52.55091 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09eed67c-72fa-3cc1-b17f-46a338ef75a4 | -14.22105 | -52.84681 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3119d22-b6ef-333b-9f87-3bb202c3733e | -14.23707 | -52.85204 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcb2c22e-4d8e-31af-bba8-a84f9b93b51e | -20.25412 | -58.15327 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.0 |
| ef5fa1da-7db3-33e6-ba84-642aef6135ba | -15.87562 | -56.48626 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dd387a6-aa51-3bd1-a9d6-df3047d5a718 | -13.47855 | -57.05454 | 2026-08-31 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b046224-a03d-3631-80db-b510e1fb7269 | -15.91773 | -56.22145 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b01ae82a-45ea-3b80-92e1-0fbf5534db1e | -15.23779 | -56.38626 | 2026-08-31 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d21d5f57-e8bd-3bac-b72b-c2d0d53379b3 | -14.68776 | -54.91227 | 2026-08-31 05:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52acef03-284a-3c58-9d1b-017a52f7431c | -15.68032 | -56.27777 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ead86de1-2eb7-3420-953b-3d6aeb7bb043 | -14.30378 | -52.90739 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5228ca3a-d8b9-3f9a-873c-db672cd92122 | -14.58002 | -54.1238 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be42f504-cc90-300a-a398-607c4a24edd4 | -14.14291 | -52.80202 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ddccb6c-2e3f-377f-b163-cba03df85962 | -14.42319 | -56.27292 | 2026-08-31 05:38:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a33d555-6fa6-37b7-a02a-59c067c73bf7 | -14.43244 | -52.52845 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6db5f6ba-de4a-311a-8f43-71e95af289ea | -14.29837 | -52.89512 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 280eca30-925a-3531-8c7a-920b18752d16 | -15.68091 | -56.27335 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7053576-d415-37b8-9746-0d41c4f612c4 | -14.58856 | -54.09531 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25010554-f459-3144-aa50-291c7397e1d8 | -14.58219 | -54.10571 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf1dda20-72f8-3319-bd80-7b0019d76454 | -14.1834 | -52.88014 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26b09a3b-d5ab-349c-8476-fdd5e49d0772 | -14.57642 | -54.11111 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d972db74-1db4-314c-9592-2c7cd8d698af | -14.17827 | -52.88148 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ab59946-2d61-353b-b119-bc0977583da1 | -14.1307 | -52.81127 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98469a32-8216-3d3f-9e57-2d6af2269630 | -14.22143 | -52.84358 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 847adef3-d064-306e-bab6-8c1c6e0a5a65 | -15.61302 | -56.41553 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09a6dd33-0b8a-3273-a61a-2cdf46ba30d9 | -13.96687 | -54.40589 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e0d6e97-ffc0-3912-bed3-e7f2a2c1e870 | -19.12741 | -57.41346 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 58b394b9-31bc-3a8c-908b-29228c2b4023 | -15.24052 | -53.86951 | 2026-08-31 05:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6446965-4a53-356f-a2d2-8506da538c29 | -15.67649 | -56.2727 | 2026-08-31 05:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 689b28d7-b77a-373d-85b8-df04ce5e37ac | -15.62685 | -50.09466 | 2026-08-31 05:38:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1222c177-2c93-3dcb-b81b-17ed1af56f54 | -14.2975 | -52.90216 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82962b6e-cd8c-35f6-b19f-dd92666a855f | -14.21677 | -52.83595 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ca84dc-90da-38af-a33f-3215b9df3046 | -14.68365 | -54.90644 | 2026-08-31 05:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8894602-b3f4-39a9-9093-2b1c39fa3fd1 | -14.43892 | -52.52179 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03d230f5-74c2-3d60-bc07-c74abe4aeb7e | -15.63123 | -50.10039 | 2026-08-31 05:38:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49494e79-8260-3e13-8637-cd899994894b | -20.25708 | -58.15421 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 3a96d615-028e-3829-84d7-7b2469dee01d | -13.97176 | -54.4066 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff6f0cab-b366-338c-983e-29b71aa02d5b | -14.12568 | -52.80683 | 2026-08-31 05:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0d52e93d-eec9-392f-a2c9-491f9fbd9342 | -20.25315 | -58.16126 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| fd4a2718-bbd2-3040-a897-644838fb4a8b | -14.39618 | -52.54721 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40d95706-1aee-3ded-b6bc-cd441fe65068 | -14.57743 | -54.11055 | 2026-08-31 05:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d935466-24e6-364f-8864-be237ea41890 | -14.39708 | -52.53953 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cdb940ec-cdd1-3a72-adb0-e8f6fa4604a0 | -14.29794 | -52.89864 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c5d918-08bd-3583-91c8-54d9bfa665c4 | -19.07623 | -57.40202 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d4c2962-7b15-34f1-99aa-85ff248b9206 | -14.46923 | -53.35543 | 2026-08-31 05:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00d9878d-eed7-34fb-ba1a-739f670eed40 | -15.9127 | -56.22543 | 2026-08-31 05:38:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f6ca3431-3090-3908-9e34-8dbe5c0ea08c | -15.23308 | -56.38799 | 2026-08-31 05:38:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 810466b8-528c-309b-a176-75f38632e5f4 | -14.39393 | -52.56638 | 2026-08-31 05:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d7d3a4d-ed62-3ed8-84c5-74ed10bde141 | -14.46395 | -53.35453 | 2026-08-31 05:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac93cce-af3a-3b9f-afdb-466fb5221542 | -19.1231 | -57.41286 | 2026-08-31 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |


[Clique aqui para ver as próximas entradas](README69.md)
