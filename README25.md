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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70bfcd6c-2872-374e-a45c-df9110128678 | -4.54962 | -48.01953 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d043f30e-366e-3aed-89fc-122b578d00b6 | -1.68037 | -50.71241 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9faa6a14-d6a6-37d5-9f11-ebf986c55915 | -3.98878 | -49.91266 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8aff1c7-9ca5-375d-af04-0e9eea1ca199 | -3.61915 | -51.36712 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abfc2c2b-9ba5-36f6-9666-767f490e8adc | -1.76623 | -50.86004 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c0aed0-f074-3dec-ace0-c6dfdc1e6e94 | -2.13829 | -53.64195 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bfa0ccc-c342-376e-95d2-7af28cb0b537 | -1.95323 | -54.45866 | 2024-11-19 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a2310281-5a8e-3b78-877d-8006324694d2 | -5.64342 | -46.25196 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e2dede0-e2b3-3a1c-a51e-fe7c9c139d9b | -4.16985 | -48.76734 | 2024-11-19 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1275a791-a21b-30db-b930-8cb43ded6390 | -3.7634 | -52.14112 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ee0a568-8be1-3535-9c57-8b122e6ff52c | -3.76396 | -52.13754 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e9d6fb0-8166-3dd6-82fe-fa6678f4577b | -2.20862 | -48.40556 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d02a798-8f7b-3edc-ac52-5a08fd747dad | -1.13676 | -51.6828 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9474180d-ebee-3dcf-95e4-133224328391 | -2.65995 | -48.48127 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| da8f6c48-fd94-3068-b48c-42785abbfc61 | -2.77463 | -52.60513 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6bd8dd0b-3a67-3c44-ac76-644593a3264f | -3.06284 | -54.40947 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f933870f-21d9-3878-906f-650c15f9d5c7 | -1.36365 | -55.83537 | 2024-11-19 04:46:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc291ac3-fbac-30ca-9870-1bff0dacd095 | -0.94389 | -51.72339 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02c03fd6-35db-374e-bb12-98b0b23381c2 | -5.97552 | -45.3616 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c2865ad-2785-3ae8-8ddb-15177eff47d6 | -6.27032 | -44.73013 | 2024-11-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c152a21e-cc60-37f8-bb5f-523d38a6092a | -1.303 | -52.23118 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb94ea6a-0159-32ea-8b4d-bf5e8756b7e3 | 0.03548 | -49.50167 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48cc9618-6029-3e35-8c18-b130b0bef912 | -0.85684 | -48.7503 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d4710870-129a-337f-bd77-cb0d4a1d4162 | -2.77178 | -52.6008 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5eabf533-0f61-31d8-9829-3076f68e7731 | -1.57996 | -53.80359 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 304aa34e-388a-30ef-96e7-84d310a3347e | -3.04851 | -54.40273 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 456c233d-db88-3bac-a8af-12b63e5d683a | -0.85014 | -48.74927 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 45dbdd07-41d4-3cb2-8746-286aef51a35f | -2.74904 | -54.06804 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68050d47-dd48-3f93-89b1-f61d4bab2138 | -2.79041 | -54.07 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e95d0324-ade0-3d5c-a270-ae13c45e2e35 | -3.52549 | -50.2481 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ba60f1-5f64-3c69-b718-e6512e403b47 | -2.96541 | -51.41445 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 607c8f0e-5ed9-3539-b765-68eb2ec10e73 | -3.29177 | -51.19863 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c50ee9-82ec-3639-9bf1-85f603d59fee | -3.5321 | -50.24912 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a5b03dc-184b-331b-9bb0-b4c821c70e32 | -1.24932 | -51.61521 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b5a5848-bbba-3e6d-a1fb-6aba1977aa4a | -3.96745 | -50.99031 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f1f240-5252-33d0-9236-98b580e825af | -3.36992 | -45.33297 | 2024-11-19 04:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dd1abe23-0311-358d-8eee-9370f94f93c7 | -4.4925 | -46.71751 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea5296b9-3a82-334c-a1e7-c50584231602 | -1.21121 | -51.76099 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d25ee7a7-dff0-3579-9889-32c05ee8054c | -2.70766 | -51.69122 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f42e925-87e3-3223-ae75-b5d195700147 | -5.98033 | -45.35833 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0546ebea-1495-331a-b8ce-1c4aedcf4da7 | -2.22524 | -51.99122 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea74e2ca-8265-31c5-b6fc-8c7dc62519a6 | -1.58594 | -50.44707 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0c116529-8589-3c05-9e42-ff7fb37907c1 | -4.09137 | -50.73838 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 267c4dc9-eb3f-30bc-bea9-cd15972a39d3 | -1.91586 | -53.33731 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78257988-e35b-3130-9a56-800034832a69 | -2.35251 | -48.4276 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53611287-1dbc-376f-b1ed-fe002ca95e04 | -1.2696 | -52.13089 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe83e00a-b4f0-37b8-ada5-703e2920cab7 | -1.21405 | -51.78744 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b213f9-9960-38cc-8a32-ce45de7b39c0 | -3.0478 | -54.40723 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ec6cceb-cd80-3093-9075-86b9ce080dca | -2.76223 | -54.05662 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0270912b-d9e3-3778-a65b-274f1b561999 | -5.84854 | -46.43637 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94e1880-9990-37b5-bafa-88d32f891c1d | -3.52475 | -54.67857 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bc9a3de-f1d9-3bc5-98b5-9a32273a4c02 | -6.39979 | -44.73895 | 2024-11-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea499cd7-7b8a-3b12-b96f-4d955a1f1961 | -3.92422 | -54.50803 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf1b8b8-a938-381b-8fd5-2d06f8047d12 | -7.90157 | -44.21903 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b604a33-25a9-3dd4-8ea3-01a7c6da0601 | -2.00167 | -49.54742 | 2024-11-19 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc8efa24-54c3-300b-8bce-8129faeff1b6 | -3.98437 | -49.91912 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c62784c0-172b-3804-a5ad-285e1e655921 | 0.12969 | -50.49646 | 2024-11-19 04:46:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f06fee0-4844-3d80-9d69-06b1ba5ac461 | -3.0128 | -51.43612 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e973918c-0f4c-3933-8273-06a8b61e82a4 | -1.58264 | -50.44656 | 2024-11-19 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 49c00aa0-780f-31b0-9e00-4b00b851dffe | -0.95406 | -51.72495 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a470c57c-10af-3d82-b069-36e539096c2c | -4.39068 | -47.77864 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ee5b42cc-d6b3-38c7-979a-104a3b993b1c | -3.77103 | -52.40939 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c528e7e5-2b47-3edf-8360-c6006aab9a98 | -3.2883 | -54.11863 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9da8d817-8049-3904-9b05-21a30d073cbb | -1.33384 | -51.85756 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f360e4-5409-38d7-904b-343520fdf12a | -2.60083 | -50.04722 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21c5ea34-103a-3521-ba84-6e7a97a07e9c | -1.29838 | -52.23815 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c718caff-3da3-3272-b7d4-c302fba3edd2 | -1.43344 | -53.38055 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a811dd5-873a-3c12-be13-4f5fd5916c90 | -3.70841 | -51.84029 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10b3d4f1-9693-3e4d-a77e-3be17cccd271 | -1.86787 | -53.2002 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12e90247-fe5d-39c8-be56-32a9f846d4e4 | -2.158 | -50.70588 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db85fc5-58c6-3d03-89fb-7f9088712e05 | 0.34082 | -50.41073 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98dc839f-a28b-3470-8c2f-7219a74fc85a | -1.84177 | -46.28284 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd82f971-5507-306d-a564-c9cb2b00a3cd | -0.82646 | -52.86534 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4fb125-9a05-344f-877c-f2eb56e85b3b | -1.13337 | -51.68229 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7547aa0c-d648-3e9f-971a-3c82d6f8deb2 | -3.15692 | -45.44513 | 2024-11-19 04:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f7b1f54-fac4-3576-b507-bb212dc7d6b1 | -0.91671 | -51.74156 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f3d8a56-18dc-3638-bc22-0af7035c8551 | -5.96826 | -46.30787 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfd434e6-321e-33b0-b780-035141417003 | -1.92329 | -54.05647 | 2024-11-19 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0285970-df70-3aaf-9a26-c83c3b059492 | -1.41876 | -52.43486 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 07cfd1a3-0f44-373d-b776-a25587b74c07 | -2.96208 | -51.41393 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3088bdf2-7558-3e4b-9efe-f422049fc352 | -2.59072 | -51.72051 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bab37087-1103-3aba-a900-42b41adb5c9a | -2.3133 | -52.03447 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7feb3307-6c69-35e5-9141-acd41be91fcd | -1.20613 | -51.77135 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef263796-c917-31e7-b993-af588be1a174 | -2.68701 | -51.80091 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 535085b5-d6cc-3eaf-8684-162510bca49b | -6.25602 | -43.56722 | 2024-11-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b25afbdb-bc1c-3fc5-a847-91c4abfdbf4e | -7.89215 | -44.2175 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccabfe4c-43f9-3add-87f8-5799c8efe7d8 | -1.27018 | -52.12716 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0de43d47-69d4-3708-adf2-ad8cd4df36a1 | -2.57358 | -48.03695 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43356242-94e0-3ef8-a0b3-09df3efddff8 | -2.59351 | -51.72459 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98d46ff1-8171-3000-9169-55e1a7506201 | -2.26254 | -51.88583 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 746c61e0-aa3d-3caa-bad3-09fd98f6a6e5 | -3.03655 | -50.96021 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 825c4e93-7c5a-3b84-a5a2-91e673e4b2f6 | -2.59915 | -51.79844 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc0d5907-5933-334f-b756-58ce4a9189ef | -2.92203 | -48.05304 | 2024-11-19 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49689ed4-8eb9-3182-9d9f-31fbfb74df81 | -2.51585 | -48.21165 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a862656-c148-3dca-9e6d-a5bfc0368565 | -1.20387 | -51.76357 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 73bab6ff-1220-360a-bd49-e84006c10b8b | -4.57444 | -48.02334 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa85c72d-0a3a-362f-91fe-8dccdead0d12 | -5.38862 | -40.65666 | 2024-11-19 04:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e2336df9-6704-3609-b13d-c6515b7c8f81 | -1.73066 | -53.27238 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05844612-d52d-34c2-9154-ceeb6ac501c4 | -3.98051 | -49.92208 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0e43bff9-af4d-3142-87a5-b12c0c563ef1 | -1.13306 | -52.10638 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README26.md)
