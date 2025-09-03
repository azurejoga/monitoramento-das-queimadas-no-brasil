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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d4ae88f-d62b-36ae-bfb3-3960cde06527 | -6.85297 | -52.81748 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a957c7c-f6c7-36bb-b4ca-069bb214be23 | -8.06602 | -45.36546 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50e2b86a-d56f-3407-a165-16408b6ff30d | -5.90228 | -57.75224 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecd90c77-6240-32a5-a4cd-b150e927b7a0 | -10.54526 | -50.41664 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5475acb4-f241-3a46-b1af-6b7c85928eac | -12.09923 | -47.22365 | 2025-09-03 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de12aa6b-4d62-30e5-b2f6-b49b6d068ca5 | -11.60553 | -52.08413 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d32a432-c8ea-3524-ab31-70bf9064fc18 | -10.142 | -46.26076 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d0eee6a-1055-3686-a95c-4f8dafd3c491 | -11.9643 | -45.7882 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10d624d8-470c-36aa-8cc2-8a8007747412 | -8.36065 | -48.31517 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fddb90c-e7bc-3076-bb4b-e613d0770bf6 | -6.25211 | -42.60653 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c4f5559-a443-32e4-a74e-e8eac2ca3cdc | -5.90899 | -57.71226 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb02825-af7c-320a-b1df-81254eff20fe | -6.78553 | -44.4803 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9219276c-23e0-3ec7-95c1-5f694771d4ee | -9.64995 | -47.85923 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db4b5ddf-9c44-3a55-959c-c9440be90f0f | -11.59238 | -52.12515 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 415ee5d1-7a61-34a0-8cd0-698b8816cd61 | -10.06545 | -48.08774 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e949028-5d45-3257-bd5f-3ac679da3268 | -6.17859 | -43.31397 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2e8b8053-32c0-3a41-8a13-7eb9c1da29f8 | -11.64953 | -52.04083 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b84175e1-6ae7-3324-9e89-857f785f6cd8 | -6.89527 | -45.57531 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7c7eb56-7cf7-3cc4-93d4-34644834c965 | -9.75113 | -49.40509 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 901094b0-cdf9-3208-bc14-317db23afeaa | -6.47126 | -53.40542 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9c95e5-4144-336c-addf-11f60d791b66 | -9.64306 | -47.85342 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5920bc1b-8958-3130-8ac0-7ab211d65f24 | -5.80762 | -43.23391 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f3b9c3a-321d-3de6-94cb-6e5eb07a04c2 | -7.31671 | -44.26865 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 483173e6-b5df-316b-bc05-1bbc7d931520 | -6.28739 | -43.58213 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd83447-6371-3b59-940b-f60449caf5a2 | -6.81191 | -52.81467 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22ee0667-a08c-3ec6-8b84-c67a5dc9ba77 | -7.71572 | -50.25662 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4647b261-a654-3a0a-bb53-ac912d0df355 | -11.60117 | -52.11219 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b088c4e-0664-3751-b520-cc77c413e5d1 | -5.84772 | -45.63938 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2f5b6d8-bc79-3049-bd74-7ed3a6689359 | -5.50975 | -42.65202 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b37be0fb-c997-3781-9ac7-4c879a3c4725 | -6.97045 | -44.36826 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ede07d77-e003-3d0e-ad18-8e2d6f831562 | -11.01476 | -51.50694 | 2025-09-03 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50a44487-626c-3caf-b29e-68e8f2694f38 | -11.57704 | -49.90836 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bf7cb1d-6aa3-301c-8fab-68e4e4aa03d3 | -6.19821 | -43.35061 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 809358bc-d86b-319c-8974-8915c74974a4 | -7.32136 | -44.26928 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 656e22cd-3ff1-396d-bca0-5ac34baf31ee | -6.70583 | -48.3986 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5572c192-f98c-3c6b-8938-02b612577ef1 | -7.93039 | -46.54569 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ec0d754d-a759-3d48-876d-3fe4ea237171 | -6.46511 | -55.89089 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe43bff7-c43d-3dc5-bda1-92c205de51e0 | -6.79608 | -52.82706 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d463c869-bb11-391d-8bce-4a6b5c70a84e | -8.38748 | -48.28447 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbbedcf9-1037-3ba0-9a87-1948edfe36e1 | -9.75462 | -49.40563 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f960af5-6f31-338b-b20d-4b1b3047efc9 | -8.36552 | -48.30727 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bdc9e35-5e61-32f1-b3c4-faf918577e54 | -11.62311 | -52.05819 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f797376-35ce-39c2-9bec-c7b4fe2841d4 | -10.90038 | -45.79354 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c2eea3-d7b6-3530-9f0a-461664dcbe48 | -8.01921 | -44.10203 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce7d88a4-fc45-30c2-99b8-e5c6144c83ed | -8.86582 | -52.02987 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89ba2285-eced-353a-92b9-456e1e40a270 | -10.4505 | -54.78184 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5e6513-30ac-3603-ae6b-4875e296ba4f | -12.57718 | -44.77988 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 531b2a8b-61e1-3888-8119-ca8f10fe7d07 | -8.37166 | -48.29084 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 072a80ce-33eb-388c-8b36-df89fe3f3158 | -10.5368 | -50.42667 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5cd8a1b-c08c-3713-b612-d727ee0460dc | -8.88766 | -45.80753 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 159ae33e-741c-3181-83b0-2fc2b1cccf5e | -9.61165 | -55.38818 | 2025-09-03 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d245ace8-abea-330d-a49e-76f34ad5fea1 | -11.63742 | -52.05329 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ba261d-3e0f-3046-8011-c5a96b673949 | -11.59899 | -52.1262 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e3c7dd2-78da-3837-89cf-8320bfef9e6f | -11.19368 | -55.01217 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a276bf7b-06dd-3921-93f0-59b917e4b4fd | -5.59854 | -51.94734 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6328f9-0fff-360f-b9e5-ce6b4dcc3bc9 | -6.83286 | -44.77454 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3d3fd02-5ec5-3212-adff-10b9a3952aaa | -8.8565 | -49.57542 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 808dbea6-d7d6-3a99-b827-a1d2c1fee829 | -4.90124 | -49.92596 | 2025-09-03 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb53e18-504f-3090-a17d-3ffea913688b | -8.05294 | -52.34988 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b3b8bc7-6da8-3942-8837-de358cd96ee0 | -5.94132 | -43.03321 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2f575748-bbab-3ba0-b696-04ee8c9db3b9 | -5.91348 | -57.71291 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc45e047-2919-3bc6-a620-d8112b5a4465 | -6.49316 | -44.09882 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f07fa42-aabb-3579-8891-19abe9237b67 | -10.47541 | -53.63187 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 261eac16-e37a-337a-8700-6772b0841a5a | -10.91655 | -50.83688 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30232003-b91d-369b-8067-78f1276489a6 | -11.61817 | -52.06818 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2633862-91fd-371c-a2af-bde6ed254867 | -7.93791 | -46.55041 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b67cd88a-1cfe-3a57-9878-b0273e590197 | -8.8887 | -45.83193 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22f5ec0b-5035-3025-83b3-ded3d406b40e | -11.38594 | -43.56896 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c134b83-2799-342e-b372-7b261d8da491 | -9.46252 | -46.79209 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 129cb114-edcd-3828-b741-70e40cb36413 | -11.59753 | -51.93895 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e071a1b9-eccb-372c-8d87-b79d839524ca | -8.01617 | -50.09629 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3b568a9-2f0e-3d53-bef6-242c8f606641 | -6.22564 | -41.80215 | 2025-09-03 04:46:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8726993-c7b7-3f27-8110-59da63cea998 | -6.25817 | -42.63813 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bef4c596-29cb-3606-90ec-f8c06af28c13 | -6.7943 | -44.08647 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c73c1821-1bb3-3281-a019-824a36431ef7 | -7.72562 | -48.7436 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71d4aa08-3654-3356-910f-f59514ae32fd | -8.35204 | -52.52402 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2749f049-6ea8-3763-a16f-294ecb47980a | -10.10715 | -46.26046 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38cedb8c-1d67-350c-9333-bc4ad629acc1 | -6.27508 | -44.50199 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 491476b8-67ef-3f8f-bc6d-c6acfeb2c729 | -7.80227 | -45.45371 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d96d8a1-6f40-3ba4-baa3-552dda73e57e | -9.75171 | -49.40117 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe40b1de-d505-3b43-937b-b9af45c9b1ac | -11.62202 | -52.0652 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 896edb50-6208-3d6a-b784-ca20521ac242 | -6.26754 | -43.30533 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62f011ef-a0f0-36cb-9149-0b7d3a5f9e87 | -5.43623 | -45.97785 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bb43e33-0541-383b-903e-29c95a523c34 | -8.15073 | -54.93813 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d73eb05-e5ad-3374-97cd-67aee0cd95a0 | -10.14148 | -46.29621 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 385b06de-a356-36aa-b335-a48fe8223bdc | -6.52655 | -56.20795 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5d34273-f5b7-3782-8e08-23a6f2c955ed | -8.34483 | -52.52645 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5152335d-dd02-3adf-8729-e92ce1dcb49f | -6.84391 | -52.83097 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c666b2ee-bd1a-3989-918c-38a46d514a1e | -9.76421 | -46.92257 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e8c1f5b-3cd7-30b6-b8a7-ee9b0cfcfd41 | -6.77537 | -52.80519 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dece772c-5e0a-3268-b106-f3869215cd0e | -7.53535 | -47.44586 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ada4d57-30e3-3169-aa50-d21f6390ea23 | -6.3523 | -45.6553 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ac9752d-3625-3178-b216-f8cbed9c3559 | -5.9425 | -43.03389 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c6c5944-1603-376a-824b-194782e84ed5 | -6.0335 | -46.01637 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e15443c-7559-3c81-88cf-1adb02f74613 | -10.46588 | -53.62659 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39714cd-6355-3413-abe7-be8fbf9ad17f | -11.00922 | -46.93369 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9164eaf-c33a-3145-88fb-e07835f6aabb | -5.80754 | -45.62533 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62875f24-56d2-328e-8fd7-ac1da51e835b | -5.69464 | -45.94464 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be66d334-4ba6-39a7-868b-332c91b47dfb | -5.89478 | -57.742 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3250a39-db90-336f-83e9-06510753875f | -6.84729 | -52.8315 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
