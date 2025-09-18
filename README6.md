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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9035f1-6692-3c9a-8802-7292656a3895 | -22.6954 | -47.5311 | 2025-09-18 02:20:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.9 |
| 2cb3a9af-e021-3f1f-8f9c-0a3b586f84a1 | -6.2055 | -45.1187 | 2025-09-18 02:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 8529611f-492c-3696-bd5d-df34b25b8087 | -11.3681 | -50.8486 | 2025-09-18 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ad4742f2-183c-3aa5-86b9-194eeeb3a2b6 | -22.6744 | -47.5366 | 2025-09-18 02:20:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| 49a08d9c-eb96-365e-8bae-abe00cb7f5ab | -20.3504 | -47.4294 | 2025-09-18 02:20:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 126f7694-4ad6-39d4-a2b9-8637ee0b0c20 | -8.1427 | -44.8311 | 2025-09-18 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 73c21460-32e9-372e-a542-cf5bd571a177 | -15.8955 | -43.4523 | 2025-09-18 02:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f555133b-a1d0-3808-88ba-ca72d8cf6871 | -14.8591 | -51.7167 | 2025-09-18 02:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d00ecaf8-31a1-330d-b85a-e472b576c6b1 | -10.4084 | -61.2108 | 2025-09-18 02:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f9069192-ad6c-32e9-9397-e29b23e9a00c | -3.5201 | -52.7588 | 2025-09-18 02:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 799558c2-a1cb-3a8b-a75a-98a0b250f2d2 | -9.3818 | -45.3582 | 2025-09-18 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| b0661aa1-6244-3e0e-99b3-fbd046580ef8 | -22.6767 | -47.4647 | 2025-09-18 02:30:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 9960c6c8-ee60-3fd1-af59-63252eccad76 | -11.3868 | -50.8678 | 2025-09-18 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3cfca288-0e74-30d2-a3b1-4c9d3b186ff1 | -3.5201 | -52.7588 | 2025-09-18 02:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 09d8ce64-f1fa-34f8-98de-117a16c4ab65 | -15.8955 | -43.4523 | 2025-09-18 02:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 20f12f6a-c291-3041-ac75-67155fa64267 | -7.8512 | -45.5879 | 2025-09-18 02:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| ada6ba18-ce0e-3e0f-aade-67011ea8e001 | -10.4085 | -61.1915 | 2025-09-18 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3000f586-0389-3561-9573-e9621cff3509 | -6.6995 | -46.2946 | 2025-09-18 02:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b530808e-1a58-34f9-a44a-64bfc8bd3aa3 | -11.3681 | -50.8486 | 2025-09-18 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 258cc9ce-3237-3567-8c57-1dcf8465deba | -22.6954 | -47.5311 | 2025-09-18 02:30:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| 0a095d7e-8831-3b50-9fe2-de2990f884bb | -7.3847 | -47.0378 | 2025-09-18 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0b27b4fe-6b3a-3f79-97b1-bdae8a77646e | -22.6774 | -47.4407 | 2025-09-18 02:30:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 5818a921-39cd-3450-ae6e-7ba8b211ae96 | -11.3874 | -50.8252 | 2025-09-18 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f74e4374-acae-3226-832e-0e80ca710319 | -11.3871 | -50.8465 | 2025-09-18 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 4c9cab9f-39e7-3f8a-b54a-c068988423e4 | -10.4084 | -61.2108 | 2025-09-18 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b0dea7b9-52a8-3e55-b6f3-adeba78f2909 | -22.9714 | -51.5902 | 2025-09-18 02:30:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.4 |
| cb4a7e70-54e9-3831-97ab-0715858036f4 | -14.8591 | -51.7167 | 2025-09-18 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| f3a245f1-f107-3b5c-b7f1-bced63169e22 | -12.4056 | -51.4113 | 2025-09-18 02:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a0594bb7-5d5b-3574-b625-b0659c7a2e54 | -14.9368 | -51.706 | 2025-09-18 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 248726cc-2ff1-3dcb-aee9-be5352f7e073 | -14.8397 | -51.7194 | 2025-09-18 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 086ad9e7-8bd5-3446-b154-c551782a54bb | -14.9371 | -51.6845 | 2025-09-18 02:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 84020bff-35f4-3c68-af8a-3e55228deb31 | -9.3815 | -45.381 | 2025-09-18 02:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b53fc133-278b-371c-99d2-d13d682a9cc8 | -18.5505 | -46.0369 | 2025-09-18 02:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| efbc2bd1-ca32-3215-b8f7-882a8471ae26 | -15.8955 | -43.4523 | 2025-09-18 02:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 37fba52a-39e8-387e-bffb-cc94dc9ab5b4 | -20.9635 | -48.843 | 2025-09-18 02:40:00 | GOES-19 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| 29e1e4d8-ce3f-3759-8277-ad36d7717282 | -11.3681 | -50.8486 | 2025-09-18 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ae0358a4-8f09-39d8-a0f5-10eed3a05ab8 | -11.3871 | -50.8465 | 2025-09-18 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| c144ee20-9541-38be-916d-c5436b5bfafe | -14.9562 | -51.7033 | 2025-09-18 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 92c76ee6-0ac7-3f27-9671-dead464bb15e | -14.9371 | -51.6845 | 2025-09-18 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 71910ef0-62c9-3aaf-a859-eaa388711f89 | -22.6774 | -47.4407 | 2025-09-18 02:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8d1f9ddb-f604-35f6-9d5c-409484a1a822 | -14.9368 | -51.706 | 2025-09-18 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 84efa414-e400-36ff-a73b-0c75e50364fd | -14.9566 | -51.6818 | 2025-09-18 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 34464de6-d90c-3239-b248-678192e693f1 | -3.5202 | -52.7384 | 2025-09-18 02:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 962e4dc3-5930-33e4-8e7e-2e45275f6117 | -22.9707 | -51.613 | 2025-09-18 02:40:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| 2633d3b0-91c1-3062-95ce-9ec4b086f70a | -14.9173 | -51.7087 | 2025-09-18 02:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c9b47635-c855-3e74-a4f1-03d84cab7d60 | -22.9714 | -51.5902 | 2025-09-18 02:40:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 169.5 |
| 37a4ab27-4e90-3cb8-a012-6ab54f1a3072 | -20.9642 | -48.8198 | 2025-09-18 02:40:00 | GOES-19 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| 97ebc4cd-9653-3d5e-bf5e-efdcd901f79b | -3.5201 | -52.7588 | 2025-09-18 02:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f4e2ed91-72c0-38cf-9be0-2b5236a6bfcc | -12.4056 | -51.4113 | 2025-09-18 02:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0992456f-4560-356c-9ed0-76af30840ae2 | -22.6767 | -47.4647 | 2025-09-18 02:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 16f9289a-6a10-3997-a933-4647f23015d4 | -3.5202 | -52.7384 | 2025-09-18 02:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 26d39c9e-efa4-3fec-90e7-0c0947070a51 | -11.2294 | -47.4294 | 2025-09-18 02:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| e55c07a6-07ab-3d1c-afda-4a9bdf6558ae | -22.9923 | -51.5856 | 2025-09-18 02:50:00 | GOES-19 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| 7215ae2c-c639-32f5-972d-62e1286bc0c1 | -11.3871 | -50.8465 | 2025-09-18 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 076f7d8d-d973-3971-ae26-c0e8fa0ff7e4 | -15.8955 | -43.4523 | 2025-09-18 02:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ea5e3c39-93f8-3862-81e9-8c2ac46c59af | -11.3874 | -50.8252 | 2025-09-18 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7fe88676-ac0e-350a-99ab-e3f539f885a9 | -22.9714 | -51.5902 | 2025-09-18 02:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 263.4 |
| 729a983b-975f-3048-9326-c9728c210563 | -22.9707 | -51.613 | 2025-09-18 02:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 212.7 |
| 088243e5-2f37-3dc8-838e-cea08842a42c | -11.2484 | -47.427 | 2025-09-18 02:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| e71dfbe8-4c0c-3686-be12-ed3d67f03bda | -11.3681 | -50.8486 | 2025-09-18 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3bb44d82-4c5c-3e59-a2a9-221ad1f95d86 | -3.5201 | -52.7588 | 2025-09-18 02:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 698f295c-0ab4-37e7-8263-ef2fbdb6ce01 | -11.3681 | -50.8486 | 2025-09-18 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 667fd763-eabe-3492-9f1b-40f932ec6f22 | -18.5505 | -46.0369 | 2025-09-18 03:00:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 605d14ee-536f-346d-9bb6-3bd8f767b370 | -10.4084 | -61.2108 | 2025-09-18 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 056b3389-866c-326e-ac6e-839ddc7a95e1 | -17.1777 | -45.9131 | 2025-09-18 03:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| eaf46c60-aa95-371b-9936-b7216bc53532 | -18.5303 | -46.0414 | 2025-09-18 03:00:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e6f6f1ef-75d5-355f-b51f-2d90d3156484 | -11.2484 | -47.427 | 2025-09-18 03:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 828a5c7a-eddb-3106-93e5-20ba7729d3b7 | -22.9714 | -51.5902 | 2025-09-18 03:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 273.8 |
| 312dba23-2fda-3371-827d-da68a8fe29a0 | -11.2294 | -47.4294 | 2025-09-18 03:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 50f33cce-3851-3158-aba5-68b198a381f5 | -22.9707 | -51.613 | 2025-09-18 03:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 251.1 |
| 422361af-ce59-373d-8e33-8688dd5f28ef | -11.3874 | -50.8252 | 2025-09-18 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 737722ae-0be9-3fa6-91f7-c8ae149c079f | -10.4085 | -61.1915 | 2025-09-18 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 9bf5b3e7-3a3f-3c70-9492-1b87fb891513 | -11.3871 | -50.8465 | 2025-09-18 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 368231cd-3829-32b3-bf7c-529ed2662c25 | -19.0332 | -48.2773 | 2025-09-18 03:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1f6e1300-5dce-3382-9d39-3bfd55454c94 | -3.5201 | -52.7588 | 2025-09-18 03:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c016302d-6a1e-3841-a13e-4091f8bfe73c | -22.9923 | -51.5856 | 2025-09-18 03:00:00 | GOES-19 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.2 |
| 1c5f7480-d24d-39f2-9a6b-a9493be5c7ab | -22.9917 | -51.6084 | 2025-09-18 03:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 1687f66e-b08e-3199-85d2-d976a9d9e143 | -21.1933 | -50.1645 | 2025-09-18 03:10:00 | GOES-19 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 5904b898-e61f-3077-aee1-fab38cdb404c | -6.6995 | -46.2946 | 2025-09-18 03:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9068129d-39b9-3a28-97ae-adbeee166b04 | -11.3874 | -50.8252 | 2025-09-18 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a4829ede-3072-39ef-8964-f2ae70a35078 | -22.9917 | -51.6084 | 2025-09-18 03:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| 6d07086c-8626-3826-977b-febf40e0aaa6 | -11.3871 | -50.8465 | 2025-09-18 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 73b39223-a5cf-3540-8ca1-08f9c70b54eb | -22.9923 | -51.5856 | 2025-09-18 03:10:00 | GOES-19 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| f0299ced-d8a4-384f-8206-2e4569ddb687 | -22.9707 | -51.613 | 2025-09-18 03:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 493.9 |
| 0ba27d8c-6ae7-3fce-83d1-836cfd7bbfce | -22.9714 | -51.5902 | 2025-09-18 03:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 332.2 |
| 9defb2d6-37c9-3509-ae99-18c59b59ebde | -14.7155 | -47.1159 | 2025-09-18 03:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 80fa1898-2b63-3742-9381-7233a03ad09e | -18.5505 | -46.0369 | 2025-09-18 03:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d0f060ab-568a-3261-a08e-53c52a4fbc24 | -19.0332 | -48.2773 | 2025-09-18 03:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b69bcdfd-3e0d-3c3c-a0ab-6db174a28bfe | -18.5303 | -46.0414 | 2025-09-18 03:10:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 30556c52-fe43-362a-8a8e-716ebbcef901 | -11.3681 | -50.8486 | 2025-09-18 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c0ad860e-ab56-31ab-8685-ad9650815a2e | -9.01 | -46.3039 | 2025-09-18 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bc356cac-d034-3bd6-8d8f-808d820aa4e4 | -9.01 | -46.3039 | 2025-09-18 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 85030dfa-e524-35d3-9c00-7154ebd3a1b1 | -22.9714 | -51.5902 | 2025-09-18 03:20:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.6 |
| eac0e754-deb2-33bb-b141-dece8bb1fe37 | -11.3874 | -50.8252 | 2025-09-18 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cd4b685e-eaaf-3de5-87a9-e02995836de3 | -18.5303 | -46.0414 | 2025-09-18 03:20:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 086a345c-d96d-315b-827d-af40610fb5e6 | -19.0332 | -48.2773 | 2025-09-18 03:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 03126829-26f3-3885-844b-35db31548b87 | -12.9068 | -44.658 | 2025-09-18 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 5bb89325-3820-34ea-a11e-ee70242f618b | -11.3684 | -50.8273 | 2025-09-18 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 07a99c0a-db4a-3467-8eb8-be1e14e93a7e | -11.3681 | -50.8486 | 2025-09-18 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| eafacd30-7720-30be-9dbc-9e8c3f37356e | -22.9707 | -51.613 | 2025-09-18 03:20:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |


[Clique aqui para ver as próximas entradas](README7.md)
