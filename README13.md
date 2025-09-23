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
| b179f7f9-3198-3071-b06a-1281336cab4b | -4.40293 | -44.37228 | 2025-09-23 04:17:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2e43432-2183-3ce5-bb44-9bd19b28eaec | -4.06912 | -48.04008 | 2025-09-23 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dbb1133a-aa1e-3e28-bbb3-ce083c363fb6 | -5.52284 | -46.51067 | 2025-09-23 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc182fec-9fd8-3348-8998-cf9d11bac700 | -3.19376 | -54.976 | 2025-09-23 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e28e3a36-dd94-3b84-8e4f-e3a55d6516fd | -3.65354 | -40.35085 | 2025-09-23 04:17:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bfb43078-984d-3091-abcd-ad9c4fcdd3de | -3.0772 | -49.46683 | 2025-09-23 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d29074b-62f2-392b-81e5-643b59beffa8 | -3.46153 | -43.18818 | 2025-09-23 04:17:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91510407-5dda-311b-a047-bbbc5f4f5ca7 | -5.88366 | -42.82837 | 2025-09-23 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 944d7182-5952-3077-a031-f89742cf6e36 | -4.38352 | -43.2851 | 2025-09-23 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13659bf7-0903-3ad9-be14-52ff65483f7c | -3.6446 | -48.32111 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7af6190-edf6-31e4-898b-a9ad77a3fb04 | -6.32913 | -41.71395 | 2025-09-23 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5673c35-737a-311e-8a1c-e6ff0f14d00e | -5.42739 | -47.16969 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08a79c00-3253-35bb-975d-4daa33a76a29 | -4.85726 | -45.74339 | 2025-09-23 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d89fe954-77a0-302f-8771-1ef8fb352cb7 | -6.33373 | -43.38398 | 2025-09-23 04:17:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 638b22d0-1a90-3c44-a4eb-a6ffb5def3b0 | -4.59735 | -46.59211 | 2025-09-23 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec55ff43-a73c-34ec-a1be-fe0ab0dcfa48 | -3.85371 | -52.2431 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4658db6-6e70-38fa-9098-ad5ffccb8632 | -5.75703 | -42.60622 | 2025-09-23 04:17:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ec0244c-80b6-3bf8-bab7-25d36225c70e | -5.5194 | -46.51011 | 2025-09-23 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78e1415b-6a0c-3b58-b1a2-fedda9f6b859 | -3.03181 | -51.44987 | 2025-09-23 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 385c2804-0b26-382c-95e5-7cf412a842e3 | -4.38298 | -43.2886 | 2025-09-23 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c7df226-21e0-3066-9f14-a1c7ceae3e22 | -4.07289 | -48.04068 | 2025-09-23 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71b9608e-0f92-3598-a3eb-9ff9d6a56e7d | -5.69913 | -46.39663 | 2025-09-23 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a62579da-a433-3f41-afcf-a4cfe2613b12 | -5.65323 | -42.59757 | 2025-09-23 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f4b507b1-f016-3dc6-81fc-690059fc185a | -5.48139 | -42.25471 | 2025-09-23 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b6ba035-091a-3444-90b8-d94e46397f29 | -4.77995 | -42.76447 | 2025-09-23 04:17:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cad53eb8-3530-3ed1-ab67-626156a062ba | -5.03326 | -43.60386 | 2025-09-23 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46aa551e-7ef2-32ee-82a8-9dea814c7f3c | -5.91048 | -43.8554 | 2025-09-23 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d368cd0-6c0b-3a29-a33d-7a88aee6aaf0 | -6.1998 | -44.26351 | 2025-09-23 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9c65cd9-111a-3573-a27b-7e2753625a05 | -5.6464 | -42.59649 | 2025-09-23 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0866a60f-4653-39db-a513-5e9f4b637ff3 | -6.19561 | -44.35492 | 2025-09-23 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 723e3397-7b15-3dde-a6de-2941cc323866 | -2.79138 | -49.59765 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 238957ae-e18a-300b-8d8e-469a19a2b2b7 | -4.9654 | -48.01182 | 2025-09-23 04:17:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ada61a1e-c240-3688-9b19-9cc1d8583055 | -3.85421 | -52.23978 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1aee585-0226-3e91-8eb9-cd970de93c62 | -5.55805 | -42.73827 | 2025-09-23 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f612975b-3574-3cb3-b834-fee04ea08657 | -3.87096 | -55.35871 | 2025-09-23 04:17:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a289cbb3-164d-3db7-90a2-edd6c161d137 | -2.79179 | -49.59884 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d27cf28b-ffe9-3e95-8462-f34cde712c30 | -2.79242 | -49.59488 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d6aae03-d265-3ef8-87e2-fd5a9115fcc8 | -5.05012 | -47.6733 | 2025-09-23 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e3fbe27-3e33-3b65-a1d9-dfbd07f90058 | -5.88705 | -42.82893 | 2025-09-23 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8de3bdf4-6730-3b2f-9bfe-3eb0f1d156c2 | -5.60301 | -45.81717 | 2025-09-23 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90e8355f-2f14-3866-8324-aece07409a70 | -4.00976 | -43.26651 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2456294-b18e-34fc-b4e9-63320ca429c9 | -2.56211 | -48.97085 | 2025-09-23 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b999019e-5731-3a07-ab01-676f9a452f09 | -4.76367 | -43.63335 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e28799a-af37-30cf-9728-b2b1deb80de3 | -3.68488 | -43.51791 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d007a19-4257-33a6-815a-345045455805 | -3.19214 | -54.97855 | 2025-09-23 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6b1bbb5-23d1-30dc-94bd-ae8830ce1b68 | -4.10317 | -48.74327 | 2025-09-23 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dbed8e8-6e35-382e-9f43-29d61012960d | -3.19295 | -54.98071 | 2025-09-23 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 887d7ebd-63fa-38dd-9250-d476874cd64a | -5.28168 | -42.66587 | 2025-09-23 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29c39452-be65-3d59-92f5-6e4855802a7a | -4.08043 | -48.04186 | 2025-09-23 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4e4259-297d-3742-ac90-b7dc6e0973ff | -5.75549 | -46.48155 | 2025-09-23 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 944f6de3-a9e0-3dab-ba1f-39048b4ce16f | -2.3759 | -47.72284 | 2025-09-23 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447f80e8-7ebe-3a99-8fe5-589213f2f664 | -2.45584 | -47.27334 | 2025-09-23 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e8c35fb-c05f-3572-88ab-ce6cbe632d9a | -3.84968 | -52.2364 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0a55e64-5cc7-3e16-8c0f-9a8dd1c0ffa3 | -5.38341 | -42.25591 | 2025-09-23 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea78dc9c-f6d9-3757-b604-4626de5cea8b | -5.10486 | -43.16917 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b441750e-bdb3-3158-bc17-df1a15c24a6c | -2.78582 | -49.58169 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acab5201-7821-32e9-aa8c-af2d31ebfd6b | -5.31359 | -44.24078 | 2025-09-23 04:17:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e49ff5d9-dbfe-3546-9f51-d30fad9565dc | -2.83432 | -48.83487 | 2025-09-23 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaa52a84-9859-35fc-b7a8-7f92110b3192 | -6.07939 | -42.83173 | 2025-09-23 04:17:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b746be7-f14f-340f-87bb-b8b1a8ce2c16 | -3.63808 | -51.9056 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f893b877-a04c-36dd-a621-68d0ec62c287 | -3.68157 | -43.51739 | 2025-09-23 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d057a617-9ea8-321e-9ad4-3fbca96d86de | -4.79791 | -47.28148 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c09e1d86-0891-39ce-bc71-32388003eb5f | -4.64803 | -43.37597 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ca2ee3a-1222-37b6-9de2-5216fae4fc6d | -3.86482 | -55.35771 | 2025-09-23 04:17:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9de08051-606b-3c82-b6a9-c0709dd42029 | -3.38518 | -50.25845 | 2025-09-23 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa9834cb-56d9-3f14-9893-a90c7536bd41 | -6.36109 | -43.36272 | 2025-09-23 04:17:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 187c0a7a-6e7f-3654-a185-cb1db4d528b9 | -9.19628 | -44.62127 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b865e0-e839-35a3-b66e-c4c8093901f6 | -0.79743 | -47.61299 | 2025-09-23 04:19:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7936294-023b-39f1-ab65-2f544d894027 | -6.61411 | -44.60875 | 2025-09-23 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a590dc22-1bd3-3e3e-8b37-8fd7f6419e6f | -11.40854 | -44.95224 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b622489d-5820-3080-a247-8518d71366be | -10.81797 | -44.80094 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00342347-652e-3a04-b2b7-73f05b596fde | -8.0164 | -45.45039 | 2025-09-23 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 882827f1-2231-336e-bb4f-c61f3d0120c8 | -6.81379 | -46.37905 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3ef15aa-4c6e-396f-9e2b-dbd6512b414f | -8.51603 | -44.97514 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b46d6fdf-19c8-39e2-9686-6387ea24cc03 | -8.51327 | -44.97114 | 2025-09-23 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27f794e7-c067-337b-8933-af878f0e168b | -5.69393 | -51.05481 | 2025-09-23 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b497091-d4bd-3037-8629-8033ad269c3c | -11.08815 | -45.35349 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e0e63ce-2c88-3bc6-8005-870c0cbb6989 | -9.31608 | -43.36745 | 2025-09-23 04:19:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 088c5b29-b18c-3e22-8d11-933fe5b784c2 | -11.40685 | -44.94111 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b475513-2752-3a4f-8734-15bbf9c37f31 | -8.14098 | -44.46576 | 2025-09-23 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 644af781-d572-3aa6-848c-18e714ef3522 | -11.02093 | -45.88848 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24cfc57e-781f-3290-9f1f-c1b4818382b2 | -8.80203 | -43.0214 | 2025-09-23 04:19:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbcf29ae-d4b0-33d6-815f-9f7ee63afb91 | -13.56507 | -42.22244 | 2025-09-23 04:19:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bdf808d1-79c5-3792-a3aa-3e8773ffde45 | -8.84321 | -38.76517 | 2025-09-23 04:19:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 020c95ad-a69c-3d7c-8fcd-64dc272194a3 | -10.82632 | -44.81309 | 2025-09-23 04:19:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf61bb92-a77d-356f-8c7d-43b233cf8e36 | -11.47384 | -43.53017 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5403d93b-0e53-3f49-b229-8ca65994fcc9 | -6.5936 | -44.54527 | 2025-09-23 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9758dd1c-ccc6-3a7e-85ac-411169429b98 | -8.88724 | -46.10497 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 252c8e6c-e4f8-32e0-b3b7-c8bacff3fb2a | -6.34388 | -56.19729 | 2025-09-23 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3659055f-b401-3f7c-99ee-68296db3772b | -6.5969 | -44.54579 | 2025-09-23 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dd33636-8349-325e-b5c6-a1b57ecd4f31 | -9.01782 | -48.0354 | 2025-09-23 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb520b86-3aa7-308d-a259-3fbab3ad8962 | -6.92296 | -48.26891 | 2025-09-23 04:19:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 666883ca-afcb-3ed1-8df1-4fd141abe0a0 | -11.45136 | -43.52392 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc68b85-d89a-3182-af74-2da34cf9d5f2 | -9.99316 | -46.2836 | 2025-09-23 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2abe702b-b83a-3fcc-8a16-ee1ce777559f | -8.00822 | -45.71404 | 2025-09-23 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eca6ed74-2ce5-31f6-850d-7ccb438ad1d5 | -11.40576 | -44.94819 | 2025-09-23 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1188041a-1b2d-37d4-868e-e23366e01457 | -10.85315 | -45.42351 | 2025-09-23 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1de77807-31cd-3bad-b5a8-be69ff9f7f4e | -11.89263 | -41.26477 | 2025-09-23 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0e3be7a-d58e-31cd-97ba-616a09993a4b | -7.79269 | -46.19509 | 2025-09-23 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72f232d2-7e26-3191-8af3-6bbc9d32fca2 | -11.52519 | -43.63656 | 2025-09-23 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
