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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc65352-9d55-326a-a8dc-35bba9263b5c | -20.43899 | -43.37175 | 2025-09-27 03:57:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0e7b44b3-1abd-34c4-ae58-e82defbcd088 | -15.26399 | -51.47748 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1946be27-3b21-3156-bb71-99c18fce3fa2 | -13.83479 | -47.95389 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b4e1e05-e8d8-3dba-9f0e-4a538bff85b4 | -13.80679 | -47.91769 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3354135-290d-3987-85bf-8bac9a456546 | -14.59433 | -48.25012 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8efd983-ed6c-3b7f-b895-03a2286680b1 | -14.8379 | -45.61535 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc664d53-4d3c-3f01-8991-3bc779febd7f | -19.69523 | -45.89492 | 2025-09-27 03:57:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8789a9fc-f19e-31de-b4cb-7c332efdf6a9 | -15.27157 | -51.4701 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de8a2157-69ab-3b53-8b13-a78a1c1fc179 | -13.82905 | -47.95811 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db874ee-002d-355c-9107-0f41471f66fb | -14.06281 | -48.81839 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eb94388-d4f2-3c30-a4fe-228b2e216a06 | -19.93324 | -43.61799 | 2025-09-27 03:57:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 88277c1f-d164-3058-a99d-2e0c98962a46 | -19.04973 | -48.13119 | 2025-09-27 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e655fbfe-9a99-3432-99ae-fd0d5c0cc967 | -19.41022 | -44.31023 | 2025-09-27 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66ed4e45-331b-3259-81b7-ff9c80867c33 | -14.8313 | -45.62902 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ef2566a2-7935-340e-a246-c9a3a3d7cf73 | -13.79217 | -48.33651 | 2025-09-27 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 132ca6b1-95c8-3eaf-8b4d-44f2443bd8b8 | -13.76576 | -47.87355 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f23d38b7-0bb5-37e4-8e9d-4974d7b0dd67 | -16.91054 | -45.94751 | 2025-09-27 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b73f57f9-af7e-307c-a573-9528b4c689d2 | -15.21078 | -49.41001 | 2025-09-27 03:57:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6db257e4-aa5d-3d85-af14-af7229af0a95 | -15.271 | -51.47002 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1f528222-0ef4-3674-9d28-d7c3718c63a4 | -15.26336 | -51.47741 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b2d6b36e-fbb5-34a8-b7e5-96aa2bd83343 | -15.27181 | -46.4492 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51cac727-c995-360b-99c5-576b19f35d38 | -17.73207 | -46.7096 | 2025-09-27 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97b421ed-0d34-37ad-877b-cb629bef94c3 | -16.91323 | -45.95525 | 2025-09-27 03:57:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76c2f471-5723-3c80-abf9-39c5d0a1e9a9 | -19.71939 | -45.86947 | 2025-09-27 03:57:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5f13cf1-7252-36ea-9579-29b3202cf08b | -14.9433 | -47.5004 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 185ebd6d-7fbd-309b-8d06-e6e81ca7f435 | -18.54666 | -44.77253 | 2025-09-27 03:57:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c3bfbd-14ef-3e20-aaba-5a1cd2e4b487 | -14.06226 | -48.82125 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea8945c3-8215-3c68-b7c7-cad8975f94a2 | -15.74921 | -43.84863 | 2025-09-27 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ba28e62-54bf-354a-8b17-42d32e870ef6 | -15.27191 | -51.46575 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37762b9a-ba90-338f-9c89-a6f85898f4d9 | -19.1126 | -44.39106 | 2025-09-27 03:57:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25c499e8-ed8e-3b07-9e2d-69dbc6963626 | -13.50144 | -47.41313 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1a11f22-be17-3a90-9534-530c963213f6 | -17.10999 | -46.86916 | 2025-09-27 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c6ffe40-8fb2-3dac-879f-c4fafea34d8d | -15.27745 | -46.44231 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5772f042-2107-372a-acdb-b636478d0924 | -21.11665 | -42.92216 | 2025-09-27 03:57:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0976b5da-a3cd-33bb-bb31-65f1f8cb3200 | -14.6302 | -48.29621 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 718847f6-7b6a-3d7f-9a8a-0a689f97e664 | -12.64771 | -51.66428 | 2025-09-27 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 793890f6-2802-3183-8991-88f7e97bda49 | -15.45011 | -49.63359 | 2025-09-27 03:57:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ed8ff60f-7a6c-3184-bd6a-3217239f774c | -15.25061 | -46.44567 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87a7e2f9-5a27-3734-9bdb-ca5c7a063da0 | -14.63131 | -48.29044 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3982d374-f793-3a73-a3ba-4f6bcc747b85 | -15.04042 | -46.95079 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe808b0b-5ac7-328a-9295-3d03cba81c94 | -20.32502 | -47.13271 | 2025-09-27 03:57:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a16a531-4a58-38ed-8c2c-a864f8f9fa6f | -12.65182 | -51.67548 | 2025-09-27 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9b9e837-63bd-319b-8108-f0054becfb13 | -15.00762 | -49.22932 | 2025-09-27 03:57:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a8c2f637-ddbf-30fa-8abf-f81a4cb5e984 | -15.47286 | -43.21108 | 2025-09-27 03:57:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dba9c5fd-d055-39a4-b592-0cadd529d690 | -19.63931 | -45.57642 | 2025-09-27 03:57:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d7563c6-6cce-377a-9b93-579da790aa14 | -14.51567 | -48.01431 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6b3e93a-87bf-36f7-b2d9-49dd2bc88d3c | -13.21521 | -49.55683 | 2025-09-27 03:57:00 | NOAA-21 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 498f3628-418a-3e9a-a3b2-89aa279c2944 | -15.14858 | -46.43096 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3d51c8e-2605-32b9-bc85-74339621d314 | -15.0318 | -46.94851 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9947d269-032c-3d81-b76e-d5ced30d1d44 | -14.63504 | -48.29697 | 2025-09-27 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3a30035-3c50-3371-b0be-cbdb2ffb51ce | -15.20922 | -50.16198 | 2025-09-27 03:57:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc1c6904-c3c4-3811-936d-0a707cea6ace | -19.31046 | -48.90847 | 2025-09-27 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45cf0276-b416-3b64-a217-585e95178dfe | -19.92984 | -43.61733 | 2025-09-27 03:57:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2810f485-1786-38ee-9490-8ff4d0e44bfb | -13.627 | -48.08637 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b4cf368c-9458-386a-acbd-696322c97d9a | -20.35526 | -48.79036 | 2025-09-27 03:57:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 429db5b7-ddc6-35ba-8013-2eae7aecc324 | -20.43624 | -43.36738 | 2025-09-27 03:57:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f08d3c99-8d90-34a3-a8f8-a5d2cc6f6bca | -14.84721 | -45.60972 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fb2c59f-99a8-3a7d-be1e-4fd5a6c44df7 | -14.43399 | -44.88517 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16a8c8b6-8d03-395f-9914-5241ef9a3813 | -16.0226 | -44.39748 | 2025-09-27 03:57:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbe2baaf-9fdf-3b39-a92a-c1fc12705687 | -18.68805 | -47.05137 | 2025-09-27 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cde1465-517c-3786-82e0-e8b1586eb7b5 | -15.20077 | -48.46717 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f8e0b1d1-aed3-3b51-985f-659504cf6e7a | -18.2543 | -47.01085 | 2025-09-27 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fca76b6-e1b5-3c1d-a0fd-8f2631fd0852 | -15.02751 | -46.94728 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3a15d40-3003-30d5-9612-936b64534233 | -15.53166 | -44.33812 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 55fe863d-ca2e-3ede-95bb-7c65e91105a4 | -16.45251 | -49.08271 | 2025-09-27 03:57:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de230d6-e162-3072-8356-f55820447b72 | -15.27323 | -46.44093 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62f391e6-b0ad-315a-99ae-6763adb126df | -15.25817 | -51.47627 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b3990335-46c0-3006-b514-6b24996a5b98 | -16.75876 | -53.3542 | 2025-09-27 03:57:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6a52ccd5-a767-3d6d-b76e-9453881b847a | -21.86028 | -42.10098 | 2025-09-27 03:57:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fef3fc3a-5362-3fb3-bd12-8ef0729618da | -19.40748 | -44.30513 | 2025-09-27 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a175bb56-8f81-3b66-ae71-9a0626692474 | -13.60254 | -47.30222 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cddaffcf-f0c3-39a2-8fc8-64cb540abdb0 | -14.97065 | -46.7619 | 2025-09-27 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 650ceb10-1654-3340-af61-cc9629ab5d01 | -13.60161 | -47.30715 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b701e9d-f49c-3eee-8e58-d10513a9ac1f | -14.48208 | -47.70728 | 2025-09-27 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c5a6222-c9f1-3c99-abcb-7bda47fcb830 | -20.27999 | -45.27917 | 2025-09-27 03:57:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d07f9482-181d-37cd-ae40-802577617dbd | -15.39119 | -46.10561 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3170aec3-a00e-3081-b963-11ea75649c67 | -20.29976 | -46.66166 | 2025-09-27 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 023ae135-9e74-35b8-95eb-a44e0043bf5c | -15.04131 | -47.13987 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| babbf4e8-b33c-3b1b-bcc2-a41b138a3b2e | -15.03879 | -46.95968 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 230f254b-c0f0-3ef4-b5dc-942f0f37b666 | -21.56064 | -41.33416 | 2025-09-27 03:57:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c690e9cf-e4fb-338e-8449-bf18f819b596 | -15.0127 | -49.23032 | 2025-09-27 03:57:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8132405e-bf8d-3f3d-81b0-41502f4228a7 | -13.52071 | -47.41251 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b16367c5-d73f-3fd2-8b99-b570ff4e1e18 | -14.97421 | -46.76687 | 2025-09-27 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c94e024d-c217-351b-be65-2b3c349b6b06 | -13.61547 | -47.30924 | 2025-09-27 03:57:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f79bd630-db5c-31ea-9aa0-744b1d92d27b | -14.06522 | -48.82896 | 2025-09-27 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc8aa524-5084-37ca-bc00-456fde1faba8 | -15.42416 | -48.21009 | 2025-09-27 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd8c53a7-29ca-34d7-bf6c-93dc6f55eb4b | -14.83725 | -45.61898 | 2025-09-27 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8834f1af-a4de-3563-8ea4-7e727e2586dd | -15.53419 | -44.3314 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d5b664b-bb7e-3a18-9568-2c9ecddad9c7 | -15.02391 | -46.96673 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18cd1df4-2f4e-32ba-a3f6-1107a0ef7354 | -13.50517 | -47.41878 | 2025-09-27 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 280282f4-58c9-36d4-a222-d3f981e7d168 | -13.61696 | -47.30128 | 2025-09-27 03:57:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d15d7a96-9ada-3780-8714-94bf563bbdff | -20.16879 | -46.20844 | 2025-09-27 03:57:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72c5f913-a55d-3fb5-ae34-3b36c6083a80 | -14.9528 | -47.50486 | 2025-09-27 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e086317a-d471-33b9-b698-1b46cfe4c088 | -20.02128 | -47.62574 | 2025-09-27 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c93a09ec-0bc7-3cc9-b787-77ab2ffef13d | -15.53341 | -44.33595 | 2025-09-27 03:57:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 29b1783d-4aaf-3056-8234-c8267ed243e6 | -19.40676 | -44.30931 | 2025-09-27 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3217d117-4e72-3747-adf8-18073f2d6cc4 | -15.44972 | -43.645 | 2025-09-27 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84d3de2b-a9ea-3b6c-8eed-3255cadb2b1f | -15.01956 | -46.96577 | 2025-09-27 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c6eb346-10b9-3811-92bf-1bb9c081c041 | -15.27824 | -46.4381 | 2025-09-27 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7047fba3-09a0-303f-b126-501af81f6d0c | -15.9688 | -50.87495 | 2025-09-27 03:57:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README24.md)
