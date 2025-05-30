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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd2f558-a5e2-38b7-a0cd-a05d1b2ade86 | -7.24176 | -43.09428 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dbcc3f23-7157-3f64-b75d-13fb2970847f | -7.90318 | -55.41466 | 2025-05-30 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cce6d000-6fa0-3c19-b27e-29e0c4547083 | -12.39149 | -49.96648 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bbf9626-6ddb-37a3-9e8a-b52187dc13e0 | -7.58253 | -45.86632 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18628a49-e639-31dc-947e-7601e3984b87 | -12.02585 | -49.5182 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40742f8b-43d1-34a3-83c0-612632e9c546 | -11.14474 | -53.94099 | 2025-05-30 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6641515-560f-3bf6-b4a9-55bc8ab1b1ba | -7.07214 | -44.91945 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0875f63e-bbb7-3313-8338-f65a91c3844f | -10.29857 | -59.09366 | 2025-05-30 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 054ea357-11e5-351a-b108-b74845c7b148 | -10.45974 | -47.95439 | 2025-05-30 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a94b6ee3-477e-3996-be1f-f795ab94f85a | -8.00495 | -45.68675 | 2025-05-30 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0968d434-7591-3a1e-ba80-b4cbaed818ab | -9.85187 | -48.14986 | 2025-05-30 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5b9039d-c69a-33b7-bf6c-fe183ea256ae | -12.01405 | -49.52477 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e314220-bc1d-3df0-85e3-52ec36c129b5 | -12.01379 | -49.52631 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5da1dead-a357-336e-9530-69e20e270081 | -20.02773 | -45.44517 | 2025-05-30 04:49:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd710a4f-526a-3234-a43b-22b8c233596e | -15.36187 | -48.0025 | 2025-05-30 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2568fec-bf2d-3b01-805b-115e283da0a8 | -15.91427 | -43.45706 | 2025-05-30 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e43c47dd-632a-3537-96de-f73e9799c337 | -14.86286 | -48.09724 | 2025-05-30 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8fd315-d55b-3a87-bddc-d209e814b267 | -15.24484 | -47.46259 | 2025-05-30 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f8340d5-1290-39c1-a317-5a32a7baa8e7 | -15.33968 | -49.10768 | 2025-05-30 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5180c507-777e-3ca1-a829-0ae0f96d964b | -20.02266 | -45.44458 | 2025-05-30 04:49:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7071bbde-b5cc-307e-b825-842467676313 | -16.52163 | -43.0648 | 2025-05-30 04:49:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1588818-aa88-35ba-a7ff-6ec935e18e8a | -14.84223 | -48.10042 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9263432a-b559-34cf-8331-9c99b56b046f | -16.58751 | -45.88064 | 2025-05-30 04:49:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e611443f-2c64-3af4-8490-09ba1a844497 | -15.36493 | -48.00011 | 2025-05-30 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a4971c6-d500-3206-ad86-b4ed98c644db | -15.36092 | -47.99944 | 2025-05-30 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c110d9ee-eeda-3eb6-ad24-361a1fdec7de | -14.86216 | -48.10248 | 2025-05-30 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64502f15-5d8b-3ae1-8972-f6bb40166162 | -14.85884 | -48.09711 | 2025-05-30 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e2b5d62-ad43-313f-8ee9-857fbfd3b723 | -15.24899 | -47.46321 | 2025-05-30 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d64fd53-8309-36f6-93b9-29939b2a7661 | -14.62816 | -47.964 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7780a2d9-4115-3594-a50f-613e21bf4bc3 | -15.08003 | -48.94239 | 2025-05-30 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c5d81a6-02d8-3871-af63-a6ae85e77380 | -14.84154 | -48.10568 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a340b2cd-0915-3076-8a9b-3209e001db1a | -14.6273 | -60.00198 | 2025-05-30 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09d4ee70-f2af-3fea-8b85-79d82efef390 | -14.68009 | -52.6891 | 2025-05-30 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abf70c6d-1233-3875-a324-eacb1e85b08c | -15.07935 | -48.94731 | 2025-05-30 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be1f8809-e04c-31be-9250-ccaa9028a048 | -14.84549 | -48.10634 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b252c44-75b1-375f-8b8b-586db539b293 | -14.85154 | -48.09126 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e60c3c42-7604-3e6f-999b-878d036ce8f5 | -15.90879 | -43.4564 | 2025-05-30 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5af698-2a08-3fc5-9c8e-683fb6bf7ea0 | -15.36634 | -47.99964 | 2025-05-30 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d815ec66-becd-3213-b545-93b85b116b1f | -15.90925 | -43.45858 | 2025-05-30 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 267b4e8a-7d50-378a-9a09-1643d1d6390f | -16.59027 | -45.8802 | 2025-05-30 04:49:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43a34f82-bea2-3d83-a769-d68904b563ab | -16.52122 | -43.06871 | 2025-05-30 04:49:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb54f781-de84-3e06-82a5-34d9d41e6bf1 | -13.77843 | -54.30942 | 2025-05-30 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d65d156e-796a-3d55-a2bf-86a4434278f5 | -14.84758 | -48.09059 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 62fa5346-647e-336a-8bf3-cc9e598f36d8 | -13.1464 | -56.804 | 2025-05-30 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a087c025-8b1e-301f-a236-9020c98d45f6 | -16.51554 | -43.06811 | 2025-05-30 04:49:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e8f69cb-1124-33e3-960c-d7b51b4db470 | -13.14637 | -56.8055 | 2025-05-30 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aedbb7df-3038-3cbe-b73f-34b43645d3ce | -14.84619 | -48.10109 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 711436a1-7f52-39b1-b797-e10bee40e300 | -14.86355 | -48.0921 | 2025-05-30 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bda3aed7-5a04-31a3-a007-af6c28fd91c5 | -16.03022 | -43.68312 | 2025-05-30 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fde52ee-93c6-38b2-aa08-f2dda3ec8c33 | -14.69465 | -48.30695 | 2025-05-30 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 906f1ad9-3656-3f40-b595-502ba8700e7f | -20.02805 | -45.44217 | 2025-05-30 04:49:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9f43c12-2a08-3f9f-97be-cbbaab80aa80 | -15.91385 | -43.46073 | 2025-05-30 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4362eebf-86c9-3a80-ac37-0d6d781a3885 | -16.6799 | -43.88402 | 2025-05-30 04:49:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 910f2e60-fdd8-390e-886b-560e01a9b6a5 | -22.54081 | -48.8133 | 2025-05-30 04:51:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef23338d-080f-3340-b1b9-9bbdf381de89 | -21.87229 | -57.10246 | 2025-05-30 04:51:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc68ee42-88be-32a0-b348-6d296fa110fe | -20.99618 | -51.79309 | 2025-05-30 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 40b3c202-02ff-38c7-99a9-f66815af246f | -23.63962 | -48.08435 | 2025-05-30 04:51:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4238368-04a6-385e-b0b8-a032b178f41f | -22.35791 | -47.56157 | 2025-05-30 04:51:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3421e93d-8057-364d-bcac-bc0ab5bd3010 | -22.2319 | -50.85897 | 2025-05-30 04:51:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4b38705a-2774-3d0e-b791-790ba31439a5 | -20.69243 | -56.67211 | 2025-05-30 04:51:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b54be7d0-0c92-3e84-99c8-5c8edd070dc5 | -23.64214 | -48.08675 | 2025-05-30 04:51:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3df48db9-a4b1-386f-8c5e-dc3934811715 | -21.18413 | -53.17965 | 2025-05-30 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccdcee8a-0736-33c6-b16f-b010198c14fd | -19.0219 | -57.62186 | 2025-05-30 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 36192bfb-03fd-3cdf-94fc-e403f5d70946 | -19.59562 | -53.84371 | 2025-05-30 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6d2efdc-f8c4-311c-ae5e-f7f512db7afa | -23.40597 | -46.55797 | 2025-05-30 04:51:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 81584e2b-353a-3bfe-ba96-e90bc387ae28 | -20.47789 | -53.67692 | 2025-05-30 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27443fa8-8853-3966-b1d7-b27ff39be95f | -19.47808 | -55.44199 | 2025-05-30 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0c9897c6-b178-3f46-94c3-d65e761ef4dd | -21.18749 | -53.18022 | 2025-05-30 04:51:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f4b635f-f014-38b8-bf5c-34687589a461 | -25.19155 | -49.32712 | 2025-05-30 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 74531f14-def0-3416-88e0-2fcb1fd0e66a | -22.22818 | -50.85844 | 2025-05-30 04:51:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5fe6efc2-3913-363d-96ec-9ea5eacdc99a | -28.58696 | -49.44018 | 2025-05-30 04:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e3fb63b-7800-3a1f-93d6-cfeac4127c39 | -5.20912 | -43.31003 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 673356f3-d5e8-31f6-8690-31bf8ea3ceaf | -5.21007 | -43.30299 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70ee185c-7fcd-333d-8590-bf7a295734bf | -5.21627 | -43.31145 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c81cb76-745d-30ec-b91b-dadcbeef4de7 | -5.21568 | -43.30559 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d15a26f-60b4-3bcc-a243-5775a4e44b9b | -5.21469 | -43.31262 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 015b86d6-7bd9-30d4-8743-e3f02e0a7bff | -3.35107 | -53.25159 | 2025-05-30 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ffad1f-911b-3a8a-a5af-b81ea198e482 | -5.21531 | -43.31857 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4033cac7-341e-3282-8167-d812c7dd9cfd | -4.48628 | -47.79226 | 2025-05-30 05:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| accf39a5-ec36-3414-ba4b-42cbfccd16d2 | -5.20853 | -43.3042 | 2025-05-30 05:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2466034c-7438-3687-a75e-8e43eed7af2a | -2.5338 | -53.95695 | 2025-05-30 05:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 862f648a-8cbf-3a74-bcc0-04294203e3d1 | -7.62009 | -45.75106 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad4f934f-417f-3823-9e9d-423204438a53 | -7.9027 | -55.41738 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd698de-9025-3e68-9fae-ab23b13c0fc2 | -9.60474 | -49.02622 | 2025-05-30 05:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf1fedf-9bdf-33ea-b52e-79ef32657d35 | -6.24634 | -43.37674 | 2025-05-30 05:12:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fe7f935-4f9f-3da5-9c02-fa87c1cc0f4d | -7.62118 | -45.74585 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2872d97a-6511-3c49-96cb-e25363e53b1b | -9.84676 | -48.14896 | 2025-05-30 05:12:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e98698-5a1e-3a35-955d-c1778bc245ae | -7.62077 | -45.74602 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 162c0c68-4242-329c-8e4a-b2ce69ef0811 | -7.57909 | -45.86174 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f266782-e1dd-3474-96cd-ac58f2de8dac | -8.78863 | -47.94038 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd6ad3e7-e8c5-37c4-9703-8959859e0232 | -9.1997 | -49.466 | 2025-05-30 05:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35a7db2b-8ecf-3bd5-bd01-35c3b5952281 | -7.61508 | -45.73967 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 670b2be9-052f-36f3-9bf7-6ddb46475026 | -10.26633 | -46.48243 | 2025-05-30 05:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a3135ab-9bee-3725-abbc-5665f09244e0 | -8.7899 | -47.94268 | 2025-05-30 05:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 974b8df8-422c-3308-9ef1-c1cf54ff89bd | -7.62053 | -45.7509 | 2025-05-30 05:12:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64d3e899-c618-35b7-bf64-ee687b0df251 | -9.39412 | -48.41977 | 2025-05-30 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0e036a5-d9ad-34e7-8136-484a9c2e06ce | -7.8963 | -55.41241 | 2025-05-30 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 437c07cf-ba23-3c18-849f-79b9194d7ad6 | -5.12272 | -56.11765 | 2025-05-30 05:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66a5e4e1-5f65-3f3a-8294-0e27476f1c37 | -7.57965 | -45.86679 | 2025-05-30 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cd2108c-4fae-3559-9fba-fa933f6e0071 | -6.33447 | -43.38525 | 2025-05-30 05:12:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
