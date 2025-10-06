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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a015173-943a-3f6b-8db4-a4097b6ef709 | -13.68522 | -47.30938 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e4b0d1f-a90d-3eba-b3c7-bbb764c8ede0 | -13.33165 | -48.05195 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e53e34d-40d4-32de-8594-2b3a7b24d143 | -17.95982 | -57.53398 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 0159076a-1cc2-3be8-b122-719267b6eecd | -18.24762 | -53.36723 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 731ab29e-8854-3524-9827-2fd1a56a63ab | -22.15057 | -51.46524 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b47ec00d-13ec-3054-b513-047d415016a9 | -18.10746 | -53.40953 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f05acbe-1929-3521-8457-df729a6a24ea | -18.3925 | -45.21938 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4d38aa3-9527-3eeb-bf50-9640544cbe52 | -23.39123 | -45.39159 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3e95e497-b788-39b1-aa6d-653010f8725c | -18.1388 | -53.41008 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 425c1f0f-06dc-33b0-8df5-a3783a73a1df | -23.39904 | -45.3921 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7f5bd0c3-dd9d-3f7a-b5cf-46e65cb06dd7 | -17.89991 | -57.65049 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ea039f10-ff26-3194-b4f1-9615a6f8933e | -15.99446 | -56.00943 | 2025-10-06 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 795d94ee-c2b6-3e55-b32a-5d8ead7805e0 | -17.68049 | -52.23931 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa45ceb8-a18f-3f06-b810-2a1fcaca7d2f | -18.0042 | -57.59507 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8e5a850b-e4fd-3717-9f65-431cc1d6f2dd | -21.10789 | -44.20618 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4f97c8c4-8993-37b4-85b7-3f122500b23b | -18.24338 | -53.34705 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 953c9280-95dd-30d8-94d2-962b3125f678 | -18.0034 | -57.60269 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c71b8a64-719d-3370-a3af-2c2829c7162c | -17.34887 | -46.8272 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6780bf65-fae7-31dd-a4bf-eb8eaa0f0237 | -16.95606 | -52.6877 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21e48bc0-fd35-3153-b8dd-7bc1aefae49c | -17.97191 | -57.60178 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 21c6b50f-f2cf-3047-9d42-c2d46fea0022 | -18.24081 | -53.36152 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 292a1edd-ed8b-3826-8e09-af46118d43f0 | -17.98476 | -57.5377 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| e3014193-5333-363a-b6ce-c74e7262c8bb | -19.02956 | -50.65644 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35733c30-e313-3f5f-aedb-24fe25597378 | -15.3155 | -56.9232 | 2025-10-06 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7205569-95c7-3f62-a7e2-99d719ba06be | -18.38877 | -45.21892 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32d02754-6699-36b4-9f9a-097c16f3bc8f | -17.60351 | -44.44934 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 434897c7-8861-3a14-8699-3394245e670e | -21.81245 | -43.36267 | 2025-10-06 04:29:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67a1aeb1-fb38-3a82-a882-d2556a086c0e | -22.12549 | -45.01302 | 2025-10-06 04:29:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4f841d84-0320-3c01-97a9-2d72f9ea1504 | -20.00086 | -45.79427 | 2025-10-06 04:29:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 582725f8-4f92-3b53-ad8c-547377bf145a | -18.27562 | -53.31953 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b53ab777-4462-3dfe-abce-39690a1e229f | -17.98119 | -51.14725 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa51bf68-29f9-3206-b618-2892c47903be | -18.27298 | -53.33402 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d40e872-6203-3f5a-81b5-58d02fec610e | -19.93986 | -44.64519 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 69bce8ff-2e73-35ea-9e7f-c4d1a404fbff | -17.67899 | -52.24804 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 74e60f2f-2a65-3f8d-996b-45b665c402da | -21.38507 | -45.05591 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 49b254db-eff5-36ea-b8a7-a6b58376be7a | -22.95605 | -46.13343 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 04e5d541-95d6-3d96-a5d5-012fcd8bb2ab | -21.36137 | -44.50637 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9deef9de-b8f7-3ce8-a8c7-76ecf74da77a | -22.9901 | -46.14474 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b548126-de4e-33ae-a153-79907e2cceac | -22.82174 | -45.53565 | 2025-10-06 04:29:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| aeb9581f-60a3-3814-93da-99e1fe6c21cb | -19.62528 | -45.91955 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4c1abd1-81a7-3fc2-ac04-57c09054597e | -18.25723 | -53.35606 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9c1e132-1016-32b8-815f-1d05987832f6 | -19.62665 | -51.59585 | 2025-10-06 04:29:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93d1e395-53b8-3823-adbb-550ff6e52876 | -22.96814 | -46.07051 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a5ebb9d2-da40-3325-8ee8-f18bcd721908 | -16.45249 | -52.16141 | 2025-10-06 04:29:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b810e197-6471-3142-b7ac-55618892823c | -16.14716 | -57.57224 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0c72dc2d-d1db-3c1b-8260-a32b2cb030aa | -21.86646 | -48.28826 | 2025-10-06 04:29:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf319a9-19cd-33ed-a38d-5693da178b63 | -20.42965 | -48.86075 | 2025-10-06 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d5feaa9-e015-31e4-b30b-df0feccd6299 | -18.11301 | -53.40044 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c58c71e-910c-38ea-9b46-4abeb98e40de | -23.14584 | -46.12926 | 2025-10-06 04:29:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 72b68c0a-1b55-36ec-958a-cac3dbb67584 | -21.31915 | -48.66515 | 2025-10-06 04:29:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ccd79b20-561c-38c2-acd6-872d453b1be2 | -19.01972 | -45.03261 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cc82faa3-d9d9-3b8c-80d0-980610e733e3 | -19.01658 | -45.02732 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0017259-d30d-32a9-8391-c1124863b133 | -19.93593 | -44.64474 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 5328eec4-fa0c-31ea-9157-b1d4b593091c | -17.9886 | -57.59937 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4c5a1ed7-1ddc-3d09-831b-57bba3b6be1f | -18.25062 | -53.32825 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 31ccabbe-7bd9-3420-a817-6c6690208ab8 | -22.38078 | -49.96788 | 2025-10-06 04:29:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c03db3d5-e476-37c2-9e5c-db0396f9cc28 | -18.19183 | -53.37271 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 670b2f1b-bb5c-3664-bd1f-edca1f42b1c7 | -17.95479 | -48.55159 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 964330b5-5cb2-3df6-b3b8-add694034f66 | -21.1755 | -43.56963 | 2025-10-06 04:29:00 | NOAA-21 | SANTA BÁRBARA DO TUGÚRIO | MINAS GERAIS | Brasil | 3157302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 62d8580a-c723-32a4-8685-f285aa74708c | -17.96226 | -51.1761 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 354c846c-12bf-398e-85f3-3d88d3fcc562 | -19.01991 | -45.0303 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf1d90c4-aee5-3fc5-bf52-3b8a4f9076cb | -20.12185 | -44.40822 | 2025-10-06 04:29:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90b8a8a9-753b-39cf-b3b7-3277d7c394d8 | -18.12162 | -53.39619 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a56bcf03-bfb5-34d5-b825-0aa2be106c3a | -21.72483 | -50.07246 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5c13c5d2-4559-3467-85cc-202f97f11f59 | -17.84002 | -57.63769 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9ecf6544-8fbb-38ff-be2a-bf042160e9c3 | -20.34984 | -47.18449 | 2025-10-06 04:29:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66189895-8b13-3991-a323-dac3aa74fc08 | -18.18055 | -53.3701 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9f54089-6fb0-3e64-8ecf-0a499eca41b5 | -17.99719 | -57.60437 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a3bc87b7-a988-30d2-aa94-55bb31383719 | -16.34889 | -51.45283 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc42a631-7e5d-34b7-93ba-67db5d9329d8 | -17.92825 | -57.61326 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 18fa56f5-6799-33fe-b687-4da8e62a27a9 | -21.70386 | -50.07628 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7776ef69-6db3-3245-bf4c-467dd1bdf590 | -21.38554 | -45.05721 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6b2fc34-aed1-348b-babd-0e619effbf06 | -18.17593 | -53.37397 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28fa3b27-1eef-3c94-a5af-2af8f2cb0976 | -23.18568 | -45.63362 | 2025-10-06 04:29:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 8552caa5-419e-37d5-9f63-cabd1f6aa6ef | -18.13849 | -53.40711 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 017f32d5-26a9-3e03-924f-37119748919c | -16.95896 | -52.6931 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1cf30c31-2dbd-387f-b793-1c352d76907b | -22.9932 | -46.1503 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7c14950-4e5d-3ad7-9d6a-4b2aea6aa9d8 | -16.96217 | -52.67455 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96859da6-03dd-356b-bb58-b867bb22341d | -18.18983 | -53.36208 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aecc5327-2bb7-3135-8a24-47b59570cadf | -18.39188 | -45.224 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f83dc96f-ef66-36e0-928c-76c0bb835431 | -20.20653 | -46.14627 | 2025-10-06 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8cb9d5d3-5125-3ae6-b2a6-fdf73d55dba4 | -17.84557 | -57.63591 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5673069c-a12b-354f-82b9-a49cdde2140f | -22.37986 | -50.01734 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1354312d-aabc-3e47-804a-9eb5b118959b | -16.36664 | -51.49805 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d644d6f-d8ee-32d7-8760-e86dbffc1c65 | -21.36539 | -44.50697 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b976790-0105-3685-a747-f6c559aaa7c5 | -23.17597 | -46.26026 | 2025-10-06 04:29:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 98d4cf70-72b8-37f7-9280-8f38e4ec2be9 | -17.95479 | -57.53339 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 418c011a-a0b6-3640-8a60-bbef0acc233b | -17.99454 | -57.54596 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8b617f19-b259-3427-a493-a1b10e87e0ca | -22.00983 | -49.75058 | 2025-10-06 04:29:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bae55caa-6a92-3f18-9748-9753a4df6376 | -18.13411 | -53.41434 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ca49fb20-ed27-3852-b0c9-1f8875b8c4ee | -18.81089 | -54.96189 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4a71c08-163f-3f90-bfea-32c2aa6b95dc | -18.13492 | -53.38757 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eba2d581-5f61-3039-bdfc-a5080f8945f3 | -17.83858 | -57.61917 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 441af47f-31be-3ab7-b55a-ce47721ed61e | -17.84107 | -57.63253 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d914d1f8-3142-3e87-ac40-22b9b9491460 | -22.29488 | -49.90739 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3b76cc99-1796-3521-9b72-ddddac8f1a8a | -16.36167 | -51.48451 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00633d77-2189-3c9c-86a5-a0b747452919 | -19.01612 | -45.02979 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e283b4b-1bb1-39fa-bcff-6becd93040fb | -17.38725 | -53.59476 | 2025-10-06 04:29:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1188165-0a22-3dc6-a53a-017e0d0b8dbc | -16.33904 | -51.468 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1cdb04-e866-372b-bb29-2c101fac3330 | -17.66446 | -44.43311 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README55.md)
