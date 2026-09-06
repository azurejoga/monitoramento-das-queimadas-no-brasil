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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 556e41a3-1276-36f8-ac0c-0db2bf992daf | -5.14816 | -55.96582 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca8b70ff-6171-3c7b-b1b6-a1b42c8b9ecd | -3.21884 | -53.16928 | 2026-09-06 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a3cb925-0768-3180-a6d9-4d527423066d | -5.25171 | -59.98396 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9221db31-6b52-37af-801f-07fa3629209c | -13.79571 | -51.63786 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62755606-3773-3590-b9fd-8ed848795913 | -5.14365 | -55.95052 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b82b28d-6e00-30f3-b840-bccc3136b8a7 | -6.48753 | -57.8779 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd19dfe1-d39e-3ca5-a023-91c6a32f7cd0 | -15.09314 | -52.52279 | 2026-09-06 05:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28cbace6-0557-3c4b-876a-00a5547f712c | -1.39216 | -55.18153 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82179d8a-90c4-3661-b4a3-a15f971e9721 | -6.64077 | -59.44569 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d149e93-2dda-351a-aa2f-aa825e0d8f4d | -4.67592 | -55.63303 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff97d786-0838-3c40-81d2-c976f4147be6 | -4.90153 | -55.81795 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 126fb373-7195-3fff-90d4-a9189b62f37d | -7.09645 | -56.51468 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fee76190-20d0-313a-81b0-a7f510d827b3 | -5.35952 | -56.01979 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3cc556bb-1a59-3b39-9e3b-f8bfb1f7406c | -1.39383 | -55.17091 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d1e642b-b9f8-3477-9c81-e8405986c830 | -4.77377 | -56.1181 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06384dcd-d052-38c0-96f1-e57fff48828b | -3.81197 | -55.88865 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9132d3c8-6fde-3343-b4da-f5f41f4a68d2 | -5.25235 | -59.97994 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6f136c-e66e-3c2c-a17c-4b2333b58c3f | -5.36404 | -56.03508 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85e2d838-a845-3bb1-ac8c-098f84ded6a4 | -5.36237 | -56.04576 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92f50c29-24a4-3966-a577-5b73f48bfffe | -6.12938 | -57.74937 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e3c33ba-dc68-3468-adaf-abc1d54fd017 | -4.35439 | -55.03031 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74f42f57-06bc-3f9e-b5c5-c6b57f8c5e90 | -8.49925 | -54.65051 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c20a5e65-516c-3eaa-a73a-865a19b1979f | -6.00237 | -57.78287 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c420ffc0-b8d0-3bad-bb4c-d6f26b922033 | -1.62153 | -55.16588 | 2026-09-06 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472ed865-1f62-3191-b39a-7ab3801511d5 | -3.08861 | -59.14298 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4772f0a-85b7-38f3-86ad-93fa637ac8be | -4.9167 | -55.80935 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7c0b79-22fb-3faf-8aa7-2e4b7fbcfa7d | -5.30411 | -56.01148 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf322bd0-dd06-37ca-a69c-60001ffe4950 | -5.44313 | -60.11705 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba970ab1-7993-3705-8073-1a1b13b368fb | -7.10317 | -56.51571 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35433f71-667b-3726-9337-d5514ac5accd | -6.95666 | -59.73132 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68191923-2dde-39f3-946b-dead91045542 | -5.15489 | -55.96688 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50e4e7d0-09d4-3fc7-96ec-926244900082 | -4.66915 | -55.63197 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d505e9b-735e-3eb5-987f-17f1b343ad5d | -7.8959 | -47.69926 | 2026-09-06 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b20029f-1451-3224-a97e-4ba3a9648a4e | -5.17297 | -56.0496 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbf2d059-881c-3c5f-8cb7-1987e8c18836 | -4.97792 | -56.00093 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05a650d1-398e-30b4-b961-8d3317427509 | -5.34721 | -56.03247 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 894e0084-9000-3c96-b8be-ff8254ee3823 | -4.36156 | -47.77811 | 2026-09-06 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2095ecf9-4b86-3e6a-9559-f7dd6cc4a9fe | -5.35956 | -56.04168 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b6c131b-9320-35c6-8f1f-84fd83eaa82c | -5.34225 | -56.032 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79743546-ef8c-32bc-b410-4ae1831b46ac | -5.83508 | -60.25612 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e4bff0d-40db-3722-b175-023b3ae85ea0 | -6.06397 | -57.796 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d96886-fb4e-3b05-8aab-8c88961e8a98 | -2.86628 | -50.45807 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52813b11-97e0-31c7-89be-f9919cab5bd2 | -1.56478 | -55.78483 | 2026-09-06 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f9fb6c-34ae-3068-a09b-a9e617ac0055 | -2.86559 | -50.46056 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3134ba6b-d808-3eb3-9bd3-8af4985b93ff | -6.06176 | -57.78852 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c7e6399-425f-38e0-9952-955cfe9b5f58 | -5.14872 | -55.96226 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36d31df1-1f7f-37a1-89d4-5df3b539bbe4 | -1.49346 | -54.82442 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fbefc25-9954-33a4-a872-7810f75bb551 | -7.10036 | -56.51165 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084ea94b-7a5a-3df4-a81a-8d4dc4e2ca69 | -5.84903 | -52.04548 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dac063c5-c839-3026-962f-73c4ac611bc7 | -2.86496 | -50.46642 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7b06b5-a5ea-3414-af19-9c9722e4c2ea | -5.25455 | -59.97898 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 946bd0f6-b5c2-3391-9008-600d0501fe79 | -5.35675 | -56.03759 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8d213df-7fc2-3eb4-a0be-9889c1e63f9e | -2.45651 | -57.91857 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f33a921d-a509-3531-9aa4-8178f60336ad | -5.33889 | -56.03148 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c98c006e-a47b-31dd-a101-609cc89ff662 | -5.16736 | -56.04147 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c090b68e-630b-31b1-b759-4ae0bca4e9be | -5.35394 | -56.03351 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b31ed67-7b25-3ace-a361-f1a0dc3108d3 | -7.09925 | -56.51874 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be5d3ac8-6e55-3148-9624-523955bf9586 | -6.87039 | -55.61223 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c145b6a-9a77-3e4e-80fd-5d3d0db463da | -5.97685 | -57.68622 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf54f34-82dd-3c93-8507-6c544c1ef36f | -2.92025 | -60.99484 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19ffd9e2-e604-3ef2-ba19-ef7556c8caff | -4.28892 | -59.95907 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd16e0bc-0be4-3a44-b64d-bbb0388a20fa | -15.49117 | -50.36404 | 2026-09-06 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 283f10b0-af87-3a8a-9265-28dd31b69732 | -5.36012 | -56.03812 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 141bffe3-a11f-347b-b941-7d30e767037b | -6.09308 | -55.58732 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bacc9e13-2752-35e8-a5bb-70fa27ef36d7 | -6.12994 | -57.7459 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07e9efac-b72c-38bf-aaa0-cd0eab2b1657 | -7.34547 | -55.21844 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9a2093-d69d-3d59-8462-793a90da4f18 | -2.71315 | -59.76537 | 2026-09-06 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b33143d-0fe1-387e-bf6f-74caa389a3a4 | -3.90363 | -55.88508 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89d67efe-9a6a-350d-8b27-25bfddf103bd | -5.92112 | -47.89151 | 2026-09-06 05:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39ae8185-1ea8-3662-bb19-57cee4c4f447 | -6.44341 | -58.15369 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0094f3e-4021-3576-9dda-8f4832e840f9 | -3.14151 | -60.64471 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d799fd9-9e6f-3c1c-b6f6-c35458806947 | -3.54502 | -48.18164 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d7a224a-000e-3ce4-bfdd-b7d8cc837971 | -5.28776 | -60.13407 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a33c936-3a32-33d6-a98f-f41d33956b08 | -3.23435 | -50.57243 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d00f2930-49c3-3ef3-829f-917c5e4eab44 | -4.67986 | -55.63001 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 597052b5-4d64-39d0-8ab3-80439657e8b0 | -5.34832 | -56.02536 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e48490ca-8a45-3d6f-b282-752359375bb8 | -5.36345 | -56.01675 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 50869d8f-65e6-3c2c-b2eb-2e75100d547b | -3.9391 | -48.4454 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 906dbefc-25d9-3dea-8e50-780834e86fc6 | -5.25521 | -59.97498 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cd969c70-bfde-3b55-aaf9-737121cc13fb | -3.17189 | -61.14637 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fac236a7-c50e-3421-bc8d-cf721bc732b4 | -7.10988 | -56.51677 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ba2c191-4bcc-3172-a11c-fc91d90d21e0 | -5.6556 | -60.23974 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bea940f6-8102-3637-bcee-a205fa390c8e | -2.76821 | -48.57391 | 2026-09-06 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3b6b977-bac6-3999-b06a-e212fa970b1b | -6.56934 | -58.56837 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c9d5e53-0649-304e-bdf5-2210a0544831 | -6.95195 | -59.73834 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446cab4a-9ad6-335e-9640-14bd5eb67b3c | -4.47111 | -55.08998 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ec09b76-dfff-3811-ad8a-50a2ab812ccb | -2.86496 | -50.46475 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb88ef28-e56b-359d-b3db-cbe5e9d68903 | -6.95603 | -59.73512 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55f29d8c-d0d3-3430-bb4e-e61c51787a00 | -6.51897 | -58.29531 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6d9cbf0-553c-3d84-b637-532c119d8d8f | -2.8619 | -50.45739 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6200d9b7-edc3-3bbd-a89e-ae4cb598e2a7 | -4.11461 | -49.08314 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 239a3694-dc48-3fdc-805a-55da90ac2942 | -4.35055 | -48.97379 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65c624f3-a980-3c00-8641-f336a1133f6c | -1.49036 | -54.24813 | 2026-09-06 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f1b220d-ee18-3ecd-a47d-2fc2fdea845b | -13.82088 | -51.6674 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e34b1455-8be4-3df4-aa67-202ac6025f4b | -3.55064 | -48.17945 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aab39e42-ed25-3c5f-92be-e872b83f0279 | -3.11277 | -60.6541 | 2026-09-06 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee3822d1-7877-37fe-bee9-8ff05c413bf5 | -5.5955 | -60.23988 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbf3ac08-2ca1-3f9b-86f5-301dbdeab9cf | -5.38293 | -55.91373 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 297484e3-a92b-357f-8c32-937d8c10bb2a | -3.93953 | -48.44246 | 2026-09-06 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ae29dba-f200-38c8-b619-1913700bcfb7 | -4.47513 | -55.0868 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
