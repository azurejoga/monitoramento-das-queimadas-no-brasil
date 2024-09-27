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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 472da16d-1a67-37fd-8a1b-2b18804e006d | -12.1972 | -50.774601 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fd113ca-1cce-3fe4-a72c-3d002f0df844 | -12.2007 | -50.788399 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d632fa2-29e9-31c6-a880-5dd287465113 | -12.191 | -50.790901 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b4441f5-036f-326f-9259-1045f493fba6 | -12.1945 | -50.8046 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4d3c7d8-b047-34d0-ac1d-2bdbd1175acb | -12.198 | -50.818298 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 333f22b3-f929-3a9e-8878-6eb5b43d8e99 | -12.2015 | -50.832001 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29451118-c5a2-3acc-a0ba-ed1032f45f97 | -12.2049 | -50.845699 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 053234a8-98c2-342b-b4dd-6f4748821b61 | -12.1812 | -50.793499 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 288e1f24-0491-3271-8758-8abbb03239c0 | -12.1847 | -50.807201 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63c3fd3d-81b2-32ad-956d-611fc0e22ed4 | -12.1882 | -50.8209 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44bb0c42-1a8b-36de-9c67-d9ddd439d625 | -12.1716 | -50.796001 | 2024-09-27 01:28:03 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cdaa087-e4ef-3145-89c9-e796d67c68b9 | -11.8401 | -49.623901 | 2024-09-27 01:28:04 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8e1a68c-f422-3113-bd77-78d278d6132c | -12.8613 | -54.004902 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec357072-1191-30ea-9967-fc3661531f11 | -12.8634 | -54.013599 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc18ee6f-f0b7-316e-8049-1d38f316e18f | -12.8655 | -54.022301 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc5a5f6-e8e0-3afe-8944-aee577ab8a1d | -12.8494 | -53.9986 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 095fd39b-9a80-33e4-939d-d1bc544df145 | -12.8515 | -54.007301 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40affc81-b893-3dff-b7b7-2d5a3b61582c | -12.8536 | -54.015999 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b51d986-9e23-3625-87bc-187634c4b538 | -12.8557 | -54.0247 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26e7c8d2-577b-34d8-822a-027cf551cd7a | -12.8578 | -54.033401 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10fe0264-8794-38b8-b389-9ab125727897 | -12.8599 | -54.042 | 2024-09-27 01:28:05 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24a7a96a-e9d5-361a-89dd-e61bd135fe79 | -12.526 | -53.175598 | 2024-09-27 01:28:07 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06d02d04-2a0b-3da8-8f96-47b2417d7b1e | -12.7351 | -54.081902 | 2024-09-27 01:28:07 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5a8773d-3a61-3214-bf2b-a7fd80d67a19 | -12.7372 | -54.090599 | 2024-09-27 01:28:07 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0e5091-f5ec-37ed-8abe-0fca8c2a95c1 | -12.7232 | -54.075802 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| faaddc5e-0648-3def-a963-5063d54f1f1c | -12.7253 | -54.0844 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed8376f-1aff-3a19-89a4-44913d902f88 | -12.7094 | -54.060902 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1532a12-bb77-3dc4-9720-f2f43a828de8 | -12.7073 | -54.0522 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c282f080-41b7-3472-93b6-8b033a6dfac0 | -12.7115 | -54.0695 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d502a9c-c829-31f0-85bf-2438c67ca9b4 | -12.7135 | -54.078201 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8da44c-abd8-304a-92b8-342ff25b68c4 | -12.6933 | -54.037201 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3e313b-a0ef-368f-b010-865fd23d8951 | -12.6954 | -54.045898 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3972c881-5953-3a97-b909-c10e9fb6a675 | -12.6996 | -54.063301 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab06efe0-b0bb-3143-9638-8851dfead11f | -12.6975 | -54.0546 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0fd0cda-8dda-34e6-94f9-351ac475a0bb | -12.7017 | -54.071899 | 2024-09-27 01:28:08 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd3aa8f6-8cb1-3616-8ada-898c16fd78dd | -11.132 | -50.812199 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a44a71c-b348-3b52-ba85-20da915cc68e | -11.1356 | -50.826401 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7140a20-5468-38fd-a69b-6313d782fe2d | -11.1392 | -50.840599 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58bbfdae-7288-3d9e-b180-3d169fcf6a20 | -11.1223 | -50.814701 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 184d2cdf-ffc8-36a2-b8ff-80726f855093 | -11.1259 | -50.828899 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf7c68e4-b4e1-3ff6-b158-493e3b764daa | -11.1295 | -50.843102 | 2024-09-27 01:28:10 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc8a4e86-5ba1-3727-b856-595d64abc79c | -11.056 | -51.412601 | 2024-09-27 01:28:13 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af0c6756-ea85-391b-8fef-b0b64cdf051f | -11.0593 | -51.425598 | 2024-09-27 01:28:13 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e87ca866-3851-306b-b626-d19f9fb4e107 | -11.0463 | -51.4151 | 2024-09-27 01:28:13 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5f39929-84c4-31ad-bddd-5ae090f148ad | -11.0496 | -51.428101 | 2024-09-27 01:28:13 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23be36a0-8b94-33b1-8cb9-e7f7a064b08a | -11.684 | -54.439499 | 2024-09-27 01:28:15 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7b851c1-ad1c-3dff-b925-f4d4499be901 | -11.6722 | -54.433399 | 2024-09-27 01:28:15 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3098d076-c767-3ccb-9620-25070f108101 | -11.6742 | -54.441898 | 2024-09-27 01:28:15 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39631ed8-bbfe-3266-a42c-e08dde5f6560 | -11.6763 | -54.450401 | 2024-09-27 01:28:15 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a4007ed-add8-34a1-9acd-c68e4cd5ed8b | -12.4473 | -54.9995 | 2024-09-27 01:28:16 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6729d8eb-a606-36dd-bc58-04f2fea0a18f | -12.4454 | -54.9916 | 2024-09-27 01:28:16 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 929bada5-9dbf-33c7-b54c-25f46e002f13 | -10.7346 | -51.0793 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5ebdc3a-97da-3b32-a533-102e13729235 | -10.7381 | -51.093201 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d070d57-90c6-33e2-aea8-69120e58bbf1 | -10.7214 | -51.067902 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1828b53e-9727-3455-9c7d-194f20f699c5 | -10.7249 | -51.081799 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6654ef61-55df-312b-8546-edfb1fe4d5c4 | -10.7284 | -51.095699 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 147cafa0-5332-3805-881d-f17d997bfd0a | -10.7152 | -51.084301 | 2024-09-27 01:28:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25454868-1714-30e1-b1ab-e246166c2592 | -10.6182 | -51.1091 | 2024-09-27 01:28:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb2ae80a-4376-3827-9b85-c51a1ff02a56 | -10.6217 | -51.123001 | 2024-09-27 01:28:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa7ce0ea-783a-349b-8caa-b3327f09bc7d | -11.319 | -54.0382 | 2024-09-27 01:28:19 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd5add1-4c64-3d3a-8669-0c60a5c4c6a8 | -10.4721 | -50.734798 | 2024-09-27 01:28:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f45c237-d945-3bd5-a4ba-e22082c62a54 | -10.4759 | -50.749599 | 2024-09-27 01:28:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c5e440a-a6d4-3812-994b-c8f165a953df | -10.4796 | -50.764301 | 2024-09-27 01:28:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60e6916d-06ad-3c82-8a71-3d0e5d5c188f | -10.4662 | -50.752102 | 2024-09-27 01:28:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f13990b-43fb-3e97-84c6-34055d8b1978 | -10.4699 | -50.7668 | 2024-09-27 01:28:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f5c6afe-2269-3cf0-8ec3-426c9fb513c0 | -11.2038 | -53.903 | 2024-09-27 01:28:21 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e836de2-c107-3696-ba41-dd8e06542e6b | -11.1918 | -53.896198 | 2024-09-27 01:28:21 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58a5240e-b8b3-3824-bc8a-3e91c9102beb | -11.194 | -53.905399 | 2024-09-27 01:28:21 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e50127a5-f4b1-3b45-bd5a-7061f3e293c2 | -11.1962 | -53.914501 | 2024-09-27 01:28:21 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c24a7d8-6683-36d9-98d3-cbeb96fe14bf | -10.49 | -51.215401 | 2024-09-27 01:28:22 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9640946d-8717-373a-9664-e14a4093f8ef | -10.4935 | -51.229099 | 2024-09-27 01:28:22 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddf0f388-f168-3f21-a19a-8af58ed07e87 | -10.1404 | -49.998901 | 2024-09-27 01:28:22 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 457c5bb0-e9ce-3fc1-8c68-aa721c32dff8 | -10.1447 | -50.015598 | 2024-09-27 01:28:22 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56fbb313-2660-3f31-aea4-3d42a595b91e | -10.1307 | -50.0014 | 2024-09-27 01:28:22 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89053935-bea0-3511-bbc1-077bc5523566 | -10.135 | -50.018101 | 2024-09-27 01:28:22 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f46576b-7a6a-3265-bf08-d687808a1597 | -11.1453 | -54.175301 | 2024-09-27 01:28:23 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61fb0d55-8b4d-342a-a66f-0b0ad3ec2a97 | -11.1475 | -54.1842 | 2024-09-27 01:28:23 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5759f33e-be93-3720-ba76-73aae6194165 | -11.1356 | -54.1777 | 2024-09-27 01:28:23 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43119c1a-a131-3bd9-90d5-c6346f638134 | -11.1377 | -54.1866 | 2024-09-27 01:28:23 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72a483d1-93ff-3c2e-aa75-bf9b7991817d | -11.236 | -54.7705 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8785f94c-64ea-3566-8d54-4d8abc029e25 | -11.238 | -54.778801 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b62af9cc-6ac8-3488-a19a-296e44c31fb7 | -11.2399 | -54.786999 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b88f8bb1-dddf-33cc-81d4-9a8bc432b893 | -11.0391 | -53.991699 | 2024-09-27 01:28:24 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83de6d0e-d2cf-3513-a5dd-49fc76422e68 | -11.2263 | -54.7728 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aebcf045-1e6b-3095-b853-850788b59334 | -11.2283 | -54.781101 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 413a66e8-771f-3425-911f-4341b8700489 | -11.2302 | -54.789299 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82afdcc0-53af-32d6-a935-912922239263 | -11.0161 | -53.939301 | 2024-09-27 01:28:24 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f924c7de-f350-33d3-aeb7-431e2ac11b68 | -11.2106 | -54.750301 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebef556-f8cb-3c17-9e04-78965ecf2219 | -11.2125 | -54.758598 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61400bbf-a53f-34f8-a778-98a2129724e3 | -11.2145 | -54.766899 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7405a42b-d652-3940-8a5a-cc4e6d56e95f | -11.2165 | -54.7752 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34828ae1-a876-3d46-ac3b-985018aa0218 | -11.2008 | -54.752701 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9461c085-ff42-397c-a266-f92bfc912ced | -11.2027 | -54.761002 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35bb19f3-3807-3dc0-b173-cc7f22b3517d | -11.2047 | -54.769299 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31bb9e63-4c26-355a-8b88-e0d6bb4a514e | -11.2067 | -54.777599 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f899da1f-903a-37c2-8575-c80aaf08a15b | -11.1832 | -54.765701 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85a8201e-26af-3183-a341-fa5fe97f50ec | -11.1852 | -54.773998 | 2024-09-27 01:28:24 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03f20b9b-601e-34e8-b929-bf5ad53c878c | -10.7745 | -53.538399 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80d906b9-f34a-37fe-8e43-7f7acb27d740 | -10.821 | -53.730301 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 383e5524-4985-3cf0-be91-a03d47476ffb | -10.9348 | -54.245399 | 2024-09-27 01:28:26 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README34.md)
