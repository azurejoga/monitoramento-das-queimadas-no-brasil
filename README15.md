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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc8f3e6b-aa74-3aa0-96de-efc362b254c2 | -14.46131 | -46.5036 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33db0431-e6d4-377c-aafb-347da9f02abf | -12.09031 | -44.84901 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a024ccfe-cfe6-3d70-98fd-c39ca918f2c8 | -11.30093 | -47.41106 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1b37895-88da-3469-8c34-ed9831278544 | -15.13702 | -44.0456 | 2025-09-21 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d0777e2-30ae-34f9-8354-67df3e0a3569 | -12.09243 | -44.81443 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 761c6d65-9450-310c-b989-72875740033e | -12.70407 | -46.83443 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2264055-b4b0-3d50-ae1c-9284e7d10df2 | -14.62754 | -48.26463 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63ec86bf-bbf1-367e-a068-7978740ebb39 | -13.25427 | -47.28059 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f7fe5af-49dd-32e4-bdd0-0bdcb8974914 | -14.78969 | -51.36944 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b160262f-65b7-3013-82cd-fd8cadf6ddf9 | -14.15214 | -44.07445 | 2025-09-21 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d71023f-24f9-3c54-a7be-76b4443844a2 | -17.44234 | -44.80912 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e14c7f6b-d9d1-35f5-b88b-30cdbbdc65bb | -12.14608 | -44.93914 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d628bff9-c3fc-38fd-884e-228fc2e08b69 | -14.25634 | -44.38211 | 2025-09-21 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 692404eb-d620-3bef-9cc2-9052a86517ac | -13.25101 | -44.11075 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14b857ae-e22d-35aa-bb2f-0a99bdf69ca0 | -14.46057 | -46.50787 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dd8425d-6064-301d-ba8b-ecece74bb44d | -16.54885 | -42.35024 | 2025-09-21 04:10:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cd60dc4-86ab-366b-ae46-0074ac816ac9 | -11.62816 | -50.59276 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 619a9e98-e58d-3bb6-946e-cc48967eb93f | -11.27757 | -47.40659 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc9d456-33cd-3f18-ac0e-0279aff441cf | -19.31704 | -43.75671 | 2025-09-21 04:10:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c15ec2d9-aa1a-3de4-bfbf-9bc95b53390d | -14.31739 | -47.79685 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ddd3f407-55d2-3198-b1eb-32b108f9a49e | -12.07077 | -44.8186 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e44d7fe-b09a-3adb-85c5-c8b718da5db6 | -12.70256 | -46.84328 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d793743e-33a7-32f4-ae84-69d628b84380 | -12.33546 | -43.44616 | 2025-09-21 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d4ae817-b4ff-352b-9d26-98335579d8a6 | -14.6184 | -49.76028 | 2025-09-21 04:10:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd639f74-e264-3c1e-ada9-b25ac884a8ef | -12.08006 | -44.80451 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2debd7e2-55ad-385d-9c19-cc75cb7a7cf2 | -12.70924 | -46.84881 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b052ff7-a72b-3222-9624-00321889554b | -16.54547 | -42.34974 | 2025-09-21 04:10:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01a2c2de-38ec-3f29-9153-af1762009d03 | -12.0748 | -44.81535 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f88a026a-702d-3348-bd16-f7f887f37cb3 | -14.47194 | -46.5057 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5c50cf7-2f39-3f54-80ed-4887b1117e30 | -12.116 | -44.84163 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46cafa0d-e8cc-3139-8c98-8b2e9214afaf | -14.44981 | -46.5114 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11431fa3-91ab-3f26-bcdd-7770d6dfad61 | -14.28942 | -47.41595 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f75806a3-02f0-3af6-aac0-60f1ec68d657 | -15.69006 | -46.99215 | 2025-09-21 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31d12ef4-d7c3-379f-a168-5f70b47f4abd | -15.99798 | -47.27533 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe479624-2b26-31ae-8491-4667858d9b83 | -16.60279 | -43.67915 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1819fe69-3854-3451-bfe0-1e786377c83a | -13.62395 | -47.41552 | 2025-09-21 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a88be0f1-2a81-3ba5-92bf-6bf3d645f56b | -11.30313 | -47.51538 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 32702a2e-2a1c-330b-86e2-6c33cb25d316 | -14.45486 | -46.49846 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633033e2-56d6-3cb9-a0d7-3e6f44b16bc7 | -18.29016 | -42.93206 | 2025-09-21 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| daa604cd-616a-3bc3-8091-be7ec67e0eff | -14.74237 | -49.19268 | 2025-09-21 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8681e7f0-8e54-3ce8-9316-43ff39e9db3a | -16.87405 | -43.90433 | 2025-09-21 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 446b46de-0106-3dc7-b311-8e84b23274dc | -13.27234 | -42.52297 | 2025-09-21 04:10:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3be4eb7b-34a8-3a6c-ae5e-ba6229cf0bbe | -14.97877 | -44.41924 | 2025-09-21 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e17032e8-19a9-3b9e-9763-c1173c837144 | -18.46736 | -47.23722 | 2025-09-21 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1392e73b-d9c4-3c0f-ac6c-3d2ac6907864 | -16.87131 | -43.90019 | 2025-09-21 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8000e397-f148-3ef0-89ff-f7883af67079 | -13.36345 | -44.28091 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 359dd7ff-8486-3fac-8b55-f9a79cc17679 | -14.97992 | -44.41205 | 2025-09-21 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725f95d4-b42e-3932-bf59-9d9182bd3ead | -12.70332 | -46.83884 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3180c36-a394-3c4f-8e60-80096b083334 | -12.42102 | -45.10533 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a37ea4fc-3051-34d6-9785-b34e8ae099e6 | -15.11634 | -44.91862 | 2025-09-21 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e79a386d-c821-36c0-a7e5-a601c71b1d6e | -12.70702 | -46.83948 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b688f9b-ee5f-3639-bbaa-386cd6281a27 | -15.75098 | -44.37997 | 2025-09-21 04:10:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08012931-1d8a-38d5-ad74-4f9b359b35e4 | -12.11539 | -44.84543 | 2025-09-21 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78060790-672a-3037-b7e0-ba9166c508d0 | -12.07232 | -44.83053 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b1611d9-60a0-3cfe-98a3-4fa1619a98c4 | -14.45121 | -46.50306 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 516d1b4a-bc11-3695-b4f9-502d0d3f3025 | -11.29398 | -47.40472 | 2025-09-21 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6094a485-fb5b-3600-aaf2-2b6e5c291a8f | -12.70849 | -46.85317 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60a24abf-d2d6-3dbe-a6aa-8ebfbaf8abbc | -13.37283 | -43.77308 | 2025-09-21 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 298a5d7f-4941-3778-97b4-152fd302b055 | -12.47182 | -46.69557 | 2025-09-21 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f489382-255a-3240-b14d-49d4c44e152b | -12.33419 | -44.09772 | 2025-09-21 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04a1c0d-3d9b-3a38-a843-868bcd0dda03 | -13.30725 | -47.28822 | 2025-09-21 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44b77b46-050b-36a4-9076-2710ca1fb1e4 | -14.4712 | -46.51001 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10247e2a-e1aa-3802-aa10-7b661ad7a04d | -12.41974 | -45.11302 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8545de0d-ad4c-33ba-9b47-f98d4659d55a | -12.70775 | -46.85755 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 436ad705-2958-3f9b-b08e-35d8694bce4e | -14.43427 | -46.51662 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 852eaa6a-390f-38a4-8982-572fde7e4ef3 | -15.48418 | -41.91765 | 2025-09-21 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3161f3f-20d9-3275-bd94-276e5b229a77 | -14.79027 | -51.36739 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f233d8b7-df0a-3a8c-be10-432408a0265d | -12.6996 | -46.83826 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eaf8b524-4cae-346f-80a8-c8e7f06dd6b3 | -12.89428 | -46.77596 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa1adcf5-4e58-3020-ac76-18399e9751f0 | -14.78821 | -51.37798 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50263b06-f654-3922-af40-07dd1264372b | -18.46593 | -47.24564 | 2025-09-21 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7d2e6cb-f4e7-3562-aecd-79eb7352d535 | -12.07948 | -44.851 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33e8b7cb-5d44-3a0a-a1ed-fb87d5b078ca | -13.6478 | -45.70256 | 2025-09-21 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b408c582-7562-36ab-aaed-acedbe2af8dc | -15.53366 | -42.17472 | 2025-09-21 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 38a8a982-e327-3b4c-b7d7-cebeb82e98c8 | -13.68279 | -43.90066 | 2025-09-21 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb911f5-15a3-3572-b3c6-4294b23fe634 | -12.96716 | -46.95073 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38a4cd61-1b84-3785-9e05-53feabb52903 | -14.62361 | -48.26406 | 2025-09-21 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11214aab-937a-30d0-858b-5bd75fa7f083 | -12.33809 | -44.09467 | 2025-09-21 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ac413c-293a-3a54-ae9a-85a21be0cd04 | -12.43159 | -45.12667 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7a3391a-2313-3d10-94c0-9adc1e60e221 | -14.44294 | -47.5661 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab726879-09e6-37ca-955f-d0e78ee82519 | -13.22816 | -43.5064 | 2025-09-21 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bdaeada-194e-3b7a-8f5a-8adf1e8949a9 | -11.20754 | -49.62986 | 2025-09-21 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5132b5a-7f68-3c36-8540-c5d9f1761497 | -12.96641 | -46.95523 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02fad9c4-46db-37e8-a601-3ae8df325bb7 | -12.42165 | -45.10152 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6898a030-227f-3a0d-9e40-6451ec324bba | -13.32581 | -43.03479 | 2025-09-21 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a39860f-eef6-38d4-bb09-2c5887ceef64 | -15.97629 | -47.27109 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79aec3e5-a576-3f7a-ae4e-004f51b81b47 | -11.30581 | -47.4998 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8e769306-3a75-3e89-93d3-21bb5bd3a501 | -13.31185 | -47.28399 | 2025-09-21 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dc926d7-226f-3ae5-809d-757a10e6462b | -18.11085 | -44.67149 | 2025-09-21 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20d40f2a-7c94-37e8-83ec-1f15b5bb63eb | -14.74528 | -49.18887 | 2025-09-21 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 711b7019-ad8a-3eed-a5fc-d78fd7a271f2 | -14.45419 | -46.50235 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c80fdf7-6d0d-3024-ab13-f7a8501eede0 | -12.96861 | -46.95365 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe004fea-98cb-3702-9849-f725c572ce6d | -12.07108 | -44.8381 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a30f37e-934e-36df-9b95-1d11b4168766 | -14.27807 | -42.30087 | 2025-09-21 04:10:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03f2d539-d614-397a-81a8-a318671fee7b | -12.72259 | -46.83754 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1a5d491-958c-3a30-ac2a-ca8e65a8fafe | -11.62532 | -50.58126 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5eb190c0-a0e0-3617-8e0d-d2895a48d87f | -13.25044 | -44.11432 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 350eb6cc-4235-3bdd-b873-b468dfc22527 | -12.42255 | -45.11736 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e737bed-2bae-32e8-9f28-bae223e8276c | -15.25017 | -50.22683 | 2025-09-21 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9628ce35-12c4-31b8-a520-ba8f271a942d | -12.72411 | -46.851 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README16.md)
