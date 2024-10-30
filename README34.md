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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b85be459-7bc4-31a8-b515-104938edb9e7 | -5.8433 | -42.78542 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2e1c874f-c94f-3e8f-846f-0bc0f8d35997 | -5.83991 | -42.78488 | 2024-10-30 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fb3b2643-5b8a-3380-9286-6266acebd14d | -5.68837 | -42.64919 | 2024-10-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15857fb2-1a92-334b-a864-c5c7e8353a8b | -5.68781 | -42.65289 | 2024-10-30 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6db73694-3cea-3cfb-a7d8-9622bd6d1036 | -5.60206 | -42.9634 | 2024-10-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 456f8621-ceb0-3771-aefa-639c521adace | -5.5892 | -42.97977 | 2024-10-30 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 700322b7-4999-33c2-bd29-e4829d87a339 | -5.57197 | -42.87795 | 2024-10-30 04:19:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 571699bd-7009-30a6-a185-00a330a54978 | -5.48657 | -42.81702 | 2024-10-30 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5abbc9d-265b-3574-9240-9228e8a10e4f | -5.486 | -42.82064 | 2024-10-30 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02fe5f48-a779-3925-8567-58fb0d1e47e1 | -5.37649 | -42.23314 | 2024-10-30 04:19:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ead6d532-9a8d-3abd-b2b7-71385cfca9c8 | -5.366 | -42.6684 | 2024-10-30 04:19:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e290a23-ceaf-358e-94ca-c14485321c2f | -5.93182 | -43.45186 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e299cb-df7b-394e-8739-1d1c3d2ac3a7 | -5.8292 | -43.28036 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d2ef1a5-927c-37e6-bf09-016d88f28091 | -5.8281 | -43.28743 | 2024-10-30 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21a5f733-3051-33dd-b648-b06229823932 | -5.46052 | -43.17635 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 848ddbfe-c832-3b85-b725-563417512ec0 | -5.45997 | -43.1799 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ded1c82-b4df-383f-8846-823d80f28d4f | -5.45608 | -43.18293 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46272a0c-042c-34aa-8064-f6c38bbcacd7 | -5.45553 | -43.18648 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697a1807-bdc9-37af-8f21-5ecc49474aaa | -5.45273 | -43.18241 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841a767a-193b-33cd-ab93-69c40890d093 | -5.44946 | -43.20369 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 018a59e2-0d0a-307c-a98d-633cf31d03d7 | -5.40404 | -43.19323 | 2024-10-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af9ff5e4-3d93-3949-af41-e6f410d29801 | -5.30972 | -43.07699 | 2024-10-30 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f99d91a1-6a38-3f37-bc81-af0ba9a9f10c | -6.52051 | -42.2299 | 2024-10-30 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b25131a-cc7f-35e2-b7f4-b7d56beb8947 | -6.49772 | -42.35629 | 2024-10-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 962dad5f-7047-3c24-ae88-ca06f0faf8bf | -6.47929 | -42.19605 | 2024-10-30 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b3b09a05-5b29-3471-a1b1-8104acc2410e | -6.47638 | -42.1917 | 2024-10-30 04:19:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 05570143-ff63-384b-9f1e-2668447f8f2d | -6.47519 | -42.12802 | 2024-10-30 04:19:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4edf183e-5d46-3ab4-b421-c428dad36e16 | -6.47386 | -42.12818 | 2024-10-30 04:19:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 992177cc-b03e-3197-8ec2-a47f4971d6ca | -6.43199 | -42.09779 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13982a64-36b1-3b13-90c3-047b2b938acf | -6.42849 | -42.09727 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 224f0af8-2d75-37cf-bbb5-8c9c40c31943 | -6.42501 | -42.09666 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| fea550ae-d030-387e-b9f3-f6b95f929b7d | -6.42442 | -42.10051 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| d85c823b-3c84-375d-aa66-674db667fc9c | -6.42152 | -42.09605 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 93ae8129-c33e-37b1-9b30-febab613fe7f | -6.42094 | -42.09988 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 6ebd31e8-d498-3b46-b693-c7551481e722 | -6.41919 | -42.08781 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1c0b0825-2a42-34c3-8c7c-0a3500d5dd9c | -6.4186 | -42.09166 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71d6bcfa-92af-3d40-ab3b-557610e2efb7 | -6.41802 | -42.09549 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e69c857-51bd-3d3e-95d5-7d051d74b28a | -6.41744 | -42.0993 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a4b01f5-4d7a-3f1f-a3af-d32f282faeca | -6.41453 | -42.09493 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f418bc67-d368-3a14-a7d3-34eb4d6dfe0c | -6.41103 | -42.09437 | 2024-10-30 04:19:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02399845-5700-35ab-96db-45fd3aa7b33c | -6.19433 | -42.8044 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 784fcd35-157c-3e62-be0b-031f2c0fa569 | -6.19142 | -42.36562 | 2024-10-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db3192f2-90ae-38e3-97a6-f572928ffd68 | -6.18739 | -42.36887 | 2024-10-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c5b0a9b-81ce-3336-bdad-4773abc5d927 | -6.06289 | -42.65284 | 2024-10-30 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d01eb8ba-87be-322a-a165-4508c26c8b5e | -6.05947 | -42.65232 | 2024-10-30 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f06e572-91d8-35b8-a679-d5f4c4d2d13c | -6.03903 | -42.58076 | 2024-10-30 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7bd4678-d028-3f8a-9b54-f7a6fd1586ec | -6.25228 | -43.13644 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4da8d49-4877-3dd2-ae53-effaff1ff13b | -6.17456 | -43.18008 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4f5eadb5-236d-38bc-8542-406f5ef57b33 | -6.1712 | -43.17958 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bf892d23-378b-36d9-9afc-71f40d133c1a | -6.05404 | -43.3443 | 2024-10-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e468ea8a-3e43-396e-be42-3ab411c6852e | -6.32948 | -43.45227 | 2024-10-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36bb3528-91d4-3a57-82e1-c2309943a3f4 | -6.32613 | -43.45177 | 2024-10-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c5c902e-09ff-3d19-8d6e-49ec89dae098 | -6.21346 | -43.27716 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72a14d17-77cf-3390-bac4-a57d403598e1 | -6.21236 | -43.28431 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6ed41f7-164a-3936-bca9-3c7fcf91f21b | -7.92549 | -42.83451 | 2024-10-30 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9396b95-28f3-3079-9f9b-becd4a48466a | -7.92492 | -42.83831 | 2024-10-30 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d402f95-624a-3953-9fe8-b96315d61c82 | -7.92434 | -42.84212 | 2024-10-30 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1c58f9d-e68e-39bb-8260-155907590aa5 | -7.92147 | -42.83781 | 2024-10-30 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42f95ef3-29ff-3bbc-aad4-b031720e72fd | -7.9209 | -42.84162 | 2024-10-30 04:19:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b7e190d-fab0-3405-8431-3c577f2514e5 | -7.88731 | -42.97136 | 2024-10-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3bfea52-a1cb-3bd2-92f2-7e175c525db8 | -7.66405 | -43.03355 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08368921-8ce2-3371-bde3-080449435022 | -7.54826 | -42.8716 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e78fcf3e-8f1c-3a70-96f1-546c381d5f6d | -7.54484 | -42.87107 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84a7dcac-f089-3d8a-846e-7bf63672d370 | -7.54426 | -42.87482 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90d676e9-c61a-31a7-8ed3-96a68ac7c6a0 | -7.53684 | -42.87749 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 60c72b8f-103d-3f50-a202-f64454e6753f | -7.34492 | -43.55096 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc59ba62-6cf2-3e20-a552-1017979847fa | -7.34101 | -43.55402 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42fcf4e1-f915-36c5-8df5-add7411b5058 | -7.33766 | -43.5535 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54a66a7a-6e43-3da8-a120-7ad349234608 | -7.31796 | -42.93213 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a9549b0-f0c4-3102-86a1-45716a4a0d12 | -7.31739 | -42.93581 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3d02e7b-aef8-3c62-909f-fdd21efa0ac7 | -7.31512 | -42.92789 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8280d8d-db06-3a6d-a670-091edf77de57 | -7.31398 | -42.93528 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e746736f-23c5-3fd9-83c5-eae597bcf36e | -7.0169 | -43.02278 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ab037e2-b573-3cad-802d-58bfc6fe8d71 | -7.01634 | -43.02643 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 894e2cb9-443b-3c55-9aa6-b7dfd3ed3f37 | -6.84496 | -42.81561 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a360d88a-7aa0-3539-bfc3-7d4a1e06edf9 | -6.8444 | -42.81932 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93282451-ebb0-3b28-a158-095e07805364 | -6.84268 | -42.80767 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e1c9776-e097-3575-8bd8-3b8fcfec4176 | -6.84212 | -42.81137 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e58edb43-6f38-383f-9b7b-93435636c93b | -6.8387 | -42.81083 | 2024-10-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f644c4b-084d-34c0-8cd6-96dd6233e598 | -7.38667 | -43.47268 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38c76c3b-03b4-3f4f-8c42-2d3d339f072e | -7.38613 | -43.47625 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1dcecc93-e3cd-317d-95e6-41c64888560c | -7.37995 | -43.47165 | 2024-10-30 04:19:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31ab35d8-e9af-3a42-80f8-b9093f919839 | -7.32489 | -43.25634 | 2024-10-30 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d341d1ea-0aff-36db-8e8c-4c99092f932d | -7.32433 | -43.25998 | 2024-10-30 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90e8f270-cf7f-3f0f-a759-38cceca4b372 | -7.30049 | -42.29136 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03428e9b-2eb8-3516-908f-c3fee5511c4e | -7.29989 | -42.29527 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 35373b1d-8673-313c-b955-f5793a7417d8 | -7.28651 | -42.28914 | 2024-10-30 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aca604ae-5c6a-311c-8446-2018a85f1592 | -7.27921 | -42.4074 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ddecb7b7-f1ff-3ef8-b518-c11a795acd1e | -7.26338 | -42.48777 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7ce5da6-3518-3160-9210-c823081ce4b3 | -6.97381 | -42.43401 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 785905e3-5204-3a1f-80d9-123893ca4778 | -6.97323 | -42.43782 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9b9d84b-2865-36be-ad0b-ceca49a86725 | -6.97273 | -42.43282 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b64c74ad-5db7-3203-87f7-ee2d769932e9 | -6.97216 | -42.43663 | 2024-10-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1982db65-4762-31c5-821e-e11bcb14fb72 | -6.96976 | -42.43727 | 2024-10-30 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f1c3fb3a-94af-3b45-b06a-8a91e0af0a88 | -6.72113 | -42.15128 | 2024-10-30 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7f267e8-0b05-38ac-b023-65f1bce0e5d2 | -6.71763 | -42.15076 | 2024-10-30 04:19:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 100838d1-be15-3e0f-991a-40026663e01a | -6.63989 | -42.82631 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eaff801d-cd62-35a0-b4d7-04b064b8a2f7 | -6.63932 | -42.83002 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 596b73dd-0851-3c5c-b80a-19e3acedaa0b | -6.63705 | -42.82206 | 2024-10-30 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65ac5be8-4265-3eed-8a69-199892f19f95 | -6.63648 | -42.82579 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README35.md)
