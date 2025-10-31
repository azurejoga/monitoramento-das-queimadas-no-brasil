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
| 4beed211-ff85-3dd2-a28f-c416db45c4bb | -5.54448 | -38.03781 | 2025-10-31 03:15:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1bd06077-efec-34c9-abcb-4cddb8c368da | -6.51581 | -40.80086 | 2025-10-31 03:15:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5344c620-dd05-32da-9037-192d9c785866 | -8.85813 | -41.4458 | 2025-10-31 03:15:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b86b7738-912d-3eb3-a13f-031f6b751d78 | -8.39769 | -41.84769 | 2025-10-31 03:15:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 16adee9b-5b6b-3b8e-b841-60a3fb3f177d | -5.45755 | -40.87296 | 2025-10-31 03:15:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1fb015f7-1414-3501-beab-1e1bf30a781d | -5.4139 | -41.24022 | 2025-10-31 03:15:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8423251d-d852-3c7c-9b4d-a9f8f06d1262 | -6.03087 | -40.26395 | 2025-10-31 03:15:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 792fdba7-b3d7-35ec-9e75-80fa33bc8b21 | -8.89817 | -37.96655 | 2025-10-31 03:15:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a0ebc73-805e-3051-b224-3b025446781a | -6.2007 | -42.51926 | 2025-10-31 03:15:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 916dbaaa-2066-3d32-81f2-6a9223caf333 | -5.85065 | -39.51072 | 2025-10-31 03:15:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 636cacaa-2216-34dd-b9c8-d2579c4d1740 | -7.04889 | -41.47521 | 2025-10-31 03:15:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5008070d-efdc-35f1-90e7-ad534e534400 | -5.79003 | -40.81174 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dc7f805b-72b7-3099-84ba-fab847afa02b | -5.85664 | -39.51163 | 2025-10-31 03:15:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d908a3a9-68f9-39e8-b550-43206263cc1d | -7.04658 | -41.47691 | 2025-10-31 03:15:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 034ab396-7195-3749-a32a-288ed805b9ec | -8.90014 | -37.96938 | 2025-10-31 03:15:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b90cd13a-6061-3e60-adf9-617294cd8c2c | -5.80109 | -40.82467 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 61fc25fe-6441-3a04-900e-2c95ff26ed0c | -7.7935 | -41.57742 | 2025-10-31 03:15:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 454141be-ffbd-3ca3-a6cc-295c51f03d85 | -5.79031 | -40.8132 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8c71d62e-abb6-33df-a1a3-571e725f3302 | -5.41285 | -41.24619 | 2025-10-31 03:15:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d7c2367e-8251-33e4-96df-3e98eaa53fca | -5.80215 | -40.8214 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8560df8b-c40a-3c74-8c14-577ee87301a4 | -8.92235 | -37.28461 | 2025-10-31 03:15:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6366b228-d67e-35ff-9341-cdb4fc29632f | -7.75251 | -34.91634 | 2025-10-31 03:15:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 642e664b-ac70-33ca-b504-ff6edb1f65ef | -4.57137 | -38.28235 | 2025-10-31 03:15:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 292a5ef4-5ad3-3804-b569-2242cded93cb | -5.80193 | -40.8199 | 2025-10-31 03:15:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b64826b4-a578-3e00-9555-fb97c77abd73 | -7.78694 | -41.57624 | 2025-10-31 03:15:00 | NOAA-21 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3b9665d7-5806-3504-84fc-3cc55ecf9ec9 | -6.2059 | -42.51238 | 2025-10-31 03:15:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| def56b43-a3cf-3a73-9cf9-682490e46f89 | -10.50524 | -42.40388 | 2025-10-31 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 6bec33b9-f323-3e78-aef1-7fe7a5354610 | -9.31571 | -43.09295 | 2025-10-31 03:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c9938e7-bcc8-39e2-8e74-26a1f8fa7495 | -14.21398 | -44.39516 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4b16673-880f-3c15-ade3-2ef6c35273c9 | -12.29457 | -43.19526 | 2025-10-31 03:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a180ae8e-9588-32d4-b1f1-38d78e51030d | -10.50959 | -42.40649 | 2025-10-31 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2ff7c9a3-823b-312b-9a1d-926b0d822645 | -10.50301 | -42.4052 | 2025-10-31 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 38170598-8468-3f2c-9f44-8d554d3df916 | -11.01001 | -43.87502 | 2025-10-31 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4375256-e5a9-33de-b255-90e1eed252e8 | -14.20862 | -44.38676 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78657ed0-2969-3e46-a347-2760cf5c4bf7 | -13.68195 | -44.71452 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 43474de8-6256-30f1-baf6-3d9d14a5f905 | -12.823 | -43.48873 | 2025-10-31 03:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c62c4b2-6a17-3c04-8961-7041c62038dc | -14.12411 | -44.18345 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b1f6cbb-cff0-3beb-98f4-7b3143a0618d | -13.67863 | -44.7137 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6c29eb85-5dc0-3988-83ba-fe8c67d3516d | -14.20887 | -44.38934 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c613d188-fc18-3e72-8e7c-a07ccc90edfc | -14.07919 | -44.15967 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07f011df-0eb6-3b39-a50f-069772cddd59 | -12.83775 | -43.48545 | 2025-10-31 03:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e89ecfd-ae10-36cc-8ad0-6787b2972f2c | -11.01324 | -43.8788 | 2025-10-31 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69dda18f-95bc-3d0f-a080-19879eb89d0e | -10.50409 | -42.40966 | 2025-10-31 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 3bc007ac-d87a-367e-9f6e-26ce6deaac1f | -9.32267 | -43.09439 | 2025-10-31 03:17:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c4059ae-1640-3fb8-9a9e-de1c764120d4 | -12.82972 | -43.49017 | 2025-10-31 03:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 198d6278-e60c-34ad-910d-4b9b078dc18d | -10.43335 | -40.50232 | 2025-10-31 03:17:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c1b66235-52c8-3591-ac23-908a2edbbb01 | -11.71457 | -43.91908 | 2025-10-31 03:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e17603a6-41a9-3403-bd1d-5bb420a45d01 | -13.68741 | -44.7233 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 1836f9be-b69f-36de-9d32-74a0393ffc4b | -13.68415 | -44.7224 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8c9b0243-fbf8-32ed-8451-b92a8a0202fc | -14.08603 | -44.16115 | 2025-10-31 03:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9efddf9-b899-3107-9d89-7df0f9f45816 | -13.6858 | -44.73046 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 8eba47fb-67c7-3795-ac92-f0d1ceb4b76b | -13.68262 | -44.72942 | 2025-10-31 03:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 28677ca8-f5b4-37b9-a916-31c70c13efdb | -16.36819 | -45.24788 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d3ad3bae-187e-36da-80fe-93a27a96772f | -16.37513 | -45.24955 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13241aab-da31-398c-921f-b6c7bbc5d425 | -15.65187 | -42.89879 | 2025-10-31 03:19:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea4ad85c-6711-3ee0-b08e-a59fb02c5977 | -16.37354 | -45.25655 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c12a98da-f7cc-3e2d-9cda-c72dfaf192d7 | -16.36625 | -45.24788 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0896dd39-33cf-34f5-a733-146d7ff31d22 | -15.65298 | -42.89365 | 2025-10-31 03:19:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 177625f4-4a7b-3cfc-bc43-51f8e669f455 | -16.24643 | -41.72572 | 2025-10-31 03:19:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a867575a-3c4c-32e0-bab0-9c70afdc0c0e | -16.3732 | -45.24951 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2ca8a97-0ddd-37c8-850e-9dc6594f605b | -16.30139 | -45.09854 | 2025-10-31 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6182244-e569-3919-9a06-f2cda1bf8ebf | -8.0824 | -45.134 | 2025-10-31 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 7a799637-13d9-3cd3-93c7-707aa0f0a97a | -8.0821 | -45.1568 | 2025-10-31 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 90688bcd-2b59-3a33-8242-4a3164dd53e7 | -7.6491 | -43.5876 | 2025-10-31 03:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| f47bfc79-de28-35a8-b325-41c481d54b32 | -13.8967 | -47.3405 | 2025-10-31 03:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| e1f8e210-aac7-3807-985e-94b3f21662fe | -3.017 | -49.4482 | 2025-10-31 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 231e6125-8037-3638-b35f-08c2d66d2a7d | -8.1013 | -45.1321 | 2025-10-31 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 7a23684b-2a86-3604-8bbf-1aca8e5ed65a | -3.3024 | -51.9254 | 2025-10-31 03:20:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f9e179bb-113a-314c-837c-459cc6ece7b4 | -5.0399 | -43.6205 | 2025-10-31 03:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| f97a06b1-1b72-3c0b-bed8-d95ba31b1998 | -10.5293 | -44.7798 | 2025-10-31 03:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2bffaaed-54bf-32ed-9187-5083af10481b | -8.0824 | -45.134 | 2025-10-31 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0eea3a74-2cf8-31ca-962e-3a1c39c551e4 | -3.017 | -49.4482 | 2025-10-31 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 80f6259a-4f90-37b4-af7e-fc4d0d19304a | -7.6677 | -43.609 | 2025-10-31 03:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9bb786f4-cccb-32e1-ab2f-0ffdd4d07ccd | -7.668 | -43.5857 | 2025-10-31 03:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9367349e-cb3d-31e1-b933-660bfa6acea2 | -7.6491 | -43.5876 | 2025-10-31 03:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 9a9358a3-fde9-312f-be83-7348b2755d32 | -5.0399 | -43.6205 | 2025-10-31 03:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 53417568-3a68-3464-9fe5-8ce286b455e8 | -11.559 | -47.0742 | 2025-10-31 03:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 314e0250-03e9-3fb0-a20f-bbe2ae60ff95 | -10.5483 | -44.7773 | 2025-10-31 03:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| acd6966a-5e9c-3a78-89c4-5b97b6d2ef9f | -5.0399 | -43.6205 | 2025-10-31 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 689efe39-acec-38fc-bdc5-0011ec80c52d | -7.6491 | -43.5876 | 2025-10-31 03:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 00d06df9-dbf6-3cf3-a887-6fda89b2f4a6 | -7.668 | -43.5857 | 2025-10-31 03:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e794cd5d-e8ce-3ef2-96d6-4b15c6af2ea7 | -11.559 | -47.0742 | 2025-10-31 03:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 883d353e-1416-3ed3-88b0-80bd74b12131 | -10.5483 | -44.7773 | 2025-10-31 03:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| fcee8cb3-319a-3d4f-9359-63b5f519810f | -10.5293 | -44.7798 | 2025-10-31 03:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 6fc4c550-df16-3eba-81c7-aa41c2e333ae | -3.017 | -49.4482 | 2025-10-31 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3af7c65c-9caa-356a-8fbd-41cadace1393 | -12.2874 | -48.0676 | 2025-10-31 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a727e77c-1cd1-39ec-a6bc-b9ab9110cbe5 | -7.6488 | -43.6109 | 2025-10-31 03:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7d66b0d9-d991-3c7e-8e45-fc4ea4f03108 | -6.5631 | -51.1126 | 2025-10-31 03:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 36e22330-fe79-3f91-b6c8-70ad3720f3ef | -3.43451 | -42.50746 | 2025-10-31 03:45:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fa72369-efff-3bac-96ef-79648a672aab | -2.73285 | -45.20943 | 2025-10-31 03:45:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2e8b3a14-4035-3008-8ec1-168cdb91f005 | -2.76532 | -45.39219 | 2025-10-31 03:45:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5e42ace-23b3-38b6-b98c-685f7911d472 | -2.91272 | -45.41054 | 2025-10-31 03:45:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b90aff-edf8-36ed-8af8-bc0562a27554 | -2.10092 | -48.05344 | 2025-10-31 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 729374e7-b3a6-35bb-a5f4-91d0bdc4badc | -2.10213 | -48.04636 | 2025-10-31 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff55cf07-cf4c-35f7-9d13-a8de6ea6fed2 | -2.73884 | -45.21037 | 2025-10-31 03:45:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a2d6883-b785-30e9-83c7-ca5b47111d58 | -2.48986 | -48.15208 | 2025-10-31 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daf55bf0-5984-38b4-a063-bca920fecca2 | -3.61561 | -40.38086 | 2025-10-31 03:45:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 853854e3-abb7-345a-8f4f-f2eca5894a9f | -2.75925 | -45.39127 | 2025-10-31 03:45:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a43110f6-af11-3bd7-b654-692e240d964c | -2.90667 | -45.40959 | 2025-10-31 03:45:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7736d2c9-2717-3fc9-b46f-9577dcb4a981 | -9.73578 | -48.03121 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
