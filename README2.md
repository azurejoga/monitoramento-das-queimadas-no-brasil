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
| 471611e3-156b-32c0-b91a-80007faccf44 | -12.9068 | -44.658 | 2025-09-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| fa0da663-5cd9-3d47-98c3-fb142ee8e9fb | -22.3457 | -46.7406 | 2025-09-18 00:30:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| bfe1f0e6-f018-3ef6-8ca3-768d51dc24ea | -7.8012 | -48.3825 | 2025-09-18 00:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6e3b40a8-34e2-3ca6-a0c9-fd79add54ce4 | -5.8245 | -45.9129 | 2025-09-18 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 84ed356f-e612-3d6b-962b-8ea56cb5f81c | -11.3871 | -50.8465 | 2025-09-18 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| e387fc98-4b4d-3efd-830f-f88a56175a9a | -7.4109 | -50.0019 | 2025-09-18 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b8952ccb-8b36-30c1-add9-5bf3b110363f | -5.0944 | -43.8252 | 2025-09-18 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6b5e7549-2c35-3283-95de-c60c9c651e0d | -19.5865 | -57.7973 | 2025-09-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 08fe6b9b-9289-3956-9e0e-0de1927beb29 | -18.9873 | -46.9702 | 2025-09-18 00:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| beb05774-35cd-3713-bdaa-863fa6aae089 | -4.6971 | -41.9748 | 2025-09-18 00:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 5b6ada1e-4314-3d1a-8de6-c6d0ef21f689 | -6.558 | -43.597 | 2025-09-18 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 96e6ed2d-540c-34f1-a7d2-640a08557cf4 | -18.5303 | -46.0414 | 2025-09-18 00:30:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c0617c39-774f-3512-881c-aae43c4d5d45 | -18.5505 | -46.0369 | 2025-09-18 00:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| d9b3b5a7-79d6-3cd2-b136-18cff5bb6942 | -22.3457 | -46.7406 | 2025-09-18 00:40:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 896a8ac8-8c2c-331c-b823-44cb9a3d74ea | -5.8245 | -45.9129 | 2025-09-18 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 03990694-a72d-3145-908e-882ea58f9c66 | -17.5325 | -40.2669 | 2025-09-18 00:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| 9501fabb-d2ed-3aa3-9ef4-8df12d112ee9 | -6.6808 | -46.2961 | 2025-09-18 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 98437dec-5262-3374-9522-68c91191fd19 | -11.3871 | -50.8465 | 2025-09-18 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 95a4c587-acc7-33b1-afef-95c5f9f8a854 | -6.6995 | -46.2946 | 2025-09-18 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4d232b98-afdf-34d1-9e35-12c4b2eff232 | -5.8058 | -45.9142 | 2025-09-18 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9e720ccd-b818-3c00-9a33-a0571c9898fe | -6.6993 | -46.3169 | 2025-09-18 00:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| cb1f5cae-bd2f-3371-a9e5-9f789e009968 | -4.6971 | -41.9748 | 2025-09-18 00:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| db8a4680-e202-3d99-8bc1-ed9ef1f88220 | -17.0947 | -49.3991 | 2025-09-18 00:40:00 | GOES-19 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| aaec0a82-6aa1-393c-87c7-934b67102a91 | -19.5869 | -57.7765 | 2025-09-18 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| beaf4875-b860-342c-8a64-342ffed19e2b | -17.5123 | -40.2724 | 2025-09-18 00:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 352.7 |
| d53c6bcf-9d64-3f84-9c6f-216dd1a8ba37 | -17.513 | -40.2464 | 2025-09-18 00:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| 36623ace-78bf-3371-b4d7-11deefcb955f | -17.5115 | -40.2983 | 2025-09-18 00:40:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 101.2 |
| 2da28a5a-34df-3294-a253-432dc7d9563f | -22.34687 | -46.76208 | 2025-09-18 00:48:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 69e895f3-8d15-39c9-a173-96596c79af7d | -23.0234 | -48.00267 | 2025-09-18 00:48:00 | TERRA_M-M | CONCHAS | SÃO PAULO | Brasil | 3512308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 5f94df3e-40ac-3ee2-9c42-a430c38d504a | -22.68021 | -47.50914 | 2025-09-18 00:48:00 | TERRA_M-M | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 3c2e2ccc-107b-39da-af75-52f2240843b5 | -22.33698 | -46.76403 | 2025-09-18 00:48:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 94a58c66-977a-3dfd-b362-b1c4ed88146d | -22.68111 | -47.45205 | 2025-09-18 00:48:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 85367283-99c3-3dec-b069-4846f6cbfb46 | -22.32365 | -46.74759 | 2025-09-18 00:48:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 81f24df9-c8e4-34d8-858d-f5d9b9c99ce1 | -22.81664 | -47.4492 | 2025-09-18 00:48:00 | TERRA_M-M | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 5e243d62-b714-333c-bbfe-9a34af7c91ff | -23.59526 | -49.7795 | 2025-09-18 00:48:00 | TERRA_M-M | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| f392392e-9619-3775-aab6-f91399935de7 | -22.6923 | -47.46132 | 2025-09-18 00:48:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9866d021-de1b-3065-b129-a40037350142 | -22.70253 | -47.52767 | 2025-09-18 00:48:00 | TERRA_M-M | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| e72f4f92-6137-36f7-b80a-1e8076a9a0d3 | -22.74316 | -47.44596 | 2025-09-18 00:48:00 | TERRA_M-M | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 569e2d96-bf46-37ac-8455-34f761fa5eb2 | -22.335 | -46.75192 | 2025-09-18 00:48:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.1 |
| 322c5d42-58aa-3168-987f-b3d523c49173 | -22.96455 | -51.58887 | 2025-09-18 00:48:00 | TERRA_M-M | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 68af1c54-f653-382c-acb9-1d046a390b3b | -23.02911 | -47.04171 | 2025-09-18 00:48:00 | TERRA_M-M | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 4938e6dc-4b84-3127-9c6d-e8a795445825 | -22.3449 | -46.74993 | 2025-09-18 00:48:00 | TERRA_M-M | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| ba86cf4b-fdab-3cf9-8f7a-b13b5e1f6c7e | -23.02728 | -47.03028 | 2025-09-18 00:48:00 | TERRA_M-M | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 09c2a905-e669-3c31-9df7-f97d460265af | -22.68283 | -47.46315 | 2025-09-18 00:48:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 713450d6-ddd2-395e-b2e2-d9d8459e4684 | -22.65421 | -46.82197 | 2025-09-18 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 94b9cb51-c3b4-3598-8c4a-178b546f8d8a | -22.65886 | -46.02104 | 2025-09-18 00:48:00 | TERRA_M-M | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 9e20896f-3ff6-3d7f-9344-e1cc183012c5 | -23.20153 | -49.98727 | 2025-09-18 00:48:00 | TERRA_M-M | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d3c635cf-ab5e-3de4-85bc-4497ed9ed389 | -22.47197 | -49.01016 | 2025-09-18 00:48:00 | TERRA_M-M | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 727f8576-4d18-37a1-aa41-f7bcef94e2f5 | -23.13565 | -49.64579 | 2025-09-18 00:48:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| a77d3227-a61c-30cb-a7f0-f47f97eda680 | -13.3042 | -61.7887 | 2025-09-18 00:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 09eb2471-d794-3043-af42-0e41c20b4a9d | -5.8245 | -45.9129 | 2025-09-18 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e6bfaf33-3573-307b-95bf-9b339437ea7e | -22.3457 | -46.7406 | 2025-09-18 00:50:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 6d01ed6b-dd81-3342-8e9a-4ea5f45c03b3 | -19.5869 | -57.7765 | 2025-09-18 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.7 |
| a63c299c-fdd4-3f0f-8a00-72b71fdeaad0 | -6.6993 | -46.3169 | 2025-09-18 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9e534ebe-d47f-34a2-8adf-24384831b5bb | -15.3207 | -59.4086 | 2025-09-18 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c4edc9a9-fb1f-3e80-8f80-76c91a5907f9 | -6.6995 | -46.2946 | 2025-09-18 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| f5e9bf2d-517d-357c-8e33-15af96c1ed3e | -4.6971 | -41.9748 | 2025-09-18 00:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| a1b1cccf-4a33-3a55-9628-4976bdbf374c | -13.2852 | -61.7899 | 2025-09-18 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a54001ab-c61a-3d17-91d6-879883cd1c9e | -6.6808 | -46.2961 | 2025-09-18 00:50:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3ef7373e-981d-3a68-b4ab-b04b9488f20c | -13.08759 | -42.14179 | 2025-09-18 00:50:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 152e38c8-afc6-3ec5-a697-f6bb93ab1ebe | -15.04389 | -55.27475 | 2025-09-18 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4a55dcca-d816-30af-8540-0153580f8699 | -12.82034 | -52.98813 | 2025-09-18 00:50:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 051b3112-2fba-3e60-9ab1-943403cb749e | -19.04032 | -48.26852 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 31891d06-f882-3b33-9052-0d1c8eb55118 | -15.91033 | -43.87022 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 7395f2b4-8121-3b0e-bbda-1f3e5cef2834 | -12.72019 | -47.96487 | 2025-09-18 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3d1d42f9-eed7-3e23-8d1f-c380dd23e3c7 | -13.0316 | -47.9482 | 2025-09-18 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1aa4bc68-9117-3102-9100-acbb6635f8d3 | -19.0482 | -48.25599 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| dfdf437a-543d-3d7e-b05b-513e0f3ba46e | -14.96044 | -46.25404 | 2025-09-18 00:50:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3cde05c8-f029-3b44-b4dc-264ddaece44b | -17.68411 | -44.14968 | 2025-09-18 00:50:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d2ab0e5b-841e-3304-b23d-e5956e98972e | -17.49988 | -46.74672 | 2025-09-18 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1003bf6c-0c2a-3ebd-b587-ed6d4e82bdbb | -17.08675 | -49.3973 | 2025-09-18 00:50:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49ed5313-5b36-3e4a-9554-ae52ecb4f469 | -17.17817 | -45.90465 | 2025-09-18 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7cdb6835-ec33-3214-a0d6-6e897e210256 | -13.71243 | -49.856 | 2025-09-18 00:50:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 13e8ba11-9d7f-342a-8dfa-3019d5161f81 | -17.18091 | -45.92132 | 2025-09-18 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 933f7f2e-f0e0-33cb-a18a-68c935bfb4ee | -19.56879 | -57.77648 | 2025-09-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.9 |
| 765fe3d4-9973-32e5-a8d1-bf0dd8d16236 | -17.59645 | -44.17653 | 2025-09-18 00:50:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 98d4c70e-1275-3847-90e7-edefa456b50f | -12.4469 | -49.73957 | 2025-09-18 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6d044539-f695-3453-9b83-27dd716db527 | -21.57541 | -51.85727 | 2025-09-18 00:50:00 | TERRA_M-M | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 84c36d9b-9296-3325-9ad2-375901e82190 | -12.39928 | -51.42645 | 2025-09-18 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 07458a49-ab6c-38b9-a1cc-3b195d72030d | -18.98111 | -46.96995 | 2025-09-18 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ddc89b22-1f25-3d9d-b4d3-24b5461edd7a | -19.59498 | -57.77351 | 2025-09-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 89a487a4-0f99-3f1f-b690-b145ea3f4926 | -21.30665 | -48.54851 | 2025-09-18 00:50:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2f9165b1-25bd-33cb-bd5c-9d703f0bcca8 | -12.90319 | -44.67434 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| e84a1b42-3eb0-389d-8cb5-642a77f9efa7 | -16.7269 | -48.48944 | 2025-09-18 00:50:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a164c547-2662-3826-b3a4-15849b064c55 | -20.3458 | -48.79738 | 2025-09-18 00:50:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 76a565f8-1fad-3693-9a9b-62d201a6a513 | -21.10401 | -49.11528 | 2025-09-18 00:50:00 | TERRA_M-M | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 15f46dc3-7515-3cdf-bd21-c97fd1fc39ac | -12.44375 | -49.74641 | 2025-09-18 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 44950a55-a0f7-3a40-954f-d1291efc2cf2 | -10.64793 | -42.31858 | 2025-09-18 00:50:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 2b4c70df-feb5-31a2-8016-4489f67d9b6d | -20.88437 | -48.44588 | 2025-09-18 00:50:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 81f2bad8-852a-3249-83f0-7d2f59fcefbf | -12.39797 | -51.41721 | 2025-09-18 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 64a4c6d4-4fde-3a92-927f-ee5c038103e6 | -19.05148 | -48.24903 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 138a192d-5f18-3531-ad6f-3e2d4f063844 | -17.06176 | -48.13554 | 2025-09-18 00:50:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 410a5afa-f14e-3f24-93c0-f92660335a45 | -15.91959 | -43.88727 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 27.5 |
| ba889bcb-a28d-3c88-89ce-2ffa18ebfd54 | -12.43419 | -49.74799 | 2025-09-18 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8c2d9bd1-f602-3313-9fec-76e3268f187a | -12.10031 | -44.82309 | 2025-09-18 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a1d370b1-ede6-3493-85a4-beb77f0bcfed | -15.91467 | -43.89507 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 121a150e-9cab-315a-977a-86620718fcee | -17.49758 | -46.7324 | 2025-09-18 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6ae0eb79-d36a-3f2a-86a7-504ce1a1afdd | -15.88772 | -43.46955 | 2025-09-18 00:50:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| b0047d6c-e9b8-39d5-98c8-1c55e8241c2a | -17.18869 | -45.9131 | 2025-09-18 00:50:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9bf0fdd8-c981-3243-bb26-9cb3713f8354 | -15.04267 | -55.26857 | 2025-09-18 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |


[Clique aqui para ver as próximas entradas](README3.md)
