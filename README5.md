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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9edcf45-6593-3fb0-8288-017d962c3c56 | -12.38054 | -43.46083 | 2025-01-21 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19eab9a7-66e3-3c6c-a73b-3ab05819542d | -13.21812 | -40.49849 | 2025-01-21 12:23:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 8546346b-cead-3ffc-b448-a20ba367110a | -12.23416 | -38.80731 | 2025-01-21 12:23:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 94b12858-0374-3aee-b5e5-d90aa99e6216 | -7.73277 | -37.63558 | 2025-01-21 12:23:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 31.1 |
| c748a604-e894-3cf3-a206-3391f130cb21 | -10.23671 | -36.8982 | 2025-01-21 12:23:00 | TERRA_M-T | CEDRO DE SÃO JOÃO | SERGIPE | Brasil | 2801603 | 28 | 33 | nan | nan | nan | Mata Atlântica | 38.2 |
| f8589e72-4c4d-3582-b853-8d8d53ab2d75 | -7.73142 | -37.62975 | 2025-01-21 12:23:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 62.3 |
| b0d37567-4768-352a-9f4a-95273e04469e | -12.52057 | -44.22801 | 2025-01-21 12:23:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 467e40ad-cb49-3f80-99bc-2a25dd10edbc | -11.13429 | -41.56524 | 2025-01-21 12:23:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 77662e87-d581-3950-a5ea-5f8199ca90b8 | -12.23102 | -38.80016 | 2025-01-21 12:23:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 941f918c-8fbd-3844-af29-cffd4b4b86a1 | -10.45251 | -40.33469 | 2025-01-21 12:23:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 41e4e34e-6aea-3b57-9090-2fbee97d6f28 | -17.04638 | -42.85606 | 2025-01-21 12:25:00 | TERRA_M-T | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8c3b7cf-c80e-3d35-83fd-42a191b717af | -16.94355 | -42.77174 | 2025-01-21 12:25:00 | TERRA_M-T | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 536ae58b-4aeb-3fc7-9f7e-840b97a4736c | -16.98397 | -42.78334 | 2025-01-21 12:25:00 | TERRA_M-T | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 466632db-8e04-3787-a24c-918d6907c80e | -14.87562 | -40.12732 | 2025-01-21 12:25:00 | TERRA_M-T | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| d7defe05-3f5e-3bbf-b566-bb41bf320ad8 | -16.72844 | -42.70727 | 2025-01-21 12:25:00 | TERRA_M-T | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c7573a01-93b5-3593-a86b-f5ce2524bb60 | -16.72994 | -42.69565 | 2025-01-21 12:25:00 | TERRA_M-T | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e2d080ee-7563-30c5-8be8-45ca7fb04bd4 | -16.87629 | -42.7512 | 2025-01-21 12:25:00 | TERRA_M-T | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f1212a47-8eab-3d49-82c3-9944942c1918 | -16.87776 | -42.73962 | 2025-01-21 12:25:00 | TERRA_M-T | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 835bfd0d-17b9-31c7-aa92-015dc4e8e2d8 | -19.87748 | -45.00474 | 2025-01-21 12:27:00 | TERRA_M-T | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 382f1e65-4e35-3c64-b274-1619b617951d | -21.4514 | -42.86736 | 2025-01-21 12:27:00 | TERRA_M-T | ITAMARATI DE MINAS | MINAS GERAIS | Brasil | 3132602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| a1183cb7-56b6-359d-b242-8551a3e6f694 | -21.53563 | -43.01658 | 2025-01-21 12:27:00 | TERRA_M-T | SÃO JOÃO NEPOMUCENO | MINAS GERAIS | Brasil | 3162906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 95c0053f-042b-3330-9247-88027b650158 | -21.46034 | -43.55213 | 2025-01-21 12:27:00 | TERRA_M-T | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 094b92c3-267c-3501-9172-853b10b2c796 | -19.58788 | -42.64662 | 2025-01-21 12:27:00 | TERRA_M-T | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 9281c7d7-8b11-3572-b3df-c2a430bf9bed | -20.32855 | -41.4151 | 2025-01-21 12:27:00 | TERRA_M-T | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 014a913f-f2c1-391b-8ad6-ba399e809f3c | -22.42834 | -44.34334 | 2025-01-21 12:27:00 | TERRA_M-T | PORTO REAL | RIO DE JANEIRO | Brasil | 3304110 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 46774bca-1d8d-3be8-b11b-aab0c08e55c3 | -18.86619 | -45.00467 | 2025-01-21 12:27:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9ee621af-5040-3d35-807f-135a94cb2c8c | -22.28732 | -42.5292 | 2025-01-21 12:27:00 | TERRA_M-T | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| a3c5da6b-ba50-32bd-a2ef-3d7964fa82bd | -21.86435 | -43.00092 | 2025-01-21 12:27:00 | TERRA_M-T | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 58877599-894b-359d-8031-b7ac18ebcbb6 | -23.95477 | -46.45881 | 2025-01-21 12:27:00 | TERRA_M-T | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 5fd68948-1c0f-3c59-a4fa-20c5d17cf131 | -19.8882 | -43.66488 | 2025-01-21 12:27:00 | TERRA_M-T | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 862f3954-aa45-3c41-a18b-c77b63477f07 | -20.39798 | -43.41586 | 2025-01-21 12:27:00 | TERRA_M-T | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c5d0f252-39de-3076-8b83-b7968c004e13 | -17.99212 | -43.42776 | 2025-01-21 12:27:00 | TERRA_M-T | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c33b61d6-62ee-3be0-ae8b-a5fa27d82a26 | -19.3238 | -47.93898 | 2025-01-21 12:27:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 16be65a5-981d-3bba-8c88-66891be2faa0 | -17.60933 | -43.62104 | 2025-01-21 12:27:00 | TERRA_M-T | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cc22d46f-5d94-3502-9038-9aad173ab637 | -20.60404 | -41.20798 | 2025-01-21 12:27:00 | TERRA_M-T | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f557a436-22ca-34b4-acbc-cf6f39802183 | -22.90296 | -43.73491 | 2025-01-21 12:27:00 | TERRA_M-T | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 904d5ff6-bd04-326a-8310-78404d52d9c2 | -20.95205 | -43.79643 | 2025-01-21 12:27:00 | TERRA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 98bf4c0c-bc89-347f-83d9-18ad4c0f02fe | -18.72854 | -42.27621 | 2025-01-21 12:27:00 | TERRA_M-T | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0fe5e10d-eed8-3edb-a4aa-d4569fd5bdbd | -19.89047 | -43.80014 | 2025-01-21 12:27:00 | TERRA_M-T | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 18d42b68-10fa-3ca6-86e5-87d279feef91 | -29.73993 | -50.01393 | 2025-01-21 12:29:00 | TERRA_M-T | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 13.3 |


