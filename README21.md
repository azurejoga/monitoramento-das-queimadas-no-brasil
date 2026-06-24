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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b27b579-a3a3-3389-a945-44c0ddac077a | -6.6393 | -45.62346 | 2026-06-24 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c291e9d3-714f-3c75-9627-fc28e75e1e9b | -6.99187 | -42.89848 | 2026-06-24 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 717c7700-d3bb-373a-8e1e-c850ff82990f | -8.93257 | -45.6894 | 2026-06-24 12:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| af6d726d-50db-386e-82e7-05001813c27f | -8.39313 | -48.21309 | 2026-06-24 12:08:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 77fdd9f6-6750-36a6-8fa1-5287b8cb2379 | -9.40432 | -50.68472 | 2026-06-24 12:08:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 6a6a2b87-333a-38fd-88ee-9e71703b14ca | -6.92699 | -51.93774 | 2026-06-24 12:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dcc218ab-3088-3172-8d02-41954159e181 | -9.26377 | -49.24667 | 2026-06-24 12:08:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0ae11fd7-3875-3b5a-a679-da26e4f07f1c | -11.30597 | -43.33006 | 2026-06-24 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5f0961d9-2f78-376e-bf8a-000dfefadbc6 | -9.40305 | -50.69375 | 2026-06-24 12:08:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c8f58f67-a0a8-38d8-9231-6265fcaf474c | -12.78782 | -44.42031 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 294.3 |
| 638a3b19-007d-341b-b94c-618687bf6332 | -9.74467 | -47.88033 | 2026-06-24 12:08:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c961be3c-06ee-34e4-b55f-6cb243e7866a | -12.7884 | -44.45185 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e56b0824-a02e-312c-8ccb-e07067feea3e | -9.68183 | -47.01997 | 2026-06-24 12:08:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| a0377237-fc8f-383a-a5b1-f143792a0504 | -12.83974 | -44.37914 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3587e35b-2bbf-3f6d-886b-aa9f5f4acb10 | -8.3916 | -48.22429 | 2026-06-24 12:08:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 629017ed-b4d7-3362-bb86-75b11c28bab4 | -12.83676 | -44.37339 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 807181b6-832e-3723-b04b-da5412eb995f | -11.22761 | -43.36861 | 2026-06-24 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 5b52f7ca-3732-3442-b220-d6fbd76c020d | -8.43592 | -47.90035 | 2026-06-24 12:08:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a3b9e092-d8cf-3296-9799-8a6b66f4c7c2 | -10.81928 | -53.54132 | 2026-06-24 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8ae4e8b3-5012-37f2-9323-3c156e462d94 | -10.81785 | -53.5509 | 2026-06-24 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 76c2423c-49fa-3f95-a99d-04318c361b33 | -12.79117 | -44.42606 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 5f112c52-7130-3370-9a6b-34c97481d5d7 | -6.59648 | -43.89354 | 2026-06-24 12:08:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 93acbc2f-b5f0-3e12-8fed-cb8f1fc34c39 | -11.19405 | -48.11667 | 2026-06-24 12:08:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7fd3c43d-5b0c-315e-bd88-0a935cb88002 | -12.83981 | -44.34744 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 0ea394ae-7c18-3e2b-897b-00c9b1a6e793 | -6.99266 | -42.90371 | 2026-06-24 12:08:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 7a67b92b-aae3-3427-9fbc-a5bac346b7f5 | -6.36816 | -43.5853 | 2026-06-24 12:08:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0e86815b-0906-3619-8833-a897201a9359 | -9.96127 | -47.87024 | 2026-06-24 12:08:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5aa44be3-dffb-38b1-bb0d-2d45156f9ed8 | -10.11589 | -47.55466 | 2026-06-24 12:08:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ca0aa3bd-941d-390b-8e64-ade2304519a3 | -12.77353 | -44.41883 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 69e258d3-e479-3a3c-9e8c-5db3fea5d6eb | -11.30308 | -51.41831 | 2026-06-24 12:08:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| adb83ab7-c19d-35ef-8c4d-eee4568d3feb | -11.22888 | -43.34636 | 2026-06-24 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 2d69b6d3-1203-381d-ae52-975f141a2373 | -11.23108 | -43.33956 | 2026-06-24 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 1ab45c8e-9c83-3a85-bf54-22f6fecaa1f5 | -10.11763 | -47.54136 | 2026-06-24 12:08:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f60a0c0a-7076-392a-b3f1-72c9fb0c07ff | -8.61039 | -46.00472 | 2026-06-24 12:08:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 795f7dde-8c68-3d0c-a694-a7eb322ab355 | -8.43753 | -47.88856 | 2026-06-24 12:08:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1c3e64d6-24d5-3642-976b-a403705e8c9d | -12.8426 | -44.35317 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 302.3 |
| be0ab2fe-20b7-3743-816d-77789780dbf4 | -8.93475 | -45.67188 | 2026-06-24 12:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4300feb3-3409-3f33-91d6-5ccf77417e46 | -11.30831 | -43.3253 | 2026-06-24 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 57.5 |
| feacf082-731d-3c03-add8-198c27493861 | -8.60802 | -45.99339 | 2026-06-24 12:08:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a4c231d7-4bb2-3238-86a0-31d4e3c5df3f | -12.44798 | -47.89076 | 2026-06-24 12:08:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0d59eca2-eb5f-3e6b-b2fc-7121ad62200b | -12.78487 | -44.44612 | 2026-06-24 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 332.9 |
| ff1a832f-5c1e-3819-a9c9-64868a18ae50 | -11.58682 | -47.44987 | 2026-06-24 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 031c8946-8e84-3915-b097-5855fe1c2500 | -9.74627 | -47.8679 | 2026-06-24 12:08:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ad9ef1fb-e883-3df1-9af5-b8f189dd046b | -11.58866 | -47.43541 | 2026-06-24 12:08:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c89bc8ba-9a37-37cd-a84d-8ccf51aa9312 | -10.77234 | -54.10914 | 2026-06-24 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| edba4d56-4273-395f-9942-5a71de9b8a8b | -12.8548 | -44.3625 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 675263df-74c5-39a2-ac17-2f6a98a1f501 | -12.7953 | -44.4426 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 230fed0b-4f16-37af-8c92-4d873bb7eacf | -12.7958 | -44.4191 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| a082d9dd-17bb-38bb-9f11-e88acfa1552b | -12.8552 | -44.3389 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7bdfd745-ff23-3e7d-a1a1-3d8a365d9175 | -12.7764 | -44.4223 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 322.8 |
| 88378d15-5a1b-341f-862d-b561c176b3cc | -12.776 | -44.4458 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 1ed2bbc4-f8da-3ff1-9113-1baf791fa61c | -12.8354 | -44.3657 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 333c4fc1-26e7-3766-8015-006c742cc4c8 | -12.8359 | -44.3422 | 2026-06-24 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 095b1f40-07d9-3eaf-b5ee-7c7e207901da | -14.06805 | -52.79559 | 2026-06-24 12:10:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a47aab9d-dd18-3694-89fd-59c2270efb81 | -14.69809 | -46.14309 | 2026-06-24 12:10:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 919918ff-3283-365b-ac50-5499cd372cea | -14.69572 | -46.16337 | 2026-06-24 12:10:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 558e47d4-c232-34a9-b1ba-51f08b3e6f88 | -13.06335 | -53.35501 | 2026-06-24 12:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 01497482-2d50-329e-851b-39fe6ee7333c | -13.07226 | -53.35634 | 2026-06-24 12:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a2b39781-ddaa-3113-bc4c-d2327da8a3bc | -14.05925 | -52.79429 | 2026-06-24 12:10:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db2000e3-aa0c-3453-a4e0-21a05a36c9fb | -14.81872 | -47.61068 | 2026-06-24 12:10:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6ec480bb-cbf4-3433-b259-925db99c48ba | -15.76146 | -43.20646 | 2026-06-24 12:10:00 | TERRA_M-T | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 8b4a297f-694a-33a4-8f0d-a3e7b3858ca5 | -14.69764 | -46.14996 | 2026-06-24 12:10:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 9e6d6a86-d668-3579-a899-ae65e93796c4 | -14.90502 | -47.75262 | 2026-06-24 12:10:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 01f07285-94a7-3d42-a0b8-6ee84c166eb1 | -12.7764 | -44.4223 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 330.7 |
| 9e3e5ed0-a527-31ab-aa14-fb448c334770 | -12.7958 | -44.4191 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| ef78f075-72f5-3b0d-b309-a34caace299c | -12.8552 | -44.3389 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 43ccc3c1-9563-34ee-9ea6-3b238124e15a | -12.776 | -44.4458 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 242.9 |
| 1bcf7e6f-d260-335d-aec4-b953547f2c27 | -12.8354 | -44.3657 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 04fcb537-d91b-38b3-92db-cf59e8d52810 | -12.7953 | -44.4426 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5835c101-eb7b-3a75-b921-ffd477d02e58 | -12.8548 | -44.3625 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 7935b103-d302-3486-9f14-e6936056211a | -12.8359 | -44.3422 | 2026-06-24 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.0 |
| f8e2537e-d1a3-31c8-b4fc-f609fd3772a7 | -12.776 | -44.4458 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 09eb4363-e514-3564-97dd-ee6d03f2f4b7 | -12.8354 | -44.3657 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| a4f1baad-cfd3-3c30-b8d9-a19025d97e6b | -12.7764 | -44.4223 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 283.3 |
| 509c73da-e130-3210-9807-187553ee10c3 | -12.8359 | -44.3422 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| dfb005e0-d75a-3cba-b246-c3992ef3b6ce | -12.7958 | -44.4191 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 487407db-83f0-3fef-8b00-16448b979a81 | -12.8548 | -44.3625 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 37e64fcb-66d4-31b8-b64e-02b9e888b72d | -12.7953 | -44.4426 | 2026-06-24 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 73471b91-728c-3cfc-83f4-1f1b72ccb23c | -12.8354 | -44.3657 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| c6d33a93-f432-3036-8977-aef81ccdfe83 | -12.8552 | -44.3389 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 843c43e8-ed7a-3d40-b148-43183b3b74b9 | -12.776 | -44.4458 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 61d2f688-6d45-3b43-bdc6-3a50c343eba9 | -12.8359 | -44.3422 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 2e4b5e13-23ca-3109-b406-3dfdd4bd2380 | -12.7958 | -44.4191 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ca32cd5f-70c6-3dac-a058-96094f0eafc1 | -12.8548 | -44.3625 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| ec7d258e-f820-3cf1-a80c-3eb46316c215 | -12.7764 | -44.4223 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 60ab5eed-ce99-3653-b813-96b5dbae6afc | -9.7442 | -47.8688 | 2026-06-24 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fd01db38-d95d-3248-9897-4b65d9f7e7ef | -12.7953 | -44.4426 | 2026-06-24 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 74273bf0-f707-3377-a879-9f046176f3af | -15.7635 | -43.2146 | 2026-06-24 12:50:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 105.0 |
| b828f60d-4c81-300b-8367-4f71fd870c81 | -12.7958 | -44.4191 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6fa8951f-ba58-3b0f-8dae-da4107415334 | -12.8354 | -44.3657 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 8c02af3e-c9ce-3011-9918-302af731adec | -12.8548 | -44.3625 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 87db6477-5ca5-302d-899a-9f3d07061304 | -11.2407 | -43.3464 | 2026-06-24 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 8b911a49-4eac-34b7-a568-d6db8071b2b6 | -12.8359 | -44.3422 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 1e00de76-0a69-3e07-a7cc-8c96a59f69f3 | -12.776 | -44.4458 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 58f0b6c3-40ba-3338-a317-912d64166d7f | -12.7764 | -44.4223 | 2026-06-24 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 719396db-714b-3664-85dc-04cb442a5681 | -9.7442 | -47.8688 | 2026-06-24 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e3749182-2ab8-323f-b3d7-41f1e15e1895 | -12.8359 | -44.3422 | 2026-06-24 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| e114ccc1-69b9-3668-85f8-00e37b8c6349 | -12.7958 | -44.4191 | 2026-06-24 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| cc94718b-390a-3e5f-b30e-62813cdb639e | -12.776 | -44.4458 | 2026-06-24 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| d727c3a0-af3a-3036-b8ea-2d02e1d38b6f | -9.7442 | -47.8688 | 2026-06-24 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |


[Clique aqui para ver as próximas entradas](README22.md)
