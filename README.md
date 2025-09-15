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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c788b0-6de8-3f4f-8c5d-5a965b8ec1ac | -7.8567 | -43.5662 | 2025-09-15 00:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0e290257-634e-3c35-86ac-aee73179d94e | -5.7047 | -49.1998 | 2025-09-15 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a44ce485-0ffa-352e-8f9e-c25033228921 | -6.9254 | -46.1647 | 2025-09-15 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| eb7d3fc7-c78d-375a-8566-c9b39a84774c | -14.0407 | -52.1663 | 2025-09-15 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| afe99d85-6a21-305c-b243-7977e7f074d7 | -23.0083 | -47.5437 | 2025-09-15 00:00:00 | GOES-19 | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 7709dce6-2b01-3086-9589-4af39b79a2aa | -10.9365 | -45.5063 | 2025-09-15 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 2c1b7575-3027-3d6b-a32f-ee61cb2f69d0 | -8.9073 | -45.5024 | 2025-09-15 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| dbf4365a-3873-32d7-937d-579661e56c56 | -7.8753 | -43.5876 | 2025-09-15 00:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| e364df6e-71e7-34d3-bce9-f49f3981ec13 | -11.78 | -47.5583 | 2025-09-15 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| b7c4eb3f-d364-37f9-9d14-b8120bf6df69 | -15.8619 | -59.418 | 2025-09-15 00:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 20aa7350-f832-3224-b2bf-070ffcb859ef | -7.8564 | -43.5896 | 2025-09-15 00:00:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 32b3d25b-28e6-3bda-895e-670539a8915d | -16.491 | -55.1067 | 2025-09-15 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 153.5 |
| 0991b3b8-e96d-36c1-a4b6-92ec53e57bcb | -12.006 | -47.7505 | 2025-09-15 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 32a0940d-8ffd-34af-9137-5e75236f842b | -5.6861 | -49.2009 | 2025-09-15 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| d4be56d2-d98a-327d-9b95-3a726bfe3ea3 | -15.8425 | -59.4198 | 2025-09-15 00:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| dcff69c8-c65e-39dc-a822-bfdbf31de3bb | -10.9361 | -45.5292 | 2025-09-15 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f3d78bc9-28a7-3e96-971e-5a763137c4d6 | -16.5106 | -55.1042 | 2025-09-15 00:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 66c70a18-77fd-3cb9-acee-873589939918 | -14.9416 | -46.5525 | 2025-09-15 00:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f092fa3d-4bef-389e-b950-1d1873f738db | -7.8861 | -63.7135 | 2025-09-15 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5d426d04-e96f-38a0-a669-836cb5724ce1 | -7.6838 | -48.8682 | 2025-09-15 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d169577c-fb81-3276-a824-5355eb363ca3 | -8.6136 | -46.3452 | 2025-09-15 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f5c38dc6-1bbd-3b65-bb18-eb8c6b80684a | -5.4798 | -44.6942 | 2025-09-15 00:00:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| be85740d-463f-3d5c-a406-6eb67a335b61 | -7.8862 | -63.6947 | 2025-09-15 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ac2417a0-e677-3cdf-912a-cc753ad561ee | -10.9365 | -45.5063 | 2025-09-15 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 79804821-3234-37df-8d33-bed405a545f3 | -23.758 | -51.8917 | 2025-09-15 00:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| d74c9aec-4c61-3849-b87f-5da92906ccbd | -7.8862 | -63.6947 | 2025-09-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8bae4a23-d5fa-351e-885c-0b53a62d3253 | -7.8567 | -43.5662 | 2025-09-15 00:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 269.6 |
| 002ad732-5325-3245-8089-56c7fc50da9b | -7.8564 | -43.5896 | 2025-09-15 00:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 398.9 |
| 8e0e605c-7888-3f89-b2d7-3ef3865135a1 | -18.0502 | -50.935 | 2025-09-15 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e6fa74cf-660b-3267-8b34-4e7131880401 | -6.9254 | -46.1647 | 2025-09-15 00:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 296e6c5a-4662-3624-9f64-dfa8b4cd1e32 | -12.006 | -47.7505 | 2025-09-15 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c0c6a707-28f5-36bb-889b-544bce746fab | -5.4798 | -44.6942 | 2025-09-15 00:10:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4a0dd369-6421-371e-9cea-3b8af202f4bb | -11.0807 | -49.724 | 2025-09-15 00:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b4b289d2-ee47-397f-ad81-0f406b003f72 | -7.8861 | -63.7135 | 2025-09-15 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4aa41e6e-b090-3762-b8fa-f60edbcb1fbd | -5.7047 | -49.1998 | 2025-09-15 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 009ddcde-b7ab-397d-aba9-cd99fbc2b32c | -23.7369 | -51.8964 | 2025-09-15 00:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 04e1a35e-0c4b-37ff-b342-1cf1631986fe | -11.78 | -47.5583 | 2025-09-15 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 18cebeab-8303-3bc7-939e-f90cbd429e7b | -7.8756 | -43.5643 | 2025-09-15 00:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 6ba913c8-c716-3686-899b-4601d418ac1c | -8.9073 | -45.5024 | 2025-09-15 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9b2bcb09-9928-3a26-b04f-5c6fe9a1ca9f | -7.8753 | -43.5876 | 2025-09-15 00:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| fe9bb5f3-5d0e-378a-9e64-e62369cf90a0 | -5.6861 | -49.2009 | 2025-09-15 00:10:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 20818180-8fff-3db6-8b62-ff643988d299 | -7.8862 | -63.6947 | 2025-09-15 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 606a504b-6695-3639-bea2-ebee80b968e5 | -7.8756 | -43.5643 | 2025-09-15 00:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 1a066c00-fbf9-30bb-9051-877b2ffca8ec | -7.8861 | -63.7135 | 2025-09-15 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1957ca75-d629-315a-8c94-283b8e5c3777 | -16.4906 | -55.1276 | 2025-09-15 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 409a8638-2852-3acc-bb95-7d916521aab9 | -16.5106 | -55.1042 | 2025-09-15 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| ab12549b-1b5d-39aa-bc06-232288010f61 | -7.8942 | -43.5857 | 2025-09-15 00:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6059202b-d285-38ba-8427-460fc7e60c35 | -6.9254 | -46.1647 | 2025-09-15 00:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9466025b-d95c-3d1a-bbfc-ffff7e4fe7d9 | -10.9365 | -45.5063 | 2025-09-15 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 96e60fdc-d37b-3034-80f2-9922d13690f7 | -5.6861 | -49.2009 | 2025-09-15 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 264c589c-6e0f-3559-b109-e32fba374933 | -7.8567 | -43.5662 | 2025-09-15 00:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 326.7 |
| 53ee857d-ad3a-384b-bd7a-fd75421e1313 | -16.4914 | -55.0858 | 2025-09-15 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| e1d55e09-7f87-362e-9d83-71bb21f09ecc | -17.7632 | -42.6538 | 2025-09-15 00:20:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 6714288c-a3a2-36df-a4e3-37a3bec3659b | -12.006 | -47.7505 | 2025-09-15 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 429b86a7-0893-31ee-bbc8-a21e908c2578 | -7.7025 | -48.8667 | 2025-09-15 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 33222001-b238-34b9-9dda-40ba21b6ebb1 | -16.491 | -55.1067 | 2025-09-15 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 306.9 |
| 2768f88a-4d36-3798-83d7-18e6a9f17b38 | -7.8564 | -43.5896 | 2025-09-15 00:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 488.8 |
| ed2ee169-87d0-3996-abe4-308bf150013c | -17.743 | -42.6588 | 2025-09-15 00:20:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 65d64e75-6c38-39ff-837b-a8c6d6123b7e | -5.7047 | -49.1998 | 2025-09-15 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 25c31808-a6c8-3639-9a3f-daf0ea46e86a | -15.7985 | -53.4582 | 2025-09-15 00:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 97028d96-282c-3a89-9e43-2401385892a0 | -21.317 | -51.6916 | 2025-09-15 00:20:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| 3d2e85a7-3ae9-3cd1-baa4-f83fa3683643 | -5.4798 | -44.6942 | 2025-09-15 00:20:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 14bc4901-6830-3c3e-b706-9215e040593e | -12.58 | -45.636 | 2025-09-15 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 22c995a7-c5b5-342b-b041-01ac5386f673 | -7.8753 | -43.5876 | 2025-09-15 00:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 211.0 |
| f7ffb936-bfa4-3cb7-b7fb-8be383f1638e | -11.78 | -47.5583 | 2025-09-15 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5d7a8ab8-33b0-3982-a55e-406d678e4d06 | -18.71536 | -51.79425 | 2025-09-15 00:28:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d5078669-1e62-315f-afe3-cb75103d9c06 | -21.61149 | -46.82682 | 2025-09-15 00:28:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b9395ff0-81db-3b51-9866-8d2643545fef | -20.86044 | -46.22512 | 2025-09-15 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3ca77ca1-f3ca-319e-bea3-cf4cb2034b6c | -18.54043 | -45.10417 | 2025-09-15 00:28:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a5a7ef6-2efb-3bd0-92ac-8390be553193 | -19.71324 | -45.44657 | 2025-09-15 00:28:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 02caca52-7fc1-3a53-ba31-72a878d3891b | -19.50227 | -44.80243 | 2025-09-15 00:28:00 | TERRA_M-M | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3e913367-8ddd-3cbc-863c-390d40ae7515 | -19.21383 | -42.43005 | 2025-09-15 00:28:00 | TERRA_M-M | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 7a7556c7-4b8f-356b-a6b4-0894f40d468d | -17.23936 | -49.46622 | 2025-09-15 00:28:00 | TERRA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 96cab2e7-9803-3870-b93b-30696fec106b | -18.15557 | -49.20423 | 2025-09-15 00:28:00 | TERRA_M-M | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| cfdcbb1c-d5e3-3eb1-b1ea-e97d4beb4b12 | -17.7521 | -42.6604 | 2025-09-15 00:28:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 176.4 |
| 409cfe36-38a7-3a28-92ce-697d7e18e1b7 | -17.34919 | -46.66045 | 2025-09-15 00:28:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0bce0616-ab0d-32ca-9965-c9f35360a4b7 | -16.67752 | -49.78223 | 2025-09-15 00:28:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 93ca58aa-becd-3c5b-99c5-1837ee868277 | -17.34072 | -42.65611 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b8d16f70-45d3-3100-a62a-41e1b25602cc | -21.30479 | -51.69947 | 2025-09-15 00:28:00 | TERRA_M-M | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.9 |
| b63504c6-3395-355a-b2fa-3b820b49e07a | -16.28208 | -45.68274 | 2025-09-15 00:28:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a55b7228-e207-354f-b74f-197b685e1ce0 | -17.24127 | -49.47224 | 2025-09-15 00:28:00 | TERRA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e98a6541-e966-30cc-be2a-151ff40b5d8e | -22.53142 | -47.26623 | 2025-09-15 00:28:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb1750b8-5716-3a2f-8e79-28f271e10b68 | -17.47663 | -42.41463 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c400dd87-53fe-3182-86f0-ab07df830bf2 | -20.85915 | -46.21559 | 2025-09-15 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 400702ff-55db-316e-9c67-9b33c6ec51ca | -21.62834 | -46.81402 | 2025-09-15 00:28:00 | TERRA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f1ac3ac7-c8f9-30cc-8fb0-a59f63634811 | -17.33876 | -42.64369 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 256a4e7c-1588-354b-91ae-a505461522fe | -23.00672 | -47.55388 | 2025-09-15 00:28:00 | TERRA_M-M | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 1268da4f-df0a-3829-94db-f87ebaf5bb54 | -20.53297 | -46.8712 | 2025-09-15 00:28:00 | TERRA_M-M | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5c0f800a-b07a-3219-ba8b-1df4e5394766 | -16.66591 | -49.77057 | 2025-09-15 00:28:00 | TERRA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 80aef37a-5c00-3a6c-a7d5-912d9ffeeaf1 | -17.16849 | -49.38034 | 2025-09-15 00:28:00 | TERRA_M-M | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e02aa2c7-92a6-3962-a51f-ba8878da772d | -21.92628 | -46.56101 | 2025-09-15 00:28:00 | TERRA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 4313a8e8-3b90-393f-b207-9fc98b303dab | -22.99678 | -49.94424 | 2025-09-15 00:28:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| d621eba2-f027-3d47-9381-f82088706e26 | -19.8363 | -47.88396 | 2025-09-15 00:28:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d5ea204e-0b7d-3861-aa11-a15c0e14ed88 | -21.76361 | -48.12617 | 2025-09-15 00:28:00 | TERRA_M-M | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e37f8c2-e1e6-3d43-9501-1b151690435f | -23.25771 | -49.52215 | 2025-09-15 00:28:00 | TERRA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 3347b76b-8bde-3e4b-9c8d-d662ed847c12 | -17.51157 | -51.41698 | 2025-09-15 00:28:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a381c92b-939f-3eca-a0f3-19dfe8f5ac9e | -17.76288 | -44.51088 | 2025-09-15 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7759e1f-2db5-348d-8718-25a37a4efd27 | -17.00027 | -45.8779 | 2025-09-15 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 885aa5a6-70ad-3902-933b-901eed8136fa | -17.75401 | -42.67275 | 2025-09-15 00:28:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.6 |
| f74c7936-5b73-33ce-aed4-0877d968584e | -22.02594 | -47.39859 | 2025-09-15 00:28:00 | TERRA_M-M | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |


[Clique aqui para ver as próximas entradas](README2.md)
