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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b2e6ce8-7ee0-313f-a833-ec7ae9a60683 | -15.1366 | -49.576698 | 2024-10-02 00:30:15 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0461505-cc2d-3036-a00f-c2e6ee85e448 | -14.7604 | -48.057999 | 2024-10-02 00:30:16 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31f7b57a-985c-3383-8f3a-1df1d2ed7a71 | -14.7621 | -48.0658 | 2024-10-02 00:30:16 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4be5dca1-a907-3a6c-a0ba-2bfcdb0443c8 | -14.7637 | -48.0737 | 2024-10-02 00:30:16 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87df0e5e-6523-3cca-8958-c0e646020f92 | -16.5201 | -57.2327 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb04c2d3-4a63-3f08-bdb9-fa4cb9b4aeda | -16.5252 | -57.2635 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93cc8f2d-8584-3838-b5dc-73ba9d359976 | -16.5105 | -57.234299 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 794777a3-4909-3359-9abd-0e50f320b5c6 | -16.5156 | -57.265202 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c74b772d-2c21-340c-aa33-21ed15b7a068 | -16.500799 | -57.236 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 558ae9d4-1145-3fef-8c5b-87fb139a4dcf | -16.505899 | -57.2668 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ef085ed-abd1-347f-b105-a25dadc24a9c | -16.4911 | -57.237701 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0cc10eac-4064-37f2-9f03-57a5ba7e9bf8 | -16.496201 | -57.268501 | 2024-10-02 00:30:16 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfb36778-59fe-3fbe-98ea-63106b9f2d24 | -16.481501 | -57.2393 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 963ebfde-9557-3aa5-9643-16a9df9ff325 | -16.486601 | -57.2701 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1128d077-0a58-361e-99f4-a3e6025d7338 | -16.4718 | -57.241001 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64590cec-ffdb-31ca-8aaa-5695ef63e275 | -16.4769 | -57.271801 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bdf3afd9-3b6e-3ab2-849d-b15493d5c7d7 | -16.4821 | -57.302799 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36a806d1-d613-3f31-9513-c7ea7ab5a2ea | -16.4622 | -57.242599 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 525ac284-590f-3776-836b-917a73b76318 | -16.4673 | -57.273499 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52be168c-c9b5-3f7d-ace1-788bc771bf71 | -16.4725 | -57.304401 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60754cf2-3afe-3891-b04e-10b52c22920e | -16.457701 | -57.275101 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa7b423d-e731-32e7-a7d1-f9bccf8e0a2a | -16.462799 | -57.306 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c61dcf53-2641-3063-bb14-2d63ea328cb7 | -16.467899 | -57.337101 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7be8a91-f543-39c0-ad64-b5012ce50cb2 | -16.5982 | -58.134701 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39316f3f-873d-32de-ac36-2017c5e86ec2 | -16.4531 | -57.307701 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75e29303-77b0-3f4f-a195-0d5b5a95ed3c | -16.4583 | -57.338799 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f020f2cb-15f7-3e79-8fc3-f65b17e012a6 | -16.5886 | -58.136299 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f841fa39-b242-3b82-9f16-42d343982536 | -16.578899 | -58.137901 | 2024-10-02 00:30:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db13d29f-b12e-31ec-be52-d8ee154a6bcc | -14.8161 | -48.764301 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4b40ba-312e-365e-bdff-1984355d75dd | -14.8029 | -48.749699 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a1336ed4-0fb9-3156-85af-23d2c2e71348 | -14.8046 | -48.757999 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbb0e9d-b91e-3fe9-922c-5a3ecf7ef6ed | -14.8063 | -48.766399 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb831ad4-ab32-3b40-818d-b43416693dff | -14.8081 | -48.774799 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5ece1eb-76c9-3373-b184-b0e396ec35c8 | -14.7931 | -48.751801 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 51e08289-c3ec-3888-8ea1-60f3fe02566e | -14.7948 | -48.760101 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3be487ac-2008-3fa9-9d2b-c1963bd2a9a8 | -14.7965 | -48.768501 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e68493e3-e1ed-3dab-9520-2f7c6bf6204a | -14.7983 | -48.776901 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c328c895-755b-34fd-b75e-96ad65d5beb3 | -14.7867 | -48.770599 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8fee156e-08fb-3aa1-b82e-0daf4c9ecdf9 | -14.7885 | -48.778999 | 2024-10-02 00:30:18 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca7a8637-6b93-3ccb-8925-4f5c5f33d429 | -16.444201 | -57.373402 | 2024-10-02 00:30:18 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92d90603-69b6-3945-92ca-0fddf9cc6f6b | -14.7752 | -48.7644 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62975605-da4a-3571-a8f4-ae94f450312e | -14.7769 | -48.7728 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 763e0972-a639-3d22-85e3-0291e59b52be | -14.7787 | -48.7812 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d7ac47cf-2bef-3aa3-ac79-62e74871f835 | -14.7689 | -48.783298 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 450df528-3a5f-3643-85a0-d8efa9e559c8 | -14.7706 | -48.791698 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c585344-7cc2-3f82-9444-eed1eb2d5689 | -14.7591 | -48.7854 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc47c947-7b42-30cc-a52c-c41019cc96fc | -14.7608 | -48.7938 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 21de8d67-ed2c-3f28-8abf-d7a644a976b8 | -14.8101 | -49.031601 | 2024-10-02 00:30:19 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8c3f6b0-9399-36d1-b497-abaf072aaf64 | -14.8119 | -49.040298 | 2024-10-02 00:30:19 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ef5960dc-0610-3d35-ae9b-dbe6794fd023 | -14.8137 | -49.048901 | 2024-10-02 00:30:19 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7850648-9705-3b90-a881-7b272500140f | -14.7458 | -48.770802 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9813a121-9e31-3159-8412-1baf9726a149 | -14.7476 | -48.779099 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68f63d1a-f3f1-3f13-a187-98b3590daa38 | -14.7493 | -48.787498 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0b077b0-f42b-310a-94fc-966d922da8b5 | -14.721 | -48.75 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12f85f56-1a53-3766-ab75-a256d003d3fc | -14.7227 | -48.7584 | 2024-10-02 00:30:19 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b90b2b9a-1fce-3db3-bf70-04f1fd17bfcc | -14.1714 | -46.464901 | 2024-10-02 00:30:20 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93e97158-cba3-321d-ae9a-df4fd14d1409 | -12.7147 | -40.215099 | 2024-10-02 00:30:20 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 755c6f53-8003-397f-8805-a540631082b7 | -14.1699 | -46.457802 | 2024-10-02 00:30:20 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23d24644-6fdc-3c7f-ab49-29676ecce2dd | -14.7113 | -48.752102 | 2024-10-02 00:30:20 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 089413f5-01a3-3a15-83df-1f1dd9d6d5d8 | -14.713 | -48.760502 | 2024-10-02 00:30:20 | METOP-B | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a199c638-53cf-359d-8a73-6bac449a89de | -12.8913 | -41.105202 | 2024-10-02 00:30:21 | METOP-B | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| adf59f48-73b1-3751-95c1-5795f99edc0a | -12.702 | -40.205502 | 2024-10-02 00:30:21 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 247c2940-daaf-3344-a28c-74911c174583 | -12.705 | -40.217602 | 2024-10-02 00:30:21 | METOP-B | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2640bc03-feb1-3a95-be5a-d6c5684a4e79 | -14.0321 | -47.9123 | 2024-10-02 00:30:28 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56d8ff66-61f2-3729-b489-d6c95cef03f3 | -13.8671 | -48.052799 | 2024-10-02 00:30:31 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9780becc-0100-3737-9d7b-ca82aa5bae6a | -13.7347 | -47.577999 | 2024-10-02 00:30:31 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f29a49b-c012-32ae-a801-183181ac8d74 | -15.3781 | -55.799999 | 2024-10-02 00:30:31 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d94a38b-b3dc-361d-855e-5f0c7bb6c0fb | -15.3823 | -55.8237 | 2024-10-02 00:30:31 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1f3b557-56d7-398e-80cb-4d950bb1a3c1 | -15.3684 | -55.8018 | 2024-10-02 00:30:31 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9a95adb-c429-3b35-af3a-fd1d02919e3d | -15.3726 | -55.8255 | 2024-10-02 00:30:31 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a078fd79-f096-3a42-9f2a-01c4146fa6d6 | -13.7447 | -48.152199 | 2024-10-02 00:30:33 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 55d88af1-0a84-3413-85c0-29d510bb60f0 | -12.127 | -40.894798 | 2024-10-02 00:30:33 | METOP-B | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 98d86885-51bd-3dfd-abdd-356ce9718e5e | -12.1243 | -40.883598 | 2024-10-02 00:30:33 | METOP-B | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fd399ffc-e640-3a28-a1eb-b5d9cbc89cc3 | -13.7528 | -48.1423 | 2024-10-02 00:30:33 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8515021f-756c-313b-849c-7d2df6263226 | -13.7544 | -48.150002 | 2024-10-02 00:30:33 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa37d37e-770f-3ee4-887e-e4e8931bb1fe | -13.7431 | -48.144501 | 2024-10-02 00:30:33 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c37d7e9b-644c-320c-aa95-0b267e90a6ac | -13.7511 | -48.134602 | 2024-10-02 00:30:33 | METOP-B | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9283588-ff95-305c-b4f8-17105492aab3 | -13.756 | -48.1577 | 2024-10-02 00:30:33 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5939168-d074-37e5-a948-be3a8024f1f9 | -13.7564 | -48.303799 | 2024-10-02 00:30:34 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e175e5a-35d4-30a4-a0f2-a3cbe8860a8c | -13.758 | -48.3116 | 2024-10-02 00:30:34 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be523b0c-d237-3ed4-a191-92b3471952de | -15.1371 | -55.795502 | 2024-10-02 00:30:35 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edfb0115-833e-33b2-a715-ed640c4dfe22 | -13.1683 | -46.301998 | 2024-10-02 00:30:36 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6345ca2-fe77-3e3f-a3fd-bab8887a2f81 | -13.1699 | -46.308998 | 2024-10-02 00:30:36 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4e83ec1-d47c-390b-8168-b2eb1f8f20a8 | -13.1632 | -46.325199 | 2024-10-02 00:30:36 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 943b5fef-1176-38c8-b47d-cfa0959fd3cc | -12.4367 | -43.713699 | 2024-10-02 00:30:38 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 487f2718-d72a-3645-80ca-e4102d8c4053 | -12.4385 | -43.7216 | 2024-10-02 00:30:38 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1945aeb4-0fd8-320e-ae49-9b2adcca11bf | -12.4404 | -43.7295 | 2024-10-02 00:30:38 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf0131d-415e-3415-8e06-b351fdb37e79 | -13.5075 | -48.580799 | 2024-10-02 00:30:39 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c056e553-4b85-32bf-b938-6f0bc950de1d | -13.5091 | -48.588799 | 2024-10-02 00:30:39 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f18aa91-0c9d-301e-babd-47c655afa613 | -12.427 | -43.716099 | 2024-10-02 00:30:39 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50c236f9-a315-3d30-b0df-06804826a8bb | -12.4288 | -43.7239 | 2024-10-02 00:30:39 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef58c45-8cd8-330d-b899-4730a95095fc | -12.4307 | -43.7318 | 2024-10-02 00:30:39 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cda566ad-cdfe-354d-ba97-0d14ab38d01b | -13.6361 | -50.3302 | 2024-10-02 00:30:42 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5d1545de-c247-3637-bd0a-8185fe762c8c | -13.6243 | -50.322601 | 2024-10-02 00:30:43 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 965b9ed3-2e25-3f71-8631-889b985ea0fc | -13.6263 | -50.332298 | 2024-10-02 00:30:43 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37307b96-6423-3cc0-bbce-653a2a8aeb0a | -13.2264 | -48.6092 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9d8d40f-b86a-3c68-a9dc-b6dc8f4de1ed | -13.2166 | -48.611301 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6d7b911c-58b3-3ef4-bcf5-bdb700df5a6d | -13.2214 | -48.585499 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 232decb5-fa65-3927-81b8-2f7d376000b9 | -13.2116 | -48.587601 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 32004398-9177-32a6-9721-6b00dbe7ce1a | -13.2133 | -48.595501 | 2024-10-02 00:30:43 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
