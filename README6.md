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
| 7c857dc5-11cb-33dc-b3e6-6a9db0a72746 | -14.13241 | -46.34404 | 2025-07-01 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1c17697-e9c8-302f-8730-e72982d0fd39 | -9.97055 | -48.23242 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d8ee22f-8104-3cb9-b1e7-d44420678f99 | -9.97467 | -48.23936 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 307b5894-7eee-3f30-b8a8-1de4f5e2f1d5 | -12.0205 | -47.7711 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 847f8938-6d31-3b80-95f1-e55727ca5103 | -12.7633 | -44.40375 | 2025-07-01 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50c1f958-bdc3-39ca-96f2-8a1c98a46be6 | -10.05816 | -49.65839 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eaf6846-a985-3051-9e67-c78eca167197 | -14.22071 | -45.50265 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aca77cea-d891-37cd-825c-1a825a6a5dce | -10.54933 | -52.03831 | 2025-07-01 03:55:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d441e27-8131-3c85-9fa3-a618f37e08a5 | -10.12347 | -52.3517 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c9b4d6a7-2cf5-3d55-9e4c-273132de3d20 | -14.44081 | -48.87378 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38db3d7b-f337-3e71-bdfa-9d141872249b | -10.08614 | -52.75031 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b04483d-4b50-32ff-be61-cc586f639937 | -9.68509 | -48.34153 | 2025-07-01 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4032ef4d-b27f-3186-8e90-9c015081ca54 | -10.06493 | -49.6616 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 919e1d5f-b68a-390a-8a57-095b0413df83 | -14.20862 | -45.52304 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1136525-4e82-3c12-af31-e6ecbbb9bcf0 | -11.13989 | -43.33117 | 2025-07-01 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d771b544-867e-30c2-968e-9d3dcbf33bfd | -10.08645 | -52.74823 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 703c36f1-16c4-35c0-8f35-2e5e7af2b7c6 | -11.14361 | -43.33181 | 2025-07-01 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6c5f9d1-c33a-35b5-918b-31220bcde728 | -11.13694 | -43.32598 | 2025-07-01 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 13edc04f-8a28-365e-8fa7-2c4b0e5dbc8b | -11.14144 | -43.32211 | 2025-07-01 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 84e9710a-8e74-31e5-9674-565478f15bb4 | -10.61803 | -51.79347 | 2025-07-01 03:55:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0330e65f-e1b4-3f3e-8507-08b5fbbf7efb | -13.70613 | -45.61897 | 2025-07-01 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d960563-39a6-35ad-a50e-49266fd3dab3 | -10.54767 | -52.03873 | 2025-07-01 03:55:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa9b7a6e-02b8-340f-9ad4-ba3a5e910051 | -15.92411 | -43.51636 | 2025-07-01 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8a8ab9d-9164-3c0f-a721-9b55e91d157f | -13.013 | -44.10065 | 2025-07-01 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 038e71fd-4433-338d-802b-8db39ac8c100 | -10.07141 | -49.65871 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88634ec8-6bac-33d9-9e45-a4d9916a5a6c | -17.09508 | -43.80306 | 2025-07-01 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 374ee208-0d2a-3dbe-84df-04977f5d92dd | -10.27523 | -52.83902 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f298c524-ce4a-3096-9e0d-589d3fcccf1c | -14.44195 | -48.87325 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5763ec4-7a4e-3dba-9305-9ae95419c819 | -11.57368 | -48.14607 | 2025-07-01 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 872f455e-f772-3fca-b4cc-4502603b95d2 | -12.82964 | -47.36959 | 2025-07-01 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 886c0b5e-52c0-3137-bee9-d3d046c98f3b | -9.9793 | -48.24355 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 960cf0bd-422d-31af-bfde-27aa4b92e2c2 | -10.07793 | -52.75541 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8130fe1e-c413-3b68-82fe-d04a5b23b628 | -9.57576 | -49.10477 | 2025-07-01 03:55:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e291526b-635d-3d66-a003-bcdc50991adb | -15.01653 | -47.60178 | 2025-07-01 03:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c60fa26-b03a-3162-938d-b45f1b0424b7 | -18.45631 | -40.0409 | 2025-07-01 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d6274ad-5b64-317d-bc96-892d0b38355e | -14.22137 | -45.49899 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf76e500-ddb8-3a46-8f80-853e38d1aaa3 | -14.44253 | -48.87021 | 2025-07-01 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 564a5b83-2632-3c8d-912e-fc67815f79de | -11.83279 | -47.50468 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86a22b4a-a68e-3f3c-ae69-66bcb3a63947 | -15.71822 | -43.48934 | 2025-07-01 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcb9b9a1-3583-3ab7-9fde-e1fa53f458d5 | -12.62914 | -54.22139 | 2025-07-01 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 725d118d-6c1a-3c8b-b902-9b5cb6c19f61 | -9.57505 | -49.10854 | 2025-07-01 03:55:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71294e9a-793c-3800-8cb7-a751919a50c7 | -15.35071 | -43.06586 | 2025-07-01 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8cbd21e-ee75-33e6-8adc-7fe470c4dcb0 | -13.33913 | -43.37494 | 2025-07-01 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1310b04b-ce1e-3a72-ae2a-1a2f5f2dac4b | -12.57023 | -48.88554 | 2025-07-01 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fc86327-18d7-3d23-a1d2-c801b3b9106b | -12.14587 | -40.48405 | 2025-07-01 03:55:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a549c3a1-ecd0-31b7-bb1f-234a019abdfb | -10.36456 | -47.96901 | 2025-07-01 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6483a3f0-7e5a-34c9-ae06-32630906c8e1 | -11.83758 | -47.5057 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 678d4b7c-6e42-3104-b9ce-f8346a2ef2f6 | -12.62201 | -54.21986 | 2025-07-01 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8832b5d6-3a90-33ea-bbf8-457bb6558b20 | -17.75319 | -42.89635 | 2025-07-01 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 757a78a9-5e18-3b2b-9eec-09ac491047ce | -10.12466 | -52.34576 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a018dc00-f97a-338c-93de-028efbab7e2c | -12.29196 | -48.81272 | 2025-07-01 03:55:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6d63c85-cb31-3b60-a49f-6c22a331af36 | -12.7649 | -44.40145 | 2025-07-01 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5fe93cd-4090-37fa-b1ec-9b99439a6b81 | -14.22475 | -45.50342 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c27b3f6e-9414-3c97-b479-41e0fb254a16 | -10.07273 | -52.7454 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 056a8ed1-7da2-3a7c-a9ad-281ad9cacf70 | -13.54437 | -43.70881 | 2025-07-01 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15c6171a-f07f-3418-bfd2-46f728f2c1f7 | -12.01664 | -47.76468 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be0c8136-e4a0-3c34-8419-c9e68574111f | -10.34226 | -46.49224 | 2025-07-01 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf3b5d41-5a02-3f16-8da9-4b7e9aa01eb7 | -11.14066 | -43.32664 | 2025-07-01 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 66a19db2-6f14-359b-bd0d-6bda96180559 | -9.9799 | -48.2403 | 2025-07-01 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f92780e-c861-384f-85a9-41e3f30619a9 | -10.07063 | -49.66273 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee9505a9-a694-3e1b-82b8-abee3b4fe5e4 | -12.40952 | -40.47262 | 2025-07-01 03:55:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 077bdb24-1109-36c0-8c47-6d01d24fc808 | -14.20592 | -45.51492 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91fce5f3-6b28-3a4d-bdfd-4518519a5cb5 | -9.5702 | -49.10372 | 2025-07-01 03:55:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 94dc890b-7e39-356a-b9f7-614d88617dae | -10.28298 | -52.83568 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a0ad8d1-a033-314b-aa72-3e6f7ca64c8a | -15.07937 | -48.94464 | 2025-07-01 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81599a05-7131-3647-bbc7-37b9bd0d6216 | -9.65705 | -50.74227 | 2025-07-01 03:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4b8827-aade-3664-a077-3bb6864b5021 | -12.29258 | -48.80949 | 2025-07-01 03:55:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28956839-4131-343c-801c-0b9d848c50a1 | -12.28381 | -50.10109 | 2025-07-01 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03966c9d-e014-3731-befa-026ef9462f1d | -10.28342 | -52.83386 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09047369-9afd-35ad-b862-9fa0110ce221 | -10.27655 | -52.83243 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca4eff5e-3274-3467-b33e-7bca7567906b | -18.05801 | -44.49491 | 2025-07-01 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b3bc8c7b-8aaf-33c2-bf38-6c1730bf2ae9 | -10.06956 | -49.66072 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df39c47e-fe55-35b1-9de1-38f00a1f4b39 | -11.77771 | -45.21565 | 2025-07-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef0c0e4-df37-3755-bacd-b3e3c34bd30d | -12.82497 | -47.36862 | 2025-07-01 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f600a319-6bf6-331b-8909-b9529421666b | -9.65748 | -50.74417 | 2025-07-01 03:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d648f91-a3ef-332e-9599-94a3fe38591f | -14.2012 | -45.51784 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af9d0bd7-a9aa-32a0-bd6d-caabec4d63e4 | -9.65606 | -50.74736 | 2025-07-01 03:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 634f248d-f4b6-33ef-b2dc-d2d7160d82ac | -16.4308 | -44.52213 | 2025-07-01 03:55:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9656b425-fc31-3945-b901-fe18e4f71fef | -10.06571 | -49.65757 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| feed241f-4491-3b56-a90f-aa50ae5aed47 | -18.0399 | -39.92451 | 2025-07-01 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41e373e3-350f-3197-9eae-df7c058e4ee1 | -13.00879 | -53.42204 | 2025-07-01 03:55:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bcf4462-f80e-3170-b711-9f3079625d5d | -16.02086 | -44.39621 | 2025-07-01 03:55:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9484140f-d921-3865-a538-57daeb187a94 | -12.29777 | -48.81056 | 2025-07-01 03:55:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43cbda48-7f72-33b6-b3c4-c58285684684 | -10.05922 | -49.66047 | 2025-07-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e51bebe8-ba71-3124-9c73-ff1007732632 | -12.76245 | -44.40871 | 2025-07-01 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57fa0609-fef5-3ef2-a41f-8d8da3cd863b | -10.0738 | -52.74086 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1ab48c9b-b119-3234-93e1-80c0454af1fb | -10.08751 | -52.74363 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2f17aa4-e563-3e13-848e-4feb1138a218 | -11.57425 | -48.14305 | 2025-07-01 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cbc4d71-5175-3a71-b70f-11ffc795185f | -15.9234 | -43.52051 | 2025-07-01 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28402af5-002f-39b3-8bef-5add15071ebc | -17.78144 | -42.81076 | 2025-07-01 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53bef9cf-a0b5-3a43-9f7f-4ea04b311338 | -10.13015 | -52.35317 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12a25dc2-a1e4-3d88-a9aa-9937b96136a6 | -10.08092 | -52.74018 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63f79b9f-3a76-38e2-8b6e-b2d0733acbae | -14.21667 | -45.50187 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41e1cf50-0c05-3dae-8e69-b1b973d74877 | -12.63076 | -54.21393 | 2025-07-01 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b37bfa1-05fa-357a-b869-e3290d89e8f0 | -15.91986 | -43.51987 | 2025-07-01 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bef6442-cb87-3738-b0cf-f309e3df3519 | -10.0793 | -52.74879 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd49b2ca-80cc-3dd4-826b-3f75ce3e0241 | -10.27611 | -52.83427 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 762f8272-87d6-389f-ab3f-4b18e5854134 | -12.80308 | -40.34847 | 2025-07-01 03:55:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f1eeb5eb-a279-35f3-8911-e42da28c5ba8 | -9.6799 | -48.34006 | 2025-07-01 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f3981a3-0476-308a-a27e-e71ba11b81f0 | -10.11797 | -52.34436 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README7.md)
