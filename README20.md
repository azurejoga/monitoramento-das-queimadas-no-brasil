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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c95e1e0c-c411-364d-a3d4-932bb54359b0 | -10.46052 | -46.22054 | 2026-08-24 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4e4e06f-d8a3-3d0b-b13d-6ec4f218ec17 | -6.4366 | -52.75878 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 119e8dfd-73c9-38dd-8e02-a8b29d64be12 | -16.14249 | -50.24756 | 2026-08-24 04:27:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a57a0bfa-7809-3156-8ed1-48a70d725b3a | -14.7758 | -48.78152 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1c6c77e-68ff-3543-91c0-3241881ed7e3 | -14.40319 | -51.78267 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5889dd8c-3d2f-3d0a-bbec-a2ed29550bfd | -13.10098 | -43.35044 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bb68ca5-4c3c-38f4-a031-eb34bff19082 | -19.57389 | -42.70609 | 2026-08-24 04:27:00 | NPP-375D | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 526967c9-77a6-3aca-8f31-e81a218d48be | -14.78236 | -48.78756 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01a3cc1b-b2ba-3e99-97b8-b921d90aac0e | -12.86331 | -48.488 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b306e60-d04d-3eed-839b-cd79d8556bbd | -19.01337 | -42.12608 | 2026-08-24 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b454083a-4536-3a24-8a8b-bdbd7d4ba933 | -17.43291 | -48.84486 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3b76e64-fb63-3beb-a61d-272e3f81d9d5 | -14.28419 | -51.78796 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef838a51-ea7c-32ee-bc1f-b293b5b1f4fe | -12.86045 | -48.48241 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 90bac5df-6c37-3c20-9cf6-bfefa5a5f8a8 | -16.40668 | -49.92064 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b797da1f-99f9-367a-9bea-568421ad964c | -12.8918 | -48.4787 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38f8f8b-397f-3ba3-ba13-aafcad86a34b | -13.17087 | -51.39597 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcfb7c21-de36-33e3-872e-48f78df2d8da | -13.89563 | -54.03901 | 2026-08-24 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2b287be-426d-378f-aff1-328a19511f1a | -15.28168 | -52.82058 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f7fd3499-d8a5-3bab-abc9-8291c0e5492a | -16.41437 | -49.92197 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27f5cbef-777b-32d9-bf11-664dc97b5c06 | -12.71818 | -48.40578 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29b5a656-3b4f-358e-8e8e-607e2d54ec89 | -12.86871 | -48.47903 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6ef0f99-12a4-379e-982d-cb14ad7138e6 | -15.28079 | -52.81853 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4b690f20-d4ff-384b-8c9a-ce54ed390e84 | -16.87687 | -49.45877 | 2026-08-24 04:27:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8834771-cad5-3292-a01b-99f4c974d1b5 | -14.37764 | -51.84352 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d53d17d-2685-3dcb-a6f3-bbc8bc342f80 | -11.8511 | -51.6796 | 2026-08-24 04:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eba8f294-800f-3a0f-8673-57355e605527 | -15.78629 | -56.07096 | 2026-08-24 04:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a2854771-d6f3-3e9b-9de1-57e55df95632 | -18.5643 | -44.42662 | 2026-08-24 04:27:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d0384e5-6a8b-3972-8e9d-38af81d66aba | -13.27329 | -51.43914 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7bea7c9-eadf-30f6-bcd0-fe6b6afcb987 | -13.17231 | -51.39825 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3307a58-be04-3d03-bc87-cf75e1d63094 | -12.8934 | -48.46939 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac435bdb-2881-3019-94aa-ca640b61954d | -11.69321 | -54.58923 | 2026-08-24 04:27:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b61f45a-1f92-3087-a9c3-2e14560168b3 | -12.85124 | -48.49117 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f21cfaa-6a7f-39a1-b9bf-bd78cf54d17d | -12.86786 | -48.48394 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b90934-8e4b-341b-8e6f-aa00338a0ca9 | -15.35138 | -52.78773 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf43c14f-d772-32d5-9c78-d9b5969450f7 | -12.087 | -50.59043 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3779cf4b-aa40-31f3-8673-0e2f099764af | -12.89411 | -48.46525 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed932583-7451-302b-9701-124fc2d55f4a | -18.69436 | -47.47304 | 2026-08-24 04:27:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f7bf2e00-3b59-33b8-8be8-42337eb73ad6 | -17.83256 | -44.47349 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2333c1a-45e7-3d4b-9972-ac687332e9a1 | -16.8599 | -49.44611 | 2026-08-24 04:27:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c6f5562-4389-3da9-92dd-0043e06de426 | -19.08132 | -47.13799 | 2026-08-24 04:27:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da9ec461-378f-3ce0-946d-619173ffb93a | -16.04762 | -50.45226 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b5438a3-dc32-373d-a01b-e96dd56bb8bd | -14.33119 | -51.75972 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9066dbe3-0060-37e5-8533-db2a0392322e | -13.68554 | -51.8362 | 2026-08-24 04:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c310a21-e199-34f3-a10f-99fed9dd3d0c | -18.52714 | -47.17342 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e57d9f87-59c2-3dbe-a1c4-7934eb62086b | -15.27032 | -52.87819 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ab4f1b5-8fe1-3516-977c-9da9f4266a82 | -12.11342 | -50.62455 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8ca497a1-9c3a-3e1c-bdc7-8be3e902ba63 | -16.85701 | -49.44069 | 2026-08-24 04:27:00 | NPP-375D | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da8616fd-8b00-327e-87c6-22e00ade14b8 | -13.1789 | -51.40215 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5069c29-577d-3162-ad92-8765fd5a09d9 | -14.80015 | -48.77275 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a9e5e01-c43c-3265-b834-04e38b6d487b | -17.43366 | -48.84056 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed3a8ac0-5609-3a02-bb56-4649071f2bd8 | -12.72413 | -48.39333 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e89aac9-f6a1-3124-bbfc-6f6c4075391a | -15.26705 | -52.84518 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c49b306-d535-3e53-a0c9-dbf4e78a7eed | -15.34785 | -52.78084 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9b8e2aa-5602-3f01-b271-124c624cc437 | -12.74794 | -46.44629 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75318c76-03ee-3e2a-9576-65a433adb70c | -13.09365 | -43.35305 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b716d87e-3191-354a-9268-73fee7e52bee | -13.16199 | -51.39424 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 07cef40c-cfb2-3598-be9d-c59784596018 | -12.10194 | -50.60605 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f24100b2-734b-395a-a01c-749881a8a61a | -16.40998 | -51.83193 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2044346b-a038-39df-9b94-c0174c059367 | -19.15614 | -44.40514 | 2026-08-24 04:27:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51d1e0be-52cf-3eef-9f7b-f6a98ed4da80 | -16.06373 | -50.44775 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a43f640-7251-3487-a3e7-db575f3c06b5 | -16.42063 | -51.84678 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b798498-5c94-3be6-a930-0b2d20eb32d6 | -13.27669 | -51.43272 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4cc488f-e8c3-3ca5-acbb-1f5781371e0d | -14.28301 | -51.78589 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c0c29cd-69d4-3f94-92a3-c073e5eef996 | -18.57965 | -46.9157 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8cd87e5-9325-344a-8172-60072325958c | -17.83538 | -44.47779 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29c97959-7f31-36a6-a62a-ac19c996103c | -16.39778 | -51.82546 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44a205ec-58ff-3dcf-b684-4cd33ca73830 | -15.40827 | -55.78263 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c934a63a-4079-3fdc-a03f-25f6017bce65 | -18.32273 | -47.20299 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cb73a78-7418-329e-a63f-056403dc1455 | -15.2631 | -52.80901 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f68bcac2-6a14-38dd-b0dc-ea60cd6fb0fc | -19.01309 | -42.12799 | 2026-08-24 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1013dcbd-fbb1-317d-8183-e6dc79114faf | -18.08606 | -47.28094 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e1cb1f8-cbcf-36e6-b13c-b59e16bea994 | -16.05565 | -50.42384 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94d5be72-2242-31b9-9509-d321a33d7bb9 | -14.78911 | -48.77066 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf552ec0-3142-30b6-882d-66055a8730c3 | -16.04861 | -50.44695 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9020f31-9d90-3716-ad27-e9ca01751657 | -15.27373 | -52.85586 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f378a4a-727a-3ba3-804e-30f96875b86a | -15.28539 | -52.81997 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0b8b7fc3-c148-35e7-af1e-3b70e59c5846 | -17.92347 | -44.39988 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12de0f23-b35a-37da-b780-0d0e2480e99f | -13.16787 | -51.39737 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d816cb92-b97a-3f3a-8dc1-7c8887010692 | -18.33357 | -43.9117 | 2026-08-24 04:27:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfb58e9e-a52b-356a-aec9-beb5d7250694 | -14.32674 | -51.75883 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3da2ace-6ba1-36ea-9dcc-63332f3c3363 | -19.27846 | -46.67619 | 2026-08-24 04:27:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97e8815b-c02e-3101-82ea-5386660411f2 | -13.09422 | -43.34937 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1397646-fc75-3cd1-adc3-2926aba4ae20 | -17.43009 | -48.83988 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df10d73d-3de4-3bbd-bd08-db86a5a6eb4f | -12.07635 | -50.57566 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f95549a-b350-30b6-afde-0dfb9e34b0a7 | -16.57408 | -51.62793 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5206fd65-774b-392c-b90b-d590fe1cf318 | -14.98398 | -52.67931 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 373ef52a-19be-38cf-9124-a1b65bf960b2 | -15.25967 | -52.85264 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d307898a-ab6c-3cca-950a-eac147e59d58 | -16.40289 | -51.82209 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a474a96-73ef-38ff-abe4-4fd1ff4ec9fe | -19.28208 | -42.35145 | 2026-08-24 04:27:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4cc57a4b-86cf-3778-baf3-e35f1719f63c | -15.44434 | -52.84127 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ad1a42-f3ae-30af-8258-dbc17e8cb1cd | -18.99969 | -44.70561 | 2026-08-24 04:27:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04dc0983-b54b-3a3a-94ea-26826a57e569 | -12.08419 | -50.58139 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb7d4f4e-8913-3bb9-a742-0fade45a0d1f | -17.44005 | -48.84622 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 64ad509a-c857-38b4-9a65-29cb3a8534f3 | -15.28627 | -52.82204 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 32ace241-6e88-3240-b28b-ecf66548e135 | -15.26781 | -52.80986 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 986a3e02-f7ac-391c-873d-00f6c420691f | -16.41284 | -51.84055 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51078b1a-2d61-3ffc-aa00-c7645d8a635c | -14.30019 | -53.21078 | 2026-08-24 04:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88a5ce39-ec2c-306d-b956-e70d1a2fcd56 | -16.02133 | -45.52312 | 2026-08-24 04:27:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 100686bb-f340-3ce5-a373-d853af1d98f4 | -12.88933 | -48.49308 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33b8f456-aecd-3d33-97f4-3b5485415ac7 | -16.41522 | -49.91724 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
