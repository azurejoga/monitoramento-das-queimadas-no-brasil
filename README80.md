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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 806c9502-70eb-3f94-b6a4-d78ccd0caa5d | -18.65722 | -43.68995 | 2025-10-02 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a770f959-af40-3703-94e3-9f4843588ea8 | -15.99637 | -50.90638 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a755a0c9-33fb-3090-bab5-1252844e81be | -12.80703 | -47.01625 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 406656a1-774f-35a1-81e5-cf015f82b210 | -13.53194 | -47.25673 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 428f8980-b761-30ab-bdcc-46352f2f8100 | -14.89811 | -48.12763 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b1acd73-66d4-3768-aef7-efa7c733cb91 | -15.22385 | -48.73981 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13c47689-496c-36ae-9dcb-86e708496e15 | -19.95447 | -43.66586 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97f50e25-33ea-3094-8769-7973be672f8d | -13.20899 | -48.4967 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70ad3913-41c0-3670-ba3d-018cecc8172f | -15.70095 | -49.93693 | 2025-10-02 04:32:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0a6fe96-b65a-34ba-8dbb-c58d6b953016 | -12.81749 | -47.02862 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 930ad0e4-c33b-373c-8a4a-1458e14f230b | -13.31535 | -47.20402 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73df9ce4-47b0-38df-9e1c-e0b72ba6d5bf | -18.11744 | -42.73012 | 2025-10-02 04:32:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 869fedae-f071-34cb-8328-78ad604b83f2 | -11.85656 | -48.02615 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a98df8fd-e827-33a0-b60d-e81f0d4ca505 | -12.80642 | -46.86549 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71d716e3-67eb-3a95-abd3-62b2b09d99a1 | -15.35162 | -46.28617 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f705e93-35c3-34d9-b34d-033ae7da676c | -11.8504 | -48.0433 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5661d360-d977-396f-b076-12c862646193 | -19.59344 | -43.8429 | 2025-10-02 04:32:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83de8f9f-c238-396c-ba4e-6b18c4f26b10 | -14.43779 | -46.36408 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45e85f5a-a7c3-37dd-9c20-a036e2948109 | -13.15947 | -47.82797 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 307a349c-206c-3118-87d0-076283f962cb | -13.94365 | -48.12761 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f26ebe48-5936-3dda-94f1-0265f4c3d20c | -13.17394 | -47.80123 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66776b8f-e87a-313f-8bf5-b0b03c8dbb8f | -12.62854 | -44.85209 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef8a75c5-09b0-38e3-97a1-6f88c91a05b3 | -11.17128 | -54.11648 | 2025-10-02 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5bc1a75-6650-36e3-9a2b-b72fb0b853bf | -14.48129 | -48.40642 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d848d9c5-cfd6-3264-a5a7-9770346227d9 | -14.90203 | -48.33317 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a9bec80-1e12-3a85-8d5f-a2ec68697e1c | -12.47741 | -54.42727 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfab1cc0-e655-3d50-9918-cb77a1b694be | -14.3136 | -45.98494 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b7ebc58-1f80-3b11-9f24-245f5b79f44e | -17.21122 | -46.98629 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcd65658-fdd8-3910-92b3-e8288f44c17e | -13.3187 | -47.20452 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50e5e8e1-5f98-3317-8c3c-e4618a05d063 | -15.25718 | -49.31271 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6fa0e4e-ce03-3866-aa61-8c1feed3e6d4 | -15.13981 | -46.44751 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f47f0b85-741b-39b0-83e1-f1da5af0f14c | -12.82139 | -47.0256 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cb0a962-a029-3efd-b7c1-c41ba3d97872 | -16.01642 | -50.87287 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0015dc68-d66b-3b6b-98ee-a13bbcbb3439 | -13.31934 | -47.00175 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dcb31f4-2bc8-34b9-b5fd-921a611a1020 | -12.89489 | -46.90538 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 117f8c7c-478e-39ff-b47e-6436b45f183a | -14.5822 | -48.32469 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0564eb98-7190-30af-a5e3-ab9fde058e77 | -14.86383 | -48.30157 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72669d24-3b91-32f8-aa19-cbe40c1c39b7 | -15.25442 | -49.30848 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 643172aa-c216-322d-a50b-75296e255c67 | -13.56262 | -48.10157 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3140c513-32f5-3746-b58c-7d1446a539c4 | -13.12901 | -47.41895 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19b9aa22-5071-383e-bae5-61f467e21c92 | -16.02997 | -50.92015 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69028667-a801-35cd-955e-b3d4e7aa6da6 | -14.81464 | -51.40818 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3705b77-e357-3dd9-8840-afc2d91ae4f2 | -13.76114 | -47.97756 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f4741a0-b2e7-3709-8309-21be4497f41b | -19.96583 | -43.71258 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d9ac55f-cfef-30ba-b6f5-5770bf329cde | -12.82255 | -47.06242 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a8f3bd8-059b-32ed-bc92-88ba23b59203 | -13.1661 | -47.85091 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07b2290-43e8-30b9-b172-5ace803cad5a | -13.75451 | -47.95456 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c7a8b53-5841-3783-bb83-fb31052fdca4 | -15.17375 | -40.43039 | 2025-10-02 04:32:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4604071a-5929-3d29-89b0-65c002cf3cbf | -14.46798 | -48.40419 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f3d390a-7b10-377a-b519-452d022b9886 | -13.69452 | -48.6321 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4bf211c5-8bb1-35ae-a9ac-69c62ffcc0a9 | -13.69785 | -48.63265 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15c5748-a558-3888-8d92-d9235a061058 | -13.16115 | -47.81733 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ecbe6780-0350-313a-ab61-5cdb760ae6ae | -13.7982 | -48.04575 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b800660a-c90c-3da7-a6a2-d500a701d872 | -13.30873 | -47.00373 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9802c513-3c46-3183-8dfe-7de81430f681 | -13.80366 | -47.51654 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f14e3db4-11a9-3942-bcc4-9ea1ad412917 | -16.36986 | -47.06676 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3938d089-4649-3621-a352-90519280133c | -12.80306 | -46.86496 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dc944b4-3856-3972-8c74-90bf465e5bed | -14.79382 | -49.26466 | 2025-10-02 04:32:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f944bc07-e6d8-322d-8c69-467d9c71f1d7 | -15.20995 | -48.1643 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66f347e8-3558-3148-b7b7-8ca74c584acd | -13.31256 | -47.19993 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b312ac8a-1211-3a66-be12-ba819fa6ebd9 | -12.84681 | -46.86071 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1447e24-4ac1-3732-a36e-8be85dc6966c | -16.27942 | -42.54467 | 2025-10-02 04:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73fa1b19-6033-399b-a440-a45fc635e41d | -15.18397 | -46.42597 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0014d931-382a-3580-8c67-e834073c465b | -16.03995 | -50.86099 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e3609b33-c400-3aa3-a61b-6becc78d23da | -15.92838 | -43.3423 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| fed25914-51ad-3293-b553-13f918067732 | -13.67577 | -48.09069 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75e26f3f-cd2c-31d2-80cb-0d7c222a3b3b | -13.94641 | -48.13172 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5fe3b422-e8a5-34f2-97af-e5900a5f641c | -13.23343 | -48.50779 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5c5a933-311e-3ef2-9298-c3c314bb5c3a | -14.91545 | -47.23266 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dfbbd322-edbd-3ceb-a822-cc6bb6cf5ac2 | -14.62332 | -48.30227 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b483449e-a27c-380c-97cb-b8055d03bfea | -11.58263 | -50.17068 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c873229-099f-34d3-a52b-cd7fefcc0c43 | -12.36819 | -45.78859 | 2025-10-02 04:32:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80adb1f8-0cb2-3a6b-9cab-4f24e167f38a | -12.18611 | -47.90855 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1baa9789-3eec-3df3-9a04-c02a8d729f00 | -12.70058 | -48.58157 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 422d159d-ed6d-34e0-a814-0ba5b3e30eb6 | -11.85713 | -48.0226 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f65c3d8d-c9ee-39b3-b73e-8125684aaffd | -14.98521 | -46.91323 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb13865e-9914-3760-8a82-6f1ed007f9ad | -12.64029 | -46.95324 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1e7a6cf-cb16-3c0b-b592-848799d69d6a | -11.92879 | -47.05507 | 2025-10-02 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecac4509-4e8b-3224-925b-f60faec935cb | -14.32689 | -45.96721 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3f3ab82-fcfa-3b4b-b47b-fab3e175b130 | -14.88368 | -48.13255 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bad6722a-d000-350e-abc9-e142e1c5a258 | -13.78652 | -48.05477 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d49637e3-c9cc-30d5-b1e2-aa0f8b399e76 | -19.89416 | -44.93737 | 2025-10-02 04:32:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cea80114-7ab6-37b0-a92b-433bfff3119a | -15.80215 | -43.73064 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03fc2fd3-4fc3-392c-9445-9ea4ecb4c280 | -14.41151 | -46.09824 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f98dce2d-d5e5-35a4-b0ca-65543bbf1a80 | -13.51963 | -47.259 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33ee0881-64f9-3208-8054-b6e2485e25d8 | -13.20524 | -47.33968 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e4c1915-e4d0-3546-8883-1ed6a8e747d7 | -12.58455 | -49.90559 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9e46137-26ed-381c-b1e4-055dea4431a4 | -14.62 | -48.30171 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 738ba8c9-4bb1-3426-8695-db57c3a5e36d | -13.21642 | -48.45022 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 67b96404-51ee-3fee-8ae2-d3e9d14bf2bc | -14.18406 | -46.66213 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 666fb4b3-5baf-318b-a7e4-5a0e4476f89a | -11.85651 | -48.04795 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26c4d096-5a15-3786-86a6-94f06b38f6ea | -13.64567 | -47.18658 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bf16966-b72b-3c32-9aad-9538d7395349 | -14.70175 | -48.20871 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8aa1f468-1c70-38c3-bfb7-fd473b53b3bc | -14.4366 | -46.34849 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b39caad0-ed31-3f26-b8a2-25bd526dd825 | -13.75616 | -47.96579 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 41ef02f7-e196-379b-89c6-ef2652f0bcf7 | -13.31543 | -47.00481 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ac18119-7321-355b-8cb3-e2192b9eacfb | -15.21941 | -47.16413 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c20b7134-a7fb-306d-8fd0-bbeb9843edae | -11.86882 | -48.01361 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7749b2e7-e4b6-3d8e-bd1a-371dee08d717 | -14.37043 | -45.96873 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 342a67eb-cdb0-3563-971e-96ef9a9a652c | -12.58931 | -49.8984 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README81.md)
