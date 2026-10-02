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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906f7aa9-7d3f-391a-8e5c-a7f6e094801d | -13.32273 | -43.7444 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 163d59c8-8be3-3765-82ba-6a805cae7fd8 | -12.54016 | -43.08101 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 228a10bd-e47c-354c-b9c9-db7c3383000f | -11.71122 | -43.42733 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 0331244d-1bba-3d8f-b593-5c08f40716d9 | -11.67694 | -43.60177 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1a41ae73-bdcc-3112-831c-c7d2a402064c | -11.26189 | -44.24588 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d6a1ea6e-a82d-3d4b-a176-91c50a0a9132 | -11.80923 | -43.55998 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| bf396190-d8b5-3513-a201-80dc920e4eb2 | -11.81497 | -43.56385 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 45acdee5-fbe7-38b3-ba9e-5eb925d9f4dc | -12.58563 | -42.10772 | 2026-10-02 15:54:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 3eb93cdf-17ce-3a6c-8faa-9e59392f094b | -9.82508 | -44.80652 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0a0438a4-86d8-3485-a758-de4376ce64a2 | -11.79308 | -43.5533 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 35898ce5-b252-34b7-a44d-e9014ee0bf27 | -11.14738 | -44.614 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af1fd8ae-003a-387a-ac61-5079bc5628f5 | -12.49304 | -44.13583 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 044c3e9f-8b5c-38ae-a73a-98dd9ae55f82 | -11.64743 | -43.57007 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f8544509-9753-301c-8e73-cafe33f20f0e | -10.63733 | -41.40302 | 2026-10-02 15:54:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5979c5c7-550a-33fa-9479-50e131544d2a | -12.17149 | -44.66175 | 2026-10-02 15:54:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 9d5b0dd5-6a4d-3f6a-8371-f2609ab159bd | -6.79567 | -35.40563 | 2026-10-02 15:54:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 15e0ce12-6c3a-3119-89f1-e9c14724a282 | -11.26182 | -43.51179 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| eb2823df-e83c-31fe-9b32-d70db2e02122 | -13.10083 | -43.49774 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f181deaa-f82d-3b34-818f-6d31769a7a16 | -11.30727 | -44.26974 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 2bdbab31-52a6-334a-8b19-2232111ed2e7 | -9.96474 | -45.12317 | 2026-10-02 15:54:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3624f877-e060-3f52-a812-2517ddf88cef | -12.16908 | -44.65947 | 2026-10-02 15:54:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3e5325b5-6ae1-387e-966d-3b12e615bccb | -11.70979 | -43.62142 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 530793d9-9439-323a-9d26-180908bb7b89 | -13.35079 | -43.8567 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| c5c74966-038c-3068-a721-b813efe02cba | -9.18367 | -45.69926 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9d98a226-21e3-3aa4-9313-f16cc278b665 | -11.70427 | -43.61578 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 923a864c-f8ee-3e1d-a977-d95e0893ded4 | -11.7432 | -43.44074 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 422c7a63-bd62-3ebb-98fe-3fa06303da59 | -11.47815 | -43.43809 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d85db76f-8228-3f7d-a057-fb36239ab5a0 | -9.79728 | -44.80028 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e59545d-f791-3360-9ff0-f5063935a159 | -11.48099 | -43.42046 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ffb77ba2-f295-395a-83a9-42c9cdea2ab7 | -11.47594 | -43.50872 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 98cdb0c9-7511-31a9-8b10-004f101d734b | -11.81026 | -43.56707 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 16aa0e91-25d6-359b-91d1-2ee3b106fedb | -12.49466 | -44.149 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 184.0 |
| ec37715f-903c-3def-90c3-2c0adecde5e3 | -11.70704 | -43.59779 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d7d40096-def6-3e42-a6bc-2e7a68826af2 | -11.65183 | -43.60496 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37ec88da-bd67-350c-8ea1-7e0d6bcbe281 | -12.14015 | -38.70243 | 2026-10-02 15:54:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 716dc4c4-fd83-33c7-ba3a-8e54e9c92869 | -12.54514 | -43.08095 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 6f15440f-c1e8-37f1-851d-546a6ddd01dd | -11.73859 | -43.52476 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e1827f1-bdf4-3fde-ae27-09c7cf2612bb | -12.54165 | -43.09295 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| a63a2608-8636-38ef-914f-7d968ab69a2e | -11.73541 | -43.5808 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4218aa0a-383a-387d-8a5c-b463af6338b1 | -11.72769 | -43.60085 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 0f50eee2-f59a-3ed2-8646-13255f6f7e68 | -9.84939 | -44.83485 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5a6e1361-8bba-3107-bb00-57dfcbee2baa | -8.62852 | -35.36379 | 2026-10-02 15:54:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d980cc3f-6171-3857-b0cf-5513f9938a90 | -11.71634 | -43.5915 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 914b9267-3e14-3b22-8078-eb55096abe61 | -11.26751 | -44.24848 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d45a8aa3-395c-3f05-89cc-b71468b323ab | -11.16833 | -44.60818 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e82f5049-6a89-38f5-8e0b-e6448f9cffbf | -8.78289 | -45.81321 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32e2eda3-e528-3d02-91cf-65e58c6bb60e | -11.4421 | -43.40353 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3e9546d2-f939-3d34-b205-a9eb81a15668 | -13.10773 | -43.51233 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 86608f4a-4335-3a78-a32a-8b905b99a07d | -11.84501 | -44.7466 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc4e4ca1-1719-309f-968e-bfb81d6e6fd9 | -11.49315 | -43.5242 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 684bf912-899e-3c23-9c12-35a7f3216e48 | -11.69665 | -43.59635 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a8427621-caa9-3493-a691-06ed65e13745 | -11.73572 | -43.58331 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| aba4d90f-2dbd-353e-9f8b-ec67e02c6df7 | -11.1502 | -44.59333 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 979eaef8-c216-34e1-b404-28948c3dd00d | -13.34138 | -43.85954 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c251fbae-c901-3095-88f2-bb37b0e786ce | -11.62776 | -43.57555 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 53bb0a92-b3a9-3579-8712-548be1f67c04 | -11.63314 | -43.57782 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed2bbb51-d586-392c-a3fe-725bbfcd6fa8 | -11.28919 | -44.25236 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0f40aced-e029-382c-a1e5-436aefe62e91 | -11.4598 | -43.41157 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 392ad299-de0f-3782-8bd8-8c5cefe5ade2 | -12.78233 | -45.13825 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 825a724e-2fcc-345a-a5dd-1d488e01ad5a | -11.74896 | -43.52642 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 5550c5f3-477d-3499-b8ad-887dc104c5ab | -10.9157 | -43.83508 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 702b501d-eb1a-39ea-b59e-df5d8d4ff00d | -9.94727 | -43.4619 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 17add29a-f542-3fb4-bcaf-dc5e31fda5b5 | -11.74786 | -43.51772 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| f0cefd22-ecd3-3365-b9b5-080f33f0a8a4 | -11.75958 | -43.45034 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| fb02c350-8311-3822-b413-4c9dfaa7f31e | -11.36583 | -43.4356 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c0dd828-719b-380f-a807-790f1d2a1fbe | -11.71602 | -43.58897 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 527c597c-c7ba-3c79-a29e-a9d96a06f62f | -11.48029 | -43.41483 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 15491d43-da88-3f72-8908-dbbdd376f5a1 | -11.67328 | -43.61309 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 0c70383d-d244-3a00-aa80-55bee0230eef | -11.47819 | -43.41062 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 354.0 |
| a3b74b67-4ba8-3355-bbb3-c4fd7517162b | -9.10114 | -40.74671 | 2026-10-02 15:54:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3fa7328f-a2c8-3905-89ba-726cbbc63668 | -9.96306 | -45.12432 | 2026-10-02 15:54:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ae30bf4-c909-3915-9fe7-8665e972ae18 | -11.65791 | -43.6127 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 73638e3a-1adb-3ed9-a456-afe4360fa630 | -12.25893 | -42.14822 | 2026-10-02 15:54:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 4fa7fed9-ae34-3f15-92b1-c54c86ce1e24 | -11.76618 | -43.54197 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7492adf7-cd1a-31b5-9951-55045758639f | -12.73984 | -40.23183 | 2026-10-02 15:54:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 73f2599a-c2fe-3ae9-af73-f52271728003 | -11.71912 | -43.61415 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| adabcdec-0d10-3643-a9f8-b1445479e599 | -11.27273 | -44.24787 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0a2f3016-464b-3b9b-a297-645017f41bdf | -11.70946 | -43.61865 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 5f39fb93-cde7-30ce-adca-72fb6100faf0 | -11.27343 | -44.29673 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1bd0403a-a22b-3e9d-98c9-f05a9bb446eb | -13.34435 | -43.8475 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| ac81e7aa-780b-3371-991b-d7222cd6754e | -11.76692 | -43.54779 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| df2557ca-bc04-3eba-8862-452f547a499a | -7.9464 | -43.72969 | 2026-10-02 15:54:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 692d441e-b331-31cd-95b6-ea866ce55ca3 | -11.70961 | -43.61758 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5b6f3fd-bfab-3d04-a4a9-8261d792abab | -11.67191 | -43.60235 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f0144ad-10b5-399e-9a27-705ef79ec187 | -12.52688 | -43.09453 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 1fd4c134-2f88-3db3-b7d4-e6d181780000 | -7.52197 | -43.91278 | 2026-10-02 15:54:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 879fc0dc-5d93-3c62-b11a-ee5aefc95ef5 | -10.52037 | -39.02496 | 2026-10-02 15:54:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 7ced4478-c44c-3c72-a6a6-f02c06fef883 | -6.77521 | -40.98421 | 2026-10-02 15:54:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b1013a90-8651-34d8-a1d3-783fcfa81199 | -12.77194 | -45.1474 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 885da936-9e61-3d32-82db-7b82ada43711 | -11.81072 | -43.57142 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f5279e2e-747f-3635-be06-32e626b10803 | -9.20324 | -35.69644 | 2026-10-02 15:54:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 7b0fe772-54db-322d-9fd7-ad332af10e43 | -11.74669 | -43.58946 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 374c0386-1802-3296-a9b6-30a0611e01ba | -11.74749 | -43.51482 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 57224bb0-5037-3d58-bcd1-aa18dced2c9d | -11.48742 | -43.5191 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3460572a-a3cb-3dad-8c98-427880f5bfad | -11.4924 | -43.51852 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| cf68e06e-e465-3f20-b54a-124571525566 | -10.30752 | -44.65013 | 2026-10-02 15:54:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6ae9c45d-5c93-3eb0-a69c-c6dee58cd61b | -11.74395 | -43.52703 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 85130443-8641-31e8-b166-fb372161c591 | -13.34034 | -43.85799 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f8f7c002-a897-3cdd-9f50-6611ee57ce2b | -7.5819 | -41.30021 | 2026-10-02 15:54:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fe46e316-b671-3d8f-9f4e-ba9d7d62ad67 | -11.28475 | -44.25939 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README97.md)
