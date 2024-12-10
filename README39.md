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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03ab1444-59ca-321f-8de2-4b4f61232621 | -3.11109 | -54.0781 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 926a8d15-68e9-3b2c-95f1-efa1569370f3 | -12.5617 | -58.3347 | 2024-12-10 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 0a89f6f4-d6f5-326a-a10d-2ff9a2e86311 | -4.3959 | -47.7618 | 2024-12-10 05:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 864c910f-31f6-30d7-8619-1940f6c03895 | -12.5427 | -58.3362 | 2024-12-10 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a5a721aa-fd75-38e6-899f-637f31ac3da2 | -12.5615 | -58.3546 | 2024-12-10 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 33ba79bf-a2cf-3ef1-913b-61df5e71db71 | -12.5425 | -58.3561 | 2024-12-10 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 81b3b426-eff8-32f0-b8ce-c48591954d5b | -9.14651 | -62.72251 | 2024-12-10 05:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baeab9f0-b85a-32ad-9b5f-0b6e0dec0f7a | -12.36903 | -54.17122 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89fe80b-7ca3-3607-b795-9d7335b74d86 | -9.96314 | -65.04499 | 2024-12-10 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1bf271-012d-36d6-ba8f-37e278fcc488 | -11.65793 | -58.26948 | 2024-12-10 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe8efe24-85f9-3269-927f-24bd5d618369 | -12.37679 | -54.16065 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3ac7841-4630-342e-abc3-cb2f696c112d | -12.36846 | -54.17408 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52ac9834-f52d-33ef-867f-04aa39d7fd27 | -12.3691 | -54.16861 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3dbde48-5d23-387a-bf00-197b5d82f75c | -12.36252 | -54.17051 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38db588a-a17d-3bcc-9cb2-a8062203b490 | -8.57506 | -63.42659 | 2024-12-10 05:40:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b6afd1-da14-3a9a-8e4c-d312bd272ee1 | -12.36192 | -54.17597 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb5c8d41-b491-3d59-a6ce-ba3d82360b4c | -11.82731 | -57.82507 | 2024-12-10 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6277d016-1bf7-31ed-a56e-09901797f0a9 | -11.82769 | -57.82204 | 2024-12-10 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3459554a-790d-35a5-8e4e-7c592c193fb8 | -12.36195 | -54.17341 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d453199-98b9-35e4-bdef-66eea869a2f5 | -12.16228 | -55.17728 | 2024-12-10 05:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5628cfcd-3830-3af0-9855-71c3719e7354 | -12.16282 | -55.17262 | 2024-12-10 05:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff32740-173c-36be-bab0-039cf1a154b8 | -11.41548 | -54.32204 | 2024-12-10 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cffd9ab5-788b-301b-b191-8e7f348b87a0 | -11.78117 | -55.13164 | 2024-12-10 05:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53784c00-ae5d-38b2-97de-d82f1880288a | -11.65718 | -58.27506 | 2024-12-10 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eac15866-7d90-3132-97c0-5fe142a52736 | -12.36976 | -54.16299 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4e87019-0b1d-3d6b-9f8e-f15598bef599 | -12.37617 | -54.16626 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 669632b0-579e-36ed-b403-1632a9348c1e | -11.65941 | -58.27153 | 2024-12-10 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52131044-a279-3f05-b8e0-ad0eba895093 | -12.36965 | -54.16565 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b3ff9db-0cf4-3cda-86ad-6dbb7a04e9db | -12.37628 | -54.16361 | 2024-12-10 05:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 361f70ce-6421-382c-997e-167979408d2f | -12.15672 | -55.17191 | 2024-12-10 05:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eef2e800-26f3-3dbe-99fe-43bfbd80f059 | -9.3958 | -62.57784 | 2024-12-10 05:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd200d5e-f6bd-354b-b3aa-b82d8a319a9f | -9.39643 | -62.57361 | 2024-12-10 05:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dadfd3ca-6e3d-3984-a7d6-77c7295933c2 | -11.41488 | -54.32721 | 2024-12-10 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87d83833-0455-3293-9720-658d1510be35 | -9.20421 | -62.43475 | 2024-12-10 05:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe73ab50-16f0-39ee-9578-f5c8bfe87225 | -12.53291 | -57.72573 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01efd6e4-4b22-34a0-b600-89116456e41f | -12.56305 | -58.37182 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70e77c69-ac09-3b66-9ede-57d1acaf6a84 | -12.56087 | -57.71315 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f8769db-8880-325a-bc95-9e5508cd9f2d | -14.14119 | -60.18807 | 2024-12-10 05:42:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca6fb8ac-1e65-31dd-a206-8ba243572f6c | -15.08891 | -59.63121 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 905f7a61-baab-3705-a417-53973452d9c7 | -15.06621 | -59.65935 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d94fd5f6-9eff-373b-9e8e-71dd59590bf9 | -12.54039 | -58.35144 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 06ad7698-0d81-3173-ac42-adf749aae416 | -15.093 | -59.63686 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7130cfb-c752-3f08-8443-b35838cdfb39 | -12.92117 | -55.73529 | 2024-12-10 05:42:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3d49e2-0291-3db0-8f5d-b5b7669e2316 | -15.08827 | -59.63631 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0a93ac3-06dd-3c44-90a7-2dd724d79044 | -12.71411 | -54.97715 | 2024-12-10 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 475d5f42-759d-324a-9025-a4bb14e55bd5 | -12.55917 | -57.7677 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e97cc058-f1b0-30cd-bbab-7182899383f8 | -12.04836 | -62.78811 | 2024-12-10 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 545d9597-38e8-393e-ab35-5e36f0786788 | -12.56475 | -57.76519 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48da7fa8-81da-39dd-8447-1a65fbfd5ba4 | -12.5361 | -57.74228 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 403e215d-97db-3d41-a33b-ed74822da78f | -12.05142 | -62.79311 | 2024-12-10 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7179b7c-deb9-3b14-8c54-2072a7d643f0 | -12.56379 | -58.3661 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| da542821-9324-3c2b-b6db-70d2870fc90f | -12.56076 | -57.76916 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70cee6c6-5afc-36e3-ae46-67d49530ce0f | -15.06685 | -59.65425 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2092c9c-c2ac-3114-aaea-296803014a37 | -15.06748 | -59.64915 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 980c1638-a66f-3791-862f-2d1a42a8b208 | -12.91524 | -55.73448 | 2024-12-10 05:42:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c3f363-13a0-3f0b-9378-33303812ce91 | -12.54112 | -58.34565 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b20d9303-aa4a-3998-a6cd-1e26d854e7cb | -15.61492 | -59.74575 | 2024-12-10 05:42:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d7fd029-295a-3c37-abef-99a5626b8731 | -12.53852 | -57.72306 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06be1568-fbf5-3cff-b2a7-21b60b94828e | -15.08957 | -59.62603 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 908ca7fd-701f-31ea-9cba-9021d1586d52 | -12.54463 | -58.35789 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8e869de5-f565-30f3-9e6d-8f9fbae3d765 | -15.08419 | -59.63059 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cfd8b43-e1ef-3583-9f4f-ffb29d543462 | -15.1633 | -56.4755 | 2024-12-10 05:42:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc5f7141-655d-3f7f-8629-1d12cb4f8d52 | -15.16381 | -56.47535 | 2024-12-10 05:42:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a9e233b-4717-3cc3-9a45-1ff455037886 | -12.53689 | -57.73599 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6ecad50-90c9-3bf2-aad7-fa9e6af21cfd | -12.5377 | -57.72953 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 040cadbc-75df-386c-8ce9-e5b86d30c5e4 | -12.5603 | -58.35384 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 470c1346-b327-3c31-b9ee-bddad4611c6b | -12.55607 | -58.34741 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d90fdb70-10e2-378d-a839-d25c698fe0ce | -12.54185 | -58.33993 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7a59a4a5-69a1-3c91-b9f4-5aeec077e7cc | -12.04773 | -62.79256 | 2024-12-10 05:42:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2327787-d0e3-3845-b52f-563d2ca886fa | -12.53811 | -57.72629 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc044cee-f56b-37b5-b38d-2dd5539c3382 | -12.54536 | -58.35212 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0f35eb95-10c4-34dc-95a1-94d7c04534a5 | -12.55311 | -58.37058 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e57b1ce6-c430-3cae-9399-9c5bbd5d9cba | -12.56593 | -57.76986 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f03716bb-ab5e-379a-92a6-c7ecc94d7a64 | -12.85708 | -58.21919 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d952411-335d-373a-9850-015eb6024dac | -12.5439 | -58.36361 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 01df1a43-4b59-3aab-b49d-b74988d8d0a9 | -12.55881 | -58.36551 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84eafbbd-3592-35df-970b-b025d560123c | -12.56434 | -57.76839 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08ad7c73-3db1-30ec-a716-ae1433b1b54b | -12.91036 | -55.05534 | 2024-12-10 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b60c26d6-f391-38b6-89ab-d92a9882bb4b | -12.5715 | -57.76734 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a1f558b-ca40-3634-988d-e97a56273c09 | -12.53649 | -57.73915 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73936bad-ed53-37de-b494-4123ea64cf11 | -12.90418 | -55.05442 | 2024-12-10 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 593f829d-34b5-3ac0-87d4-dc7d6445c705 | -12.22255 | -64.26658 | 2024-12-10 05:42:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ead17aa-e6d2-39b1-8620-0b45fee1a726 | -15.07948 | -59.62994 | 2024-12-10 05:42:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b2d2dc7-cfbc-311c-8c96-b731a3d5fa15 | -12.56115 | -57.76597 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5f571b02-7e83-38b3-9a8a-bbdd443b3564 | -12.5312 | -58.34418 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 141c9587-f305-3b1c-bb6f-528dcceea28e | -15.16284 | -56.47986 | 2024-12-10 05:42:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbc2cef0-346a-39bb-9576-c59a5ea2bebd | -12.85744 | -58.21625 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9157185-6468-395b-beb4-8fa935e7e61f | -12.90485 | -55.05642 | 2024-12-10 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a43e016d-7631-3c3b-b64e-bb52426b1161 | -12.56632 | -57.76667 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfebfa5b-e067-3af4-9696-0702602eb9eb | -12.56453 | -58.36029 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b134dca-6598-3bea-94cb-07715a4fc45c | -12.56047 | -57.71631 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1adeae6f-7a2b-3116-ab03-8db84e3b38b2 | -15.25848 | -53.57692 | 2024-12-10 05:42:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ed1f32a-14fc-3e15-8baf-7c7e41c39936 | -15.16331 | -56.47969 | 2024-12-10 05:42:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d1d5643-0338-31b4-9fa6-b09bd5eca33a | -12.56153 | -57.76278 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5fdab957-bf59-3e34-97bc-1c444d0d6233 | -12.55532 | -58.35325 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2f258b05-00ca-359c-a04f-099e098bc092 | -12.70847 | -54.97128 | 2024-12-10 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5a466de-fd09-39ad-9f0a-734f3bc4ed43 | -12.55182 | -58.34108 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 66cf7368-5bbd-376d-8c98-ad88fbcf911c | -12.54887 | -58.36428 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c16c367-131b-3bac-833e-ed5ca576c22f | -12.85672 | -58.2221 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e00054d-d470-3bff-8193-d93dd9dda02f | -12.54129 | -57.74284 | 2024-12-10 05:42:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README40.md)
