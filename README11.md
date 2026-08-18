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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed40d5bc-9af5-3a30-ab55-7434cfb63e23 | -7.81573 | -44.59905 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c8cb56c-66b6-38f8-8155-f253d5a35c7f | -3.68371 | -47.65178 | 2026-08-18 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ef38fb7-6cca-35ce-93db-4d9cab463cea | -8.32898 | -46.48236 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e3fc577c-9f8b-3d56-8cdd-dddf1af15868 | -3.43019 | -51.51854 | 2026-08-18 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c428d47e-c74b-302b-91f9-1df5c368de71 | -8.3354 | -46.47079 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| efb70152-15ad-3d78-8eef-7cf92a1040aa | -3.20812 | -49.057 | 2026-08-18 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88518fd0-355f-3e41-bd58-6a2e42eefecc | -4.99305 | -37.10093 | 2026-08-18 04:02:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cbabe144-86c0-32f7-af35-91aaeaf586cb | -9.07463 | -50.8444 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3c4245e4-6cc9-36a8-b7f8-582a4fe9841a | -8.59226 | -50.35019 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0230d810-e7f5-36bf-b177-54d4fa4b3128 | -9.77882 | -46.7202 | 2026-08-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c93ab8f1-815c-3c19-81c3-584833c6f10b | -7.17981 | -43.4196 | 2026-08-18 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa00741f-6486-3ee5-9e34-fc269277cc80 | -7.81417 | -44.60851 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ebbb657-6244-3b22-b132-652ad131d5e0 | -8.48585 | -48.805 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5926f776-af3f-3e70-a5d6-8e8f277f3696 | -7.818 | -44.6091 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e38fff05-4e37-3ba5-bacd-365544eb9e72 | -5.55468 | -43.43103 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ea778e4-2a08-3c5e-af32-39bf5b461690 | -9.79656 | -47.30819 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b53b5a6f-04e1-32e2-bc81-4656929c6fdb | -6.26578 | -43.27607 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fe09b3d-67aa-3793-bc40-a831ce3813f5 | -8.33398 | -46.47898 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76f0794-6a2c-38a0-9c63-2831abffede1 | -7.15668 | -43.15269 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4fea0ce9-c374-3232-9e26-a3cc4aef1d78 | -8.49478 | -48.81278 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07470a3b-d9da-3620-92cd-27305d0dc444 | -6.18329 | -47.81851 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 95559f87-e5f1-3dd0-9fe1-3989d63bfee5 | -4.01544 | -48.90761 | 2026-08-18 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 82bb4660-6c53-396f-9808-e67de89a6404 | -6.184 | -47.7852 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d120943-6a04-38f8-acfc-893192a7e484 | -9.47686 | -51.60355 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa8b581d-51f0-3954-8d1c-21a8a45202df | -9.19595 | -49.96772 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5674a31e-598b-379c-94f8-eb0d29bf04c8 | -7.17619 | -43.41902 | 2026-08-18 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5b13098-780f-373a-9647-05dde9824570 | -5.27127 | -49.04987 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8bdb2de-c4fb-33dc-9a8a-4f309b9d2b65 | -7.16871 | -43.14632 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1034ad23-9fcb-34e9-8186-b27e4dd2c0a6 | -4.4927 | -42.56094 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 520a0780-08e9-334b-9302-59a4c0ef6067 | -3.42448 | -51.51659 | 2026-08-18 04:02:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f599644-9aa7-3c58-be55-2b9a42cf22d1 | -8.36037 | -46.47927 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22c0c8dd-feb1-3bab-b174-2da7224d4c5f | -9.21428 | -50.09528 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b6c1be-365e-37c5-8850-f3bb21f78ab8 | -4.49539 | -42.56029 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80e2c508-2c55-3a5e-880d-42e76cf97ae9 | -9.06833 | -50.84678 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e56de041-af9e-3a7e-8b7e-489e925ef30c | -9.76261 | -46.74273 | 2026-08-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72ac46c8-e933-389f-8304-f12da88384b9 | -7.00356 | -44.83466 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62d5143b-a6c9-34e2-a811-2ae9a2b32809 | -6.53598 | -43.11229 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3699f7b-a447-3063-8f68-952c1b802f93 | -4.49182 | -42.55973 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bef81d0-0343-3110-8596-76d11090541e | -3.67871 | -47.65093 | 2026-08-18 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8ede4e9c-3254-38ba-a14b-7aa141f62bfc | -8.08502 | -44.35661 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9c15685-dc9d-3e7c-8f1c-10b1910e84ba | -9.07212 | -50.8266 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de73dbe8-4f75-3ab0-a0c8-a966568d302d | -8.68484 | -44.30727 | 2026-08-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b9c3c7a-3748-3eae-a87e-4ec70d7359ed | -4.48977 | -42.55631 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bab43125-f63b-3259-bdda-41d92e22fa91 | -4.79259 | -40.04423 | 2026-08-18 04:02:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1462a81f-aa20-3343-ad55-3686d9f22ae7 | -11.12595 | -46.49232 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d38e2fe-20cd-3acc-b6f6-6e5fc1fa7def | -12.267 | -51.54052 | 2026-08-18 04:04:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 26e96b4f-04f1-3b44-9837-91bc0ccb1688 | -13.4135 | -54.32905 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 656477ed-c73d-3d71-af1d-8ceb9cca2f78 | -11.3401 | -45.92203 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3929935b-cc8b-3806-b337-56a7c8534c77 | -14.22932 | -45.41656 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b706ea1a-fb5c-36b8-b96f-1276826021e9 | -11.13086 | -46.49333 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9311dd0-0dc4-305a-a523-556d938087dc | -11.46068 | -46.56661 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d5a5513-2503-35cc-8930-472cda4435f1 | -11.36333 | -55.42025 | 2026-08-18 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7885388-72f5-3b30-a1cb-e2c41a6896d6 | -14.16044 | -52.90532 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee3d4d8e-aad1-37eb-b4a5-529d162bbbfd | -12.40108 | -54.9572 | 2026-08-18 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30242aa4-83b0-3cf8-800e-8108eec1a6d1 | -14.25408 | -51.92971 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7b5dd400-9ca6-31a0-8667-9930ff06f277 | -11.3857 | -46.39824 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16eb7093-26c5-312e-bd3b-2d47731f97ea | -14.17926 | -52.93292 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd905d99-04ec-31fb-b77e-b9fe8f4fd7b0 | -15.9243 | -55.54434 | 2026-08-18 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5182100b-36ed-3e27-b261-3a13a4776b91 | -12.46535 | -54.19285 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e983c7b-4e98-341c-aeca-0c8e38e75286 | -17.9816 | -44.44054 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec7393e4-d289-3f9b-a836-44cf0718a31d | -11.62548 | -46.78007 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5237cd23-c0a3-337e-a4ae-99c622cf641e | -11.1382 | -47.27733 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1804921e-d1d2-386e-aaec-3dea16f1bb3c | -11.30123 | -46.33072 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a5a9dce-3f7e-3abf-94b4-792f4402f612 | -13.56286 | -51.70092 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c49b5c4-f7b1-3c0f-bc21-46270ec609da | -14.35529 | -51.93627 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef7bdc87-1485-39f3-bf44-fca64660b921 | -11.38916 | -46.40235 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2d957d73-ba77-32fa-bdf6-88984da6900b | -17.10852 | -46.57827 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae125e21-39ec-32f4-9604-e4183c06c479 | -17.45737 | -47.85785 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27f6edb9-e5a2-3f3f-a895-0732215a49b5 | -11.36063 | -46.39706 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18ef2949-5aaf-3640-8543-11b5f9f6f686 | -14.82351 | -46.63016 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 85ef071e-4899-37b0-84b5-4b9ffaf52266 | -11.36213 | -46.38985 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e40d786-9a6a-34ec-a2fa-9e2cf52df987 | -14.25625 | -52.1427 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 027c5fa5-09d0-3363-82fc-20dfcc9452bc | -14.16925 | -52.92197 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50f1f987-5c7b-38fc-bbd7-3b6b97a5041a | -11.46411 | -46.57106 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d26ca7d2-1f16-3817-8838-7db49ce8fd61 | -11.36532 | -46.39408 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7122929e-e4e3-36f9-95b2-617d6f80bc0b | -14.16816 | -52.89773 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f088d2be-2788-3f7d-811e-d3b4da509728 | -15.4395 | -41.38174 | 2026-08-18 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 349f5867-56d1-3aab-8925-a55f246fbc5c | -12.00987 | -46.42333 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9f1a80f4-d1ba-3d5e-af10-4cc622d2c111 | -12.23006 | -47.03216 | 2026-08-18 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1041d783-4089-3ebc-a474-9f25ba9b67e6 | -11.3602 | -46.4007 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed180cf1-93ee-3476-b1c7-4e396d29207c | -12.39912 | -54.9631 | 2026-08-18 04:04:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d9795dd1-128a-3742-a630-10da516b842e | -14.18189 | -52.9202 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d96a3496-279a-3b99-8582-eeda431ed82c | -14.03508 | -53.68499 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 07f36195-3ef2-3f3b-8722-66693bc1f6c4 | -14.43279 | -51.89032 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a74511c3-747c-354a-866b-3fb7e0be7770 | -11.35496 | -46.38144 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba716277-ac69-3f83-b5fa-35ca8c0afdfa | -12.23099 | -47.03559 | 2026-08-18 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f05e53-8347-3b7e-ad7f-da340671f9ae | -14.8072 | -46.6537 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| d4344feb-89cc-3722-8dbb-bdc963c6fb3a | -11.30805 | -46.33935 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4f09700-9d08-38c9-bb50-794f7f2b8191 | -14.26688 | -51.91853 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b95bdeba-3421-333d-a369-32a63a08960b | -13.26989 | -51.65416 | 2026-08-18 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac59d9b4-1727-31cc-8aaf-c7a51501fc30 | -14.43353 | -51.88663 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55719c47-8e63-35ef-ae01-8fc29c904302 | -14.17784 | -52.91015 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 65c59ea0-7a90-336e-acaa-2c5ed1c1ce2e | -14.35667 | -51.87113 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45a5f464-0ac6-3541-9156-0ff9f764318c | -10.56797 | -51.97526 | 2026-08-18 04:04:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 879827b6-0f11-37c6-a4e6-9332ccc60340 | -11.13307 | -47.28119 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b48a702d-0cf1-3da2-997c-afa187adabc7 | -14.80514 | -46.64283 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a16b99a7-923b-32ca-b088-5f24b5ab0b37 | -13.57932 | -51.76262 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3326f00d-f5a6-36a4-91ea-199da905be3d | -14.85389 | -46.64024 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2932bfa7-f1ea-3d46-b886-a8667ac02416 | -11.33705 | -45.91631 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b1b4f5-a46c-32ca-8d2a-8e3fb84b2e18 | -17.9517 | -44.43139 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
