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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f70e4785-7bf7-3656-b1e0-6aad4501e909 | -3.53776 | -42.15755 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| aedcd75d-b661-305a-baf0-00f0360ab203 | -3.53092 | -41.69862 | 2024-11-03 12:16:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e2765a25-5eb2-3013-8d43-b4f293217f0c | -3.48742 | -42.17982 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 7c3489c2-e2fc-3c20-bf3f-e64f613b6e39 | -3.48599 | -42.18945 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 3ce9e96d-8731-3c9f-b8e2-eaeff131d298 | -3.48456 | -42.19913 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| debbf2fd-990c-318d-a341-476fbf57185c | -3.47532 | -42.19783 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| c7ffd986-1234-3823-a477-964d93657a46 | -3.47388 | -42.20751 | 2024-11-03 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 30ec7939-7107-3941-8aab-45da1334ce05 | -3.36245 | -42.15954 | 2024-11-03 12:16:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 86.6 |
| f65d6f98-c52b-3549-8e34-fcd90a8b92d1 | -2.97891 | -41.75401 | 2024-11-03 12:16:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3418f3b2-a15f-3904-ad57-f76d5b4348b8 | -3.13446 | -42.39357 | 2024-11-03 12:16:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 600b044e-19f3-3a10-9e1c-cd1a7df5fd3e | -3.12509 | -42.39233 | 2024-11-03 12:16:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| b56e9bd0-397e-3e04-b42e-effc067d119a | -3.12363 | -42.40227 | 2024-11-03 12:16:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 614e04a8-17aa-34be-9929-e8cbe7fb893a | -3.06215 | -42.00001 | 2024-11-03 12:16:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 30150eea-be7b-3ab6-a22b-7ca0e568b7d5 | -4.55831 | -43.10746 | 2024-11-03 12:16:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| a2f31081-d7fb-3396-bb00-b1c958418c2e | -4.55676 | -43.11788 | 2024-11-03 12:16:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d176063b-671f-310f-8c98-384264d947d2 | -3.70136 | -42.73306 | 2024-11-03 12:16:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2a8a137b-991f-35d3-b5dd-834367526089 | -7.54785 | -42.85902 | 2024-11-03 12:18:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d9f90e0d-aba5-351b-8f86-047d233ed262 | -7.52669 | -42.87539 | 2024-11-03 12:18:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 950cdd25-518b-3c2f-9287-7a362c86f866 | -6.6402 | -43.4376 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 83065523-012c-35c7-b989-7776eb93d592 | -8.00877 | -43.3505 | 2024-11-03 12:18:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| dc56afac-19a0-3e44-bbfd-85aab07631e1 | -8.0031 | -43.34369 | 2024-11-03 12:18:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d1b12705-490b-3242-bb0a-52461977a019 | -8.3466 | -43.62019 | 2024-11-03 12:18:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d6f138d5-ce24-35d4-be84-cc1564253dff | -8.33874 | -43.60869 | 2024-11-03 12:18:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d1d15284-3bb0-3e46-b4ac-ba4ed54f1ac3 | -8.33719 | -43.6188 | 2024-11-03 12:18:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 30dc19a5-a518-33e9-a505-6fc47f0a0b65 | -10.25874 | -43.36811 | 2024-11-03 12:18:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 125feae2-732f-3ec8-ad00-af6e1ea5e50d | -10.00827 | -43.80645 | 2024-11-03 12:18:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 2cb1ea40-99a9-3559-bb23-1b87acd9c455 | -9.79577 | -43.86457 | 2024-11-03 12:18:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 818eafad-8feb-3220-87da-b446469f24bf | -9.79424 | -43.87461 | 2024-11-03 12:18:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8dffaa76-2bba-3158-ba60-366ef8847b42 | -11.13554 | -43.30494 | 2024-11-03 12:18:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 62f6a5f1-82d2-31ab-b771-30631ad6d5fd | -5.23183 | -43.47097 | 2024-11-03 12:18:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d93cc818-75bf-35e6-b7f7-1f8712f0ce2d | -5.23023 | -43.48158 | 2024-11-03 12:18:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2b724fec-cb36-3027-b076-9248ebb1878e | -7.96309 | -43.90731 | 2024-11-03 12:18:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c021839b-8996-30fd-a69e-0a2f0fb33cf2 | -7.9615 | -43.91785 | 2024-11-03 12:18:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| eea8e5e1-e1ab-3f4d-aebb-91a2a9875f48 | -7.95188 | -43.91653 | 2024-11-03 12:18:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 33a61f6c-7c16-3fc9-9b84-7da2cabc513e | -7.37084 | -44.36502 | 2024-11-03 12:18:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 533dae41-bac7-32b0-aefe-83b0237fa30d | -7.36916 | -44.37622 | 2024-11-03 12:18:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 49a10358-6ded-3ea0-9025-53ff80c0a078 | -8.49416 | -45.47062 | 2024-11-03 12:18:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9be33655-0795-309c-8575-85ddcb58cc02 | -8.13995 | -44.02292 | 2024-11-03 12:18:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 992f84dc-eaa0-392e-b677-36b75c4c0b7c | -8.13032 | -44.02138 | 2024-11-03 12:18:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3b5e8e50-17f0-3beb-adc4-9484997b0748 | -9.4881 | -44.93063 | 2024-11-03 12:18:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b0210e11-5644-3845-b869-e56cb85fafb7 | -10.89758 | -44.89279 | 2024-11-03 12:18:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2ffcfde7-ebf7-3fe1-86c2-0a1eed6c6856 | -10.89586 | -44.90409 | 2024-11-03 12:18:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fe933c0f-9463-3e90-adbd-3d75641fcb13 | -10.90737 | -44.89436 | 2024-11-03 12:18:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 81bf675c-14be-3f69-81ad-145889f4413f | -10.90567 | -44.90556 | 2024-11-03 12:18:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fc9c5221-8acf-3e10-9473-c903dae72d2c | -8.03 | -45.87481 | 2024-11-03 12:18:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3933dcd9-c726-3a8e-a09b-c60b47aab8e0 | -4.77048 | -48.97049 | 2024-11-03 12:18:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d11ce87e-31b2-31c0-8224-dc954c6f01ac | -4.76933 | -48.97622 | 2024-11-03 12:18:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8e8e511b-b171-31b3-b8b5-97a1bfafe202 | -8.18304 | -35.2797 | 2024-11-03 12:18:00 | TERRA_M-T | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| 3cde1c55-f007-3116-bd5d-e1628cde8b88 | -7.8009 | -37.66993 | 2024-11-03 12:18:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 18.3 |
| d5dcfc94-fc2a-391e-8fee-febfc36ad9d7 | -7.90003 | -37.48146 | 2024-11-03 12:18:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 24.0 |
| be23462c-10a5-34cb-a16f-a2c2382c1b87 | -7.8983 | -37.49408 | 2024-11-03 12:18:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 27d82329-46a8-3ba2-91fe-2232acfbf97f | -11.05834 | -37.38279 | 2024-11-03 12:18:00 | TERRA_M-T | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 00dfa63a-2d14-3027-a152-d7c9d767694e | -7.84581 | -38.8511 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 622acdd1-3686-31c1-b1b4-fe89043cf280 | -7.84439 | -38.86145 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 0fed40f3-24eb-3b5c-a77c-d01562549903 | -7.79214 | -37.67467 | 2024-11-03 12:18:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5f1337dd-4a6b-3709-98ea-a199d88ee0ee | -7.29297 | -38.03048 | 2024-11-03 12:18:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 2beddf06-0f3c-3979-9e6c-2a753378d3f3 | -7.15564 | -37.84157 | 2024-11-03 12:18:00 | TERRA_M-T | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 11.2 |
| f864918a-953d-39f0-8bb6-ef24fdfa7b36 | -6.61203 | -38.07771 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 6f0e294f-7293-37df-b579-aa4068a15c95 | -6.60068 | -38.08731 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO FRANCISCO | PARAÍBA | Brasil | 2513984 | 25 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 0e16ac06-0d21-369b-ac46-092ca35f2b3a | -6.28937 | -39.51738 | 2024-11-03 12:18:00 | TERRA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 338631b0-83df-30fa-8d7c-2ad73fbc3918 | -8.83615 | -40.86122 | 2024-11-03 12:18:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0a45ef66-84cd-352f-a8c6-fff41cb31648 | -8.83487 | -40.87022 | 2024-11-03 12:18:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4aeb097e-7d8b-3097-a59a-b842c9dfe8c8 | -8.5449 | -40.31371 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 43a0c278-f8dc-38bf-9a39-e7df64d08f6e | -8.53399 | -40.83964 | 2024-11-03 12:18:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 6c17c9ea-7297-31af-9fa7-c8ab91c1cdd4 | -8.53271 | -40.84858 | 2024-11-03 12:18:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7c33ca75-a431-3c5f-bcd7-484790005fcb | -8.5251 | -40.83838 | 2024-11-03 12:18:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 71e83fac-23e9-30df-a72a-c4e134639b4a | -8.52382 | -40.84733 | 2024-11-03 12:18:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 488e7754-c163-33a7-aa2e-6d841abee649 | -10.24906 | -40.37912 | 2024-11-03 12:18:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| dd6aa0c0-8382-3185-bac2-f09df878b9c2 | -6.31659 | -41.56942 | 2024-11-03 12:18:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d36bbf53-9124-32b1-a2d7-88c1c01eaed9 | -5.99943 | -41.91011 | 2024-11-03 12:18:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 06610cc3-174d-357e-a3d8-6fb256d7b92f | -5.99046 | -41.90881 | 2024-11-03 12:18:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| e7245107-1102-3d0c-9789-e6188b14ef5f | -5.59511 | -41.65196 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 37a1448d-1350-3782-9cd2-b7cb60b5478b | -5.59379 | -41.66096 | 2024-11-03 12:18:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 66e6708b-176b-37cd-b0d4-b8f0fa8d1018 | -6.5334 | -41.48263 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 267d4833-2cf8-3bc7-8948-82c4d707d66f | -6.5321 | -41.49153 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| d435b698-2c36-3046-8fa9-f91175185db6 | -6.52255 | -41.48369 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| b4e6ca88-03f5-354e-a056-bbb71ddf1b9a | -6.52126 | -41.49258 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| c3f72cb0-27ad-3ce4-9ed3-f4d49d4ac301 | -8.84469 | -41.11826 | 2024-11-03 12:18:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 644517f4-2b53-3b10-a539-b543aba89a3e | -8.51443 | -41.61504 | 2024-11-03 12:18:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 66f866e7-1f9e-3745-bb17-22ba6d50700b | -8.45203 | -41.34626 | 2024-11-03 12:18:00 | TERRA_M-T | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fb5acf34-3395-3425-ad49-1ff4f48892ad | -9.9585 | -42.09311 | 2024-11-03 12:18:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 7691e86a-e5f9-35cc-9a5e-b66da3acf414 | -11.21847 | -41.60661 | 2024-11-03 12:18:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 850e3af5-179c-319b-ab27-00acb0418999 | -11.21719 | -41.61561 | 2024-11-03 12:18:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 440f3460-69c2-382b-a625-7b6a4434a75b | -5.59475 | -42.96201 | 2024-11-03 12:18:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 8f54fe2e-cbdb-3b8d-b459-d2ca9ec2e673 | -5.1513 | -42.90731 | 2024-11-03 12:18:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f4e8d83c-f5bf-3ffc-b66a-b6b322cbcf4b | -5.14982 | -42.9173 | 2024-11-03 12:18:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff88e938-19ab-36af-a9d3-72287a2f720c | -7.66042 | -42.78506 | 2024-11-03 12:18:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| c532997e-ffe3-3feb-bc47-8f9d186686b0 | -7.65552 | -42.75547 | 2024-11-03 12:18:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 5fc72a90-0c19-3aec-9d13-8fcd502c2ce9 | -11.84129 | -43.82782 | 2024-11-03 12:21:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 218a0d50-4b77-35a6-9b05-0ff1a37d999c | -11.83983 | -43.8375 | 2024-11-03 12:21:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3b3e30bf-3333-30ce-8716-4be8cb6b6b37 | -11.83213 | -43.82644 | 2024-11-03 12:21:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7932767d-5350-3f4d-9eda-f005f9052e2e | -11.83066 | -43.83611 | 2024-11-03 12:21:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dd0b690b-37b1-346b-91f3-a8037d0e7d08 | -12.61964 | -44.17258 | 2024-11-03 12:21:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 98044f39-0609-3b43-9325-15687f5d821e | -12.30302 | -44.30841 | 2024-11-03 12:21:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8c3e2294-bb26-3e66-bf90-a28d59cdf4bc | -15.10346 | -44.10521 | 2024-11-03 12:21:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 9.6 |
| af3173e1-25e6-330e-bbcb-8ce4e7305ca4 | -11.25357 | -44.78216 | 2024-11-03 12:21:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 80f23e91-bc36-3c8d-be52-d6c44945568e | -10.42374 | -49.49046 | 2024-11-03 12:21:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b4be4e40-a1bb-3058-a040-9d9473852258 | -14.29711 | -43.06939 | 2024-11-03 12:21:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| b85e90a6-b1a4-3a97-b03c-f7d337e5a9f8 | -14.29578 | -43.0785 | 2024-11-03 12:21:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 64c7a27f-4275-3107-8c44-f3965c3f3ea3 | -13.95865 | -42.79873 | 2024-11-03 12:21:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |


[Clique aqui para ver as próximas entradas](README92.md)
