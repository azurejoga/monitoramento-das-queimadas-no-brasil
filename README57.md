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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cc797f9-1b5a-33e0-ab21-c1f653abe5d4 | -19.98236 | -47.16359 | 2024-09-27 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b2af0c80-1b03-3365-a24a-4f5be543aff0 | -19.78149 | -47.02754 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797b4f6f-7046-3f48-8fba-ebef24d89cff | -19.77782 | -47.02374 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eeac489c-d3cc-3659-978f-6fd44619787f | -19.77698 | -47.02648 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 438fae80-04f9-3d02-8bc9-e531c6de16bc | -19.77688 | -47.02838 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e62eea9-9035-32d1-a8cd-e015cf8e7833 | -19.75406 | -47.25845 | 2024-09-27 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c38433c-b285-330d-bdc8-fe1e8da51635 | -19.75304 | -47.2635 | 2024-09-27 03:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3181f8b-ef45-319a-8cad-e070b0aaadc3 | -19.59772 | -46.9748 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 04b9b4ab-3377-3768-b64e-54687ef90ab3 | -19.59674 | -46.97967 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6a9f421-db30-3934-a62d-f5e9a289bf2e | -19.59574 | -46.98465 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9136c92b-b966-3e9b-b9e3-31e1f61c261e | -19.59322 | -46.97366 | 2024-09-27 03:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ce00f058-8955-3cb3-9c88-e1d7b00cd357 | -19.53119 | -47.88875 | 2024-09-27 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb9fc94b-a6dc-3ed3-82e4-7b16e83639ce | -19.52756 | -47.882 | 2024-09-27 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7056aab0-92c6-3a42-9da9-93a0bf430a48 | -19.52639 | -47.88768 | 2024-09-27 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d871bb2-1bf8-3b16-a492-5090b1fe7e21 | -19.52276 | -47.88087 | 2024-09-27 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 916de2c5-bc7a-321a-8865-ad6526b97fe6 | -19.52159 | -47.88658 | 2024-09-27 03:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb31e4d3-160a-3442-8899-ac42d22e29f4 | -22.33521 | -47.75921 | 2024-09-27 03:49:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e7b2d92b-b89d-3683-b275-7b83876e186a | -14.78383 | -48.27858 | 2024-09-27 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 971e3766-8a8d-30c5-ab52-2cc98decdf05 | -14.60147 | -48.16261 | 2024-09-27 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 009cd3ea-6351-3f6c-afa4-ebd0cde887ff | -14.5961 | -48.16147 | 2024-09-27 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e80a96-3b32-3f3d-ae97-1e3e3132b199 | -16.51193 | -48.05537 | 2024-09-27 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 540f8177-2514-3269-8de7-f2af17ffffc0 | -16.51131 | -48.05848 | 2024-09-27 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ebe08b2-c338-3a59-ba91-e6aab2fbff46 | -16.50677 | -48.05433 | 2024-09-27 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de8c90ab-9848-37d5-8b84-dcca72f1bcca | -16.50614 | -48.05747 | 2024-09-27 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e1e7377-ba04-3f0c-9bd5-10bb45ed4377 | -15.61339 | -47.23299 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae8d145a-c54d-3995-a339-abd58e146086 | -15.61323 | -47.23383 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47d3d745-e2da-34dd-8a70-9180088e3e54 | -15.6123 | -47.23866 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fed5279-e6cd-34d7-b08f-5fec7c0769af | -15.50659 | -47.30186 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c32ff60d-92b0-3b26-bba8-d869d474c895 | -15.50601 | -47.30479 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb14c307-5e68-3551-a1a9-3f0a85d98b99 | -15.38349 | -47.45279 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e51bb3fc-228b-38d3-b018-d3ab2b80331c | -15.38287 | -47.45593 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ccc27860-8fa7-38e9-ae9d-879ece69a6c9 | -15.37647 | -47.46159 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd3f2d8e-b664-35d3-9494-0f1ca6d49505 | -15.37081 | -47.46357 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ff89903-6f46-3863-957e-b9f08832d561 | -15.36778 | -47.45234 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 408bee5d-3f41-3957-a956-642d27a9ae8f | -15.36725 | -47.45501 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4860ee5-b4ee-3568-a489-64bed222c57c | -15.33411 | -47.44696 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24eda064-693b-3519-be52-8e62be047739 | -15.33354 | -47.4499 | 2024-09-27 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23192621-e58a-37d3-b155-89f83ee2c5de | -17.49812 | -47.83187 | 2024-09-27 03:49:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 150acd34-a063-349b-8261-b1e5c2f2ba0c | -17.22039 | -48.02476 | 2024-09-27 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d14e2246-ccb2-39ac-aa18-e6a99222bece | -17.21973 | -48.028 | 2024-09-27 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c533d3e-190d-37ab-8635-06931176fc7b | -17.15187 | -47.64846 | 2024-09-27 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 54589e7a-c50b-3b0d-89a4-8a6b8aeec7c3 | -17.15182 | -47.64678 | 2024-09-27 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d1f951b7-ce75-31ef-81ca-9d374dbea952 | -16.85077 | -47.7013 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a474b3e-5fb9-34ad-84ea-759af169c7fa | -16.85015 | -47.7044 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27a715b5-f511-39f9-bf5d-2d3a494b6d36 | -16.84873 | -47.7633 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2015b2ab-d871-39ed-ae30-1221d19660f9 | -16.84513 | -47.70344 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d368b73-8acd-3d1c-ba09-38120aa8ed52 | -16.84449 | -47.70657 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07b2ea2e-cc07-32ea-80c1-463de01a5590 | -16.84386 | -47.70972 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2f73c10-9695-3ff6-985e-f37bcfe7f9dc | -16.84311 | -47.76521 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| caa79e73-8407-3c58-a990-e79348d2a739 | -16.84241 | -47.76866 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4eb2243d-2477-3af7-aed5-da66b29bd18f | -16.83884 | -47.70874 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a16bf7f-3a05-3e93-a7b3-9250eb8a867b | -16.83822 | -47.71177 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d03da9d2-c10b-38e8-a0e6-eaa66e559fd4 | -16.83816 | -47.76379 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 145e297a-4002-3edc-a9a6-945378f33b49 | -16.83762 | -47.71475 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b25c6aba-3c31-3d2e-93a2-dcc16bfee0cc | -16.83743 | -47.76736 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 43ed7ac5-1c04-3f74-9cb9-77c1d873a9ae | -16.83702 | -47.71769 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7684943-06d8-354f-92b7-790330bd752a | -16.83673 | -47.77087 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f59596a-95bb-3a5a-906f-310e61ad87f7 | -16.83273 | -47.73888 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3143a0f1-941c-3328-af50-f2412356db4a | -16.83209 | -47.742 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7784c414-7cdb-3538-934a-b260b037e708 | -16.82773 | -47.73773 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7f7cec6-8399-3180-8048-d11156d01d5a | -16.82709 | -47.74087 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9eaf3826-c2e1-3213-917a-801827a04890 | -16.68099 | -47.83052 | 2024-09-27 03:49:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 540dcbfe-eb44-3ee6-afb0-df1ed06ac1f7 | -17.76939 | -48.76796 | 2024-09-27 03:49:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e394ad5a-654d-317d-a937-ac82be24730f | -19.32115 | -48.92232 | 2024-09-27 03:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b1f7b03-f002-3b26-830f-516d8febc369 | -18.91875 | -49.19981 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| f2e2dca1-1d02-397c-984e-f112130520c5 | -18.91573 | -49.18806 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b129fa1-e188-39bc-b8a9-41b6f57fc43e | -18.91499 | -49.19151 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 496f18b7-1416-3a84-b864-453eddcf0184 | -18.91424 | -49.19499 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| e00afaa2-2eef-3d3a-b9a5-9c8c219186f6 | -18.91351 | -49.19842 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 7b093caf-dc13-309b-904b-3c20ef20e287 | -18.91278 | -49.20184 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 8239a151-988f-3b9f-97f6-a6cec32c80bb | -18.91256 | -49.18567 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae81e49a-c4f0-3fd6-81f3-1ba4e9a7bc5b | -18.91204 | -49.20527 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 763c80c7-5985-3339-bdb1-c8c23f12baee | -18.91186 | -49.18903 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 82faa7ad-af95-383f-b970-412a8528480c | -18.91132 | -49.20863 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 136c5778-1564-3d47-9a7a-d0c5f5d96271 | -18.91114 | -49.19254 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 6a8f77b6-7a33-3982-b24f-abaaa10a9ac0 | -18.9105 | -49.18662 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9403991c-c98a-38bb-b344-caa5b3b8186c | -18.90977 | -49.19004 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| faf38e95-548c-3aab-aabd-9c094655cdcc | -18.90969 | -49.19953 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| a6c1478a-13a3-35df-a89b-e088a9d3962c | -18.90903 | -49.1935 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 10a3e1f9-c9d1-3ec7-b5c0-dc1d7907e123 | -18.90897 | -49.20303 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| da54aeae-a066-369a-a122-5070e6e47ecd | -18.90828 | -49.19698 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| bef6aaef-18e9-37a3-a513-3817eb8de611 | -18.90826 | -49.20644 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4f1031a1-7253-343a-95d0-fb856ac2dbf8 | -18.90757 | -49.20977 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e151657-c667-3ca4-8299-11e238a6796e | -18.90752 | -49.2005 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 57b96910-2780-3440-a03f-378798d7cbc5 | -18.90677 | -49.20401 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 5e9dac9b-6f74-347f-a3c2-641ee0feb2d6 | -18.90661 | -49.18768 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| da36ce2d-f397-394f-b011-40f213eed2ea | -18.90605 | -49.20738 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 39fe0e41-1fed-3c72-8ade-38630d7abea7 | -18.9059 | -49.19111 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 503753f0-fe16-3743-885c-82eb0eb0b3f7 | -18.90519 | -49.19454 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 97b5eb20-1058-337e-bb39-1dda5c7d2d94 | -18.90446 | -49.19807 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 0a954c34-d3d8-31fc-86c0-3b1cce65ff31 | -18.90371 | -49.20168 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b5fd7ff5-a640-3201-ac79-438d10155d28 | -18.90305 | -49.19555 | 2024-09-27 03:49:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| a4c1d4a4-3a25-33f3-bcd3-b9e89dd5eaba | -18.59817 | -48.81055 | 2024-09-27 03:49:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29879bd6-aa7b-3e76-9b56-451af31a2e28 | -18.59299 | -48.80935 | 2024-09-27 03:49:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 91ba153c-80d2-383d-911f-71eff89a0623 | -15.13547 | -48.76832 | 2024-09-27 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69719025-9a2b-362a-8061-d5d973517724 | -15.13467 | -48.77224 | 2024-09-27 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c129158d-b028-3dca-b9f4-f16337feeb8d | -15.07553 | -48.94762 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ff9baca-8da7-319f-8c8d-171e59e7dd2c | -15.04311 | -49.16192 | 2024-09-27 03:49:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dd31c09-4801-36d9-9664-dfee91ca8937 | -15.0423 | -49.16587 | 2024-09-27 03:49:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78e1e3ef-9fb1-3fa8-af58-00fc9f31a1cb | -14.86694 | -48.90738 | 2024-09-27 03:49:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README58.md)
