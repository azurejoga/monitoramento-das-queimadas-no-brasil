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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a856437-9ca3-3b97-bbf1-01d25dfbbe61 | -12.35823 | -54.51935 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1480aa6c-08a8-3fc6-a2fc-9f43c5ec73be | -11.57507 | -54.56813 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad16d532-d7da-3f9d-91f8-9d13292b648c | -12.03685 | -54.97135 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e4cb6e6-0334-313c-b71c-815f1daedeb4 | -12.03283 | -54.9746 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33cbab6e-cbee-319c-98b4-ee7ee894ebfa | -12.50226 | -57.22661 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bd38cb7-492d-3938-baf9-3fe34d0c8a47 | -13.71315 | -57.47171 | 2025-05-21 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 276a1da9-5e6c-3a3b-b416-42b7b0caf88b | -12.48077 | -57.19057 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c726677a-5994-3d84-a9cb-6ddc8441bf2b | -12.68417 | -58.12957 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b52f1f54-a836-301f-b4b5-2d96a33686e7 | -9.9122 | -60.73561 | 2025-05-21 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9dda056-8dba-3186-aabd-a001b5285d74 | -13.71646 | -57.47225 | 2025-05-21 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4246d00-ec92-32ef-9e6a-535ee0bd9720 | -14.05033 | -56.06614 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc35c2af-4569-3cd3-a409-d457adaa661e | -10.67924 | -57.60244 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 981d2c9c-5c53-30e0-b686-cfc1c6e4c7fd | -11.35923 | -55.12402 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ebd2dee-de13-3be5-afec-576097080083 | -11.6461 | -58.26192 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6a70d2f-7a84-37c8-bf5b-04fc0328e170 | -11.13543 | -53.92179 | 2025-05-21 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8c6cb16-3029-38bd-83e6-7d1e742efc3f | -11.66697 | -54.93954 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea91c7ae-a15e-376e-8b04-f71c1a980683 | -14.01616 | -55.12765 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17e7f2b3-cc73-3f3d-b229-1b091f1f3d61 | -10.00094 | -55.508 | 2025-05-21 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6cf2a829-d8d9-361b-98da-86c58e1a83cb | -11.3581 | -55.13145 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f824ae-d21b-3796-9fa9-db59de89ba1c | -12.27533 | -57.26574 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea39f9cf-4ce8-3f5a-b752-bcfcc6223506 | -10.85966 | -55.48284 | 2025-05-21 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6960302-f5c0-304a-a4aa-c64ffe05a5eb | -13.66363 | -53.92934 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a5f72de-e7c3-3b5f-8167-89bef4b46789 | -11.78024 | -44.28535 | 2025-05-21 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56cd2c63-cc29-32e7-af60-661ab5bbbe69 | -11.64886 | -58.26612 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a03d75e8-2e96-327a-bd1b-7374c7b553e0 | -12.12201 | -54.28552 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 781f6d95-41fc-3b89-ac2a-ce257cb45af1 | -11.0793 | -54.77866 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ad237bce-7fd7-3922-ae18-9461dbb4ceca | -13.80181 | -52.89331 | 2025-05-21 05:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 511ef43b-2780-38e4-8268-85fbbd6fe9c4 | -11.07644 | -54.77432 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8b8490d1-ad59-36bb-9e60-61041c0b2b42 | -11.83632 | -60.92636 | 2025-05-21 05:04:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a3598a9-2169-324c-ae41-c2386a53fcfd | -10.07729 | -55.49419 | 2025-05-21 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bab24ff-63e6-3094-91bc-3d219175a9fd | -12.13087 | -54.66488 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb3eb941-824d-3774-8f78-0a20ccb93868 | -10.67867 | -57.60598 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 598862dd-5c72-39a0-bb08-bd6dbe3a84cb | -11.6468 | -48.10074 | 2025-05-21 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0a35204-8509-3f02-ba30-c43161eb153e | -12.13145 | -54.66095 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1128754-23f2-3837-b3f8-04073b591358 | -12.30096 | -52.47618 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8811e230-ad79-3a0b-9f0e-69b183362782 | -14.02833 | -55.14167 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a1d5cb2-4fc8-3ac2-88fb-249d83946466 | -10.77367 | -55.57269 | 2025-05-21 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8a6c8c92-1fe0-34c9-b297-26e9aef3a49c | -10.5982 | -52.84829 | 2025-05-21 05:04:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0c44f60-7705-3b8e-8816-d7b21b6ec42f | -11.43951 | -54.0893 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdf0049-8752-3c0e-a9ed-048c8c9e0636 | -11.74931 | -54.72115 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9011d3c-5082-3636-aa30-bde537788cea | -12.47139 | -57.18542 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ea15912-cba4-3b39-8de1-abc2287fc753 | -11.8239 | -57.81497 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 631a2884-9487-3c21-a386-092a281b93c8 | -11.80816 | -44.2771 | 2025-05-21 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 420ec81a-e12c-3391-835d-cc6c331b79eb | -12.41115 | -52.14739 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd37eb76-4652-31bb-8686-55145d7d47d3 | -12.29632 | -52.48066 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57f66f40-2e24-308b-afbe-26912b1f8755 | -11.36264 | -55.12455 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2b32c0-949f-3b4a-9a81-8d777f374e0d | -10.87308 | -44.93899 | 2025-05-21 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a89a7ff-0e91-3097-adc5-f6605a9c443d | -14.01964 | -55.12818 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d68e519-85b4-3935-8da7-e5b2d7acbea7 | -11.2938 | -53.97825 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 385647b6-b1cd-39cf-9d1f-80f803692279 | -12.30145 | -52.47346 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d5f2958-54c6-3ecd-b10f-adb131896f54 | -12.5561 | -52.24643 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6b4da97-86b6-3961-b4a5-b6bca452f722 | -13.61797 | -55.45635 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0ae5aaa1-2490-39ae-b942-9f934462327c | -12.29938 | -52.48864 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 31a6d9d0-59d5-35e2-8f99-b4af19c0f577 | -10.68038 | -57.59534 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67fa7489-ed9e-3fb2-8aeb-9b527b6f41ed | -12.29313 | -52.47504 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa15a866-b456-3097-9633-781c3e7e9bdd | -10.68257 | -57.60297 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e6c181-248b-3158-87d1-fa1973fda456 | -12.11984 | -54.66716 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba34e853-ff2e-3010-a08f-8ef4c2a9f8c0 | -11.08675 | -54.77594 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1d7c549-ecf7-3f91-9c00-8246d5731dc7 | -14.01906 | -55.13214 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61d4b798-f3c6-3afd-8372-4cae1bacf4a5 | -12.50282 | -57.22308 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d28dab2-7c5e-3a9e-9033-70976bb86cae | -12.29155 | -52.48749 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 876fe575-7009-38ae-9033-f959baea9fdc | -12.30007 | -52.48358 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9fbe6111-c046-372f-8fd4-289a6fac00a3 | -12.50724 | -57.21658 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efea9698-0f22-3f19-a8d8-c954f2db69c4 | -11.07702 | -54.77051 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| cbdb836e-0d6b-320e-85aa-7a49bf2a0f82 | -12.03627 | -54.97514 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24aba329-5a49-3b5a-8bb6-14fefad7a493 | -10.34124 | -51.69604 | 2025-05-21 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 271cb9ee-bd57-3a25-aef8-4a9125c5a349 | -11.29675 | -53.98287 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5603b11-115a-3c61-b2ee-0f92373985f1 | -12.2956 | -52.48571 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 44c204fd-35d7-3c02-b73a-12fc19176ba6 | -11.29024 | -53.97769 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c5fb507-8fac-33c8-88dc-9934163afab0 | -11.08389 | -54.7716 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75e55df4-a487-3fc0-b2e4-dd8e14715bcc | -12.12332 | -54.66771 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e06fa412-76b2-32ad-a0af-83d696aad549 | -12.68475 | -58.12599 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13ca05a-02d2-3c57-8b7d-e741cbc9b033 | -11.41235 | -56.7294 | 2025-05-21 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf66ce61-f566-3496-95ac-8c0de66de39c | -11.07988 | -54.77486 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 052947e7-ffc4-3a97-af2e-dd0d2c8fb3af | -10.82624 | -56.95833 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8eb9637e-4335-391a-98b2-64318fb3a2b4 | -10.05059 | -64.99891 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed9ac5e5-d05d-3d4e-9539-6bc80b16849b | -10.82293 | -56.95779 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5e9fa77-c427-3aec-b493-2513feaadb06 | -12.83904 | -47.39585 | 2025-05-21 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2416cf4-b1f4-36f7-aa7a-7907ed33f9ac | -11.15472 | -48.68159 | 2025-05-21 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b89e520b-4ce4-36b9-bbe0-d0f4a6c5adcc | -10.68704 | -57.59644 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f275685d-213c-31f6-9bdf-3fe0e0a11b1a | -12.72166 | -54.97009 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33152fcb-1f2d-33c2-a148-0fa02d7a742a | -12.50338 | -57.21956 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed7c321b-7a4c-365f-85a5-f1c1df89ee5a | -12.50669 | -57.2201 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f63ccf69-d0fc-3781-befa-a43c7116f6e2 | -12.3422 | -49.96221 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d1b362f-c865-30e3-8d05-3a3535dd6006 | -12.43052 | -43.72806 | 2025-05-21 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a4aa6559-4f65-3ecb-bb4f-aebf6a6918be | -10.05505 | -65.00285 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17908b9c-82c6-3b30-947a-3deb9b43c4a8 | -13.61111 | -55.45527 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f067260c-a155-396f-b072-7923d6e1e5be | -12.12141 | -54.28957 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d506643c-7846-3456-9c37-5969f436c774 | -14.04752 | -56.0619 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e186f3c8-14be-35c7-aa95-66b2c3121e6c | -12.48408 | -57.19111 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 567cc2c4-f570-33a8-a307-e25e1f5fb092 | -12.33757 | -49.96155 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49f53e43-116b-33fc-a1ff-a7b42dd11609 | -12.65126 | -57.18578 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da8573ab-3882-35c7-9a5e-2f1cc4816741 | -9.16833 | -61.95402 | 2025-05-21 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 703f16f2-ec4a-315d-aca3-fd2bead0e709 | -12.34282 | -49.95741 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a51da8a7-af3d-301f-a19d-90403c53179e | -12.64795 | -57.18524 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 318b00c6-9795-396d-9e67-d1cde08c0a6a | -11.08273 | -54.77921 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c4546cf-13fb-346a-b7b3-2ddf672bf253 | -12.3647 | -49.97041 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3221443-42a9-39b7-8aae-bf95f23df2f8 | -12.41066 | -52.15091 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f38c40-d27a-3497-9756-c13ae604dbe2 | -10.05616 | -64.9969 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b2cf3d1-a65d-3ba5-845a-12c65033bb1d | -11.08045 | -54.77105 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README18.md)
