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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e367648-e0e9-35d1-8fab-352faae0c1f5 | -21.85032 | -48.44091 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e74a196-0866-3a01-bdd6-b2a7ff147dcc | -21.85006 | -48.36097 | 2024-10-06 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92bc9533-672b-35d8-a528-1ce7306db6ae | -21.84899 | -48.44635 | 2024-10-06 03:34:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e955fb7-982c-3901-ba50-02a9e3454bce | -21.84766 | -48.45182 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 413976ab-df66-368c-8aa8-3263bd52ab3d | -21.84649 | -48.35989 | 2024-10-06 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3822d627-a7f7-32cb-92a2-4ebc0be0eb98 | -21.78383 | -46.18545 | 2024-10-06 03:34:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6017a367-dc54-3808-989c-90a1d29ec661 | -21.78296 | -46.18933 | 2024-10-06 03:34:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e5121d8c-0e94-3a6e-8a52-702d057547a1 | -21.59502 | -48.61102 | 2024-10-06 03:34:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f315d42-06b3-3fac-bb1e-c9bcc8ea4b25 | -21.59036 | -47.94832 | 2024-10-06 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36943103-bdb0-3e59-8d65-23a3d9d3f6b1 | -21.59003 | -48.61131 | 2024-10-06 03:34:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d0a2d27-92dc-3095-98a1-f342062e3abe | -21.5843 | -47.94664 | 2024-10-06 03:34:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72153515-d7e1-352c-b9a1-f071e174e65c | -21.16259 | -48.88048 | 2024-10-06 03:34:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5f9ff7f8-bd3e-3f20-8b89-2aaa0027ced6 | -21.15623 | -48.87836 | 2024-10-06 03:34:00 | NOAA-21 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 9cda9c67-b3b2-3e12-8e54-d3affae99b86 | -21.08153 | -45.72302 | 2024-10-06 03:34:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c863b40f-0889-3866-8110-96a7a149ce21 | -20.7885 | -48.59452 | 2024-10-06 03:34:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3aa68b65-b3ef-36f0-9a7d-2d4f2ad7fd89 | -20.62141 | -45.82451 | 2024-10-06 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ddb53ff-8079-3730-9054-21deb4725e77 | -20.6206 | -45.82812 | 2024-10-06 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f4321f6-e611-3b39-9b0e-375792f9ad40 | -20.59136 | -49.37936 | 2024-10-06 03:34:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 443b75e9-2be3-362a-80d0-650966dd5fcc | -20.58977 | -49.38588 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1a255776-b99f-32d3-9746-ff478580c277 | -20.58821 | -49.39224 | 2024-10-06 03:34:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e00d0a5f-2ca3-38cd-97b8-29667f1f069e | -20.58635 | -49.37074 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1c0f5949-4617-3614-8c9c-01ace7604018 | -20.58469 | -49.37747 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 0d69487a-8b4f-3a7a-a9a9-872a91461d58 | -20.5831 | -49.38396 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1001.4 |
| ef319dfe-da5e-3d73-bb2c-608a071641ae | -20.58153 | -49.39034 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1001.4 |
| 97db5cd5-8921-37b4-beb8-8a849799431c | -20.57992 | -49.39693 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 0d49e6c4-5f95-31c5-b40f-79b2c227c8d4 | -20.57964 | -49.36903 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 61207b37-e9ae-32ff-b5d6-028126a2b5dd | -20.57837 | -49.40325 | 2024-10-06 03:34:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 9824ee4e-8a8f-3980-9909-a0a7ff8907c8 | -20.57802 | -49.37559 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 2c70a0e0-6929-3fbf-a80b-d5c0df58155a | -20.57323 | -49.39506 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| a12ae2e3-789a-34e8-abe7-86f53469754a | -20.57298 | -49.3671 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca376f97-5559-3132-b83b-4a6809f14849 | -20.57162 | -49.40162 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4a101ec3-4967-33ff-9dda-99f38ff65e0e | -20.5714 | -49.3735 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 362f4934-4081-3f4a-83c4-77150d66460a | -20.57002 | -49.40814 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e633914c-7bb2-31fb-a704-1aac950a2844 | -20.56984 | -49.37986 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b407393c-9298-3930-a066-14a9ca88409b | -20.56823 | -49.38638 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fd0b33f6-3e8b-3360-ad16-b88bd9ca6337 | -20.5666 | -49.393 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 23368151-6111-31b3-8e15-a5d595e11fcb | -20.565 | -49.3995 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2867ebfe-326e-334b-a22c-b00b177d3c35 | -20.56338 | -49.40605 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 59aad6bc-4380-3417-97dd-f29086a3b170 | -20.56317 | -49.37797 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 386b54f1-3148-3adf-b6a5-73eb60bbfbc1 | -20.5618 | -49.37669 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb75d0c8-4ed6-3107-962d-ac66c10ca543 | -20.5602 | -49.38338 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a8c6bd0-2be3-3854-9381-e078056198c3 | -20.55651 | -49.37604 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dab6a441-c11b-39ac-b73a-d8159abb747f | -20.55514 | -49.37476 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9feba9f6-221f-3ad2-921e-046a4650d934 | -20.55489 | -49.38256 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e17a326-30c5-3a5b-918c-391520864ab4 | -20.55357 | -49.38128 | 2024-10-06 03:34:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dc856a7-2959-3e68-9dac-583f6c091094 | -20.51593 | -47.49223 | 2024-10-06 03:34:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 4255e87c-1cf3-3294-b686-1cee2a39c0f1 | -20.45658 | -49.98466 | 2024-10-06 03:34:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b2884be-5629-340d-aae7-b9bc9794923b | -20.44974 | -49.98246 | 2024-10-06 03:34:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08f82631-8e28-31d3-b9a7-628b6c1f7096 | -20.43619 | -49.94794 | 2024-10-06 03:34:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 14c026fa-88c0-3626-ad0f-3a4ad8891f50 | -20.02711 | -45.65249 | 2024-10-06 03:34:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c86c4f52-48a7-36dc-83cc-c2f42d4df00f | -20.02623 | -45.65649 | 2024-10-06 03:34:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9bba6dc3-a5df-39ea-8a2a-5e808c4d45b5 | -19.91701 | -44.52234 | 2024-10-06 03:34:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 688e2fe3-8785-3b1c-b05e-9550c3534fb7 | -19.91624 | -44.52592 | 2024-10-06 03:34:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 138dd2cc-6c42-3a09-a505-59bacf01bac8 | -19.91256 | -44.51792 | 2024-10-06 03:34:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8319f5d8-513f-3c90-b7c9-c0adc7de2269 | -19.91184 | -44.52127 | 2024-10-06 03:34:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d481142b-e891-3c3c-a022-c4a69f28512a | -19.88105 | -44.40527 | 2024-10-06 03:34:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b35443d-f375-325a-b14c-1e63a8ef2a28 | -19.88032 | -44.40873 | 2024-10-06 03:34:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a40e4af-39e8-3a39-b984-1bb3f5152027 | -19.83204 | -46.44657 | 2024-10-06 03:34:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9b6c597-05da-3c11-876f-c13763d744c9 | -19.83103 | -46.45101 | 2024-10-06 03:34:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8efc6f4b-8427-30bf-9841-74d620bfeb38 | -19.82741 | -46.44011 | 2024-10-06 03:34:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b93544a2-a7d1-317a-962d-be3508b95fdd | -19.82637 | -46.44469 | 2024-10-06 03:34:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdb7ae65-cc9a-3617-884a-395403a0b59b | -19.81523 | -43.84787 | 2024-10-06 03:34:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a97f71c-d1d7-3b33-8663-e7806e66ab01 | -19.81083 | -43.84408 | 2024-10-06 03:34:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e578444d-6927-3240-bbcb-c6f75687b582 | -19.81022 | -43.84704 | 2024-10-06 03:34:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83cefb8b-7355-39ab-af49-3a47ac65b559 | -19.78579 | -40.83861 | 2024-10-06 03:34:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 844d86d0-76cf-3986-a581-3f419d145a58 | -19.61362 | -46.25832 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52a187f0-a475-3406-843b-8fcaf5289783 | -19.60682 | -46.26171 | 2024-10-06 03:34:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9855416-2c43-3342-85c5-47a7432b8b45 | -19.56514 | -40.49582 | 2024-10-06 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e2766e6-8458-341d-a98d-8a8a2358d754 | -19.56109 | -40.49509 | 2024-10-06 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3c5ad5bf-c989-326b-b212-27f825d82ee3 | -19.45189 | -40.69753 | 2024-10-06 03:34:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f8532155-04d3-3198-8645-309ff71f895a | -19.30098 | -46.22133 | 2024-10-06 03:34:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aa248ca-9a5c-328d-8812-bb6bc9bc48d5 | -19.29997 | -46.22593 | 2024-10-06 03:34:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dcd2997-3c99-3092-8af2-2a81538f98eb | -19.29992 | -46.22446 | 2024-10-06 03:34:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f9da4de-9863-352a-bf22-24e6920227e9 | -19.29405 | -43.7782 | 2024-10-06 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91bbeb22-7866-3ccf-a042-cd44981e4411 | -19.29395 | -43.77862 | 2024-10-06 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 470bac54-5116-34c7-9d46-1064f79d704a | -19.2934 | -43.78125 | 2024-10-06 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bdafe58-013b-37a4-8737-815bfd73c678 | -19.29333 | -43.78168 | 2024-10-06 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb8af74d-9d15-3bd0-b578-407fba124cda | -19.06898 | -47.00842 | 2024-10-06 03:34:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 11c36c23-69d1-38cb-abe5-26faf17e16d0 | -18.5652 | -43.83344 | 2024-10-06 03:34:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1d845f9-7870-33b9-abea-a6cf08d811a2 | -18.56461 | -43.83633 | 2024-10-06 03:34:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79b2a5c8-ba9b-3a3e-95c3-58ebd50e15ff | -18.47935 | -47.39359 | 2024-10-06 03:34:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba6c8ba2-0c4c-376f-8678-af4863375412 | -18.47639 | -47.39344 | 2024-10-06 03:34:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43ba7260-fccd-3811-909b-41c25d73053d | -18.45503 | -46.66047 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dcfee01-dfbc-3c99-99bb-d8b84137e8d0 | -18.44965 | -46.66146 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60cc3388-ae44-3aff-9b18-4fd7b50a539d | -18.44891 | -46.65953 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 125aa85a-5e24-33f7-a8ca-2374f191a4da | -18.44792 | -46.66399 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6c6b733-29ea-35ef-97fe-d59576a53609 | -18.44241 | -46.66541 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c6b64e-9085-34c1-aaac-8a17fa8f9200 | -18.44066 | -46.66819 | 2024-10-06 03:34:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 719c0aa0-f8ed-3ca5-a0a9-ccd6a1b65cd7 | -18.42395 | -42.23218 | 2024-10-06 03:34:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1d02f377-6444-3daa-8021-a90b9dd8c1e5 | -18.08471 | -45.61252 | 2024-10-06 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 254f1499-576c-34d7-9a38-0b14cf296d49 | -18.08385 | -45.61653 | 2024-10-06 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 870ee825-65a9-3379-9471-756f6e77f201 | -17.81679 | -45.89941 | 2024-10-06 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e107ae2-1fef-329e-915c-a159ed1aa304 | -17.81582 | -45.90387 | 2024-10-06 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ec8ddc6-141c-3fc2-a832-8dadc6514ce6 | -17.81484 | -45.90839 | 2024-10-06 03:34:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b2687409-b772-37d5-829b-897ac2fe4891 | -17.76558 | -39.7975 | 2024-10-06 03:34:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b897ffe3-fd79-35d8-b4aa-8a8645d99fa8 | -17.64547 | -44.42221 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c75c4801-b971-3ed3-aa86-cb2fa527a7fc | -17.64306 | -44.4072 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bf60c98-c4a4-3bb2-8659-1cf8aff8635c | -17.64026 | -44.40686 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a65c114b-457f-3d4e-b49c-897c95a7a2b8 | -17.64014 | -44.42094 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 910638fe-ac7d-3e9f-bc42-a0cdbefe78e0 | -17.63766 | -44.4063 | 2024-10-06 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README44.md)
