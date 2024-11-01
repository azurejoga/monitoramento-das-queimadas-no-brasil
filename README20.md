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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff1b96b7-54a4-354a-8f2b-1664b142d5d7 | -3.56165 | -47.37725 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 909c7309-1085-3db7-90fd-d057845f7473 | -3.5609 | -47.38171 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| d34fd1b1-7e74-30d8-90fd-37e7be614f90 | -3.56014 | -47.38618 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 2280b46c-e687-3972-bf84-935a6cb33bab | -3.56 | -47.37955 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f450315f-05fe-3516-a4c1-46afa0802988 | -3.55928 | -47.38401 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0b575d00-13f1-3162-8a14-3088abe009c1 | -3.55855 | -47.38854 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2858efac-cd7a-366a-9648-5fb77ed55ced | -3.55639 | -47.38102 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb0771a0-31bf-3626-8810-bae5b331bef9 | -3.55564 | -47.38547 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eed4ddb1-7e97-34bb-a715-ec7d03b2cb9f | -3.55477 | -47.38331 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 86f7de3e-72e8-3f95-b03f-b287d5483fb6 | -6.0405 | -47.93846 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22d26a29-6210-3c54-95ef-c57daf7cf605 | -6.03601 | -47.93771 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 213218b1-7232-38e1-ac11-59a9dfb82968 | -6.03151 | -47.93704 | 2024-11-01 04:06:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 718d655f-a3ce-3fa5-bf19-181f79990ba7 | -5.52378 | -46.91423 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3a1c146-3bfd-30e5-a2a9-75c5dad09a31 | -5.52082 | -46.53638 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c417d6c-4ab8-354f-b48f-f4f093e1ef86 | -6.60877 | -47.3943 | 2024-11-01 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54657e1f-53ec-37e3-b8ac-9bc50f3f1d13 | -6.60448 | -47.39359 | 2024-11-01 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a409205d-8dc8-3e92-af84-a6436a684425 | -6.60021 | -47.3928 | 2024-11-01 04:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 509cc023-00e7-330e-ac9b-052373229fdd | -6.55619 | -47.51955 | 2024-11-01 04:06:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5eba987b-10e4-3a27-b259-f09383d31e94 | -6.55574 | -47.51608 | 2024-11-01 04:06:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbe628c1-bac7-3a06-b50b-207fd428add9 | -6.55506 | -47.52017 | 2024-11-01 04:06:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 374e46c3-ea66-375f-b529-82b7adc7732a | -2.14155 | -48.10691 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e0a8a06-82e9-358e-bd1f-5faa0c9cb469 | -2.05215 | -47.91158 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99aaa856-f9fc-37ce-b107-8ae7acdcdf56 | -1.98713 | -48.51075 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 494e8a64-3f8b-3a6f-b566-712e5c7b899f | -1.98705 | -48.51187 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96109d96-3fae-339f-b76a-c3b814563d60 | -1.98624 | -48.51636 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34a7117b-d689-31ae-bee0-7bc2a2ffc41f | -1.86568 | -47.82547 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bb0d182-d3e7-39d0-b67b-76ce2397d50a | -1.86545 | -47.8273 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f3c80df-bf41-3665-aab1-ff325b548540 | -1.86035 | -48.00715 | 2024-11-01 04:06:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61f2ae98-b185-3707-9d73-6be551bcb810 | -1.8571 | -48.00502 | 2024-11-01 04:06:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 492f7abe-8257-3239-8136-f9c5d3653f64 | -1.48617 | -47.14953 | 2024-11-01 04:06:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6f9499b4-a1e0-349d-b9e9-43dc1ab0cc28 | -1.24322 | -47.83745 | 2024-11-01 04:06:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed20a04e-6f50-37f4-8760-ce3d681afaa7 | -1.23535 | -47.73501 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6591938c-d098-3070-8885-e11c965ef6ec | -1.23534 | -47.73718 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35b81838-496d-38df-bfa7-767112a678d4 | -1.23451 | -47.74014 | 2024-11-01 04:06:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7619e1be-d896-3ec2-9b42-39f5a86baf7b | -2.62499 | -48.32988 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2bd8784-3383-3278-86ab-5444b7a95dd8 | -2.62011 | -48.32908 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ceb68e42-7be8-353e-843b-a7a9e8530de6 | -2.61923 | -48.3345 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b960effd-1d2c-3eda-8282-d704c7be91a8 | -2.59376 | -48.15563 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7bf3c53a-8b3a-36a2-b2af-a7d313c01b5e | -2.55287 | -48.17353 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2c8b679-edd7-39a3-8090-b5a8e327e9ce | -2.53609 | -47.51703 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fcf6776-478f-3418-9f70-9691bccc9507 | -2.52307 | -47.4514 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b533bfe-1d63-37d6-8eb8-13558fe358b7 | -2.52231 | -48.46411 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fa166ce-0cd0-3614-a02d-3a16495f39f9 | -2.52138 | -48.46964 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47e6cf5c-f8b2-3164-9fc5-06b119e6ab0e | -2.52084 | -48.46738 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfe31bde-a656-302e-9556-2687c1c8ac43 | -2.5177 | -47.45536 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec0ab41-7357-3d70-b451-f8ec8eaccade | -2.51693 | -47.46011 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfb3692f-c180-3349-a06f-80381202b32d | -2.51591 | -48.46658 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef3f1f20-5cfe-33af-8fe5-dfff4bc7a6d9 | -2.46429 | -48.50346 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f1575fe-fdb7-3d8b-8f9a-23338541cd18 | -2.46025 | -48.49708 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a50eb981-e384-3dd5-b18b-6e9d4c8d1053 | -2.45934 | -48.50263 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7ffd393-4ef0-31b1-a80a-5a95f25beaca | -2.4022 | -48.22328 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72c99fb8-582f-3b86-9892-7c922e234379 | -2.40134 | -48.2286 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc447a26-a28d-355b-98bc-ae1dd4769f98 | -2.39982 | -48.58499 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c53f4a96-70f4-32b2-adac-7a675dffec79 | -2.3998 | -47.72676 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa997afb-de1f-3886-a63e-1baaea0fe065 | -2.39881 | -48.5895 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ef910a8-71ad-300f-b3d4-74030ef272b2 | -2.3959 | -47.72105 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59a10169-0744-35d4-9f87-e61c70ae2194 | -2.39512 | -47.72594 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce343b09-12e4-3a2d-b839-ff0eb74be114 | -2.39484 | -48.58417 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3707ac7-c93d-36e8-910f-939dfb94b103 | -2.39474 | -48.58294 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89adbb25-e22f-3b36-ba6b-cf751b0e4e4d | -2.38975 | -48.58212 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8564092-1bc4-3234-a580-b4d0a18c853c | -2.36828 | -48.68424 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e55353d-b6a6-3692-bff9-885f65bd25c3 | -2.36759 | -48.68528 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f01b308a-5012-3b98-8670-3af7e4576530 | -2.36327 | -48.6833 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6d1f653-95f5-3907-9bc1-918e6298d582 | -2.36259 | -48.68436 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ca66fe5-6f2a-35b8-ab58-4bfb2734222d | -2.35826 | -48.68243 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d331be1c-f2d8-3227-86ac-5552edb27c83 | -2.35324 | -48.68159 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f02f55d6-19d1-37ca-8945-0d43f0e9127b | -2.34915 | -48.67501 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a02733d-2999-394d-b286-882070962b9b | -2.34822 | -48.6808 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0efeb6df-cb2c-3d6c-a390-d627354946ee | -2.34413 | -48.67419 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33e541dc-4b6b-361b-b00f-a1896714628b | -2.3403 | -48.44745 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d64bdac3-8afe-359f-b6ce-b753b21a0e46 | -2.32854 | -48.83465 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea51c334-75d4-330a-8c00-32699f1dfd81 | -2.32807 | -48.83759 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 178bc941-d00e-3bb8-aa09-5d616ac34064 | -2.32347 | -48.83379 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c0e7981-9f51-3f03-95bb-7dbc83142052 | -2.323 | -48.83672 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 56257a40-a9ea-38c3-9f9c-f82b35b48676 | -2.30317 | -48.57943 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cbd0d1b-0db4-32a7-a328-70f69dbd4125 | -2.20129 | -48.35439 | 2024-11-01 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73095f17-0355-35df-a8c6-05140e5c08de | -2.17657 | -48.72771 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 977c249b-def2-31d9-8c2a-ecb28193ffa0 | -2.17609 | -48.73063 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 06dc9d50-1470-3214-a7af-7cafab7dce98 | -2.1756 | -48.73357 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07f4e163-870a-3005-ab5e-c27c02f44bd6 | -2.17152 | -48.72689 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ef304d7-4b16-3fe2-92a6-a9496851f94d | -2.17104 | -48.72978 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 37ea8cdc-c7cb-3268-8c1a-d2aa03d11bf1 | -2.17055 | -48.73273 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f98b3fcf-d37b-343e-9509-ce965ede86a4 | -2.1621 | -48.75236 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 988e9868-104c-3f81-8705-66a866f81b97 | -2.16162 | -48.75528 | 2024-11-01 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c462cec9-0c2d-30d3-a032-4e894f67fe88 | -3.06846 | -47.7746 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00772127-2340-389d-afa4-2114d6e88cd9 | -3.06668 | -47.77268 | 2024-11-01 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fd448f5-66e4-3f7b-a8e4-8af4bd8a8960 | -2.98021 | -47.92006 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 420d89d2-a3a2-3774-a80e-01481818da93 | -2.9755 | -47.91925 | 2024-11-01 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6868f2b-e1d2-300e-bc1e-9ee724d93855 | -2.91721 | -48.61333 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e111f0ae-ab8a-3e3b-aeba-2799152334e4 | -2.91627 | -48.61892 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb58307a-b142-3072-b428-d8a09105f6a0 | -2.91605 | -48.61805 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f21b5e4-c25e-34ca-b9cf-f439b4eb4e39 | -2.91226 | -48.61251 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42a250a9-55fa-364c-8766-09384388a19d | -2.912 | -48.61161 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e2ac104-92d9-3dad-9ec8-f148894584ab | -2.91131 | -48.61813 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5d96bf13-6661-3232-aacc-cedb16a06e49 | -2.91109 | -48.61724 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74c981d6-03d2-3a3f-9c42-85a75970f2ec | -2.91035 | -48.62376 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a96faa4a-dd56-30e3-9323-c458cf88c987 | -2.91018 | -48.62288 | 2024-11-01 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 457cbff5-4532-31c2-9d09-eef6182481f7 | -2.88944 | -48.28996 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b717f6f-6bf5-397b-a2ae-87b4b42f42c2 | -2.88653 | -48.28794 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ee6fa7c-4b9e-355c-9e7f-d69c55a0adf4 | -2.8846 | -48.28915 | 2024-11-01 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README21.md)
