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
| 579f2127-9282-3a2d-9e2f-5d2b741f2f86 | -10.57969 | -49.1244 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d3ae071f-1681-3735-b0fb-97d6e20036ea | -8.37876 | -43.95082 | 2025-07-09 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5f5218-438f-305c-af6d-b97caa8916b3 | -11.10788 | -48.87249 | 2025-07-09 03:55:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1aa77953-d405-3623-b673-4d0366240b64 | -8.50976 | -43.29391 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 73da2d40-1ede-3452-9753-bc67ceea8d77 | -9.79193 | -47.74955 | 2025-07-09 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a518484-0b40-36e2-973a-c3ed19d7914c | -11.45148 | -45.11345 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 135ed95f-af9e-3f66-895c-9b3ab33c5d66 | -12.50193 | -43.15189 | 2025-07-09 03:55:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49451e2d-d11f-3e72-8f70-f2beea8fbc10 | -11.41904 | -45.11192 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| df01ff66-3cf7-3c66-a68c-2fcebf4b14cd | -6.67737 | -46.30018 | 2025-07-09 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6e82fce-5d94-33e7-9e7c-a5296ed869c9 | -11.43763 | -45.12687 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bd8169a4-3df2-37cf-9232-49139da038e0 | -6.85068 | -44.06969 | 2025-07-09 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 900bbc04-75f3-362f-b96a-26a0b38f73dc | -11.45558 | -45.11419 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8ede8fd-e049-30fe-bf69-5105cb790844 | -7.23693 | -43.07127 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d8c14813-dc6e-331b-99cc-2c13c4e06e8d | -10.64819 | -44.48684 | 2025-07-09 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f0f9f1e-dd91-317c-b641-51b12c4c0c3e | -8.5078 | -43.29116 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 19cb9b47-0d55-33ec-9e6e-c2fdc4be6f96 | -11.43267 | -45.10658 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cd1cf2b8-15d6-3f0b-a890-a3821bfb5e48 | -10.63583 | -49.46146 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d120e8b1-a935-3435-b966-e50ade6290d7 | -8.22283 | -44.93465 | 2025-07-09 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa5930a1-a6f1-305b-9ca2-f919cb1a125b | -12.98326 | -44.88307 | 2025-07-09 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc1c1558-b070-3dcc-9d73-a2f3a86e14ef | -7.57175 | -47.06544 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6945e9d-908d-3da6-bcc6-b84f9fe00797 | -8.50592 | -43.29327 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8546b19b-3081-39d5-8fe4-b6da94174743 | -6.16798 | -48.05508 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 43cd8a41-6080-3ab3-acfb-1c2ec032a690 | -11.45626 | -45.11044 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b7a38c3-e81a-39e5-9e6a-72509b8f41b0 | -11.43072 | -45.11786 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d90e123-a508-3a92-a794-e8a507e872c0 | -7.66998 | -44.36883 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d402769-0a72-374c-8e9f-4b7de5c0ca7f | -9.28178 | -44.84098 | 2025-07-09 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d4ad1f-108d-38a0-b43b-15d2d5a3ba11 | -5.96411 | -44.18158 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ad7391b-3598-3c78-9953-b204a0d717b5 | -7.23164 | -43.068 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8b56902-9b7b-3b8c-94dc-924c0aa807da | -11.44024 | -45.11182 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0442e806-cd1a-3c97-8334-d1e0113a4804 | -5.96346 | -44.18554 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd493c8c-b46f-3984-b203-dc234d652736 | -11.67831 | -43.78532 | 2025-07-09 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f4afe52-b3c6-362c-b8a4-4db18cd4d4cd | -11.45795 | -45.10725 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a099776e-720c-3108-a3e6-769f612df027 | -11.46446 | -45.11195 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 38e250ea-8ae9-3e3f-af13-507310110a08 | -11.41559 | -45.10742 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4d14bc5-0ef4-3239-8a1c-bc9754c68372 | -11.90741 | -49.19714 | 2025-07-09 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 219d6f8f-ec6d-3213-83ce-8df3571d934b | -7.03401 | -43.48902 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da7a0e10-8610-35be-8124-e91cde865f60 | -5.95924 | -44.18484 | 2025-07-09 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92ed7e03-bf1d-35f8-9bc1-ffdadced136b | -9.4067 | -48.44687 | 2025-07-09 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37dfccd1-ea15-38f2-bb1d-78665b2de8e2 | -11.45666 | -45.11478 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c207bcf2-888f-3d80-a19a-b69688d84f25 | -6.16745 | -48.05324 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| df416aac-0381-35f7-ad6e-d28c92b2273f | -11.42315 | -45.11264 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 51503c01-5f02-3a75-b750-3214ea8976ed | -11.44715 | -45.12082 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 18e96a0c-8b3c-3753-bb56-80dc8f6fd6c5 | -7.02949 | -43.49172 | 2025-07-09 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 802dbd3f-27e9-3299-8eee-7ac97e388f14 | -7.81191 | -46.5728 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01b12e05-2fd8-3ed3-8afa-6cad75b95cea | -8.51278 | -43.29933 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 21d1a781-012d-36eb-ae7c-5e2e58d49453 | -7.23388 | -43.06585 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 75307075-b3e8-3fd4-8571-28c0fc7cec72 | -8.50894 | -43.29869 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.1 |
| 66b87642-1494-3d39-b208-937ff2b926e7 | -6.62164 | -43.35284 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 15bf312d-cb9c-3d28-9d25-fca732c0999e | -7.67656 | -44.36555 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 937670e3-1acc-3d10-b8cc-b3a58ede03a2 | -9.22134 | -48.59473 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2decfb1-83c1-3cab-858b-e4e17d09bdd3 | -6.24005 | -43.36687 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb3bf1d0-020c-3e9d-9320-f4846b12e25f | -5.72155 | -43.79113 | 2025-07-09 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cb75bf0-7053-30bc-8888-197836d33724 | -9.28383 | -40.51889 | 2025-07-09 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af81bd3b-571c-3f84-9499-32e59aecb2e6 | -7.23774 | -43.06648 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 73ef918b-6551-38f6-88ff-e0b6d9fbba5a | -6.57906 | -38.10531 | 2025-07-09 03:55:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| af611aa8-f702-343a-af00-73961e2eb9ef | -11.47363 | -47.92573 | 2025-07-09 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc37b7a3-a4cd-3e1c-9d9b-fcbb8d497a94 | -13.32158 | -42.28643 | 2025-07-09 03:55:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4660d813-b9f2-3b03-b77e-993606fc3de0 | -6.98099 | -47.08696 | 2025-07-09 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0dafdae-8ba9-3f2e-a204-c70a454fdec5 | -5.7846 | -43.61575 | 2025-07-09 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06c4b1b7-9bd7-38e3-a80e-0afc8383d7ef | -8.22965 | -46.96507 | 2025-07-09 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 715c1fa2-8e55-3603-a2bf-c94f648e053c | -8.50248 | -43.27555 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28003795-6439-3c6f-8387-2ebcaf582068 | -6.86486 | -42.78864 | 2025-07-09 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 882554ec-9222-3e3e-93d7-ddadf1ce329f | -9.79062 | -47.75082 | 2025-07-09 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b35adc-627b-3cd5-91a8-4473547bbaca | -8.50917 | -43.27425 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 45f2246d-0d9e-3228-95cf-361e26b83f64 | -11.44758 | -45.09379 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67290c5a-fdaf-31e7-9106-233c6da4fde3 | -12.39223 | -40.30095 | 2025-07-09 03:55:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 2ecbd010-cfc8-357c-a8ac-84aaad5f6317 | -7.67787 | -44.35801 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e476b6c-b381-396d-81f4-1c3982b5e621 | -11.90207 | -49.19611 | 2025-07-09 03:55:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f87dfa9-f72c-3f63-b5aa-149e340686ff | -11.43483 | -45.1186 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bc284500-ed5d-393f-a2be-a0fc3767bcd8 | -6.17291 | -48.05428 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1aba2d4d-5f8d-3413-804f-8a5bd09a1899 | -6.56598 | -48.2426 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68998c49-557d-3b53-893d-3d98dbe1ece0 | -12.05734 | -43.5096 | 2025-07-09 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ee1971c-2b31-321b-8ec6-63ec32934ee7 | -6.66453 | -43.90107 | 2025-07-09 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749e8ab6-9c35-3b19-8d62-8968e32c849d | -9.47762 | -48.68008 | 2025-07-09 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64f35ecd-82bf-399f-b50c-ded1545bedf0 | -7.23628 | -43.06382 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6874a069-2912-310c-a988-9b0572e8b801 | -7.0873 | -49.16298 | 2025-07-09 03:55:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58038229-08c6-3d6c-adae-323b9f7fd1d3 | -7.24013 | -43.06446 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76091383-01e5-32fa-b35c-a2e9e0683f68 | -11.43548 | -45.11484 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c03a67ac-d303-3f87-a5a9-d17a7a79753d | -7.67174 | -44.36869 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c90e8328-5fa8-30f3-a48a-802be926b998 | -7.66404 | -44.3637 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb96d522-13da-3f1c-8b93-8e09d3df740e | -10.58037 | -49.12076 | 2025-07-09 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1b3ec3ed-9fcd-3598-abb1-cb6cfc7c0e14 | -12.47134 | -46.90914 | 2025-07-09 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c35408c-2f4c-332e-9aff-4f6fe0e7c071 | -11.45693 | -45.10669 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bcc5d2e-dfa8-3aa3-bb7a-dba389b87f20 | -11.45215 | -45.1097 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19e18907-6fa8-37f2-bfaa-adc2e118f1b0 | -10.46324 | -47.94306 | 2025-07-09 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73cb111c-f4dc-3d77-b960-d0cdd946383e | -12.46995 | -44.49501 | 2025-07-09 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd6ef42e-b46d-3241-b847-6a99cb6c2ac4 | -6.56618 | -48.24222 | 2025-07-09 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6358a911-e7d6-3176-a7dd-81e71f6ae4a7 | -8.83225 | -48.0653 | 2025-07-09 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6e760bc-c9c7-35ef-941d-3a496733be46 | -6.74587 | -43.15965 | 2025-07-09 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 906f37ac-bb10-366f-a102-5594f3edac57 | -11.4573 | -45.11101 | 2025-07-09 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a26ea93b-5310-33d3-89cb-23c4efff1199 | -7.23936 | -43.06926 | 2025-07-09 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| dc38eab0-8180-3743-a175-00cab56a15b8 | -8.51359 | -43.29455 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 80f3a957-9c2c-351e-a5dd-a79fea1e96d0 | -7.67239 | -44.36494 | 2025-07-09 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c90b36f-ce26-3156-a91f-d08fe2240a0d | -8.50709 | -43.27147 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 85e7f06d-5d53-316f-8408-083fbab1c49a | -6.17463 | -48.0494 | 2025-07-09 03:55:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| c7304ef1-09d6-37be-81f2-78dcb41637d7 | -11.10723 | -48.87588 | 2025-07-09 03:55:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9012bf7f-d24e-39c5-b822-e1effb32028a | -8.51139 | -43.28437 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 20cca182-d109-37bf-ab77-6dabad17dcc0 | -6.96007 | -42.70821 | 2025-07-09 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e69e225b-0731-312c-8065-068e2e557cf9 | -5.76505 | -45.78796 | 2025-07-09 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 474e1514-88b7-3303-ae09-57a8a4f79ef7 | -8.50453 | -43.27832 | 2025-07-09 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |


[Clique aqui para ver as próximas entradas](README10.md)
