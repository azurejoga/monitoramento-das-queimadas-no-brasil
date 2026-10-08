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

## Dados Diários - Página 228

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd5f9b4f-db09-3b56-abe5-b11a8a583dc1 | -11.7485 | -43.64681 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0da8ada7-d839-32f8-9083-ac8504707c04 | -11.61432 | -43.62694 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| f6dcadd3-914d-3bda-a772-2bb8d778f2b7 | -14.43278 | -40.80825 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3a0e7c68-4a26-3189-9e7d-614bd434c3bf | -14.42641 | -41.1379 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| e49dd117-f4ba-31c9-89b1-6e8a37ab17cd | -16.19552 | -44.56943 | 2026-10-08 15:39:00 | NOAA-21 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 3e0fce53-773d-394d-81f2-83976d20b2a4 | -14.7897 | -42.83661 | 2026-10-08 15:39:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 96d7da8e-b579-356d-b681-14fb1c4e230f | -15.01062 | -40.81831 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 97cc19de-52e8-3759-8295-5e90cc002910 | -17.95765 | -42.77211 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 89b6dc25-6bd6-325e-b877-3408ba866378 | -15.34143 | -41.69606 | 2026-10-08 15:39:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1205fcb7-7eb7-3a81-a082-f361be014bfe | -11.62008 | -43.61851 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 38ab0325-bace-326b-8cfc-d2e8ccb7c32b | -11.84007 | -43.52977 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 64efbf67-d1bd-3f63-a801-2dd0199cdd9b | -11.80217 | -43.52513 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 79b3a739-1733-3869-8203-82924f8afe97 | -15.40387 | -44.32776 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5a3ec88a-cde8-3d3c-9e67-5c957a4a8d07 | -16.90704 | -40.88977 | 2026-10-08 15:39:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 72da1a6c-6b94-3151-8497-07bf0f68486a | -14.98921 | -40.49923 | 2026-10-08 15:39:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 31ffb60a-3d72-3085-8f32-89411ce1ff12 | -18.08741 | -42.93751 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| b1893cf5-9536-3599-b3d9-23a6e862e053 | -14.26177 | -42.43667 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 98.5 |
| b1188535-bf3b-30f2-9101-de0d8957fc55 | -15.17612 | -41.23462 | 2026-10-08 15:39:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1936a03a-39b4-3034-8d64-cd195d6f0395 | -16.24825 | -41.73299 | 2026-10-08 15:39:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 13a56a31-ffe2-36f5-b9d3-64fe7e42d059 | -11.60719 | -43.66822 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 732eacc1-d779-37ac-a717-5029f1ce1764 | -17.09096 | -40.0913 | 2026-10-08 15:39:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 36982bcf-1ffa-3ce6-9a6b-92b0c11eb1ee | -13.97697 | -43.26107 | 2026-10-08 15:39:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 60944794-ec24-3ba5-bf0a-3c62e69fde8f | -17.20574 | -39.28141 | 2026-10-08 15:39:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 14465332-a34c-362c-9f42-4baee9530e4b | -14.75824 | -39.81011 | 2026-10-08 15:39:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| ebc454b5-0acb-3894-82af-9831f5956b68 | -11.72246 | -43.63936 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5bca6822-3638-35de-83c1-c69b5dfb268b | -11.62795 | -43.69214 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7e2ebf2c-ec8b-3f37-868a-9737665ea28e | -16.34922 | -44.71991 | 2026-10-08 15:39:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1557fe77-9960-3f36-9701-abafdf41058a | -11.84775 | -43.5405 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 435e7e0a-06b9-3799-8ff6-82754ee30c7a | -12.83937 | -44.62809 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 93568ff2-1a1b-3a09-a1da-c0026ae485c7 | -16.935 | -42.10824 | 2026-10-08 15:39:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1ad96ce6-df5c-39e1-978b-9f30ee8c32ec | -14.5372 | -41.77693 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 110.5 |
| c16f7ea3-6c99-3f7d-911c-c85dbfb73fdb | -16.01447 | -40.66183 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 64d43ae6-73c0-3cfb-9afc-75090c2363d9 | -11.6139 | -43.61922 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 73e28def-9aed-3448-bc5d-63163d7a886b | -14.52563 | -40.32788 | 2026-10-08 15:39:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 92bd8b34-c1fe-39ff-a864-fcdb5d8369a5 | -17.11335 | -41.34146 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 55cc62e2-2b41-348f-9cbb-0d6304ad6e79 | -16.69103 | -42.51995 | 2026-10-08 15:39:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7499d04-5b13-336f-8e2e-7d5470b3a19e | -14.46982 | -40.7185 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| b9373170-1587-3cd5-aa54-7250c9ab2311 | -14.26373 | -42.43676 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 6e666d95-e51a-3c61-98ab-8cde4578645b | -15.95633 | -41.10157 | 2026-10-08 15:39:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.5 |
| 7e9621a1-7ab6-393e-a451-40aaa286aed1 | -12.15565 | -44.75074 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 792182f5-76ec-3188-a85e-9a4fca8360b2 | -16.43447 | -40.26872 | 2026-10-08 15:39:00 | NOAA-21 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 3c4522c3-2d0e-3a69-a5d1-d42a5facaf66 | -11.72797 | -43.42246 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f8edfac-c19e-31e6-83e8-16ea2c15a2e1 | -13.93485 | -42.3563 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8749899c-285d-31b7-b827-088d602927dc | -14.49962 | -40.82292 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a01e607c-3741-3282-a94e-27910e37cd4d | -14.17826 | -43.66805 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 922efd61-ca3c-37c5-b0aa-cae59625ccc5 | -15.60505 | -41.7794 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 061bf03e-bab0-3924-b8a1-ed5277c51d4e | -13.29707 | -41.50991 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 6d0de37a-369c-35dc-aa09-c747e7396913 | -12.71978 | -45.81895 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b5e6400d-15cf-331a-be80-db50a59596c5 | -14.35538 | -41.4965 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 16.4 |
| ca7c9c92-a97b-32e5-ae6d-a9352194c692 | -15.95551 | -41.09412 | 2026-10-08 15:39:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| bfcbd65c-5010-3dca-8f1a-d5aa12331e13 | -14.73396 | -41.79215 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 8e1e0c28-977c-3f42-be8b-63028da77e2b | -12.02982 | -43.44461 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 73bfdca4-e72f-30da-8245-9ef0fb3d7b37 | -15.51076 | -42.65482 | 2026-10-08 15:39:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 3653a8de-cb8e-36d7-8332-db5c6bc45a03 | -15.47823 | -42.075 | 2026-10-08 15:39:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 387599f9-7d3c-3930-af29-23a1f926e675 | -11.73161 | -43.50849 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 625fcb5f-ba95-3353-8b25-866d72855c88 | -16.14802 | -43.11842 | 2026-10-08 15:39:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9af3bf50-ede9-3af1-b1f4-a432ff1a8c7f | -14.52204 | -40.79783 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ccb544a0-37fc-35c4-8175-fa220286d88e | -11.76253 | -45.55502 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ed0c1df4-0788-3727-855f-1106506af48f | -12.21328 | -38.48658 | 2026-10-08 15:39:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6053a964-f21e-398a-8aaf-b8a78def041c | -11.76405 | -45.5682 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 971ff201-0385-3d99-a688-ebcb66fddee9 | -14.13834 | -40.79495 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b03b15c2-236e-3dfa-b40d-51aa9773bedb | -14.43158 | -41.18426 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 404af1d0-abc3-3ced-ad48-b75274d6564d | -15.59969 | -41.16316 | 2026-10-08 15:39:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b8c59423-e399-3b67-b59d-21df384495a2 | -12.15698 | -44.76246 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b5336883-38de-30ed-8ce1-cd3d4c2c067c | -11.59991 | -43.65983 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 92e40e51-0b8c-3f3b-9294-5b4d501dea1d | -11.77851 | -45.57805 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b1371f3a-3006-3003-99ee-b1056a436b5c | -14.11456 | -40.27025 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 67f51cd7-be23-392b-8097-54486122a68a | -11.72718 | -43.63498 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d7b17f78-1d94-3472-9ba1-680b49c15737 | -11.0195 | -37.58283 | 2026-10-08 15:39:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f2fbd346-2aed-3e4a-9045-e7977664da57 | -15.79411 | -44.68477 | 2026-10-08 15:39:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e04263b3-6f25-3dd5-bf86-77ff5aae130f | -11.75525 | -45.49376 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b4796779-352b-3db1-8628-49353bf992ce | -11.60975 | -43.64209 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 9db00ed0-ce2f-3262-aa01-9bd66c4e682e | -12.14967 | -44.75747 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eb809d51-272f-32bf-823c-66cdb26ee91e | -14.42543 | -41.13933 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 3f96e23c-8bbf-30bf-986d-dd09c49f2906 | -13.29324 | -41.5217 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 2fdcc308-6ef2-3ce7-82f4-a99c8f118e29 | -15.39153 | -44.3411 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| b87aceeb-9341-3a5d-9f57-f9bd9cd17b51 | -14.43661 | -40.47696 | 2026-10-08 15:39:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7d102894-6f85-3365-a0e1-2cfc1bc33016 | -14.85198 | -42.06431 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 796e2a94-b5f4-3bb6-a7bb-e722979521e7 | -13.85364 | -40.64405 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4584cfa3-2cc2-30b2-af53-d0286a30a765 | -15.5738 | -42.89565 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 5a7102f5-e949-3457-a846-b70097ba2030 | -14.34534 | -42.0141 | 2026-10-08 15:39:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| edbaebde-ada6-3c41-88a0-f8b5e33a4eb3 | -15.43127 | -42.30643 | 2026-10-08 15:39:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7cfe7262-0081-3252-8621-8c2b71e70252 | -11.62474 | -43.70991 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| adef715f-51ba-3c2e-b9c4-bd88bad4ad39 | -15.63018 | -40.13654 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| c9c57ca0-2b71-3f54-be1f-051ccc5f9bb6 | -14.73563 | -40.29773 | 2026-10-08 15:39:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 11fb8172-bb3d-3400-873c-755db8aa8a2e | -17.67364 | -39.14703 | 2026-10-08 15:39:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b6854b71-9ddf-3981-ba29-8772c0ca98ce | -16.20397 | -41.37307 | 2026-10-08 15:39:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 118fc95e-51df-3e85-9ac8-3bb93be4446c | -13.97603 | -44.84317 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| de4d26a9-49ef-3bca-ae35-6459bf146eb2 | -17.7045 | -43.29014 | 2026-10-08 15:39:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 71f12484-7190-300b-8154-d4fa8c2228b8 | -11.59877 | -43.65023 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c213f679-9bf7-300f-93a9-e824c6bdcacc | -15.34518 | -41.04398 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| b988cbde-328f-39b5-957d-e07cc677d32a | -11.63667 | -43.70427 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| d7809795-d8b0-35f9-b02f-6d479b2ac714 | -11.68357 | -43.68301 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f64f1f09-efb5-3e17-8a3f-66073b4ab637 | -15.62461 | -40.13393 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 32b20746-cb26-39d7-b2f4-9bbcf82c3aac | -11.77781 | -45.57159 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 6a520b77-d8c6-31be-b3df-35f575fb5475 | -11.62343 | -43.7079 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| b394a0c9-f485-394b-be30-4971d4d723d6 | -11.7733 | -44.68671 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9360a822-0db0-3e86-a6f2-c3ef6164e5c7 | -11.8016 | -43.52035 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 23cc16fc-28e9-3202-b947-1ab9280a8a2c | -11.73452 | -43.64439 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 027a0295-adab-3507-baef-fb89bc164bef | -14.56534 | -41.53475 | 2026-10-08 15:39:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README229.md)
