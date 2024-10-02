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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c80a60a6-309f-3b35-b2ac-1f23da1d65ea | -16.14223 | -55.41996 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e351b5d7-d645-3685-a9cd-4967a8c8cd94 | -16.14223 | -55.4123 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0514d4ae-6f84-3787-9410-29a8464c1656 | -16.14098 | -55.42156 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd234499-42fc-3664-a9ad-4ececf3d432f | -16.13849 | -55.41895 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47978e1e-6736-379c-982d-3e5731b298e3 | -16.13027 | -55.42216 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e12a827-d491-339e-b4d0-6cb9dc53b562 | -15.50397 | -55.75401 | 2024-10-02 05:12:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1aebfae6-c3ac-3d58-8113-567357a29817 | -15.38034 | -55.8391 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbd04f56-20a5-380e-bd4d-11fc99b2e6b5 | -15.37973 | -55.84341 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6181d5a5-b1ee-3b03-943e-052e674dc84d | -15.37912 | -55.84775 | 2024-10-02 05:12:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d862e8f-a39c-38b7-80e4-7f86c99c1ca3 | -15.37727 | -55.8342 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| db265953-09c7-3f02-af97-52e4dafdda8e | -15.37544 | -55.84717 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e1518b2-ab61-3894-bc94-8195c717cfda | -15.37419 | -55.8293 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75c1348b-81eb-3f62-921f-add7103705e1 | -15.37358 | -55.83366 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 705763e3-1228-3e61-b368-ecbc86e7b4b1 | -15.37176 | -55.8466 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cc60f68-829f-30f7-81c4-57ceaaff6698 | -15.36991 | -55.83302 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5dea6c37-540d-3c28-93bf-d001467422fc | -15.3693 | -55.83733 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9e361a09-fd63-371d-86c8-f2d3a7f6ba91 | -15.3681 | -55.84586 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c3e537b-163a-32e7-90c5-e4702b01a24c | -15.36506 | -55.84074 | 2024-10-02 05:12:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5c4b6e8-3cad-3aeb-8f3a-ac87f2cb2c68 | -15.14122 | -55.82069 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea080242-8e6e-3142-9cc9-dbb4a2a2d64a | -15.13569 | -55.8334 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f360348-0505-36ff-9f1d-ef78e920a225 | -15.12893 | -55.82805 | 2024-10-02 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b85a4e5-2312-32ef-baa0-c641e9a17aab | -16.58855 | -55.93475 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 85a44e54-72eb-3616-8d52-d4f5de41891f | -16.53006 | -56.02791 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7b7a1b66-3f3c-341d-adf3-caee2b5dc74d | -16.58419 | -55.93876 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 20c44e47-df56-3b7e-9fca-93f00bb72639 | -16.52636 | -56.02736 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9118d446-642b-3ce6-b924-8d1ed99123f5 | -16.14598 | -55.41329 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a815750b-56f0-3185-a479-ad4a4f3cb157 | -17.22179 | -56.17138 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a008e8ec-1574-32f7-96e8-00c3a6732b56 | -16.14288 | -55.41534 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 743ce872-11cd-3ab9-8c6a-65470bdbdae8 | -16.14161 | -55.41692 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23e2e900-1a74-3657-a238-78b1e8b0fb61 | -16.13914 | -55.41432 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23567032-eb98-342e-98f0-b1f71b561787 | -16.13785 | -55.4159 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a8713d6-1956-30ec-9db6-0589a2e88fe7 | -16.13782 | -55.42371 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34cd6d7c-65f3-3aef-927e-c5df45e23604 | -16.13722 | -55.4206 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d77a0916-95ae-310b-93ce-6d25109551ec | -16.13472 | -55.41813 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 843146ea-65f7-3bde-8d46-2b90cbe4f874 | -16.13405 | -55.42292 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d244f823-aff6-3f18-b685-ebd46192ebb0 | -16.13094 | -55.41738 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1edec63e-1e2a-3943-8006-1bc959bb295b | -16.12715 | -55.41669 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9d23de9-fd35-3c6e-9108-5e0b8aa61d33 | -15.90209 | -55.40514 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a730905c-be97-34bc-82b6-dbcf7aa36465 | -15.89826 | -55.40481 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98cab166-1465-3143-9936-0a67c7613181 | -15.89511 | -55.39957 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e0680ea-8397-3a82-9b6c-9c2ea3163fcd | -15.89129 | -55.39912 | 2024-10-02 05:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78297feb-6a4e-33fb-9255-7746bd9f4cdb | -17.43858 | -56.21381 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4401890e-a1df-3025-a3dd-10261992355d | -17.23104 | -56.18666 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 8d6ae522-a854-3aa9-a1be-a46cbba8b839 | -17.23043 | -56.19118 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 8e3d4954-3021-3de0-872a-b14342decaba | -17.22982 | -56.16796 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 78d55b65-decb-3c3b-8432-075a876bd8c2 | -17.22863 | -56.16563 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 69d72806-abfe-36e9-a75a-82ce265bb94e | -17.22798 | -56.17017 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 90615e6b-74cb-378b-8ebc-483a879bffbe | -17.22734 | -56.1861 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 449ccf84-95f6-372b-ba47-4e660bf38733 | -17.22673 | -56.19062 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bdb03ac3-3019-327b-9407-1ae43d9f0aa1 | -17.22673 | -56.16285 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0cc75192-0216-3bb6-b6f9-f4b3904ca8f8 | -17.22605 | -56.18374 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c8d70d62-340b-3ffd-a2c1-f5e8729866fc | -17.22549 | -56.17194 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b4350931-f422-3e54-8ef1-31ea70f6c2f7 | -17.22541 | -56.18826 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 96e4b196-bdcd-36b7-8fee-9eaa51ca0878 | -17.22492 | -56.16507 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5e80a7df-5e77-31ed-9197-b925f932932f | -17.22477 | -56.19278 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 75078d57-3b0d-3fd6-9b32-2a7683d853ef | -17.22364 | -56.17414 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 170de04f-e258-3097-8d70-d4cb22e4892d | -17.22122 | -56.16452 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f224d1e2-edfd-3c60-acc9-fb2b08f78a65 | -17.22117 | -56.17592 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b19422ff-fa4a-3919-8559-74f8ebc84134 | -17.22107 | -56.19223 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7561a191-5e60-3907-a86b-1523cc0bcd88 | -17.21933 | -56.18951 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 272a8ebd-8fff-368b-91eb-807962cbec27 | -17.21929 | -56.1781 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ef243bcf-db80-3f6a-a295-960483673fca | -17.21801 | -56.18715 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f41bd965-7d86-3cf0-8ee7-617326e87126 | -17.21747 | -56.17535 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c5448754-9832-3a42-b6ff-d726123ec82a | -17.21688 | -56.1685 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 814fa7f8-23a2-3e84-9d69-0e5d0395e3fe | -17.21381 | -56.1634 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4ad0fa98-2ea1-3642-aa10-6412970dc4b5 | -17.21317 | -56.16793 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bd6d9ac7-ae51-3ddd-a820-2dc83334bcdc | -17.21139 | -56.15377 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 050f16e7-18e7-3bd6-8118-72b440ac8c86 | -17.21075 | -56.15831 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 16950acc-f6fe-3c94-8c56-47b87e5a297e | -17.21011 | -56.16284 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 077331ed-4e6c-310b-b940-b406f1024ff3 | -17.20947 | -56.16737 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7b01dbc8-6d92-3584-a643-eb0a4e4931d0 | -17.2087 | -56.19961 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6e133147-6d14-3ba1-b1b5-e4a72f9636cd | -17.20768 | -56.15321 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 379c064b-982d-3d89-9def-1193257aee03 | -17.20704 | -56.15775 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 26fab041-0f98-319f-ae17-0e9eed90b538 | -17.20641 | -56.16228 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 70182ad8-b8c1-340e-b499-f28f082ff679 | -17.20577 | -56.16682 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| de36f075-853f-3fea-9837-18fead48ac7c | -17.20398 | -56.15265 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 258c8999-fe46-3003-80e5-86c0993430d6 | -17.20334 | -56.15719 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6ae349da-a292-39da-86a7-32be52f328bd | -17.2027 | -56.16172 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 45ed1fee-d8e6-38e8-9b5d-38a5e99a5ba7 | -17.20206 | -56.16626 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0238c84b-603c-300e-bb6d-e9da8230ae49 | -17.20079 | -56.17533 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a017d901-c1d9-3954-a9f0-99ddec82b2f6 | -17.19964 | -56.15664 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1cd5a82f-4c12-3aaf-a438-0f2882da6c8f | -17.19836 | -56.1657 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 24a85377-85ac-3689-9556-0b056d28560e | -17.19709 | -56.17478 | 2024-10-02 05:12:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0c0f0669-ec7b-38c5-8446-646b2ce9e962 | -17.20949 | -56.23412 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a737ddf8-257b-3ca4-bf8a-f73b8b68ca9a | -17.20888 | -56.23861 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1bb93995-b26c-3a7b-9550-9ab4022f8fe3 | -17.20792 | -56.23171 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 60e7656b-18c0-31a6-8fe0-63aa4faa3321 | -17.20728 | -56.23619 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a4bb1b67-c8a6-3432-929f-3d1388cbe5ae | -17.20665 | -56.24068 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0a2e05e9-e720-3d26-9ba7-db402aa820bb | -17.20564 | -56.19454 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2b3572d3-09b0-3268-be0e-a2e67bc72316 | -17.2055 | -56.22216 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f2de5cf0-1e5d-390c-a88d-b97eddadd399 | -17.20487 | -56.22666 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1b8cf268-afda-3922-90f9-e296a1723f64 | -17.20423 | -56.23115 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 557edbe0-28f1-334e-a664-2db81968a04d | -17.2036 | -56.23564 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3b2cece0-d64c-398a-b3d7-7d1f1a9b62e2 | -17.20347 | -56.26312 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5b666328-34ef-31f7-80b9-37cdc5f1ebfa | -17.20296 | -56.24013 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a0e97544-4c94-35d2-af29-ea4422431795 | -17.20245 | -56.21709 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a4024f98-b9f3-35de-8919-24d61416efc0 | -17.20232 | -56.24462 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 47c8d52e-8424-3e48-b532-0daeec0716f2 | -17.20194 | -56.19398 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cbe9a4a6-d39a-3ca7-ac30-eb37f721c7a5 | -17.20181 | -56.22161 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d0929251-4c4b-39cb-b4d2-7d34d35ff322 | -17.20118 | -56.2261 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README141.md)
