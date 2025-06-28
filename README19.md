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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 639b19e6-541c-3ea4-83b7-8a7a4516e536 | -12.11156 | -54.59502 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b07a098-457e-3fe6-9131-94700b1a4e6e | -13.14299 | -56.80977 | 2025-06-28 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f91c620b-b863-3c00-9d97-2a42f5758219 | -13.28982 | -57.0796 | 2025-06-28 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5be20f76-d6cd-3523-9a35-3acddec2c549 | -13.6473 | -46.81565 | 2025-06-28 04:29:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84e4074-8c1a-3a2e-8c4a-5b41df24ff58 | -11.8255 | -57.77207 | 2025-06-28 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acd9ea5a-e293-3f83-9d42-f8aefa0a0d9e | -12.10869 | -54.66342 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e88c1744-370f-3420-afaa-8c3573c91c3c | -14.47546 | -51.07099 | 2025-06-28 04:29:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0c8b46f-79a4-335d-b6e1-7a99b15de1ac | -10.28785 | -57.01346 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8520ef1a-1e0a-3208-a4b6-899d08dedd13 | -12.31115 | -47.27127 | 2025-06-28 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a47227fe-ec91-3264-ac5e-940957e1dc29 | -10.95652 | -48.15229 | 2025-06-28 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eec367a1-139a-3daf-b03a-f060cc620391 | -14.89443 | -48.39893 | 2025-06-28 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09fca45e-b24a-3c82-8cf6-c1952581d48c | -11.32397 | -51.4489 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e319cc6d-3d5f-352a-9fa9-de2738f86eb2 | -12.03255 | -48.75219 | 2025-06-28 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 162ef9ba-b189-3b6c-8da0-fbd2ece5ba7d | -10.82415 | -53.75504 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7804fa5c-e0b2-355d-90ce-01412511cfe0 | -13.29739 | -47.52118 | 2025-06-28 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 648974cd-e266-3266-bcaf-b277d1d25951 | -12.0365 | -48.74913 | 2025-06-28 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fb0f3e5-614a-36a1-b201-d6c4fdb3b098 | -10.28303 | -57.00871 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eff33221-d34a-3eaf-a56a-af89051b0588 | -10.87921 | -53.77297 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7656c495-3135-34f0-960c-4987fd10f5c1 | -10.8314 | -53.76554 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2edee1c1-4caf-38c3-817d-fb60c6d30931 | -11.44426 | -54.46233 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 624f7a06-6977-3602-94a3-b3492b7b29e3 | -10.28924 | -57.00621 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbc59551-f0e0-346f-9b70-025136c13f0d | -12.10331 | -54.58851 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efcd3c90-e626-3a6e-9336-446e82bf474c | -15.25956 | -51.47468 | 2025-06-28 04:29:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b21e9999-6dff-34e0-a36d-528ab5059274 | -11.26988 | -52.74552 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f58d7b5-fd14-30e1-9397-4590dd39fd54 | -10.05554 | -59.35886 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1983e824-b1e9-357d-b6da-eb567b2b7573 | -12.02631 | -47.77128 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 635a75b6-1d73-36da-a9cf-2a9921cca5e1 | -11.2686 | -52.75297 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 0ac58160-62a7-3170-8b5f-13eff795d861 | -11.18966 | -55.92471 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b9fd79d-bd1d-3709-85bf-c0ecd0599f31 | -11.88082 | -58.72715 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a0813e-476b-37e8-a606-97c0a42eca7f | -11.27189 | -52.74928 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 21b511ad-eec5-3b3d-8914-db2f50c4f0cc | -14.53554 | -53.83239 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cce06e8-86ca-3233-b091-e531be24d94d | -12.10787 | -54.58937 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bdb25c0-7f5a-3aa2-a44c-7ebdc83adc31 | -10.87623 | -53.76968 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c2cb47e-23d0-3bda-92c7-0ee70d6f15d9 | -10.95438 | -48.15213 | 2025-06-28 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c22a2f32-58a2-37ba-82b6-e21f0cda8f59 | -13.57278 | -45.26059 | 2025-06-28 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdcae0c7-6c2a-34a9-8fe0-c7cbe12a3486 | -14.53408 | -53.84019 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7cbc6ae-85da-380b-accb-3baede119c42 | -15.35245 | -49.04958 | 2025-06-28 04:29:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b283ee61-115b-322d-bfa4-6c215bb7d39e | -11.06004 | -55.37742 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 49f889d8-7d3f-3cf7-92a4-4bba68a2238a | -17.13764 | -46.59896 | 2025-06-28 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14257990-a121-3966-bc5c-f0829756120d | -10.0545 | -59.36406 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f30fcc-8653-3fca-93ae-9db9448b1c3a | -10.03094 | -54.32114 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 411e6e1a-4142-3564-b7c3-9b7c8ecaf72f | -11.27122 | -52.753 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d8e27135-a020-3c1f-9961-f6457c05c41b | -12.0259 | -57.0877 | 2025-06-28 04:29:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d264d783-ba8a-3a08-b8ea-e761f58ebd8b | -16.42608 | -44.51708 | 2025-06-28 04:29:00 | NPP-375D | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1848c0c-086b-3057-b71d-a404f66a5454 | -13.07465 | -48.83591 | 2025-06-28 04:29:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b34744-3909-330f-b5e1-85ac3866ce11 | -10.29953 | -57.1329 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db7189ae-3570-3e0f-b177-52e44e20a502 | -12.11043 | -54.57521 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707a807d-f1eb-3af0-a357-6959bb380834 | -10.84541 | -53.76358 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef51764a-b4c6-3415-85aa-77abee8f44d6 | -9.70212 | -56.18284 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 669d84f2-c4fc-357d-8f07-595b2ef5d12e | -12.10696 | -54.67301 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf373ee-3090-3d95-b4be-b8bd6428a931 | -11.54268 | -47.87331 | 2025-06-28 04:29:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc57e5c5-0f93-301f-986a-8eb33c0b4a7b | -10.81062 | -55.86973 | 2025-06-28 04:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 971439cf-986b-3241-a85e-b6b060bd5852 | -9.09223 | -59.49756 | 2025-06-28 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3517a58b-a1fe-3785-9098-c7c17456aa60 | -11.48213 | -47.44853 | 2025-06-28 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2af9eed7-e7df-3adf-8685-5ca874ff6cae | -13.12187 | -48.58538 | 2025-06-28 04:29:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3860c29-b5e1-3ead-96eb-f7b6d684689e | -11.54074 | -43.24532 | 2025-06-28 04:29:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b610745f-edae-30c9-bd26-d56677d8ebed | -13.99716 | -44.02862 | 2025-06-28 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80ad6ff1-8b04-35e0-b3f4-cec950154494 | -11.43968 | -54.46147 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d036fab6-b284-3092-8e8e-c5c7f5eb2d80 | -11.26713 | -52.75224 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5a77a150-304f-3102-bded-0d58aa60bf0e | -12.02299 | -47.77074 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d53f0b14-8de5-3cfa-8404-977ac153e050 | -13.94364 | -43.24234 | 2025-06-28 04:29:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 47048860-215a-32c5-b89d-22f2e58bfb23 | -16.45505 | -49.51672 | 2025-06-28 04:29:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea9dc9a-f1b8-3a39-a822-c0599089b974 | -10.8688 | -53.78003 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6369e8d-aa52-3d77-a6e3-bfe48e50ed92 | -12.25556 | -46.76643 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ef67a8-3a52-3a3a-81ee-9f47547b9188 | -11.57632 | -47.43122 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f37b285a-0cd1-3398-84b3-ed20dd65a954 | -13.14361 | -56.80663 | 2025-06-28 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3af68d3-bf31-3f78-bc08-462823af76b7 | -11.57287 | -47.62556 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b345d724-7e8e-32fa-8021-f260e7ea5fb7 | -11.19474 | -55.92561 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b67b7475-7d79-37b8-bc9a-884dc5cda1b4 | -11.88182 | -58.74423 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7461e91f-b362-3f19-b4ab-5331c4f761f2 | -9.71211 | -56.188 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| be27744d-1d19-3892-bd29-e5e17aab7230 | -15.15664 | -55.35362 | 2025-06-28 04:29:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 005a6f03-54e5-3386-b200-c4a55861ddc9 | -12.26314 | -46.77473 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8661d406-f197-324a-b887-4c72a0869479 | -11.77839 | -59.32463 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f47a48b-a432-354e-9414-576455812ccf | -10.81274 | -57.75799 | 2025-06-28 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba96ce8-ad28-3558-a7a4-b8a7174b6b6a | -9.7041 | -56.1843 | 2025-06-28 04:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ba097ad6-6584-3b8d-ad95-6482c0514870 | -9.7228 | -56.183 | 2025-06-28 04:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| eb522966-fe17-3c22-8486-285ae85d6072 | -11.0455 | -55.3773 | 2025-06-28 04:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 942e3709-ed98-3d0d-b295-e9cadd9a42dc | -11.0457 | -55.3571 | 2025-06-28 04:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1c2da38d-dc98-3a8e-bcac-5af8d996ed77 | -11.2664 | -52.7527 | 2025-06-28 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 88f0a907-7183-3664-b098-0b2c76bf964b | -19.63185 | -45.18764 | 2025-06-28 04:32:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f263857-34cf-38fe-bb17-5942b99580e9 | -17.75233 | -52.43568 | 2025-06-28 04:32:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| accc446d-95d2-388a-8d2d-8fd82b093ae1 | -19.7358 | -47.90789 | 2025-06-28 04:32:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2673d402-77b5-320b-a756-8b3cd9009cdd | -20.41508 | -50.10275 | 2025-06-28 04:32:00 | NPP-375D | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e068449d-9ca5-34dd-b285-5acf0182da37 | -19.94214 | -45.24565 | 2025-06-28 04:32:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e006aaa1-8751-3fad-8405-5218de8b40c4 | -21.17763 | -43.98139 | 2025-06-28 04:32:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eb79ada-fea2-311a-9c4e-950ffb652b32 | -19.63564 | -45.18826 | 2025-06-28 04:32:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b10f59f-a14e-322e-8753-ffd9f2880db9 | -19.16521 | -49.13161 | 2025-06-28 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d98a26f-0316-307a-9a4a-7323842b4ba7 | -20.31124 | -50.37096 | 2025-06-28 04:32:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| af6d0495-c2b4-313a-a19d-330d7c42dd4e | -21.60666 | -57.57018 | 2025-06-28 04:32:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81440fdf-b35e-3317-ac91-4a111165252d | -20.8521 | -45.53283 | 2025-06-28 04:32:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3b0e4db-6156-30a7-bee1-957b2d0e73e3 | -19.16464 | -49.13527 | 2025-06-28 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0d137bd-ab04-3432-9c4b-5525719bd8bc | -19.96754 | -44.21738 | 2025-06-28 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1a6cad68-874a-31bf-a2f7-814c820553ca | -17.61467 | -48.28065 | 2025-06-28 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 46df1e60-e21e-3049-a1ce-98f11a4839af | -19.51992 | -49.28984 | 2025-06-28 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13f7f301-83f3-3b87-a948-42f024c0708d | -21.63394 | -49.84137 | 2025-06-28 04:32:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab23f815-10c0-303c-9872-4022489a20b6 | -23.59321 | -47.43891 | 2025-06-28 04:32:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d235f54f-9ed7-3f62-a944-aba2df29f971 | -20.24045 | -46.74557 | 2025-06-28 04:32:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 677bc347-ff1b-35e7-a5a9-6fcc2fc37b95 | -19.16739 | -49.13951 | 2025-06-28 04:32:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2eddc69-2c29-38f4-ac32-65606ac8c09c | -20.99472 | -51.79338 | 2025-06-28 04:32:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a4efa47a-41c4-33f6-a2e1-6fe0f1fcdf8c | -21.19446 | -44.93671 | 2025-06-28 04:32:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README20.md)
