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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e0cee64-8cda-3a96-bf7b-d1a3fe5c7d08 | -13.20081 | -43.35605 | 2026-05-20 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e655f307-7382-3f1f-bb02-f0439ec31912 | -13.94542 | -44.25202 | 2026-05-20 03:51:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be7a2990-e0d2-39ea-8aa4-95d1ab70209a | -17.5932 | -46.56446 | 2026-05-20 03:51:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15afd8fd-1fd9-36ef-b661-893e14ea0bc8 | -14.08093 | -42.11808 | 2026-05-20 03:51:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0f8f9fb-a064-35cf-830f-4030a4f2f5aa | -14.17096 | -52.8704 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd2f6e95-e969-3eb5-aad2-efe889e835dc | -13.31263 | -43.0241 | 2026-05-20 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| df86ae9d-047b-3697-a4bc-26080583ccb3 | -14.64405 | -46.08683 | 2026-05-20 03:51:00 | NOAA-21 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e184ff11-66cf-35be-99e0-f8f94494082b | -13.1968 | -43.35533 | 2026-05-20 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d3fa4b1-d3c9-3ac6-91f9-9f3aefdd232a | -14.16388 | -45.31068 | 2026-05-20 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50a7b703-ffc3-3c89-9639-ae35d4228b88 | -14.16387 | -52.8688 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c00130de-cbae-3e71-bb04-c3164e3b7f48 | -14.9137 | -47.73573 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01944310-d52e-386e-9bf5-c9787ba48b05 | -14.1577 | -45.31892 | 2026-05-20 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f45ae85-9b6a-3e5b-9355-4d0d9ca6294d | -7.79582 | -41.23583 | 2026-05-20 04:21:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9e1e3a95-7ded-3bde-8745-399841788b91 | -7.01315 | -44.99035 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff5c3f15-77dc-3ddf-9592-463b30d8c1aa | -6.29965 | -43.63562 | 2026-05-20 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fba566d3-0b20-391d-a210-f0f1e1d6c334 | -5.95099 | -43.48746 | 2026-05-20 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 45d82fbe-89f9-38cb-acf9-bb40955d32bf | -7.72333 | -44.55046 | 2026-05-20 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffae14cf-2655-3af6-9384-aa9aace150e9 | -5.72925 | -43.43474 | 2026-05-20 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bf416b3f-f8fe-30f7-9b14-ce5437f5a6eb | -5.95044 | -43.49094 | 2026-05-20 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9aacccd7-3cb4-3484-b62b-018d17af9052 | -6.45337 | -44.13012 | 2026-05-20 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68503b84-13f3-3723-a94e-829577801d1a | -6.39379 | -44.16687 | 2026-05-20 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12752f8e-d955-3acf-96be-544bbebc9c44 | -6.29632 | -43.63509 | 2026-05-20 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec79c61-5b21-3c2d-9417-01f3750a55ad | -8.10088 | -44.1131 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f012be79-0abb-3d92-b56d-fd4a4be432fd | -6.75382 | -45.01662 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75084fab-b753-3717-a785-abcbba0039cb | -5.30555 | -43.05824 | 2026-05-20 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f1585f2-074d-3285-8fe8-2b520b38d18c | -8.09976 | -44.12009 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b448e50-01a0-3489-a1ee-42eeeaf28287 | -7.35489 | -46.21507 | 2026-05-20 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2bdef44-dd06-334a-994b-9e17a7f593bc | -7.72219 | -44.55756 | 2026-05-20 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9256482e-e5cf-3973-b614-2cb7f20beb91 | -5.75141 | -43.40265 | 2026-05-20 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6027154-3d6b-3026-a836-6e699811091d | -3.96211 | -43.12255 | 2026-05-20 04:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 824f3387-f59f-36c8-8d43-b91063e25d5c | -5.75473 | -43.40318 | 2026-05-20 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b1a8b19-4028-383b-bb25-6e33b8edeca7 | -6.75442 | -45.01296 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f52fcf17-aca8-38ef-b4dd-0867f6511f4f | -6.75664 | -45.02081 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f64a045-f835-361d-bad2-949adc96b3a7 | -6.63909 | -44.49406 | 2026-05-20 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2313c1fa-2214-355b-b429-1aebd8d03a18 | -8.10198 | -44.12762 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75c359cc-d589-316a-b471-0f657a201953 | -6.18865 | -44.85894 | 2026-05-20 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5531bb91-971e-3118-ba83-b53a62455795 | -8.09755 | -44.11256 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ed0473b-9125-3505-8091-3ee9238ea93f | -8.09867 | -44.10558 | 2026-05-20 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe28603e-a1ad-3ecf-a98d-8790f5653231 | -3.95822 | -43.12549 | 2026-05-20 04:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06626375-7c56-3bcd-aeea-71c725caa3d0 | -7.40364 | -46.6238 | 2026-05-20 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4463d722-cc4f-3eef-a4b7-c4aebeb8bf22 | -8.0959 | -44.10154 | 2026-05-20 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f0087aa-c1d4-3f61-b28e-8a848950f833 | -5.95432 | -43.48798 | 2026-05-20 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| de654254-be26-37a9-9476-c5c47ffcecb1 | -3.96155 | -43.12602 | 2026-05-20 04:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e2e512a-35b8-355f-b0c0-981895e9da8c | -8.10254 | -44.12413 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77a6a390-a8a8-38e5-b44b-bcc7dc0049be | -2.87524 | -40.02052 | 2026-05-20 04:21:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5ae13ef-9d98-30d3-8633-d143faf8e29c | -8.09534 | -44.10504 | 2026-05-20 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5005ce44-d427-3b3c-90cb-6eaacde55f86 | -7.40002 | -46.62321 | 2026-05-20 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 406b04e6-6c01-33e5-a395-b8f6fbd566a6 | -6.751 | -45.01242 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53f8a8fc-4686-3268-9ac3-0f6dca677b41 | -6.21904 | -46.89781 | 2026-05-20 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3fe3c3-76fd-3def-829d-51a13633986a | -3.95878 | -43.12202 | 2026-05-20 04:21:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89e334d2-1952-3e09-84da-5934fb151c23 | -5.94711 | -43.49041 | 2026-05-20 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2f828f8-f177-3bc9-8478-81c2a1080fa6 | -7.01256 | -44.99399 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8409b91b-85c0-38fa-8a46-e9f2dea950de | -8.1031 | -44.12063 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 553874e6-95a1-353e-bf01-4a8e2df34ad0 | -8.10032 | -44.1166 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9edf45a5-d742-3c83-989b-70b35b4040b8 | -5.95377 | -43.49146 | 2026-05-20 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 931db560-4cae-3678-a7db-609660c741f9 | -5.72592 | -43.43422 | 2026-05-20 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7555d2f5-6753-3334-b875-066a97da77b9 | -8.09811 | -44.10907 | 2026-05-20 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66854388-97ee-3f80-bb01-5d707d601bba | -6.75945 | -45.025 | 2026-05-20 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c93a6c22-2f58-30ae-8bd7-ff4cfa88703d | -12.60548 | -44.52441 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b89954d7-6cb0-3875-8179-673ef89fea48 | -11.93777 | -46.92787 | 2026-05-20 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8534a6ff-8aee-303f-b347-0606e75cc96b | -10.48781 | -49.36261 | 2026-05-20 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5dfcb40-07d0-3e09-92d2-657725781c6a | -10.49542 | -42.40689 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97cc2c93-4aad-3811-8ea8-07d35ef542cf | -8.7347 | -47.97762 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ad2e7e6-651e-3ec1-9310-a1011afd7291 | -11.93029 | -46.92773 | 2026-05-20 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31d30455-d7fa-37ae-b414-c78d56042b08 | -9.95444 | -52.47152 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d56486-fe58-326b-9246-913dc1e70063 | -12.59939 | -44.51978 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6db8c28b-30dd-3c6d-b012-c5ca62716cb8 | -12.35395 | -45.67957 | 2026-05-20 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83efd098-d8d4-39ac-b9e8-b021205dfa07 | -9.96486 | -52.41448 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 620de839-c30a-35bd-b2b4-55dea6d5c207 | -11.47109 | -47.33809 | 2026-05-20 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f694517a-0838-30b3-be8d-dea01a569996 | -8.55493 | -45.98683 | 2026-05-20 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac381db7-31c8-3f34-9ef6-bf23c176ce65 | -10.39913 | -49.44457 | 2026-05-20 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 036c27e9-2369-3fd5-91b4-834315653882 | -10.57729 | -46.6585 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 063becfc-abe9-3575-8dbf-ca2d148c4e65 | -11.60534 | -54.19306 | 2026-05-20 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2f116b4-ab87-32ef-8636-9ce11e87d52b | -11.6002 | -54.19141 | 2026-05-20 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c501aae1-428e-3e7f-9241-aebd8a6fa610 | -11.45272 | -55.1128 | 2026-05-20 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28fd6b36-7cab-3b20-98fa-cccdd5bbe87c | -14.18969 | -42.01678 | 2026-05-20 04:23:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f462baf5-9736-38e8-a726-c1c932bb391b | -9.95986 | -52.4135 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cccf0ff-fcac-3b65-af83-d54f0b334872 | -8.73088 | -47.97696 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0587203a-957c-36fe-aed8-e475463b511e | -13.52992 | -46.71577 | 2026-05-20 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5107e8f9-93c0-3cc4-b1f0-b63c76b636f4 | -14.15658 | -45.31756 | 2026-05-20 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da53b054-7c7f-367d-9b13-bcf8db96704d | -8.70066 | -47.91179 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 533454e5-b5f5-35ac-a0c7-7920dc0c99f8 | -11.60507 | -47.10154 | 2026-05-20 04:23:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bce5ac9e-5595-3e71-b1e0-1d9142612019 | -11.47417 | -52.91718 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1054205-9859-3fc6-a945-3d7b33a0bdcf | -8.70672 | -47.92241 | 2026-05-20 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8aaa2fb-44f4-31e9-9108-fe52025fa534 | -12.60604 | -44.52087 | 2026-05-20 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08ecd15b-19d9-30b6-b896-5b5aad6a9fad | -10.11837 | -52.41518 | 2026-05-20 04:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e163f373-9e3e-3373-b8e2-466ebcecb947 | -13.05782 | -48.31099 | 2026-05-20 04:23:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c5dcffc-714a-3f77-bb2d-f158e6c4330e | -12.22742 | -44.26357 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fc1a3cf-f00c-394f-9861-aa22bf6b4c6c | -8.73167 | -47.98484 | 2026-05-20 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e0e434c-3ec2-366f-9932-0a6d2c236dcc | -12.22622 | -46.60774 | 2026-05-20 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5db5a8-266e-3ba4-a86a-37a3541863aa | -10.57093 | -46.6534 | 2026-05-20 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1db78c5f-8480-3a27-a69b-30e4df3002e4 | -9.17871 | -48.99432 | 2026-05-20 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaec17f1-44e3-3291-b393-99eb30a5e734 | -12.44492 | -44.74826 | 2026-05-20 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 929639e4-00f0-3af2-bac6-8ec3c3ed6067 | -12.2252 | -44.25594 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8795f2f0-1054-30a9-a22c-dfec2e7b0794 | -10.49642 | -42.40723 | 2026-05-20 04:23:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab413a47-e4dd-3592-87a7-06b1d0c49f74 | -12.22408 | -44.26302 | 2026-05-20 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4664f8d0-c3e2-3b70-b0ca-054a4811bf53 | -12.05756 | -45.28867 | 2026-05-20 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84b2fd1f-4225-39ec-9bff-9a18ee47c355 | -11.45793 | -52.92012 | 2026-05-20 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05022b4e-0f79-3865-8a7a-17a0c5d7054b | -11.60087 | -47.10493 | 2026-05-20 04:23:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 218cfe70-7df5-3bac-8475-baa922ee1f35 | -11.5999 | -54.19184 | 2026-05-20 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
