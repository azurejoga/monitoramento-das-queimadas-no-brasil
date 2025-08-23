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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f17fd8e-7dff-3db6-a33e-3d3971c894a9 | -14.80913 | -47.94604 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cda48a7-5a87-3ecb-8160-54ac6493c9ed | -12.78693 | -48.72404 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f305c5c-27d0-308d-8ccf-22aea489cc93 | -7.78989 | -61.57784 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea328027-511f-3c07-b42e-ae1358b6af2b | -9.19346 | -59.65439 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbdc322e-bbbd-3aba-aff8-de4d7c0fd04d | -12.58125 | -60.35323 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0fd43c8-040d-3b22-bd7b-e85be633aa13 | -9.94555 | -60.17849 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9f8c10-2d89-3f0b-b5ed-e2defed96fb8 | -6.87297 | -59.81844 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 367415fd-df91-3542-adba-c51536f3c446 | -12.58237 | -60.34616 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f5e9186-aff2-3b9d-96da-4dd790adafa0 | -7.09994 | -59.77551 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea6382cf-b143-3c44-aa25-aa1721d8df79 | -9.1796 | -59.59131 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eb28449-3d79-39ed-b7cb-8e527e8c4644 | -14.68029 | -54.87221 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| becdb4ab-89e4-3dba-b68a-8d600958e92f | -11.50744 | -50.47164 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d058e77-6950-30a7-a47c-b6b589fab873 | -7.04695 | -59.83581 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e08e91-dd20-3bd6-bf56-2a8b7a8b4284 | -11.189 | -55.03029 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 984004c0-1f04-3884-a670-6772f0b5a06f | -8.87232 | -62.41952 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b420b2e6-0775-3667-b0af-fad3d206a2ec | -14.36985 | -52.05483 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cae66a45-7b6c-320a-98b0-c17aa4933d67 | -14.61333 | -54.82231 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff83553f-23fb-3300-b84c-f8057be8290d | -7.90556 | -61.51233 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 069507dc-e661-36a6-af9a-1cfb59f21302 | -13.0226 | -56.82584 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 759042c4-9913-315c-a17b-1767f3501ff6 | -7.30305 | -59.62427 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b7d6513-f962-3e6f-9a3b-5643d8d5a90d | -7.29748 | -59.63774 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c551a2e3-b473-3209-8867-aa0f48a29f2b | -12.98414 | -56.88305 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0f89096-8f3d-3d84-837e-baa8b7ab1603 | -9.17851 | -59.66275 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0b098a7-f6ef-31b0-bf7d-b8ff15ab8d65 | -9.44175 | -47.65382 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1f9b23bc-69b4-3a37-8d9c-fb96e71a0a07 | -8.61959 | -62.63943 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04dfeb20-58c5-3378-9d2e-50f119cdfe61 | -14.27567 | -58.53257 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05a789fe-faa6-3508-9ed6-839cbbfde2d5 | -7.81335 | -63.56084 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9ac0b8c-f078-367d-a331-4c8187f7d86d | -13.39279 | -46.35315 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b836f2a0-1ab1-3c71-918a-adf1b0874ac5 | -9.22884 | -59.74966 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e31d3050-fb20-3637-bb4d-cfbb30fb40d4 | -14.75729 | -55.99186 | 2025-08-23 05:21:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed277634-e608-3344-a783-4aa24c95d7ea | -9.20501 | -59.45212 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fdaac0f-07d1-368e-b0bb-3ea21eb71adc | -13.43545 | -57.17692 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04c6f5de-8f67-3020-b5c2-d6ee02dda29d | -9.19179 | -59.62193 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 57e6f347-68c3-37a1-b99e-6dcb312b4a1e | -7.31473 | -59.61536 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87858a83-4fa4-3201-83bc-aaad01d95998 | -8.60195 | -62.61014 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74fe8618-ae16-389d-9dc9-842af356c23a | -14.33095 | -58.57634 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6dee193-0f7b-3c75-86ca-9dd932850507 | -11.19375 | -55.02565 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a8cc827-cb57-3096-bfe1-2f847b811d04 | -11.3282 | -55.22274 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bbada227-09c1-390d-ab06-5c241d48e107 | -9.18681 | -59.63188 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bb3a494-6c63-316e-90fc-350427b0a067 | -12.94546 | -46.29856 | 2025-08-23 05:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 052b2d58-42f2-36e3-b099-eb33448dabf2 | -14.29982 | -58.52393 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42301eb1-9cad-34af-9fc0-0316c2e92b80 | -15.02245 | -54.86987 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63094db7-e921-324c-8b7d-5c42dde3d65c | -13.02694 | -56.82195 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e779e0aa-79e9-3fc6-8fb6-92bb38ad6d4b | -9.88376 | -60.29552 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd82c65-a36b-383d-90a1-ea8ba520db4c | -14.47255 | -55.94215 | 2025-08-23 05:21:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88632e23-0a9e-3b6b-8d49-c6315b010884 | -9.06832 | -60.41778 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eb3a77c-0222-3313-8b5d-78c2552c91f4 | -9.17184 | -59.59723 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94f3d1eb-3e7a-3a5a-9dc1-a2889f727ad9 | -14.35322 | -53.12167 | 2025-08-23 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7e785a7-c07a-378e-b137-0ada6e406439 | -11.18679 | -55.04594 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39dc72ab-1e8b-3864-b735-75e3d47ee671 | -9.18128 | -59.64528 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3515f3b-f993-3d36-b343-d21e50d2d0a0 | -14.68404 | -56.61086 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89c95cf1-bee3-3116-adc9-948951c9d6bf | -14.37534 | -52.05242 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d9669a0d-9b3a-3cde-97a6-33e8a2d43c26 | -15.54835 | -51.70132 | 2025-08-23 05:21:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9dabd44-47fe-38f8-9a22-c96ac3ed0c51 | -9.21284 | -59.61814 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32520288-af6b-33f3-9df8-8994816e2194 | -15.00224 | -54.87261 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0476bd4f-9d01-3964-9bd9-cbe486f056e9 | -15.01445 | -54.86455 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 552de252-b8d7-32d3-81c9-3674c00304e8 | -7.81723 | -63.56151 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0fee1ce6-c2c7-381d-ad1d-19759b35e715 | -9.57909 | -55.35522 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34310237-b566-3ee2-a380-982c702a45a9 | -9.16853 | -59.70416 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cad8963-d3ae-3c38-afd2-61cc28d94740 | -8.61429 | -62.60349 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4feeb411-863e-3472-83ea-fa2e1580690d | -14.28377 | -60.3874 | 2025-08-23 05:21:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2812d7d9-5eb0-39d8-b4d7-54d159b2b8af | -7.04863 | -59.82523 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7007c8a-62ab-3c65-a8d9-272435dfd09f | -13.42262 | -46.27612 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 205aa99d-e34d-36e1-bfbf-171a30de6d43 | -10.60871 | -55.41048 | 2025-08-23 05:21:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1533bfb-aed8-3fe6-8420-882755e69773 | -13.49592 | -47.03368 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f692e71f-1d2d-3092-89e2-c3c8082315a0 | -9.37438 | -48.25386 | 2025-08-23 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca5843b6-ad26-35f0-aad9-39cdd925296a | -10.10815 | -57.76263 | 2025-08-23 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e1034d5-27b4-30ce-93a7-23a04723f868 | -9.38543 | -60.50965 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd1f63cf-428f-307a-a51c-836dd930563b | -9.16852 | -59.5967 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7422cb04-5b04-3d22-acb2-b60ccb092795 | -9.96277 | -60.17767 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b1a0a832-24f0-38b0-8eee-1f2bb3f5259b | -7.05302 | -59.83296 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f344af06-5d17-3478-97d9-e098afb71454 | -15.70236 | -48.09284 | 2025-08-23 05:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 561b5264-dd71-3744-962f-632a7af13321 | -9.18514 | -59.62086 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b94c482-6ab2-3693-b82b-a19c2d4609dc | -13.47578 | -46.89717 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c492f8d-34ff-3d40-abe9-ff5d7e4cf600 | -13.4612 | -47.03427 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1146109a-bf28-395b-be4a-433bec78d711 | -13.02552 | -56.81944 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9779627-ef8e-3d26-b0ce-2b7c1e6acb44 | -14.66062 | -56.59093 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ef9b461-7e03-30ce-b889-adec9c5d0506 | -14.25319 | -58.54096 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c17edbc-323d-3f85-8758-ae6977f54320 | -7.25756 | -57.68139 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2d52c50-501d-3679-8854-cf5f66d1271b | -13.3745 | -54.40201 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 872d92a4-0374-3862-995a-bc4725df04c3 | -13.37665 | -46.20601 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7002f255-628a-3ee9-b935-6d22ea90b7c1 | -13.37075 | -54.39721 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6377fd22-a99a-3015-bbbd-7ea3174028e8 | -11.197 | -55.03147 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df1015d8-3984-31da-9058-f502c3d4b47b | -13.36998 | -46.21698 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57040d7b-cfcb-3635-aba0-00c76de87c2b | -10.63337 | -50.13776 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b01923-2984-32c0-a9dc-798d494294bd | -13.36162 | -54.40005 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a2a23c5-20cd-368f-8894-b120dc24bad0 | -9.81317 | -64.27106 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76c5edad-6e1b-3d9a-991a-f177b13d4d5f | -9.52879 | -60.52538 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d27f1cc-2438-3358-a54c-70d6e90faf7b | -9.18459 | -59.62436 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07b2c380-7f36-33a7-8844-580d8d7c4b10 | -9.16521 | -59.68213 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 946931a1-e641-367f-a51a-135df4e21902 | -6.83429 | -59.88834 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3156662f-cb8d-3b7d-a646-97dbf3470c80 | -7.79404 | -61.57449 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2693ab3-378c-3362-8cae-44d31650fc82 | -14.66061 | -56.61167 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57c42cfa-aadd-3520-bb58-ae2d7c027d47 | -9.2499 | -59.61684 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea534fa-78fc-3fd3-b402-44b5266bfb73 | -9.2097 | -60.79818 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed11a872-c9f8-379c-91ff-53f7f17433ce | -9.22796 | -60.33421 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87dcdad6-7e43-3572-94ae-aca718fdd0cd | -9.61094 | -55.36303 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7734f6f6-456c-33e3-8eae-413b421aaf02 | -8.59759 | -62.6138 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79c02f20-9902-35c5-83f2-dce20d069eab | -7.80558 | -63.55949 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da651620-7438-3b94-a6ca-054e109a3911 | -7.79276 | -61.58233 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
