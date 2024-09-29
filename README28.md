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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2899d319-1558-306e-9863-05018e94e598 | -8.07605 | -42.92105 | 2024-09-29 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d4b683d3-56d6-3bfa-995e-f9a674b179b9 | -8.31253 | -43.38367 | 2024-09-29 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dc325c7f-70fd-34d1-a18b-01e10627869d | -8.0802 | -42.91764 | 2024-09-29 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 17492d25-c5b4-3592-ab75-f7045abdc565 | -9.288 | -43.50251 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 42406e02-98d4-330b-879e-9771c2a585f8 | -9.28644 | -43.48977 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b2b0733c-743d-382c-8304-eef6dda97e58 | -9.28578 | -43.4938 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7d4e7ae4-d68e-3f31-a32c-31a4c3b88849 | -9.28511 | -43.49784 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 01f20eee-b794-3184-a3ed-01ecdbf1fce1 | -9.28444 | -43.50191 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 4e5ff088-92d6-36a9-a38d-5001e074ed18 | -9.28156 | -43.49725 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 23741371-9bec-3f70-9a54-e944345ae17a | -9.27558 | -43.46716 | 2024-09-29 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cec5fdf-f5b1-3a19-b1a0-d3531639028c | -9.26734 | -43.49488 | 2024-09-29 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4eb2c405-b962-35c1-869d-de577c293acf | -9.19598 | -43.40015 | 2024-09-29 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e0e8420c-e62d-326e-bd6c-57fa940ecb40 | -9.18669 | -43.39027 | 2024-09-29 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c5f6e8f-65e7-3a2a-9334-857f665d500c | -9.18337 | -43.41041 | 2024-09-29 04:02:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0944f1ac-b275-3d75-8923-1f1aaa272484 | -8.32189 | -43.3937 | 2024-09-29 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea3a1a5f-b29d-3065-abd6-0a6d141ce54e | -9.95635 | -44.02763 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fef2c3dc-c929-39d4-a260-f80a7239fba2 | -9.95273 | -44.02701 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2807fec-afdf-322d-895c-df074b39aad5 | -9.94911 | -44.02639 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3c63d14-ed44-3f8a-a59a-942c2f28c787 | -9.94698 | -44.03917 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8c2bba7-3f3a-3d0a-933e-82516830fdb7 | -9.94478 | -44.03002 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7817334-745f-3615-be4f-919e7936790a | -9.94335 | -44.03855 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3222bbf-1a0a-34ca-8053-5e2214517b79 | -9.94264 | -44.04282 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a54b38cd-4d0c-3a0c-9faf-ec2e9eca0ed7 | -9.94193 | -44.04709 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea3ce665-c0b9-3068-b4db-a7913fb11dac | -9.93973 | -44.03793 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d97f5b-e7df-3f9d-80b7-afc9cc63322d | -9.93902 | -44.04219 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6b3b3b-de42-3818-a2c7-7ef0e36333e2 | -9.9383 | -44.04645 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2985d7bf-9f1e-3775-a2c2-1da5533d9447 | -9.9354 | -44.04156 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5682260b-18c9-3552-99d9-08b07ff335f8 | -9.91658 | -44.06475 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05089a66-67f0-3160-8db4-164a16968fd4 | -9.91295 | -44.06411 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 440f9693-48cf-3b99-a04f-2cc943d732cd | -9.91005 | -44.0592 | 2024-09-29 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f2435f-6dfc-36aa-bbb9-69d4f4c7c57d | -9.4869 | -44.0719 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca7400e-aec6-36e4-bfe0-82c18dcf1277 | -12.8209 | -44.82751 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 841c62e4-e2b0-31cb-a2a3-8bf1bcf839a7 | -12.82078 | -44.84989 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6886de4-d5a7-3637-b9eb-7cfe8192227c | -12.81864 | -44.84055 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7d010155-5b36-3048-8789-ed54d65621f9 | -12.81789 | -44.8449 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ac98b767-52fa-3217-b1f6-6d30283f945c | -12.81714 | -44.84925 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e8cc6750-d3cf-3dfe-9506-20a132159fea | -12.81512 | -44.81757 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1f9716ad-5e11-3d94-ba8c-bb72e6808c9b | -12.8151 | -44.81475 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8aa8b205-17b1-3d5a-b6ab-b9a06a4bf2e0 | -12.815 | -44.83992 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7efa5a58-2daa-3443-9c95-a821a2a36a7a | -12.81438 | -44.84149 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2c4068c7-6353-3451-a111-b2c50648906b | -12.81438 | -44.81909 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94722b1c-47a7-36ef-ad8e-40a5cebfc405 | -12.81437 | -44.8219 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e824707f-2761-3f4b-89db-3ce4c4dbc019 | -12.81425 | -44.84426 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c46e3259-fe6b-31e9-8155-75b839dc0081 | -12.81365 | -44.84585 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 71b532c6-fb5a-3843-8e31-7142ca1e63d3 | -12.81365 | -44.82343 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c2cdd0b2-78d5-309b-bb69-805fa2f10e4f | -12.81362 | -44.82624 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f9f22563-a535-37f7-a368-ff3816ddefd6 | -12.8135 | -44.84862 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| efab7453-81be-3da8-adf3-1345c4ff47eb | -12.81292 | -44.8502 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6af1b1c2-6735-385d-aa7f-b292c366eb50 | -12.81292 | -44.82778 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8f4fde1a-0980-37b1-a66e-96a6e3332b05 | -12.81287 | -44.83059 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe79a192-2b97-31b7-a8d2-a648e8fdc606 | -12.81219 | -44.83213 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 379a5a1d-9ed9-38c4-9427-ee096c7c2744 | -12.81212 | -44.83493 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7b546506-2e83-3a73-ab1a-de36ca1daa57 | -12.81149 | -44.81693 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 943b0049-5d50-3360-bbc2-0040d3ad330f | -12.81147 | -44.83649 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f44d57d9-c8f9-37ed-857c-7227242fe711 | -12.81147 | -44.81411 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 35bcf086-bfb0-35a0-bb20-61818e8d0fe3 | -12.81136 | -44.83928 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0b1ee262-12ed-341a-8309-a9aef0ec95e7 | -12.81074 | -44.84085 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fbc050d1-77c4-3b9c-a745-788c0ebc136a | -12.81074 | -44.82126 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a512e2e7-cb6b-382d-893a-99cc06b460a6 | -12.81074 | -44.81845 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c5531ea3-4e04-35c9-a826-3a923561a285 | -12.81061 | -44.84363 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f76b4586-2592-3d7a-8446-737f0eb4039d | -12.81001 | -44.8452 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 15e5a1be-90cf-3e8d-a023-86495ade3793 | -12.81001 | -44.8228 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 80094c4b-a3ce-3748-a0a8-ba20a7ce310d | -12.80985 | -44.84798 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb212ad5-0c2a-36a3-a1e3-baefe877c606 | -12.80923 | -44.82995 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1f1795a7-c120-32ce-bec3-42f48cfe59b3 | -12.80848 | -44.8343 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5d07685e-43e3-3c8a-8406-0f5337292b21 | -12.80783 | -44.83585 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a7f83df-9ca5-3df1-9262-2ab9630d6009 | -12.8071 | -44.81781 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 82addb76-1c55-3347-b79f-dce071368e34 | -12.80638 | -44.82215 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 54f291a0-cccc-3cd7-a005-8a503f9835e5 | -12.79983 | -44.81654 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b3b28265-8f5e-32cc-af01-64a6917d9b98 | -12.7991 | -44.82088 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d2fbc00-e118-393e-ab8c-2f7159d164f2 | -12.79692 | -44.81156 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa4cedaa-c3df-3f9d-b69a-51c40decdc6f | -12.79619 | -44.81591 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0a26c93-5a67-3006-8808-b787259d8524 | -12.79546 | -44.82025 | 2024-09-29 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae715715-643f-313e-ac78-d89d9176920c | -13.62076 | -44.10428 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49b3945b-3203-3960-a7df-92c73ffb87f1 | -13.44091 | -44.02584 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c61c4762-1270-3d4d-b28e-2d056786686f | -13.43743 | -44.02525 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b230a57-d8bb-37cd-8514-f3cf07bece21 | -13.43395 | -44.02466 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 465b85a9-de53-31ee-90a7-ef8ea9440cbb | -13.43328 | -44.02861 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 397ffcd4-25e9-3e9e-981d-187a964b5166 | -13.43046 | -44.02407 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43628c2a-c3d0-3a34-b7ef-029933379626 | -13.4298 | -44.02802 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f248560d-4bd0-3656-9a31-214db0649aa8 | -13.42914 | -44.03199 | 2024-09-29 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef2a7511-6768-3632-87df-69c4b84994a2 | -12.73771 | -43.47335 | 2024-09-29 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f048acb1-dc62-37a8-aec4-04ef46a308e2 | -12.73428 | -43.47277 | 2024-09-29 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca42d6e5-3fbb-3878-b8bf-29933a43c950 | -12.73364 | -43.47659 | 2024-09-29 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2887901c-858f-3a1e-9359-31930e7527c9 | -12.58617 | -43.83536 | 2024-09-29 04:04:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| befde3ee-7e9d-3bd6-904a-a88abb8bf7fb | -12.58551 | -43.83932 | 2024-09-29 04:04:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6ab3ec6-c7db-30dd-9fac-aa6a679e9e9d | -12.58202 | -43.83874 | 2024-09-29 04:04:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a303038f-195c-3ab3-83bd-ca1833794863 | -14.52111 | -44.97285 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f5d86a5-d5b0-337e-9fa5-a0df1f42e025 | -14.5204 | -44.97709 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a624a591-9130-3a3a-b1e8-abfe7e2c8bf4 | -14.51394 | -44.97155 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8de1b8a-0a30-3e8b-996e-1d3856bd0228 | -14.51324 | -44.97571 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8cf1320-6652-3716-bd61-e827549afd47 | -14.51036 | -44.94902 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e47dd747-cfea-3416-81cf-c9cb9f146102 | -14.51035 | -44.97091 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff94c7f4-db15-3c59-a143-aa5a24fc8e94 | -14.47952 | -45.24088 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27bdd80d-7f1f-390b-9232-3b3009fc42c1 | -14.47878 | -45.24529 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42ca5236-84cf-3aaa-838c-026d7ece5fa3 | -14.47634 | -45.1057 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de31e842-00ec-3df1-ba0b-481898d71212 | -14.39754 | -45.19456 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e593c17b-f1fe-34f9-a04e-cff96802377a | -14.38874 | -45.20202 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae7473a-81dc-3275-920b-db37830f5ba7 | -14.38817 | -45.20348 | 2024-09-29 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ba1f06c-0b73-31ef-9f21-685ff486e345 | -14.67681 | -44.352 | 2024-09-29 04:04:00 | NOAA-21 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
