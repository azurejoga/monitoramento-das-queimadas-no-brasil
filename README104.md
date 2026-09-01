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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af664464-989b-31fb-87fc-56c9fa41f184 | -15.4202 | -41.2232 | 2026-09-01 14:50:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| 9ae6ce72-e3e7-3aa1-9dbc-db8dc61ebf9c | -12.9032 | -45.8382 | 2026-09-01 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 473.6 |
| 71281b1d-f911-39e8-81d1-cdd50d71d238 | -11.2478 | -45.1425 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 83bfaf1c-d053-3424-a712-f17dfca419f9 | -14.7302 | -53.5966 | 2026-09-01 14:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 8bfb75f9-8479-30d9-8935-b98061bb54c9 | -14.5634 | -52.0344 | 2026-09-01 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7e81c4ae-91ed-32ed-9d40-33cbed721879 | -9.4349 | -45.625 | 2026-09-01 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a741e112-7bef-3918-86bf-8e6c39cca717 | -7.3118 | -60.5897 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3f84d9db-79c3-3de0-985a-478c0bec7fd1 | -11.2485 | -51.2647 | 2026-09-01 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 885a8a7b-9b00-3878-8820-19187339227e | -17.1345 | -46.8516 | 2026-09-01 14:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 18ec2709-35d7-35ee-9dee-23d620d0f36c | -7.571 | -60.4643 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| fe25af36-a326-34bb-8cf6-1956accde722 | -8.1296 | -54.9672 | 2026-09-01 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a33890cb-93f3-3c81-ab84-6e9e9bc465df | -10.7274 | -50.6192 | 2026-09-01 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a770460e-dfcd-3b9d-bada-ba339f1a021c | -10.1722 | -45.7414 | 2026-09-01 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2de4d27a-252b-3318-908c-092c9c3e8fbb | -13.9474 | -54.4179 | 2026-09-01 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a436fd29-c5a6-3ce2-ba38-3c1a150504be | -11.3236 | -45.1778 | 2026-09-01 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 220c14aa-5c07-302c-8ed6-8b921bfad271 | -6.6541 | -59.4452 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e5aebe6f-5bbd-3247-9e89-cd1882a59975 | -14.6732 | -53.5408 | 2026-09-01 14:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 3a8e94e1-89e9-306f-95be-2e34addda2ee | -7.3119 | -60.5706 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 00164be6-f17c-3806-b38f-a3656a34e856 | -11.6967 | -54.6081 | 2026-09-01 14:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 315692ee-ab16-35c8-beb4-51a845a2cefd | -3.4002 | -61.3276 | 2026-09-01 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| bc8fe8d5-7349-3743-b1bd-83e8fdba9769 | -7.2006 | -60.6706 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 4c23af69-3822-3a1a-af9c-0c459165d215 | -13.3748 | -51.7831 | 2026-09-01 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f1127325-00e6-38b2-af5a-d338194c0d15 | -3.6216 | -60.547 | 2026-09-01 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 565f2b9c-ca69-360d-8175-58bb6c863cba | -13.9477 | -54.3971 | 2026-09-01 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| aeed73fc-4786-3cf1-b714-aaaf4da2a8b6 | -7.3685 | -45.066 | 2026-09-01 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7e1769d8-65de-3d6d-a4e5-ed431c0caaac | -6.9367 | -55.636 | 2026-09-01 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4f5ac3c0-5c0d-3d2f-b5a3-4016155fd37e | -15.4429 | -52.681 | 2026-09-01 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 9b5b0f9a-901a-35ca-a3e4-ad933df6932e | -7.182 | -60.6904 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 20a2a1ce-f4da-3534-921b-e57e99eb0f90 | -8.7628 | -46.4642 | 2026-09-01 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5546dd7a-14f8-34c3-a9da-7f60e098ba7f | -7.0242 | -59.2374 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4cec0fdb-d339-3dea-9d15-08e075078a76 | -6.1659 | -57.7403 | 2026-09-01 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bc9f9600-4d0c-33d7-97f9-80b42dbbd82e | -14.6728 | -53.5618 | 2026-09-01 14:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| dc2d116e-0338-3d22-8596-33ce18e977a9 | -9.4421 | -67.4535 | 2026-09-01 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d671423a-ad23-3558-9c60-c14297595482 | -11.2317 | -53.9958 | 2026-09-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 899bc911-5506-3064-8ee7-79f6a86cffdf | -15.6475 | -50.1062 | 2026-09-01 14:50:00 | GOES-19 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d833ee2e-c9c0-3278-a1b9-26c41760186c | -10.7407 | -54.0401 | 2026-09-01 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| d7a0c20d-2639-38ed-b760-64069dfa514f | -14.7108 | -53.599 | 2026-09-01 14:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 56c9c7fe-73bd-3732-be7d-054323e6ec00 | -6.8217 | -43.5271 | 2026-09-01 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1d0d28fd-7b7a-3f0d-9c84-ad6bc68193f2 | -7.5474 | -61.3818 | 2026-09-01 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b1b55332-186c-35dc-a390-deb9b5ba2030 | -6.6727 | -59.4252 | 2026-09-01 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| adc25738-06c5-3e13-913e-92a3813a4e65 | -7.5256 | -44.4795 | 2026-09-01 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c642c70e-a1f5-373a-a067-0454134d2354 | -9.4538 | -45.6228 | 2026-09-01 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 38bdcb75-bf3d-3de6-be4a-8fdfd65ddfb6 | -5.9635 | -57.6899 | 2026-09-01 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3fadf8ea-6423-3d31-a7d5-e107ecf614c4 | -7.5289 | -61.3825 | 2026-09-01 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| eb0a1b92-fd14-3ee7-a7f2-7b41cd54120c | -5.5648 | -60.2121 | 2026-09-01 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 08e383e2-7849-31c6-909f-f814bd44221a | -14.2599 | -52.8782 | 2026-09-01 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8803fae3-bef4-3b12-a234-456a6407ecd6 | -10.1531 | -45.7438 | 2026-09-01 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 56701d0b-6dde-3a9d-9b1d-e274aaca7e20 | -11.2478 | -45.1425 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e47ba97a-8442-314a-b608-4b0fb21e9d35 | -7.2006 | -60.6706 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 47e03423-41e1-3324-af21-6b093a431cb3 | -3.4002 | -61.3465 | 2026-09-01 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7a8dd469-a255-3f35-9396-ae98e3d68b1b | -10.8624 | -45.3789 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d126e3dd-1228-38c5-89a9-1f5e2fbd175f | -13.9477 | -54.3971 | 2026-09-01 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 88116dea-c0d7-30f9-ac55-71768e2800c6 | -10.8046 | -50.5046 | 2026-09-01 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 7fe4e546-88a0-3b4e-9d74-64b0b1681a9d | -7.3117 | -60.6089 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d4f8f30e-bc13-3403-918f-049288f15198 | -13.3946 | -51.7382 | 2026-09-01 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 677bec32-d1ba-3669-91d4-c5ebbd4636e8 | -6.0726 | -57.9583 | 2026-09-01 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| dbe1f801-c417-3019-bf67-4f7529b4669c | -7.5526 | -60.4651 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 2d552a09-0038-38b0-b0be-c3044d1ff0b1 | -13.967 | -54.395 | 2026-09-01 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 625.1 |
| 6aebb1ae-3797-37d3-aebb-8bc44d2a430f | -11.2292 | -51.2879 | 2026-09-01 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2056d721-9582-3e60-8959-8dedd260acd9 | -10.7457 | -50.6599 | 2026-09-01 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9c31ec84-b2d7-376f-83c3-39f1f33f6f13 | -13.3374 | -51.7241 | 2026-09-01 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ad657240-a218-35ee-adb8-3a72311f9be2 | -13.9474 | -54.4179 | 2026-09-01 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c6a47a99-fd5e-3440-974c-8409c60bc487 | -6.7514 | -55.6654 | 2026-09-01 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3d7a4ba1-bb9e-3972-90d8-ba8334e5730f | -11.112 | -51.5536 | 2026-09-01 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ecda2c65-33d4-33de-8816-7e9b420c1413 | -11.0434 | -49.6851 | 2026-09-01 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 371ff044-db29-3765-abea-2fe3a934b4e0 | -11.5479 | -45.4676 | 2026-09-01 15:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 618.1 |
| 46539d47-7cdf-3919-93a1-cd231536c717 | -3.79 | -59.3031 | 2026-09-01 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 00f709ab-533b-3a60-813a-4f9621f4193e | -14.5025 | -52.2126 | 2026-09-01 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5200358a-99b4-3a6b-8292-a403f8809bd4 | -3.4979 | -59.0409 | 2026-09-01 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4ecc92a4-6ac9-3186-8c02-99a3c3958cfc | -13.4499 | -51.8799 | 2026-09-01 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4d45c816-c65e-3af3-916b-7491011f75b3 | -10.3391 | -49.9762 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8c2b6c7d-8006-3b53-9ca5-237e02c817f7 | -10.3388 | -49.9977 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 018675bb-1497-37e4-a775-7830ac225650 | -3.1266 | -61.2188 | 2026-09-01 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5d5748f9-f5c4-3c3f-a0ae-87ea06acb37a | -11.0437 | -49.6635 | 2026-09-01 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1bcda5f6-c709-336c-9d4d-f7bc20edde29 | -11.2295 | -51.2667 | 2026-09-01 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 5e1fbb85-82f3-3554-9d6a-dfda267af5fa | -10.358 | -49.9742 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| a5f5ca89-b4bc-3972-8a7d-2b563c855608 | -4.1515 | -60.7257 | 2026-09-01 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ab414554-4a75-3d48-9304-da72e19e21b1 | -5.9635 | -57.6899 | 2026-09-01 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d3ca65bf-351d-37b8-8ce5-db78cab30757 | -11.2439 | -45.3727 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7bd3e0fc-c157-31b1-bc24-22ed9ab6f344 | -11.304 | -45.2036 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 70c3417b-72e3-3219-832c-41c34d814797 | -8.9242 | -63.2804 | 2026-09-01 15:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| caa16e66-2e21-342c-bac9-3e5ec4528609 | -11.2482 | -45.1194 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ebba5bb5-b081-3af9-a0bd-c44ac2ce8b89 | -7.182 | -60.6904 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2a35987e-0798-3d5d-99ff-c9ea1257ac99 | -14.2792 | -52.8758 | 2026-09-01 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3495d55e-78c7-3662-bf5d-e40d1f57c24c | -15.4429 | -52.681 | 2026-09-01 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| cbd22326-a798-3971-b69a-6d89b1d2aba8 | -17.1146 | -46.8556 | 2026-09-01 15:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 254.0 |
| d05c4f74-13fa-314a-b011-21a03673b6bd | -11.3236 | -45.1778 | 2026-09-01 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4113fd13-ab29-3aeb-99cd-1f6c895d8e1b | -3.8792 | -44.0346 | 2026-09-01 15:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 753e740d-e0e6-362d-b5e7-4dc87d5f1eed | -5.9451 | -57.6906 | 2026-09-01 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3fb0c0c0-730e-3b61-9973-9c881bb884ce | -3.1265 | -61.2377 | 2026-09-01 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cd478c6f-9afb-35a2-880d-e93049b085a3 | -10.7271 | -50.6405 | 2026-09-01 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 168.5 |
| d4471201-365b-3186-b944-a69b61faff6a | -10.3574 | -50.0171 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 69dbc9a3-aeea-39f8-96ff-dc4f0749d59c | -11.0744 | -51.5365 | 2026-09-01 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| a5c28821-0569-3a63-ad1e-b67b572e5370 | -11.2298 | -51.2456 | 2026-09-01 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fede7a12-b104-3b4e-ac0c-e83b58d55066 | -10.2212 | -50.3303 | 2026-09-01 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f4571cf7-8aae-3101-bd1b-48eb10b840e1 | -7.4734 | -61.4037 | 2026-09-01 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d62fadf4-a4e5-3fa2-9243-a3f7f1fbcdff | -14.7108 | -53.599 | 2026-09-01 15:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f4f8c1ef-17f4-3646-a040-4e4628c1edaf | -7.1822 | -60.6713 | 2026-09-01 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 97c89961-ed4b-33f9-968c-982ed02c7068 | -7.5709 | -60.4835 | 2026-09-01 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.5 |
| be44a301-7a99-33a3-9d0e-dd941142dcd9 | -3.6216 | -60.547 | 2026-09-01 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |


[Clique aqui para ver as próximas entradas](README105.md)
