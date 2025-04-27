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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a73d8098-8daf-381f-b17c-a5336f350ee6 | -22.90288 | -43.75727 | 2025-04-27 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d4153007-0230-3b24-9fea-f856e09c9754 | -22.97573 | -48.44385 | 2025-04-27 03:53:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b278cee-fe92-3642-b844-f90fb9ac2b9c | -22.78647 | -43.75787 | 2025-04-27 03:53:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7e7f2328-772c-3715-8b75-3a708a309bc1 | -22.69726 | -43.3459 | 2025-04-27 03:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00c4e79f-003c-3983-92cc-35c6e7e5302d | -22.67738 | -42.85426 | 2025-04-27 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71741c09-9178-37f5-93ce-6e4ba499f01e | -11.3963 | -52.9477 | 2025-04-27 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4aa252ff-b70b-324c-a0cf-d9673fadcfc2 | -11.3963 | -52.9477 | 2025-04-27 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1b23547a-3955-320b-8464-4976185106fd | -5.22417 | -36.14553 | 2025-04-27 04:10:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a360a11f-47c2-3d63-9d1f-0b0f2417e8d8 | -3.23827 | -43.22403 | 2025-04-27 04:10:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d37269d-1290-3edb-b918-39ff473d7617 | -7.17662 | -44.87135 | 2025-04-27 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e63102c3-7f18-3984-91ad-b59aec1272ac | -5.79798 | -43.62106 | 2025-04-27 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ad5e805-f538-3cf6-8805-1a07d6972a62 | -5.75165 | -46.25887 | 2025-04-27 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b475031-57e7-3999-9fad-2da2fd0bbcc7 | -9.61997 | -37.02748 | 2025-04-27 04:12:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6dc73e7c-9700-3fa7-ae0a-13e9d8794611 | -5.75215 | -46.25697 | 2025-04-27 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7598b6a8-a587-36c1-a1f4-2d87b5b57ec2 | -5.43733 | -43.34633 | 2025-04-27 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68974f6e-c054-3f83-8e12-20fcdf531514 | -5.44064 | -43.34686 | 2025-04-27 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07bb1430-a3fe-3832-bed8-626333e344a7 | -6.28039 | -45.27084 | 2025-04-27 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9298b876-f43a-3434-aabb-d8a7cb9fe214 | -5.43678 | -43.34981 | 2025-04-27 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eec14091-1162-3271-b028-7411a70dff34 | -10.3324 | -37.01688 | 2025-04-27 04:12:00 | NOAA-20 | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49d86faf-45a3-3d56-8e0b-784c246a0599 | -6.84802 | -42.80058 | 2025-04-27 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 10ce17c1-2fb9-3ec8-a716-e230514d475f | -5.4837 | -43.33268 | 2025-04-27 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a926ee5b-c49f-314f-97bf-457bdd2ae220 | -5.87666 | -43.93955 | 2025-04-27 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db684d26-b455-3ac5-8a17-7cf77e65b902 | -10.69695 | -37.04789 | 2025-04-27 04:12:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e53ab2a-af59-3138-bf03-72d3274cb6c2 | -6.25761 | -43.78713 | 2025-04-27 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53fbb7e6-f596-38ae-a647-1cb2b9e06480 | -5.79521 | -43.61705 | 2025-04-27 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5b2a51e-9b34-3c94-8322-c73324cd7d3d | -11.39217 | -52.94063 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 735ca776-f652-3b34-b53a-28603ca0b58f | -11.97029 | -44.15311 | 2025-04-27 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff143882-37e4-3a8a-a8fc-21eaacf84b71 | -11.40125 | -52.94892 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c3597348-706c-3548-a19a-42231de15398 | -11.39672 | -52.94474 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| de3b4f8f-5106-34fd-921b-c3e32e0dc6f5 | -12.24813 | -41.37651 | 2025-04-27 04:14:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf97da7b-a491-36b0-aaab-16c4ee1d0b12 | -16.34925 | -43.69661 | 2025-04-27 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ab9e31b-f586-3022-86df-8a11017dd703 | -11.40694 | -52.94691 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a1f619bf-0a79-3ad2-a5f8-66ba362d4068 | -12.71693 | -41.79581 | 2025-04-27 04:14:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 618dd0f4-36a1-39a4-b362-6faed5aeccd0 | -11.97305 | -44.15717 | 2025-04-27 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7c5696e-d7ae-3f43-878e-4ace23a9422f | -11.39729 | -52.94167 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe5ee361-7cd9-3613-afae-cdf190f8a45e | -11.4024 | -52.94273 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b62172d-e7bf-3c7b-a955-4676cae15bf1 | -11.40579 | -52.95314 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 40b2b877-6cfa-3b7d-a84e-e8f3245cc5fe | -11.39159 | -52.9437 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 36a13949-478f-3b76-8412-6e88e30a8de5 | -12.24395 | -41.38015 | 2025-04-27 04:14:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9e819093-e006-337d-9736-6fc44e8996bc | -11.40637 | -52.95002 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| beadd779-86d0-37bb-8345-a596a8a32f6d | -16.61871 | -46.6501 | 2025-04-27 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2bf48d2-a47f-32e1-a4f2-bf356c5314b8 | -16.68225 | -43.88268 | 2025-04-27 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af8fcd0-21e5-3aeb-b30c-c0fb9794a510 | -13.22749 | -42.00496 | 2025-04-27 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27fc4a50-742b-3ae4-9526-7df1f1503753 | -13.23101 | -42.00534 | 2025-04-27 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54bb2293-5351-3c14-9768-eb3b3f6dca45 | -11.40009 | -52.95518 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 21b0738f-48b6-34cd-ad11-72cb474c03f9 | -11.47118 | -43.80667 | 2025-04-27 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720a1d84-e74b-3c8a-a5e9-d6ac296b89ee | -11.39274 | -52.93756 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9432f70d-6a37-3814-8f0b-82d2df9e85b7 | -11.40067 | -52.95203 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf6b9cf9-7f51-3ac7-b984-84174ff2e261 | -11.9736 | -44.15365 | 2025-04-27 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27587eae-d753-33e2-98d0-c17506f054fa | -11.40183 | -52.9458 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 038de082-e1f0-31cd-85d3-3a2934072450 | -15.6779 | -43.9452 | 2025-04-27 04:14:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9af5518f-6092-3780-ac1e-d3b473ddf84f | -11.39614 | -52.94785 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| af275203-8f37-3275-83ba-e5ab5c9e43d5 | -11.39786 | -52.93861 | 2025-04-27 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9264264c-c330-3573-bac2-7397e63bc570 | -22.78478 | -43.75565 | 2025-04-27 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f1f5c53-bc89-384c-9f1f-954d0ec779ca | -23.59408 | -47.4384 | 2025-04-27 04:17:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f19430f-1dee-3d30-9603-03185252d5b3 | -20.3099 | -45.58614 | 2025-04-27 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e085f830-3c9e-39b2-b384-8adb8eb44d6f | -19.45391 | -45.30603 | 2025-04-27 04:17:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c83779ca-8451-3e8a-ae22-fc2a9b973844 | -22.97385 | -48.44611 | 2025-04-27 04:17:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15f97c1a-898d-3395-935e-cdbc94e24363 | -24.24129 | -50.73976 | 2025-04-27 04:17:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c6cb6d9e-7188-3f57-a254-0c42dd08f050 | -19.85009 | -43.84265 | 2025-04-27 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2f1b7e52-cafa-34ed-9348-3b3cd8765ef2 | -23.63012 | -46.42638 | 2025-04-27 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 20e05f86-0d6e-3b97-bf39-c336a2d6ce80 | -21.19663 | -44.93629 | 2025-04-27 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0fc2c47c-3ecf-3451-b6f4-f633b5938341 | -20.31048 | -45.58244 | 2025-04-27 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f252647d-962d-36ee-91c5-dc51d2b4b6fe | -11.3963 | -52.9477 | 2025-04-27 04:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2da730cf-7575-371b-b806-54470b658a6f | -11.3963 | -52.9477 | 2025-04-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9efd099e-3e6d-325b-be7d-c63bcb232b4f | -11.3963 | -52.9477 | 2025-04-27 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f801d242-4fe6-3609-9b97-9db72cb3ef78 | -11.3963 | -52.9477 | 2025-04-27 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| efb99a53-8ca5-3790-9408-bf884cbd0d82 | -11.3963 | -52.9477 | 2025-04-27 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 2ad8e5fd-8c1b-39f9-ade4-47e578250f53 | 3.70176 | -60.04456 | 2025-04-27 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37bb49d7-13fc-37c6-90b1-e3e693e87915 | 4.35756 | -60.80982 | 2025-04-27 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e920592-134d-32a5-9428-78e239b5ccdd | -5.43735 | -43.34749 | 2025-04-27 05:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37c2ab3e-5116-3470-8180-dc75d1223b58 | 4.35832 | -60.81502 | 2025-04-27 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2229d00-437b-3558-8c3b-6ae7668bdd0d | -6.61211 | -47.33169 | 2025-04-27 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27e10f41-ee5e-3e6d-b3b3-84b70b11e360 | -9.9245 | -59.92801 | 2025-04-27 05:04:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b72889ac-97da-30fa-abe5-b830ea79ddbb | -6.61251 | -47.32874 | 2025-04-27 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87b3faf5-af3a-3174-bf10-78c047ac8e0b | -11.27421 | -52.47071 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1fa7cee-c0f7-3793-9d46-52c8d34a5ae2 | -11.39583 | -52.94275 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 24149798-8f54-35c9-a1ac-ffc009f406de | -11.40135 | -52.9575 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a62c654d-2905-3f6b-a668-61265039437b | -9.22436 | -60.33831 | 2025-04-27 05:04:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c0992112-c4c2-3420-8772-cedf56352f41 | -11.40332 | -52.94384 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 51af18ea-9eea-3bfd-a69c-d83c5ecc06cf | -11.39892 | -52.94787 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dca49fde-8db1-3979-8359-02e6c3a82fcd | -11.39275 | -52.93761 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 647d93bc-ef1f-3969-acb3-6a12e11dbd44 | -11.39957 | -52.94329 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9f3b4a64-a667-3b97-96d3-df84a3a184f3 | -11.27703 | -52.46784 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 358ac9f8-c04c-3b76-8049-33e7c0299038 | -11.27874 | -52.46647 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77bbfc2d-ce9c-38bb-bc72-e76ea7181600 | -11.40266 | -52.94841 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c0b342d3-2a7c-3872-9806-532c0e29ca4c | -11.40706 | -52.94437 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7dacc5f9-68d7-32f7-bbc6-818a53dc7e80 | -11.4064 | -52.94894 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f1297df9-c670-3b04-82b6-c4deeab5d150 | -11.2749 | -52.46592 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80cddf4c-6054-3003-8fdf-73ac7a3d1b2a | -11.40574 | -52.9535 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6aeec816-8091-3d93-b636-62757c213c91 | -11.402 | -52.95297 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a3199a84-483c-343a-ac55-44abacf67e05 | -9.93253 | -59.90271 | 2025-04-27 05:04:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56c4c2fd-570c-3d06-977c-34c0dc6ab3d4 | -11.40023 | -52.9387 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b1cca4a7-ab31-3e45-9c6a-ac19ebc863a3 | -9.9318 | -59.90702 | 2025-04-27 05:04:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f42d789-4f7f-3057-a017-e5239bdfb0e2 | -11.39649 | -52.93816 | 2025-04-27 05:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 64e42179-66aa-390d-82cb-659e18576a06 | -13.0039 | -55.97215 | 2025-04-27 05:06:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dd4afd8-3cbc-3fbf-87c4-020aa13ec563 | -11.3963 | -52.9477 | 2025-04-27 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 42a6f068-a754-3c85-a253-6ed35dccee04 | -11.3963 | -52.9477 | 2025-04-27 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d6aa647a-2571-38d7-a326-a336f12f06a2 | 4.35717 | -60.81346 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b349f223-dc08-37b0-a050-0edb66c5b2d0 | 4.35997 | -60.80936 | 2025-04-27 05:27:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
