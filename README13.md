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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcd86bfd-db80-3922-8289-626cf0d5b05b | -18.050301 | -44.430801 | 2026-08-21 00:42:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7059259-3a09-3288-808c-0c3cc688d957 | -8.4439 | -46.961498 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2a75e3-c93f-3e39-9527-7877e75c1cee | -6.8364 | -59.405399 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df437567-4171-312b-94e5-7b6a69e8592a | -15.7164 | -47.786301 | 2026-08-21 00:42:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 568418b6-0512-3545-8dd4-6714478f493a | -9.6267 | -48.200001 | 2026-08-21 00:42:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da6e3367-fc3c-30ed-b478-5ca206b4e067 | -6.1152 | -53.065701 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0303c958-8d30-3419-9118-e9366e9ecab7 | -4.0519 | -50.296398 | 2026-08-21 00:42:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255a19e9-dc34-3574-921e-34cb1fa1a046 | -7.3605 | -45.816299 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 797e1ed3-128f-3a8e-8bb5-25d45edb9bb8 | -7.2405 | -49.9048 | 2026-08-21 00:42:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe029cb-2527-3dd1-8268-bb5232f75e01 | -9.0564 | -50.891201 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c52d9fe0-0dd4-37b7-aba0-187e5211c580 | -8.586 | -54.778702 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe95f17b-833a-3751-a59d-8d87859e5582 | -6.2344 | -55.622601 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5d4dda-b139-3dc9-b64f-b29e3dabb6e7 | -14.4517 | -45.619999 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2248741e-ca80-3d7b-bb8c-4cdba27646e0 | -21.0833 | -43.246399 | 2026-08-21 00:42:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a39f926-d42c-3d7c-aacc-9967971fc2d3 | -6.2241 | -55.480801 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50bc4311-ae35-3b2b-b956-4cef2c0e4857 | -9.2128 | -59.750099 | 2026-08-21 00:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea2b9a0-752c-3abc-a7b3-c63f7ddb26a2 | -15.1884 | -49.424198 | 2026-08-21 00:42:00 | METOP-C | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 20e56401-c547-38e8-9ffb-5fdbb65eef11 | -12.8542 | -48.4361 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db7261ba-2ba4-3364-8ab8-b05b4100ad01 | -12.4438 | -43.3979 | 2026-08-21 00:42:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61f08d69-9451-350e-b678-89cdb65e9ba8 | -14.7256 | -47.131699 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1dba9384-0372-311d-a641-cd35e6abafbf | -4.0998 | -42.5117 | 2026-08-21 00:42:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 171aa3ec-4e66-3499-abb4-f169ac29b85b | -19.861 | -45.5261 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e21a5cd3-da5a-3878-a711-04ff138d23a8 | -18.656099 | -43.187099 | 2026-08-21 00:42:00 | METOP-C | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 848aef66-6726-3eef-9386-884caa245c13 | -5.9364 | -52.214298 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e950fd0-e7fd-3f9c-bc6d-a150f7a5575a | -8.7212 | -49.618099 | 2026-08-21 00:42:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754d79de-5578-3787-abde-6fefc9e47c37 | -14.341 | -51.924 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64950aeb-3ace-3c53-a2bf-081936f9e4eb | -4.9399 | -55.780201 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4269ca-bc6f-371c-b013-87f3e008945b | -10.7602 | -50.319199 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da6594ef-6a43-31cc-95f7-1e8ff43b0bd3 | -10.3206 | -50.377102 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0fa5ec8-a91f-32ca-922f-4e0e77b8cd63 | -3.2674 | -49.5252 | 2026-08-21 00:42:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94ba545-d9c0-35a5-9339-9b092b69bdf2 | -7.3505 | -55.685902 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e702668-a76a-36a3-ac09-5ccd528f3b14 | -10.7278 | -44.772499 | 2026-08-21 00:42:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 537f3bb1-b873-3e18-9346-bb62a73dd139 | -5.9346 | -52.206299 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd13e401-f49f-312d-bf51-5e0b9995dbc9 | -12.0087 | -53.435101 | 2026-08-21 00:42:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 327ffacc-12a0-3349-85a0-43e3db144af8 | -19.704599 | -46.9193 | 2026-08-21 00:42:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2196c84e-37e5-39b4-a4e2-976eb44d447b | -6.3638 | -58.3148 | 2026-08-21 00:42:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe41cbd-7987-3462-a7de-79a209ce1427 | -9.272 | -45.647202 | 2026-08-21 00:42:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40d3bc53-4f4e-341f-a0f5-636eaf3cb6b7 | -13.4412 | -43.842499 | 2026-08-21 00:42:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b696fe0f-8934-3342-b6ab-6cc82c506103 | -9.4378 | -51.645802 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d050902-7266-3a70-95b8-fc3eb9273a3a | -18.0466 | -44.415199 | 2026-08-21 00:42:00 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8bb157a-ec0c-30b3-bd7e-01ea59430a01 | -6.8704 | -59.423199 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8324af02-7bd1-3947-92c5-81d899a1f736 | -10.357 | -48.237202 | 2026-08-21 00:42:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 151434aa-6966-3124-84a2-0c462a49b8e7 | -8.1053 | -51.657902 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e642d0fd-0f61-3f08-ae58-d4f4a68c7508 | -8.4555 | -46.966599 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7ffbe19-8422-319c-a7e9-0b802c7da65e | -10.2634 | -50.304199 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c775b20f-d2cb-3b3c-b999-eb2410d7bbe9 | -10.8043 | -50.2859 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5008cb6e-3103-3760-8edf-9934c76f7aa2 | -10.8281 | -51.005699 | 2026-08-21 00:42:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da1b3490-3e8a-3571-8e3c-e49e7e63f81d | -12.4462 | -43.407799 | 2026-08-21 00:42:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfdfd9d4-7576-3204-93aa-71d1e9c979b6 | -10.7618 | -50.326599 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d52cff3-ea92-3609-a166-ad62602f9916 | -12.7432 | -48.446602 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8cbd685-fafa-3257-b8d3-6c8a355bc022 | -12.7958 | -48.405102 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a13397a-83da-3d7d-a4a6-43595f720d9d | -23.308399 | -47.558899 | 2026-08-21 00:42:00 | METOP-C | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46b73e10-129a-3221-8bfc-d46731525f78 | -10.7472 | -50.353401 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15d6defe-4a5b-35dd-8534-c30d914867c8 | -6.4674 | -43.5401 | 2026-08-21 00:42:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7761f907-077d-3b4a-9cbf-58a2053fab56 | -9.0662 | -50.889099 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5899dfd6-d9e4-3efb-bce1-e3cb74ff520e | -6.8803 | -43.756699 | 2026-08-21 00:42:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e70bbe76-fdc9-38e8-b8f1-9f3fc685b4b2 | -12.8639 | -48.4338 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5064b894-6eb3-33ef-a1f2-9fa0fbc28773 | -14.7174 | -47.141102 | 2026-08-21 00:42:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 959710d3-77f1-3725-bb99-cbc9681e3fe3 | -7.4614 | -46.157799 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 808a1b65-b566-37fc-ba62-7bcb035ac83e | -7.3742 | -45.830799 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 623df1bb-dcaf-3eb8-bf9a-09f4be71c32a | -9.4111 | -60.3983 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4fc3e97-27ad-3b97-afb3-36c54c5bb697 | -5.6106 | -45.7034 | 2026-08-21 00:42:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9452e8-b54a-34d3-840c-14fd77e392d0 | -11.373 | -46.370998 | 2026-08-21 00:42:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47b61236-b9a6-3a53-bb9e-31f909381101 | -3.9573 | -43.1189 | 2026-08-21 00:42:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cfeb191-c50f-3434-b9bd-559fdaf8eb0b | -7.4595 | -46.149799 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c1ff7d6-695a-32d7-aa99-f736cbcf3990 | -4.9426 | -55.792599 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51b50387-9ebf-3e69-bc4f-e96c9f42a588 | -4.9116 | -56.257099 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a96b8e2-f8ee-3fb4-99c0-efad7109e60e | -15.7195 | -47.800499 | 2026-08-21 00:42:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 39a6c039-d701-37b7-93c0-b97483f440bf | -11.6315 | -46.550598 | 2026-08-21 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf5debd9-f704-385f-a74e-6033388acd26 | -5.1759 | -47.955502 | 2026-08-21 00:42:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 434b27fc-199f-3008-8425-92d6e98898f2 | -11.9966 | -53.425999 | 2026-08-21 00:42:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a282e28a-0382-32f6-b321-76ee3417dca3 | -8.5855 | -54.728401 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1805dba-a44c-36a7-976f-611ee3fe98eb | -11.0871 | -47.593899 | 2026-08-21 00:42:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37bdbf41-bad8-3522-b483-c063441352a7 | -15.4981 | -53.893002 | 2026-08-21 00:42:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 502f0447-2d25-349d-8ac5-5592e3f8c7cc | -9.4423 | -51.619202 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 678e5b79-1db7-3094-bbc8-0cf610f3640f | -18.7013 | -47.463402 | 2026-08-21 00:42:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38dbafcd-343a-3311-8fe8-0724f7f035d2 | -6.0152 | -57.822399 | 2026-08-21 00:42:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14d7f7cc-7d51-3bc2-ad91-a6c37b75a19e | -13.3902 | -54.373798 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c388f1c-2331-37a3-aed5-b297aad1ea3c | -22.375099 | -43.015202 | 2026-08-21 00:42:00 | METOP-C | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2fb3044-28bb-3155-8152-159ce04608f2 | -8.5907 | -54.752499 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0781db97-4dc3-37c0-b200-6e997cfadb04 | -13.3999 | -54.371899 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b82829c-cf34-3787-bfc0-396c5bce3d38 | -15.7097 | -47.8027 | 2026-08-21 00:42:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 3f187327-1001-3379-93d3-2a69f5eec6ff | -9.0545 | -50.836399 | 2026-08-21 00:42:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbb972a8-252b-3532-9ae4-4b0a316f68b5 | -22.0749 | -46.561401 | 2026-08-21 00:42:00 | METOP-C | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8447116-00b4-3b58-aa8c-943ef491bb09 | -7.3527 | -45.827 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8bde21-ce72-3a8c-9d35-c8881fdcc243 | -7.4497 | -46.1521 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec55599-a5f4-3f89-82db-b9790c2b976c | -6.4242 | -52.745098 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac05567-70bf-3c28-8620-2b8baed6c039 | -6.8751 | -59.397499 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f314b767-9132-34f7-9d00-2696db1f78cf | -13.4455 | -51.794899 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 716ec9fa-0d8e-31d5-80fb-ad7c34b084d0 | -6.0634 | -47.822201 | 2026-08-21 00:42:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ded20c7f-e88c-3625-bcbb-9e1c2cb6e96b | -12.2701 | -43.152599 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41a3726c-8fd1-36ed-a194-db23d60bcb0c | -10.3026 | -50.295502 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c67a4304-37bb-3965-bd62-033d60875467 | -4.9535 | -56.2621 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12c6d090-66a5-3b1d-b965-27acc43cc0da | -6.3582 | -58.336399 | 2026-08-21 00:42:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54ad6f43-5b3f-3a6b-8d46-7740aaa741b7 | -6.5812 | -58.959499 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a519943e-d491-3f4b-80f8-a3a03a12008d | -8.0596 | -50.111698 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e35e6793-5aef-3778-b86e-2c98108a9cae | -9.3978 | -60.432499 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 629e9adb-8039-32a9-bc5c-3b8477f1a42f | -14.3369 | -51.904499 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1bfea140-3e8b-310a-bd05-628ccb7ac1fb | -12.4982 | -54.7388 | 2026-08-21 00:42:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 143e8480-3c7b-3fa8-a8ee-767f1a06ff3b | -13.9371 | -53.854801 | 2026-08-21 00:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
