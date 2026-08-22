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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9340323a-acb8-31d5-80bf-2834674f598e | -16.28858 | -57.6666 | 2026-08-22 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 07d73513-faac-3b7b-a9a7-02353c03945e | -14.72583 | -47.13927 | 2026-08-22 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa708118-489f-367d-bba3-58d591e3faed | -20.63118 | -47.44167 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 1fc17594-ec88-30ab-b0a5-4e89e10ea9f4 | -14.40296 | -51.80446 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64c5138e-6391-38b0-82b2-10ba9344aed2 | -16.50298 | -55.18453 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e01703ef-7389-34ab-bcb1-6bcedb8155bd | -18.79209 | -43.77784 | 2026-08-22 04:29:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa4f2ac2-99af-3e8e-9d84-15eb9d616578 | -17.98749 | -44.41309 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97404e5a-d8d4-37a9-bd2c-0e2ce26fa47d | -15.63805 | -47.73096 | 2026-08-22 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e359240-fc98-3e72-8fc4-476113a993fa | -14.55521 | -53.0053 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15712774-5bc6-39bd-a769-bfe11aeb64f0 | -15.17478 | -48.74643 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| c44006b9-6302-3028-b6fd-6d548f09c8e5 | -17.91943 | -44.41803 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8b0fe0d-7815-3c70-a00f-5d5a13c7e47c | -14.01256 | -53.70201 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 354118ff-1568-369a-8beb-e98f00010e63 | -13.53461 | -58.1138 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6d5aa2a-3614-3c39-8afc-81bc08b65f8b | -14.54344 | -53.00329 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c594b4e-3e16-3eb4-a0c3-e40a3885a352 | -14.00505 | -53.67256 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ae18af-afc7-3f7f-99ea-43c2c703452c | -13.94396 | -53.84538 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4b0bdc9-7e61-387a-87bb-45b78affb7ee | -18.71506 | -47.58289 | 2026-08-22 04:29:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ce321c-5837-3a8b-99aa-8eeadc1ca3a3 | -13.95161 | -53.85071 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66186508-49c3-3b0d-a6b8-73d9167230e4 | -17.56725 | -47.88407 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb8bf9c6-62ca-3ab6-bdea-9efd9c4b9531 | -15.2056 | -52.77905 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0a45bc9-2bf2-3dc3-972b-2ab4d299a300 | -16.50215 | -55.18885 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9c3057a3-3b9d-37de-ae41-a2e0e80d41f7 | -18.27826 | -43.31424 | 2026-08-22 04:29:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01c12419-5dc6-3629-a145-e6304f903957 | -18.09061 | -46.94405 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a907f24f-935c-3f04-8ce0-048be92603f3 | -14.5543 | -53.01044 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc79a719-4565-3411-a6cd-873706b1359b | -18.91408 | -43.59648 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 876579d9-9f47-30b7-9700-4e15b295c7b5 | -15.21798 | -52.77607 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7d16002-34a9-34f3-b295-923840be53da | -16.19527 | -43.13084 | 2026-08-22 04:29:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 972160b3-ac67-3d68-adc0-1359992c343c | -13.99676 | -53.69511 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3662eb3-e02c-3881-9d95-3786cb6c7679 | -14.9746 | -52.65863 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efae2133-13b2-34d0-aa23-762a69a89802 | -15.07273 | -45.32647 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e3f6b28-df77-3cec-9325-eb328051d27b | -15.17865 | -48.7434 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1eabeca4-6f5f-3f7a-910f-a176a34f347c | -16.03591 | -52.16798 | 2026-08-22 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddc6e647-c24b-339a-b3c3-0974d66d41d2 | -15.17259 | -48.73874 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7ad096f-f43a-38cd-a2c1-6d71da4a5809 | -16.7427 | -49.32716 | 2026-08-22 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 813c7979-aab0-3799-936b-fa5f05b7c252 | -15.33007 | -53.80817 | 2026-08-22 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce5ce89a-2b0e-3bd6-81e1-9b96dbf4108d | -18.27455 | -43.30982 | 2026-08-22 04:29:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dd7aee2-698e-3777-9771-11094538d430 | -15.53743 | -47.31601 | 2026-08-22 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c129e9f4-5810-3cb5-baa4-8a51138ca692 | -18.7642 | -43.80122 | 2026-08-22 04:29:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e900959-1478-37f1-b245-1334ed564a7a | -15.51689 | -45.86003 | 2026-08-22 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684073f1-e0c1-36fd-b8bb-026ec99d5b0b | -18.63683 | -43.92608 | 2026-08-22 04:29:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 470a8d0b-bd5f-3587-8355-9a2da5b59452 | -16.43171 | -39.51751 | 2026-08-22 04:29:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b6cf358a-c815-3c36-b055-949ca69b900d | -17.5667 | -47.88774 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68616884-bf9d-3419-883c-ebf757b46673 | -14.72529 | -47.14291 | 2026-08-22 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e0a7d21-a99c-3069-ac88-1c9e65a6498c | -18.68355 | -47.36946 | 2026-08-22 04:29:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3147461-694f-335c-90ac-4aacb5b19a19 | -13.99679 | -53.67117 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1da26c3c-d843-3dab-a5f7-322b8180bb84 | -17.56335 | -47.88719 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b485239-4ff4-338c-9ea9-d8e4f03a0a47 | -20.62772 | -47.44108 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2de495dc-ae91-33d5-98cf-ecb8cd5a5573 | -14.98729 | -52.67632 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f217ef9e-f67f-3441-9440-4758d0c0cd6a | -14.32097 | -53.00561 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12baeced-d341-3a78-93f7-fdd021832a67 | -13.87961 | -53.98402 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8cc550c2-4e91-3209-8726-ebcbf3041d62 | -20.63407 | -47.44619 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 3a242e58-09e9-3b96-a553-f0a32ad1a5a2 | -17.96356 | -42.72972 | 2026-08-22 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 5eeb7261-2996-353f-a57b-38dcaeb3a5aa | -14.39562 | -51.80316 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0ba3956f-ccba-34c8-a5b5-5ec0fc5ffe57 | -18.53066 | -48.2515 | 2026-08-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3904da81-c07b-312c-87df-7aee010f66da | -14.00575 | -53.66861 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a3c6c1a-0344-3c90-a85b-28bf12c24edf | -13.99267 | -53.67044 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da9ab220-8774-3a35-b914-551e5863f4cf | -18.34524 | -42.46351 | 2026-08-22 04:29:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6273e406-b9c7-3360-92df-fe89c20c4475 | -16.57287 | -49.36819 | 2026-08-22 04:29:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cc83a04-c637-30b0-aafd-b92741820fa2 | -17.92331 | -44.41867 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de9acd77-67e4-3cf3-b420-e238c2bd9bca | -13.99263 | -53.69436 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e008b03-9b4b-33bf-808e-9b285c7ed6cb | -15.17534 | -48.74286 | 2026-08-22 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d65e021a-14c7-325b-bb75-8eb4234859de | -15.19431 | -48.23081 | 2026-08-22 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d9069d6-9e2a-37c6-b6cc-faa97c39e608 | -19.64893 | -46.03786 | 2026-08-22 04:29:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd087be-5239-3162-87d5-49c7b88119a5 | -21.02468 | -44.19667 | 2026-08-22 04:29:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 5ce68f2f-d671-3a68-ab17-a7e543c65344 | -13.878 | -53.99263 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f73580c-2331-3b4b-9901-6c2371d614d3 | -14.72863 | -47.14346 | 2026-08-22 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4228169f-50a5-3c00-a0bd-cd34c2210208 | -15.24576 | -52.84273 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d1ff150-b4db-32b6-bcf9-75dccf553b5e | -17.96157 | -44.39912 | 2026-08-22 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0348bc-df07-3dfb-9199-12ec482ef2d5 | -15.98482 | -44.80582 | 2026-08-22 04:29:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f392747a-7b7c-3e76-922e-88f043acba99 | -15.34055 | -52.92398 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b1bf30f-b150-345f-b81a-f445537c22a3 | -15.3393 | -46.06656 | 2026-08-22 04:29:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ace7413-4dc3-3e23-b1e3-eb52529f76cf | -18.58817 | -42.7477 | 2026-08-22 04:29:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dfa3bf40-0758-341c-a81e-43feff3c10d7 | -18.08661 | -46.94742 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 802859a4-4a89-31b9-9458-fd0b0bc64739 | -18.08725 | -46.94859 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1369724c-6e46-3a51-b4e6-3f9242ae26f4 | -14.01324 | -53.6982 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3ad40af-425a-36be-b2e3-8a0e51abe340 | -16.61259 | -49.39716 | 2026-08-22 04:29:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cbe5565-246e-38e3-923a-e1cc2e086d4a | -15.81147 | -38.91325 | 2026-08-22 04:29:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fb98254b-1d8b-3a70-8cf9-a9ed145a9ea1 | -15.24786 | -52.85335 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5e0a17a-ac34-3b0a-8e18-797d83abfac6 | -16.48907 | -47.94174 | 2026-08-22 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f560294-c19c-382c-aa53-a93c59ea8cf6 | -17.59344 | -44.31405 | 2026-08-22 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d4b7418-fdf6-36c0-bc96-34c0631511c3 | -14.00645 | -53.66469 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae9fc5c7-6e90-32aa-a727-c01a29e32095 | -20.63809 | -47.44276 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 908ba009-f9ef-34e0-83b0-80ccf57c564a | -20.63463 | -47.44222 | 2026-08-22 04:29:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 061d8163-eff9-3af2-b51b-90eb71c2f85a | -14.56364 | -53.04938 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0cfe9dc-2283-31dd-a5b4-ce8573e132be | -18.58089 | -46.91785 | 2026-08-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0baefc33-32f8-3549-803e-4a92a09496e2 | -17.56391 | -47.88351 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 294c78c9-7d13-358e-a409-5e17a0608d77 | -13.95509 | -53.85529 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9fce188-bf5e-3174-a8cb-2a51a50a1870 | -14.56122 | -53.01709 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58ed39e9-ad94-3024-a317-d109f807eed5 | -14.0715 | -58.81754 | 2026-08-22 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4e6600e-7223-3116-b046-380b77d1f39c | -19.78244 | -45.66188 | 2026-08-22 04:29:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a933629-bda5-3fc8-890a-8fb6f3e090d8 | -16.19115 | -43.13029 | 2026-08-22 04:29:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b116d341-d1e4-396a-b773-f2e5e8c3f4e6 | -18.34468 | -42.46806 | 2026-08-22 04:29:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d32e2694-c204-347d-ad73-7e0f58650f2e | -15.06668 | -45.32729 | 2026-08-22 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5976c044-a180-368e-aa9c-5555e402eecf | -17.59302 | -44.31251 | 2026-08-22 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2b70d8f-5cb6-363a-8fb1-1f25c68a6964 | -13.54117 | -58.1153 | 2026-08-22 04:29:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bf73619-dff4-3c0d-a37c-2fc1c9d02e96 | -14.56188 | -52.99033 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88872f1b-069b-3c40-a6a7-3eeac1da6edf | -18.72985 | -42.22563 | 2026-08-22 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd95f34b-e2ba-385b-b68b-fc26fc625812 | -14.00092 | -53.67186 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8be26b67-831f-3b5b-8f06-d7cd376a4ecf | -15.5163 | -45.86409 | 2026-08-22 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f56b4060-ab85-344c-a018-9c1338cc946c | -17.97487 | -44.35852 | 2026-08-22 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README34.md)
