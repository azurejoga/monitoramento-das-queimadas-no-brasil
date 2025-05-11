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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47f81bdd-21a1-3d17-913e-846c92fa5e86 | -16.49229 | -43.13752 | 2025-05-11 04:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a864955e-2553-38cd-a7ef-397db405f91e | -14.21737 | -54.5743 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd24790-4ce2-312d-a739-359b8d46c8b2 | -14.87202 | -51.98231 | 2025-05-11 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 030cb35c-7b79-3243-bc21-f0dbdabf1bbb | -11.9172 | -54.4096 | 2025-05-11 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fb212e5-7892-38ec-97e9-8725d7014223 | -13.04386 | -53.7248 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8037a3c5-f3d1-30b4-8f72-fa685b6605df | -12.3307 | -45.69527 | 2025-05-11 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8a4cb6b4-981b-3ab5-907d-f78e7c239bf3 | -15.56982 | -47.8543 | 2025-05-11 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88f8f9fa-3978-3be5-bda0-01d53d621dd1 | -14.21624 | -54.5814 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5de1241-58f6-3ebc-ae84-558f94621f9f | -13.4916 | -52.9785 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46750d6f-bafe-383f-b3de-af05cb34cde5 | -12.17248 | -54.23457 | 2025-05-11 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 980f45d1-6d06-3577-a807-34a4ff005144 | -14.65425 | -45.13602 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a209898d-ddeb-391f-b16b-0047958a1427 | -11.62462 | -54.93638 | 2025-05-11 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77b5a591-eb49-33bd-9145-84f3bd3782df | -13.05105 | -53.72233 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a70b6781-c557-3157-9c8a-5f0c72b275e3 | -11.39704 | -52.94313 | 2025-05-11 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f4e2f2-1cc2-3ae1-a3cf-a034c986535f | -13.0516 | -53.71879 | 2025-05-11 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fb79554-ae8e-3acc-9377-efc493634ba7 | -12.65077 | -54.06682 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70c5a1f9-6514-3ff8-b3e4-a1afe65b382e | -11.56245 | -47.87037 | 2025-05-11 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dcc79b6-f6dc-32ed-b21a-1caee5cdf197 | -12.32501 | -45.70026 | 2025-05-11 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 776875a5-7b81-30d6-a6ec-c27f661edba1 | -14.86851 | -51.98177 | 2025-05-11 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d819772a-4790-3051-8783-533d8a840e4f | -11.40315 | -52.94773 | 2025-05-11 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba413e30-b088-3ed3-8f46-3671cae8d521 | -13.37444 | -54.25705 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6f66362-7444-3c0a-9209-a51bdda036d9 | -12.76355 | -47.9909 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5988c6b-ed92-38ff-be8b-640825510dba | -14.6501 | -45.12506 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6107727e-f8d8-354e-a118-3782b46c575d | -13.48264 | -52.96959 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff27e641-9272-384f-8451-4dd73ed1f4d8 | -13.47761 | -52.98001 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4dcd0a10-e5e8-3619-b06e-45ffaacaf3e0 | -13.47592 | -52.96852 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b259126e-33cd-3bf4-8fe7-0d4740a558f6 | -13.98264 | -56.80747 | 2025-05-11 04:51:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6723e537-8852-36f6-93a5-7286cbbfaeb4 | -11.91663 | -54.41314 | 2025-05-11 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32072684-64e1-3e7d-b628-69844c189e34 | -13.48152 | -52.9769 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e48bb19e-aa0f-323d-b48e-8635cb26d096 | -14.64851 | -45.13878 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b721942-d164-3ff2-918e-fddef647580c | -14.31428 | -54.64901 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a09177a-9da0-394c-b36a-6c75530c524f | -14.6497 | -45.12849 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26bcd5ae-3e8f-39a3-8e72-cf8704bfbd43 | -13.4888 | -52.97431 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b63a4183-ad28-3f1b-8df5-d2fd26e74327 | -12.65021 | -54.07035 | 2025-05-11 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2969dca7-29e7-32ef-aa9f-21e198f63b36 | -11.60852 | -48.0055 | 2025-05-11 04:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62e61404-d564-3511-89c5-2428e40b472b | -13.47817 | -52.97636 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e5563283-8e58-3375-bc75-e88365aa7091 | -11.39371 | -52.9426 | 2025-05-11 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4431497f-8ccb-3aee-ab18-37887efb4a16 | -15.07681 | -48.9433 | 2025-05-11 04:51:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f552c15-8832-3351-8f03-952369365d65 | -12.10649 | -47.9819 | 2025-05-11 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51616306-c27e-322f-a734-4cdce848966a | -11.62404 | -54.93999 | 2025-05-11 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d285d16-a2ab-3e06-9cf7-202fea9f202c | -12.58818 | -48.33458 | 2025-05-11 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64988f92-103d-3d71-9650-fce6717a2d7e | -14.6715 | -45.1276 | 2025-05-11 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8694269-7666-391b-b5d7-f77a0af9a997 | -13.48824 | -52.97797 | 2025-05-11 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c500e21-857e-3dee-9ed9-71a0a19f053e | -16.67936 | -43.88764 | 2025-05-11 04:51:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6b635f3-867a-3f4d-b39d-247e01dfac18 | -12.32998 | -45.70102 | 2025-05-11 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 85332c7b-dbda-3357-bd99-1e2a9a56d140 | -20.15697 | -46.83395 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e1895ff-58c9-39d4-a905-984d2f152b2b | -20.17713 | -46.8125 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 88895b0e-cb76-304f-8d80-b8f766f6234f | -20.1768 | -46.81571 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e5fcbad-4a28-384e-a784-dd30f2c49464 | -20.19256 | -46.71299 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9366e8fc-b672-3d20-a12e-7e301423dcfc | -20.16215 | -46.83412 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdf0a5f9-89c4-3e9a-91cd-230f70d698e1 | -20.1712 | -46.81965 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5915a2b-868c-3669-a904-b5d9ae5f196d | -20.17439 | -46.81734 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 943b12a5-cd84-3acc-8a1e-d268446cc91b | -24.2435 | -50.73767 | 2025-05-11 04:53:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1fce732-f1eb-3182-bb8f-06c1804c71bf | -21.71857 | -55.37327 | 2025-05-11 04:53:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 70d92f6e-2d55-35bd-beba-98cb719f2457 | -20.4789 | -53.67445 | 2025-05-11 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1bf04dd-afce-3670-92ce-4d04668064b2 | -25.19212 | -49.32684 | 2025-05-11 04:53:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b342f6e8-4308-3219-8200-75abc0fc8621 | -20.17474 | -46.81408 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 183fe98e-59d4-3862-8e6a-a2d61858c96a | -20.12097 | -46.87934 | 2025-05-11 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fc9aad8-94ac-3000-be65-4bc4ae42bb28 | -20.12063 | -46.88256 | 2025-05-11 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61c53f0e-c83f-3f58-99ce-1b0eae448f8f | -25.19734 | -49.32194 | 2025-05-11 04:53:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 944f0ff2-b722-361f-b359-9735b7dc8234 | -20.17646 | -46.81898 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2756d081-1425-3b8a-9f57-c25e84ce8d39 | -20.17403 | -46.82059 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 12da0052-570c-350b-a755-fb6d6d3e7645 | -20.16182 | -46.8371 | 2025-05-11 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bbfe51b-4016-30ea-a28d-84047bd6986b | -13.48059 | -52.97092 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b172f15b-a2d0-3ecc-a9da-319b302ec72e | -13.49002 | -52.97628 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b4c98f02-1e4e-3191-9f8b-47ca370cce4a | -13.48215 | -52.98287 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7bc78240-5742-34d0-89ea-4772e132d028 | -13.0464 | -53.7252 | 2025-05-11 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e852e79b-b877-3c29-b8f9-cfcf96ba97d5 | -13.05386 | -53.71952 | 2025-05-11 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe0135dc-f254-3f90-9c20-d8cc1eb4b73d | -13.4837 | -52.96807 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9fac5a15-69d0-3598-925e-18c31a492d2e | -13.48694 | -52.97931 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 774dcc02-d713-3db5-aae4-715d3a96a778 | -13.05319 | -53.72575 | 2025-05-11 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbb6be21-e040-33fd-b9b6-8705155ee3af | -13.48292 | -52.97548 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 76ab8558-df99-301b-8c83-ca6a2497a5cb | -13.47985 | -52.97842 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 745d05a5-7be4-3a73-9929-a3fcdd9f25a9 | -13.04707 | -53.71896 | 2025-05-11 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7366400-08e3-3e86-a1c5-488340ab7581 | -13.48769 | -52.9717 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b99504c-7308-31bc-81c8-a21252387d97 | -13.4766 | -52.96726 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ea72238-0955-3070-8919-9ffdbff07bf3 | -12.17352 | -54.23516 | 2025-05-11 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f31cd902-9b02-3434-b3fa-17b11e519c6b | -13.47583 | -52.97466 | 2025-05-11 05:44:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f4eb444-96b5-3fc1-8b85-53b0d67eca74 | -13.48322 | -52.967 | 2025-05-11 06:10:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 33344016-6075-3204-8838-6f09ffc9a740 | -13.48184 | -52.97658 | 2025-05-11 06:10:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 12f224db-51be-37ff-b32f-f5c77ea885be | -13.47416 | -52.96566 | 2025-05-11 06:10:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a1f50c1a-f980-3e49-860f-0e0c2ef7c5ae | -13.47279 | -52.97523 | 2025-05-11 06:10:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0784e332-2b73-3b12-84e4-c7c985fdc43b | -14.87248 | -51.98002 | 2025-05-11 06:10:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 39ce8251-301d-317b-8e3a-cd9c0a2413fa | -13.04072 | -53.71875 | 2025-05-11 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ad9a2df9-7b4d-3f44-8da7-59f3b91fed3c | -13.04957 | -53.72008 | 2025-05-11 06:10:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5a0a6895-7bba-335f-a909-9c0c214db26e | -14.661 | -45.1227 | 2025-05-11 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ca6c0627-2e0b-38bf-9364-cda4db4407ae | -14.6805 | -45.1191 | 2025-05-11 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 46eb79d7-a50c-3cb4-8bbc-c520accb0b7b | -14.661 | -45.1227 | 2025-05-11 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| a18814e8-d0bd-3a28-97ba-f70a25b8a2fd | -14.661 | -45.1227 | 2025-05-11 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 8e278227-f06c-36f3-b858-982bb4e567a7 | -14.6805 | -45.1191 | 2025-05-11 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e7f72808-54b1-39e5-b6ef-37412093b934 | -14.6604 | -45.1461 | 2025-05-11 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| c4a4963c-613c-34b0-badb-56161a742dd3 | -14.661 | -45.1227 | 2025-05-11 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| af606546-eb71-3d03-bfd2-d0009542fbbb | -14.661 | -45.1227 | 2025-05-11 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| aa02b951-e4d0-361f-a31c-9ebddbbe1227 | -14.6604 | -45.1461 | 2025-05-11 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| cb045fea-3cab-37f7-a9f7-6fde4bb51169 | -14.661 | -45.1227 | 2025-05-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 6f4e25a5-8100-3b24-8e53-e15e8604b3ef | -14.6414 | -45.1263 | 2025-05-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 26626f6e-b4bd-3ced-9613-d3a6f2accc10 | -14.6805 | -45.1191 | 2025-05-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7fd6af39-0ade-31fb-8fa7-34340a0f4646 | -10.7715 | -46.3001 | 2025-05-11 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 3983bc69-5953-32de-8f09-e91697bc0e80 | -14.6414 | -45.1263 | 2025-05-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ca14cd9d-3b1a-337c-b0f6-5be0a0f7a65d | -14.661 | -45.1227 | 2025-05-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |


[Clique aqui para ver as próximas entradas](README7.md)
