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
| 6cdbe1c1-b491-318c-b1ca-58f45e565b66 | -11.9277 | -58.07367 | 2026-04-15 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92ec37d0-ef3b-34f2-bfc2-594d27c6f763 | -16.24889 | -60.0304 | 2026-04-15 05:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 946a518e-8371-3b31-b1d8-a0f86e49bdbc | -11.43131 | -55.10012 | 2026-04-15 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80a429b1-bbdd-336c-b45c-015f8199574c | -16.59226 | -58.21756 | 2026-04-15 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1184d0ba-0c33-3c95-b01d-d650678d5768 | -11.93351 | -58.06689 | 2026-04-15 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8435f10-8aad-315c-aa4b-817424401048 | -11.43177 | -55.09644 | 2026-04-15 05:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841acc11-23ea-3b6e-b6b2-d6bd878fd2e5 | -21.88741 | -56.26465 | 2026-04-15 05:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 722ff385-3dfb-386c-9fa6-16b5c12ea12e | -18.50816 | -55.52256 | 2026-04-15 05:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 88c2628b-b80f-3473-bb1a-c024fd6eca15 | -18.50858 | -55.51814 | 2026-04-15 05:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c2d596e3-6351-312b-b9b9-7b8a60c66da4 | -21.88702 | -56.26899 | 2026-04-15 05:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f8817d8-efea-35f4-88cc-205c85056d10 | -20.32845 | -55.00126 | 2026-04-15 05:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60ad94da-0913-3e73-8a54-cd26f61c4914 | -21.69568 | -56.31096 | 2026-04-15 05:42:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec1fb8d-953a-3190-9d72-b9d34f76a6d5 | -20.32174 | -55.00615 | 2026-04-15 05:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21638305-fc1b-3161-a252-c52a43ae7949 | -20.32797 | -55.00648 | 2026-04-15 05:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a74893-bed4-3067-9768-5cf3e3e1a9b8 | -20.3222 | -55.00098 | 2026-04-15 05:42:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463194ef-7596-3582-aafc-ae64c903c245 | -20.22584 | -46.46712 | 2026-04-15 06:10:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 968b93d9-f638-3386-9fa0-29c16753e8cc | -20.53956 | -49.49084 | 2026-04-15 06:10:00 | AQUA_M-M | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2e0ff589-3e62-396d-bd22-e5b2531d5a7e | -11.79176 | -43.61896 | 2026-04-15 06:10:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1bdafebd-36ee-3977-9ddb-a31fc1fbb356 | -11.78299 | -43.61763 | 2026-04-15 06:10:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d1f6dbdf-dd42-32fe-b6af-9b4526b66448 | -12.84832 | -50.57774 | 2026-04-15 06:10:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 900ebd3e-a9e7-3db8-b747-8dcf95d30bf2 | -11.79042 | -43.62787 | 2026-04-15 06:10:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9d4adcb4-d3be-3f9f-8c4a-2929ca3ec830 | 2.56869 | -60.54849 | 2026-04-15 06:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 16cdf6a1-df9d-3fbd-99cc-49f6a5c87c01 | 2.56983 | -60.55526 | 2026-04-15 06:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ef42e86-fd53-3068-ae32-05ab761887e4 | 2.94751 | -60.16905 | 2026-04-15 07:41:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 52eabdc6-f6e2-3976-90a8-0d5d1bd2b628 | 2.5679 | -60.551 | 2026-04-15 07:41:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 166cb094-90ef-34a8-a748-3d9a53983286 | -9.01782 | -46.11408 | 2026-04-15 12:21:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 33b4b1bb-a98f-3155-9117-d3709cd33745 | -11.6015 | -55.33075 | 2026-04-15 12:23:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 143f9f1f-a9fb-36f9-a335-d7f142a8b235 | -12.34743 | -43.45401 | 2026-04-15 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3452be07-ae1d-3e61-8d3c-15bb5884fc4b | -13.66856 | -52.93751 | 2026-04-15 12:23:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6d05f589-d45a-3578-a5bc-4b69f38bafc9 | -12.00642 | -45.35777 | 2026-04-15 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| dfdbe02b-acb0-379d-8388-93b96cf1be0a | -13.24721 | -54.86645 | 2026-04-15 12:23:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 28de2657-a729-3c44-97cb-d54f6727e820 | -12.00836 | -45.35271 | 2026-04-15 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1c4c4178-ba52-3c56-85cb-68e9079d116c | -12.90806 | -54.66124 | 2026-04-15 12:23:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6cdd0f15-4883-3a0b-b01f-0ecc870068d7 | -9.01167 | -46.11892 | 2026-04-15 12:23:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| eac896bb-3545-3358-9a46-809fae3019e1 | -12.34648 | -43.44723 | 2026-04-15 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c2d66378-96ce-3d22-ae30-b0394749d5fd | -12.05517 | -45.33307 | 2026-04-15 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 76455035-b21c-3ad0-9d1b-0cbd02de12bd | -11.30412 | -54.71878 | 2026-04-15 12:23:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 565b9cc2-8cc8-3acc-9913-41593e45707f | -12.99739 | -54.68089 | 2026-04-15 12:23:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 295334d2-daa2-34c4-b9a5-5921f2e285c7 | -11.1858 | -46.5745 | 2026-04-15 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 059f72b2-7ea6-3d42-accc-14135c7e1022 | -11.17229 | -46.57228 | 2026-04-15 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 320299e9-2cd9-3b57-9f7c-829ae9d10055 | -18.31657 | -51.73149 | 2026-04-15 12:25:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1cd929ca-9eb1-39b9-80d8-37d84f80f264 | -20.08083 | -50.62285 | 2026-04-15 12:27:00 | TERRA_M-T | PARANAPUÃ | SÃO PAULO | Brasil | 3535903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 2a60083b-3d0b-33e1-b7a9-8475596fbf8a | -20.16283 | -46.7385 | 2026-04-15 12:27:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 30.2 |
| e0c2dacb-a8c5-39b3-8a90-61bf16be8085 | -21.20701 | -49.30049 | 2026-04-15 12:27:00 | TERRA_M-T | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 91676e5d-639c-3219-9690-37035ad06f0b | -20.08266 | -50.60723 | 2026-04-15 12:27:00 | TERRA_M-T | PARANAPUÃ | SÃO PAULO | Brasil | 3535903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 19ae2936-5bb1-310c-9764-d0318a4b725f | -19.2735 | -55.14625 | 2026-04-15 12:27:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 229d1a58-37e2-32e3-a774-26bcbac5393d | -20.18911 | -46.58788 | 2026-04-15 12:27:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 27.6 |
| c07c9ca5-a299-3edf-be10-196cf4c697c3 | -20.32515 | -55.00009 | 2026-04-15 12:27:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 75a3ebde-813c-3f1e-9741-4cbf758a8629 | -20.59365 | -48.95719 | 2026-04-15 12:27:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| af0cd789-e5ab-3c86-a2bc-95eeb87b2d1e | -20.2261 | -50.74811 | 2026-04-15 12:27:00 | TERRA_M-T | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 7ed4573d-44a9-3292-9ec2-cde02160ad7d | -20.32648 | -54.99055 | 2026-04-15 12:27:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 148fb603-4394-3f9e-9498-25ae5b2c03b7 | -22.96196 | -52.69533 | 2026-04-15 12:27:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 95177667-00fc-3b59-89c0-73219a558eb9 | -21.6177 | -51.15956 | 2026-04-15 12:27:00 | TERRA_M-T | FLÓRIDA PAULISTA | SÃO PAULO | Brasil | 3516002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 82789316-f693-36ad-b6ad-3f5a2de844ae | -22.96045 | -52.70817 | 2026-04-15 12:27:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| c6960936-3478-3755-a9cb-e00471e65e3e | -20.19262 | -46.58315 | 2026-04-15 12:27:00 | TERRA_M-T | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6fb5a605-8353-3a03-bf05-800313bfd8a1 | -11.1479 | -46.5671 | 2026-04-15 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8c9a5e12-c193-3e38-bafc-981eca71603e | -18.5129 | -51.6003 | 2026-04-15 13:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 680bd753-6275-3712-a2e4-223f75b28dc6 | -11.1479 | -46.5671 | 2026-04-15 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bd85358b-422f-3304-9633-47660099ce4e | -18.5129 | -51.6003 | 2026-04-15 13:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f2d5266f-2831-37f7-b365-e6755ae740f9 | -11.1479 | -46.5671 | 2026-04-15 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 1556e8c6-1751-3c80-8baf-070f02f5f786 | -18.5129 | -51.6003 | 2026-04-15 13:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5cbd1d14-1406-38b1-be11-3e73793b5fbe | -11.1479 | -46.5671 | 2026-04-15 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 103833a6-4875-33ad-8b04-e4a8a6311485 | -18.4929 | -51.6038 | 2026-04-15 13:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ad174b45-e9d1-3101-b85d-da1e1898b1e0 | -18.5129 | -51.6003 | 2026-04-15 13:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5c7a7575-494d-3549-8af0-7775f3f40258 | -11.1479 | -46.5671 | 2026-04-15 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 256.0 |
| 78a9daea-df6b-30ca-92b0-b3d0012919a2 | -18.5129 | -51.6003 | 2026-04-15 13:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 45164439-d822-3f52-a8f3-fa790256c2cd | -18.4929 | -51.6038 | 2026-04-15 13:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1532b720-c480-38a7-95dc-22a636069813 | -11.1479 | -46.5671 | 2026-04-15 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 52fd832d-4b6c-385e-a190-da93a234a67a | -11.167 | -46.5646 | 2026-04-15 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |


