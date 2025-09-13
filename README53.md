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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e657c65-7860-3378-97ce-4dbe3035f8fa | -12.96811 | -54.75276 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdce4b7-1574-3080-9fe1-07fb2af54296 | -12.13027 | -47.59349 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a18afa4b-4597-37e9-8843-8022213e244e | -11.4707 | -43.61015 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f005467-e9f5-3bf9-a4c0-77fb8d9d2685 | -11.73151 | -46.60284 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0dee36a-30ba-329c-9b6f-cdbe3ce69caf | -10.89218 | -45.57963 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09fca419-49e2-3b92-9b40-96a19bbfb349 | -13.77778 | -46.29229 | 2025-09-13 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 00697ac0-c422-328f-8f2a-e5d6a558495a | -9.51265 | -54.64942 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa101715-c8f4-3530-88bd-7e605adc8285 | -14.18622 | -46.2778 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 9eb566c9-f0c3-3a7a-a897-64ec31e68587 | -10.69417 | -49.18015 | 2025-09-13 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdfe33c7-6d24-3b35-9c6a-403ff969f8f9 | -11.18183 | -51.4197 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e4d7e3e1-203f-314f-801a-ebaaeb334e59 | -14.27962 | -46.0499 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e25f4f2-61c5-3e17-a6eb-55243934a69c | -10.89643 | -45.57615 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bdea8b4-f62b-3c7c-a8e7-08c94fbd837d | -14.28823 | -46.08513 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3981df46-25f4-39ef-b630-12d448a6df70 | -8.49584 | -45.13803 | 2025-09-13 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c030c9b2-156f-3f4f-80a2-c842189c2465 | -11.7469 | -46.62518 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 682ddf4a-03b5-3c92-b9df-f2bb6bf4b870 | -14.22499 | -43.51101 | 2025-09-13 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd65e8fe-5202-32e6-8651-a9181993aec5 | -14.1819 | -46.26027 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 582c63a9-c358-303c-a7f2-c7a6b46ce5d6 | -9.85405 | -43.14267 | 2025-09-13 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 571a03f4-f710-38c2-a98b-c3804045275d | -13.26869 | -43.75731 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 160ce504-fe39-3d5a-94c6-982c1af665a7 | -11.87616 | -50.57662 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4c4f2ce5-f38b-3ea2-9d70-f78ed66bbf17 | -10.9119 | -47.21264 | 2025-09-13 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0168c2d0-834d-301c-9904-1a47f15e5ab5 | -10.92363 | -47.21481 | 2025-09-13 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b22e999-b306-3c7e-8b67-793c5aac5ebd | -11.73813 | -46.60906 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| de7de2b1-b05f-3bef-9981-658e4d3b1bb1 | -11.40846 | -43.641 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04c3b461-01ce-31ff-9a9c-eba55e449d2d | -14.69729 | -45.14311 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f3e0d5-94dd-32f0-9cb1-fa05ae5bd8c8 | -14.1321 | -45.37551 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d656f6c-9de9-3e2a-8dc9-f5ffc131ace9 | -14.17622 | -46.25067 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa63f371-290b-388f-84e4-baa7cee83dad | -11.72105 | -46.66315 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ac31a8-235f-30f0-8390-486c1759a7a6 | -9.02908 | -47.05069 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1bf4cd3-1cbe-3eb8-b992-45f0aeda4fad | -11.20055 | -48.42511 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3334375f-0b4a-3d38-a154-452fee2463c3 | -9.51061 | -54.65979 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03afd0c5-5372-3559-9101-55ef148130d9 | -11.83876 | -50.56831 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f2d1be7e-c3a5-3374-b826-44df3e965b88 | -10.15239 | -47.90838 | 2025-09-13 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66f3c7b4-dbfb-34a4-a83a-096fd90a3c76 | -12.93398 | -47.99377 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1fc1cab-8952-34e6-a0fb-db856c83742b | -10.51112 | -51.53727 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22a06f6e-217f-3c80-a18b-b4d2564f87f9 | -11.06379 | -51.5074 | 2025-09-13 04:08:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4e8cfb2-2296-37a8-9ec2-7ca70fb86102 | -11.3926 | -50.47381 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7356cff1-a0c5-3c51-93ad-276c5cda254d | -12.08999 | -47.57373 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 133eb796-4a9d-3a9b-8b1a-6570edbcfaf6 | -11.42288 | -45.61316 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2e17fd51-24be-30c6-99f5-3b256f78cbe2 | -9.19826 | -45.77969 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 502f933a-bb0c-3004-8f2c-1e2990725285 | -11.43116 | -43.54221 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab3589b2-e960-3093-b3ea-6d47917ec225 | -14.18193 | -46.28141 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| af83a5e4-f858-3531-90f0-dacca7ec92d1 | -14.4364 | -47.3429 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c2556eb-69c5-3904-8662-688e9922ffd2 | -12.91717 | -54.75121 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e0d6dd0-4347-3d8c-bc9d-7415c77bdd6b | -11.73573 | -46.62293 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3651122-cad7-32d9-824f-771ba4b37846 | -13.65464 | -43.82839 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86d87db6-8e99-31df-8777-34a975d110fe | -7.79807 | -47.10024 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df3b25ed-efc1-3eb9-ba36-9237a33c731b | -13.47623 | -48.44894 | 2025-09-13 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fddf6a2-685f-313e-bbc8-fd0eea082937 | -7.9438 | -46.90274 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2804e2f7-c1f2-37d3-a731-a812f2090b53 | -9.05238 | -45.82006 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3553cae-aa57-369c-807e-3f378704d968 | -11.08734 | -51.43999 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb28cb8d-51ca-3d7e-bd48-6f47291ef75e | -9.89659 | -51.86481 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 967ed1d2-443f-395c-9a21-c6ae1b1dae32 | -14.22099 | -46.28905 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 24f79d11-af78-32c0-849c-d3bf6e1c2c66 | -9.69984 | -47.53042 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fff76491-d1c7-3417-9f59-68233906351d | -13.25321 | -43.7474 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f378d59c-42ec-3967-af67-d0fcf8c44165 | -9.25781 | -51.24421 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8346bbe5-92bc-31e0-83e2-005d5926dfeb | -8.47307 | -47.25294 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8343458-839b-317d-9ecd-823ffbc0df7b | -12.9367 | -47.9784 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b346b42-6938-3b48-83f1-fe3e9cc54f57 | -9.54157 | -45.52074 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50a801d5-a900-3fe5-ae58-b2a735002dc6 | -14.8778 | -44.48423 | 2025-09-13 04:08:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cc2a53f-817d-377b-801d-3a02f31b768e | -14.19171 | -46.18182 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c980b002-b087-3292-b76a-8223005c80cd | -12.1046 | -44.885 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc7f7c95-1c0f-3280-9447-8a1ee4908dda | -11.12789 | -50.70383 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff7435d0-d7c1-3ed6-b39d-11d101f583c4 | -10.50547 | -51.54153 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe8afa90-fdc5-352f-8b41-ab5ffd35e5af | -10.65935 | -46.27873 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 08f5ec2a-455e-3e32-b77f-0beb01280b0e | -11.81281 | -46.73862 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efe501e7-4184-379c-a8e2-9c74fec7246e | -10.50802 | -51.55357 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2992ef66-cfd1-3bee-bdf0-111dd769cd20 | -8.23647 | -44.36245 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32da481c-858c-3de2-882a-a603a2948442 | -10.36049 | -45.39598 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 086b690d-7336-3b1c-8573-7dc3b4a06896 | -9.99847 | -51.73873 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d474f5dc-e583-3e94-ad6c-bfef171da732 | -12.09554 | -44.87561 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31c830c0-bf03-3478-b4e9-8b661ccab000 | -13.91046 | -48.28771 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 533fcb59-91f2-3fec-9914-f074d5c55481 | -14.70283 | -45.15182 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| affbb18e-6134-378a-8808-796dde2f0b67 | -14.2003 | -46.23838 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1e29892b-606b-3b02-b506-3c9b29ceeb16 | -9.5004 | -50.89082 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a9dd4e-ac0c-30e5-bafa-09f245b66daa | -12.82465 | -47.92786 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 815ab4bb-cb9e-3083-be43-5f0e00f1e504 | -14.19687 | -46.27987 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 505afedd-759a-341b-a49b-9a2b27976eda | -11.85698 | -50.57743 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5585d96-4bc6-381b-9e25-6f96d288706a | -9.74006 | -45.39185 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29b8427b-d4e5-31e6-8dc9-0bae2a8d9b29 | -9.25306 | -51.23631 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caa2ba73-d800-331a-b275-9394efbf0986 | -11.41932 | -45.61249 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4a128341-131c-347b-80f1-569ac8b239c5 | -11.47013 | -43.61372 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5de587ce-dcbf-3fa3-b42f-61a6063bd2d2 | -11.07043 | -51.47262 | 2025-09-13 04:08:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ca019cd-0481-3fd0-bef4-a8d708e42c42 | -13.13131 | -47.13573 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8265e602-b24d-3398-bf01-7548ea19c4f2 | -13.13966 | -47.13242 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25996e39-b507-3e27-bceb-3f2b512fef9a | -15.74489 | -43.01809 | 2025-09-13 04:08:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c28c9c1-8267-382a-a69e-a249811ea9e1 | -12.99259 | -46.74015 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ea2351c-8c0c-33ca-a2f7-eac5482fedc9 | -11.72946 | -46.59249 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b4553c4-181f-33d3-898b-840516f90bc8 | -13.66931 | -44.22156 | 2025-09-13 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cd80cd0-352c-3c82-bde4-f9fa3271143f | -11.72433 | -46.57778 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7a64934-15fc-36f5-a90d-ddc545661db3 | -11.14901 | -45.31942 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 044a00db-febb-3f29-b264-ffa14da93ef3 | -16.25004 | -39.02835 | 2025-09-13 04:08:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4dcfde0c-01f2-33e7-8fc4-57bca9918ba3 | -12.99948 | -46.735 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 157157d7-5001-39c1-aa0f-570f2b2db109 | -9.01068 | -45.78352 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8520a0a-9572-3dd9-80b8-f5a87dd43743 | -11.77257 | -50.54984 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2f426dd-3382-33b1-a633-83565ab035ba | -13.67266 | -44.22212 | 2025-09-13 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23bc6502-2441-3c98-acae-122576b8297d | -9.51722 | -54.62624 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| f3b3e407-548e-3b5c-a55f-1f26e555462b | -11.87237 | -50.57035 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 076e6686-ebb3-3b62-bc6b-ad1cd111cff4 | -9.80078 | -48.89207 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 009f57c7-044d-3457-b9a5-140dd9d3eb68 | -9.78697 | -47.79332 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README54.md)
