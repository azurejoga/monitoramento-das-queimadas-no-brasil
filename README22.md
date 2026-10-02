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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84a73fc9-2eae-3a47-b1a1-08f009df071b | -4.50852 | -38.21754 | 2026-10-02 03:15:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68aa83a9-7834-3779-a898-19991a846348 | -3.98101 | -41.52074 | 2026-10-02 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| da912cf3-b270-3782-818b-aa3c787db89b | -3.98352 | -41.51569 | 2026-10-02 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0edd054b-a830-3188-bc44-74dd5419b42b | -4.39511 | -38.21759 | 2026-10-02 03:15:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e22773ee-58f1-332f-8507-1e0e494e0915 | -3.98242 | -41.52193 | 2026-10-02 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4392e116-580b-3112-b5c1-95943b8a721f | -8.78258 | -41.07986 | 2026-10-02 03:17:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90477616-18ef-3188-8595-d0d1c9df4bc3 | -5.57654 | -42.73228 | 2026-10-02 03:17:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c1534ea5-8bdd-38d9-a0d2-1f233b0688e4 | -8.75997 | -35.11689 | 2026-10-02 03:17:00 | NOAA-21 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3880987f-3afb-3214-a189-17c788f94861 | -8.75584 | -35.11614 | 2026-10-02 03:17:00 | NOAA-21 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fb002fd0-6900-3fca-b517-3004667a9c5e | -6.33476 | -42.64272 | 2026-10-02 03:17:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| ff15800f-e878-3ba4-8b3f-279eabf7174e | -6.34288 | -42.63776 | 2026-10-02 03:17:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| df9e0b83-f816-301a-8bb6-057d32141620 | -6.33598 | -42.63597 | 2026-10-02 03:17:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 969cd35c-cd31-363c-97b1-af2789ac040a | -11.74933 | -43.57975 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 87e8ab40-ff42-3fef-8039-774b6cf84443 | -11.73445 | -43.44936 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed8c0753-0c7d-3935-b42e-8f403650f1a4 | -11.73018 | -43.57024 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| fbcb4993-9e74-342a-a90d-6a3a7ea7cece | -11.68507 | -43.60993 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 684706f6-7716-3cc8-9b49-b07ac81c37c5 | -11.76905 | -43.55251 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92c8cbb2-5c98-39c7-a611-f205efe91e3b | -15.66866 | -40.73173 | 2026-10-02 03:19:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 591162ec-59de-3d37-9e11-a015543d5907 | -11.77118 | -43.57622 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8f962def-f4a0-3d66-8e6a-9dc45f4019fe | -11.68616 | -43.60458 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9e18fe7-97ec-33ed-8407-95e5561f3e91 | -11.78398 | -43.55899 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4279fced-19e6-3065-86e3-7a98610a76e6 | -11.67508 | -43.59749 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 3d021d5d-c1e7-3289-9cae-9054f93d51a4 | -11.6476 | -43.55222 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b1718cfe-8083-340a-b369-155323faf400 | -17.44525 | -41.91529 | 2026-10-02 03:19:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bafd82aa-b920-3ba6-89be-b9f78b4d769a | -13.33278 | -43.86443 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a145c888-914c-35ee-b397-3bb4e62f4d74 | -11.7425 | -43.57871 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 6dcadc7c-17a8-3073-9644-c749452beff4 | -11.42388 | -43.52544 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 041d3bd7-83b0-3b02-bc6f-20bf60a5a5b6 | -14.33672 | -44.74026 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31d6aef0-9025-38df-aa9e-8f9105d2d0b5 | -11.69558 | -43.60073 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f3135ae4-1b9f-35ee-b89b-19d994fbeafb | -12.52033 | -43.10957 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0a4dd9e5-3539-3476-a6ef-12f7cf9d6ce9 | -15.63416 | -43.23698 | 2026-10-02 03:19:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 49e64cfd-5c50-3f1e-91c3-31d421b48d64 | -11.77814 | -43.57659 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 9f39d95c-ced7-31fc-bcf5-ea6984afd740 | -13.85353 | -43.63615 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90be5fba-55f8-343a-b1fe-6ced8c403c8e | -13.3408 | -43.85954 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 79a9e014-3b42-345b-91fa-b9a4ad5b687e | -11.66019 | -43.59359 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| eabeea48-c0fb-387c-a9d0-3af3c21b7e3c | -11.4116 | -43.51662 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01848dd8-eee2-31ff-8aea-0456cfbf7b71 | -11.7303 | -43.43579 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43a22a9a-2d2a-3605-8a16-13190af363d7 | -11.41889 | -43.40207 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 44c6ad16-b815-32c9-8a0f-42761e9838cf | -11.7357 | -43.57754 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| db854358-c4b9-33ce-a597-90c0b28a2050 | -13.54504 | -40.07317 | 2026-10-02 03:19:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a4788e2c-f0f3-3ba8-a0d3-322f1ef26322 | -11.65648 | -43.61156 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e1e8a9f1-47d4-308a-a8fd-3d25e582aa0e | -11.7102 | -43.43169 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ce2b526-2556-3731-bdbd-51b880ea2484 | -13.86485 | -43.64001 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b51696b3-472f-3188-8727-7941c819c411 | -11.65767 | -43.60582 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 54850767-f2c8-3d53-a297-8fd8d6089368 | -14.50443 | -42.21809 | 2026-10-02 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d35ef09d-c6c3-3fc0-949f-5b846f4cfd1b | -11.70369 | -43.51885 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db130ba2-c1b2-3074-8cf2-5cfb5aa32e7b | -11.7264 | -43.51068 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac0c8245-b401-30ee-b6be-973e4469d6c2 | -11.7942 | -43.57719 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3ed4f1b5-4e51-3a06-b2f5-8c3334b5b5b8 | -11.78978 | -43.56484 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9546e1ec-d105-30cc-ba61-3a0aa214a52e | -11.69302 | -43.61287 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f762ded6-a2e1-3d77-8a35-eb0872a523c1 | -11.72775 | -43.44795 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc430da4-9fd0-3db5-b7b3-2251f0be2256 | -11.69302 | -43.60555 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 719a865f-57ac-30da-b1d5-1fd61f2a8c99 | -14.03009 | -41.59906 | 2026-10-02 03:19:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6617c83c-ed46-3640-85db-1b20e3852d31 | -17.22714 | -41.2018 | 2026-10-02 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99fad2c8-e5ed-33e3-afa8-9039f9c02b9c | -13.63901 | -41.35899 | 2026-10-02 03:19:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02fe49d1-a8fb-3925-94f7-06e8363c5c82 | -11.66702 | -43.60217 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 40be8eb8-21d0-312f-bbfb-20c2c9204052 | -14.33518 | -44.74729 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8c20858-54a7-330a-ba83-35e9db1db4b3 | -11.76652 | -43.56474 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 70941fe2-0419-3167-84df-c16c63fd0d17 | -11.7758 | -43.55385 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df300380-450a-3399-bd2d-362e6e436f38 | -11.68992 | -43.59407 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8fb55bf-c707-3c5f-b7b1-9ef05079d576 | -11.69178 | -43.61161 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 486b4ccb-1724-3d4e-b21a-173deae2244f | -11.76208 | -43.58622 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ab3fbddb-5bb8-3cce-9562-ed30878db9f6 | -11.74558 | -43.4506 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8deb4825-f869-3dcd-9038-699797a7df01 | -14.50349 | -42.22257 | 2026-10-02 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fe98bdcd-11c9-353b-a425-eed9a9dbc7eb | -11.76426 | -43.57567 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 65e9a191-c937-32ab-84d0-bd2d19679aa7 | -11.6942 | -43.59978 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41e74fe7-ccf8-3d52-b7b1-024b18c759cd | -11.4657 | -43.42519 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 84dd9fb0-ad44-3034-a1bd-4657037e0045 | -11.7653 | -43.57064 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 64bcbb06-3503-3135-8c92-00ddc3d1c5fe | -11.73573 | -43.44326 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39cbfe90-d039-3bae-952c-2dcdbfe8d61a | -13.86361 | -43.64577 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9ba0a920-dc71-3e69-aa9c-962e60ebfe20 | -11.80069 | -43.57979 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 07108d09-8bfb-3846-ac63-2d0e5c5fccbb | -16.1246 | -42.22703 | 2026-10-02 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 96718930-5bdf-34f9-906e-e32075ddd34c | -11.45482 | -43.40997 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0eb4fd7-734a-30c8-aad6-8cc9053cc0fc | -13.34262 | -43.86477 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e730d1da-4e54-3bf3-92c1-afeab95a11bc | -13.49541 | -42.50606 | 2026-10-02 03:19:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4670ddf2-29b5-39bc-9f93-aa212120d1ab | -14.87214 | -40.70006 | 2026-10-02 03:19:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a82d4e6d-57ed-3f5d-832a-51c839ee24e7 | -12.92315 | -42.45013 | 2026-10-02 03:19:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dcd56338-4b38-3deb-ab01-c3ca19af9f12 | -11.67141 | -43.60769 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fb45cc0-6746-389c-ab9b-d8754e50ab45 | -12.91033 | -44.8175 | 2026-10-02 03:19:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d363b715-feff-3c8f-a6d9-3ee6b5c6a4be | -16.85997 | -40.57985 | 2026-10-02 03:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 178aceef-2e0d-37aa-a533-cd154a18d0f7 | -11.76873 | -43.5881 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 06e962b9-27ec-3f38-ae80-322f74793699 | -16.11961 | -42.22208 | 2026-10-02 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5338daa8-4a59-38d7-875e-ceda3e333603 | -11.79565 | -43.57034 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 314ff8f5-4410-399f-a09d-23e9cd98953e | -13.344 | -43.85844 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6bae1458-4993-3958-89cf-cd75bfa08543 | -13.85886 | -43.64336 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cfb8eb20-ae4f-3ddd-9eac-1eec4ec0ce5d | -14.34484 | -44.73483 | 2026-10-02 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48ba0fb9-752d-3352-aa3f-79b3213bfa58 | -11.78282 | -43.56446 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a983db4-aa25-300e-a065-3d12596672e3 | -12.53048 | -43.09312 | 2026-10-02 03:19:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6119ec9b-505a-30ad-bffa-1a6c8380c629 | -11.67252 | -43.60227 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8915704a-f6d7-3434-ad22-d50371a28ed8 | -12.86141 | -43.81156 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 174e8655-ba21-3cee-81ab-3fa664cfba26 | -11.77217 | -43.57142 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb1f0c8f-f50a-3963-8535-3abacda9867f | -12.85469 | -43.81019 | 2026-10-02 03:19:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21d9b6a2-2b02-31fa-aaff-f80c5c1aa62d | -11.73694 | -43.5716 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4785c1b4-232d-35d2-a5dc-d78b6bce953d | -11.45899 | -43.42375 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0eb949cc-94e5-3ec7-a2b4-2ccffdd5009c | -16.12386 | -42.23051 | 2026-10-02 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c73eed69-9859-3370-84c9-e6ce477a2b28 | -16.86375 | -40.57982 | 2026-10-02 03:19:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43ceb007-ba28-321f-b8ec-c5d69c06fcfa | -17.21432 | -41.21011 | 2026-10-02 03:19:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 226b112b-46c3-36f2-8707-213d4f112a14 | -11.78621 | -43.57159 | 2026-10-02 03:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59a6443a-3d99-381a-9c96-65ae6ddffa52 | -15.63527 | -43.23178 | 2026-10-02 03:19:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 12529da8-580a-31e4-a46c-b399dd2eac95 | -13.86539 | -43.64479 | 2026-10-02 03:19:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README23.md)
