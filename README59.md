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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 309ae5fa-2a63-31f0-add6-56f8df9748bf | -19.05108 | -54.0155 | 2025-10-25 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cc55b22-e854-3d83-ba9c-dd200d2da4d4 | -18.16505 | -51.75291 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da690826-4b25-3d09-99e6-91667e5c395b | -22.83739 | -51.35465 | 2025-10-25 05:14:00 | NOAA-21 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 34f4748f-53e2-3c7e-ab98-a259ddba0c8d | -18.16665 | -51.75864 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| af56ee80-2646-3c05-8bed-2498ee335f31 | -19.65214 | -53.56203 | 2025-10-25 05:14:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d836a7a-12a4-3ee6-8e08-286fa9ac9f90 | -18.47488 | -48.05385 | 2025-10-25 05:14:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ad30923-370f-32fc-81fc-126ae79419fc | -18.56147 | -50.27475 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 618895e4-4424-371c-a7d5-d3e4406e04e0 | -18.17095 | -51.76485 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 530c31f3-9132-33d8-b4c4-513218ab209f | -22.15252 | -55.27469 | 2025-10-25 05:14:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ee785ce-4d9d-3ba5-8f8f-aeb348231fca | -18.17425 | -51.75958 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c8b79e95-41e9-3643-96ce-b3a1c4692dec | -22.83171 | -51.3576 | 2025-10-25 05:14:00 | NOAA-21 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0436a610-5542-35b5-a0b1-333a135396e7 | -18.56731 | -50.27152 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7fd0af22-2f84-3259-aa13-d783075c9712 | -18.56692 | -50.27536 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ecfb4163-4f02-3a03-9228-7cc8ad204bbf | -18.17066 | -51.74757 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fb8437c-e4e1-378f-9cd5-f6e6a40b227b | -18.56653 | -50.2792 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ed91ab5c-86b7-32f6-904b-003e5c022fe8 | -18.554 | -50.27782 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7fc820e7-37d6-36b0-9aaf-e81328099e5e | -17.94731 | -57.62046 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ab66a38b-b272-3c22-8ccc-e1e07a9c2de5 | -18.16932 | -51.75909 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d5778a0c-8bee-3fcd-8446-7a7113cf1e38 | -19.76846 | -48.28868 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02567109-49d7-3a3b-aec8-c0db66c9c508 | -20.50883 | -54.57843 | 2025-10-25 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2084b3ff-a6f9-3057-8e01-50a3256564d6 | -22.83242 | -51.34996 | 2025-10-25 05:14:00 | NOAA-21 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| fe597d2c-77f0-392e-9546-f7d04d1aa767 | -21.04902 | -47.33127 | 2025-10-25 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f06bce5-65fc-3ff6-85b7-9087fbd5959f | -20.44271 | -46.58263 | 2025-10-25 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 184293e2-807e-3e79-9ad1-bfcc3952cfcb | -18.47535 | -48.0487 | 2025-10-25 05:14:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2d30c19-dcf2-3414-88e7-8f065e3bd993 | -22.1484 | -55.27413 | 2025-10-25 05:14:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b264d643-1560-34bb-aaf6-e9fd52f57b73 | -18.16603 | -51.76429 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e5fc0ee4-fe50-33aa-b4fc-021b8ee62632 | -17.95135 | -57.61703 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 97541f1c-7c93-303b-9503-e983026488cf | -23.39399 | -51.12922 | 2025-10-25 05:14:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5735f56e-2e30-3bd6-80a4-5b548724202c | -20.4362 | -46.58266 | 2025-10-25 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b718396-a948-3fee-a1e0-0fcba69f94fc | -19.76221 | -48.28809 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56f5f196-adca-3a1c-8b7b-2f7652263ac8 | -17.81272 | -57.62889 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 66a50494-31cf-3a74-b174-9bc35cf725f4 | -17.94789 | -57.61649 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7507a327-d42b-3094-ad58-22135290e625 | -17.96278 | -57.62637 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6c9aee90-28e9-3964-8697-15add00b29fb | -26.17934 | -51.73104 | 2025-10-25 05:16:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d9aaa30-f8f0-3ad5-8b42-1f62c1c6988a | -29.10663 | -50.31878 | 2025-10-25 05:16:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 86027e58-42ea-38cd-adca-2b6a4e5a2eeb | -24.98633 | -51.52604 | 2025-10-25 05:16:00 | NOAA-21 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2df78ad1-5c97-36c9-930d-20b8e0c2ad11 | -26.40248 | -49.91238 | 2025-10-25 05:16:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9c3b00bd-2f3f-3c4e-b2b9-96150465807d | -25.04391 | -49.71439 | 2025-10-25 05:16:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dda9f6df-e6df-3c6b-89c3-a3e146bc6610 | -24.80866 | -50.22902 | 2025-10-25 05:16:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 16ea0b65-6afb-3b0b-a81a-143c43e9525f | -26.40285 | -49.90741 | 2025-10-25 05:16:00 | NOAA-21 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 51c5c3a6-aecf-3ca2-87f7-d1c442d9c63a | -26.17902 | -51.73486 | 2025-10-25 05:16:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83b2bc3c-e48a-3916-9b22-63df8d579c3e | -2.8149 | -49.1354 | 2025-10-25 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9542f5c1-956e-3002-a351-60cec400a3a8 | -2.7964 | -49.136 | 2025-10-25 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7ef277f4-2bc6-3e93-a75a-400ac154cd0e | -2.8149 | -49.1354 | 2025-10-25 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| c29550c9-e737-388c-ba54-8f7b15f85812 | -2.7964 | -49.136 | 2025-10-25 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4dc3eb43-fb16-3106-b42b-166adc0981a6 | 2.07822 | -55.72168 | 2025-10-25 05:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9109a60c-f06d-35a7-a301-2ac9a7f0fc2d | 1.43464 | -50.89386 | 2025-10-25 05:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26cb9522-3edd-3928-840d-1df02752b31f | 1.42857 | -50.895 | 2025-10-25 05:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9500e34-0a26-3b9a-8aa0-f0b1610dc73b | 3.88718 | -60.12606 | 2025-10-25 05:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ed9394-8e69-31d9-b230-d635e7758671 | 2.07483 | -55.70116 | 2025-10-25 05:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 942b87ca-2c9d-35b0-acc4-792f3056bbef | 4.66691 | -60.51005 | 2025-10-25 05:36:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75ee4bf4-aeaa-313d-8135-02c6572c11fa | 2.08326 | -55.72512 | 2025-10-25 05:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6733fb90-45bf-310d-bc10-8ad49cd0e168 | 3.88381 | -60.12655 | 2025-10-25 05:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae845887-25d4-325b-abf3-56cee4b5278a | 3.88544 | -60.11517 | 2025-10-25 05:36:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b42e50-a712-3ee4-aa37-59536f67d3de | 3.13785 | -61.01066 | 2025-10-25 05:36:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 047bac73-a5e2-3c1a-b034-acee039cb6b3 | 3.91982 | -60.55922 | 2025-10-25 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a408c260-b4ba-3c9a-8203-062000d0e1f3 | 2.07458 | -55.70368 | 2025-10-25 05:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783fcce2-f1ca-38d5-ac02-4fe1e113007a | 2.07549 | -55.70517 | 2025-10-25 05:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af7c672f-be54-3820-b04c-e779cfc15833 | 1.63621 | -55.73893 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb39f952-da5b-3ab1-972b-c46e4127e81b | -4.83127 | -50.93587 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaf1b20f-bd5f-31f2-a58f-7366e9ee1876 | 1.64626 | -55.71831 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55cd0ce8-e1a2-3e35-89a2-8189916a0c10 | -1.5878 | -54.30844 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cdf9fd6d-e791-334b-bd1e-9a3988051386 | -4.84058 | -50.93673 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2923094f-f7d6-33e0-8a1c-b31c0e58e938 | -1.59625 | -54.30732 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 357bd1cc-6743-3c8b-a0be-7507267728cc | 1.64254 | -55.72324 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7dfa50f7-0432-327e-bc05-36e804cc728f | -3.11681 | -49.10677 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d29b412-4c1e-339c-a0be-29a5647e6c36 | 0.45257 | -51.0159 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb889650-72da-38c5-9490-b3fa879e1512 | -2.85534 | -50.74287 | 2025-10-25 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05520322-1f74-33e7-8dac-3e4ece35b8f7 | 0.44645 | -51.01557 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7a939f-0ebd-34ed-8c37-c011937d3a37 | 0.44641 | -51.0168 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f6880cf-bd5a-3770-87ec-d78882d865bd | -1.59288 | -54.3093 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2950e68-2e4d-3f88-b789-f4ba119c6d14 | -2.8008 | -49.14927 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf786695-0a05-39f9-93e6-eb047943340b | -1.59337 | -54.30624 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06ac0a55-92cf-3dc5-8678-b8351f5fc769 | 1.6327 | -55.74641 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 839d41db-e6fd-3612-a338-fa0c815e7569 | -3.4344 | -50.26217 | 2025-10-25 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de769a30-7c40-3a0b-be6e-7569efc5f493 | 1.55566 | -55.99488 | 2025-10-25 05:38:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1433879-c23a-3bcf-ad0d-c11cb4cbd581 | -3.82998 | -50.20058 | 2025-10-25 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1990e20e-c569-3e64-80a3-43e72a37fb64 | -4.82807 | -50.92934 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7fef0ad-8dda-3486-be60-ea232d5158a6 | -2.80187 | -49.14222 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c74b3cb9-7701-3f1d-b441-89ebfaa26f22 | -2.81083 | -49.14929 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07eb962d-0c98-3b47-9523-025e18097720 | -3.11768 | -51.2069 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eadd4629-05f8-3dbd-af38-8d897be88b11 | -4.84456 | -50.93783 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b016477e-5ebe-39fc-95fe-c14874cb2916 | -4.82728 | -50.93488 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02098683-54c2-3973-b16a-07e12d2bc566 | 1.63337 | -55.75064 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c66e3236-12d1-3196-8736-c75743c386a8 | -2.81184 | -49.14233 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba915a20-d21c-35c7-9133-230acf07b522 | -2.80369 | -54.3805 | 2025-10-25 05:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc264130-d55e-39a2-90e3-261b6cc29636 | -1.5907 | -54.30952 | 2025-10-25 05:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fabdf31a-63ca-3aae-83aa-e6f9de0f9ac9 | -2.80568 | -49.13421 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c36ee57a-83b4-3d1f-8f78-d28eb06da202 | -4.83473 | -50.93022 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d850c5c1-8f82-34a4-baeb-a89461e7d592 | -4.83868 | -50.93124 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d9eb860-555b-3f57-931c-5e9ae137534d | -3.83087 | -50.19438 | 2025-10-25 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f22161b-0092-31e3-86eb-92af406f59d0 | 1.62291 | -55.76963 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800dca43-2d78-3726-852f-cfd068f83110 | 1.64289 | -55.72489 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37c80d5e-508d-388a-84b4-85b261263c85 | -2.808 | -49.15026 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 483e726a-4b72-3b25-92e8-1348859f66ec | -3.11693 | -51.21206 | 2025-10-25 05:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ce78806-78d6-32cd-b228-54c174c72aaa | 1.64659 | -55.71997 | 2025-10-25 05:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c045dd5-2b66-3248-afc2-2a871a574c1e | 1.5643 | -55.99355 | 2025-10-25 05:38:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11039532-37e9-3778-969a-676280ebe713 | -2.80293 | -49.13527 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1084decf-19c8-3c17-a97f-1bcce3651c82 | -3.12503 | -49.10105 | 2025-10-25 05:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eda0f42f-5830-3fdd-9811-43695f73140a | 0.36205 | -50.92268 | 2025-10-25 05:38:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README60.md)
