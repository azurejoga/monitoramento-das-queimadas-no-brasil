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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c16c769d-0433-3639-8e49-0891087071cf | -2.71951 | -46.80943 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76170e49-8e79-3f65-bfa7-b4cf49b43149 | -2.71901 | -46.72186 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27016369-1f72-3512-8e26-312da2a6ba7c | -2.71632 | -46.72222 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22eea6d3-73d1-371e-9114-a6627354e824 | -2.71593 | -46.80883 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1fdca2d-4710-304f-b941-1017d9fcb981 | -2.71544 | -46.72128 | 2024-10-06 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf7cfc9-85bf-3063-b39f-a1a18cd231a9 | -3.90772 | -46.44789 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0adc058-a601-31a0-a780-c40c508fd9eb | -3.90424 | -46.44736 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 658f8906-b381-3d63-a698-afd50aadfc1d | -3.85178 | -46.46265 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 786a3d8f-fbb3-3f9d-93cd-d7d435fcbdaf | -3.85116 | -46.4665 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3743748-7563-38b7-abbd-ba469c340bbb | -3.84768 | -46.46591 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 0690bfd6-a607-3f63-ad80-1a3f489c8c43 | -3.84669 | -46.46225 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 17ef4262-b2cf-343f-9cb3-4c74033373a6 | -3.84609 | -46.46611 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| c948e791-dee7-3da9-9b30-d3769afce23f | -3.84482 | -46.46148 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 61a11fa5-a1d9-3404-8cc4-e60691a5bdf4 | -3.8442 | -46.46533 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2b22822c-ae05-3bb8-b780-42a4fa0198a4 | -3.84321 | -46.46167 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b1dc8844-3aa5-3f0a-beb2-50abc2b74d1c | -3.8426 | -46.46554 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b3adff30-2c38-313f-a1c5-164231f8fb5c | -3.82619 | -47.49432 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695f11ee-edb6-37e3-a4fb-fb26add52c8a | -3.82321 | -47.48949 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdeee162-20a8-3196-ad8d-4cd8e827a95c | -3.82252 | -47.49375 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec7bd3fc-e0ba-3c83-a23c-ff9475d15955 | -3.77634 | -47.61509 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9788f40-77b5-31bb-8615-6a4aebf02925 | -3.61661 | -47.51676 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0dfd30d-3f7b-3780-ab92-46e8e42fe890 | -3.61293 | -47.51618 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b24e5d-a78b-358b-81cb-de172cd736f5 | -3.60925 | -47.5156 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7433024a-0bb5-336d-9173-2e6ae70db4ad | -3.60855 | -47.51992 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76014548-d309-3c1a-a121-3e40b9c9a8fc | -3.60487 | -47.51934 | 2024-10-06 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7357a97c-e80b-3a7d-a170-1a8e4d1806a8 | -4.82621 | -46.7979 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5388cae9-7a9c-34c7-a038-b5b271358016 | -4.82558 | -46.8018 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6757953d-9638-339f-a0bd-31726a90c9e6 | -4.82495 | -46.8057 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f5d6813-59e8-3c65-93fe-eacab1d4dfe3 | -4.82271 | -46.79734 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94d87c23-bf3e-3254-9e34-dd2fbbc2de0a | -4.82208 | -46.80124 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adbf59c2-e36c-39b7-b91c-c5651adc3e92 | -4.7666 | -46.67084 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6210f9dd-cf5c-3caf-8c30-37475cb3f36e | -4.5317 | -46.82652 | 2024-10-06 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3dabb41c-7e5e-3c1b-9ee2-d8f231b4fd25 | -4.42792 | -46.43723 | 2024-10-06 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab001bf6-eb0e-3ec0-abb9-98f10710f446 | -4.42731 | -46.44106 | 2024-10-06 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9874922-53da-3fe8-8eba-58be4f868e25 | -4.42446 | -46.4367 | 2024-10-06 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3be3ad8-7eba-372b-907a-6b157f4a937d | -4.41876 | -46.42795 | 2024-10-06 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b90b8ffa-4147-3c2c-aa17-4866084546c0 | -4.29808 | -46.77048 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51295504-76c2-3833-b405-b3eb8c52d6ef | -4.29745 | -46.77439 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec28a186-b06a-32c8-a14e-d476f9b9bf64 | -4.18377 | -46.85061 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52bbbcbc-99cd-3127-8cfc-61490319d9ad | -4.18314 | -46.85455 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b64eaf14-67e9-37fa-a5ff-9527285e7ce6 | -4.18024 | -46.84999 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54b75eb4-c21e-3f53-8595-7755f4a27d51 | -4.17961 | -46.85397 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 000ef386-72c0-3d48-8635-f539e9517200 | -4.13431 | -46.19127 | 2024-10-06 04:19:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5651f0a6-3edf-3278-8501-14183f2a6531 | -4.13361 | -46.71335 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a0d4627-73e4-3622-9546-578599d8d631 | -4.1227 | -46.68807 | 2024-10-06 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fabb84a-9f18-3372-992e-d612e78bc37d | -4.45687 | -47.46447 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e701f6e7-ffbc-371f-bd40-835682ba1f29 | -4.45618 | -47.46864 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c0435d3-60eb-3eb1-84cb-decd34166be3 | -4.45255 | -47.46805 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9149b70d-1413-31d7-8ef4-603d93da7e1b | -4.34791 | -47.29894 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae793df7-91b9-3044-836c-04d72525e9ee | -4.34495 | -47.29432 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bdeb2fb-0139-38de-b6f3-87017b5a9337 | -4.34199 | -47.28972 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35af877f-d143-3abe-9267-85c1229381b1 | -4.33936 | -47.3062 | 2024-10-06 04:19:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 505a536f-7a0c-3dde-9386-5b71a3d0ec54 | -4.31245 | -47.70598 | 2024-10-06 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a48d99df-7586-3d2d-822c-393dc6d934d2 | -9.45492 | -47.58107 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6d91833-5836-3680-b12c-d70eb418b4a3 | -9.45209 | -47.57666 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14cc528b-c257-389e-b0db-5a8d3ae584f5 | -9.45146 | -47.58049 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f51e9625-fb1f-3c20-982d-8508a9c4694c | -9.43668 | -47.56236 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b28afd-3a8d-3743-98d0-fa28f56918ad | -9.43323 | -47.56178 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd938afc-c692-3737-ae70-228f9a4a8429 | -9.43259 | -47.56562 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab4c83cb-2b4e-3edf-89e3-b1df4443872f | -9.42913 | -47.56503 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7374059-84b9-3987-901a-79abb53a8358 | -9.93357 | -47.70603 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed8dfa9b-1661-3f6d-9418-c2216ac72416 | -9.93073 | -47.70156 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 454e38fd-b5eb-37a7-80fb-bb4d38f9c410 | -9.93011 | -47.70541 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31dec5f4-ed1d-397f-82ee-3a56567cf501 | -9.92854 | -47.69319 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa1cabad-4729-3658-9cd9-3592d2ad25c0 | -9.92728 | -47.70094 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38d333c4-5482-343c-8a42-2862381c78ef | -9.92665 | -47.70479 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a04d0dc4-93de-39e4-9e92-8ec8b481e289 | -9.92445 | -47.69646 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b5bdd92-5b73-3b93-8529-3378a0fa0b35 | -9.7736 | -47.58531 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b392aa-7b75-3e2c-b88f-f5a86ca91456 | -9.69864 | -47.83548 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 389936eb-8ce8-3c4a-954e-6afd7f4f18a4 | -9.6977 | -47.81918 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b44eaf86-96ec-3e73-89ed-5d393fcdaffb | -9.69707 | -47.82308 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed1ae2c4-1550-3a8c-958d-e6f6c50b5e6a | -9.69643 | -47.827 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0463988-bffa-3429-81f3-c991ef0d4fe1 | -9.69579 | -47.83092 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3a8b977-d600-36b7-b64c-de85da939a26 | -9.69515 | -47.83485 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10b02044-0593-32ae-8a29-bdac4c06cbe4 | -9.69452 | -47.83877 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c6ab42c-2f7e-3723-a6d0-e85634fd9eac | -9.69421 | -47.81859 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dcf5dcd-53b1-373e-8901-9c7dbbd57c85 | -9.69358 | -47.82248 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 536b12cc-0248-3e7d-9c54-5beb6ceb3e8c | -9.69295 | -47.82639 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd29e8c1-0458-39df-a4cd-8c8336651a86 | -9.69231 | -47.8303 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b208e75-ac96-3189-ace2-327a50a12dda | -9.69103 | -47.83817 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b0af3ea-fc29-376a-9ce1-494edd485896 | -9.69073 | -47.81801 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c369570a-0083-3842-a359-3f0f900b5fa8 | -9.69009 | -47.8219 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87f30a44-603a-32e6-bc1f-430070bdad1e | -9.68946 | -47.82578 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2920904a-9d21-3df4-b190-3db45332b9c2 | -9.68819 | -47.83361 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 429204ca-ba24-3331-a27d-4eeebea803f2 | -9.68754 | -47.83757 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c4e3229-6873-3156-a0ed-0bde9d1c9fa3 | -9.68724 | -47.81743 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7621f755-30c8-3a87-8f40-f42f81108504 | -9.68661 | -47.82132 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9be7a65a-10cc-3b82-8d7a-75b343d98c16 | -9.68598 | -47.82519 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af60c695-a016-3859-add0-2a46402603b1 | -9.68406 | -47.83696 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 447a4e52-113b-3d56-bb85-19bd16001cd5 | -9.68376 | -47.81684 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb457b39-4e2b-3bb9-9a8e-c10e71c72ef1 | -9.68342 | -47.84086 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd7e7dfd-9feb-31ec-9f59-8413a6444ede | -9.68312 | -47.82072 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 46f83963-a802-32a3-8683-ef88b4504786 | -9.68027 | -47.81624 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e60d2022-d5c2-3a9d-82f6-b41976d0dd1a | -9.67964 | -47.82014 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4152c89f-540d-3408-aaf2-434a765b82b0 | -9.67865 | -47.8481 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e67c749-35d3-3a49-a874-874216c4e38e | -9.67679 | -47.81565 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d186bb92-62ef-3cc9-9744-8e159a7e1581 | -9.67615 | -47.81956 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 646c468a-b261-3480-9d00-82fda34a8bc3 | -9.67551 | -47.82346 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51dbd2d4-6929-3887-89c1-b4da87c2a623 | -9.67487 | -47.82737 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 924d7602-0b1e-34d9-a8de-281b51e209d9 | -9.67423 | -47.83128 | 2024-10-06 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README74.md)
