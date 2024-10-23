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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed72f667-f43f-3492-9423-40768a34e51f | -19.55156 | -56.61633 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 69d47e00-bd85-36c9-bc2f-d17eac552517 | -19.55004 | -56.60462 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a46a560d-6710-3781-ae68-b3e153e945ed | -19.54943 | -56.60832 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6ceb722e-7e5a-329f-93ce-9241efff444f | -19.54884 | -56.65397 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5cd1597c-1903-39a4-b9f8-4dc08dbdc21a | -19.54823 | -56.65768 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d29779a9-e364-31b5-a05f-3d8f4ebe7701 | -19.54823 | -56.61573 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6abfc03d-5ab2-3bce-b01b-55b5d3d36a62 | -19.54763 | -56.66138 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 11e3bcec-e1cb-3540-b677-954c52041f6f | -19.5461 | -56.60772 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e5b00ebd-15a3-3b99-891b-a7b5d7194ee6 | -19.54551 | -56.65337 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 770567cb-9dbf-38cb-bfda-4c316100b8d9 | -19.5455 | -56.61142 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9ec7350b-ef14-3fa2-8b3d-e9ac35379313 | -19.5449 | -56.65708 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b29bb1e-1bbf-3dec-a9ae-941cc1608115 | -19.5443 | -56.66079 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 50f0194d-29a5-3bfb-b68b-e6decbfacb26 | -19.54326 | -56.6077 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 4312c2d0-c417-3dd0-8de3-9a2ea9d8227d | -19.54278 | -56.64906 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a8b72ade-69e0-34bc-b307-ad72c253918b | -19.54218 | -56.65277 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0919fadf-5243-3fdb-85ff-356984d77fd8 | -19.54157 | -56.65648 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ce7a8c21-3c8d-38a3-86bd-0b2523cd0bce | -19.54096 | -56.66019 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| abb0924a-e88a-3f6c-b17c-ca88f22b3dac | -19.53945 | -56.64846 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| addadae3-2e70-31cb-a5fa-28444f3a71b1 | -19.53885 | -56.65217 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9ed0e417-a880-3d13-a967-84b9d84316f7 | -19.53824 | -56.65588 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8dd6352b-2817-3b70-b316-9f65dc4127f2 | -19.53788 | -56.64105 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| ba0abb5a-4b5c-3e4e-9c11-df4253127a48 | -19.53763 | -56.65959 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 3c35bd9d-df4a-324b-8842-986e6692922a | -19.53728 | -56.64475 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3676ecaf-58c2-3a31-8d16-ba1ce313c150 | -19.53668 | -56.64846 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 40d1c00c-ba3c-3eb4-88dc-156d1dfa7bf3 | -19.53608 | -56.65217 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0ed79df2-581b-340e-87ef-6ec8bfd47f0e | -19.53548 | -56.65588 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 35de2c52-e74b-358e-b0af-d76ac56c9de2 | -19.53488 | -56.65959 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2197de03-264b-392f-ae04-3c422995d054 | -19.53395 | -56.64415 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2431f1f2-fd27-33b4-9d9a-c5a58286d4e1 | -19.53275 | -56.65157 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| eb380988-2a7a-31bf-ac3e-ed64ad44d88f | -19.53214 | -56.65528 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 396cbef4-adcc-3a1b-8316-66d53183cafc | -19.53155 | -56.65899 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 80478051-d11a-3133-ac66-7304ad28c0b5 | -19.52881 | -56.65468 | 2024-10-23 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 437a4030-8be0-3b92-88f6-8a65e15a8e09 | -19.52821 | -56.65839 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5dce4984-27f1-3f91-9a78-2138a72ddf70 | -19.52548 | -56.65408 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| efcc8d4e-dccd-3655-a2f7-71c41a3c2a5a | -21.36139 | -57.64598 | 2024-10-23 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 743fc9fa-d58e-3778-9a39-aa321b6153d3 | -22.12326 | -56.99088 | 2024-10-23 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ee8e9125-b91f-39e1-b40e-c9f5c8d65bed | -21.26465 | -57.50936 | 2024-10-23 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d49f52-6bea-396c-b211-618496872087 | -16.42459 | -57.20528 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9cce86eb-aa7b-31fa-8f0c-dded3622b39e | -18.05161 | -57.32226 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1bd6b460-2afd-3698-b76f-55d6facaba58 | -18.05096 | -57.32615 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 21ab04a6-5de6-3776-b5b2-7b90569cb6ba | -17.96499 | -57.23075 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| af989f04-3eae-32ed-be4b-cb98dbd967b3 | -17.96223 | -57.22627 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4bb7c4f-724c-310a-830b-e1f15eecb984 | -17.96158 | -57.23013 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fbd05264-abcf-390e-bd67-a98f756504c0 | -17.95329 | -57.21669 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c49bb9ff-256f-31fb-bdd8-258bc0d3d062 | -17.95054 | -57.21222 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 37a2a7f0-99fd-3974-b132-5dd40bb900f9 | -17.94989 | -57.21607 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c8f0131-472f-3908-88df-2b98fa079ade | -17.94924 | -57.21993 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2a765080-02de-37a3-b803-ebd87b9c7856 | -17.94778 | -57.20774 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1e6bb204-44cd-3051-9452-18e71c956368 | -17.94713 | -57.21159 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d1b0b7c5-4e3a-31c9-9f06-7320b3230426 | -17.94648 | -57.21545 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 755a5852-a6e1-33a2-aa10-ec6358ac6b87 | -17.94583 | -57.21931 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7c6e24e7-39cd-338c-b38a-2b730cadfda4 | -17.94437 | -57.20712 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dfd3e2bd-f124-3394-abeb-039976d41573 | -17.94096 | -57.2065 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 844e7764-05d8-3c65-946f-7157462fd5a9 | -17.94032 | -57.21036 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 559055bc-27a7-3ab6-9db7-faa7beb4a5d7 | -17.93967 | -57.21422 | 2024-10-23 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 11f6cb3c-1c9c-3b29-89ee-fe0462864c66 | -17.78351 | -57.49207 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 59b80c7b-21c8-32b7-8916-7ad9d74d5d2a | -17.77595 | -57.49476 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| e531e93e-a0f0-3ca8-9550-c64e16c059a2 | -17.74317 | -57.40026 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dbcff85e-de88-3529-bacf-34e55fb818a4 | -17.74039 | -57.39572 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f9189810-bb03-3cc9-9f55-d645934a8b40 | -17.71342 | -57.47183 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 681936db-662a-3a53-9173-d09e60cd6517 | -17.70998 | -57.47121 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d3d788be-1654-3709-bf5d-5c1bfb487920 | -17.70308 | -57.46995 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6aab8150-73bf-30d3-9737-67a091b807d3 | -17.70117 | -57.37648 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d3b82d80-4a0e-3752-9ece-5d2030eb7467 | -17.70051 | -57.38039 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 58190eb2-c4c5-3a61-b653-cff9f12c72d4 | -17.69753 | -57.46082 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 400449fc-513b-3faa-8f0e-5f04fdd062b6 | -17.69409 | -57.46019 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 29be1707-d8cd-3c75-be71-28c4ef35a6a0 | -17.69342 | -57.46412 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8e46408a-9a15-338a-8855-a965f20484ca | -17.68309 | -57.46225 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 57ea70fc-63bb-3c2c-af49-838963620b2b | -17.68242 | -57.46618 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c17f3d7e-e5ce-3c02-b5b7-7ee3cbc0c515 | -17.68176 | -57.47013 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 24dfea24-b636-3b3b-a44d-2aa7cc48b471 | -17.68099 | -57.45374 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b234d064-e1b9-3533-b8b0-42b091f0c7db | -17.67965 | -57.46162 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1bc16807-0240-3f41-b0bc-f8e5c1a17e84 | -17.67898 | -57.46556 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f0b1e6ce-f60e-3962-bc1e-b861b7ab5eac | -17.67822 | -57.44917 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| caa7cd4a-b50c-3c8e-a6dd-21b76e0340f0 | -17.67755 | -57.45311 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 4a6725f1-73c6-39b1-8758-6e0c28d2c32d | -17.67688 | -57.45705 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6e94df12-47fb-3237-91a9-2e6b4f852050 | -17.67621 | -57.46099 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cbf891c2-e7d1-3a5b-97d8-1b6aa1a69748 | -17.67554 | -57.46493 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 383df465-5dd3-3d03-8704-642b15bed584 | -17.67487 | -57.46887 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d3135666-6c8f-3fa7-9493-2d3b8e7d6688 | -17.67477 | -57.44854 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e96c213c-fca1-3606-8076-3d9cef779e0b | -17.6742 | -57.47281 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 305e1563-5f75-35e9-a534-fca3425db989 | -17.6741 | -57.45248 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 79244a9b-d90f-3755-aecd-7205fa9e9655 | -17.67209 | -57.4643 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 711234eb-1967-3fc4-a089-e2899dd87ba9 | -17.67142 | -57.46824 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 772f9c05-4b1f-3ecd-97ce-e974cc49259a | -17.67133 | -57.44792 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 1bf49b77-2795-34dd-ba11-d500fcf12abf | -17.67075 | -57.47218 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2ad07cfa-4a7e-3541-973a-9992f74cf3fa | -17.67066 | -57.45185 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 8bf5c7fc-4745-31fb-81f2-d7ee8977d0b2 | -17.03383 | -57.38868 | 2024-10-23 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6df95c14-c14b-36e5-bf7e-6c6b53f1767a | -17.02936 | -57.47782 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4c411168-465e-3328-bf8b-2a658aaec3e4 | -17.02868 | -57.4818 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b7f653f6-a582-32d5-9a36-b8a703caddf9 | -17.02657 | -57.47321 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0ee81781-81b5-32ba-88ea-5262e6ec84fd | -17.02589 | -57.47719 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 83023995-45d0-3d06-832c-32ef439957b6 | -17.02311 | -57.47258 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ddb1cc82-58c6-3fa6-9af6-33eebae97507 | -17.02168 | -57.46003 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6959cb06-f586-344e-9a6c-ff632fce9080 | -17.021 | -57.464 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| da594386-54ca-36df-b79b-082cd970fefa | -17.02046 | -57.50908 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a8f5b536-bc69-3dbd-aa59-afc59c1c0566 | -17.02032 | -57.46798 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 31cf3086-68e7-3908-ba42-77a47880706a | -17.01978 | -57.51307 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 32249c46-7b35-3b1e-ab98-41d07cce3370 | -17.01964 | -57.47195 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b2d2f27e-5710-38bb-85ac-6af68a3029f4 | -17.01909 | -57.51706 | 2024-10-23 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README48.md)
