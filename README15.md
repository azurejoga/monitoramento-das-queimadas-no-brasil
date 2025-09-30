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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e14983a8-b666-3aa5-9c15-0759252040d5 | -0.1012 | -51.2738 | 2025-09-30 03:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 93644150-9afa-3c15-a960-03a13ff273e1 | -11.1546 | -54.126 | 2025-09-30 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 195.2 |
| 7041495d-3ece-3291-9377-974e14827346 | -22.5197 | -44.622 | 2025-09-30 03:00:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| fa7abb6c-a8cf-3ea8-9c20-6513513d1e81 | -11.1737 | -54.1037 | 2025-09-30 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ac88b168-bf48-3e1c-978d-764a1974f84d | -13.2158 | -50.95 | 2025-09-30 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 896d8f2a-bb39-3753-ab63-675f9f2d5b96 | -14.5327 | -48.4715 | 2025-09-30 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2d45dec7-7e9d-3336-bb78-03154a2b5b92 | -10.2041 | -44.8915 | 2025-09-30 03:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| d29410bc-94c5-3f7c-9028-911e96c3959a | -22.5205 | -44.597 | 2025-09-30 03:00:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| 2a579e75-1ffc-3455-af56-8a77b88305e0 | -10.0906 | -50.2154 | 2025-09-30 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 904c09a4-ca3b-3a9e-be7c-5f1df59f8d61 | -17.61326 | -40.68062 | 2025-09-30 03:02:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 695d8afd-01c9-35fd-8e42-0f6e08c9427d | -20.32385 | -41.40135 | 2025-09-30 03:02:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e80b5b3e-74e4-3591-af44-c7527e95ee49 | -16.82941 | -39.33819 | 2025-09-30 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 90845a52-86aa-30b3-959b-fa26248d070e | -16.83063 | -39.33273 | 2025-09-30 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| aee8cff3-e7cf-3ea5-8c48-dd19b45a0bb0 | -10.1851 | -44.8939 | 2025-09-30 03:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 319.4 |
| 95f4d00c-dc75-38a3-821f-4f7740b6ea6f | -14.5137 | -48.4522 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f0708f9f-67e3-3df3-b496-4743355c8c83 | -13.2158 | -50.95 | 2025-09-30 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| b862b9e0-f58f-35b7-a80b-034634099100 | -14.7465 | -45.6656 | 2025-09-30 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 46624dcd-f6bc-3832-bf35-d6667151863f | -14.5323 | -48.4938 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c08ecea3-3e31-3b7e-a0d6-5f72ba068b9d | -14.5522 | -48.4684 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 27e8da42-4509-377f-a54c-f3538bdd3c80 | -10.1847 | -44.917 | 2025-09-30 03:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8e2c2c5e-24db-3e64-a31d-2a217c133da2 | -11.1546 | -54.126 | 2025-09-30 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 1cb96274-53c8-33c7-9124-0113e8aeb190 | -3.1013 | -47.0082 | 2025-09-30 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 15fa91e7-1c42-3716-8f6e-5f9b7c7ec15c | -0.1012 | -51.2738 | 2025-09-30 03:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f7a5302f-ee81-34e0-a062-f443f4d28c1c | -11.7519 | -44.7461 | 2025-09-30 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0f3af201-2e92-3935-9584-beab36fd5e7e | -11.1737 | -54.1037 | 2025-09-30 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2d2260af-048a-318b-810a-0e84c4718401 | -4.4013 | -44.0755 | 2025-09-30 03:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5c84b16a-6bcf-34c7-8128-81967281a3e1 | -10.1855 | -44.8709 | 2025-09-30 03:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fb099d99-78de-3261-a33d-07c32cad0391 | -14.7142 | -48.1301 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 79ca1e1f-4f63-3c3d-8bba-abd19af174dc | -5.5243 | -43.8647 | 2025-09-30 03:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 4ca02162-f752-3ce7-a4dc-a6630ef11791 | -11.2707 | -47.2236 | 2025-09-30 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3943c6bc-4e53-361e-ba2b-2a65588eb668 | -14.5517 | -48.4907 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c2b5dd72-3cbc-382d-9fa0-3b5ff118953e | -11.2516 | -47.226 | 2025-09-30 03:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 712aba88-5fe7-3635-8b58-bccb51c2e0c7 | -20.0491 | -41.3251 | 2025-09-30 03:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| b08cdd7f-0064-37f7-918f-6ef32834b709 | -4.8915 | -43.4678 | 2025-09-30 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 1afd10fb-a434-337b-bf32-da1ec66ef9cd | -13.7511 | -54.7286 | 2025-09-30 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 24754632-4c72-3584-807c-b18a6cf75fd3 | -13.7703 | -54.7265 | 2025-09-30 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a6209abf-d16a-3081-bc28-639c0fb7e66d | -4.9102 | -43.4666 | 2025-09-30 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a3db02c3-6f40-3205-9b4b-8941ce851c35 | -11.1548 | -54.1054 | 2025-09-30 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| a8443fae-a6db-3f92-b0ae-5201b7454352 | -10.2041 | -44.8915 | 2025-09-30 03:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 69f0d2df-7464-34e9-aca9-f1938250297b | -14.5327 | -48.4715 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4f01362e-fbee-329e-bfb2-3fdc4037ba56 | -11.1735 | -54.1242 | 2025-09-30 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 93c24163-f913-3651-b1a5-ac0a53e74c89 | -14.7137 | -48.1525 | 2025-09-30 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c0b40aa7-3a40-3b11-baa7-8c24b225c159 | -5.5241 | -43.8878 | 2025-09-30 03:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2fa45ea0-bf4f-3ce9-92c2-53d5cd5b1a08 | -12.8429 | -47.0063 | 2025-09-30 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7f5f43c4-7898-3833-9807-ace300c27318 | -0.1012 | -51.2738 | 2025-09-30 03:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e1532f96-3743-350f-9d0e-07d6718d58bd | -5.5243 | -43.8647 | 2025-09-30 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0c0c7bf7-aab9-3d51-bce5-02e1e5741451 | -10.1847 | -44.917 | 2025-09-30 03:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4de46e33-9dd5-3b3d-8be8-006d5bd2af40 | -14.5327 | -48.4715 | 2025-09-30 03:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2565784b-057e-3343-9850-c3070697c96d | -22.5197 | -44.622 | 2025-09-30 03:20:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 6e94dd97-66c9-3f0a-96aa-119893616eb1 | -11.2516 | -47.226 | 2025-09-30 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 6e5b72d7-b130-39a5-ab6c-4df091c2bc9d | -5.5241 | -43.8878 | 2025-09-30 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f990bc7f-9207-37fa-ba94-2a6b40bb882c | -12.8429 | -47.0063 | 2025-09-30 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| a268c509-4476-33ee-ad50-f2c8ee249ade | -11.1735 | -54.1242 | 2025-09-30 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 5a1e360b-e23f-3f31-9337-971b6e0f8163 | -11.1548 | -54.1054 | 2025-09-30 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| ffcb12bf-ea4e-387c-b3f3-42cf6af0923a | -15.2329 | -49.4021 | 2025-09-30 03:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 37c628f7-b444-3c03-ba42-07caa597035c | -13.2158 | -50.95 | 2025-09-30 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9f5d98bf-c2b9-3a2a-b30b-dc39d720f0f7 | -3.1013 | -47.0082 | 2025-09-30 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a2bb04e4-162f-3ab2-bb4d-82210b7cf6c6 | -4.9102 | -43.4666 | 2025-09-30 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 29fb8f4f-6f9b-359c-9954-3a68053c39d3 | -10.1855 | -44.8709 | 2025-09-30 03:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 692cef3c-279d-3de7-b5e9-a23be2d4d60c | -15.2524 | -49.399 | 2025-09-30 03:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0ff0d9da-a386-3da9-ac38-17757c567e3c | -11.1546 | -54.126 | 2025-09-30 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.2 |
| ad54f8af-c68a-3766-914e-48d3198e3c7e | -14.7465 | -45.6656 | 2025-09-30 03:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| abbbdf2d-d647-39f6-a5d0-a997a7692023 | -22.5205 | -44.597 | 2025-09-30 03:20:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| 86ca64e2-bc82-3354-accb-5b53bb345a2b | -18.4862 | -44.0191 | 2025-09-30 03:20:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| baac73c1-9829-3f16-8b1a-e798b73fea04 | -10.1851 | -44.8939 | 2025-09-30 03:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 10e0fb18-6efd-31a2-9a34-ef0ba9d55cd8 | -10.0906 | -50.2154 | 2025-09-30 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5115a0c4-1760-3c28-97db-15e8a9304514 | -4.8915 | -43.4678 | 2025-09-30 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bdff646a-2136-3f7a-a1e8-70e8383022b1 | -10.2041 | -44.8915 | 2025-09-30 03:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| a9b0b152-16ba-3ef0-8a46-2c1b9542e4d2 | -4.39944 | -44.08061 | 2025-09-30 03:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c8d3540b-67cc-3397-bdec-815f1d5de6f1 | -8.06577 | -42.94618 | 2025-09-30 03:25:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4def96e-d089-3f83-bbde-528b1de81ce1 | -5.42033 | -42.29479 | 2025-09-30 03:25:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7ca76af-126b-30df-a080-e95d42bbc38e | -6.46122 | -35.08668 | 2025-09-30 03:25:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79cdcad6-3d84-3f30-9942-a93d102ce44c | -5.96497 | -35.58092 | 2025-09-30 03:25:00 | NPP-375D | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7856de5-2b1a-358b-b1e7-acf8fa12e38a | -6.43147 | -43.08433 | 2025-09-30 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d74c7ece-76db-394d-895a-bdeacd749832 | -5.97101 | -44.13375 | 2025-09-30 03:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4089e6e-ff7e-3a09-88cb-a144fffbcc07 | -6.40959 | -43.75678 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1f95682-fe07-3f90-9766-8e48a0272955 | -5.97242 | -44.12622 | 2025-09-30 03:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 780e7f3e-fb2b-3157-a875-df9539dd0add | -3.68102 | -38.93694 | 2025-09-30 03:25:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e52bf60-c3a4-3e65-a18b-401187d96e9c | -6.49058 | -44.26731 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bb0247b-bcc1-323b-a0c6-7424b98382a8 | -5.33248 | -43.73027 | 2025-09-30 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 929b08b5-94b8-3cef-9c8b-1759651976e1 | -7.91642 | -44.62104 | 2025-09-30 03:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e62d84a-7e26-3fbb-bc9a-1f11016c33fa | -3.67568 | -38.93604 | 2025-09-30 03:25:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab02b909-50c3-3b42-8378-d8667135ce2f | -5.03618 | -43.61193 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0092d4c1-e665-3f3f-8ab5-9c8c4454f423 | -5.52242 | -43.89026 | 2025-09-30 03:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 952c60ba-abf2-3a73-91a4-8d9d7b3bf594 | -6.83771 | -44.83183 | 2025-09-30 03:25:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab5fa0fa-943c-3b66-92ad-003129ae9023 | -6.09297 | -42.66116 | 2025-09-30 03:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6bfa9f8a-23df-3bdd-9a06-4e2ba55362d7 | -4.89285 | -43.47055 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f9df2737-ad73-394e-8c07-7841935ec99a | -6.48936 | -44.27376 | 2025-09-30 03:25:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ba39d411-33ae-3f14-9b49-418f85fc7cce | -4.89983 | -43.47167 | 2025-09-30 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 663c35af-700f-3b2b-bd87-0a9ae738a4cb | -6.43259 | -43.07847 | 2025-09-30 03:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fc7b3ea2-bff5-3c2c-9faf-8ea1b7273445 | -5.50949 | -43.88129 | 2025-09-30 03:25:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd33074-60e3-37b7-8a6f-de95fbc482d5 | -4.86878 | -37.45243 | 2025-09-30 03:25:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54bd35d9-43a3-31b1-9d91-16b6ecd88662 | -6.41031 | -43.75635 | 2025-09-30 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdf42113-4534-3da6-95e0-c8f40f2b5d44 | -5.18614 | -37.65891 | 2025-09-30 03:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4113a959-66bd-3c87-b456-83d499da6d6e | -5.52365 | -43.88354 | 2025-09-30 03:25:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4f424bea-d91c-3d9f-bc94-9a521b4141b4 | -3.88573 | -42.51973 | 2025-09-30 03:25:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34ee0ec2-8c63-368c-a6d4-b112f5bab12d | -4.79459 | -40.54903 | 2025-09-30 03:25:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e14d23ce-45e1-3d57-9f70-47e9f3e2244a | -4.46769 | -38.6082 | 2025-09-30 03:25:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fc4ade71-3240-39e5-b32f-0a3e1dcf2ef6 | -5.90794 | -43.71037 | 2025-09-30 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d2a757-f9c5-3452-8d61-d7af8d828777 | -5.7445 | -42.67205 | 2025-09-30 03:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README16.md)
