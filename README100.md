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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8158e98-5d80-3ab2-9114-294dc6eab134 | -12.41195 | -39.27565 | 2026-10-02 15:54:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 19c2f329-1212-308f-89ae-079a31be403d | -11.45766 | -43.40733 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 787bc061-d337-3656-aa0d-2194d61c58b1 | -11.50297 | -43.51603 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 492.7 |
| cbb8c8e6-c1fd-3293-8fa7-568720c3cae1 | -11.64561 | -43.5556 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 02a34752-abff-34d1-941d-9d86167ee066 | -9.81979 | -44.8073 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 91424776-8bbe-3641-910b-d5639a0a50a0 | -9.94801 | -43.46748 | 2026-10-02 15:54:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8ac09b3f-aa1e-3570-9dd3-127a0327fa84 | -11.41171 | -44.88753 | 2026-10-02 15:54:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1a87e4eb-4c81-3ad9-806e-43e447aa913e | -11.16877 | -44.61158 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b48261f7-36e0-316c-9de5-b318d7829feb | -12.13648 | -38.70296 | 2026-10-02 15:54:00 | NOAA-21 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c05963d6-9354-3b9d-963b-9e073fade515 | -11.65147 | -43.6021 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb26dea3-5f4d-38b7-94ef-9960bb4a30d9 | -11.40258 | -43.40837 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d5dd1d65-07a1-30ae-8b44-b1a0873edbac | -11.25318 | -44.30974 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6d81a97f-4405-3ba5-9633-bc98ff5e45a4 | -11.80312 | -43.55208 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0aa479a3-d259-3c13-b32e-c6449cbc754c | -12.79435 | -45.19221 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 332e295f-a5bf-3c82-8bac-94441c079c4b | -11.70168 | -43.59576 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 74bbdf4b-eaf0-3340-b62c-0b6a6b44c166 | -11.72187 | -43.4318 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 86403423-edb5-3d52-807f-4947c8c94133 | -13.34998 | -43.85015 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f2f34867-ad77-35af-9852-f3d7010f9fa6 | -12.18824 | -38.40917 | 2026-10-02 15:54:00 | NOAA-21 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b2dbd617-dff5-33c3-93b1-4202a2980412 | -11.7558 | -43.54032 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3454f2ed-7d11-3092-b1e6-df0776a496bb | -10.90091 | -43.8398 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d97678a8-d9b2-3613-9b4f-9ed15db294d2 | -11.48523 | -43.41419 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 9a28ce14-7c12-3b74-b26f-22d72144c8f3 | -12.53254 | -43.09995 | 2026-10-02 15:54:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 7999615d-5b4e-33c6-b236-e0ce80f6b962 | -11.47472 | -43.4225 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 08d5c2fa-7f3e-3fa6-835c-11879dba083a | -7.04588 | -42.3056 | 2026-10-02 15:54:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 19f56af9-b62f-3b2f-afc0-4fe6020983e7 | -12.02725 | -39.03988 | 2026-10-02 15:54:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| b426bde9-1f7c-3468-a628-c6a4288bf6c0 | -11.29521 | -44.25813 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 24f922fc-3aa8-3716-b56c-542dea739460 | -12.89157 | -44.73057 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 03003d21-7724-3c6b-9769-fc8b154a0420 | -11.25481 | -43.52711 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 813f501d-cc00-3057-a31b-c1b5d4af75a7 | -11.30084 | -44.26072 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| de7da4b1-87c5-3ee9-a5c6-5de7b9b905aa | -12.47887 | -44.15102 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 0d25d9f1-acb7-3101-abd6-568d83c4f594 | -11.59943 | -41.43862 | 2026-10-02 15:54:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5a7af5dc-ea39-3ba4-b7d3-de3c1ea30449 | -11.30606 | -44.26009 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0f39f3df-b833-36d7-8229-e449ac282492 | -10.15192 | -40.10115 | 2026-10-02 15:54:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 13.2 |
| be0f96e2-7927-3a8a-b75e-83f0ac260b53 | -11.16298 | -44.60875 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5f93310e-4775-3117-89d3-d57ba1cc389e | -11.78306 | -43.55459 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 70400fdb-7fa6-3dbc-b9a6-f95cdb0808e3 | -12.58573 | -38.91785 | 2026-10-02 15:54:00 | NOAA-21 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8fc8a5d7-77d6-3baf-aa2c-eed883d270a9 | -11.25835 | -43.52382 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2d95be6f-0289-3caf-ac3b-8ac50609db18 | -11.48168 | -43.51394 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 65815b71-4589-34c0-8ac9-4b7c3a611cdf | -11.74859 | -43.52352 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b2fd31c1-10ff-3eae-97ab-bcc58c10b9e7 | -13.10628 | -43.50018 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 93f80620-d061-3c9f-aa7d-aab56eb9a359 | -11.67404 | -43.61912 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0ef703e3-aada-3422-8c4c-b9a4a8a0974f | -10.92771 | -43.84883 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7b866f0b-649e-3d5c-8a21-9a275bacabdc | -11.78195 | -43.54593 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 839ecf99-417a-36e5-86c0-76f89827ca5e | -8.78747 | -45.8159 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9661d237-e9ce-3350-8c09-c30124604a30 | -11.30768 | -44.27296 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 53f9858f-25a6-36c4-8c7e-9580d41e56c1 | -10.91101 | -43.83851 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 796fefd8-641d-3260-bc4f-85e427888b53 | -11.24228 | -44.30772 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 37d48f0e-0646-3ca4-8a47-02b5da96b1a9 | -12.46836 | -44.15256 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 75a6235b-ad6e-3f72-bae4-4a635e23890c | -13.0961 | -43.50138 | 2026-10-02 15:54:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ac9c4383-e9dd-3379-b6e8-b3473160da23 | -11.72454 | -43.61669 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 01ae98f8-9b87-3b56-ad4e-2fcf5670dd8d | -8.80986 | -45.81299 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ce978c38-c0d8-34ef-96dc-1d26a0e32476 | -13.33593 | -43.86525 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 980104ae-d696-35e3-bb72-9f5e7020c81f | -11.72002 | -43.58001 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2747187a-989c-3a21-b23a-dc770ba1a2a8 | -12.51089 | -44.15041 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b234cf87-b409-3393-8ec8-5c6fb3c58ce0 | -11.11318 | -40.93783 | 2026-10-02 15:54:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 364676fe-1af3-39b9-8f7a-65afb79922ca | -11.80887 | -43.55717 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6fa6e64c-01fe-35fe-a448-835112b7442e | -11.36514 | -43.43002 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fe750d68-e285-37c5-80aa-c0f157a9853c | -5.88879 | -35.21451 | 2026-10-02 15:54:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 47a3f4c2-22ea-30a2-bb1f-12ddbab30b9c | -11.66792 | -43.61113 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ba3790d1-6693-33c7-84f2-bfb179d753bd | -11.42584 | -43.39415 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 66d467f6-c4af-39f2-a710-ddbe36725cd5 | -11.72538 | -43.58213 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f6124a77-1a13-3eff-ba29-bb2e0b8a023f | -8.80381 | -45.81015 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5b4983f9-15f0-3c9a-be91-0540767d7ead | -8.77781 | -45.81774 | 2026-10-02 15:54:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 588cb616-811c-39f6-b97b-0b84b4759074 | -11.25534 | -44.24423 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 156cfc7f-159b-3530-9aba-92cae7ae948d | -11.39694 | -43.40343 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| bb465258-c78d-3248-9720-f7f87258114f | -12.18389 | -40.57689 | 2026-10-02 15:54:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cfb6cc70-c3cf-3858-87c4-33b087039615 | -13.34516 | -43.85403 | 2026-10-02 15:54:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b0433970-2df5-3747-9638-cb70bac6535c | -12.17929 | -40.57376 | 2026-10-02 15:54:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 39c14f14-5a61-3ce6-8343-4831e10a8abb | -12.79389 | -45.18827 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 07f9d8bc-d6d1-34e1-be8b-0e872f22461a | -12.78075 | -45.17405 | 2026-10-02 15:54:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c74485df-65ae-370d-9750-734aa434402b | -7.60447 | -43.98145 | 2026-10-02 15:54:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5d39e5dd-adb2-3163-a15d-918dc1c73f68 | -11.81568 | -43.56969 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6fcbe094-40b4-31ee-8370-30fc535f00a4 | -11.59806 | -43.54089 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4954bd14-cb4f-37f5-8036-a6faa661cd9f | -12.48372 | -44.14702 | 2026-10-02 15:54:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 83b0f02d-2c83-3f98-b4ac-6ea058cb210e | -11.4697 | -43.41043 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a80d3c30-d638-3b18-ba55-773ca75b9414 | -9.85469 | -44.83396 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dd00360-386f-3b89-8f44-3e6920fbe975 | -11.7425 | -43.51545 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c0741bef-b5f2-38ef-8e85-0b034ee83506 | -7.88972 | -43.8539 | 2026-10-02 15:54:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8dccb1af-9dbb-3968-80bb-8b995dccb1c7 | -11.78771 | -43.5511 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f0653866-ab03-3061-91a5-f581db681e17 | -12.00794 | -43.26868 | 2026-10-02 15:54:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 674d37cd-1d82-34d4-9ead-63611e93a643 | -11.29601 | -44.26456 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 12d91439-7420-3808-9b60-186da1f14b0c | -12.7439 | -40.23128 | 2026-10-02 15:54:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 72e25579-8728-3dfb-9edf-efca532fa942 | -11.25012 | -44.24485 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d6b79a59-7c1a-3221-8520-c9a6a102a523 | -11.25411 | -43.52143 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e937bd1d-fac2-36c2-8174-057f2d2e6490 | -12.77826 | -41.83295 | 2026-10-02 15:54:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| edebf433-12d1-336f-a974-745108a683ce | -11.68604 | -43.55362 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9a5a9622-6dbc-3aa3-91ec-56963a963812 | -8.35044 | -47.22228 | 2026-10-02 15:54:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5cf2fa32-c812-30f0-b7ff-390e15636c37 | -11.31291 | -44.27235 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| bbe765cd-bbb3-35e7-a6fb-ca37e84f42f3 | -11.71034 | -43.6232 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| aa093a84-7ac4-39f7-88f7-d95f261fd3ee | -11.80416 | -43.55882 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2487d8ec-3ade-37d7-8df1-0f8fb68097c2 | -9.84852 | -44.82796 | 2026-10-02 15:54:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 82cf1671-3ae7-388a-8f2c-bdaeaaff3425 | -7.41209 | -40.52583 | 2026-10-02 15:54:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 49.6 |
| e31bd3bc-c048-3dbc-872d-3c6aa11ac184 | -11.70742 | -43.60198 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6ae3cf5e-8427-34f1-aaf8-c0c02fd6cc37 | -11.64414 | -43.54398 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f93e1ddd-0a69-34fc-b7d0-fad9a76a5935 | -11.30204 | -44.27036 | 2026-10-02 15:54:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 7e802e0a-cab1-3535-b2b9-6cbf4da090ab | -11.70174 | -43.51797 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 133a7470-87e5-3abb-af48-a833764ddbd5 | -10.91606 | -43.83792 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 0911edd1-8de9-3cd8-9fd8-c1d602d2a306 | -9.16956 | -45.24425 | 2026-10-02 15:54:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b74662e7-21f9-38fc-ab8a-8cc3bc03ad6b | -11.77193 | -43.54717 | 2026-10-02 15:54:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 36c27ea8-4e69-33e9-b799-67ffe185134d | -11.11903 | -44.60387 | 2026-10-02 15:54:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README101.md)
