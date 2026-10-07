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
| 90abcac1-0886-3265-831d-f2b986bc7ffc | -9.75262 | -44.79855 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd2222a-644e-3d12-a371-2682abf648be | -11.06192 | -45.72052 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1bdd03a-0f66-341a-9fec-e4652eb48e27 | -11.78564 | -43.53747 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf99c206-088a-324d-9514-522232718812 | -9.51555 | -54.74197 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55e09bb2-28b4-35d4-b7d2-7b15bd0e2bb9 | -12.16022 | -44.70184 | 2026-10-07 04:21:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9db2df1e-7d77-3aae-9acc-801c23d26dcd | -15.25142 | -43.27076 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 50.1 |
| d9e0c090-08f9-37af-bee8-c1850a2f84a5 | -11.06478 | -45.8518 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be6a94fd-b72b-36b5-aa0c-ccf2a53d3b55 | -11.108 | -45.71313 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16985506-e014-3706-a664-1d6e1306e5fb | -15.4176 | -43.70096 | 2026-10-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 78a06a63-d264-32c4-8a85-1e57c78d0603 | -11.1064 | -45.70168 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07f4119a-ec3e-3185-b53d-a3d1752c18e2 | -11.3696 | -46.71275 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06f6975e-89a1-3743-a40d-9ec7fe475924 | -8.58883 | -45.67288 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d92f4d48-82f9-387b-ad82-6a48dc3c0b7a | -9.51657 | -54.74421 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e44e1d2-0505-3b12-b00b-2425ed79bedf | -8.44024 | -48.91489 | 2026-10-07 04:21:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2969b664-15a2-3611-b250-9f728a42efc7 | -10.85828 | -50.68201 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63575450-53e5-3c45-a5df-993a55270422 | -10.49018 | -50.43603 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53d08719-9d46-3172-b4f7-ebe5aa6af9c7 | -8.28394 | -50.27736 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 972664ab-1a20-33eb-b5a0-b5b19c601319 | -11.01458 | -45.46861 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58fdcd5a-53fb-3524-8645-de4276a0bc8b | -9.80864 | -44.78959 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afed6070-15c1-3848-b6d6-5b0b606e2703 | -11.69993 | -40.1143 | 2026-10-07 04:21:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61cb5dad-ee31-3377-af3a-787c94b1f82a | -16.12885 | -43.74221 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16deae64-d265-32ea-9545-4cf034ed0dd2 | -13.58231 | -44.42673 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7831f318-576c-3d71-a1dc-a07446db5ac8 | -15.23654 | -43.27629 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 68de6a6d-c0bc-3699-bf17-3677ef3c7f6d | -9.25537 | -45.65116 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 733506c4-565c-349a-acd1-253a9373aceb | -14.78543 | -42.27084 | 2026-10-07 04:21:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd0fd90c-7288-36f3-bcfb-f7b9c86c6e2a | -10.2408 | -47.0677 | 2026-10-07 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a29a7f2-b700-35bd-b5f1-cdeae2f78f05 | -16.61193 | -39.5894 | 2026-10-07 04:21:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 214558d0-6e61-3152-b3e6-4019cebee78f | -8.28996 | -50.2693 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 47343613-ca84-348f-a12c-b82993aed5fd | -11.37944 | -46.67448 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94511bfd-25e1-30bc-8949-7ee3cf7da5b6 | -9.25876 | -45.65177 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 695e6ad0-0045-35a4-b543-2848991fd2bd | -10.37066 | -45.0336 | 2026-10-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b211a6-1880-31a8-a6d0-883eb89327bc | -11.7053 | -43.66339 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39aeeaff-9dae-33c7-8eb1-2c2891908db9 | -11.67362 | -43.62556 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01d298af-4100-36fb-a2ea-0bba0e662545 | -10.46972 | -46.82827 | 2026-10-07 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a21ef846-4c81-3ce3-9d7f-c62c5b17a644 | -16.27318 | -43.965 | 2026-10-07 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c7dcc12-8197-32db-ae0f-662fc8b66468 | -9.81252 | -44.7866 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479325b9-6ceb-3e40-bc38-4e74333e88bf | -15.33332 | -42.76642 | 2026-10-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 450d2a8b-997a-32a9-aac5-7019a51dd0ca | -13.97458 | -42.5039 | 2026-10-07 04:21:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d6a7c962-10ae-3c85-bd07-dec614c0d44a | -12.20771 | -44.65922 | 2026-10-07 04:21:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc43ff9d-a95f-3dd9-8a06-a41055f6412c | -9.17645 | -50.60735 | 2026-10-07 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10136d84-4ec5-3fb3-ac4b-d6bea0e5b010 | -9.51472 | -54.74624 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b0c02e2c-21cd-310a-ac3b-fdfbb11d17ca | -8.70137 | -45.20178 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69ee1da3-2c59-353f-aabf-17a13d1c739b | -8.58945 | -45.66907 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9e05d83-7809-3fa3-ab6e-bf6244479384 | -8.43962 | -48.91854 | 2026-10-07 04:21:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98cf233-a5cc-3b68-9dd3-44a4bb003bb5 | -10.14448 | -36.24726 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 1ba02e70-5d23-39aa-b57f-00e27f869023 | -13.02567 | -46.79729 | 2026-10-07 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 759f6cbe-09cf-3b12-b8a3-a9b6f41fdcd4 | -11.22678 | -45.26831 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a72cc90f-c504-3434-a1de-5071b97381c8 | -11.83402 | -43.5343 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aadf0125-1300-3b28-ac71-03bf445dcd62 | -15.3224 | -43.09468 | 2026-10-07 04:21:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bcb2987e-69a2-39d1-ba8e-cd2701a4282f | -8.28473 | -50.27295 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1212ab04-4215-314e-99c9-2a436c3172e1 | -11.70475 | -43.66694 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc08efd2-0552-3444-9525-b8d1fe7bfebb | -9.89634 | -44.81499 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79f50b74-8c01-30d4-96d2-d788c56df09b | -10.47795 | -50.42942 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d2fa72c-4fc9-302b-b47b-80a9fe24ddcc | -13.0288 | -42.67513 | 2026-10-07 04:21:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 52c9e89c-50b3-3280-94c2-29302b7cb5e0 | -9.91189 | -44.80309 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1019bb11-9f97-3c2d-b197-e0d32ca8f09c | -11.23918 | -44.87513 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6fb85f6-9bae-396a-8ba8-7f615e0895bf | -11.22649 | -44.86945 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65434049-0390-36ef-b5d1-da4d2942bc54 | -12.16342 | -44.25177 | 2026-10-07 04:21:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7b9ff91-35d4-3437-a865-21bad5ddc9cc | -12.19162 | -44.7178 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c719d16e-f191-3128-bd55-19227cec1b19 | -9.24798 | -45.6537 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c20dfbe-4faf-332d-b176-f8f38fc2e82a | -11.62934 | -43.67336 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 782f9976-ebfe-35f6-87a1-35c93b0be121 | -11.73416 | -43.65341 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fb1c3d7-76c5-3357-a1db-3c5ea3b8ca64 | -8.69505 | -45.2193 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b827cd4-b773-3455-bd43-ce2d426af6b8 | -9.54207 | -43.03862 | 2026-10-07 04:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3895785b-118e-3297-b734-0a2ec096d9c6 | -9.87915 | -44.81583 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 705ec9ab-576d-3792-ac46-379b8193bee0 | -11.38226 | -46.67897 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b36897d2-683c-3496-b5f8-22a3d056626a | -15.81198 | -43.93905 | 2026-10-07 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61942efe-aa43-3642-b7a5-f0252d738734 | -9.16062 | -45.11746 | 2026-10-07 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a3028ed-8a60-305d-b51c-dea8186df149 | -11.62104 | -43.66099 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cfb0a77-9250-3463-9c04-83b4cfe45e1f | -11.11222 | -45.73966 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d3725d7b-03ee-3987-a893-a7b64751ea8c | -15.252 | -43.2669 | 2026-10-07 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 56c22e45-474f-3302-86dd-f7a6469e15f5 | -9.80358 | -48.91826 | 2026-10-07 04:21:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d0a086-9b3c-3d2b-b7ef-39c0ee6b9e2a | -8.90296 | -49.97399 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ea7c9abf-e275-382e-94fa-08e543e2c565 | -11.37622 | -46.69416 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76d8dcd2-eb81-38a1-a99c-1968a0363218 | -9.92031 | -47.84729 | 2026-10-07 04:21:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e43657e-6a26-3891-8961-ffff6a2c0632 | -10.49377 | -50.44102 | 2026-10-07 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45d53b30-011c-3350-aec2-370bc6372157 | -11.36868 | -46.69672 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3329074e-e2f6-3b10-b538-6b4052f514ac | -12.38798 | -49.81907 | 2026-10-07 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bdb7d36-c26d-31a7-bf20-d134aebd3ea3 | -11.67084 | -43.62148 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ca99619-5f3f-349e-9b64-b9ae5ce7e14b | -11.00864 | -45.44161 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ea3635bc-d89a-3dbe-8ef2-a05d7d12ed14 | -9.87809 | -44.80121 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e298e7e0-f013-3eac-b9e3-19f7f0745c81 | -16.04142 | -39.84417 | 2026-10-07 04:21:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fb004240-3bec-32a7-a50b-6d202a60adff | -9.25996 | -45.64437 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed77b64e-26b6-3569-a396-4f244c56a2a5 | -11.60925 | -44.14758 | 2026-10-07 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed999a73-e4a1-3100-a777-13cd442d1da8 | -11.06159 | -45.82878 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54a16bc2-2084-3d78-a8f1-95dd0c95061a | -11.22705 | -44.86593 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc8a3168-40ca-39f5-837d-96fdd1165a96 | -11.71564 | -43.4197 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5bc99a4-84f3-3846-90e1-aa534381cea4 | -8.28107 | -50.26773 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 089189a0-21b4-3386-af41-a8de2182ea1d | -13.37931 | -43.87401 | 2026-10-07 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| adc5236c-41c9-3cab-ae94-9e661c5f76ec | -11.79901 | -46.70399 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 260a62ef-bdcf-3c71-9618-1b54c7497c48 | -9.8742 | -44.80419 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69035a37-2024-3eca-bfe1-454f15f40e86 | -10.59435 | -51.83689 | 2026-10-07 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b603d778-15d9-3379-b45c-43991c69e229 | -11.37277 | -46.69351 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02edd460-c491-300c-afb5-5ac908a4419d | -10.14624 | -36.25164 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 78113baf-d71e-36ba-94e2-a46c8cd579dd | -9.51575 | -54.74859 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42626e1f-a458-3760-b554-1bf6cc93fdfc | -8.70591 | -45.19511 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29c8e8c5-de15-3f45-b07a-c202a48056c1 | -9.34868 | -45.42604 | 2026-10-07 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398198df-5c45-3ca9-9d49-b25d40d2417e | -11.22345 | -45.26776 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96585628-da3e-3c7c-8ed5-ed0df78133c9 | -12.16628 | -44.70644 | 2026-10-07 04:21:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96ad1858-8512-3779-bb71-17da99bfc968 | -12.16565 | -44.17265 | 2026-10-07 04:21:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README60.md)
