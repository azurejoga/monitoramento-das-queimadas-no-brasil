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
| 7e14c950-da54-34aa-909e-61fb1477c7ae | -5.729 | -53.46675 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11129ea6-b395-3dd2-9ef5-c8cfe165c2f1 | -8.79443 | -44.2808 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e4a299b6-4b14-3049-9208-28f508b3ff55 | -3.39754 | -59.51879 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c085eebb-88dc-3bae-b20c-e5796190c513 | -4.22208 | -48.62055 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cf21233c-c794-3f60-b9f3-580c27906c02 | -6.79907 | -59.13916 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 385012e2-93b1-302b-9106-a3801d9da183 | -5.01496 | -56.09388 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee3dbc4-bcd2-3d5b-8248-e00dd91c6733 | -4.26855 | -55.44194 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab0006ae-9e20-3a53-9c3b-931fd8206c70 | -2.17342 | -48.31586 | 2026-09-22 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91d9f350-6df0-311e-84ee-b9ddd3c45ee7 | -6.61698 | -59.91442 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e36eb9e1-eff4-3296-bbb6-c98a5ec35a8c | -3.0611 | -54.39754 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac1c23dd-0891-3b4e-b542-5b68a2ad1f2b | -6.10443 | -57.70019 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b428ff73-9d1a-3a62-ac9c-8d73d5cd5c26 | -9.10438 | -65.37019 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95a8710a-4eca-3445-a80f-91842e1388ac | -6.05773 | -57.86434 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac8eece2-4864-3bba-9eef-01de2935f93c | -1.99142 | -56.54489 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1595718f-22c0-31a9-80b5-8989cc7476af | -9.10255 | -65.38029 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d089669-71ef-3569-b350-afac0c55980e | -10.0962 | -69.1284 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d19d96f4-07de-3628-ac03-bc998d6b4e6c | -3.58362 | -59.06349 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adc372dd-6da5-39f9-8fad-1fa58cfb0a7a | -3.33163 | -59.8081 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ead837c-1f50-357a-8a1d-aff259ef3261 | -3.39086 | -50.43903 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf5ecf06-354a-3b53-a383-daba00d0a376 | -9.40475 | -65.92378 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a4cf2c8-11ff-3215-93e6-74a7035dc448 | -12.33789 | -50.67161 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 328fcec6-5c61-3b46-b591-2383328fef94 | -3.81774 | -58.88908 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01360668-71ba-3192-afcb-283f9597e5b8 | -6.73028 | -55.06355 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17c2a714-b846-3ee4-9aa8-1771da49280c | -10.91864 | -53.94789 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f7fe85b-6e9d-3ffd-bcad-5f426da7dac7 | -6.30407 | -57.74247 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0363d12-492e-3375-8631-5117597ba42e | -2.89604 | -60.05555 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef5f0bee-d9d7-3b15-bb3e-3e245f8f8912 | -3.06505 | -54.41775 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1a36726-9828-3862-a581-fb4f25680a7c | -6.1964 | -57.78262 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8cc5479e-9657-3a71-9188-1b44c05fc100 | -6.13515 | -59.96902 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 066bc0ea-1dbe-3079-a594-3a2fa21ba708 | -6.83238 | -55.52991 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03cab654-8c5d-38a4-920e-94dd5188accd | -6.40495 | -51.24257 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4db51673-f2ee-310b-9532-fea86a2384a4 | -6.46082 | -59.9871 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffe6c053-e34e-3985-a3fb-a9d5fbb0eaa6 | -3.00345 | -54.16568 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b46114e9-81db-3f9d-a75b-d93728ac5495 | -7.24071 | -55.60329 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c4d7d36-f3fa-3a2d-93a0-5912968dbd08 | -11.29184 | -54.04103 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7fdc9c5-deef-3b82-968e-9ecbdd4a64d1 | -12.29815 | -50.70626 | 2026-09-22 05:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebefe050-157e-3780-86dc-46af2e0cd907 | -8.10469 | -55.35503 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aebf0310-1800-32bc-8be0-8bc0af9f350f | -6.68667 | -58.45564 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e84bed4f-eb8c-37b7-97e4-15023f8b0fe5 | -13.71452 | -48.7905 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 124e282a-cba5-316c-ac43-13afd4537d57 | -2.20507 | -56.09013 | 2026-09-22 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f63210d-daa3-3dda-80f2-3dad2a8b804d | -12.57143 | -45.98203 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ac53c175-cb27-3767-a534-54cea55bd995 | -4.26911 | -55.43833 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad51b253-ed2a-3dda-9d70-ced31924ecd7 | -7.31778 | -54.94495 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 318b7cfb-5343-394f-b430-e4ce2c2b8cf3 | -3.57968 | -54.5606 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e28129b7-ff87-3ef7-9392-41562cedbe19 | -3.8342 | -59.38483 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42ac54b3-65da-3803-a791-76f1d7f58920 | -3.52331 | -59.93888 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b5895ba-46cf-3348-a23b-938a202a9d7a | -3.05702 | -54.40085 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 549d1d60-4640-373a-ad59-7a9dc961aa1b | -10.54472 | -57.44371 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bc9a6a9-e5a8-35dc-bdcf-c81fc2594c20 | -5.9779 | -57.77301 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 026e424f-c6b0-3761-896e-fe0b10766a22 | -6.15645 | -57.71199 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa2e6d2-d141-3338-8ce6-9aac8b1505e6 | -9.566 | -66.04681 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed192ddc-6ba0-3a77-aa31-799482420536 | -6.80682 | -55.83303 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d687b467-8eab-335c-ab35-31a78e111214 | -5.20412 | -56.10512 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 121d26f3-3460-3884-8c7b-a6a47158faae | -6.43769 | -59.97562 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 572cf8fb-34d4-39d3-8026-d1a89b15d0e7 | -5.81238 | -57.73208 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce314aa-9c23-3eff-a148-e12198150286 | -8.67299 | -70.03304 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6473651-cc66-3c8a-a922-a29a3eada86d | -2.63236 | -57.53064 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02055288-bf3a-35ef-aec4-51cd3f2b9aa4 | -10.86975 | -53.95574 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09a3cfd8-b97c-3bb7-8775-175e7c5918cd | -6.65679 | -50.93637 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 426997fb-c37b-3416-ae0b-245422b0035d | -2.60479 | -59.75933 | 2026-09-22 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81b601c1-aba2-392c-bba8-8c2b44a2ce20 | -6.3598 | -58.28726 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ac36689-8af2-3951-9472-dda30e52d48a | -6.80257 | -59.00853 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db8b4eec-5a53-3ae9-b20b-900d06500b27 | -3.12625 | -51.60095 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de525843-c3ca-346d-87a9-8876b47f97a3 | -11.04535 | -54.14963 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 844efd27-c6a6-37a3-9961-611b6b7d88ea | -6.64438 | -50.07021 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03597757-91ee-3804-b947-23d69754533d | -4.52749 | -54.97237 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd5dd5e-1aed-376d-ba2b-e491ca0c3fd5 | -6.78823 | -59.14149 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8262ea0-c093-3fe8-8ca6-89263eb4129c | -3.77554 | -59.59734 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398d81bc-c7bf-367c-819f-e1a211336974 | -4.49106 | -56.07375 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7731ecd3-ff30-3c4a-b902-dbca40bebf5b | -6.92267 | -59.63012 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68489eea-6ee9-3875-9cfa-717b7eec2df7 | -3.48182 | -59.57675 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0006710-85bb-3078-bbda-94907c57511f | -4.10348 | -55.51279 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f3bc9ab-73f9-359c-98bb-3203823cdf99 | -14.67456 | -45.67061 | 2026-09-22 05:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe2b95c8-1e4f-3508-b96b-f5f7b7872584 | -3.39475 | -50.44186 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a515ed04-2d5c-3340-99c7-e11c467845eb | -3.29162 | -57.85911 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a3f172f-af78-32b7-8b24-3e6366a6c29f | -6.45506 | -59.97808 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 993ad61f-36c8-3845-b40a-be25d0dfb584 | -5.86883 | -52.03241 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44f39d77-ed92-3bb8-89d4-f9f4537f937b | -6.29538 | -47.65491 | 2026-09-22 05:23:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 052cd001-ba2b-3f84-9317-fcbc96a80b77 | -2.27519 | -57.9944 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4373e6e7-614b-30e8-8f9f-909f52089176 | -6.12938 | -59.95992 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab7cdaaf-0564-34b3-bf31-66615bf331e9 | -3.15481 | -61.39628 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 844efc20-b0e1-3354-af87-b888fdc14624 | -2.20453 | -56.09359 | 2026-09-22 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4d738fa-cfaf-34e1-9a65-949fe8798f9a | -14.75297 | -48.42542 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb99ad8-0791-35c4-9a7b-39c8ddfe0c3b | -11.93875 | -46.51498 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4222caaf-1b52-3d15-85ca-363748ef9b39 | -3.39689 | -59.52282 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ecb8f30-8e61-380d-86d5-90958f5fc25f | -6.91982 | -59.62574 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1135ff69-23b9-336f-89f1-10f397f8910a | -5.61372 | -44.84237 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b766733e-7d78-334e-9040-dcc366beb9b9 | -6.157 | -57.70851 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cab64aef-6133-34b4-982b-df9394cf89d5 | -7.605 | -55.35289 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d911b2f4-1dd1-32f4-b52e-aa79e882492e | -6.31073 | -57.74354 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2917961a-415b-318d-b886-b28bb58ab872 | -8.7963 | -44.29211 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9fa7558f-0619-3f2c-99d3-91b6893617c6 | -3.13405 | -61.39816 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ffe50b4-3baf-3147-9199-beacedd3b748 | -4.05849 | -56.31031 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1fa2aed-c34e-3bdc-b6a2-d9c0bb215a3b | -6.35533 | -55.7535 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a092bca-b388-3ec4-9d21-17beddf76b6f | -3.39397 | -59.51822 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ac2df45-67cf-3e1d-a189-43e2030b2d86 | -3.06396 | -61.2912 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3475fdb4-f397-3152-8350-933ecc17d567 | -6.22639 | -55.61708 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e25b9c85-2a19-31c4-b4f8-403cf9eaeb05 | -10.89949 | -53.97016 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91468ba0-e788-3a62-af36-b4928b476372 | -6.31466 | -60.00148 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6002d76-ba33-3717-9aa8-33d1639e5146 | -2.62947 | -51.70488 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README95.md)
