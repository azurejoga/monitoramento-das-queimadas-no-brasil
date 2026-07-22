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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f53acd25-31e8-346f-9905-f91a9bcd25cd | -21.19847 | -48.27155 | 2026-07-22 04:49:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91607996-6d67-3b63-afd3-5332cd15ef54 | -19.51431 | -49.6835 | 2026-07-22 04:49:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28d32794-fe0a-373e-95c1-d908df889570 | -23.19262 | -49.15192 | 2026-07-22 04:49:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ab9b29e-ef37-330d-be3f-4d13e8896eb0 | -22.14537 | -44.53283 | 2026-07-22 04:49:00 | NPP-375D | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63bcd4aa-c165-3dca-9e2e-2159604f25e6 | -22.21044 | -49.733 | 2026-07-22 04:49:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad04b2c8-a174-355b-a70f-5e4eb8fa060d | -17.5748 | -47.4996 | 2026-07-22 04:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 534b8a50-aa50-3748-8bbc-7d6332067d38 | -17.5947 | -47.4956 | 2026-07-22 04:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| c4e808b0-2e9c-328c-b339-25152c0b43fb | -17.5748 | -47.4996 | 2026-07-22 05:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| abd942e2-b41c-387b-aa07-88a7df091288 | -7.8354 | -47.10914 | 2026-07-22 05:01:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec1e27af-91ef-3fe1-9993-c5db2fa5869d | -5.31033 | -43.05787 | 2026-07-22 05:01:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e46712c-8d3b-3c06-a144-bfc414f320d7 | -5.67037 | -43.57444 | 2026-07-22 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfb7c273-b5b0-3a99-86cf-5d0ade9fead7 | -0.85604 | -52.71502 | 2026-07-22 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c756632-6a85-3138-b640-ae33346d190b | -6.04323 | -43.87434 | 2026-07-22 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c9db466-b5ef-34a6-b6a8-e10dda165bde | -3.63858 | -49.71058 | 2026-07-22 05:01:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 499af85d-aa8a-32b3-a6db-710534477813 | -5.67625 | -43.57533 | 2026-07-22 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e44b34c-a2cc-3234-809b-de96f87539c0 | -6.21824 | -55.60358 | 2026-07-22 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5156696c-b0df-328f-b345-75dd3c1344ef | -6.15294 | -47.11647 | 2026-07-22 05:01:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2d83ad6-a233-3d45-a69b-3c544bb0cb7e | -6.54251 | -55.15281 | 2026-07-22 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9036380-521f-331d-b248-66246266b652 | -6.01317 | -47.1093 | 2026-07-22 05:01:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11d9c99f-20c4-3b47-92c8-674e931ed687 | -7.00437 | -45.42934 | 2026-07-22 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4381da2b-35a2-3f65-8fba-92c5755d81bb | -6.34373 | -48.4054 | 2026-07-22 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce73867a-fa0f-3494-93b1-f61753ad5ac9 | -1.8167 | -54.48357 | 2026-07-22 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 903bb57f-a1e6-3b6c-afc0-86b301c98e0a | -3.73189 | -49.27063 | 2026-07-22 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1c5e8ae-ab1b-3ad3-8034-9256e713da79 | -5.71268 | -45.66286 | 2026-07-22 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b80ff4a4-eae0-3cbf-aba9-c12c9b3b3b69 | -5.30971 | -43.06227 | 2026-07-22 05:01:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b344b664-f276-3d14-bc1c-f34c705e17e3 | -7.00482 | -45.42605 | 2026-07-22 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5e4eb737-2b1a-3ac0-b8b8-3bd998585a06 | -6.11771 | -55.8084 | 2026-07-22 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cf08165-82bd-3d42-bb39-bf5b1054d7e9 | -3.73048 | -49.27369 | 2026-07-22 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 16d3379d-f145-3bf6-b1cc-b46970bec1ae | -5.70757 | -45.66198 | 2026-07-22 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eb0746d-6613-3536-a739-35244b1d404d | -5.67096 | -43.57019 | 2026-07-22 05:01:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c6cde6f8-db30-3734-ade0-dff8c8293104 | -0.08704 | -51.27964 | 2026-07-22 05:01:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acae6975-34d7-34a0-90cf-2ad5a1cd8d44 | -7.35147 | -49.60138 | 2026-07-22 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 828969ac-f615-39fa-8654-98ed0e5d5f41 | -7.90183 | -48.27677 | 2026-07-22 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b428bff5-7369-3a40-9585-bcf1d7d8a819 | -6.56384 | -51.69667 | 2026-07-22 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ffe9ec3-aea8-3bc4-8665-3d55c326f99b | -6.04904 | -43.87511 | 2026-07-22 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9626dbb0-0f58-3878-89e4-3120e5116311 | -7.3499 | -49.60079 | 2026-07-22 05:01:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8d5c9fb-fb7f-3071-b65b-ea9b51355842 | -5.63637 | -47.09805 | 2026-07-22 05:01:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59172a5c-feda-372a-8707-00c2dbcb5313 | -3.728 | -49.27004 | 2026-07-22 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6daa83c0-7b5a-3490-bc71-7ba10c7c103f | -6.56323 | -51.70065 | 2026-07-22 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6464653c-1f24-3b70-92f0-6cf628af1013 | -6.59495 | -51.70553 | 2026-07-22 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea4d3fc9-f1b2-3f72-afa0-bd7c3c0141cd | -6.12109 | -55.80894 | 2026-07-22 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b22a6618-ab9f-3d8b-8909-489401c16eca | -6.53919 | -55.15229 | 2026-07-22 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f6de10-760c-3ab6-bc24-580ab1572a62 | -6.04959 | -43.87108 | 2026-07-22 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92cac025-ec20-3418-885b-c1fbbfe325ff | -6.04268 | -43.87834 | 2026-07-22 05:01:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2342b24-7b61-379c-b7ba-ef043cb9a594 | -7.90625 | -48.27746 | 2026-07-22 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40a806ca-4480-385c-b017-07da2324f95b | -1.81781 | -54.47652 | 2026-07-22 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49dfe78a-37ec-3edc-bf9f-795b86826077 | -6.53863 | -55.15577 | 2026-07-22 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 879cba2c-7f2e-3e27-995d-17c0907de76f | -9.1847 | -58.06477 | 2026-07-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62403d1d-714e-309b-8d74-16fcf468a508 | -11.32871 | -48.00634 | 2026-07-22 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65578509-7d87-38aa-ad55-0df416a62c23 | -13.33321 | -54.31622 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f321af6f-e983-3b6d-9859-b389e3c5738b | -10.62899 | -46.59694 | 2026-07-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d203b754-97e2-399c-87ab-e1e04e960430 | -9.22708 | -48.55505 | 2026-07-22 05:04:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab048c31-0e4f-3a49-be06-3880329fcba3 | -9.90234 | -47.87677 | 2026-07-22 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afd7ff40-2b83-3d0d-a519-4acf2ff4c102 | -14.43468 | -56.44425 | 2026-07-22 05:04:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb05d8f1-67a6-3c5c-92f4-f089aa3ec69d | -9.10384 | -59.4034 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eca01e0f-9df0-3bab-a05c-192947a10725 | -12.41247 | -62.03366 | 2026-07-22 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9c8e0f0-b125-3094-9383-837c641d8b80 | -8.7539 | -49.08111 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ba2dc7d-9e9a-3ffc-8d9b-a7bd7f5b13e3 | -12.66581 | -48.22007 | 2026-07-22 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf74a08-92fa-3473-b634-bb7a71f0b0f3 | -10.62381 | -46.59641 | 2026-07-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77b01450-35b0-33b1-9843-5f977d690e30 | -13.36879 | -54.31043 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a898b64b-2145-33ae-8b46-89498735a705 | -8.75446 | -49.07713 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24f17477-d2d8-3f35-a983-e380217fb263 | -13.32192 | -54.32203 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 512169bf-50de-3f1d-a58d-275dce6de377 | -9.26249 | -59.8168 | 2026-07-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b208eba-cbac-3f76-8ac0-e191643f019e | -10.83156 | -50.44376 | 2026-07-22 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350b60c7-69a9-31e1-b97d-0183a4daf078 | -11.3344 | -48.00753 | 2026-07-22 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f59901ad-2155-3cc9-8f1f-4bea8783c5d7 | -13.31627 | -54.31353 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526bf9ca-508d-33a2-9c68-b0e1c92d52c5 | -10.83205 | -50.44027 | 2026-07-22 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd2c230b-fed5-3244-aca6-1d4bd16f3ba9 | -13.32248 | -54.31832 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ff15f34-3641-3706-b90a-81be59c87d00 | -15.2409 | -48.57031 | 2026-07-22 05:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29239130-3617-3aa1-a28f-9b6933859e5c | -11.81664 | -47.33566 | 2026-07-22 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0314ecaf-91ee-3c79-a9b7-b0fb931c575c | -12.02832 | -50.55091 | 2026-07-22 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8cf9456-52a6-3caf-b7a3-d167b701cb98 | -10.01978 | -65.05058 | 2026-07-22 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae279557-cd1a-3781-bfb5-6560e79624d2 | -12.45488 | -46.51691 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbff7483-46f2-3ae9-bb90-be503a76d513 | -8.74544 | -49.07978 | 2026-07-22 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 024ce6d2-5b49-3df5-bc78-296bec0476a6 | -7.61242 | -55.2636 | 2026-07-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0355bd44-5877-3452-982b-ed07ec9dd716 | -12.4553 | -46.51357 | 2026-07-22 05:04:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff7ef86a-ef98-334d-9686-3a68464517a5 | -13.33716 | -54.31302 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3beedbed-e2e6-375b-9159-81897e858a55 | -13.34337 | -54.31783 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81a563cc-8095-3767-8bdc-d645ca95ac36 | -10.42563 | -50.20183 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d85d313-382c-3493-8c8a-522b996c8e19 | -11.63858 | -48.54443 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78be4c22-a873-3b60-8ab9-033e84e73ec6 | -11.39848 | -47.503 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f570c5fa-d427-35f0-a152-60dcb34fda8f | -10.50656 | -50.27816 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 654df4f4-ef4d-326c-9b30-e154d775e204 | -10.5407 | -50.26868 | 2026-07-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 009f89f4-49b2-3e32-a74c-9d3ff8f66ac3 | -12.41321 | -62.03533 | 2026-07-22 05:04:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bdc1d95-cd53-30a8-9167-56e81f64051d | -13.32869 | -54.32312 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f944c8-10ac-3be0-a6ec-c592d56c136d | -13.31345 | -54.30926 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62425621-c09a-34f2-bcbd-21c38bafac20 | -13.32135 | -54.32575 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d8fd2d5-ac25-332b-8c35-204cc1140d14 | -13.33884 | -54.32475 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d94507-8a27-3895-b011-0eb52bfae09d | -11.88561 | -43.83309 | 2026-07-22 05:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73019a03-5e1e-3926-a284-43045cc2340f | -11.634 | -48.54376 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e71c1781-8227-38f8-b01b-19e48e7a75fd | -11.38873 | -47.48552 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 198be4bd-1b41-317c-95aa-86d9fab002a6 | -9.69685 | -47.70191 | 2026-07-22 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8028348a-a1c5-3b9c-af64-6b207725150e | -12.09287 | -53.33484 | 2026-07-22 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 131f2f38-3973-3f8a-a78a-84e82da4e87c | -12.1394 | -48.25586 | 2026-07-22 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3bad54e-12c9-310b-830d-769198cb0a3d | -12.3273 | -50.01214 | 2026-07-22 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94b8d1c9-81ad-3267-944a-448aac0928c4 | -11.40836 | -47.50383 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c86c2cbf-91af-3647-9ae9-ea61ced6963a | -12.3257 | -53.27673 | 2026-07-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd0c24b-90ae-3f42-9c92-ab8ccbbbea99 | -11.4021 | -47.49774 | 2026-07-22 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 322d0973-6bbf-37a8-a109-01d988ca9421 | -13.3654 | -54.30989 | 2026-07-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 655db843-d2ad-338d-92b7-22b086774a27 | -9.47586 | -57.31846 | 2026-07-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
