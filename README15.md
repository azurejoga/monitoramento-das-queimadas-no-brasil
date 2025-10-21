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
| 757d2b17-0200-3a32-8cd8-a024aa41dbd7 | 0.07074 | -51.38245 | 2025-10-21 04:44:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e7e084-0b57-3513-aa32-a074853432a6 | -3.32989 | -50.22427 | 2025-10-21 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79a01734-26b4-3032-b523-76572e61b43c | -2.85422 | -49.54433 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5122537-f31a-326b-9938-e2ddc7dcc254 | -3.33393 | -50.74165 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69fc5f21-b4e3-3426-b8cb-031b8b21c4e1 | -2.25259 | -51.90794 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b4bd26a-6472-3906-9e42-4850e03f5484 | -5.18835 | -49.58593 | 2025-10-21 04:44:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5ca8a8e-bbb8-3192-9ef4-fdc009acc2ba | -2.87484 | -50.71463 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3185148f-cd5c-3f4a-9cfc-12f067c5f6a5 | -2.16705 | -53.48956 | 2025-10-21 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0b10999-80e0-3900-a2fa-c1983ca6ab5a | 1.70923 | -55.73581 | 2025-10-21 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d76a9cc-2a0d-3179-a3ba-4a2737d40cfa | -2.72289 | -48.83692 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e15ed207-a1dd-3efe-95ca-bdeb9834fc09 | -3.10848 | -48.60266 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130ddfa4-7873-33b4-879d-54f255a7bebc | -3.33339 | -50.74509 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a55bcec-4b83-3b4e-8f91-4e45de4bab84 | -1.00461 | -52.60818 | 2025-10-21 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 293d7211-ccfd-35b0-b315-562d567c18f7 | -6.14466 | -49.44519 | 2025-10-21 04:44:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cfe3f42-f6f1-3db7-9192-366dd8897388 | -3.86899 | -52.26328 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99bd964f-70c7-3460-b0d7-93f297d725e4 | -2.42376 | -48.59426 | 2025-10-21 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccc1ccc4-cabc-3bb3-87f8-96f769c52a17 | -3.32049 | -53.35731 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83fb54d9-30b3-3c41-9124-053a608a35d6 | -4.48729 | -46.47377 | 2025-10-21 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19d8f177-a1bf-3e88-9bcd-1c7315baa5d0 | -5.60211 | -50.0554 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29032656-061e-3332-adfa-fd9189ac216d | -4.00417 | -46.96448 | 2025-10-21 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18d6d8ae-a59c-3661-af1f-583ff5389143 | -5.68376 | -48.96972 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e9bd864-9764-3bc2-8d38-1c9df1300e63 | -1.19878 | -49.07368 | 2025-10-21 04:44:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c362d2-7b1d-34b8-9e5d-c4b294dd3892 | -2.79128 | -49.6193 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ad35108-737d-3245-ab16-dc02cda9ae2c | -2.86722 | -50.74168 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8e7d4e3-af8d-3d9e-9e09-b031165356bd | -2.20136 | -48.35795 | 2025-10-21 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09dc9bb0-08f8-3fc6-b140-1f17faa77eae | -5.58224 | -49.74395 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce526e9-e151-360c-a929-2f9945cdf985 | -6.89959 | -43.5939 | 2025-10-21 04:44:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8645318d-49c9-33ab-97da-5f4c5e9802dd | -3.37334 | -51.57233 | 2025-10-21 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1bf507-b587-3c4c-85eb-e8d67f791c47 | -2.73551 | -49.38726 | 2025-10-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be005f5c-4b4a-37ef-932d-743241132eae | -4.07478 | -48.03981 | 2025-10-21 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a90349b-40fe-30a4-9605-0e1733e47211 | -2.86373 | -48.56558 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a89bd327-453f-3187-b041-7500faeb3ed8 | -6.72923 | -44.1471 | 2025-10-21 04:44:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1035e227-a874-39c9-975d-57343abe3c3c | -4.74511 | -44.43696 | 2025-10-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ea38ffa-f2d1-3eb7-8b07-25471aac35b1 | -2.69636 | -49.55109 | 2025-10-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ffdc5e6-81e0-3fd1-9658-b9b8483683c9 | -4.87176 | -48.40723 | 2025-10-21 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43eb7c12-2476-3092-997d-0761079d90ee | -3.84717 | -51.67255 | 2025-10-21 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7406835a-dd86-3800-8e92-cc68cba8fdeb | -2.79867 | -48.93897 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb74282c-4e87-3262-b62c-e9b8936a07a1 | -4.61547 | -49.57266 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a663600c-8900-3c83-abc6-1d0c54acdabd | -2.25087 | -51.91897 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c99736-46c6-3375-b030-11fde8cf5b82 | -8.06306 | -41.05573 | 2025-10-21 04:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3e5aa63d-0e08-3963-aad4-01428359f220 | -2.48329 | -49.25963 | 2025-10-21 04:44:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3e1ecc6-9a29-3a23-9063-dc35144e9daf | -3.13554 | -48.62901 | 2025-10-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8205ab8-7816-34f1-8d12-428ff22b1c9a | -5.71063 | -49.22393 | 2025-10-21 04:44:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 070bf5f9-89bd-368c-bef8-78a6b60dba1d | -3.24483 | -50.02806 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cfeb968-c958-3445-90c4-fa16abe0c5e0 | -4.38779 | -49.68074 | 2025-10-21 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce546dc0-1308-324c-a485-9552fa75a4b0 | -3.33062 | -50.74113 | 2025-10-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c81821b-8ff5-34eb-88b3-e4e8aa153996 | -3.40674 | -52.71954 | 2025-10-21 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92edfd97-32a8-351e-b6a2-647fb13c874b | -8.71476 | -50.04796 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e30b4580-1335-35f3-9378-3feb705dd17b | -8.78129 | -44.20796 | 2025-10-21 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff2413dd-4706-3779-9fdb-37eda2b13292 | -8.71645 | -49.59836 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a143a333-3e7b-3b47-883a-fa7d49b4d76d | -7.99157 | -49.95575 | 2025-10-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff363d0-b009-3649-93c3-d0d6ed4eb641 | -9.11345 | -65.36019 | 2025-10-21 04:46:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c53d461-8204-35d3-ade6-04e1a5b3dc88 | -7.92956 | -47.18594 | 2025-10-21 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01ff4bfa-fe01-3543-9e1c-12806c3d8fb3 | -12.4242 | -54.49608 | 2025-10-21 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44805596-66ac-363e-8077-637797874b4e | -8.93687 | -49.79005 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05547899-8072-31bf-b8c9-c5790937a52f | -7.49118 | -47.32312 | 2025-10-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 743ebf6d-3e17-31c7-a851-eb9bb0a50285 | -9.01832 | -49.75729 | 2025-10-21 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4053d8b0-1505-3098-91d5-620df5255bf0 | -8.14721 | -49.46806 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff9439ef-9412-3fe4-bf2d-92e0222830d0 | -12.42249 | -54.42188 | 2025-10-21 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87e032be-75b9-305f-8160-165301cbaab2 | -12.42311 | -54.41806 | 2025-10-21 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b060c83c-3b78-33cf-9277-2ee6805bebde | -7.94201 | -47.99122 | 2025-10-21 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02bf5983-25e6-3a5d-bc56-de15f1a41206 | -9.64327 | -65.25288 | 2025-10-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f145794b-d87d-3edd-a128-7e8a98c45097 | -12.0482 | -54.23896 | 2025-10-21 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a27e6b55-44ca-3718-99ee-58f40fe087bd | -7.36491 | -47.74633 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86ae0da1-d083-3960-9b18-97080a058ff1 | -7.36797 | -47.7488 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bb3538f-ffea-3b05-ba4d-1366fea74e0f | -9.37963 | -62.63829 | 2025-10-21 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 598a2c47-1304-3f91-9eed-a289793d8849 | -8.15568 | -47.98932 | 2025-10-21 04:46:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 244162f5-52cb-3d9b-9c10-ed109de96edf | -9.12043 | -65.36159 | 2025-10-21 04:46:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccc72fd2-92d8-331b-8bd9-24ceed0be511 | -8.71195 | -50.04383 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b72480de-bbdd-3894-b071-e9a9667ac10d | -9.45352 | -49.85292 | 2025-10-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 378543c9-b96f-3242-a6e4-ac37bb87caba | -9.18934 | -61.38276 | 2025-10-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a79642f-adb6-39af-a0a0-d586d8087d05 | -8.60065 | -48.81464 | 2025-10-21 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f4bc750-5b38-3ba5-9037-8db2c5a58429 | -11.98255 | -58.0614 | 2025-10-21 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 606ebe98-9a22-3d01-9edf-d84695f92a3b | -11.90971 | -54.82834 | 2025-10-21 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b0e997e-9f5a-3dff-9e1a-de6242e717e0 | -9.45748 | -49.84975 | 2025-10-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 368b4d43-37b4-3581-88f2-685f960e6602 | -9.64197 | -65.25936 | 2025-10-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a57c8f84-eae1-356c-ad0c-aa404792d5d7 | -9.65016 | -65.2542 | 2025-10-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 564a88e1-563e-3e37-af49-84ce2f1fb060 | -7.36857 | -47.74688 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed12c75c-f0be-3778-b86c-bbcb37ed1c01 | -8.55543 | -50.04158 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84dc405-924a-3da2-bb4d-41300b26b6ba | -8.55879 | -50.04211 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3be3a17c-de18-380f-8953-3ee5e3145ec6 | -8.84743 | -49.70881 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a7d34dd-aefe-3596-ac81-33a169391bed | -9.37538 | -62.62838 | 2025-10-21 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99b8c66-0176-33e3-a5e1-1f004000a2ff | -8.85083 | -49.70934 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dfc2c03c-2c69-359d-bd26-25360f1d53be | -9.38822 | -50.33155 | 2025-10-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47cc8665-91d0-3cc9-97c0-7115b1f5c83b | -9.18865 | -61.38648 | 2025-10-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66d12619-8c53-3337-a18d-6fa1d0e5fc53 | -7.36432 | -47.74824 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d09178fd-23bb-3b00-a41f-e6c5ef1effc6 | -8.71693 | -49.59844 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4062eb7-2653-3ca6-8ef7-1f83c3dff2c0 | -8.71421 | -50.05156 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7976a5da-b1cb-33f1-ae59-6fed851bbf71 | -8.72034 | -49.59897 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26634d00-9e6a-3df3-9e96-360e7b04ff3f | -9.62207 | -64.74825 | 2025-10-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ab985e7-90b4-3022-add0-dfe6e9d592d8 | -10.07454 | -65.17023 | 2025-10-21 04:46:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a70413-fdad-3fae-969d-98e829b7d69f | -8.7806 | -44.21304 | 2025-10-21 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1244e34-ef96-3707-8779-6b4e42a417ce | -8.71085 | -50.05104 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7b2181-1088-36ae-b4a7-81cce83df507 | -10.08133 | -65.17165 | 2025-10-21 04:46:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73e83549-d25f-3b19-a0ba-45e5030e4a22 | -11.90621 | -54.82774 | 2025-10-21 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35689a5b-44ba-330d-ba25-321efb16d436 | -9.6288 | -64.7494 | 2025-10-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbf7a7cf-cca0-3d33-8f57-39692d893599 | -9.45692 | -49.85345 | 2025-10-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dbd0d87-19e4-3dfe-9457-808d5b5f5c49 | -8.2946 | -49.30616 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 695d03df-fcfe-342d-9a90-dd65ff08bf4e | -8.88039 | -47.97092 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce5cb57a-2b15-3a16-85c7-ae091b8267be | -8.84687 | -49.71251 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
