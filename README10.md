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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66aa1671-8576-310e-8cf5-3ce760fc6a53 | -4.42272 | -49.72159 | 2024-11-12 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a688280-c07f-3ee9-9128-fb85e9cd4728 | -2.77706 | -50.31519 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5e6d473-4612-32e7-8c5b-dc3ae47d42f1 | -2.77564 | -50.31707 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb5762aa-1af0-3f72-bad6-1c141c86652a | -2.78426 | -50.30383 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8cb4683f-1c7d-3aff-9d3c-9c143d2789e7 | -6.85519 | -38.88617 | 2024-11-12 03:59:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b80a692-ff87-3d9c-9d74-52d7a8ef648f | -3.07229 | -49.20335 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac4d8933-3abc-3c18-a2c8-e3d0521b1de4 | -3.84804 | -50.21607 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78605f86-99fe-3b2c-9882-3591d9270b78 | -4.15467 | -50.80137 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 486c9274-d341-3a5c-8276-cc7c84d6c876 | -3.19626 | -50.28048 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bdd93fa-e4b6-3384-a107-e0d4692780a7 | -7.77802 | -34.92722 | 2024-11-12 03:59:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb38d96c-4a05-38c2-99ef-3ac920aec594 | -2.12038 | -50.72071 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fda3eed5-2571-39ea-bc3b-3ef14b342370 | -3.6089 | -48.91076 | 2024-11-12 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f0f8ac6-e083-3543-8a8e-e64f64a9cf3a | -4.4169 | -49.72071 | 2024-11-12 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 518b432f-66b9-3aba-b1e8-693eacfd22ae | -3.84616 | -52.38379 | 2024-11-12 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2adc1da0-7337-3566-a1e6-7eea1f573fa7 | -7.1818 | -35.01686 | 2024-11-12 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 190cb875-f484-3be5-ab97-d2e6508f7f0c | -3.73411 | -40.95771 | 2024-11-12 03:59:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e17a349d-5cd6-3c03-8187-ef35a90de297 | -7.4307 | -35.2361 | 2024-11-12 03:59:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| faa805b7-ea9f-3bb7-9893-e6f72a318c11 | -2.78507 | -50.29911 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47969f6a-ed9b-3ee2-95e0-37d8c5bd213f | -3.05459 | -50.34118 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b235519a-5b95-3e55-9641-f68397524bdc | -3.43067 | -43.03462 | 2024-11-12 03:59:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ac5e8aa-28d2-3319-a0ba-66adbfefbb07 | -2.78479 | -50.30672 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a068e1ce-3739-31c1-a2bd-3b36a3bc3abc | -3.24157 | -50.30945 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d73e4b6-0bc9-35c9-8191-7b592a530fb2 | -3.07832 | -49.20651 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce81e9e4-e4a4-3692-9be1-688f870d3b14 | -6.13002 | -38.89639 | 2024-11-12 03:59:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9e886ad-cb24-369e-88db-92d0f6fdb578 | -3.74597 | -50.18744 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2987caa0-cca0-34bd-97bf-b13af5c6d925 | -2.77628 | -50.31994 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ed81f59-aee5-3dd5-982f-4fe456c08860 | -5.88017 | -39.67015 | 2024-11-12 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 642f00d1-11c0-326d-9b51-6f346e1d5406 | -4.55962 | -37.9749 | 2024-11-12 03:59:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cb531924-e2a8-3e7f-9cfe-1603a3083213 | -3.30436 | -42.48306 | 2024-11-12 03:59:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 035026d7-7bcd-3ab2-8d4f-89fc602b357a | -3.84727 | -50.22049 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c998a3ce-3891-3a03-a17f-af7f342b2cda | -6.8652 | -39.12949 | 2024-11-12 03:59:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8728d247-4d7b-376d-b5b4-01f3ec048143 | -3.79234 | -50.09904 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60d9f1a4-94cd-3e3a-b274-5c1850eb3efc | -3.43618 | -50.30866 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfddf6ff-f6b0-33cd-8683-3c5ef8b5da1c | -3.06154 | -50.3375 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c60f9b27-658c-3e0f-9489-9d64d11cf597 | -3.66 | -50.21227 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f9bda2d-acbf-3509-aca6-423947412f36 | -5.12693 | -37.8534 | 2024-11-12 03:59:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 89950c07-1908-3067-be8c-780c4cf0952d | -3.04844 | -50.34008 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9ed55629-f018-3b05-849d-0d302a91d2fb | -3.8532 | -52.38402 | 2024-11-12 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 759032aa-28f2-3a09-a868-6d8f8dcb4a52 | -3.85419 | -52.37841 | 2024-11-12 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c12c17d-ed90-3582-85b4-3f41238d2080 | -3.22108 | -50.28196 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0a995d3-b1d2-3b1c-99db-01000316fe06 | -5.80968 | -35.53962 | 2024-11-12 03:59:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b09d7287-2a69-3391-a38a-83693d220e6e | -2.78402 | -50.31146 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2419fec6-f252-31ea-8212-15ef35589473 | -3.73863 | -50.1889 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 613fd16b-135a-3920-82c5-7ad4878749cb | -3.15987 | -44.06303 | 2024-11-12 03:59:00 | NPP-375D | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfe2f834-c16d-3438-b2f8-0ee7b3e822f3 | -3.07801 | -49.20431 | 2024-11-12 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b5b8e3c-0fc8-33dc-8f5c-482a09bde26a | -3.73919 | -50.19067 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b748a56-616e-3fba-a08c-1de2e8c6771f | -7.77854 | -34.92362 | 2024-11-12 03:59:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bb82bac-c475-323c-bb61-34f74a237356 | -3.73999 | -50.18614 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ab2e2f5-4056-32be-a980-126a11dd6842 | -2.77645 | -50.31233 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 368e455d-d798-31d5-a324-10d85d62c94f | -2.73236 | -51.8293 | 2024-11-12 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d2c465e-771c-32bc-a58c-9628720a344c | -2.78019 | -50.29614 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 80c1ca00-62e6-323e-8908-4fba1cdf8b35 | -2.77728 | -50.30754 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16abe721-ef9c-3082-b488-531589a5ecb1 | -2.77809 | -50.30279 | 2024-11-12 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db7fbeea-b3d7-345a-9370-593a73e3e45d | -3.79456 | -50.03923 | 2024-11-12 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b106a4a-d3f3-36a7-a6f9-b490d3fd41ea | -2.1271 | -50.7121 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f2b19e0f-7c71-305d-bedd-32baa3d23536 | -2.7922 | -50.2986 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 24fddc89-8c1b-3ad6-bac2-6b914ab17753 | -2.1455 | -50.6908 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2811388b-0a77-3bf9-8374-61d6e98b31c5 | -2.1272 | -50.6703 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0a38d6db-bbbd-3dd3-a6e6-05bebb6e61f9 | -2.1087 | -50.6916 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e98549ed-c364-3a91-a5ec-c7e779dda310 | -2.1271 | -50.6912 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 262de4dc-f13b-3bae-bf93-3210b8c01f11 | -3.1096 | -54.3066 | 2024-11-12 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c234fdab-ccf2-3acf-99cb-6e30d1e8f4d0 | -2.7737 | -50.2992 | 2024-11-12 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 88a1b046-0e19-3e4f-b4e6-8b8013848dd8 | -16.3497 | -43.69392 | 2024-11-12 04:01:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6b2c2a3-16d6-35a5-899b-66a6a4808759 | -15.89543 | -43.45852 | 2024-11-12 04:01:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67c1360c-a1d9-3404-babd-51b1122e0342 | -14.79264 | -42.71963 | 2024-11-12 04:01:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f278516-a9e0-3587-868d-0e43cfa3b44f | -15.89482 | -43.46226 | 2024-11-12 04:01:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 37a1fbc8-bf31-30a2-8c41-8f2e72240e32 | -16.57187 | -44.06446 | 2024-11-12 04:01:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c86ef0e5-112b-30a8-9b64-0a930e20d5a8 | -15.89205 | -43.45793 | 2024-11-12 04:01:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2dc4161d-e43d-361b-9696-aa4aafa26c52 | -16.57465 | -44.06895 | 2024-11-12 04:01:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb606ea3-3358-3991-835a-ba4e1d082f1e | -16.17346 | -42.18928 | 2024-11-12 04:01:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10d8c70d-61aa-3d1b-835d-d780c84db8c8 | -16.34907 | -43.69769 | 2024-11-12 04:01:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d66a16e3-a179-3eae-8799-b552d300139d | -16.17289 | -42.19287 | 2024-11-12 04:01:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8c26029b-3a43-3830-bc6a-ec81812a3ca3 | -16.57123 | -44.06832 | 2024-11-12 04:01:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c7bc3f9-ff2f-3c9b-8246-ee46b8a08f8c | -15.89143 | -43.46167 | 2024-11-12 04:01:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 73d324d4-4952-36fd-a7f6-dcde60a63676 | -16.57401 | -44.07281 | 2024-11-12 04:01:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 237ddce4-9a55-3984-9805-5c181bf202ef | -16.58087 | -43.7341 | 2024-11-12 04:01:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b30b406c-e163-33ce-9c1d-55525337f9cb | -22.6764 | -42.85358 | 2024-11-12 04:04:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6af23aa3-be7e-3eeb-9e1f-6ae7d1a16e01 | -19.83739 | -40.08149 | 2024-11-12 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17e10e25-cd7d-35d7-842f-8bdb1b48cdf3 | -21.62463 | -43.46708 | 2024-11-12 04:04:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 36587fda-0e21-3757-95d0-5c23233c76c4 | -17.41533 | -48.52818 | 2024-11-12 04:04:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07582e6d-5790-3b7f-9784-50a46be64835 | -20.31842 | -48.83138 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4237e9b-77b1-3acd-88aa-774e7bdd6a18 | -21.31604 | -53.92255 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d76f4bcf-a42d-3e19-b4a4-a24ad6b766e5 | -19.62109 | -54.15223 | 2024-11-12 04:04:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57c66ec0-16f6-3aca-9f0f-a857a21db389 | -19.17725 | -40.12805 | 2024-11-12 04:04:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f29bb4f-6d16-3f6d-895a-6c571dcfe74e | -20.90142 | -43.81988 | 2024-11-12 04:04:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 46797511-366e-3345-8d4e-5bfc061a5f33 | -18.03965 | -44.52788 | 2024-11-12 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a747aaff-6b60-38ed-a14c-427ca59f2129 | -20.51919 | -47.33258 | 2024-11-12 04:04:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 703a28d2-5a87-3595-8983-03e2e55a6124 | -18.03688 | -44.52333 | 2024-11-12 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b5ee22e-339d-3d36-839b-67dd934cb273 | -18.44828 | -47.55076 | 2024-11-12 04:04:00 | NPP-375D | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c47cd98-50bd-3cc0-bf71-829d3dcc1a1f | -23.5218 | -46.97452 | 2024-11-12 04:04:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b70b93cc-70bc-398c-81df-bba5718f8864 | -20.31766 | -48.83531 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fee93bbe-7308-3944-bd03-a217f51188d2 | -21.32071 | -53.92791 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66c08b0b-8f65-3c9f-8cc1-a3d4b7c2fe67 | -19.17255 | -40.13577 | 2024-11-12 04:04:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 49625b7d-2f9b-31f7-8179-9e408041330a | -22.92279 | -45.41415 | 2024-11-12 04:04:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75eb4475-f4d7-3717-91bf-84a64f5e914d | -17.73643 | -39.52234 | 2024-11-12 04:04:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36799913-2ca8-3bd3-8070-22caf66edc4b | -20.32331 | -48.82831 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 206e8a75-f8e4-31ee-9e5c-4ffa4ae2a06c | -21.3198 | -53.91966 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 841c50c7-5900-3f1b-9df5-0d46cefc80d6 | -21.31688 | -53.91872 | 2024-11-12 04:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50dfb72f-f7b9-30f1-8ed0-6172994c9d40 | -20.31919 | -48.82742 | 2024-11-12 04:04:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1e4068d-6033-31e6-b320-15259102f1d1 | -20.10701 | -49.18609 | 2024-11-12 04:04:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README11.md)
