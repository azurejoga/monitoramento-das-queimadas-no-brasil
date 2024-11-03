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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d5bd030-8d3e-3ffa-bcbf-16b1c470034a | -5.51553 | -37.99965 | 2024-11-03 03:27:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5f0dce6d-c5d0-393c-8a1a-ada21f4c8bfa | -5.51542 | -37.99791 | 2024-11-03 03:27:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5153b1c3-f6f0-3317-aeb5-cb9e8e15eaab | -4.24906 | -43.42067 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a0b91493-3948-31b6-9e95-a9a3642073cd | -4.24894 | -43.41994 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1b2c246b-92c2-3bf0-9539-91ca2a01ecc4 | -4.24815 | -43.42574 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f0e5d6fb-ffc6-3971-b6f6-0270169c28fc | -4.24807 | -43.42497 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3a5456a4-7e11-33a8-b3a9-922fe580b4fe | -4.24723 | -43.43089 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f5388f15-77c8-32a6-8638-354639c2e03a | -4.24719 | -43.43007 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a5deacf1-0475-3fff-b255-8e9cdc3de329 | -4.24624 | -43.43638 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71fdb34d-1885-399d-8123-b6f5ae69ce12 | -4.24624 | -43.43558 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d01465ec-3e16-3592-a654-25a6befc5613 | -4.24351 | -43.41473 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 46b87d75-410e-3426-8650-71be16b7e681 | -4.24337 | -43.41388 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5595da06-f372-3c3c-be3a-46b1c3e40d65 | -4.24259 | -43.41983 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6b1806cd-9b41-3d10-84e6-8a8df9ccdb21 | -4.24248 | -43.41906 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d414bbd0-4a50-3c8c-8b57-170cfabf2cd6 | -4.2417 | -43.42479 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 17887216-2fa4-371b-b802-d8b7dfb3b88b | -4.24162 | -43.42401 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 42330dde-83ae-3e03-ab34-45862bc13917 | -4.24082 | -43.42969 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 936b8254-e5f1-3b06-b83c-1e019425a954 | -4.24077 | -43.42892 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b409decd-d8b3-3a55-bf48-aedd21eec449 | -4.23989 | -43.43488 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b5cdafd-526c-34de-9adc-b676a641360e | -4.23988 | -43.43409 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1307ace9-ad11-38d7-9f60-99f574cc33e6 | -4.23695 | -43.41277 | 2024-11-03 03:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f37e076-8914-3ad3-b898-50dac7315721 | -4.23604 | -43.41802 | 2024-11-03 03:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a1afa87-9bee-35fe-937e-4125d69fa238 | -4.23517 | -43.42302 | 2024-11-03 03:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02ca2aa7-a66b-3d01-a400-e5792cac14b0 | -4.22874 | -43.42196 | 2024-11-03 03:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35b8fb8f-bfbf-31fa-bc62-3144cfc92a77 | -4.22319 | -43.41581 | 2024-11-03 03:27:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2330e0b8-6017-349d-a89c-0d011169b7da | -5.9413 | -44.71476 | 2024-11-03 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8ab2dbd-4b8e-35d0-8de7-9791dffa7b82 | -7.24751 | -44.68463 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf95f01-a452-3199-af8d-685b5b4ffef1 | -7.25045 | -44.68567 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f011ab4d-bbbf-303b-b484-059f665dca2c | -7.25412 | -44.68583 | 2024-11-03 03:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bdb1b1d-e2f9-3337-836b-b46f27f59934 | -9.62841 | -43.82736 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5725a4e-0d7f-37c0-8415-d2a6a6126918 | -9.62782 | -43.82458 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00f1d236-f1e6-3502-94f2-b095d368fd94 | -9.62323 | -43.8219 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22c8d77f-2ebe-3498-85ac-562eb7ffe08b | -9.62178 | -43.82345 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1800dfc3-31f6-33d1-b458-bfb70dd028a0 | -9.50382 | -40.53726 | 2024-11-03 03:29:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| acbfd7d7-be64-3490-91e1-f6eba1c251cb | -9.50039 | -40.5376 | 2024-11-03 03:29:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0502ea33-05f7-35c8-aa1f-766f27e9cb91 | -9.49894 | -40.53637 | 2024-11-03 03:29:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b71c337d-15fc-3654-8d7f-1469bcb4bb4d | -8.32886 | -42.05284 | 2024-11-03 03:29:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01fab5c7-dbb6-37e8-8fdc-e62396e165ee | -8.32336 | -42.05175 | 2024-11-03 03:29:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6da82b93-1718-3fed-9067-a2ea47a00734 | -8.15907 | -43.52655 | 2024-11-03 03:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e6c9779-eecf-3e63-9dd5-ca750fdcccea | -8.1582 | -43.53125 | 2024-11-03 03:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cfa9f31-4911-33e6-a77e-be94d7c2f383 | -13.71563 | -43.2914 | 2024-11-03 03:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 930d4a12-7d85-3048-81bd-0c0ddcf6b92d | -13.71504 | -43.29227 | 2024-11-03 03:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 900f553f-b85b-38a5-8d87-8417de47ca95 | -13.7149 | -43.29498 | 2024-11-03 03:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b6f3c8bb-dd9c-3fac-be83-c3b2cf3928a5 | -13.71434 | -43.29586 | 2024-11-03 03:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 196390a1-925a-38a5-bf5d-19e582c34151 | -13.42271 | -43.13784 | 2024-11-03 03:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5b481d7-f4dd-3840-9f72-932cc29a1675 | -13.42123 | -43.13776 | 2024-11-03 03:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77dcbbd6-cceb-31fd-80a8-81795a4977b9 | -12.53985 | -38.52784 | 2024-11-03 03:29:00 | NPP-375D | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| aa4cffd4-af9c-3dcd-908a-167d1f660fef | -12.22661 | -38.29826 | 2024-11-03 03:29:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a842d51-539a-377f-8a66-8ca616b7b110 | -12.22599 | -38.3018 | 2024-11-03 03:29:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ed6d611-86e6-370f-af05-e039938d7c44 | -11.64637 | -39.10378 | 2024-11-03 03:29:00 | NPP-375D | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc85016d-67ba-3db9-9cd2-3a3e3b99bcfc | -11.37228 | -40.36817 | 2024-11-03 03:29:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4218cfc8-db46-3642-9988-746c4cce2f6d | -11.36925 | -40.3694 | 2024-11-03 03:29:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 752343d8-3702-3bca-9df5-321bdb58b8cf | -11.36761 | -40.36726 | 2024-11-03 03:29:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 035b9c80-0d7e-3700-82b1-e27de3741229 | -11.06769 | -39.36358 | 2024-11-03 03:29:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0133f232-4f2f-323e-a578-720261fcc0b8 | -11.06691 | -39.36794 | 2024-11-03 03:29:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 64a92b53-c644-3f06-b7f4-5b4c738fd0f1 | -10.41535 | -41.43717 | 2024-11-03 03:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f78f635-940a-3511-b282-7b54e92376f6 | -10.41211 | -41.4367 | 2024-11-03 03:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 395375b8-96a3-3631-ab92-a0c551a338ea | -10.41028 | -41.43602 | 2024-11-03 03:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d1821e38-c232-38cd-a727-25cca4ecd464 | -10.13242 | -36.26151 | 2024-11-03 03:29:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f23841b3-260b-38a0-ae58-14673ec1b763 | -10.12968 | -36.26297 | 2024-11-03 03:29:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93e9be30-9514-3866-849d-f425c148f479 | -10.09042 | -43.32827 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c13b272-d23b-32c8-b773-a7b8516c6864 | -10.08384 | -43.33123 | 2024-11-03 03:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 836fed88-9e95-3ec3-b753-80e5671a597e | -20.08134 | -40.18173 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f3081f60-8614-3641-aecd-f90544dce91c | -20.07929 | -40.19252 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8efbd490-7e7a-3c8b-b90b-a34a9242b7b4 | -20.07706 | -40.19599 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 122f57f6-3ac2-33bb-bba7-5e53d5c6c3c0 | -20.07533 | -40.19168 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 796859a9-fbc2-31e5-aebe-0d9c01fdd1f6 | -20.07309 | -40.19514 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e862db16-e9fc-37b7-956e-d5e679eb8cf4 | -20.07136 | -40.19085 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 69870609-1cc0-35e1-b4f0-c6c7123a0194 | -20.07033 | -40.19624 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6846d74b-232a-3ed7-8a19-5a265d2ea72a | -20.06912 | -40.19431 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d141165a-effb-3248-b426-db09a7a9c56c | -20.06444 | -40.18384 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dd3f39f8-1812-3046-a01d-8ea31cc64f8a | -20.06217 | -40.18727 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eb8969a3-9216-3300-9179-265a4223b57a | -20.06118 | -40.19268 | 2024-11-03 03:32:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 166ba87a-a4cd-3e33-be49-f47c9de58d5b | -16.18121 | -43.64561 | 2024-11-03 03:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44822c93-1ffc-3d9e-899a-c8f8ab1ade75 | -15.78871 | -43.50231 | 2024-11-03 03:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2800e6b3-5d03-3ee3-9803-044ec24b3fab | -15.78801 | -43.50575 | 2024-11-03 03:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18c928ee-f6ba-33b7-bea8-48a1a268f2bb | -15.56397 | -42.87114 | 2024-11-03 03:32:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc362daa-a685-304c-b341-9732dbd52db1 | -15.55896 | -42.86962 | 2024-11-03 03:32:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2810ac26-a739-363b-b6e1-4baa9b5d77be | -15.3835 | -43.12279 | 2024-11-03 03:32:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d5a854f9-f262-31b0-bbaa-fba5b46926fa | -15.32821 | -39.39806 | 2024-11-03 03:32:00 | NPP-375D | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c904d867-c858-3909-8930-b351b162764e | -15.21849 | -43.00236 | 2024-11-03 03:32:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5e808a3-6be8-3245-b5a5-38ba75592225 | -15.21791 | -43.00521 | 2024-11-03 03:32:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5f994f6-a730-39cd-888c-b5e588c0bb21 | -15.06569 | -43.27729 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 106bd4a9-eabf-33ae-94da-0c994aa52b35 | -15.065 | -43.28069 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c4773400-9a38-39c4-b6f3-0cf55dc6c237 | -15.06431 | -43.2841 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9192900d-058a-348b-9639-d66b23534958 | -15.06041 | -43.27614 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5ac1b59-f711-3e4e-a0f0-0c11c9a18e25 | -15.05972 | -43.27955 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2ef61907-107f-37ec-9579-94a9aa110a01 | -15.04545 | -43.22431 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e7b7c78f-33e0-3aaa-8129-182e0e47e6be | -15.04361 | -43.22322 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 93873ade-e9ea-3b75-ac87-070e1046df16 | -15.04293 | -43.22658 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ca98d5b7-2b45-3ef8-9e34-01ba5b2a645f | -15.04019 | -43.22314 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7e28243e-de4e-3b01-9259-339806f63f7f | -15.03835 | -43.22206 | 2024-11-03 03:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| aa40fdfc-09d0-3537-822e-9deec6df8e05 | -14.98746 | -43.66424 | 2024-11-03 03:32:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76b3f7e9-744c-3c8f-aa53-61f9ed99f505 | -14.98673 | -43.66783 | 2024-11-03 03:32:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc37b3b2-93d8-3a01-9fd4-e8745e00e848 | -22.34738 | -44.05724 | 2024-11-03 03:34:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f78461a-6a69-3cfc-aad7-57b0f51c2949 | -22.34615 | -44.06298 | 2024-11-03 03:34:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5a19ad77-435b-374d-a242-c0c161a93433 | -1.2755 | -53.4138 | 2024-11-03 03:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 5bc4b96a-b15c-3da7-90ac-acbbfb4d1b30 | -1.2755 | -53.3936 | 2024-11-03 03:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 057079e5-d749-3ac2-9bbd-1b3c7b6596f7 | -2.5796 | -53.3927 | 2024-11-03 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| dffff2f4-bda8-3ee9-a47e-29c8cd541c90 | -2.5797 | -53.3724 | 2024-11-03 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |


[Clique aqui para ver as próximas entradas](README22.md)
