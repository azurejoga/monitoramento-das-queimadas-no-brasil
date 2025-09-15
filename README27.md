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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5ccf761-7038-30c1-8dc7-8f2b6d4d7ce4 | -14.34629 | -46.13 | 2025-09-15 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96626669-37e1-309f-a3bc-6fa1f48ac190 | -11.32032 | -50.83923 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b70608a2-77c2-34af-86d9-00e9161aa0cf | -10.36552 | -45.39615 | 2025-09-15 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0882e664-5c4f-3c44-b012-9baa8c060b6a | -10.7527 | -50.64338 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d2b7cb9-ab57-3beb-b227-8cb42e55b702 | -10.9291 | -45.57589 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e348b765-9b60-3bb4-bc7d-c5477926c689 | -11.13431 | -45.30689 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a80222f-2742-39fc-836c-8a9d9a62379d | -12.80551 | -47.94807 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 95e80ed0-7fba-301f-82eb-671ead06cb10 | -10.74112 | -44.76701 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a936095d-5843-345c-8ea3-039ac338d68e | -11.39393 | -43.66082 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1159b81f-bcf7-385e-8a75-e7b9fabe3413 | -12.12012 | -44.84219 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 043ba4ce-e384-3ff3-a57e-9a7e2bcc5700 | -11.77504 | -47.56196 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9f0af92-d075-3afb-a2ff-7319c2602815 | -13.92768 | -44.8116 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d028d262-7eac-3144-855c-03a43bdf4fb5 | -14.15116 | -46.24786 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 259b990d-e8dd-3f8b-b012-17900931104c | -11.84701 | -50.4508 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 642fc15a-e472-3e13-8b11-2336e6720f99 | -15.08071 | -52.46644 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65828e00-2cc9-3b21-b10f-4381200d5296 | -14.44723 | -47.35089 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f55f72-bad2-3569-8784-3da8af2f52fd | -11.81535 | -44.70196 | 2025-09-15 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d897ac6d-87ed-30ad-9348-670e103167cd | -14.94139 | -46.54761 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba8b8854-38a3-3c80-964e-fd12acb97845 | -10.78503 | -45.97835 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b2f74c3-2f14-37e6-bc64-7f1fa396e6f6 | -12.99082 | -47.97786 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6b867458-ffc0-32a0-979c-d6e5b033a35f | -17.33837 | -42.64074 | 2025-09-15 04:21:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7466b887-8760-3236-84af-0f9510a0d24b | -13.19143 | -47.28445 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 814d5f8c-d3d9-31dd-b205-634e15a344b4 | -11.07644 | -49.71988 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b97c59-e079-389f-a24b-d87bef86fdd0 | -9.85683 | -43.13959 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6248871e-896c-3d6b-b9a0-5d54c7ca9aaa | -13.88893 | -48.31307 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2309513-f3bc-3424-b5fc-c0f0ce3fcc71 | -10.76817 | -44.72386 | 2025-09-15 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1145aef7-3e31-3ab5-8478-2b45d1bc26d2 | -11.43901 | -43.54863 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1438af1-c2c5-3d1b-b06c-bfe8bc73ed82 | -13.88955 | -48.30934 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f559f5ee-82e5-326b-9213-ca0a81fc87cd | -11.08903 | -49.73603 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d6463d5-40b4-37b6-882a-99273e70d350 | -12.61669 | -44.2023 | 2025-09-15 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5695629b-1644-3675-871a-997ad04c600f | -12.97727 | -47.97575 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 05f37e1c-f19e-3bf6-9f2e-5ece7af8ba61 | -9.14643 | -46.97217 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 979c928c-8118-3fdd-9248-d25acaae4b21 | -13.21744 | -44.075 | 2025-09-15 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc3bf7e-5961-3caf-9e0e-8d5c58103051 | -16.42644 | -45.67827 | 2025-09-15 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96567967-ee69-3f7c-badb-5bd44d1e48f8 | -10.77788 | -45.98078 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 144cbdba-008d-3bcb-92f6-d74f97220623 | -10.13471 | -46.15226 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8246385d-6ee3-3dec-a3f0-df823bb3c837 | -10.75925 | -44.71515 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ad80e8-0846-3eac-b03c-6b7a4d13d92e | -12.08839 | -44.87039 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73ad71ef-a7c7-3f54-88ef-d9238ec465f1 | -11.36009 | -43.49337 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 141bdfc9-2080-3bc6-aa32-ec1232aeffcd | -10.65916 | -46.23679 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e3570a8-f477-36e3-9e05-6e741f3ca254 | -11.26883 | -50.83006 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 407d83f9-727a-30ad-a6dc-e3ea1ac56ddf | -12.0501 | -46.54298 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88387585-d332-37f0-afde-f925eeee0965 | -9.14202 | -46.95653 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4caf77-3319-3114-a80a-4f18a7171c2e | -14.40473 | -47.34021 | 2025-09-15 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20e70e82-4864-3c29-aa6d-4918b7165f27 | -10.16735 | -45.31427 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc321f9-4371-3f04-89ca-ae09209b83e4 | -16.98944 | -45.85796 | 2025-09-15 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65e4b664-724d-3628-9de2-904de853f2e0 | -11.00979 | -51.25052 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f83b016e-3a71-32fb-a4eb-b1a58954aae0 | -14.82272 | -51.63073 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 68150bfa-d7f1-3d2e-ba8c-49cd1c78d50a | -11.01275 | -43.1557 | 2025-09-15 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96229053-7d2d-3056-9f48-6a387b10ba6b | -14.80487 | -51.61666 | 2025-09-15 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b8b9788d-bd16-3887-ad93-24458260122c | -10.16903 | -45.32524 | 2025-09-15 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 878d1788-f0ca-32bc-8ef7-977eb3c12aef | -10.93502 | -45.49443 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85ec0a1e-933e-3504-b7b5-1c86dfbbbc83 | -12.95944 | -47.99973 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61fd7c86-c26f-35f9-aca2-8c88f5f955fb | -13.95025 | -44.79992 | 2025-09-15 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3ce7b5c-5fbd-3461-864c-d399b672c98b | -14.93366 | -46.57539 | 2025-09-15 04:21:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76f1104f-0009-3b31-a4a6-cecb5c29aeaf | -15.7936 | -52.21033 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9126213d-1dc4-3f47-b4f2-92df101baf9f | -10.66522 | -46.24134 | 2025-09-15 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2f80583-232c-33ea-99dd-297a5b4c4aba | -12.6053 | -45.73341 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 355d649d-5c14-3b45-a1bd-befde96267b6 | -12.43598 | -46.87849 | 2025-09-15 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa9c1861-06e0-3d42-a83e-338f2aed80da | -11.7779 | -50.43869 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4093f3f9-1cef-3988-9af0-569b6081e52f | -16.38321 | -48.90058 | 2025-09-15 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 776966ef-b749-3304-8181-7a75b6ae262b | -11.08016 | -49.72052 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f2019cd-8f21-376e-9d29-649830e4e630 | -10.79713 | -45.98745 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79f48cb7-eb46-3325-b85f-66b813dedbd6 | -13.87805 | -48.13891 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad88d2c-343a-35a7-9f92-a6a0ed2b453b | -10.72608 | -44.77926 | 2025-09-15 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efad0393-6411-3387-a528-32c40342354a | -12.00249 | -46.65089 | 2025-09-15 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05026fcc-9c66-3db4-b6e8-edd449da95e8 | -12.16632 | -47.58121 | 2025-09-15 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a3d0825-ed2f-3ce2-bb81-bef948eb0c6d | -15.78679 | -52.20205 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02487737-6b78-33aa-9eca-d2c15090ce3b | -9.17701 | -47.0407 | 2025-09-15 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e31bd347-ac79-3915-bd66-0d3488a71ac9 | -11.86231 | -50.5239 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cfb348fa-7f59-313e-b03d-39068d0fcde1 | -15.75675 | -52.23034 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6de4c736-cf7e-320b-aacb-8ef0201239ef | -11.12992 | -45.31342 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c54957a-6928-3389-b704-41180871d05f | -13.18928 | -47.27664 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae00fa4a-6c0c-36a7-917f-f938e7d87e36 | -11.31472 | -51.13448 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6b12efd-9d12-3ac0-a83d-5988e8e169fb | -12.96493 | -48.00856 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fe9a7d3-65f2-3b4d-b9a6-481717eab142 | -9.85917 | -43.12396 | 2025-09-15 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50da1f8e-3add-3fd7-8535-df4053e4557f | -11.07413 | -49.73349 | 2025-09-15 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bae8098-42b2-39b4-a511-119d94507fbf | -12.44701 | -44.7477 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 482e9652-29a6-31f9-b9cd-724bad4c33de | -12.09673 | -44.86065 | 2025-09-15 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fdd6baa-c056-31d9-8b9b-234627a77001 | -12.97787 | -47.97208 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bcf69929-cf68-31d9-800e-8bf78853f57d | -10.88868 | -45.44413 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f052d20f-4a80-3a65-8a43-a45e2df563d9 | -14.14566 | -46.26147 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0038ae1-2112-370e-950d-983148f591d1 | -11.33182 | -50.86718 | 2025-09-15 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e8dfe1f-bff2-31db-b7f0-a5fa7682f847 | -13.19417 | -47.28862 | 2025-09-15 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85abe0e9-a0d4-31eb-bc42-babd251ede8a | -13.87717 | -48.2998 | 2025-09-15 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b387a31f-e371-3954-bd39-6ad3b2d00685 | -12.60087 | -45.71824 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c4b4443-a6c6-3551-94c3-5ebc204ff29a | -14.2074 | -48.76936 | 2025-09-15 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 729d3096-0694-3eba-a6a8-42e205708d88 | -10.9389 | -45.51296 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30c163c-07fc-3879-aa6d-307ce5b135a5 | -9.0151 | -48.02877 | 2025-09-15 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15942dcb-2b32-3717-9f38-c64e5ade7a7a | -15.25614 | -43.08963 | 2025-09-15 04:21:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 10.5 |
| da337208-3383-3fce-b6ad-98a4a634aa54 | -12.56103 | -45.64673 | 2025-09-15 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d9c7b46-6183-3a52-8964-8762421e4dbe | -14.14896 | -46.262 | 2025-09-15 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 562455bf-95c3-39f2-b534-8445fe980b6f | -10.74597 | -50.64013 | 2025-09-15 04:21:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aaa32395-6df6-34be-9488-2e771127da6c | -15.76744 | -52.21724 | 2025-09-15 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 984c1078-4c23-3ce1-866c-cd448c079a65 | -11.86365 | -50.52642 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1a482bf6-76c6-3560-a387-19ca0c8423e1 | -12.78838 | -47.96792 | 2025-09-15 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70208137-e522-3e28-a13e-ce7a12dd120d | -16.06442 | -47.56102 | 2025-09-15 04:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbb7f1f5-2eb4-368c-a29d-39cc940a3036 | -10.92254 | -45.59633 | 2025-09-15 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d6d2aac-6759-33fc-b0af-0e0bc3595ead | -11.20727 | -48.437 | 2025-09-15 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 166f4f1d-3ee5-322e-a1e9-80679553e6d9 | -10.14408 | -46.15732 | 2025-09-15 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README28.md)
