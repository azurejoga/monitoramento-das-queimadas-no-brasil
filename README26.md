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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a42095-60c5-3e45-b9cd-315d75349925 | -29.80422 | -52.12241 | 2025-08-15 04:08:00 | NOAA-21 | VALE VERDE | RIO GRANDE DO SUL | Brasil | 4322525 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee675ea4-6b6a-3017-a84f-d809675f1347 | -28.73127 | -52.35608 | 2025-08-15 04:08:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 59868ed1-23b4-345e-a72f-39ea65846b76 | -25.00574 | -51.10509 | 2025-08-15 04:08:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fcf8ebe-fad5-3b7c-8396-d3b40d8e7e9d | -28.60525 | -50.63107 | 2025-08-15 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a302766b-4ba9-32d1-a535-af7abcaeab77 | -28.60429 | -50.63492 | 2025-08-15 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e887f344-d76c-34fd-857b-6e666d18b284 | -25.00148 | -51.10415 | 2025-08-15 04:08:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0ed1df9-17a7-3be8-9b36-350324dc430f | -11.3468 | -55.4124 | 2025-08-15 04:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5cecbe6e-3752-3a89-91b0-623fa03ea63d | -6.9303 | -59.5305 | 2025-08-15 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ae71ad77-7149-3fbb-9c3a-847b01e336ba | -9.4994 | -60.5278 | 2025-08-15 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 93bc94a5-f6f1-388d-8205-6e18912fab06 | -9.1706 | -59.6762 | 2025-08-15 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 874d0bb4-0023-3385-9bce-51bcf06fca5c | -9.4995 | -60.5085 | 2025-08-15 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| be105791-6f15-3cdd-a9fc-a6f45e7fcadc | -6.6945 | -58.8259 | 2025-08-15 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| dda20202-4d9e-37f0-91d5-d681b610c4ca | -6.0806 | -59.9657 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e4f8357f-93ad-3a24-afb8-009f68e96fce | -6.0807 | -59.9465 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 1627a1ad-d781-3976-a5a0-7bec428e276e | -6.0623 | -59.9472 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a4f78dea-5f2b-3a8f-b3b1-b76d0e07eb52 | -9.4992 | -60.547 | 2025-08-15 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| de6d1b92-372e-3724-844e-912412038f89 | -6.0991 | -59.9459 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 38b85dc3-7d2b-311b-9f67-c9ab03b69af5 | -6.0808 | -59.9274 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cf5a705c-3d84-33d9-8654-bcb7b7576778 | -9.1708 | -59.6568 | 2025-08-15 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5a720a31-92e1-36f9-aa41-4191313ef1f1 | -6.0622 | -59.9663 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9da5e486-fe2a-39b2-b9ae-799b431cfc89 | -9.1894 | -59.6558 | 2025-08-15 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 0468f685-4907-320a-8f27-d04172dfe0c5 | -5.455 | -60.1391 | 2025-08-15 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 68eadeb5-c18e-39c7-bdff-9ba99c7c4bdc | -6.9303 | -59.5305 | 2025-08-15 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f32d9c93-ff6f-3555-a85d-5f946e19dab8 | -11.3468 | -55.4124 | 2025-08-15 04:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 92cdcb06-8abf-3ce9-a7c9-fd8b7f445db7 | -9.1894 | -59.6558 | 2025-08-15 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 47206cff-7971-3859-a76a-c7b865162337 | -9.518 | -60.5268 | 2025-08-15 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 59582f7f-ea99-3e47-8f46-83edc319a449 | -9.4992 | -60.547 | 2025-08-15 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a1b4c2fe-e712-302c-bcd9-717352050a9e | -7.5291 | -61.3444 | 2025-08-15 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c39a08c9-4dcf-361a-9c97-a07e5183a865 | -9.4994 | -60.5278 | 2025-08-15 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 009b217b-bbc9-344f-8d41-668f839f95dd | -7.5292 | -61.3254 | 2025-08-15 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a605b961-2681-3839-a217-286f989e78c4 | -6.6945 | -58.8259 | 2025-08-15 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 08d52b27-2b3a-3059-a83d-8d40070786f8 | -9.1708 | -59.6568 | 2025-08-15 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 97cf6b69-329b-3599-b74d-5927bd8bd319 | -9.1706 | -59.6762 | 2025-08-15 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3748273a-311b-3af5-a276-abf7433d9723 | -2.53897 | -47.71585 | 2025-08-15 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 464ff63c-139e-3717-9961-e4f1934aed5e | -2.30893 | -46.99363 | 2025-08-15 04:25:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d6c7509-7c7a-3a6a-959a-b16fe2fa73d6 | -3.42781 | -40.4145 | 2025-08-15 04:25:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29261ca7-e214-35b3-bf83-ee3ef0360d25 | -3.49324 | -43.31231 | 2025-08-15 04:25:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ae047d4-1f8e-3fb1-993a-ac7c77185e08 | -2.53959 | -47.712 | 2025-08-15 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7c657e-3ebc-36d5-aa56-dc95868d6796 | -2.63654 | -44.2612 | 2025-08-15 04:25:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c20830a7-4b56-3b18-9937-2cec97b05f64 | -2.53546 | -47.7153 | 2025-08-15 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da200410-1487-3bdb-be60-3ce96c6614b4 | -5.89265 | -43.81344 | 2025-08-15 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f26ba2a2-be67-3e68-9c42-6c2f9febddac | -9.02984 | -40.52705 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8659e46c-59d8-3adf-b670-8638cff419c8 | -6.09181 | -59.94851 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b44a436d-e786-3a21-80d6-25b0310ca74b | -5.36432 | -41.24174 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7c699e3-4792-3805-bc49-686058302510 | -9.85051 | -47.82585 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9c14e68-70ec-3a73-a368-6dd536ea52ff | -4.29898 | -48.06237 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 984fd200-f8de-3e6d-95cf-7ad3c23e17de | -9.85204 | -47.82649 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48f3e522-3610-36b4-afee-478f6649a445 | -8.31251 | -45.01733 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4eff81bc-ce66-3173-b49b-1e1762b1bb3c | -7.1478 | -44.3999 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a48b81f-42b3-32a9-a51d-5134ede5ee03 | -7.06244 | -59.2212 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b665ed2-51e1-3efc-94b5-86dae89d4b1b | -7.38225 | -44.87186 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c06762d5-8559-3435-9d9d-ddd080b41edd | -4.22748 | -47.20944 | 2025-08-15 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e3ee7228-1d58-3b8a-ac8d-f0a3f9a5de70 | -7.39208 | -44.88044 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4b8dab9-8f9f-3de6-9dcc-2e3beed8ca8b | -6.90686 | -45.2104 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3c62b7c-2282-3d08-8d31-be12a8208d94 | -6.94426 | -60.00514 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd52b57d-d480-346b-b0b9-db251658df0b | -4.59084 | -43.32481 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f799e5eb-f60b-39e1-aa55-9888dd0ea340 | -7.29173 | -43.82762 | 2025-08-15 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fc49f35-e905-3e60-9415-6d51835b2f0f | -6.91545 | -59.14221 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0263d14-a3fc-3f39-bbcf-2bfb895bdaf5 | -6.90755 | -59.14708 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f4ce674-92ee-3616-b701-4b0f6b2861fd | -6.92568 | -59.14942 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a41ebd20-e33e-3e72-82e7-ef5c33f15136 | -6.35137 | -43.3809 | 2025-08-15 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74b26d56-b18f-369e-aefa-dcce76d7b9b0 | -7.07458 | -59.20573 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06cb015e-1387-3357-ac8e-e18622b7c40c | -6.21201 | -45.92905 | 2025-08-15 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9e0e9a1-c786-365b-9785-42aa4e472130 | -7.07791 | -44.94795 | 2025-08-15 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68791b68-bb79-3b35-8b1a-6cc7e22266a9 | -5.32175 | -45.21963 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d00fc880-2a72-376d-8524-7d71577bc585 | -7.23774 | -44.36412 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02f1b77b-c1a0-3e05-b4b7-0481fb12e154 | -8.31534 | -45.0215 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 297a4618-42a1-39e5-8005-0528ae33b23a | -6.1003 | -59.94245 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a9bc3b9-a47a-3248-9ab4-226d09884807 | -7.73837 | -43.9684 | 2025-08-15 04:27:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ebcb92-2464-359f-bd1f-7e3fcf45bf06 | -8.30628 | -45.01262 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cc8ed32-d06a-30b9-8c63-a45f2d9c611b | -5.79354 | -43.6143 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f0daa73-6f13-3382-afcb-beb63bb76cfb | -5.54455 | -43.89708 | 2025-08-15 04:27:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 494c8fa7-ea8c-3e3b-b37c-495a1295263e | -7.0095 | -43.8616 | 2025-08-15 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb15c79-7f34-32a3-8600-4031d6d6b647 | -7.15697 | -44.40895 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae851697-2b35-3d15-be5d-c615b6541be3 | -6.22181 | -43.33843 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ccabe0c-6f07-3fb3-b3d6-fe27656ffcd4 | -9.00683 | -48.7263 | 2025-08-15 04:27:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3d95427-bd87-3986-972f-4f9bb575665c | -8.51845 | -43.32411 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b6250531-deba-32d5-9ab4-fabc1cde1554 | -5.23131 | -43.19264 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eef311c1-ce63-3d98-b148-e67f872d3990 | -8.52224 | -43.29844 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23495ae4-c9d9-3634-bbf4-16ad93ecf799 | -7.0838 | -59.21894 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2ad97a0-ebf9-347f-8bf2-a320cc27c3f9 | -9.19238 | -45.32999 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 894e2bbb-d22c-3e2c-b16f-2c3add9748a0 | -7.86347 | -48.23316 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a678dc8-bcfa-3245-9cb6-6e361910241d | -6.22423 | -43.33738 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12c3f8a0-2134-3319-8542-e8031130ad3d | -7.39263 | -44.87681 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66f92ae6-1a4c-33d7-af26-6f413c7c38e9 | -6.69494 | -58.83418 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7194cba-0735-3ce3-a43c-ff5364ac4ae6 | -7.0213 | -44.29683 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f0cc41f-aec7-3ce5-86dc-7ab0a5c60fd1 | -3.31758 | -48.72179 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88d935a8-3bdf-36c9-9983-8f0e68ed96a1 | -6.33721 | -42.80502 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f37fba9-5392-37c5-96b2-a53c27f4b557 | -7.09278 | -44.42196 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb467524-3143-39a6-88b8-7b14ed185dec | -9.21269 | -45.33315 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a60e13bb-1b6f-3cf2-8192-35bc87a6c091 | -7.02159 | -47.45512 | 2025-08-15 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af2cebdc-134a-3455-ac36-b093e2d16f14 | -8.89865 | -48.48654 | 2025-08-15 04:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87de509b-4425-31d1-af05-ab396ace3473 | -7.14668 | -44.40728 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f038b555-b8da-37d5-8af7-6645cb0f37c2 | -6.10871 | -59.91465 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ff1ee9-2408-3ec8-992b-c9c3d59c61bf | -6.21328 | -44.19637 | 2025-08-15 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 872a4672-1258-3c83-9077-c37bc0037104 | -6.11455 | -59.92268 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fa30570-d753-3fe1-b1c8-ede447899106 | -6.22007 | -43.34089 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45ad38dc-8556-3057-aab5-f731b1d3bd5d | -9.19859 | -45.33469 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 756e4536-86f9-31b4-b841-d7b7cd143cff | -9.84275 | -47.81 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94c4ad20-0396-3bf9-986a-6b7267ff2ae8 | -7.74064 | -43.97691 | 2025-08-15 04:27:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
