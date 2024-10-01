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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7eb0d3-a552-34ef-92f6-a991c6518ab7 | -23.06551 | -45.40795 | 2024-10-01 00:43:00 | TERRA_M-M | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 62203880-ba26-3b9d-8637-d0a61d89aa1a | -22.38062 | -45.80162 | 2024-10-01 00:43:00 | TERRA_M-M | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 115b6235-05f6-3f32-b313-b5f1dd5cc6e8 | -23.10413 | -46.59151 | 2024-10-01 00:43:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| e6f34efb-948d-3ed8-b15b-9f14e84be37a | -22.72756 | -46.67969 | 2024-10-01 00:43:00 | TERRA_M-M | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| 15010ce3-86cf-3cec-a6f4-17a1602dc8ea | -22.12394 | -48.56997 | 2024-10-01 00:43:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 7580ae36-c6f8-3b5d-bae9-07d84ac69e4f | -22.12203 | -48.55172 | 2024-10-01 00:43:00 | TERRA_M-M | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f22a0e36-45c4-3f2f-a6d4-b6bd642833f1 | -21.85943 | -47.17765 | 2024-10-01 00:43:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 52d4fa15-d14e-3992-8b98-2890675c0142 | -21.85787 | -47.16365 | 2024-10-01 00:43:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 187e89f4-9420-3cd0-b4b9-7c694b7a0f2a | -22.38141 | -49.31217 | 2024-10-01 00:43:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| f3dbbf0f-43ab-3fab-8ab5-255103171202 | -22.37079 | -49.3339 | 2024-10-01 00:43:00 | TERRA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| a8dd2b61-542d-3b37-83f7-8f2327d489fb | -22.36994 | -49.34053 | 2024-10-01 00:43:00 | TERRA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| ab64fd8b-d9f0-374d-bdb1-f39ea488d1a5 | -22.36882 | -49.31383 | 2024-10-01 00:43:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 283.3 |
| 9b8dd21f-0f55-3fad-96f6-435bf6093241 | -22.36782 | -49.32034 | 2024-10-01 00:43:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 217.0 |
| 53a9dbd6-aa11-304a-b232-9aa2e44fadcc | -22.36574 | -49.30063 | 2024-10-01 00:43:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| b96df1c8-40cc-39e3-a9c8-fdea915a0bc7 | -22.35622 | -49.31541 | 2024-10-01 00:43:00 | TERRA_M-M | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 873ed66e-45c8-3e99-a7a6-4647d2c58539 | -20.08301 | -51.3462 | 2024-10-01 00:45:00 | TERRA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6596eebe-04b6-397e-82cf-722f8e10e949 | -20.06878 | -51.34813 | 2024-10-01 00:45:00 | TERRA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 27.3 |
| fe48b0e0-e47f-3997-a405-a62ad2a7cda0 | -18.60627 | -53.07748 | 2024-10-01 00:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cf4c7628-b747-38f6-9a1b-29fb3fedbf41 | -18.53567 | -53.18938 | 2024-10-01 00:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b4461850-ccd9-3aad-8677-bac074b4bc22 | -20.81466 | -53.15451 | 2024-10-01 00:45:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 71e484f4-0f86-3f78-9880-d02fb4718159 | -20.81157 | -53.11652 | 2024-10-01 00:45:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 2c3a75a6-25c7-3bcb-a193-7ed25cfe6279 | -20.80836 | -53.16045 | 2024-10-01 00:45:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 35.9 |
| ceee2497-396f-3e49-a9b2-2dbffdaccd8f | -20.80505 | -53.12262 | 2024-10-01 00:45:00 | TERRA_M-M | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3d502c38-8906-3cf0-88cf-2c1c7e64c882 | -17.7234 | -42.35693 | 2024-10-01 00:45:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7f9b11fa-d6f8-32eb-a22c-c2f3c2df13fe | -17.72198 | -42.34715 | 2024-10-01 00:45:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3be9826c-ca56-3b54-a81f-9165bdaccbe3 | -17.32125 | -42.63486 | 2024-10-01 00:45:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d6b8c7a7-5572-32ec-ad5e-d7e771986e90 | -17.29652 | -42.65509 | 2024-10-01 00:45:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4b4ab818-d2ab-3bd5-a924-8527bb53152d | -17.29514 | -42.64552 | 2024-10-01 00:45:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f731ccdc-e3a5-3002-aa2f-7b37857eb7bd | -19.50091 | -42.3461 | 2024-10-01 00:45:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2c70c7c2-eaa0-3852-9ace-671f47453784 | -19.49193 | -42.34759 | 2024-10-01 00:45:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 407ee37f-4a3a-3b44-a6a6-4fc461573087 | -19.49055 | -42.33816 | 2024-10-01 00:45:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a7f4e153-5f90-334f-a433-6f949be34136 | -19.05367 | -42.95185 | 2024-10-01 00:45:00 | TERRA_M-M | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| bc8e71b6-da72-3aa4-b058-da107a65950c | -18.85129 | -42.57155 | 2024-10-01 00:45:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 3096016b-feb6-30cf-ae65-61e081e9e171 | -18.84991 | -42.56195 | 2024-10-01 00:45:00 | TERRA_M-M | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6abf28ae-a8ee-3782-b531-a4ff1c5ddb18 | -18.66803 | -42.26259 | 2024-10-01 00:45:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 61fdae60-42bc-3cd8-b4da-685f6ce63d50 | -18.66659 | -42.25281 | 2024-10-01 00:45:00 | TERRA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 95c12409-cb6b-3191-90f4-8390b52ece75 | -18.53276 | -42.6613 | 2024-10-01 00:45:00 | TERRA_M-M | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4b3b270c-99f9-3a3e-a10d-7b696dceb61c | -18.53138 | -42.65183 | 2024-10-01 00:45:00 | TERRA_M-M | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 75116199-2b8d-31c2-a557-f981bbfe6750 | -18.05168 | -42.9696 | 2024-10-01 00:45:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 72981245-f631-3ac4-a49d-e5b5178b7180 | -18.05033 | -42.96025 | 2024-10-01 00:45:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 011a3bce-2b7d-3449-ab33-45f6ffc1b0db | -20.46218 | -42.94954 | 2024-10-01 00:45:00 | TERRA_M-M | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f53379af-22ef-300d-98da-7183da3eb183 | -20.31379 | -43.1398 | 2024-10-01 00:45:00 | TERRA_M-M | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 436e9b38-f8c0-3d7a-9e6c-3a4602b80fec | -20.30493 | -43.14122 | 2024-10-01 00:45:00 | TERRA_M-M | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eb51a771-f136-3474-82ca-7700d5af3fe5 | -20.19122 | -43.51726 | 2024-10-01 00:45:00 | TERRA_M-M | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ba419614-8175-36ee-bc54-0c662fdf82b5 | -19.79389 | -43.16744 | 2024-10-01 00:45:00 | TERRA_M-M | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| efbe44c2-b68c-35f8-a4e7-10282b66f7b0 | -19.51388 | -42.88559 | 2024-10-01 00:45:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| ba895cb0-069f-3d23-b6bb-f91e3a8cb89d | -19.51254 | -42.87619 | 2024-10-01 00:45:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e77ed3a6-a3b1-3200-8385-fc5eb9705ce7 | -21.00882 | -42.84306 | 2024-10-01 00:45:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3976d81f-b074-3598-a6e1-d1cc8f615584 | -17.62022 | -42.98243 | 2024-10-01 00:45:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b852a1a3-008b-364f-b57f-02dd72b8d6e4 | -19.24799 | -43.35483 | 2024-10-01 00:45:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9a26ab93-477f-3c1d-8d08-6056effcf096 | -19.24669 | -43.34548 | 2024-10-01 00:45:00 | TERRA_M-M | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f21a1270-d975-31d5-9266-aebf4de143d1 | -19.24089 | -44.36866 | 2024-10-01 00:45:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a7c18497-9603-392a-aecf-b344fbcc0be4 | -18.66675 | -44.27101 | 2024-10-01 00:45:00 | TERRA_M-M | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 37df6147-3192-3601-b4c1-8e26b2743a6c | -18.62364 | -43.42385 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ca6dd479-3244-3a62-b615-52579e152bfc | -18.54298 | -43.37607 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 45e5ce39-71ac-380a-922a-d341ef5247f8 | -18.54167 | -43.36674 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 368f0061-23aa-36e0-b078-473ec3c6c2ce | -18.53836 | -43.47184 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| f48090ef-7685-3c0a-94c3-a46abd465634 | -18.53706 | -43.46256 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.2 |
| b2c1b814-71ad-398d-957f-3c05e9c86767 | -18.53282 | -43.36818 | 2024-10-01 00:45:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 99b4b3b9-26ee-37a0-821b-638006bb2ec7 | -18.27649 | -43.44615 | 2024-10-01 00:45:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a9b8192-3145-3231-be21-4e7c3cea4dca | -20.44948 | -44.5406 | 2024-10-01 00:45:00 | TERRA_M-M | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2d60cded-e03a-3957-9ec6-6ec306ca22af | -20.01713 | -44.53618 | 2024-10-01 00:45:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3a876b94-0f6a-37f4-afe4-79912622af42 | -20.01583 | -44.52642 | 2024-10-01 00:45:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 2076f468-5c8a-3ca4-8fae-ea66d13f4d1a | -20.00809 | -44.53745 | 2024-10-01 00:45:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| db720620-0317-3965-9816-4578a2a679ae | -20.00679 | -44.52769 | 2024-10-01 00:45:00 | TERRA_M-M | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 84a5f218-0505-3cf1-83a7-0565e9be1bfd | -19.99241 | -43.54181 | 2024-10-01 00:45:00 | TERRA_M-M | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5623bc65-84cd-3465-822a-48847bfab603 | -19.97663 | -43.9642 | 2024-10-01 00:45:00 | TERRA_M-M | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 7fc77869-7362-35b2-9045-3734acce91f0 | -19.97533 | -43.95468 | 2024-10-01 00:45:00 | TERRA_M-M | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| ecc2d4d7-c75a-3ab1-8e9c-23b259c47110 | -19.81256 | -44.24485 | 2024-10-01 00:45:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e68f15bf-f551-3284-91c7-aa33b0045b43 | -19.61073 | -44.11304 | 2024-10-01 00:45:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 04392c1f-daea-3d01-8f70-6caaed59169a | -19.08758 | -46.25206 | 2024-10-01 00:45:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 386e7fee-8892-3329-a6ea-0673f1bffbbf | -19.0036 | -45.9252 | 2024-10-01 00:45:00 | TERRA_M-M | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2a1acd3-db9b-3eea-b248-13745a82da13 | -18.81399 | -45.80265 | 2024-10-01 00:45:00 | TERRA_M-M | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 917c3abe-3288-371d-b5a8-76cc264169f8 | -18.8046 | -45.80404 | 2024-10-01 00:45:00 | TERRA_M-M | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c87185f4-7601-368b-b643-e340501f046e | -18.71576 | -45.48065 | 2024-10-01 00:45:00 | TERRA_M-M | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2bb09a1-7d3b-3eaa-8de9-4c4c426bf43f | -20.5371 | -46.29587 | 2024-10-01 00:45:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b718909-a2d3-3f72-ad5b-9584d1722c7c | -20.5273 | -46.29767 | 2024-10-01 00:45:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 2348e817-a923-3425-a421-a2a46dab057a | -20.51748 | -46.29929 | 2024-10-01 00:45:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c9b8634b-5839-3a01-b30a-63372fd23f0c | -21.31306 | -46.64938 | 2024-10-01 00:45:00 | TERRA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 02c1fa04-37aa-31ec-bca0-d0398b758579 | -21.3115 | -46.63647 | 2024-10-01 00:45:00 | TERRA_M-M | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 4f170a30-a764-3087-b771-e7ab67114382 | -18.09361 | -46.13754 | 2024-10-01 00:45:00 | TERRA_M-M | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 856ed7d0-b9c4-30f2-917b-7499a8384759 | -19.30317 | -47.44028 | 2024-10-01 00:45:00 | TERRA_M-M | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2d768443-fd24-3db1-9e47-e8116d9c7bb2 | -18.92709 | -47.03051 | 2024-10-01 00:45:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2e09dbf3-9898-3870-8011-b00714c7ffeb | -20.87507 | -46.98818 | 2024-10-01 00:45:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fd8ed1f7-726d-38c8-a0a8-7375cb9a37c1 | -20.87354 | -46.97521 | 2024-10-01 00:45:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c3668710-3a59-3400-b469-1ef275dbd9ff | -20.7206 | -46.89739 | 2024-10-01 00:45:00 | TERRA_M-M | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 93ad6872-3a09-300e-979a-6391b8c0c469 | -19.69421 | -47.23808 | 2024-10-01 00:45:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5195a1ce-0bb9-3b1d-9ea0-24116351117f | -19.69264 | -47.22479 | 2024-10-01 00:45:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 388fd5f4-aacc-3fb0-af6d-2786ca6543ea | -19.6915 | -46.70417 | 2024-10-01 00:45:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 564b25d7-173f-3b88-acc9-1f0f84465478 | -21.85381 | -47.16993 | 2024-10-01 00:45:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 568e3edb-f7cc-3f43-9077-4ab044a95848 | -21.59684 | -47.8001 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bd8b4591-9dc3-3108-b9dc-aded722cece0 | -21.59084 | -47.84784 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 474e30cc-1b17-3c95-b8af-7ace423501c3 | -21.58912 | -47.8322 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1061.8 |
| 75e88ccc-dba4-358b-b574-b565e4532149 | -21.58738 | -47.81646 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 473.2 |
| 3037811e-ec14-33c7-b532-d20613c64015 | -21.57969 | -47.84915 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 6563499b-84c0-36ee-9df0-a0135d7b9a30 | -21.57798 | -47.8335 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 437.2 |
| 88aa8d60-8dc3-3539-a5f6-1e4065cd5c97 | -21.57625 | -47.81774 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 831.3 |
| 4d454995-7078-3656-befd-0d3a0a27d196 | -21.57458 | -47.80249 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 304.2 |
| a9ab161c-3bc8-39ab-82d2-d6160adf1b43 | -21.57296 | -47.78767 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bcd4cbfa-f56e-31cc-a2e5-c70a297fa5d1 | -21.56684 | -47.83488 | 2024-10-01 00:45:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 133.3 |


[Clique aqui para ver as próximas entradas](README6.md)
