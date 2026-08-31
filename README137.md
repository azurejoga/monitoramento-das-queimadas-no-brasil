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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1250f057-0f94-39bb-ae47-45e5b6b3d771 | -15.22534 | -56.35901 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 7100d7ec-b7d3-32d9-8fc7-263891c5567e | -14.66183 | -53.55611 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d46ce95b-3129-39da-b5ad-ae62093b08a8 | -15.36836 | -41.18109 | 2026-08-31 16:48:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7e39a8be-d6bd-304f-a263-4660d08562be | -14.53013 | -52.29163 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 377057f8-b8a8-3a4d-8242-a0ec68b59537 | -18.65904 | -46.84796 | 2026-08-31 16:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88637535-2887-359c-8375-9afd1079e29b | -15.63982 | -56.38667 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d9f185bc-844f-33ff-ab69-fb278213ace1 | -15.62699 | -56.41639 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cbe11c5f-de21-330e-bb6e-14f8cfe62a1d | -13.7369 | -42.4933 | 2026-08-31 16:48:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 147.4 |
| 785bd401-1d4c-3e60-bd29-a4c7c6204cb8 | -16.54999 | -52.51025 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 56c9e7f7-1dc8-367e-a2ca-d25beec816c2 | -17.31957 | -41.31184 | 2026-08-31 16:48:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 09a53e81-359b-320c-8ce6-a366f9f11518 | -19.48256 | -57.55724 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| a37acc7b-4add-37ed-8923-6a01229db2f7 | -14.56819 | -53.59388 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 3e38a668-4879-390a-afb4-8e65942a71e1 | -19.11273 | -57.36778 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| a96852ec-4409-3408-9717-898474ec991a | -16.5681 | -52.50834 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72dada05-16ae-3000-a3a3-4823b117c7d8 | -18.27393 | -52.68893 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| a11e4b4e-8d48-34e6-acea-db25e04eeaee | -15.99766 | -43.5512 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 941771bb-172f-32b4-8e2d-a0eb53115435 | -19.14211 | -57.395 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 56663bc0-b1a2-3d8a-a505-e3d286934ec7 | -19.13481 | -57.38199 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.7 |
| ef819250-ff83-3484-ba7a-08bb8eeabe45 | -18.26907 | -52.68519 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| c3942647-5cb6-3d20-a6c6-aaeb9986b655 | -15.67363 | -45.92558 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4db5aac1-bbd9-314a-9ad2-61b81c9710f9 | -14.99202 | -48.1257 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9353fa2b-0df1-3237-a568-ef9329084378 | -19.11101 | -57.38435 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| ddd3bd6a-3a24-3472-9b6d-c59456a6b7ad | -15.43031 | -52.69318 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ee23b93d-ba03-3cd7-9708-fd1bccf586eb | -19.15646 | -57.38617 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9ce36b27-9bc4-3a72-b786-168f5d905e5b | -17.50393 | -44.22489 | 2026-08-31 16:48:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2bd5093-0d7a-3d2e-b460-55c5e0888626 | -17.18891 | -54.30958 | 2026-08-31 16:48:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf453e72-baeb-3c88-a39d-c051867a5a4f | -18.64869 | -47.53381 | 2026-08-31 16:48:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 081dbf73-4cc4-3eee-9d1b-8c75895e6d2d | -18.05397 | -42.23374 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9c6c8de6-3333-35c4-9999-39949a664421 | -17.75698 | -45.39967 | 2026-08-31 16:48:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a2de75d-e4dd-36e9-baeb-8d0959a4bcd1 | -19.11366 | -57.41161 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 0e094d10-bcf4-31a2-b328-635e2c3d83c4 | -15.45991 | -52.82599 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e9aa06d-c106-3f2b-aced-391556d2b867 | -15.23368 | -56.38535 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3bafdac5-5399-3f78-b405-d83c359c0d02 | -14.03247 | -47.80416 | 2026-08-31 16:48:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d474c8b-3074-3ad4-ae5a-37a60fbf92ff | -16.46485 | -41.81489 | 2026-08-31 16:48:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c1641c52-fec7-3168-886d-59e1d78c8212 | -19.20655 | -57.34446 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| c7c831be-26d9-306f-b5d6-34e105d7036b | -13.37458 | -40.35565 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 6ec1d8dd-409c-3a84-ae70-bf50b62957b1 | -15.66858 | -45.91528 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e0fb326b-d5eb-3eb9-98d3-2fd2f8fbd57e | -15.98167 | -54.45427 | 2026-08-31 16:48:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eba4b5f-adba-3872-a501-7894c901ded9 | -15.60856 | -56.39766 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 476cd916-1d0b-3e29-a8ae-dd0942ddc87b | -14.99082 | -48.14071 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1d7e4e7b-d44f-360f-8db7-b17a4b44a76e | -19.17689 | -57.41161 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 0731fe0b-2f83-32ed-a6b9-5f4545a7fe5a | -16.56072 | -52.51746 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 288408cd-5982-3165-8fd3-ed4f54128db5 | -17.74876 | -42.4451 | 2026-08-31 16:48:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| acd65b21-b05c-3881-a895-e2fffcfbb0da | -14.97067 | -54.58864 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| eb7416ae-24b4-3b34-b980-cd51d70f18ec | -19.21887 | -57.34779 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| c2344f75-cfe5-37f9-9207-0dc2faa3ba74 | -14.09507 | -40.06762 | 2026-08-31 16:48:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 648e727c-4d4c-3b31-9175-176a2747f8d4 | -15.40621 | -52.70352 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6837ac6-af86-309c-a064-98a1c104643c | -14.54252 | -39.73923 | 2026-08-31 16:48:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 133c004d-1d4f-3ca8-81cd-46abdeb67f43 | -17.87091 | -52.10758 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 187.2 |
| e71b4b89-6cfa-37d2-9da8-587ab5ab98b2 | -18.2662 | -52.73373 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 28ecf617-dceb-332a-a896-985ec98b29cf | -18.20822 | -43.98565 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0faf71c5-4a6e-31a2-b9a2-44af525f4d84 | -19.10679 | -57.36843 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| c6792826-bb4c-3110-a96f-b5c0f7b02d43 | -15.4256 | -52.6894 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a2aa8256-f431-32fb-a8c0-a47abd07e08f | -19.18872 | -57.34629 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 139db7b6-f787-3f49-9ed8-95d5bad7d395 | -17.5294 | -41.31418 | 2026-08-31 16:48:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| afb7d6ba-38cf-3a6f-98c1-a6951568f164 | -19.21336 | -57.35289 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| e1215b71-d86c-3777-b604-7377a6c81a2c | -15.21262 | -41.7464 | 2026-08-31 16:48:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9681e2fa-dfa4-3c35-a571-5bbf761d5fbe | -14.54568 | -39.74111 | 2026-08-31 16:48:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 382fdcb9-4b05-3cb4-9fc4-ef75dd4576dd | -15.24612 | -47.98537 | 2026-08-31 16:48:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11bccc65-46bd-3a5c-859d-a4ad9e207511 | -14.40732 | -53.27208 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 21c68cee-e540-33d9-8689-4eb56699feab | -13.54756 | -48.23287 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7254871d-a265-3fac-9374-56b03df1fe6e | -15.40254 | -52.7081 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d76e94f-f427-3607-92a0-e6af4dd95e03 | -13.20067 | -44.07187 | 2026-08-31 16:48:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 045c7941-5d32-3b87-b073-b9b9d53c5ce3 | -13.19703 | -44.07264 | 2026-08-31 16:48:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24be8d92-b88e-37c3-a2f3-8eb30e4fb016 | -15.11759 | -48.10247 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89fc4ec1-c832-3b97-851d-fd966cd0e652 | -14.2171 | -48.63722 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6a6cb4b-8f41-30a5-9e92-3e4b1842d3b9 | -17.86573 | -50.49732 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 44b16f27-875d-3b17-b846-3523c48252bd | -14.99029 | -48.13709 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f8c07f3b-6a92-366f-a979-623d60c05716 | -15.6658 | -45.91945 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a5588db1-842c-331b-96e4-aef14a09bf99 | -14.54352 | -39.74438 | 2026-08-31 16:48:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 8abd7801-c09a-3b88-a3df-1d255d62893b | -17.86163 | -52.1008 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 9f261ec5-c8e3-39d7-8437-38be14382d8c | -17.88702 | -52.1017 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4c32ab95-10f1-31f8-a498-8b7424f0fffe | -18.27826 | -52.68835 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| de24d18b-aa26-378d-bbba-08b1dc6c207e | -15.4209 | -52.6857 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b65af9f3-8ced-3be1-ae34-134961a27195 | -14.25078 | -53.38901 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fedabb60-0626-3c44-85b2-548b05a53eb9 | -14.44486 | -49.00339 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 82bc3246-d400-3e0a-a296-fe2aededf702 | -14.80579 | -40.66837 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 68471ae1-f3ea-3c61-894a-c4edd7aa82bf | -19.1076 | -57.37746 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 6876ae47-ce98-31f2-b01c-4b2ec717b10e | -18.26514 | -52.7251 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| de2f6c90-5b2b-3f7f-a8d7-723a3e6662a6 | -17.86212 | -52.10472 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 67334d3d-d6a1-34a1-9333-fd8f41c65ce0 | -17.85847 | -52.10918 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 49f10015-dbe4-39e6-b21f-c7f19dc9dd6b | -17.22078 | -39.29538 | 2026-08-31 16:48:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 2f2c81ac-1bf4-37d0-ab7d-3a49b13b8ce5 | -16.32516 | -49.39928 | 2026-08-31 16:48:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0f8be8f4-fe78-3e4e-9e29-9749fb31caed | -15.02119 | -48.18449 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d770ec3-f522-3aea-ae13-32f0b1504743 | -15.02131 | -48.1621 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f1fdc623-81d1-3ae7-a84b-cf073ca0abb4 | -15.97833 | -55.95483 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 993e8acc-b768-3dc2-9338-0beb0ca6e340 | -15.66915 | -45.91888 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6235d33c-4ff4-38ed-bab5-7a080bfac035 | -17.88653 | -52.09781 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a1f397d7-6890-3310-a983-0f9c97208111 | -17.71383 | -49.22304 | 2026-08-31 16:48:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b601abad-cb12-3620-a497-d918f71b7939 | -17.23248 | -53.27285 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a087407e-10dd-3393-bf70-574f3d2ded80 | -17.94003 | -42.79813 | 2026-08-31 16:48:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2bab7b3-c324-3dd1-849f-fba043964495 | -19.18958 | -57.35529 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| f16f060d-aa5c-347f-8204-2e824d13356f | -14.27237 | -40.02512 | 2026-08-31 16:48:00 | NOAA-20 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 22e5d4ad-6237-3525-94ab-d36f57083854 | -12.77142 | -41.53966 | 2026-08-31 16:48:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a156ea55-09a0-3aaa-ae95-f7554174e430 | -14.56681 | -43.8326 | 2026-08-31 16:48:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 872b6b53-06fd-3ed5-9fb7-b4f335e252c3 | -17.84756 | -50.5048 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4e7da9fa-0113-347f-b337-83cde101f531 | -20.77778 | -57.7863 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 7e623be9-2852-3cbe-83c0-9f1e0eae2773 | -14.64104 | -41.10569 | 2026-08-31 16:48:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 68c33388-5210-3166-a074-f767e5f63777 | -14.59011 | -53.08508 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 579056d0-fc86-3900-9743-21382e33270b | -17.88495 | -52.18546 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |


[Clique aqui para ver as próximas entradas](README138.md)
