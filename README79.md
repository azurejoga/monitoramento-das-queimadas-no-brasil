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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c428e7-7991-3bf7-93b4-0a9484dcaca3 | -19.05788 | -48.33994 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d11324-4057-3c59-a7e4-efe7151b7b12 | -12.56949 | -44.73127 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b890b5b9-f4e3-3c1a-b184-7042257a75c2 | -12.97971 | -48.01237 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 923cc363-a226-37c1-8970-8bc1af07a091 | -11.86582 | -58.81702 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92809189-152a-38e3-9265-1e2cd95efc74 | -17.14039 | -48.5001 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9289a9c-4e31-3382-981a-4d75d47f6f9c | -14.43325 | -48.41944 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f4dd384-c56a-3ded-b7de-1972bd4dc85c | -14.42189 | -52.92902 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac1a4ee-b089-3c03-bcb7-bd9103f3f007 | -15.68602 | -47.01104 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16d3014a-3067-37f6-a915-9fd78a42f1fa | -18.68231 | -47.6679 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 648f5780-0d07-3e6d-8a0c-eb3587e301e6 | -13.36477 | -41.91791 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48e08b68-8a88-372f-aeee-424d00f42d69 | -19.63612 | -41.58221 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b9344016-d499-3057-a375-8fee1f757b73 | -17.78641 | -51.72895 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fc3ee55-a68b-3cfe-8a20-b685045fdee5 | -14.16705 | -46.19993 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb9882fa-dbb0-3047-85ae-332f125014e3 | -17.13376 | -48.49897 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c719aa8-c121-3230-8982-cc2e9b167875 | -15.07499 | -48.01132 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd60fbff-f1d8-3f02-951a-a9ae511a40d5 | -14.71897 | -55.61021 | 2025-09-12 04:27:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdc6db02-37c2-3a4a-b355-ba805784982b | -13.53557 | -43.00826 | 2025-09-12 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d97819a9-e5d9-365f-ac9d-de193be7b654 | -12.83766 | -52.9442 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3081649c-cefe-362a-b5ee-ba9e8d5a0d5b | -17.21242 | -48.68953 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe2c3354-7a8f-344d-ab90-b4b2dee47b2a | -18.62135 | -48.24968 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9db6dfc2-3aef-39ea-b223-807cd421afd5 | -14.18473 | -46.19848 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b1d48a3-5eac-34ba-b421-46d050ba9963 | -12.93849 | -54.7491 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b775ab2c-53cd-3e3e-9e67-a16e45afc902 | -13.95266 | -48.21682 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb58f196-e67c-3e55-950f-6b89718bba91 | -18.30132 | -50.42765 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56a14613-c64b-3f32-9c9e-aa2a888ec8f6 | -18.06279 | -45.42742 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97e17991-f0e5-3adf-818f-a4dcd5f29211 | -17.72358 | -46.13617 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd2ebe15-6016-3581-bf7d-74c45679ff0d | -14.1739 | -46.20085 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 781d5164-c13a-30c5-a539-5e04bf497712 | -14.45081 | -47.30883 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97de70c5-6020-32da-b5e3-8590ea446927 | -18.05672 | -45.44458 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 130f4f53-3f45-32b8-8120-67d0cb4b169b | -14.38385 | -52.95969 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2496455d-3963-376a-9366-710c78a34348 | -18.02258 | -46.86113 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77a7cb2b-ad57-3d57-a55a-482098c98527 | -14.17501 | -46.16977 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a60a5524-915b-3125-a70e-8d69aa1ffb2c | -14.55895 | -54.52246 | 2025-09-12 04:27:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7d19503-45db-35e0-a1bd-3583c15c73d7 | -11.87082 | -58.82323 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc66e9ef-f72f-3e0c-ba3a-724b0211b73e | -17.21128 | -48.69674 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 344e0340-3b4e-3a82-b1c0-64d9e460d1a4 | -12.82305 | -47.97273 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b8be0c0-79fb-3f61-b4f3-ff463466b0ca | -16.25178 | -52.65337 | 2025-09-12 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3a37503-83c1-3fd2-ba21-b41d23a7c46d | -13.32654 | -43.59343 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f74b5c42-0c43-3247-82a6-02a20326e73d | -13.16714 | -45.2837 | 2025-09-12 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a1c43aa-c938-3cda-9cb0-6392610b1b64 | -13.89961 | -48.22988 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0991f5c8-7dae-31b3-94af-3c919c8cfe52 | -12.58345 | -45.68262 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e48abdd-3a52-33ac-9df7-3d58489141d3 | -17.93597 | -46.92786 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c8da46e-412c-3765-ad97-768df6d53f9a | -16.88347 | -45.75782 | 2025-09-12 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa336bd8-afb5-3f92-b9cb-13a0309763b9 | -18.66039 | -47.65264 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 090f4784-6338-31d0-be16-b214733d48f4 | -13.32271 | -43.59286 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35338abf-f077-3666-9fd8-747dfb99730c | -12.90748 | -47.97574 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d8c8e3b-c466-3396-9b80-fc3212129afc | -15.12504 | -48.5974 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cd05bf0-71ad-37c4-bd79-98eb03fd6501 | -17.80631 | -50.00396 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a5b3529-2107-3a2d-9452-573e63c240cd | -18.38495 | -50.55793 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 557527e0-510d-3a7c-99f5-ccdb95fb0ac9 | -19.63549 | -41.58755 | 2025-09-12 04:27:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c27a8ee-f48f-34be-b4a6-6b8a59374c33 | -15.81171 | -52.21884 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcc64102-c222-3583-b18e-4f88591e77c7 | -16.43899 | -49.02839 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0282f105-019f-3d2a-ac42-15d3ec0deb04 | -11.9423 | -51.18402 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 18ab39e3-a1b5-37dc-9c19-5edbf395ff26 | -16.51459 | -55.16847 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3d48a1b3-c295-3d31-91d5-1866f0ffbe1e | -11.99584 | -51.17326 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94718319-7353-3e5a-986c-7a5471bc82b0 | -12.47704 | -53.82209 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b3f1b7-57d9-3f52-bc02-b29a9306370b | -16.43338 | -49.04225 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c80e21f-491c-318b-aea4-d4abaff38491 | -18.05998 | -45.42529 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df422188-476a-38eb-944d-4b9c7b94c600 | -17.56431 | -44.55085 | 2025-09-12 04:27:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf2650d6-86c3-36d6-bc9a-cba002d4680b | -14.03994 | -42.15025 | 2025-09-12 04:27:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d92e312c-d91a-325d-ad94-7f9ffd26736e | -15.22289 | -44.05964 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eab48205-5646-34ee-9e33-075bdc66b334 | -15.49373 | -47.34598 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70ff6bbe-cc0a-3401-9391-df1f8c8e6073 | -18.05792 | -45.43571 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcd9ec19-e289-3cc5-b0ba-ca6d953c8771 | -12.84051 | -52.97457 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74e3f6b3-4658-3cef-ae7d-347e3ad5b516 | -15.68223 | -52.22603 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8a44935-005f-3fd8-8221-2d4a1036ba15 | -15.65356 | -47.05636 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae938254-8698-394d-91be-d66de71bcbcf | -19.19008 | -48.01143 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e34aeb3b-996f-3361-b49e-76140522499a | -18.39295 | -50.55162 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19711c9d-9819-32d8-b995-7762cbe59e79 | -11.98275 | -51.13906 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fcc77f1f-d5bb-322d-af54-c272dcd6843b | -13.27719 | -51.71702 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9c7de18b-4041-3217-b2e4-b7c66022f3ad | -12.80426 | -44.75603 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfd0eb7e-fef9-3fe4-97bf-6a540873a1a6 | -14.17962 | -46.20938 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 26756691-524f-3c8d-90db-ca05a0158209 | -11.86982 | -58.82819 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7891752b-d1c1-379c-96d5-6bb0f2e40309 | -15.54553 | -49.74309 | 2025-09-12 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72ee00c-9288-374e-9fe3-78e1f31fe1d6 | -17.94226 | -46.93281 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f7de19b-3ed4-3581-a7f3-b00826f3b347 | -12.97472 | -48.02245 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 035c5e4c-513b-3f90-8b30-a8f503228501 | -11.96116 | -51.17624 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ea4c297-1c2e-35a6-be9c-c12fd2ea6b81 | -11.17528 | -55.06214 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e13c7ef-11d9-3010-b018-d6ace444be92 | -14.43656 | -48.42002 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf99a8a3-478a-3670-ae98-0d157217fd4b | -14.60313 | -52.03065 | 2025-09-12 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c65e9c5-fcd6-317b-870a-0b3322ae40bf | -18.67556 | -47.66681 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce3ddfbe-b087-3d15-941b-b59ab4e3908a | -14.60233 | -52.03528 | 2025-09-12 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c81f1d38-ac70-3486-930c-6d5c2f3be044 | -17.66553 | -46.67894 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 03dc7f26-18bb-3e14-a1fb-3469622d29d4 | -15.6922 | -47.01587 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 210776df-fea0-3a77-8755-9ed1149372e5 | -12.50691 | -47.43638 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d741285c-de32-3e63-852d-467ae33cbf89 | -11.18671 | -55.08041 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5b3833e-935e-343b-911b-2df2bd90a047 | -19.95374 | -44.45945 | 2025-09-12 04:27:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4c5bba66-b390-3dde-a707-27bad1bb7c8f | -12.2436 | -47.33983 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8476a70f-3b8b-3c62-ac6c-63e31d478f07 | -12.46882 | -53.83122 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d92aae6-97e4-3765-889d-f853d6b92a96 | -18.4499 | -45.07017 | 2025-09-12 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 439a4383-4ce9-379d-b181-6d71f21e2482 | -12.8114 | -44.75711 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40229293-6e04-3abd-b68a-e9fc5aa62a1f | -20.036 | -41.74439 | 2025-09-12 04:27:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| cd17eb56-a5a4-31a2-a4bc-00221c12e1bd | -11.97387 | -51.1466 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e639844-0a2b-360b-8744-9aa01344f6c3 | -12.42825 | -47.80645 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7aab4986-90f4-37aa-8c11-fb2267e62a51 | -15.1531 | -52.46603 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed9c32e5-15e6-30ef-ba63-25244ccbf1f5 | -17.35819 | -46.69592 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6887a806-485e-3f1e-b4dd-f5a6c9bec81b | -18.38158 | -50.55734 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb03773-af47-3db0-9936-12025fa29172 | -14.66423 | -44.06207 | 2025-09-12 04:27:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99b854f7-8385-3259-9212-d817c2499344 | -15.52257 | -48.55362 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 390ce98c-e7d5-305f-a1dd-9fe66051beae | -11.64269 | -50.58191 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README80.md)
