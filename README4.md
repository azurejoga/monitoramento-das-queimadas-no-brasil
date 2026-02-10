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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35e7299e-f30c-348f-b9f1-2ca3fcac8656 | 3.37998 | -60.66246 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e81a622-cd2e-3638-b5f2-d9fecea06dfc | 2.48118 | -60.55463 | 2026-02-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be1901a1-1a62-3f78-9cb4-fab5568baf7a | 1.91165 | -60.57251 | 2026-02-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92cf4a94-ce1a-3037-98d4-3c63d2feb01b | 4.39597 | -60.69021 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3921d590-df80-370f-b6be-822140fc1628 | 0.77832 | -60.66825 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c962ebc8-a81c-3dd5-a921-ba3023bbbdeb | 3.37942 | -60.65873 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ddfea72-b452-39c8-b9a3-8d8d5ab04a4f | 0.95669 | -60.51814 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f378472e-7661-3a21-9821-431dbbeaa51e | 1.11588 | -59.19287 | 2026-02-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1480084-eb7a-3df4-8a11-9848e7cc0bc4 | -1.82509 | -54.49552 | 2026-02-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95783560-9c8a-36ce-898b-db6f54f395c7 | -3.76178 | -54.30984 | 2026-02-10 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d867c2-363f-39aa-8c9e-e6c097cf574b | -1.82568 | -54.4918 | 2026-02-10 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 857e3299-f549-3a83-a264-904ff54878cc | -10.18389 | -47.77728 | 2026-02-10 05:18:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c8c930f-b5b0-3abc-b15e-dc13a2ba71ac | -18.97888 | -52.9295 | 2026-02-10 05:20:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2e47395e-bd7f-30b5-8af4-6377b812d10a | -19.39166 | -55.10779 | 2026-02-10 05:20:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51002851-e6df-38d2-9013-7ae9d2d22f9a | -18.97418 | -52.92895 | 2026-02-10 05:20:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9dacac68-8e98-3cae-9c92-75691c38ec82 | -18.96948 | -52.92838 | 2026-02-10 05:20:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29b1eef9-b12a-339e-a2ff-5930522643e1 | -16.4506 | -58.17331 | 2026-02-10 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 96e4285b-fcb5-3311-b25a-696650bc434b | -19.39115 | -55.1117 | 2026-02-10 05:20:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8014621c-8b77-3e77-a76c-fa8d1b742dd9 | -16.58325 | -58.21705 | 2026-02-10 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0edf09ae-aac6-3266-9370-b8a9ce29e63d | -16.44435 | -58.16842 | 2026-02-10 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4780757b-e2f1-309c-bafd-06802ca63c0d | 3.69296 | -60.97053 | 2026-02-10 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44634251-79b1-33b7-b334-4bbb987084f3 | 3.30745 | -59.90288 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87296998-86e8-30bc-9826-13aa8256e501 | 4.35118 | -60.64257 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 279beb61-3a67-39d2-8e7d-33b0aa868664 | 4.01891 | -60.4552 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09d3312d-6105-3ce7-bc19-cb8bd8c29077 | 4.39595 | -60.68907 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1be9d5-3ee5-36a8-ad1b-663ad6274c84 | 3.30686 | -59.89923 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d0179d8-36dd-3acf-9366-5a6860b9abb5 | 3.25154 | -60.41609 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cbddafa-de8c-3a85-93d8-a636b111e48d | 4.41249 | -60.72916 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e95a95-289b-32b9-95b0-4c5720225159 | 3.31144 | -59.906 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f30adc8f-bbc7-32bc-aa89-bf92efe6c23e | 3.38178 | -60.65993 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95d6a2d7-ec35-3dc7-985a-ffb9927eae19 | 3.69241 | -60.96708 | 2026-02-10 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b32b1f5c-a975-34f5-aa97-5a2e7d50456e | 3.78725 | -60.58121 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08cb605c-b6c4-3988-ae76-6a6f42fa0d26 | 4.17145 | -60.96594 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15be516c-fbb4-3ae8-af86-b5fb91c4a4f9 | 3.37568 | -60.66448 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85c6f860-5dce-30ec-9891-26e45985a3a1 | 3.37623 | -60.66799 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37052835-791d-3628-a222-4b92ec3ff518 | 3.22939 | -60.81253 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1d742c-68e5-37da-81d1-ce6e6cafbc33 | 3.60383 | -60.30648 | 2026-02-10 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00f260c5-cb69-319f-bf42-a167fbe751e9 | 4.1922 | -60.41358 | 2026-02-10 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f07e1ec-01c8-3a6d-bbd2-7a74ea0a7be9 | 4.8619 | -60.64804 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bef32fad-9618-3b00-b61e-83e6de4bb648 | 3.29586 | -59.90093 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9607ab7-9a20-3e65-8d2a-a6fc7b25bba6 | 3.08679 | -60.83492 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c113ba7-633b-30ec-9d65-bbc2f78ae3a9 | 4.17281 | -60.1631 | 2026-02-10 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9885127-651e-3fce-8187-8300cd180b68 | 4.4103 | -60.7153 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2235cc45-37db-3a2d-a68a-c6fc78d99c37 | 4.3954 | -60.68561 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 062131d1-2489-386c-91f6-816d14d2cadd | 3.30208 | -59.8962 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ddc04e7-f257-385c-8a8b-baff85ab9acb | 4.30589 | -61.14972 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 073cb3f5-99ae-3d66-803a-ec5d6b20dcf0 | 4.41536 | -60.70454 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e81f0a08-96c3-35d1-b11e-662df321bf37 | 4.39263 | -60.68956 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10a93843-da3e-3efa-a138-4adcbc35c5ba | 3.43663 | -60.49257 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b25f3472-08ab-364b-bc6c-d37298238a44 | 4.41369 | -60.71538 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce14be70-a7e9-317e-9e17-2152117efcd9 | 3.37901 | -60.66396 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7573823-195f-3237-8a2c-f3ea8c7b42d7 | 3.31085 | -59.90234 | 2026-02-10 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc6d6c7-15e0-3aa8-9756-a5e732278451 | 4.86521 | -60.64752 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cebf27db-3312-3f06-bee3-4818de6c8760 | 3.60218 | -60.31766 | 2026-02-10 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf2ee07c-c110-3408-893c-6722a25b0182 | 3.46435 | -60.36495 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13254243-5153-30a0-aa63-cfe47116b1b0 | 4.41479 | -60.7223 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab714b4d-fed1-32ae-9855-848325fd7a3e | 4.41535 | -60.72577 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04bea498-691e-3c81-a099-963a8167e060 | 2.4814 | -60.55523 | 2026-02-10 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 08bd488d-b3c9-3494-beb9-71f6223fcb69 | 3.2521 | -60.41964 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba58c3b-c7f7-3a9a-ab96-fe336a4de074 | 4.41084 | -60.71875 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9c40f13c-44b4-36f2-8ab3-8adcc57533bb | 4.4159 | -60.72924 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 661371cb-cb2e-3d17-b70c-9f4734c470d0 | 3.37845 | -60.66046 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60e4e5a1-7797-34cf-966f-0b6477869804 | 3.79002 | -60.57719 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8a2a37f-7b0e-362e-8006-621f283a99ec | 3.23247 | -60.81173 | 2026-02-10 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c8181f-cc04-38ac-bc31-e0d3ccc59423 | 4.41867 | -60.72528 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5fc9ed-fb3c-3490-95da-23f04aa71b78 | 3.99628 | -60.93365 | 2026-02-10 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b86d53-ca48-3a49-acee-1a010aa1432e | 0.95293 | -60.51627 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4ff8b76-e350-3d62-87b7-87e55c47e6cb | 0.77768 | -60.6731 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24cdc389-d14a-3e1c-8d35-ac5bf7ff8429 | 0.78725 | -60.66791 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab3573bc-2daf-3573-80ad-627e877f37a5 | 2.19627 | -61.90865 | 2026-02-10 05:35:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00a94093-844a-3081-ba5b-5ff772c5b163 | 0.79006 | -60.66378 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d2f4081-ff9a-3c8a-b448-af6221dc9253 | 1.11663 | -60.50584 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8818af-4859-3d07-8a50-47198ba3a61f | 0.95862 | -60.53027 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2402d61-0b47-36e1-81b4-ba33e6b4bbe8 | 1.28037 | -60.43618 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e52ed480-de65-31dc-9169-dac4a032a852 | 0.77373 | -60.67002 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af68cbce-47af-36a7-a830-5a90960df4bf | 0.96144 | -60.52611 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dec11c8-ad9b-3074-8ddd-5be506d9d567 | 0.78444 | -60.67204 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f7f0293-c399-3fa8-a8c8-25995d45c57f | 1.11721 | -60.50948 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ae469c06-511c-3156-bd34-05c521e7359a | 0.95747 | -60.52302 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf637761-26e2-36ad-9dce-03ff111a6006 | 0.79063 | -60.66739 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8387afd2-1783-36f6-9f89-191307b41317 | 1.8751 | -60.91056 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49a41e90-07c1-3a30-82ae-9a3805d7fe88 | 0.95805 | -60.52664 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 893a88ac-8ce0-3dc1-abf9-015d65337b93 | 0.78501 | -60.67565 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adabd769-e1bd-3d6f-89f4-db234062cecd | 1.11621 | -60.50937 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6ac3a73c-0f52-3ed5-a273-8d3596b2e148 | 1.91265 | -60.57076 | 2026-02-10 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 102bb1df-2917-331b-8569-e3932a915324 | 1.11717 | -59.19705 | 2026-02-10 05:35:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9092d12b-5de5-3cc2-8ecc-52869bc25e25 | 2.17808 | -61.92204 | 2026-02-10 05:35:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 607e88c0-9373-34d8-9a80-de731757cc99 | 0.95351 | -60.51992 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 396e0b2d-21ad-3efd-ae2c-96419e617ddb | 0.95408 | -60.52354 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9403d5a4-48cb-32c4-8cb4-6cc94377b51a | 0.95696 | -60.54167 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 510f9169-e072-3c30-8b87-495ab8380c21 | 0.96425 | -60.52195 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1907e26-6620-3565-adc8-607a52d2aebe | 2.18193 | -61.92495 | 2026-02-10 05:35:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3579b891-8560-3632-bb6c-e3fffb336716 | 1.11677 | -60.51299 | 2026-02-10 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9c6de8bd-5617-3cf2-9049-d788cf90f4cd | 2.18138 | -61.92152 | 2026-02-10 05:35:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac84ebe-0f20-3e73-81cc-57b75e61f865 | 1.00596 | -59.4353 | 2026-02-10 05:35:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91bdabb6-8d17-3481-8bf3-ffefc60f04ca | 0.95638 | -60.53804 | 2026-02-10 05:35:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c52832d1-591f-378b-a93d-6c61e56d62b6 | 1.82088 | -60.50451 | 2026-02-10 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a20ac537-be2e-3aff-8d17-fa9fc1d060ff | 1.11424 | -59.20167 | 2026-02-10 05:35:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 091c102a-315e-3a20-a140-429a6032c6db | 1.1136 | -59.19761 | 2026-02-10 05:35:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 431ef6e8-fd56-362a-9239-ef377295e604 | 2.17863 | -61.92546 | 2026-02-10 05:35:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
