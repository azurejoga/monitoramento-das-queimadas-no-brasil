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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c7faf85-f4f5-3b58-9067-454de8a1b874 | -15.78023 | -43.64576 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 042a3d60-fbb2-31e2-93b5-b786a1e751b8 | -17.18943 | -40.42049 | 2026-10-02 15:52:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| e1109f6c-2855-3794-a2b2-f6c4c8433b16 | -14.65861 | -41.62394 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| ee173c31-fac6-3d7d-8225-878ce1dc9434 | -15.13638 | -43.60599 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ef19e3df-d7a1-361c-9cd0-9c425e3709e9 | -16.53132 | -40.52852 | 2026-10-02 15:52:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 00c35ae1-70e0-3bc2-9554-fd67f0e7f5b1 | -15.74427 | -43.64911 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 40192be0-650b-32f3-abdb-a04b3e888926 | -14.34811 | -44.72557 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fc40e7fb-81c8-3566-81de-1402f08071e0 | -16.4246 | -40.25533 | 2026-10-02 15:52:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 29a1c047-8dbc-3320-bad9-cb5539c01062 | -16.16764 | -43.76842 | 2026-10-02 15:52:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e32c2d8f-ae49-3c0b-a872-b8d29a58deea | -15.77703 | -43.65242 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 5273e475-7385-3eb5-b440-029a0f02d343 | -15.85661 | -44.29484 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| ece2d57a-8ad6-3966-97b0-6b93a7cab20d | -14.81659 | -42.80538 | 2026-10-02 15:52:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 3911d0ba-6f63-3777-abbd-c7246e16d191 | -15.35542 | -39.6186 | 2026-10-02 15:52:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 30b58383-0e24-3ce7-b908-fc5f1b174a60 | -13.58955 | -40.97881 | 2026-10-02 15:52:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2126ccaf-8658-356e-b410-f637f087dd7b | -15.13149 | -43.60993 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 8bc60cb0-b828-3ae2-832c-b8704558670f | -14.39251 | -44.37727 | 2026-10-02 15:52:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b62028d0-a101-3516-8d43-1dfdebcca5e6 | -15.78134 | -43.65587 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| afb9758d-80a2-33c9-899c-6d046042cf26 | -15.56362 | -44.54215 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5433c030-c0ec-3c0d-b441-784a9d3497b0 | -16.14338 | -43.74654 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 56f51c3d-575b-3283-bf82-3e2945694490 | -14.33735 | -44.73098 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 31b0429f-329c-3817-b920-c7ffd331c796 | -15.07864 | -41.16505 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.3 |
| d7030b66-b832-3aec-891b-c57a4043fa19 | -17.99868 | -43.6584 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ea7e2a09-179d-3a5a-859f-7cb184bd7056 | -15.13662 | -43.60604 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2a56732f-548f-39a7-80aa-add318160ba5 | -13.86445 | -43.63161 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 297eaced-b311-3aef-8d36-b2c40d77aae1 | -15.30193 | -41.42444 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| 899eb86b-00c1-3803-979e-47b680f35630 | -16.13213 | -43.74335 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6fd38f62-9bb6-3e32-a920-afa32800f431 | -15.84418 | -38.96072 | 2026-10-02 15:52:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a88e543c-018d-3ffe-88be-036b86f2decd | -14.32545 | -41.32764 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d526b310-608d-35aa-ae08-5c1773093112 | -15.78097 | -43.65249 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2217ea0a-df84-3cc6-a5c8-ea23f3bebe3a | -13.55733 | -43.52283 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c91cbca9-0049-3ce2-b31a-59480e7fed85 | -13.98597 | -40.9188 | 2026-10-02 15:52:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 2f19359d-9bd1-3b20-9f56-a6f19682c9e8 | -15.87689 | -42.46724 | 2026-10-02 15:52:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 86f3ce56-b149-3893-ac0b-5d54eada8ff6 | -15.92997 | -44.50868 | 2026-10-02 15:52:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a7f59f7a-85ac-37d8-8f50-f4322afbf8ef | -14.32829 | -41.3241 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 04e80b4e-f355-3485-b269-d03dee5e06c1 | -15.13175 | -43.60996 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| feb7900a-1716-3852-8b3e-cfa157cb738e | -15.34214 | -40.94166 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3da77d02-0fd3-37be-96bb-f0cd9833b9f4 | -14.70358 | -44.6963 | 2026-10-02 15:52:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 98927fe3-28e7-324b-a008-a2fcc861ef7f | -15.02901 | -40.98055 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 46e5d0c2-98c3-3ab1-86ee-ccf32739957d | -16.52276 | -41.71486 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5ffe8d39-e83e-3aca-a179-991472dba645 | -17.43657 | -43.64202 | 2026-10-02 15:52:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3635fa23-38d9-3215-bf9f-e92071a2b144 | -16.65426 | -42.45698 | 2026-10-02 15:52:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 979b76af-8248-30ee-adb6-a374b50d52a9 | -16.75916 | -46.7976 | 2026-10-02 15:52:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b70c54ff-cd4d-36d0-a138-40f2b87d0daf | -13.86518 | -43.63792 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 316a1b44-0fea-3d17-9725-9662ef314dd4 | -16.23218 | -42.98247 | 2026-10-02 15:52:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71073714-db0d-3175-9da3-e86a399dd9c3 | -17.14613 | -43.03166 | 2026-10-02 15:52:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f2dbf10-064e-39c5-9218-f3a4bbb1fa1a | -15.56841 | -40.08858 | 2026-10-02 15:52:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| b288a040-cd55-39dc-870c-e0e2553e0ecb | -17.99209 | -43.65871 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| acc2a74e-df75-3277-9d28-a751c3d632cc | -13.87631 | -43.64305 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 330.9 |
| 0c4a9454-b5d9-3f94-854d-e83ef323963d | -13.67212 | -40.12854 | 2026-10-02 15:52:00 | NOAA-21 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 87e10426-09bd-3b2e-bcd4-5d78e2487fda | -15.45599 | -41.46516 | 2026-10-02 15:52:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 02b5593a-80d0-37ae-a10b-35e9e97500ab | -15.5554 | -41.63372 | 2026-10-02 15:52:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8196d364-5ac0-3014-9395-e0585eed5097 | -14.51695 | -40.79394 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 52480ad5-3524-3818-9201-8905a41ec6a7 | -15.87187 | -44.28658 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 064fb5a9-83f3-3a11-943a-cc402a54b892 | -15.69772 | -40.60036 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c93a98b7-5472-3d09-aa63-52b33988fb8b | -13.8867 | -43.64184 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8ecc70af-c154-3ba1-b7c6-1809a6c5fcb1 | -14.65344 | -41.61982 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 93ae8141-1699-3994-bc20-abc75cf53533 | -15.13135 | -43.60665 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 0ff8b944-3559-3011-9345-53a0b77fb9c9 | -15.77129 | -43.64951 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f744bcc5-cf62-376d-aa59-8f161573c77f | -13.87038 | -43.63735 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0b295525-9c50-3419-9711-7cd373de6f7e | -14.43669 | -44.77171 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9bd0f352-9b23-3545-ac49-d4355ef0f9fa | -13.88151 | -43.64245 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 330.9 |
| 56e50a62-4d86-31b3-92b5-9af93eab4f24 | -14.75261 | -40.92036 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4345c65c-3702-3d8d-b858-14aae419caa1 | -13.64261 | -43.83755 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79db8b6e-002a-3300-a2e9-9e6606448f00 | -15.35133 | -39.61887 | 2026-10-02 15:52:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 431f0c28-ea80-361a-8373-2624e970e536 | -13.76931 | -40.60851 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7b8b7a94-979d-3dff-b9f2-05b910b604c7 | -13.8804 | -43.633 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d5bdb40f-6dea-30b2-a05b-b1332ef81a0d | -15.13017 | -43.59672 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 988b13dc-230f-3e92-96d2-d720fcf805d4 | -13.39 | -43.69126 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 480490d0-1f72-3782-9293-3a6098f0d1fb | -15.85705 | -44.29869 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 96b1129b-b2ca-3942-a4d8-04b44f4ab210 | -13.81578 | -45.24521 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 3d9f002b-9449-3e90-8ac2-be5c4e78a812 | -17.43621 | -43.63862 | 2026-10-02 15:52:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b4713e6e-56e6-3a38-b753-c309245837c8 | -13.839 | -45.23467 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1b99715f-1056-3848-ac49-52d7147bb081 | -13.39995 | -43.6868 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ea317d0-ac9a-3d9c-b08d-3a65997d13af | -14.35373 | -44.72506 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 74c7983e-fe27-3917-b393-41fb2bd332e9 | -14.03081 | -41.60077 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3e46ced2-505f-3f3f-b7f3-2f42680cb0be | -16.53568 | -40.52794 | 2026-10-02 15:52:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f46b18b9-06fb-38e9-a29d-ba481af1d54e | -15.56404 | -44.54609 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5965aef0-bca7-3e2b-81a0-2c81733c60fc | -14.3921 | -44.37362 | 2026-10-02 15:52:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 021dab9f-ea5e-3b13-ad78-cea52a71d148 | -14.44323 | -44.47961 | 2026-10-02 15:52:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6a4e6faf-8509-3016-a424-fd3317b168d0 | -14.69526 | -41.87693 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| fe5b78fd-06bf-3f45-8b16-a0f42b8e2729 | -16.08181 | -41.69564 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f95719de-ff4a-36ad-9cc1-5e746d86fbbf | -13.8239 | -45.26479 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d6892e4c-71f8-34fe-b228-03f6817f581d | -13.83645 | -40.33297 | 2026-10-02 15:52:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 468f3c88-179d-35ca-9fbf-3c55ba8b354e | -15.58491 | -40.73324 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d27b3e0d-df8d-302d-a29b-0e68a1173942 | -13.40073 | -43.69315 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a22c2d5a-9a8f-3a74-80dd-b2d499e46b3c | -14.34338 | -44.734 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 288e4266-b39d-3af4-bf2d-e03588a415ef | -15.56267 | -41.73475 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2a30951e-2e7e-3b95-9b68-46cd71aa8cff | -15.7817 | -43.65926 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| e0bdabde-b8fd-3af2-bff1-16e255c41cd3 | -14.34294 | -44.73013 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 16054fca-b923-3afd-af60-7330d47f9e7d | -15.78316 | -43.65871 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c105f63a-8441-36c5-ae78-fc0a5884740b | -15.12899 | -43.5868 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 3aa8e652-aa9a-376d-bd73-2c1f6d15409b | -15.52264 | -43.01548 | 2026-10-02 15:52:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 32.0 |
| a294edbf-18c8-3bcb-87eb-09f027582b44 | -14.39801 | -44.37672 | 2026-10-02 15:52:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 316592d1-ad52-336e-99dd-f2b51eee2d37 | -15.60851 | -41.68307 | 2026-10-02 15:52:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 226.8 |
| 41e137e5-1af0-3abb-9781-3e79e58a5ef2 | -13.86629 | -43.64748 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d07a9e51-792f-381a-aadc-76a7f83e10e0 | -15.97602 | -41.44646 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 8e93c80a-a488-37a2-a653-c5a656176e88 | -13.8364 | -45.26398 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9fa19a0f-0b85-3779-890a-16490466477b | -15.13385 | -43.58289 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 72edc10f-de13-3cb2-a1d3-614d1d0f2274 | -16.7592 | -41.16967 | 2026-10-02 15:52:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 183dfef8-189c-3bcf-8592-74c784300936 | -13.87001 | -43.63421 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README95.md)
