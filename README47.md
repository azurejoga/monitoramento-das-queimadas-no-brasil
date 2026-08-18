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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0c2cec7-55f6-3dcd-b87d-aabe0913fb3f | -14.83039 | -46.63746 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e248784e-f4c1-38c0-93a4-586ac93af0e2 | -14.44261 | -51.82468 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3b4ce68-f876-3622-921f-b59a29c9e7ec | -14.17392 | -52.91887 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b601bb9f-91c9-3510-86ba-109e7116265d | -15.4077 | -52.80695 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 722a7517-76f6-3d26-96bb-b4cab8742514 | -15.81713 | -54.18948 | 2026-08-18 04:59:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fc5c1b0-04b3-3da5-afc6-300b7e7bf66c | -14.17712 | -53.06369 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b24cdc05-5d89-370e-9b3f-8fd9b3c9baa6 | -14.16656 | -52.92155 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bb6c424f-d066-3b33-8b61-acc41065a078 | -13.41288 | -57.04578 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a984b988-7d28-3653-a198-5e53601a7cb2 | -14.16373 | -52.9173 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| c897d7df-6545-3264-932e-98137b466d0d | -14.15862 | -52.90512 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95ea6cd7-959d-3f74-b4ed-bae85e6e18e1 | -16.30368 | -53.17958 | 2026-08-18 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4d111fd-fb3b-307e-967b-021deb5f58dc | -15.26745 | -56.49044 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32689d62-8618-3b04-8861-32cb741aa176 | -14.30704 | -47.18046 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b003e711-2609-3c7e-abb4-81d42b67cd7c | -18.28719 | -52.07053 | 2026-08-18 04:59:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4168de7e-3a00-3f1a-98ba-f2baf0cec58e | -14.03249 | -53.68383 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b23bc86-9fa2-3f8c-aa3e-b0ce8e95261f | -14.35514 | -51.92824 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb1a0178-533e-3f0d-b544-7907d03ebdf1 | -14.17336 | -52.89973 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 126762aa-1bdf-3218-9555-1c32fac30d8c | -20.3031 | -46.47773 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 532af4da-ec28-3e8b-84b2-e30ea1efd83d | -14.83792 | -46.64306 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3693d18-f5e1-3fb1-8da6-e4e6765b1878 | -13.26916 | -54.24577 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ff8d2ad-a8c7-3a7b-ab60-c9e88475fda1 | -14.81925 | -46.63253 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 9554083b-6755-329d-8d66-fb63f6db0bd3 | -14.26743 | -51.91164 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2941ec5-dd51-3649-b514-1b2a04f7dbf9 | -17.45453 | -47.85615 | 2026-08-18 04:59:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e16b89-5b07-34a1-8a0c-c6b979dff224 | -13.46132 | -57.0618 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69639a3a-05dd-35bc-8913-8f9a8d96c7a8 | -14.27799 | -51.93813 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 789e33c3-8d33-382b-8513-884ab10af847 | -15.01815 | -52.70073 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f2efc80-ae4e-3635-9f8b-9e54c327f088 | -13.42419 | -57.06765 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af709eed-da8f-3e20-886f-e67ea730fdb9 | -14.6273 | -54.46154 | 2026-08-18 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b21968b5-db92-37cf-b930-364db3ac7d46 | -13.42281 | -54.39058 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26fe3fe2-22e8-3e6d-bd92-7f0d6eaf38d9 | -15.98691 | -54.16438 | 2026-08-18 04:59:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4f97362-83ed-33c0-a132-f418ef8440a5 | -20.29418 | -46.47673 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 697fb138-e3e5-3051-95a4-c5dd999b0c12 | -14.18976 | -52.92906 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0890ee27-f8cb-3e1d-952b-9e9eab3a9c56 | -16.57279 | -51.61997 | 2026-08-18 04:59:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5be60c68-e8fa-374e-bf72-cac06272840a | -14.4497 | -51.82581 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 039e8eac-c3ea-38d9-b716-e62467fdc4e3 | -14.35808 | -51.93282 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bcbebaa-599f-3348-ae9e-851fb0fd37fd | -13.4235 | -57.07165 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11a74042-0684-3415-91dc-b102b5e0acad | -17.3238 | -54.93318 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3cb9ba4-99ea-3937-86d8-45f367a76f77 | -14.44615 | -51.82525 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797bd712-09cd-3797-af39-c5a205665fb6 | -14.17786 | -52.93867 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2f5d6c4a-c087-3346-bc7e-04b304723111 | -14.83959 | -46.64415 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab47e939-0d9d-389e-be42-24c1a50aa625 | -15.30387 | -56.439 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad278951-2c80-35d2-95e0-e9bb7d94f7d4 | -14.43174 | -51.8983 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa521034-c076-3573-a78f-e426bf322b4c | -14.17732 | -52.9194 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d771a9b0-2f55-3aa4-8c9e-01aa61e1255f | -14.17618 | -52.92692 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4e605f97-1838-3781-81e4-c756baee8599 | -14.42881 | -51.89368 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34b8a1d0-7b48-36a5-bb85-2a8864b6304a | -16.28776 | -53.16896 | 2026-08-18 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a41ac4-c20b-3c8e-85b2-f17b3942f475 | -14.83466 | -46.6436 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea37d38-956a-3e4c-8b63-65e5efc2b4b0 | -20.29382 | -46.48013 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6b12bcb-4e1f-3fff-9df7-cf54271e3d73 | -14.17223 | -52.90714 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5b0d1f3f-1bb5-3725-8f09-f10adb466274 | -17.98269 | -44.43963 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17771601-b5b6-39fe-8412-1daa9df5dce7 | -16.06028 | -56.53414 | 2026-08-18 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 657b4857-0e7c-3b3e-9688-5a33bed2f9f6 | -16.04864 | -56.52058 | 2026-08-18 04:59:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9437ebd3-2ab6-3fd4-96fe-79279d266a92 | -14.26214 | -51.92326 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7194db9-a6a7-3e73-a065-b70f16935bb6 | -15.30725 | -56.43958 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca37c150-c18b-365f-a536-667efa38db73 | -14.45171 | -52.95716 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7506d18-b8c8-3e1d-a60b-e91113f1843e | -14.49988 | -45.67395 | 2026-08-18 04:59:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1accd13f-3fbb-3219-b740-3ce44b962831 | -15.26497 | -52.8997 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 529da4c8-70dc-3028-8080-9436187c2207 | -13.41221 | -57.04978 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57645f16-09f7-367e-8215-4246ded65213 | -17.8207 | -52.02248 | 2026-08-18 04:59:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa185acb-58f2-3464-b078-b8163dcfe4a5 | -16.32461 | -55.38924 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b5a6623-5c51-3a7f-8e05-9ca03cde97f0 | -14.45912 | -51.83565 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79bd619e-e157-3e00-86b8-154723750e83 | -14.18296 | -52.928 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2517c460-4fe6-3cc2-9b9a-d558951e55dc | -12.23391 | -61.95102 | 2026-08-18 04:59:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a0b9ba1-f872-3bf7-ba89-c9feb22aca5d | -14.27096 | -51.91218 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09c25c8a-375f-3caa-be7f-057a6897fa80 | -15.92692 | -55.53968 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f0bc8e5-5ace-3e89-a4fe-b8945765be98 | -14.0336 | -53.67667 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9494d40a-7b65-3356-9c1a-b033f561ee8d | -14.26037 | -51.93542 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e4c5fcc-4541-3941-ac6c-7bf808c5d260 | -14.30959 | -53.04288 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94f04b3b-87cc-3bc5-ac3d-7e1ff980bfdf | -12.75707 | -59.76863 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e36f101d-0499-33e1-afa6-ec9f9e0b2419 | -16.24099 | -57.65962 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6361ecb9-95f4-33e2-88b1-fdde680b41b1 | -15.77919 | -55.56955 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc53f75d-48bf-31f9-b82c-c3ac9a074b2b | -15.91903 | -56.47894 | 2026-08-18 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b5ef889-7dbf-3c3d-b01f-d2609133f671 | -14.45557 | -51.83515 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bee3193a-08ea-33d3-946c-104e5fb7b2f3 | -14.35573 | -51.92418 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62187714-f767-32c0-bd41-d9400d448225 | -17.3382 | -54.92823 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 910feb34-f76a-353a-8e79-4fac841a7395 | -13.43053 | -57.07286 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c7a52ee-1b7b-3e66-a9df-9c11f83e7377 | -15.24902 | -56.49122 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e629893a-a7bf-3d04-91f5-d545f66f3a0b | -16.57217 | -51.62441 | 2026-08-18 04:59:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78a157a9-bcc6-3c97-b861-b25e62d0be29 | -14.83355 | -46.65296 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b83a20e-9fbd-3f71-b75a-0804b0b228e4 | -15.06479 | -48.71674 | 2026-08-18 04:59:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58e91b12-9397-3d53-afca-857568b8d8fe | -14.80598 | -46.65879 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 46775c65-992a-38c2-9915-c577d9505939 | -13.94542 | -53.91565 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b2e8189-9824-3f7d-ae0e-93a588070759 | -20.29357 | -46.46486 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dec62ec8-4e2b-36db-a1d0-a45c3cfc2efd | -14.16883 | -52.90662 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fafb2ed-0cfb-3b2c-9496-eef407379353 | -13.26695 | -54.23822 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be58bb07-3dc5-35b2-9aca-3ed7ba82a0d0 | -17.10424 | -46.56625 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0977de0d-6cd1-3e21-baa5-fb4013bc4e09 | -15.31125 | -56.43642 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20e40303-8471-3426-9740-01408cccd5ec | -14.44664 | -53.08263 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 418a123b-f9f7-3483-855f-b9ba1d679e0a | -15.91467 | -55.55223 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c60c5c7-ebb7-3f53-bcef-d5a8ad38318a | -16.23537 | -57.65019 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c0994deb-f004-3949-a99d-12d86d5ed915 | -14.18636 | -52.92853 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0b0cbc18-1c6c-3410-8b19-2a0e4501a152 | -14.18411 | -52.92047 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a984cb74-8afc-38d7-aa19-5f66aee0891d | -14.16317 | -52.92102 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 99128d60-8c4e-3107-b87c-8c6a06f00fc3 | -15.81656 | -54.19312 | 2026-08-18 04:59:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee85042b-92b6-38de-aa4e-cfbf9d2eff6b | -13.4396 | -57.06203 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0f5ea77-0910-36c8-a1b3-eaf219e0f422 | -20.30276 | -46.48112 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee4379ee-ed2d-3dc2-b103-35205241f176 | -13.01772 | -56.59063 | 2026-08-18 04:59:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62550b5a-82f1-36e2-81da-0b6445b1af4b | -14.63061 | -54.46209 | 2026-08-18 04:59:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02336638-3289-3b92-b30c-25d35b591fc0 | -15.07232 | -48.7259 | 2026-08-18 04:59:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44f181f2-0d41-3670-b0aa-dfe9e1c78f05 | -15.88914 | -55.56258 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
