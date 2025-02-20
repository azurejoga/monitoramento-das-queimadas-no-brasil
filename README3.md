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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9d70f93-523f-3814-b251-5a54dea73a7a | -14.42274 | -45.64122 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e83f75-7390-325b-a3d4-4e732a82e074 | -14.42398 | -45.64418 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a049cd95-5f82-3545-ba2a-6d458d4549e2 | -14.42119 | -45.65035 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc7414c-7f6b-3516-a2f5-2fc6f2d153b6 | -20.22192 | -46.51912 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dc63a72-941e-33fd-b9c9-ad0a9bc8a2bd | -14.45422 | -45.66846 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139ce478-2d90-316e-b513-7df78604b648 | -20.23277 | -46.45732 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a51d53b-3a16-32ff-a32f-754502835fd5 | -20.2227 | -46.51466 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26f49955-e26f-3290-bbd2-98deb6d34562 | -18.58315 | -39.83931 | 2025-02-20 04:04:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 17191cb6-77f0-3ef3-b9a6-ce272f9634ab | -20.20636 | -46.50202 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81b46298-fff0-33c4-a02c-9e714217a478 | -16.66763 | -40.76396 | 2025-02-20 04:04:00 | NOAA-21 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4517cc2-cf8d-3df6-84ec-7ead8cafca10 | -17.05006 | -45.04329 | 2025-02-20 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbde4d28-5e65-3349-af19-4f45ad336331 | -19.11008 | -39.73484 | 2025-02-20 04:04:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6deb9a80-a45e-3290-94d9-a8e7c835d916 | -14.42862 | -45.65171 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40530f9f-3136-3589-806c-7ba6f49e8924 | -15.57106 | -47.85666 | 2025-02-20 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2067514e-e7e1-3bca-ad20-50b1d41a2b89 | -19.53431 | -45.91257 | 2025-02-20 04:04:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 867e89c2-e694-358b-bcdc-31fb49b67ee4 | -20.22114 | -46.52355 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb00cd2c-018b-3644-856b-e54fe19657ad | -17.61114 | -42.5562 | 2025-02-20 04:04:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b618a4f-a52b-3ab7-b101-5fe052a72c18 | -20.22474 | -46.52421 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 264b951c-980e-32ab-93b4-c7c9ce4f2e8b | -14.41903 | -45.64054 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131be290-7dd7-37b1-a6af-28ba0c998bd5 | -20.29654 | -46.50504 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91e44c7a-e110-3b20-a78f-bb05e3d2b922 | -20.21989 | -46.50953 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc322642-d6e0-3216-8108-e3a86c8a585b | -16.68117 | -43.88294 | 2025-02-20 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b472d422-c32c-336d-a15e-8bb8617ddf03 | -14.42318 | -45.64874 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b637201e-8da7-3f4d-8dc4-42463cb3235e | -20.21708 | -46.50436 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e663baff-e398-359b-80c4-dacafa5da7a5 | -14.42784 | -45.65628 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00fb8eb7-87db-365a-8851-f39bca36bb85 | -20.20947 | -46.4844 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97a58f90-c93a-370e-b709-a9731a92a8f7 | -20.21385 | -46.48061 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76142787-923f-3b93-9f5c-a12b90075227 | -20.21116 | -46.51688 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db0a9365-b47d-3420-a65a-acae57ec685b | -19.86807 | -46.37341 | 2025-02-20 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9052a584-17df-3a14-b698-196f8ed27c05 | -20.02659 | -47.17701 | 2025-02-20 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae18fee-a03d-3db4-9624-edd28bd54dd2 | -17.87433 | -40.09823 | 2025-02-20 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27ce64fc-da9f-3d15-a8af-1176526c59d2 | -14.43563 | -45.66512 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23865808-9af9-3097-921e-2eb559efdd15 | -20.17175 | -47.28372 | 2025-02-20 04:04:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3dbe9ed-e2a0-3973-be49-646f355fbc70 | -19.89217 | -45.71653 | 2025-02-20 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15074924-152c-3c9f-8acd-e1216672023a | -20.56614 | -42.39584 | 2025-02-20 04:04:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b27994e7-872e-3769-8d13-2f746f90606e | -14.4505 | -45.6678 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da15b44c-30b1-31b5-971e-c96fb7ea4035 | -19.86981 | -46.37472 | 2025-02-20 04:04:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42f437c3-072b-380c-9a42-6c0faedc4b52 | -20.30915 | -46.51762 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2e0b2df3-8fef-36a4-bd0c-c1768c0129c9 | -20.30726 | -46.50735 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19d888d0-835a-3d64-8b0b-b6e96e90c566 | -18.69962 | -40.01264 | 2025-02-20 04:04:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c5d5cc39-a2de-39f5-8fd8-6c614d989d73 | -20.30014 | -46.50568 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e845e80e-d5a1-366c-9b98-6aaf61841e9d | -14.41609 | -45.63531 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b887434-25c1-35a1-9be7-196e4f5aa5a1 | -20.21755 | -46.52281 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41e4488e-be81-3dfb-8f02-689ad97685e6 | -19.85065 | -43.84338 | 2025-02-20 04:04:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2cd5b00a-f5c8-33fb-b320-50b8d3401b0b | -20.21911 | -46.51396 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26d90fc4-a586-362b-b7c7-22d9ee23a0fc | -16.03953 | -43.38358 | 2025-02-20 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4381e9d8-274f-3bf6-a336-474ebbb1c6c1 | -20.30996 | -46.51302 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 619d4f18-6160-3464-be06-0491e9720e61 | -14.43432 | -45.65075 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07be7dde-dcaf-3c26-ac07-c800a5f2c875 | -14.42238 | -45.65329 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a936d72-72b4-307f-8037-1f936cf2625a | -17.46113 | -47.00555 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c241c1b-4f41-3ec5-beb9-5d67ac0ff6ab | -14.40789 | -45.63852 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 590d44b0-7413-3891-a2b2-f7ff669764f6 | -14.44678 | -45.66713 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9dca205-e873-3866-bb94-b34a97ec1173 | -17.78225 | -42.81022 | 2025-02-20 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c714593a-0dae-3570-89af-2a2e450bff0a | -18.58374 | -39.83511 | 2025-02-20 04:04:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b331db98-f7ac-32bb-82af-6ba73ed56dba | -20.30882 | -41.19739 | 2025-02-20 04:04:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8eb80695-c9b4-3b05-af20-31e7e5a56700 | -14.43078 | -45.66153 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976219eb-9e61-3914-9cae-72a9e429042c | -14.43233 | -45.65238 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92c76f72-bdc3-35e4-8afe-820a9fc8c2d9 | -14.4249 | -45.65103 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6516ea11-b2f2-35a5-a659-f9ab504c7218 | -20.21474 | -46.51764 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6e97fad-a0bd-3e94-a26a-f6e259ccc14b | -20.02287 | -47.17622 | 2025-02-20 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e1f2837-2595-32ee-b161-b15beae2df44 | -20.22565 | -46.45575 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5910020-dd88-3204-b338-b5617f6a33f9 | -20.232 | -46.46173 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9bd8c2f-5c5e-3f92-b3a5-a1f4bc2e9d1e | -20.20993 | -46.5028 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f911ebf5-9ba8-31d4-82be-97e004938679 | -14.41532 | -45.63987 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a812cbf-7b2f-3240-b37b-d62e2f9402ae | -14.429 | -45.6592 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d34c3f8b-01e2-3124-81cf-05c1762d3de1 | -17.12404 | -43.62737 | 2025-02-20 04:04:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43e20bbe-54b9-3b77-9453-14105ecd038b | -14.42412 | -45.6556 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d6482ba-4603-3290-8f37-18a757c49431 | -14.44598 | -45.67171 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e42a9b2c-6e08-380f-be0b-655ca2735a87 | -20.2182 | -46.47694 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f72b748f-1d90-336b-967e-ffcdea157143 | -19.80087 | -42.06683 | 2025-02-20 04:04:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c24c03dc-426d-3520-86b2-af21e33712fb | -17.46158 | -47.01405 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08d4f830-1722-344b-8464-c9c9427d3732 | -17.3876 | -42.65834 | 2025-02-20 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbf6ed62-46b4-3abc-955a-8fd7c89e481b | -20.20868 | -46.48885 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45556287-6104-3c0f-82d8-45fd557a6252 | -17.75207 | -42.89396 | 2025-02-20 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 468eaa2b-3440-3ce1-9ea9-2072c980512b | -20.22922 | -46.4565 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e27af01f-a70a-3969-bb8d-b0c3eb525446 | -20.23557 | -46.46253 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efd6b634-d678-33dd-8162-67fbda0cb930 | -21.4126 | -42.21191 | 2025-02-20 04:04:00 | NOAA-21 | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| ba3e74c7-d6ad-37a3-9e7c-6de8db818a61 | -19.06104 | -43.90546 | 2025-02-20 04:04:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3ef778c-f813-33a9-b2b0-6a5ff7bd61b0 | -19.46907 | -44.76498 | 2025-02-20 04:04:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| effe0bd2-20d3-3be9-8b55-ea159f2263c6 | -20.24119 | -46.47275 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89ab327e-a212-37b2-aa39-dbbd8e036909 | -21.41487 | -42.21141 | 2025-02-20 04:04:00 | NOAA-21 | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 47d06953-1d2c-3237-9d99-de96687f27b9 | -14.68085 | -47.31401 | 2025-02-20 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c373838-9670-3b98-8731-264a485b6e28 | -17.46249 | -47.00904 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f19d2e1f-41a0-3f30-ab48-ada2870845c4 | -14.43061 | -45.65008 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d561b5-befa-3d3b-8918-0048d31281e6 | -14.42196 | -45.64579 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22abc4a1-a914-339d-97d5-b8f62083706a | -20.21272 | -46.50803 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e06d8911-4bae-3abe-bafd-b73b10022047 | -17.09512 | -43.80529 | 2025-02-20 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c90c3943-eae9-34bb-bb6b-724e4dfd4055 | -14.44226 | -45.67103 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92a9ea13-a06f-3d05-8239-0bb62e5bf6f7 | -14.68168 | -47.31361 | 2025-02-20 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3820393-0a46-3e59-ae75-94f14ae2224e | -21.13384 | -42.34712 | 2025-02-20 04:04:00 | NOAA-21 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34145952-5061-3e82-a894-01aae496f14a | -14.43191 | -45.66444 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75deb137-8d5a-3863-9fad-bb4a5d1067f7 | -20.02574 | -47.18177 | 2025-02-20 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29410ad6-e854-36ab-8ae7-6bb1bc756b4e | -20.24476 | -46.47355 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e696cf4-440e-35e3-b603-3ed7f7316cc5 | -20.2079 | -46.49326 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b2fc927-f2bb-3369-abd4-5cb5137f905e | -20.73249 | -54.60215 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b5ade8f-b99f-380a-9a66-d4f9c1f08cf9 | -22.90267 | -43.75799 | 2025-02-20 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 27511b05-3d5a-30e8-b19a-493df5f9ab12 | -25.19216 | -49.32579 | 2025-02-20 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5fb19a49-0c49-3c67-b3db-78ddce739f9e | -20.73342 | -54.59795 | 2025-02-20 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92855f55-090e-3337-ac16-8809d3881a08 | -22.54073 | -48.81273 | 2025-02-20 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a242dedb-84cc-3718-9aeb-3ab8f021aa6e | -21.18058 | -44.27486 | 2025-02-20 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
