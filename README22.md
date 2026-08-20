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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f25c42ce-e5f9-3fed-8a26-ec1fdb6be1f0 | -7.97074 | -44.66245 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a2f94d17-4aa7-3d80-a15c-2ebf861c5016 | -6.33719 | -44.07995 | 2026-08-20 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 274c405a-a919-3924-a342-382bbd883047 | -7.96483 | -44.66791 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 7cb097b1-1e6e-36b5-9999-79096af724d8 | -6.33861 | -44.07968 | 2026-08-20 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d7e3dd9-4197-303a-afb0-84f99f433148 | -6.77886 | -42.88696 | 2026-08-20 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 71222127-a0c4-3f7a-8efc-0a294e19ff53 | -6.17811 | -39.38612 | 2026-08-20 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3797ea68-32cc-3346-a236-52a90d9fdf59 | -6.42441 | -43.06742 | 2026-08-20 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85c4d486-aa9a-346b-a6d8-7a0308ea025a | -6.29287 | -43.63417 | 2026-08-20 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18754a5b-3a08-3529-9bd2-fe1bfcc50049 | -7.96811 | -44.67582 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 83803990-362c-3837-bee3-3ef3c567d937 | -5.42418 | -43.43568 | 2026-08-20 03:23:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25637ae1-ffba-3b83-bb69-38b520d144e2 | -7.972 | -44.65605 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 39e1d67a-4a36-3b91-98cb-a23ba3cdbc20 | -9.93343 | -37.29155 | 2026-08-20 03:23:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 968f785e-5b0d-3b01-9828-87792c6933ca | -6.78467 | -42.88936 | 2026-08-20 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 37d43ad5-3a7c-37f1-aba0-13a192ff6126 | -5.73819 | -43.27612 | 2026-08-20 03:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4d9a2f1-2e84-3b57-810e-298629da316c | -6.29627 | -43.65386 | 2026-08-20 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8b728f7-4a8a-310c-983e-d82422cc0d18 | -8.9456 | -38.00336 | 2026-08-20 03:23:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f80b12dc-7fbc-3dba-8bf8-d85a44e768b9 | -7.97315 | -44.66248 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c203b010-fdb5-3952-9a73-e7f62c8ddcbc | -6.34413 | -44.08141 | 2026-08-20 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb69c5e1-f3fb-3e92-937e-826346407235 | -3.96782 | -43.11001 | 2026-08-20 03:23:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c402ce55-96a7-36da-b16a-0a962a567203 | -7.96357 | -44.67456 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dbf1ba67-73af-3cdd-9a64-4e928e311f07 | -7.97187 | -44.66918 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f3bb77b-d537-3845-8199-f417b373c810 | -6.27215 | -43.27826 | 2026-08-20 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 891a7568-bbc1-3fc1-93db-f8a369500fcf | -7.96943 | -44.66912 | 2026-08-20 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7d801f95-13e1-3c72-9e54-1ed95da6a277 | -13.44142 | -43.84073 | 2026-08-20 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8aa58f2-1f07-36dc-8b9c-396478e7e16d | -11.31774 | -45.21299 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 82583d2a-d070-3692-a328-44cabe5871a7 | -14.11678 | -44.38795 | 2026-08-20 03:25:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43369791-30d2-3df9-b15e-1efb3cd54bd5 | -11.81182 | -44.80505 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b8d933b0-ca3d-3cd5-a43b-b78bf2ab61a4 | -14.44803 | -45.61623 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 09d0f06c-77d6-37b7-a3ea-230ece026af1 | -11.81393 | -44.8106 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 70f2cd8f-79bc-3e6c-b722-c6033d80cba5 | -14.44935 | -45.61022 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7ad1348-cd53-3e0c-977a-ded82bdf15cc | -12.24883 | -43.16631 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1245510e-5431-3651-ad5a-4b9eb650959b | -14.08478 | -40.96564 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 176e2893-94a8-39f9-822a-2513f90f0ae3 | -12.23064 | -43.16369 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 198e4320-1de0-3d94-9a60-f7acba3018da | -16.86121 | -43.23765 | 2026-08-20 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3275f3e9-6513-3e9b-97d0-95f8802523de | -14.08153 | -40.96259 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b95d5fe1-8a43-34e0-b0cb-a61d78f8e74f | -14.08096 | -40.96561 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9800d4e8-7acd-3139-8c9a-6e134723b525 | -12.24394 | -43.1689 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 34efcc07-9c01-3134-939c-fc23d9bfc263 | -15.58817 | -43.7375 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8af96756-e6e4-3651-8c19-6f867db7ddb0 | -11.28106 | -45.79485 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98722aff-5880-3858-8e31-e47f5e7204c9 | -11.31087 | -45.21162 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4be5ca8d-4d15-38d2-a5a8-64098ef5a291 | -12.25475 | -43.16795 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a29da17e-af58-318f-87f2-9fdaef534903 | -13.44658 | -43.8466 | 2026-08-20 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6735b918-5e71-3bcf-b0b4-e7b29b3955bc | -11.28469 | -45.79591 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a0276f0-b443-3a18-9340-3f59f1716de6 | -15.58644 | -43.73811 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 755022d9-9736-3cef-9446-12b2a2eebbcf | -11.81723 | -44.81235 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7dcf0e25-1ba2-3e27-8ae7-7ea81f5bed77 | -12.23172 | -43.16757 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8696983-126d-3572-9bfa-7a959a1e20d9 | -14.45025 | -45.62246 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 41c84118-3229-375e-8502-633c40bf396e | -15.58728 | -43.74183 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b51c1a00-4952-33bf-8c52-9d4471645a8e | -15.53156 | -40.85666 | 2026-08-20 03:25:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54d6f623-9cf8-324f-a69c-8a266dc168a3 | -11.28785 | -45.7977 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f6e2ef3f-5bd4-33a3-87c8-93eebb64f956 | -14.45203 | -45.62977 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8abd01e-38d7-37ff-a7fe-39659382079f | -14.08209 | -40.95963 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6d913635-47e6-3dee-acf2-d610806f4499 | -16.86679 | -43.23865 | 2026-08-20 03:25:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fa392eb-5f43-3884-8cb3-0f9d8ce4527f | -14.43695 | -45.61948 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d41f6f28-1e27-30d4-9f5c-e0fb5ed29878 | -14.4467 | -45.62227 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 835259d8-8c4f-36fc-bb77-8550009acede | -13.44037 | -43.84579 | 2026-08-20 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3cb353a-d82e-33e9-ac95-748a161c69d5 | -12.25684 | -43.16686 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5dff8332-9017-32a0-a07f-8de1a95f238c | -13.15807 | -42.41372 | 2026-08-20 03:25:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4e18bacc-1197-328d-beeb-b3b6e43ba830 | -11.28239 | -45.78855 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d8550095-760b-3e1d-bfd7-2fea79e1a70b | -14.4436 | -45.62097 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1f600dd2-6d0f-3075-a077-87a31b84cf08 | -11.81055 | -44.8111 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 127bcbc3-3fed-34dd-99d7-c9c5d3a37bfc | -14.44897 | -45.62851 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ac8d2c1c-001f-3b24-8807-b61e7fd8c491 | -11.27786 | -45.79316 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d63e552a-54d9-3858-85da-c4f0195e32cf | -14.45467 | -45.61773 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 37e04f74-da91-390f-afad-dea2a57e2683 | -12.25568 | -43.16316 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 46b81b97-9066-3ef9-8642-e35b6e9ee91b | -14.08088 | -40.95879 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9569a248-e0d6-3cca-b3b8-d1c6a5f6db96 | -12.22954 | -43.16924 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45384a4d-6cbc-31eb-b380-759e65d81bbe | -15.56562 | -43.43858 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa80c13b-c6ca-3ed5-bcc4-b5a0c5cba187 | -12.24287 | -43.17418 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 14cc13d8-9d93-33fb-b521-ee8f7312ed58 | -14.08029 | -40.96175 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0acfd7d0-13cd-38b9-9a01-9f7b84409a8a | -15.58552 | -43.74242 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5f329c6f-465c-3ac2-a3eb-82c5f31bcd31 | -11.27916 | -45.78685 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a95f2ea9-51e1-347c-8f43-f301f553893c | -14.45154 | -45.61641 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b4d7bcc3-2024-38bc-96c7-ab0626e61539 | -14.08537 | -40.96263 | 2026-08-20 03:25:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 80769a97-3d62-321b-98c6-92dab7fa1c81 | -12.25668 | -43.15807 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7a94b46c-31a9-38d8-a59c-cf92d8d04132 | -12.25784 | -43.16194 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e06361c2-cccf-3ae8-86b2-b22e206c22ce | -11.28602 | -45.78942 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 26a82f79-6361-3fc8-b87f-9fe32fc9c68a | -12.23285 | -43.16207 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03cf9790-3b20-3124-bb1e-313073f7def8 | -12.24782 | -43.1715 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 0510065d-4e0f-3262-b301-f53f935b54cd | -14.45335 | -45.62374 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0a04fffd-b1f4-362e-9414-ff79889cd3d1 | -12.24175 | -43.17061 | 2026-08-20 03:25:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 66964c35-8533-34bb-bf96-2ab6c8304743 | -11.31907 | -45.20662 | 2026-08-20 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 01b50c19-a9a2-3b05-af7b-54cc52700cf7 | -13.15579 | -42.41043 | 2026-08-20 03:25:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 76488a49-4c38-33b3-b746-fa28b5e2df48 | -11.80727 | -44.80926 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc334465-8b3c-3bcd-9f38-e17f188b5e9a | -13.15502 | -42.41424 | 2026-08-20 03:25:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6b25b12-771f-330d-9f3a-a244470ee6fd | -15.5665 | -43.43438 | 2026-08-20 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af52e820-6483-306a-81b2-179968363ef7 | -11.81271 | -44.81665 | 2026-08-20 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8f0e0cd0-e64f-354e-9e94-c9048bc42edf | -14.44138 | -45.61477 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65f1ed5c-b7e0-3dae-9ba8-effabcc2ee4e | -14.44005 | -45.62081 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9846ae14-957d-3756-9cbe-61d3a262a0f1 | -14.44489 | -45.61493 | 2026-08-20 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7820354f-8ecb-31cb-a786-78c73fac29d8 | -17.32947 | -43.62652 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 0a9dd057-a66c-3500-91d0-a869f6c64857 | -18.84154 | -47.14226 | 2026-08-20 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce9008ac-421b-3ade-8a97-12da8ca94eca | -20.96769 | -44.12159 | 2026-08-20 03:28:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1f79d44d-22ae-3157-b75e-dca2b5c20d86 | -18.84833 | -47.14341 | 2026-08-20 03:28:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a70d332-9d73-3fac-8649-d25ea3f2ab70 | -20.26347 | -46.74146 | 2026-08-20 03:28:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f03d418-da46-3b93-a9c9-3170039412cb | -17.33221 | -43.62667 | 2026-08-20 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| d8bfc05f-37f6-3de1-bc82-b809e881509b | -17.88641 | -40.06535 | 2026-08-20 03:28:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3036aba7-8429-38f7-911c-337d2fa1c3d1 | -19.71432 | -46.22769 | 2026-08-20 03:28:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a31b78d8-1d71-399a-a7b4-698028c513bd | -19.67638 | -42.10769 | 2026-08-20 03:28:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24f04af3-94e5-3cf6-854e-f6a7bacabb68 | -21.61936 | -49.0212 | 2026-08-20 03:28:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README23.md)
