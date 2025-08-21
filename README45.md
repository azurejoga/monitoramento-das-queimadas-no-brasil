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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c757290-1914-3b22-9225-b707a6d2b468 | -15.51788 | -48.05865 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2bb5cf-b8b6-3603-ad07-673ff507ed17 | -10.27802 | -46.76216 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61348184-729f-3e55-882f-dda40bbff7d2 | -13.03012 | -45.17628 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc390395-d002-3c8b-8fea-85f9d9185e39 | -14.85596 | -47.94137 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55de3bf1-83f8-3fe7-9639-e45d9246c1c4 | -12.63583 | -46.88111 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| babf5780-a0fb-3e69-9928-7a977198f718 | -14.36992 | -51.97335 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 494a5490-7617-3533-b1b9-8f668c3a83be | -10.72726 | -48.23911 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 304ba526-70d0-3ac6-bee3-9c8448b5445d | -12.97922 | -45.20181 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ffe69e2-8fad-33d8-b254-822a6ff14b80 | -14.62346 | -54.87019 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfc55a13-ecfb-3f9f-acb8-f0abb56c7f0a | -8.87077 | -62.39355 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| ecb3406d-ec18-333f-a1e5-55d4531c8f7a | -13.53817 | -47.04994 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 583f5bf4-4a30-32d0-8f48-69a145f07d1f | -12.93054 | -46.20184 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4abf540-56c1-3896-956f-8df205a44a64 | -13.19813 | -46.88844 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27721211-6a00-3ba1-885d-c8fcdb82fe7e | -13.56904 | -47.04724 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d64d7242-2f71-31c4-ba37-8143205c80ab | -9.55949 | -48.118 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 264db59d-dc3f-34ef-bbf4-0047886822e8 | -13.03916 | -45.17339 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d3eab272-f481-372d-ba34-895ab8ec253e | -12.6667 | -44.96377 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f28c52-7f56-39aa-8ab9-0d1d31187969 | -14.12202 | -45.37838 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6313e267-cb7e-3f39-a622-a6d10b8c39a0 | -12.94538 | -46.24043 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a63f31a2-be47-37ed-a5bb-9b3a6a424b21 | -14.47127 | -48.36397 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 268c36f3-7ef7-3a63-b692-f527c2a7785c | -13.5902 | -47.00682 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b221d48-3c62-3164-840b-26298c1b8eab | -10.9774 | -45.6514 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d62abfc-84c2-34c4-87e3-dd653b3ce376 | -15.57674 | -50.30426 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26f25119-0982-346e-b9c6-dc211f466673 | -13.0422 | -46.81441 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80961cac-2ac2-3ecf-98c3-42f067074bdb | -13.42357 | -51.81581 | 2025-08-21 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| decbf558-1084-3cf7-977f-10234d1dc104 | -15.02789 | -54.85246 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1975279a-9c5d-3e61-a1b1-ae20e8ce22da | -10.7192 | -48.24557 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38a49257-3a42-3136-b72e-d50820e4c79b | -13.64159 | -43.80494 | 2025-08-21 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47dc3aad-c690-35f9-baa1-80062a95fb20 | -14.38859 | -52.0059 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 072af8ad-692e-32c5-b83c-2e8c0d6d7214 | -8.86648 | -62.41537 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 724cde19-2755-3914-a23f-d7e1496b6463 | -11.43476 | -47.32399 | 2025-08-21 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 661dbe69-3625-3d76-bfb5-732ab83ac977 | -11.29813 | -44.9271 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65cf8f2b-415b-3141-89dd-bdce1c84dda2 | -9.91838 | -49.24984 | 2025-08-21 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f03b29b-c17a-3675-9534-cbebf8e9f9a6 | -14.46648 | -48.37191 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4de1b302-2a13-3302-b8d1-43689065b192 | -10.2823 | -46.75877 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12afcaed-9994-3f12-8996-542e3bfa79f5 | -14.12414 | -45.39518 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 451a2ae9-8095-34e8-bcef-c703b3cda966 | -8.37495 | -54.99673 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9202a7d8-f2e2-3fd0-83f2-6050e7d39448 | -14.84617 | -47.93113 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a0af615-cab0-3040-9b47-5326a4beeb4d | -13.53642 | -47.03519 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67c7b637-f919-3749-84b8-c83c6335d3bb | -14.4925 | -45.95989 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3c705fa-79b5-3822-a019-405bf8065e52 | -17.38934 | -44.25186 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c5b815b-01f0-388d-bdd9-ca0ad2792d06 | -17.38514 | -44.24617 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c0fa08f-b7ff-3237-b0da-fc7c3ffdd6ab | -13.49378 | -47.06275 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd9640b1-d573-3952-8e50-4c9e1cd11a27 | -11.91207 | -44.87689 | 2025-08-21 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3d1af96-8b4c-3bcb-af07-d67f3f59e3e2 | -13.03589 | -46.81128 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 407ca425-a094-36d2-b381-25cf0421015a | -12.97868 | -45.20578 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96ac8e2e-22cb-3f6a-a2c0-abc7adc92817 | -13.15673 | -46.90648 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d1bc4e-f67e-3c5c-9dc4-58f001b0f67b | -13.16811 | -46.90838 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77cc0267-17d6-330a-b87a-7d9a12d6f48e | -13.02958 | -45.18028 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3ee2860-0b49-3dfb-aeef-c42779858b23 | -12.6445 | -46.90173 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5b9f8b2-3563-3a80-8d81-abb316cd41d8 | -17.39954 | -44.24797 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 28f6ea9b-142c-325b-a554-d71abdb7f216 | -13.14136 | -54.91417 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8a00895a-dc87-33a2-b828-2bda58dbe834 | -13.14058 | -54.91877 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8881f903-42f4-3856-8eaf-d82cc513c777 | -13.42414 | -51.81226 | 2025-08-21 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7535853-a473-308d-a017-934536e31456 | -12.2191 | -45.40399 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e856d30-93a6-353d-80e0-07f482c2a1f4 | -15.57618 | -50.30804 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c9e8731-a3fc-3889-b876-2f3cb45fb84e | -13.02205 | -45.20369 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3be996e-360b-3f13-8540-cfeceac2e12c | -13.38647 | -47.49839 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f65aa2ca-48e5-37b4-8466-c559066d0e2f | -12.63653 | -46.87615 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cd81557-92f4-361c-8c9c-8db0d926b322 | -13.64674 | -45.71749 | 2025-08-21 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d559b56d-7f5f-3f3e-a59e-6e2666b02ae1 | -8.86237 | -62.40012 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| fd2bc191-f3aa-3cd8-b886-00f69eaac7b8 | -9.90004 | -60.28372 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a690a7b-d2a9-346d-981b-8df3835aba4e | -12.9866 | -45.21097 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec2f818c-9ca5-34cb-9313-f163d8b889a8 | -10.2847 | -46.76815 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec57a9a-b91a-3991-a09a-769a7068b24f | -14.37266 | -51.97749 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c1f0300-afdd-375c-b18c-a6dd6a1436d8 | -11.37885 | -48.99559 | 2025-08-21 04:40:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2249eb4-e1c8-3ed7-b9b4-f26876e6a43c | -16.24971 | -49.94109 | 2025-08-21 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2340d547-12ab-31e1-99f3-d6237cef7f3a | -11.51638 | -50.54058 | 2025-08-21 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850baa1d-a308-350a-8c51-79c2018c6ac5 | -11.29534 | -44.94736 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d788cf78-1790-3eb4-8237-60fd33fe1c84 | -16.26193 | -49.95433 | 2025-08-21 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4a9f4725-4ade-39e8-931a-f166a35c5799 | -8.61996 | -55.076 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f67bc020-d29b-311e-9197-b9dcbcef7c98 | -15.50139 | -48.04259 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12bdf49b-3a6b-3d91-9901-17ca8f3bffb3 | -13.4844 | -47.04703 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 318d3287-ccd9-33c0-8eb2-58bddc1fda90 | -12.08782 | -44.72808 | 2025-08-21 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f061059-8e8b-3da5-8d36-aada7932ecad | -8.86444 | -62.38922 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 2f7591e9-939f-3c06-b613-16a66bfee9a6 | -11.51583 | -50.5441 | 2025-08-21 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff20037-29fc-347f-a1e0-baeb78a2e10f | -15.50506 | -48.0432 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391e25b8-b038-397f-a5f5-a879cdad29b7 | -13.64725 | -45.71373 | 2025-08-21 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcba26b6-0e0f-37f2-90f5-8b1c6c7b1b93 | -13.32222 | -54.42523 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f94846d1-6a13-358f-a9ed-c6c41be9aa6f | -13.03587 | -45.19682 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3af32b70-f177-38be-b75b-1f8c723f44cd | -14.84555 | -47.93555 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b525cc4f-ea50-354b-9d13-b4d3b3d0be34 | -13.03906 | -45.20541 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 899b8fad-5c1d-3141-9712-1a6d9a0fade7 | -8.86542 | -62.42074 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b2cf27ef-428d-3cfa-849c-f689b4dcfd40 | -12.94475 | -46.18652 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16093c7c-7f31-32e7-b016-188e9a9c428c | -12.22322 | -45.40468 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 291a2758-6574-3ae1-a0bf-12fdbe1d7765 | -12.9013 | -46.07253 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74775d73-7a72-3a83-bc92-ed1b92005aab | -15.01557 | -54.83717 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ea4c0ac-f27b-3a63-a92d-9e9c65772bbc | -12.64515 | -46.89713 | 2025-08-21 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fc80075-7ac3-3c2c-bdeb-dd903bb2f462 | -15.00167 | -54.85303 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b89d28ad-473e-3d9d-b756-230b602c1ddd | -13.38281 | -47.49764 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78825307-2034-367c-a4f9-74e1ba01fad9 | -15.01484 | -54.84149 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 781ae1b3-4e2f-31b9-9437-5a458ca207ef | -15.01774 | -54.84636 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aba60bc7-78ee-31e3-b972-5a3e07581cb1 | -12.67152 | -44.96029 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5985695-e64a-3f24-95f5-f115ef8d3866 | -14.47064 | -48.36837 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb006dbd-307c-3d63-a3f6-cd62dbe2a929 | -14.85106 | -47.94957 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2bddb69f-1b75-3c77-8f24-69a95471a614 | -13.03902 | -45.1727 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8cf8b156-56ab-3a1a-9bf3-36868c8124e8 | -13.04766 | -45.17442 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 245b4066-0954-37ec-8d00-882b785eedcf | -14.85779 | -47.95495 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e509989e-bd05-3f82-bfd2-75986e4f50a3 | -14.62711 | -54.87083 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e36be4b2-a8ea-3114-a46a-6850642191cf | -12.94751 | -46.22508 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README46.md)
