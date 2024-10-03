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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dad7b127-086f-30e1-a81f-dccae66a2474 | -2.85912 | -50.71868 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1fd4048-4598-36b7-9aaf-3925a1cb4af9 | -2.85857 | -50.7222 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b3122e0-4aac-3582-940d-6383bff0273e | -2.85803 | -50.72572 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3938e33-5f83-328a-8a22-636104617ec3 | -2.85632 | -50.71464 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 231b2877-6a01-37dd-9974-debbad1e5ba0 | -2.85577 | -50.71816 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 929fbfb0-f6ec-3955-9080-4a5a135b3fec | -2.85522 | -50.72168 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad366c5f-34e6-32c2-bd16-9b3e0186cb7b | -2.85467 | -50.7252 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1c07c5-906a-31de-aead-bb4cd84c5781 | -2.85413 | -50.72872 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b3a18fe-df2a-3276-9c39-e1c0e047743f | -2.85358 | -50.73225 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34a72515-e8d3-353f-bd07-a60b3150a9e1 | -2.85296 | -50.71412 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34a6a192-2fc1-3ef0-b8dd-95952660b8aa | -2.85241 | -50.71764 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eb0223e-3dec-302a-bb10-705f6b830cc8 | -2.85187 | -50.72116 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 810c69c7-00b6-34b6-a60c-a5b8765b9bff | -2.85146 | -50.71415 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa622ea-7bf1-3814-9cbf-004d8ae77232 | -2.85132 | -50.72469 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79b85de1-de4a-3590-86b5-7d6eae2e40d5 | -2.85091 | -50.71767 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a74af953-d3e2-3273-a689-6c9c9a789d6d | -2.85036 | -50.7212 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3de27bf-ecd6-3dc4-b0e1-f9d30c0a8366 | -2.8498 | -50.72472 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c809c57-6757-3e35-b850-cb21e07f7601 | -2.84756 | -50.71716 | 2024-10-03 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 591bf928-6f47-3fc2-b973-a2d8f5902c2a | -4.64102 | -50.98931 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 719c51c6-f31b-3cec-95e0-60f882ce9bc4 | -4.09966 | -51.11196 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd226946-d1bd-3241-a239-e0adf3abd7ae | -4.09912 | -51.11548 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcd26a82-d682-3814-bbad-d13a24e9100f | -4.09522 | -51.11848 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52d180a8-6fd0-3fb0-a3a3-570825126218 | -4.09468 | -51.122 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31225ab1-3514-3a4a-af19-2e2dc6448483 | -4.09188 | -51.11795 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3d9289c-61ca-3393-9945-32f441b97322 | -4.09133 | -51.12147 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40afff16-e311-36a2-9d22-9987c9f15929 | -4.05327 | -51.11234 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 845e7425-46f5-32db-ace8-13a7690827d7 | -4.04989 | -51.09018 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 131e1380-0367-3ee6-b511-55cb6852573f | -4.04654 | -51.08965 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96faaec6-cbbf-3088-8977-309352f67cd5 | -4.04199 | -51.05293 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05ae9a4f-1f9c-3bf6-bcb1-e94dd9691c18 | -3.95533 | -50.89143 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14bcdd9e-a61a-337c-ba32-c513b578ad7a | -3.95446 | -51.00706 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93604225-0b81-3661-b283-aae1e4f7910f | -3.95221 | -50.99949 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22286051-860b-32cb-8841-f1f85822e6b4 | -3.95166 | -51.00301 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47a5b8d0-42d0-3024-8cf2-310a2560dc38 | -3.95111 | -51.00653 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56149526-c4ce-3d3d-98c8-cedd3ad9b6af | -3.94831 | -51.24306 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cef7c22-a6a4-3cc1-9309-db86957c3391 | -3.94776 | -51.24655 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ea66f2f-2f2d-3f0c-b89e-879aa6e35c92 | -3.94497 | -51.24254 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36fdef73-7bbf-3b44-86ec-522e6d4956b8 | -3.94442 | -51.24603 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 838ffe42-178d-3045-8579-81807dc1a1dc | -3.94271 | -50.9944 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 166bfd49-7600-3b99-9a3d-6057e4b155d8 | -3.93944 | -51.25599 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83d50c98-1e82-3015-8131-2c59bef09ccb | -3.9361 | -51.25547 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 490f1b16-7c05-3d35-a7fe-c6a9a6ae8bb2 | -3.93555 | -51.25896 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60ef69ef-5f4d-3bfa-8fb8-ab055f4fa87b | -3.88194 | -52.09515 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25bebaee-16c5-33d6-86fa-eae1749286db | -3.87862 | -52.09463 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa8b7ac-36e9-38a3-aef7-1c2ac5353702 | -3.87808 | -52.09808 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 377cbd68-414e-3b1f-acc0-3a6ecabff7c3 | -3.87351 | -52.25672 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261c6278-8390-31c9-a23c-a10154a4888b | -3.86803 | -51.18766 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09df3127-d0b7-321f-a731-7d8710c73fa7 | -3.85707 | -51.75858 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 047a7037-ff10-3794-ba36-6cbd6f9535b5 | -3.83821 | -51.4008 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d06a6e5-ef0b-3d6a-a960-03c74526b6ed | -3.82756 | -51.3454 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74ea2006-86b9-3e95-a73b-c52038d8dcc9 | -3.79958 | -52.16721 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce99798b-1bd9-3beb-a2de-162f41839cb6 | -3.79626 | -52.16669 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1a6c76c-253a-310e-bf0e-1ac29a6ca1ca | -3.79092 | -50.80066 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73efc26c-05b7-3eec-9456-5ec03a19481c | -3.78308 | -51.32424 | 2024-10-03 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b4643f2-d7d4-3834-bf3a-fb084f986a47 | -3.77529 | -52.19175 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88b82f16-2ac4-3cd7-aa8e-0de560453157 | -3.77474 | -52.19521 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 675b5cc0-0033-343d-bf91-71687b9b8b09 | -3.76314 | -51.71175 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd40b7d8-9f6c-33b6-bf6b-e9c062042255 | -3.76273 | -51.8607 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f96f65a-12b6-36ca-96e8-eb82201162fd | -3.76106 | -52.26041 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262851d2-817e-3534-a304-ecd9e441ea1a | -3.75774 | -52.25988 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98760c21-4c7a-3bac-9883-0dd07e8dbdc8 | -3.75441 | -52.25935 | 2024-10-03 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac2bf87c-ed08-3764-874e-2e92f52f8e20 | -3.75349 | -51.12666 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e5c21b3-3ce3-336a-855e-bd78604bf142 | -3.75294 | -51.13016 | 2024-10-03 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf22232-cc44-3213-ad28-e0fe68fb43ce | -3.6761 | -52.24322 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95d4e663-2811-3e25-8d59-8f9c74cba933 | -3.67387 | -52.23578 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8787bc9-5d6e-3cd2-9a5f-1c9cab320741 | -3.67278 | -52.2427 | 2024-10-03 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37c2dba7-bcad-3601-802a-23290a80e891 | -6.47743 | -51.50361 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3205c7c7-780b-3aaf-b076-8851acce801c | -6.47688 | -51.50716 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cef6f88-0027-3eb3-99b6-8e925e07e22a | -6.46164 | -51.45024 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecf247be-49de-3cad-a242-5f28ab60ce22 | -6.34953 | -51.27636 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e342dea-d65d-31a3-8bf4-0347c6b547e6 | -6.38464 | -52.70134 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c84fe7b4-61f7-3864-ba47-0187294b4ad7 | -6.38409 | -52.70481 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b13395c7-ed5b-3e32-bbec-30ae4d5f09a4 | -6.38022 | -52.70776 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c68646-598d-3e52-a588-f78769ceb5bf | -6.32161 | -52.75542 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34d4ff36-f707-31a9-aeb7-3084e9a78caa | -6.31884 | -52.75502 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abf096ac-748a-3439-ab17-6d1e0574164e | -6.25402 | -52.35052 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65cfe6ec-8500-3684-ae10-b1b43bf79a53 | -6.2507 | -52.34999 | 2024-10-03 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64299d06-f69f-3897-bf03-c6e6fccd45ad | -4.22767 | -59.95462 | 2024-10-03 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 399413e8-e816-3e1a-a203-bf377263fa27 | -3.72388 | -59.36915 | 2024-10-03 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b33cb05b-99b2-3690-9134-6e85341ec633 | -3.7236 | -59.37088 | 2024-10-03 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81d9de4-504c-3186-9632-e51fda0ce7d0 | 0.8955 | -59.69775 | 2024-10-03 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72f3c437-691f-34f9-b3ef-168eb7dcc8dc | 0.895 | -59.69453 | 2024-10-03 04:49:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba3a34a1-caa7-33c6-81d2-1ab625c8c4d6 | -5.49903 | -60.46173 | 2024-10-03 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cce9229f-5bfb-3baf-b435-5e03c0251dc0 | -1.50468 | -61.59033 | 2024-10-03 04:49:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fc0b516-26c2-3aae-ba6c-09c6d9028df4 | -2.88796 | -61.87689 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57c2351a-e3c4-311e-b9a1-80bb60b5ea45 | -2.88739 | -61.87389 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3735bf34-5654-3e5f-9e39-cd57d21f04f6 | -2.88289 | -61.87215 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07ab5371-2e46-385d-8d43-441507115b97 | -2.88222 | -61.87605 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a43f6e6-01cc-33c6-af7a-4c5ce22aad2c | -2.88165 | -61.873 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fafc16c-3237-3c7e-9c48-58ea16efbb28 | -2.88156 | -61.87994 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4538009-0fdd-30ba-8ed2-d2217ef8d195 | -2.88101 | -61.87692 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde7cd8f-9782-3531-9573-04e6acc5fb74 | -2.88037 | -61.88086 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5495de4-8a0c-3736-bf79-f3476270b548 | -2.87582 | -61.87906 | 2024-10-03 04:49:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e0632d6-e06b-3417-b6a2-7952a19520ae | -1.65992 | -52.58617 | 2024-10-03 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15afe98c-b903-395e-8c27-1f73a51d2fc3 | -1.65656 | -52.58565 | 2024-10-03 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a485c7-effb-383b-a9e6-9531fcc7e200 | -1.42935 | -52.96425 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ed5896d-8786-3b80-964f-854215888406 | -1.35137 | -52.30779 | 2024-10-03 04:49:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fe5e35d-e2e0-3074-abf0-15cbdf07f675 | -3.29561 | -53.70086 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f25dd8f6-e2cc-33a2-b042-b03f5f92a4a4 | -3.29218 | -53.70033 | 2024-10-03 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05e9c40a-299a-3b83-80e7-cac1ac5d0200 | -3.08244 | -53.06545 | 2024-10-03 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README119.md)
