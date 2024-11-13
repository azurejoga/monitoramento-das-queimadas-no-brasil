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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891adc33-790a-3509-bbb5-30569892fcab | -10.7425 | -49.5244 | 2024-11-13 05:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a481d6af-29dc-3980-b1af-9af573aa9a04 | -3.0689 | -50.3326 | 2024-11-13 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 8283244f-1d2c-308b-bfbd-651cd73bc2d7 | -17.62156 | -57.53985 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9e457aa7-8896-3ee9-a7f8-c8c0349338af | -17.59133 | -57.53856 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2fbf333f-99ca-3941-8551-02e58b0cdd50 | -17.5847 | -57.53742 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0c625f71-e008-32e5-8039-dac7656cde4c | -17.58585 | -57.53017 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 74497983-5f24-352e-9a67-3310ddecdd9e | -17.60071 | -57.54389 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b9129e2b-4023-3c2a-9f83-a5afdd66c0d6 | -15.56985 | -47.85503 | 2024-11-13 05:01:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a68e6c22-f816-3e50-9dc8-25ab78747a47 | -17.62099 | -57.54347 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2ca7fb45-af77-3c8f-b861-63b6816990aa | -17.63209 | -57.53794 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3dd36f18-afcd-3323-b89c-57e63641d006 | -17.58642 | -57.52654 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b375b407-fa66-3430-8a60-e699abd135e6 | -17.6354 | -57.53851 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0d8c4b88-bbb3-3d23-8561-2d2995b91f69 | -17.59388 | -57.47944 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 93470cd4-4313-358f-8bf5-9caa033e8472 | -17.60013 | -57.54752 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ba6382e9-c90a-36fb-a6d6-cb88996e0edb | -17.68746 | -57.53257 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b6c6e2be-3418-3611-b908-8792037a582d | -17.58801 | -57.53799 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fdee1c45-5e21-31eb-b106-b0573c8e342d | -17.63151 | -57.54156 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a4edd43e-3cd8-3b35-bf86-97362a4426a2 | -17.68357 | -57.53561 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aa0dc939-c336-3a3b-a24c-d07671d5123c | -17.5935 | -57.54638 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0516bf4e-88bd-3583-9fde-e501c4fadb52 | -15.76463 | -46.17503 | 2024-11-13 05:01:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d37cd6b-3770-3d87-98c9-059543636469 | -17.63483 | -57.54213 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4cb943b5-1da4-3a67-9068-c6cbfac09bdd | -17.59682 | -57.54695 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a877b5f-3c16-311b-8758-09aaeb212109 | -15.76214 | -46.17579 | 2024-11-13 05:01:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a9a36ff-9899-36cc-b1d6-28542bacf401 | -17.62704 | -57.54824 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7ea7020f-4e2b-3794-96d1-6002d54de93d | -17.61066 | -57.54561 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6d84ae1b-d601-33c0-8df5-a740972a0e7b | -17.60109 | -57.47696 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 59b2d0e8-645d-3988-a2e5-e055b993cbe2 | -17.59937 | -57.48782 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e2ba7422-9565-3039-96a9-cac91a645e84 | -17.68962 | -57.54039 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d026c0f2-e92e-3610-aa9b-42af9e5ce3d3 | -17.68631 | -57.53981 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8fc4c8ea-5c5f-391a-909c-01e2553f96b8 | -17.58744 | -57.54161 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d9f4ad72-1e85-3edd-bd12-87cfb6bd0964 | -17.6902 | -57.53676 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e89e8cb2-8639-33ce-b1a3-46d9e51191b1 | -17.59465 | -57.53913 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 398a5168-56e8-3e04-8490-fdefa7671279 | -17.59662 | -57.48364 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8fd2d9ee-3d7b-3035-a07c-2ca31d61ae76 | -17.5972 | -57.48001 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cd3198c2-c86d-3e82-bc99-61047aaf948a | -17.63093 | -57.54519 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 76355633-3755-31c3-93da-96668abb9d30 | -17.68299 | -57.53924 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a62f92a6-812d-39c5-b7bd-c100a83a610f | -17.59273 | -57.48669 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 161c0c04-d476-309f-a91e-cf98fff2c93b | -17.60677 | -57.54866 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e7142b8a-9457-305b-a912-a8498ff346ef | -15.78346 | -46.43074 | 2024-11-13 05:01:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3eb8e2f7-aebb-377e-b0b5-fd2d88e5eee3 | -18.68304 | -47.96516 | 2024-11-13 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94fe2e37-1dd8-3292-ad6d-65994625a96e | -17.58527 | -57.53379 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fc4dc88b-e00c-38b8-96b4-ec7f0b931685 | -17.59739 | -57.54333 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5fb300ce-8873-3d96-a0a2-d8fd29e813df | -17.60051 | -57.48058 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 986bc92f-3b02-36e1-b0b0-f54024c5ef52 | -17.62488 | -57.54042 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 384b20ea-8626-3215-b09c-027776576e1a | -17.58138 | -57.53685 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fe4f2497-557a-390c-a949-9dd6b51512b6 | -17.60402 | -57.54447 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a08eee96-76a5-357a-8beb-200b7f45cc56 | -17.60325 | -57.48478 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f6f1a8ba-73cb-33f2-b034-76b8316c4c0a | -17.59605 | -57.48726 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6dfe8e72-8b96-3aa4-a589-fbf5dc72f603 | -17.60345 | -57.54809 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04989170-4622-3145-9dc4-0467b2e32e88 | -17.60383 | -57.48115 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d3f6262c-90b2-36d6-ac3d-2b2d396d6295 | -17.62819 | -57.54099 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d97551aa-261e-3840-a092-60fa0cbd3963 | -17.68688 | -57.53619 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e11da29d-66f9-3165-8064-e2318e428554 | -17.59407 | -57.54275 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6cdfa453-de6a-3c27-a932-b0a52550a491 | -17.59331 | -57.48306 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 44eb9c64-ee6e-3a19-a8b5-76459cbd07b1 | -17.6243 | -57.54404 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 24f2ed75-efb9-32a4-acbf-de5502cc1b50 | -17.58195 | -57.53323 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2a2e9f52-bda9-3672-94aa-f8dc40c75fa3 | -17.58253 | -57.5296 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dc7e1b42-fd97-36fe-9fee-11bea8d34679 | -17.59797 | -57.53971 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5d873a06-4159-3a3f-8b57-40126ece945f | -17.62762 | -57.54461 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b13e7b74-97c2-3e4b-b835-0faf8f2b90a1 | -17.59777 | -57.47639 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bf71b139-a2b3-3d89-ad03-30416a0dba31 | -17.69205 | -44.64903 | 2024-11-13 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66cb0534-bbf2-3c51-9ba0-7e505c4ec84b | -17.59994 | -57.4842 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3dc4b0ce-a6de-30c5-a126-e45cd1ec0e20 | -17.61377 | -57.54596 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1067d0ee-253d-314d-8f91-a7199895c2e7 | -17.58412 | -57.54104 | 2024-11-13 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9fce9f8c-b0ce-3c67-b258-3425b67727b6 | -12.21568 | -54.22683 | 2024-11-13 05:01:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b661b04-a438-3f86-a1be-931c523b5f2b | -23.95938 | -54.04362 | 2024-11-13 05:03:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 66046564-17fd-33b4-b72b-94fd42426d2c | -19.62338 | -54.15204 | 2024-11-13 05:03:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8749a32-20fd-3bc3-8e22-e5df4c0a0fbf | -21.0495 | -47.2491 | 2024-11-13 05:03:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8301dd54-9c36-3abc-8aff-da1b36d0d26e | -28.58881 | -49.44146 | 2024-11-13 05:05:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0624de36-98fd-3833-8501-988c72fa6ab9 | -29.52633 | -49.88895 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 13.7 |
| b45ff1bf-bc62-3759-a2cc-5ae70f0f0cef | -29.53193 | -49.88583 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 13.7 |
| a42776a8-e4f5-3085-b84f-83987be46d05 | -29.52663 | -49.88526 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 13.7 |
| b05d4242-fe5a-3e1f-ab3c-ea0b01616899 | -29.53104 | -49.88381 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 16.4 |
| 31c66c49-b9f8-3b2b-b2d9-b4be8466d5d8 | -28.91274 | -51.96824 | 2024-11-13 05:05:00 | NOAA-21 | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a923078-ab9b-3c52-aae9-2bc7e51af2f8 | -29.53076 | -49.88752 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 16.4 |
| 42bb52fe-b57f-32b4-88df-b52c9d7ac270 | -29.53162 | -49.88954 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 13.7 |
| 4f0d0246-45f1-3a16-9329-1e9761e068a8 | -29.53131 | -49.89324 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 6.9 |
| 0cfb3005-140f-3531-89a8-12aa0989f5aa | -28.9081 | -51.96786 | 2024-11-13 05:05:00 | NOAA-21 | ANTA GORDA | RIO GRANDE DO SUL | Brasil | 4300703 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34d0ea2a-4fe1-37e9-aa1c-63dad35ed522 | -29.52547 | -49.88692 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 16.4 |
| 82fb80c9-51c3-3cce-93e3-89edc1b12f3f | -28.91157 | -51.96865 | 2024-11-13 05:05:00 | NOAA-21 | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1ffedc18-8cb7-3c5c-847e-d5e359e0f29d | -29.53048 | -49.89122 | 2024-11-13 05:05:00 | NOAA-21 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 20.3 |
| c6b53ea7-367b-3b5a-89f4-3c49f4d8969b | -29.9118 | -51.05425 | 2024-11-13 05:05:00 | NOAA-21 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| c072ac82-0974-37c4-8093-4aff15cb245c | 1.0663 | -60.5985 | 2024-11-13 05:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1510a985-7f45-339b-a819-6b2a8a2683ce | -3.0689 | -50.3326 | 2024-11-13 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 873cc033-fc33-3792-bfb2-9d58e9f7d3c5 | -3.3519 | -48.9475 | 2024-11-13 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d85dbd5b-55d2-373a-b231-1826b7e7a42b | -10.7425 | -49.5244 | 2024-11-13 05:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ac1e6526-e626-3058-8517-9259639224cf | -10.7235 | -49.5265 | 2024-11-13 05:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| cbe66305-9fcc-31e0-9a2e-86928af820d7 | -3.3518 | -48.9689 | 2024-11-13 05:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c97d9173-96fb-35ce-ab07-3e894a75374b | -3.0504 | -50.3332 | 2024-11-13 05:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 7ebc3a8b-f646-3f6d-9d1f-7700d3ba52fb | -3.0504 | -50.3332 | 2024-11-13 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ca345d53-6b80-3af8-b16e-99be5d058b1c | -3.3519 | -48.9475 | 2024-11-13 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ea8c56d2-384f-3281-8974-7ca66aff2c7b | -3.3518 | -48.9689 | 2024-11-13 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a8fc09fd-7b3c-3125-a45a-ff96e76f7d3a | -3.9483 | -48.1724 | 2024-11-13 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 4f5a58a7-293d-3714-8570-a61bee144326 | -3.0689 | -50.3326 | 2024-11-13 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| df3c3fd7-4d94-3f5f-a0bd-91e0e21b42b8 | -10.7235 | -49.5265 | 2024-11-13 05:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9751588f-e730-374e-a0d8-573927eeee29 | -10.7425 | -49.5244 | 2024-11-13 05:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 06807d5d-9136-3278-8e7f-b36ebacc1aae | 1.13924 | -60.60231 | 2024-11-13 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 302c3dfc-65aa-3571-8c22-8c60cbfee6be | -2.30902 | -53.97958 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3c11ac-47cb-3f9f-a642-88cc49454921 | -1.60878 | -52.4978 | 2024-11-13 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 634602d5-03db-30ca-9276-f3bb09c03729 | -1.57931 | -53.73701 | 2024-11-13 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README43.md)
