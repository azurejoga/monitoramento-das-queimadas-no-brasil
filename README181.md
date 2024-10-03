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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7330239f-d92d-37e3-9938-4ca4d4fc41a0 | -7.78212 | -50.23068 | 2024-10-03 05:27:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| efa403d4-4148-3b49-aa86-c6a9d7402e8b | -7.56596 | -49.17454 | 2024-10-03 05:27:00 | AQUA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e9c8234a-537a-3fd4-b27a-a452255db9e2 | -7.11592 | -47.87346 | 2024-10-03 05:27:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d29adb0a-fe9f-32eb-998f-a4a97236427c | -7.1146 | -47.88234 | 2024-10-03 05:27:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 57b519c5-0963-3505-ba4d-f2b33546e4e1 | -7.07164 | -48.03333 | 2024-10-03 05:27:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3fc3b205-a555-3e44-9dfc-9a370be774ae | -6.97279 | -49.42968 | 2024-10-03 05:27:00 | AQUA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 97fd48b3-d698-3925-9c11-88bbf0ecfcdd | -6.96514 | -49.42195 | 2024-10-03 05:27:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0fe46371-185d-3258-a4c9-d6f3fcbc47e7 | -6.96375 | -49.43116 | 2024-10-03 05:27:00 | AQUA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 578427b8-78d4-3233-b661-3e6fd9109b52 | -6.67589 | -44.52009 | 2024-10-03 05:27:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 683dc668-49d7-3c90-84ce-6a398185e592 | -6.67414 | -44.53218 | 2024-10-03 05:27:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3051e9e6-3194-3698-b476-6e41dd3f1f4f | -6.67301 | -44.52518 | 2024-10-03 05:27:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0e54664e-6ccb-3f01-b118-e096ad2e362d | -6.64909 | -54.94595 | 2024-10-03 05:27:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 890cb2ca-fb78-30a0-99d4-785f1e9d5c4f | -6.64062 | -54.93703 | 2024-10-03 05:27:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bb636894-fd51-375b-b08d-16b14033ea3e | -6.14819 | -44.12902 | 2024-10-03 05:27:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e29612b3-5c4d-333f-aa71-614ee3d84ba7 | -6.04365 | -44.14556 | 2024-10-03 05:27:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 74aae6ea-ac5a-306b-907b-081fdee75fd5 | -5.08511 | -46.11697 | 2024-10-03 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9433e6d0-543a-3056-b265-970e7396b8ad | -4.79899 | -48.47292 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 01b63929-0ec0-34e8-8beb-d89eec9deb8f | -4.67803 | -45.8798 | 2024-10-03 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| c0969e9b-974e-3de4-b566-aacd8583a36c | -4.67663 | -45.88937 | 2024-10-03 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 51a44ee9-b969-3e80-b34b-11774f6141a5 | -4.66881 | -45.8783 | 2024-10-03 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| cc2aeeef-c8b4-3625-953f-fa21f2b014da | -4.66739 | -45.88802 | 2024-10-03 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d0ddbd39-4614-3cd0-a842-bd91a91b6841 | -4.65157 | -47.43027 | 2024-10-03 05:27:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cf21d319-d052-396d-9121-624fc6efdd20 | -4.57345 | -48.01287 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 07d88f46-fb0a-33f9-b317-8e08d3dc0e26 | -4.14649 | -48.39693 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 01448fb5-c322-32de-8bb8-51a0eda42988 | -4.10626 | -48.48262 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3a7bb236-da82-3466-8d91-06a3379cab38 | -4.10491 | -48.49162 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0cdb51c2-1444-3d59-8928-400cf283713a | -4.0987 | -48.47233 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 461f26f4-451b-3635-af71-4edf76fdbe73 | -4.09734 | -48.48131 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0a102316-a45d-3d97-a25c-3dba253bc5e7 | -4.09598 | -48.49033 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a7559f7c-b573-3f95-873a-5ef7b9e7db20 | -4.09536 | -51.1102 | 2024-10-03 05:27:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 912f312c-7a32-3d73-af85-a9a97117e80e | -4.09113 | -48.46206 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 281e7944-9adb-3474-b284-1ce60ed586d1 | -4.08977 | -48.47105 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1ab240f3-90c6-3587-9a42-ecdf597a82d0 | -4.08841 | -48.48003 | 2024-10-03 05:27:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e047b535-5b2c-3d70-8f98-a8ea41a70479 | -3.94803 | -51.00277 | 2024-10-03 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d088a8fc-32b0-3bad-947d-1f6c779d06fe | -3.9245 | -49.68117 | 2024-10-03 05:27:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 664c56ee-d3cf-3406-8f03-4154f3d98897 | -3.92299 | -49.69104 | 2024-10-03 05:27:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23277024-f784-39d8-807e-7bafb44043d0 | -3.90393 | -48.35817 | 2024-10-03 05:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2b6ab3ff-ca9b-3be9-96df-93104942b892 | -3.80393 | -47.79676 | 2024-10-03 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 765f8292-e939-3d16-9f58-30ccccc9453b | -3.80261 | -47.80558 | 2024-10-03 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb65e294-778e-3bec-ad53-9d4acbc41126 | -3.75778 | -52.25893 | 2024-10-03 05:27:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 91d36e3b-7294-340e-99af-d4b7eb5fceb8 | -3.70183 | -47.60758 | 2024-10-03 05:27:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2092ef8b-f5cb-36bc-b247-bf378c42f155 | -3.65417 | -54.29866 | 2024-10-03 05:27:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d3b1523e-396d-3bfa-84ff-5c06159c654d | -3.46425 | -47.65931 | 2024-10-03 05:27:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 04f880b6-d485-3621-9da2-4d96298661fa | -3.45731 | -53.97469 | 2024-10-03 05:27:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7ae72302-7d24-361d-af4f-71820d8922a3 | -3.29675 | -51.1073 | 2024-10-03 05:27:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ff3eec4-c1b6-37c3-a5d2-9f5245e34437 | -3.27275 | -49.1097 | 2024-10-03 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87229af7-48b3-3e2b-a81c-4673ec2b44b1 | -3.22651 | -48.92387 | 2024-10-03 05:27:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7d217048-ef5b-3d80-be05-ca8d4b72044c | -3.22273 | -50.78448 | 2024-10-03 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 74dc2d9b-0605-3636-a39a-d6424b74fc12 | -3.22096 | -50.79615 | 2024-10-03 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3a22128c-5dcc-3e54-a466-ca355bfabf13 | -2.95724 | -49.35968 | 2024-10-03 05:27:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8a507bd0-145f-3d61-a67c-7f1ea86d9738 | -2.88591 | -50.70913 | 2024-10-03 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 9c69fd2b-30ec-3e82-95e5-f6af1349cc60 | -2.85388 | -50.71629 | 2024-10-03 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 51115149-bb5e-35cd-b917-329f670051ff | -2.79624 | -50.28582 | 2024-10-03 05:27:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0e0a9583-ae79-3712-9ce4-9b594bc21611 | -2.5403 | -47.22361 | 2024-10-03 05:27:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 63146c29-566d-30a4-9126-06aa144dbe76 | -10.90905 | -46.31915 | 2024-10-03 05:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ad9e65e9-e256-3812-a700-6bbfb1b482f2 | -11.01827 | -46.5009 | 2024-10-03 05:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0a19f1ea-3112-3004-8de3-25c0b20974ed | -11.42831 | -54.30879 | 2024-10-03 05:29:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 93fbc924-06e6-3e75-8c3d-55cbb87443dc | -19.89035 | -42.09298 | 2024-10-03 05:29:00 | AQUA_M-M | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 97e26a55-e174-34f3-acb3-b4a455698f3f | -19.75472 | -44.26186 | 2024-10-03 05:29:00 | AQUA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d20214cc-9651-3348-a398-b1b81cda8fb9 | -19.31218 | -42.59176 | 2024-10-03 05:29:00 | AQUA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| e2a0fea7-d42d-36de-b5f6-71647bbd3d8e | -19.29771 | -42.58821 | 2024-10-03 05:29:00 | AQUA_M-M | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| fb632bc9-fb8a-3d5a-9cc5-48ac5cf4babe | -19.27721 | -43.76709 | 2024-10-03 05:29:00 | AQUA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d0aa3262-109f-3aae-bc2a-d33f157173a7 | -19.03906 | -43.19019 | 2024-10-03 05:29:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 029c9f38-7864-3f58-82d2-07a57cce8bd8 | -14.80998 | -48.79659 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa8eb2c4-90c0-3503-a657-3a6e72fb74a1 | -19.02498 | -43.18974 | 2024-10-03 05:29:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 1d6801d2-92c2-3e5b-98b7-bb8a2b8f1d0b | -19.02259 | -43.21243 | 2024-10-03 05:29:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| c368acbd-1409-397c-92e0-0a7e04b4b582 | -19.02035 | -43.18244 | 2024-10-03 05:29:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| 3995f5d3-5092-3e22-9d5a-55d4cd7c49ce | -19.01781 | -43.20529 | 2024-10-03 05:29:00 | AQUA_M-M | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| 647a3503-9d0e-3db0-97a0-af23116e63ea | -18.87779 | -41.20305 | 2024-10-03 05:29:00 | AQUA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.7 |
| b809d82e-931f-3006-873d-a46d928116a9 | -18.87451 | -41.23725 | 2024-10-03 05:29:00 | AQUA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 6f2f03a9-064e-3ac2-84d9-29c691ca378f | -18.53386 | -42.24617 | 2024-10-03 05:29:00 | AQUA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| 89d4dc3a-1706-3906-897e-6437671db007 | -18.25562 | -50.82069 | 2024-10-03 05:29:00 | AQUA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2e35bf7-6e4f-3beb-8545-ecf0c656acd8 | -17.60057 | -46.96393 | 2024-10-03 05:29:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ebe5114a-2204-3cef-8b60-8f8eef609bb1 | -17.11951 | -47.12865 | 2024-10-03 05:29:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 55503dd8-642f-3d9e-9037-1da0239f8b67 | -17.11794 | -47.14051 | 2024-10-03 05:29:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc5dd37c-8681-3d67-a705-40706b47c5a0 | -17.10941 | -47.12767 | 2024-10-03 05:29:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bc746c02-1176-3e37-9b78-fb9df22f1be7 | -16.17527 | -49.4854 | 2024-10-03 05:29:00 | AQUA_M-M | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c547df34-a6e7-3427-a56f-9f0b0c5d66ce | -16.16634 | -49.48404 | 2024-10-03 05:29:00 | AQUA_M-M | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54c2ea95-1594-3d0a-abd9-adbc64566d55 | -16.11729 | -50.43354 | 2024-10-03 05:29:00 | AQUA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b754a325-b0b1-38e2-b3c5-c7b927fe6c4d | -16.10706 | -50.44123 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| dd6ad051-73c8-3a22-98ad-6c314a458bfc | -16.09958 | -50.43069 | 2024-10-03 05:29:00 | AQUA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 434ec0de-5f6f-3123-9430-3663a29606a3 | -16.09821 | -50.43984 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1580b661-9fea-3020-802d-70c8a62e5270 | -16.09072 | -50.42929 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bcc8b7b3-1372-3e23-91d4-63cef9050288 | -16.08065 | -50.31526 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c0c79f92-df4f-3e15-bf27-662d2d6a4af3 | -16.07928 | -50.32442 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 87fb7825-15fb-3196-98cd-6e26c93156d2 | -15.89951 | -50.16459 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0f4c13c4-0f74-321b-9073-741474143f64 | -15.89338 | -50.14492 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a884af1-924c-32dd-800c-d86ff51d4d15 | -15.89201 | -50.15406 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2f170971-c3af-3182-931f-a8cade14b7b5 | -15.89065 | -50.16321 | 2024-10-03 05:29:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61337f66-25ed-3368-add7-554bbe0360cc | -15.59553 | -48.77584 | 2024-10-03 05:29:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 687db15c-8a75-330f-8453-b453fc3333c8 | -15.58647 | -48.77445 | 2024-10-03 05:29:00 | AQUA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c86e29c0-2c15-3df2-a9a0-ecfb68a251e1 | -15.27532 | -47.50097 | 2024-10-03 05:29:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| effb577e-a2d6-337a-801e-ca5554879469 | -15.25076 | -47.50411 | 2024-10-03 05:29:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 41e26eac-35ec-3f91-afb5-c38bad6e2957 | -14.82306 | -48.76626 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15dfb982-4f5b-389a-9bca-355f39e81a52 | -14.801 | -48.7951 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 42bc500a-29d0-31ae-a119-02aaa30101cc | -14.79198 | -48.79377 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6838470a-30b3-31e3-a2ce-499ff8c531bb | -14.79065 | -48.80299 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 82fe8d3d-4bee-367e-ab17-5935c1aa0be4 | -14.70625 | -48.74588 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 77d89f13-255c-3bb9-90c5-e7159684ac6a | -14.70482 | -48.75572 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 454c648b-6edd-31fd-afea-9b8b6c97decb | -14.70343 | -48.76527 | 2024-10-03 05:29:00 | AQUA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README182.md)
