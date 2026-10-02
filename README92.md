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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a67793ee-18b1-3053-bd3d-83378d1e4543 | -14.43905 | -42.23792 | 2026-10-02 15:52:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2fe21934-e1cc-370b-ae3f-99ba5177da8b | -15.98063 | -41.4459 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 4ddacb21-6858-37a8-8565-d320daf20687 | -13.60687 | -40.58272 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fb7672d0-67b4-31f8-bd3b-88c313607cce | -14.32808 | -40.59929 | 2026-10-02 15:52:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3bcf57fb-c463-31b3-8e59-e4aaeed5cef2 | -15.33728 | -41.22486 | 2026-10-02 15:52:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| d768e273-9c0f-3497-85b6-18a3507b53e8 | -17.21404 | -40.28485 | 2026-10-02 15:52:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 78674159-8e71-38a9-a477-95f8e188778f | -13.87686 | -40.97503 | 2026-10-02 15:52:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 2f7c747f-5254-3856-a716-7e2f87cdef28 | -19.41732 | -44.03698 | 2026-10-02 15:52:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e405ea29-f232-32cf-88a5-0da14a9732fb | -13.80037 | -45.26349 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d1719a1-8b14-39d3-a10c-11a538bcf5e8 | -15.0567 | -41.33789 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 17564fc0-2291-3dea-bcae-50f30ea094a5 | -14.78694 | -41.56359 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| fc389176-69ff-3237-99e2-a2a5f3e357a3 | -14.2569 | -41.61852 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 66da5da9-8775-3f2e-a225-886bb6dfb255 | -19.51862 | -43.99157 | 2026-10-02 15:52:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9da0c2ca-63b2-3736-a746-8ee03aec952c | -15.34216 | -40.94175 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fabbea6c-d8fc-3a06-9d9c-8194f0e86c6a | -15.30252 | -42.78514 | 2026-10-02 15:52:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 91f7ce97-e083-38c5-b4e3-96b1fbe31a22 | -15.11274 | -41.44357 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1423bd4e-a13d-38a9-92fb-5bcdb6ee2694 | -15.43933 | -39.75243 | 2026-10-02 15:52:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 38083704-18b5-3481-9c77-60418e2688e2 | -13.8127 | -43.36565 | 2026-10-02 15:52:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 17330791-7f7f-3fbb-a732-86a499778979 | -13.86555 | -43.6411 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7353e4cf-f735-3edb-979d-e7097a5cce20 | -15.13112 | -43.60661 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 3eb05fd5-1a53-3017-9bff-5606c7a37360 | -13.80955 | -45.24189 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6dfe6ece-1ae2-397a-bb05-9b1542b5d184 | -13.30962 | -41.05697 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 320a06ef-e81d-3c7e-8fb7-c0bd6450ddb2 | -14.51266 | -40.79473 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 1fd9cc7b-52fd-3a70-8ed9-b3bed9ced7d0 | -15.1289 | -43.5867 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e3eafaef-1e65-323d-80ea-b97191fc5d07 | -15.7709 | -43.6461 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 535813a1-fe4c-3b7f-a8f2-d9fe34f4cec6 | -16.08438 | -41.61454 | 2026-10-02 15:52:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 3c5b8a33-5cc1-3558-985f-dbfff6772b3f | -16.6764 | -41.85233 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 27c4b0b2-d3eb-36ec-b573-c842d4332403 | -15.86755 | -44.29879 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b7358662-1f05-3a81-ae0c-630f09a4582c | -13.80237 | -45.23021 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6e776834-17e4-3110-bbf3-96ed629d4b25 | -14.38139 | -41.53185 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 45.8 |
| d026e37e-35c6-3d04-a046-0d4187847443 | -13.87557 | -43.63674 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a795af1b-e71c-3424-b28e-3f2dc7264859 | -15.16466 | -43.66725 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.0 |
| a7a0fa59-7ac0-3b66-b851-7ab7592096b3 | -13.79662 | -45.231 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2c00bc4a-29b1-37c0-9bf7-19d3908ff230 | -15.01807 | -45.17786 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4ea51990-fee3-3039-aead-a0de2780c4ae | -14.05687 | -40.63169 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9370b005-7bb5-3b4b-bda7-171950a65d32 | -15.02396 | -40.97661 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| f02620ad-cefc-377a-8ed8-39c393faece1 | -15.76954 | -43.64668 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5612a4fc-4372-3b8a-b6fa-1695a7ae8cb6 | -13.82968 | -45.26419 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 068b9dd3-d0d4-389c-b8b4-e4880e2b969f | -13.8475 | -45.25863 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 2062d572-6c83-3983-b966-68934d443aec | -13.33499 | -41.22383 | 2026-10-02 15:52:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f94cd85b-910a-344e-b69a-85fca833b5bb | -15.1349 | -43.59272 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 9a7f89ef-8f01-364a-b2c4-25288d91ae1e | -15.93561 | -44.50797 | 2026-10-02 15:52:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0cbadf20-f74f-30fc-8d0b-508dfa018c8c | -15.50998 | -41.75358 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| aa34223c-b197-3556-82f9-abeaed2211c5 | -14.43711 | -44.77558 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 46cad4c3-345d-3cb1-84e8-ba2fed0a1f42 | -15.72173 | -39.37122 | 2026-10-02 15:52:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 34f7da46-5726-389c-9a9e-c33b4a633ccc | -13.87075 | -43.64051 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 99461493-fd96-355b-9513-e59301cb18a3 | -15.13442 | -44.05193 | 2026-10-02 15:52:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a53503f-6094-338f-b33c-7a5e01418d45 | -15.3518 | -39.62241 | 2026-10-02 15:52:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| eb06c40a-88ea-358b-a0a0-016a1e58b0dc | -13.40112 | -43.69632 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7af4179d-7ec0-3735-90a8-8eb9687cf0a4 | -17.98707 | -43.66354 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b03570e6-051e-3742-9d5d-ff6445034d6c | -15.11675 | -43.61859 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 19.9 |
| c9090a6a-e755-3d06-be32-d201a51f56dc | -14.69795 | -44.69691 | 2026-10-02 15:52:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4ccda44e-8386-35d4-9ddc-44e6986fe520 | -15.11714 | -43.62194 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 91780ad9-84ae-3c1d-9b9f-b9a000fb3f4a | -14.17881 | -43.90154 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a739089f-6b77-3c8f-9f48-1e680b204340 | -13.11983 | -41.68018 | 2026-10-02 15:52:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f2acf043-1499-3f87-a89f-4eb486e20430 | -15.14025 | -44.05489 | 2026-10-02 15:52:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d0dde618-8af0-3738-af33-5e446a664802 | -15.57618 | -44.55297 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f9d8dabc-b2eb-3bb1-8bb0-29321dff697a | -16.37693 | -42.97203 | 2026-10-02 15:52:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 05bcad14-8de4-369d-907a-9c9cbd758a46 | -13.60738 | -40.58669 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dc0c7481-bb1e-36eb-a41e-6a9114cd3ab3 | -13.84218 | -45.26335 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0064b13a-8a81-3fda-bd0b-4cfb17249757 | -13.99733 | -40.47686 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 3aa7f748-bf2f-337b-acee-ca637ffadc42 | -15.52774 | -43.01496 | 2026-10-02 15:52:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 0693ea53-81a2-3a38-86c1-71e9990387e2 | -15.74506 | -43.65594 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dfbc7ff1-5c42-3990-b938-8f06629140f1 | -14.93691 | -45.46616 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c7bdbcbe-06e7-3ad6-85f6-990413af61d5 | -13.78561 | -45.23664 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e26a61d3-54d4-3eb0-8816-0be186716213 | -15.13543 | -43.59612 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.8 |
| dae6e187-3408-39ea-90f5-957181c568ba | -15.86672 | -44.29105 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 224.6 |
| fa1c2c7e-bf77-3b14-8cd9-83577191b1b0 | -15.58225 | -44.55633 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 94799b61-1d11-3c6a-919c-483b27c5b775 | -16.68999 | -41.06042 | 2026-10-02 15:52:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 9bbc13ca-80b6-33da-920b-4a072e0b4443 | -13.78654 | -45.24476 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ef762f4f-3541-3ae5-a41e-d1136d0f7b5a | -13.88596 | -43.63554 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f46b447c-b96a-32d8-968d-70e42eedfce3 | -13.76981 | -40.61232 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a8a5afba-4d89-368a-b4e3-7817f1dc08dd | -14.67144 | -41.1293 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 807068f1-a856-385f-8bc1-58e6854cbc08 | -19.41342 | -44.03587 | 2026-10-02 15:52:00 | NOAA-21 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bd38238a-2fc0-382d-889a-4de0af021d5c | -15.87311 | -44.29814 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0b7f7685-9304-3142-b7f0-24a614c2c15a | -14.36854 | -41.17725 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7e860958-5be1-3ce3-9a92-0ee6d4b89c2d | -17.29942 | -42.31518 | 2026-10-02 15:52:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| e07e6ead-25a0-35dd-9b3b-f902c95ebc7f | -13.67309 | -43.33989 | 2026-10-02 15:52:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| da29e28b-9235-3de8-9844-b64a7d92c736 | -14.53836 | -41.31033 | 2026-10-02 15:52:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 432bc276-1746-3043-bffd-87d33f7714e6 | -17.84353 | -42.21629 | 2026-10-02 15:52:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 258290d1-d578-331b-aa17-09dae78cbedb | -16.71796 | -43.73342 | 2026-10-02 15:52:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c93f710-1320-35ba-9e87-6728a9079a7f | -14.23119 | -41.78881 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ab052e8c-8e43-310d-8f10-95dbae39c4ad | -13.40899 | -40.78542 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 5a2ca73b-2a43-3e86-933c-4ba0299ead48 | -14.65801 | -41.61922 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| ed5aad77-86d2-3e6a-8e7e-6790d14c8710 | -13.84795 | -45.26272 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| fc81f92d-0649-3eca-90c5-0606e99fcdb3 | -16.4198 | -40.25173 | 2026-10-02 15:52:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 455d8997-1218-3bee-ad22-86c8d1f86d5c | -15.30648 | -41.4238 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 461104e9-f934-39fd-8d85-da7c7bde9c6d | -15.09695 | -41.38953 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 685e5560-8a55-3883-8ce0-14f8d0eef846 | -13.3944 | -43.68429 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c4ae42a1-69a4-3eda-8971-4bb0d6b11164 | -14.84851 | -40.62415 | 2026-10-02 15:52:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5a3f9876-ee41-3cfc-8604-6b6817d2feae | -14.3238 | -41.3245 | 2026-10-02 15:52:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3d31d27-3a07-3ce6-9d0a-a9a1b1239228 | -14.38074 | -40.34143 | 2026-10-02 15:52:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6ff9952c-cb07-36d1-8b49-54e002596247 | -17.99832 | -43.65478 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7291d320-4ed8-3670-8273-9499f65f007e | -15.30141 | -41.42727 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| f14e8072-991b-32fe-b018-d582cf1a6b60 | -15.26435 | -46.15338 | 2026-10-02 15:52:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4653c807-50c7-31f1-aa37-570c27440003 | -15.86199 | -44.29942 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 8593447a-939d-320f-a4cb-9de52d3b6e74 | -15.0246 | -40.98114 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 163.1 |
| fe12c229-6113-3e25-997d-395bb2083a8d | -15.17639 | -43.67611 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 49e30113-4ae3-3c77-9a63-5ee95ed0bb70 | -13.99681 | -40.47296 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 57683951-0091-34bf-bca2-bdf478e57ff3 | -15.78277 | -43.65534 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README93.md)
