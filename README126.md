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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ed4aafd-a8a3-36d9-b17b-00ca5e2f204b | -19.81375 | -48.12058 | 2025-09-12 12:38:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 32da0773-ca71-395a-af6a-99c0a55ac533 | -16.96947 | -45.82254 | 2025-09-12 12:38:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 15883390-ef7f-3c4c-b034-914660756d93 | -21.647 | -50.12354 | 2025-09-12 12:38:00 | TERRA_M-T | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| f65630d1-a8e8-3661-b7a3-610105f5e7b8 | -16.27966 | -50.07758 | 2025-09-12 12:38:00 | TERRA_M-T | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| cc7d4340-e6b2-3a46-ba41-4bb50f7c85f4 | -15.12303 | -56.34483 | 2025-09-12 12:38:00 | TERRA_M-T | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fdcb641a-f749-372a-9c85-0d3da6db7bb4 | -14.20802 | -58.60186 | 2025-09-12 12:38:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 439c949e-728c-3af3-ade4-a4c479902f01 | -18.65912 | -47.66734 | 2025-09-12 12:38:00 | TERRA_M-T | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d97d5e9d-a54a-39ec-a60e-7ed18de2e50e | -16.56451 | -49.75986 | 2025-09-12 12:38:00 | TERRA_M-T | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 32799826-822d-3e13-be01-87a4a051f796 | -15.58377 | -54.75605 | 2025-09-12 12:38:00 | TERRA_M-T | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 03278414-a97d-3200-a927-0170f7f2dd0f | -16.27989 | -50.07141 | 2025-09-12 12:38:00 | TERRA_M-T | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 26732f4c-1641-3744-867c-bef5ec1cafef | -18.2539 | -47.19389 | 2025-09-12 12:38:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7c96a6f0-0380-37d2-8475-dfb8aa690a72 | -16.25546 | -46.79934 | 2025-09-12 12:38:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 35.0 |
| c3397fd8-74e1-3e59-ad63-f937440ef4b3 | -17.95982 | -45.27434 | 2025-09-12 12:38:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e2887c39-3928-3497-9f52-202c0752eb08 | -19.05552 | -48.74767 | 2025-09-12 12:38:00 | TERRA_M-T | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 595194ee-4d94-372d-9f9f-1e03313fe23f | -18.02929 | -46.87007 | 2025-09-12 12:38:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d29d7461-86bf-3455-a3ee-20a3d6dd604d | -18.03167 | -46.84879 | 2025-09-12 12:38:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 83b365c2-bf21-3a19-98e9-da7bfd7ea3fa | -14.50257 | -53.90329 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 0bc477c7-9c97-302a-97e7-54b4cfc29768 | -19.8181 | -48.1277 | 2025-09-12 12:38:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0c332cd2-c801-39f2-8607-3bb2ac8ac6f8 | -19.99706 | -46.91863 | 2025-09-12 12:38:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 681ad4a5-d74e-356a-a9e9-bbc48093864f | -16.27839 | -50.08284 | 2025-09-12 12:38:00 | TERRA_M-T | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c35a8d59-ed19-3bbe-b709-e65334a1c186 | -18.25174 | -47.2075 | 2025-09-12 12:38:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4d5de883-d044-3e3c-801d-a70a7d34540f | -21.3544 | -51.19152 | 2025-09-12 12:38:00 | TERRA_M-T | LAVÍNIA | SÃO PAULO | Brasil | 3526506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 9681ec34-ca59-30fe-9149-b3ace03fd06d | -18.91501 | -47.90003 | 2025-09-12 12:38:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7927ae7f-e9cf-3060-8eb8-012ae045e1a4 | -16.56607 | -49.74757 | 2025-09-12 12:38:00 | TERRA_M-T | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 5ce3624d-5188-3318-8dc1-2bbfc5ad78e8 | -15.52773 | -48.53032 | 2025-09-12 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| beea7bb8-d572-3c29-89a0-a43f934e953e | -16.36269 | -51.51044 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| bf3aad34-e1b5-3baa-ba2e-f8122d967c08 | -16.63047 | -49.80011 | 2025-09-12 12:38:00 | TERRA_M-T | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 87f7ea0c-53df-34a8-80c9-212cd6f1409c | -16.96416 | -45.81525 | 2025-09-12 12:38:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 8f61e4dd-a680-3c3b-b100-e03d69b9fedf | -18.78122 | -48.54873 | 2025-09-12 12:38:00 | TERRA_M-T | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 68f5fe3e-b6ed-349e-bfe9-668e5cc8e1b0 | -16.44913 | -49.04543 | 2025-09-12 12:38:00 | TERRA_M-T | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bf3e6b01-3da3-3e54-9365-83e33703a363 | -16.26992 | -50.07018 | 2025-09-12 12:38:00 | TERRA_M-T | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8c569079-8dd0-35f4-9d48-bcea5df1eee0 | -19.34619 | -50.72203 | 2025-09-12 12:38:00 | TERRA_M-T | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 185.1 |
| d815eeca-b70d-32e5-8a9b-16b85914c076 | -17.38422 | -52.97462 | 2025-09-12 12:38:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c67c0904-09b6-3558-9e20-25324c20dfb3 | -17.72163 | -48.63375 | 2025-09-12 12:38:00 | TERRA_M-T | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3f0cdfbf-3712-3b6a-8ddf-8d99c56bc9f8 | -18.87411 | -47.35066 | 2025-09-12 12:38:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 92563898-b02c-34a2-a2a3-096464350fbd | -16.95556 | -45.82086 | 2025-09-12 12:38:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c5438a31-9e81-3817-a7bc-4c4ff4d98b6e | -17.36 | -46.6848 | 2025-09-12 12:38:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e1da6202-05ce-3a4d-9e7c-d2b5da2d0d94 | -15.5761 | -54.74501 | 2025-09-12 12:38:00 | TERRA_M-T | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| eb644669-11f8-3183-a150-043f27102f29 | -19.81168 | -48.13871 | 2025-09-12 12:38:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 30a0c37d-de01-3a72-8d7c-f0cd33532314 | -18.44952 | -49.42078 | 2025-09-12 12:38:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 49f0d697-fc36-3f5b-81af-b4dc44335fdf | -15.23023 | -49.67187 | 2025-09-12 12:38:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 81d15d1b-106e-3b1e-8924-f65b4a798e13 | -14.50395 | -53.89397 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| fe309cd8-011e-30ed-8ef0-620891177a80 | -16.35481 | -51.49935 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fda4244f-c685-3a4f-ad2c-6fd41a472db8 | -15.78313 | -52.24012 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c7cc472e-43b7-3cd5-ba60-6c8154b199b3 | -17.38553 | -52.96534 | 2025-09-12 12:38:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 80fa36a6-60fd-3bf4-827b-8b0de2a9083d | -18.44954 | -47.18177 | 2025-09-12 12:38:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| c05aea7d-5ed9-3aba-819f-5cc0aaaa97a2 | -15.87953 | -48.17435 | 2025-09-12 12:38:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b6fdab72-d90f-3aba-9ad7-9fe6b0e89f71 | -14.21097 | -58.58446 | 2025-09-12 12:38:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a32161f3-2429-38ad-bc10-d9c1e22a9e72 | -15.53875 | -48.53151 | 2025-09-12 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| efb267d9-bb83-3459-a896-3ea937374c66 | -15.23007 | -49.6777 | 2025-09-12 12:38:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 273eab82-86fd-3911-a8d2-098270ce559d | -17.56288 | -48.91271 | 2025-09-12 12:38:00 | TERRA_M-T | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0dfc6ff7-cc56-37e5-8514-f1b00f8611ba | -17.83435 | -52.04815 | 2025-09-12 12:38:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c7b1c949-494a-3993-a456-b84d71eb8493 | -15.22017 | -49.67524 | 2025-09-12 12:38:00 | TERRA_M-T | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 13983d86-6360-3731-baf2-89cd923d28fd | -18.41894 | -49.40287 | 2025-09-12 12:38:00 | TERRA_M-T | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 468e2b8e-5322-31ab-9656-ad8a030619cd | -16.06722 | -49.98309 | 2025-09-12 12:38:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 815eec4e-c75c-3bd3-8d3e-c3df7f4dddf1 | -19.15861 | -50.7562 | 2025-09-12 12:38:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| 294e83c2-fd91-3db4-93cb-bbe02528dded | -15.53697 | -48.54578 | 2025-09-12 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| c923e75a-8f1c-39e6-be3c-c3c939f7e465 | -16.07717 | -49.98466 | 2025-09-12 12:38:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e83a0804-6955-3f91-8e5a-8b6acba7f6c6 | -16.51008 | -55.15509 | 2025-09-12 12:38:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| c060ef9a-ed66-33d3-ac6c-b69c2f38234c | -16.15565 | -43.40281 | 2025-09-12 12:38:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 1ca32bb6-94ec-3136-907b-3c52496a0de2 | -15.79081 | -52.25061 | 2025-09-12 12:38:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 079c3127-97bf-310b-89fe-e77760a0b56a | -16.25769 | -46.77932 | 2025-09-12 12:38:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 267cc33b-1b12-3b7b-aaa2-93606e41645c | -16.36404 | -51.50058 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 10790351-9d04-360b-879e-bc94bb855eef | -15.69354 | -50.58814 | 2025-09-12 12:38:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 977cfa82-ce06-34a0-b0dd-cd98174a3f99 | -19.33477 | -50.73253 | 2025-09-12 12:38:00 | TERRA_M-T | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 967df0f6-687e-329d-a809-69ff5c28d4ff | -15.0654 | -50.15217 | 2025-09-12 12:38:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0059d8fc-2450-3494-8a5f-c36a9ad762c1 | -14.51427 | -53.88612 | 2025-09-12 12:38:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c526e96f-89bb-30db-bd38-ceb8e684b530 | -16.44167 | -49.01722 | 2025-09-12 12:38:00 | TERRA_M-T | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| d7850194-f3fa-3128-b2ab-ca4b030b462c | -15.52597 | -48.54456 | 2025-09-12 12:38:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c033d6c5-bee5-33c7-bc72-2bb78c9d80d4 | -16.36137 | -51.52017 | 2025-09-12 12:38:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4b8380eb-5582-32a2-a1bf-76eaa3a422b9 | -16.80061 | -47.82825 | 2025-09-12 12:38:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 2128f9ec-e34e-3f88-b638-06e32f8c85db | -19.33623 | -50.72076 | 2025-09-12 12:38:00 | TERRA_M-T | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.2 |
| 676875ed-1a24-36b6-bc9b-feaf3f643d50 | -14.82298 | -53.22263 | 2025-09-12 12:38:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0fd0ed28-cc52-3e08-befa-d879618d1869 | -7.5455 | -44.3856 | 2025-09-12 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1a4a235a-1c88-3b92-9ed6-e36d597f7c3c | -14.4588 | -47.3174 | 2025-09-12 12:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 503c6e66-542c-385c-b613-586b9d9ba32a | -11.4285 | -43.5544 | 2025-09-12 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b666469c-a9c4-32d7-be29-5c5719457ca5 | -8.4705 | -47.2712 | 2025-09-12 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f454ac40-8cbb-3ed9-b492-3b7269e288d5 | -8.1837 | -46.0965 | 2025-09-12 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 91d8e3ab-b274-3e18-b2b1-3ee84a6c5b27 | -14.1717 | -46.1815 | 2025-09-12 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 384625e3-dedd-3e2a-9af4-1ca28a9dd8e0 | -7.5452 | -44.4086 | 2025-09-12 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 80e3b44a-e715-3c5d-8730-e32ef6c6c12d | -11.4863 | -49.2658 | 2025-09-12 12:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 51baa82d-27f0-32c8-8bc5-fcbac6e898ef | -11.429 | -43.5307 | 2025-09-12 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 25a53ab4-d977-3565-885d-b107ee3b214d | -6.1703 | -41.0901 | 2025-09-12 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 544.3 |
| c72b706e-30d6-3860-9278-53c74128a6f0 | -12.0852 | -47.5842 | 2025-09-12 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a3882439-2314-38c2-a2ff-be36b102df1e | -10.679 | -48.6633 | 2025-09-12 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 69b5dd82-6cbe-3526-b293-9157d6682183 | -8.9566 | -46.0623 | 2025-09-12 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| af66263e-e06c-36d5-8150-5145f77d3254 | -12.9101 | -54.7558 | 2025-09-12 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 6e271dd9-2368-38b0-a891-55961c9aeb58 | -10.8781 | -45.5826 | 2025-09-12 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| dea155ad-f9ed-3721-9715-ff7ab60d5016 | -7.5832 | -44.3819 | 2025-09-12 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fbf0aaee-5478-3eb2-8064-5f36bc397012 | -10.8785 | -45.5597 | 2025-09-12 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 7b096501-c5bb-3d3c-9468-5b5e0c6be9d5 | -7.5643 | -44.3838 | 2025-09-12 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 958d3ae6-ceb9-3dd1-ab46-6a065b985a6f | -11.4398 | -48.5733 | 2025-09-12 12:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 410.2 |
| 283358a6-4480-3330-82d4-876e03bb545d | -16.293 | -50.0901 | 2025-09-12 12:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 211.2 |
| ec783431-76f2-3447-a622-be11953c5ea3 | -10.0943 | -47.1664 | 2025-09-12 12:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c8d92c99-a407-3598-868f-32423d3ff18b | -11.9713 | -51.164 | 2025-09-12 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 96cf3e47-467b-3475-9d87-a64b0095b916 | -8.9563 | -46.0849 | 2025-09-12 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f57dadfa-90fd-3316-a7c0-b15d08add48c | -12.9292 | -54.7538 | 2025-09-12 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| b633dc75-94f7-324f-b2aa-08555d864ece | -8.4893 | -47.2694 | 2025-09-12 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6a528e94-e3e8-3413-b9a9-e6f44f574747 | -8.8899 | -49.945 | 2025-09-12 12:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4971ec5b-96e9-3330-95bc-f366b9611e36 | -9.77 | -46.0163 | 2025-09-12 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |


[Clique aqui para ver as próximas entradas](README127.md)
