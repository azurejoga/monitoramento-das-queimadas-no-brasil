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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8810b314-95e1-3384-9ce2-9211983cd774 | -19.54337 | -56.71822 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4e05ac00-fbef-3982-a70b-ef4789bc45d1 | -19.54092 | -56.71127 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| e4e25b35-6c1a-3f2a-8f75-575afd7e4d86 | -19.53941 | -56.71753 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.5 |
| fd2615bc-fd3d-31e1-b49f-aa512b7c2600 | -19.5382 | -56.71021 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| cfe9f7a8-b410-30c9-b22a-977903e4c148 | -19.53673 | -56.71648 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 14da3d24-9e40-30b4-b788-270b7b3b9789 | -19.53428 | -56.70955 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| fdf8074d-5bb2-3966-acb5-8b752e6956c7 | -19.53276 | -56.71581 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 54ab7ee4-de09-3d88-af87-309ea7d6427c | -19.53156 | -56.70845 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 0302768e-89c1-3762-9606-5e9c9507deec | -19.53009 | -56.71473 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 8c2fe901-4be1-39fb-a296-84a16fc83b9f | -19.52763 | -56.70783 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| ad851403-ee08-3f96-ad6a-109503b16e9a | -19.52612 | -56.71408 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 0d3fa222-9bca-3285-a853-d7d03a6772bd | -19.52492 | -56.70671 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 42d1e3d9-c72d-33cb-8913-4c77e644716b | -19.52345 | -56.71298 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b6e38490-60c2-3749-a207-40dc92e26b53 | -19.51435 | -56.70438 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 4e0712c3-8b85-37b0-a394-f62805ad543d | -19.51313 | -56.69696 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 51e490ec-c7b8-3140-a4e8-623e07852aa3 | -19.51165 | -56.7032 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| e1f31e3e-1fe0-3ee0-84dd-c4fa2eaeddbf | -19.51074 | -56.69018 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dad31146-faf8-37ce-833d-d4cc92d96c52 | -19.5102 | -56.59052 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8209fefe-149f-345a-889a-fb9b38aac7ee | -19.51017 | -56.70948 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| c80bb148-6641-33ca-8b75-6d976f51c256 | -19.50922 | -56.69642 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| d0d2330d-025a-3e6b-ac6c-01e44d219e02 | -19.50874 | -56.59669 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| d8b155fe-e09d-3ea1-80a2-d1c967231882 | -19.50797 | -56.68893 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 292d1e44-565d-312c-8093-815a0e86ac54 | -19.50771 | -56.70266 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| e12f9060-3363-3f36-a623-0e67b89f50f0 | -19.50653 | -56.57648 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e7a4c71b-e6b1-34e5-ab97-f1099d77d644 | -19.5065 | -56.69518 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d121361d-268f-3e65-8845-d51813309f7d | -19.50619 | -56.70892 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 699f735d-9b2a-3aba-9378-4844d7f1754a | -19.50506 | -56.58266 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 63d0ed98-ac8b-3678-9b24-4bef2491b2f8 | -19.50502 | -56.70144 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 2e07b4fb-3f35-3b31-a5c5-53ae74e0f1e5 | -19.5041 | -56.68847 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8c4b207a-dd87-3454-9d65-dcd834b60ed4 | -19.50359 | -56.58883 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 11c6973a-d72a-31bd-836c-0b6f010b2d80 | -19.50353 | -56.70772 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 2123aa44-8ba3-383a-94b3-d658c546abc2 | -19.50259 | -56.69469 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 1891bef5-2af1-362b-b680-34c118c57759 | -19.50213 | -56.59497 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| e2c18f3c-bc56-3d34-99b8-7bf8b8bea182 | -19.50139 | -56.5686 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f85728a8-8f0a-3d85-a40a-19c1000c3ade | -19.50106 | -56.70094 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 8948c83c-9f0f-3905-8127-979da9cdaf53 | -19.50067 | -56.60112 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| a6a1a78a-a6b4-3552-8533-04809eb040ca | -19.49993 | -56.57477 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ac3223ec-23ff-3640-98bd-cc0d1208a03c | -19.49954 | -56.70718 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| f6a79562-7577-31e7-aff1-119765cf773a | -19.49846 | -56.58094 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 85a04743-1f70-302d-bef1-b010143e566c | -19.49689 | -56.70597 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6b97c5f0-596d-3d1d-a320-e86b6985f6c7 | -19.5419 | -56.72451 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d7e78ae5-b4ac-3df9-907a-b56aaebf366d | -19.5379 | -56.72379 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.5 |
| b142ca3a-4fa9-3daf-a811-c4d60e968331 | -19.53639 | -56.73006 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 60cf927a-c981-393b-8596-895b0ba937a7 | -19.53525 | -56.72277 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 7771ea09-b5c1-3e63-85ca-9b00633b6021 | -19.53377 | -56.72906 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| cddff760-db26-3c92-a65e-6f5327b03a26 | -19.53125 | -56.72209 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| b49967e2-912a-3e11-9da0-0472581b6a5d | -19.52861 | -56.72103 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 44936b81-ca45-3cce-916f-3ad489e275d7 | -19.5246 | -56.72035 | 2024-10-31 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 7438a306-11d8-38af-ace9-b00470e7fdcb | -19.60499 | -56.74943 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.7 |
| 5d60b8d1-8202-36a1-bb3a-852dde421860 | -19.60446 | -56.72266 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1ec17dd9-296a-348b-ba44-48ec963b6cc4 | -19.60347 | -56.7557 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.8 |
| 3842080b-003f-3926-ad55-01977ba8c6e5 | -19.60293 | -56.72892 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| d149275c-e70c-3cc0-b4e5-5fa199c6284e | -19.60285 | -56.74742 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 4d150ea8-14bc-30c0-88ec-d48cddfecf54 | -19.60217 | -56.72057 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 1f7e23ba-5543-3f5d-ad11-edf4f92ecbfc | -19.60194 | -56.76196 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.8 |
| 21fb6f0a-626a-335c-a039-c548d466cc47 | -19.60141 | -56.73518 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 43fd9e40-0761-37c9-b7c4-b2ba4ffb62b2 | -19.60136 | -56.75369 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.1 |
| 7f7fbe04-acda-3a5e-a42e-cff0a5ab26a4 | -19.60068 | -56.72684 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 63cfaf66-57f8-3716-ace0-2e8e0b7dc5a7 | -19.59988 | -56.74144 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.7 |
| f16eb9dc-cedf-3ea7-a8c9-7e26ef231df1 | -19.59987 | -56.75998 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| e09b2bf3-f84d-3a27-9282-f78360e42cfd | -19.59919 | -56.7331 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| ff84d31f-f627-34e9-b5fc-f92ae07c2d4e | -19.59838 | -56.76626 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| d821b33b-1f4a-395f-b25e-c1cbef7d8bfa | -19.59835 | -56.7477 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 181.7 |
| e82e6e83-a7b3-37a9-8e60-83ecbc123ef1 | -19.5977 | -56.73938 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 905dd423-8c2d-38d1-ade1-6ff5556abca8 | -19.59682 | -56.75397 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.8 |
| 32a44f18-c128-39c3-965e-8a25d59ac0c5 | -19.59621 | -56.74566 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 82f3d344-bab2-32e7-9b52-478eefb1a147 | -19.59529 | -56.76023 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.8 |
| fc06dcd4-3064-3cb3-a935-b60a3cd15971 | -19.59472 | -56.75194 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 646d2813-9d26-3036-a674-2829a4f0cc73 | -19.59404 | -56.72511 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 86e9ab70-68c3-39fe-b182-8a48447a7180 | -19.59376 | -56.76651 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c0c7100e-1f48-33a2-bfc6-9789d16f971c | -19.59322 | -56.75823 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 58b956f9-ebc9-3db6-bdfa-925f9ec054df | -19.59255 | -56.73137 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| f5492e08-6e96-3c74-8dd2-a56b3823dfa6 | -19.59172 | -56.76453 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 265328ff-266c-33ec-a64b-4716d3ac95a4 | -19.59106 | -56.73764 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 695e7005-9a60-3159-9009-a865d64906d8 | -19.58956 | -56.74393 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 19984edc-d6c6-3311-9e68-2aa19e2814b6 | -19.58807 | -56.75021 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| ead8c07d-26eb-39cc-8012-c58ebb336f81 | -19.5874 | -56.72337 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 622596fb-8be4-31c0-a7b5-de7583fb8b18 | -19.58657 | -56.75649 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 44003080-84ff-368f-be24-ca79dd805cef | -19.58591 | -56.72963 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| f99e5d6c-678b-3320-ba9d-f0d35ef8c4e3 | -19.58442 | -56.7359 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| f08de552-43df-349c-a0db-a102a1f33053 | -19.58292 | -56.74219 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 8546d8f5-5a58-309a-b0ef-37398feeb52f | -19.58076 | -56.72161 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 4c32746e-f68a-3f10-bf0b-eb9eb3563084 | -19.57927 | -56.72789 | 2024-10-31 04:06:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 9b56849d-408b-36ec-808c-27f7acc56a03 | -10.6819 | -65.002 | 2024-10-31 04:06:07 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 584fc712-1eb8-3fc4-9ec4-63a3ef34189a | -19.5083 | -56.5989 | 2024-10-31 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 6032f44a-93d3-3738-b5bb-00b3c9eadde7 | -19.5087 | -56.5779 | 2024-10-31 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 97aa63aa-2318-366a-825a-8354d4d39520 | -28.03792 | -49.95007 | 2024-10-31 04:08:00 | NOAA-21 | URUPEMA | SANTA CATARINA | Brasil | 4218954 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 997b3611-d535-343b-bdf9-ecbc7da41627 | -24.65856 | -50.17625 | 2024-10-31 04:08:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b27b8f4-b0cf-3cec-bda2-bfd5c7959a36 | -29.81316 | -51.17824 | 2024-10-31 04:08:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a67c649e-0921-35e8-b854-8afac329419c | -24.34848 | -52.16598 | 2024-10-31 04:08:00 | NOAA-21 | IRETAMA | PARANÁ | Brasil | 4110805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f3a2fbf-ad8d-35b5-9c67-7695ee949ec6 | -24.24363 | -50.74212 | 2024-10-31 04:08:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ea8548c-fe99-31f0-a908-c68b08e57e20 | -24.23212 | -52.87015 | 2024-10-31 04:08:00 | NOAA-21 | RANCHO ALEGRE D'OESTE | PARANÁ | Brasil | 4121356 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8a55535c-7c76-3a54-b8a0-d260b791f28d | -24.23078 | -52.86679 | 2024-10-31 04:08:00 | NOAA-21 | JANIÓPOLIS | PARANÁ | Brasil | 4112207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e0b1b272-00bf-3d76-a273-5d41f6de78a1 | -23.99501 | -54.10214 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 97ec7a4a-01df-3f2a-8775-b021aa39aa54 | -23.98976 | -54.10075 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 43463415-a788-36a7-8f45-e005d3e12dbe | -23.98451 | -54.09937 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e491ede1-ae1c-3313-85e6-02354b6a3254 | -23.98371 | -54.10293 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7c053d4e-5cd1-3622-82d3-3ade8fe04487 | -23.9829 | -54.1065 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f6f160e1-1561-3c05-a979-da4b43a26d66 | -23.97765 | -54.10512 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e3ab649c-d1df-39c4-bde9-e4bbb0ef0815 | -23.97684 | -54.10869 | 2024-10-31 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README16.md)
