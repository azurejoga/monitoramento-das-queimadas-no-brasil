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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b580b418-021b-3960-88a8-b187d6ce8609 | -13.82562 | -44.58842 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 304fc35f-edc5-385f-991b-323040bc79a8 | -13.82451 | -44.59367 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79f19c80-c5eb-3a1c-96a3-7dc56ca6bf33 | -13.82339 | -44.59893 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7914af12-1cd7-333f-8600-4747781525aa | -13.81696 | -44.59764 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ab46e4e-e7d6-39b5-a1d6-337973f47ccb | -13.81584 | -44.6029 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa3091de-8721-3f19-a860-4f426bd6da10 | -13.80972 | -43.60632 | 2024-10-09 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83277d78-61eb-34df-8151-2b7f8c8a3319 | -13.80368 | -43.60498 | 2024-10-09 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 681f4143-bda2-38b7-8a05-18db7deafd2d | -13.54648 | -45.45358 | 2024-10-09 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22a60241-ad52-33c2-aac7-a315c4e4099c | -13.54243 | -45.43954 | 2024-10-09 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73907506-cc59-3f45-9c27-13da518671f2 | -13.5411 | -45.44572 | 2024-10-09 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ed22c46-1ea9-3112-9f1e-715524c5d317 | -13.53979 | -45.4518 | 2024-10-09 03:23:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1e5d413-16b4-3b38-a25b-100f12ff2635 | -13.43388 | -43.21264 | 2024-10-09 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e2938563-ff75-33f4-bcd6-01046ac87f61 | -13.43143 | -43.21102 | 2024-10-09 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c37d7675-8b2f-3fff-8fb1-30519cade170 | -13.02484 | -40.33096 | 2024-10-09 03:23:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 24494a64-512f-311f-9211-e957d06ee0c6 | -13.0243 | -40.33374 | 2024-10-09 03:23:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74274f68-e32b-38f3-a164-498c8fc45342 | -12.87664 | -44.61658 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9b62d56-1712-3adf-ae71-49030b379d07 | -12.87549 | -44.6221 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f60521dd-a675-3689-8efe-b0bfe974ae86 | -12.8743 | -44.62778 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d15816d3-f7eb-374e-b07e-29e19b7d99b4 | -12.86899 | -44.62056 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62c9eced-3927-3ed2-adb5-9a8575a16d17 | -12.86778 | -44.62638 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 96947396-5ccb-3153-86fe-aea0aa6f78de | -12.86247 | -44.61917 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 492144f9-7f32-3c9c-aed8-cf3a45a21c4d | -12.77803 | -44.90622 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f780c813-9357-3384-9cca-a3ecffce6aa3 | -12.7727 | -44.89845 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5a9822d-d1d0-3190-a4d2-e38e2c50d039 | -12.49225 | -40.8647 | 2024-10-09 03:23:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb502380-6dcb-31c0-8791-938935735495 | -12.49215 | -40.86473 | 2024-10-09 03:23:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2e5202a-97d7-3ceb-8958-7d04f2fac616 | -12.49166 | -40.86785 | 2024-10-09 03:23:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd9578df-5d33-3c5d-a94e-8503e9d570e3 | -12.49153 | -40.86788 | 2024-10-09 03:23:00 | NOAA-20 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1bf12ba-4e75-36f9-89a4-db0be11078c7 | -12.41461 | -42.34489 | 2024-10-09 03:23:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f318f34-6971-3235-96a5-a0953ba74c2e | -12.40972 | -42.34183 | 2024-10-09 03:23:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 69dc830e-14ef-3163-a51f-0c339397433d | -12.40885 | -42.3438 | 2024-10-09 03:23:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| afa72873-63ea-32f6-b296-7909a1b5529c | -12.40877 | -42.34655 | 2024-10-09 03:23:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 05e8e27c-ae6a-3a63-8f16-fd7f4f0a2675 | -12.37826 | -44.97681 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41a2d260-bfd6-3b39-a5d7-825c5a1c46a9 | -12.37706 | -44.98256 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c010672-aed0-3b0d-b6af-2d1e8217127e | -12.3715 | -44.97564 | 2024-10-09 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbf40825-12f1-32ea-bb22-4289c0aa4c82 | -12.36799 | -42.51824 | 2024-10-09 03:23:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4fb64110-984b-311e-b984-8ef7ecd817fb | -12.36457 | -44.74326 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b071e1d4-2e7c-33bb-a45a-048c50f42d58 | -12.3624 | -44.73622 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89fe37ce-e057-35d8-9f67-4e48cad8797f | -12.36122 | -44.742 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 725a07e8-a929-3e66-bdf1-cbe1186b3095 | -12.35921 | -44.73589 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ec44825-6d1b-3900-b30d-de9c5641f33d | -12.35799 | -44.74166 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52973605-046a-341c-a85c-4504bd689370 | -12.35464 | -44.74037 | 2024-10-09 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b982a482-2cfd-3c0f-9ae4-171ff8b191cd | -11.89002 | -43.88991 | 2024-10-09 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2500abe4-c2cf-36d0-9d9d-fab797906e7c | -11.88883 | -43.88857 | 2024-10-09 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 62129093-aba6-3a84-ad02-480d62874e30 | -11.88777 | -43.89385 | 2024-10-09 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f526e048-bcec-32bc-9deb-e8bf6418ffe8 | -11.73892 | -44.49797 | 2024-10-09 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aae36936-abf9-3fa2-b69a-1bdd68c06e64 | -11.73774 | -44.5038 | 2024-10-09 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a226dd61-88fa-3f70-bf3d-7fcf7496fb4f | -11.73608 | -44.49787 | 2024-10-09 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 530a5216-ad09-361a-bc11-af39177c0f39 | -11.65084 | -45.27381 | 2024-10-09 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6808804-9f56-3bb8-82f2-87b08e91499b | -11.64539 | -45.26536 | 2024-10-09 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d28cdaf9-11b5-32dc-bc28-020d262e13c0 | -13.93811 | -44.53493 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d098737e-bcc2-370d-a66b-ec33ee0b7302 | -13.91274 | -44.52891 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14b408f9-ef9b-3ea6-9e2a-457d421ad42c | -19.76952 | -42.84577 | 2024-10-09 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 308844f9-15ae-3fb3-acaf-212feeb0ae61 | -19.76613 | -42.33898 | 2024-10-09 03:25:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 976c196e-1c1c-3603-bd27-65e204b84287 | -19.76502 | -42.84146 | 2024-10-09 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea9c1722-ba39-38aa-bff0-7a83eec2eb27 | -19.7296 | -42.21387 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4ecfa96-15fb-3c6a-ab81-4ecaf5c52bd8 | -19.72928 | -42.21539 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea9a447a-a194-3b82-b0c1-71073a66fbb2 | -19.7246 | -42.21292 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7daf343e-5489-3b71-9e90-961e80c81039 | -19.72428 | -42.21444 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 867f36a2-ad24-3a71-bf07-e126b9e269d2 | -19.66349 | -46.23251 | 2024-10-09 03:25:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 648a1612-74cf-32d6-83f9-dbc805bf75fc | -19.66217 | -46.23822 | 2024-10-09 03:25:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47fd743d-8a48-32ab-a1a2-db32c7d97fd6 | -19.64383 | -46.86147 | 2024-10-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d45003cd-bd3a-3695-a4d6-8132c20adc5b | -19.64245 | -46.8672 | 2024-10-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03ad5259-b976-321e-9c00-ea72fb155b1d | -19.63822 | -46.86531 | 2024-10-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c72a7ec-edd3-3d24-b99d-0637b608e1d3 | -19.53661 | -46.09977 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e39043bf-a7aa-337c-aeb8-bc9a1319c0b7 | -19.53545 | -46.10485 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 30c30386-8324-3221-8221-161569f65c22 | -19.53344 | -46.0962 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d8ed4037-be65-3d68-9d89-4c449f468ea5 | -19.53231 | -46.10102 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8b6bfc2c-a3d8-3deb-ba08-219f9390d33e | -19.53042 | -46.09782 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c6e3826-9c67-3397-8744-91bcd9b2bb37 | -19.52937 | -46.10244 | 2024-10-09 03:25:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a4ecf758-9546-32db-abe7-0b717249c82e | -19.44748 | -42.51686 | 2024-10-09 03:25:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f81f50ab-9eb7-37e3-b587-c0c3775c72de | -19.33413 | -40.89083 | 2024-10-09 03:25:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4fe9b26-9beb-3b52-972a-0ad99bdfd2e7 | -19.33269 | -40.89178 | 2024-10-09 03:25:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 696e3abd-4aa7-36de-8647-6b1b192ef860 | -19.33053 | -40.88468 | 2024-10-09 03:25:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 816af72f-af0a-34cf-84fa-3de5274443d7 | -19.32914 | -40.88562 | 2024-10-09 03:25:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1c5f5cc-eac1-349e-a07d-2a3fd18c3d25 | -19.12937 | -42.72976 | 2024-10-09 03:25:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 411744ad-733b-3f9e-850e-2cc529af5669 | -19.12732 | -42.71364 | 2024-10-09 03:25:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b41994b1-3fb0-3efa-bb15-a2dc38ff8b98 | -19.12668 | -42.71671 | 2024-10-09 03:25:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 225084ea-ee1d-3578-92b4-57c7b3c07a44 | -19.1241 | -42.72902 | 2024-10-09 03:25:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f57659e-7b40-30a0-8db1-1ff5bb3d4133 | -19.00488 | -43.21435 | 2024-10-09 03:25:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92f71905-3824-3a4b-a88b-cadaf8d10e92 | -19.0041 | -43.21802 | 2024-10-09 03:25:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 614fde59-aa8f-3442-8b05-ea1d5b2f6a29 | -19.00332 | -43.22166 | 2024-10-09 03:25:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b42bde33-47de-3c76-a37c-e6e95733e57b | -18.78411 | -42.79298 | 2024-10-09 03:25:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8896c292-f482-3d07-b3e9-9154d5912931 | -18.65848 | -41.50724 | 2024-10-09 03:25:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b70511d-a2fa-3c39-aee5-0784cb5f30cd | -18.62948 | -41.12979 | 2024-10-09 03:25:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e52cd4a3-6b54-3e42-ab33-c734d118a939 | -18.62845 | -41.13303 | 2024-10-09 03:25:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ed1677e8-307d-3843-bb16-2f6b92b4d449 | -18.62833 | -41.13546 | 2024-10-09 03:25:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6664b7e9-c5db-3d44-8f6b-3a2c178c905b | -18.62475 | -41.12876 | 2024-10-09 03:25:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e092d38-cad7-3cbb-a99d-ed1ba8f50c56 | -18.6236 | -41.13441 | 2024-10-09 03:25:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae278ba8-7573-3deb-bf43-564b6943cb2d | -18.59908 | -42.34336 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 99371d7f-d3b9-3cd2-896e-849908c88dd2 | -18.59843 | -42.34655 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ce526a67-4b6e-3554-9124-028e02a2bf34 | -18.59632 | -42.34052 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b476d66c-927e-3132-97ae-b630680b4560 | -18.59565 | -42.34371 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 8b4385a3-0e5c-32db-a02b-804d2df7c263 | -18.59497 | -42.34691 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 04599d94-81de-3715-89b0-fffb2ca8ff0b | -18.59429 | -42.35013 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 744e9cad-0eb1-3a9f-ba20-8fea91fb28a9 | -18.59397 | -42.34216 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| a120a3be-e184-3540-8fcb-665adafee059 | -18.59332 | -42.34538 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| b0cd59dd-5973-3e6b-b54c-a48b4d1f48f6 | -18.59266 | -42.34861 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 1beb2d2a-f204-3ebe-81e5-ce906e8d7f2d | -18.592 | -42.35186 | 2024-10-09 03:25:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c2ad4061-c1a8-3d2d-8ac5-924a05e4e325 | -18.44339 | -43.42992 | 2024-10-09 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8275b3f3-c14c-3b1c-9cd4-0925ac79ea58 | -18.44258 | -43.43377 | 2024-10-09 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README62.md)
