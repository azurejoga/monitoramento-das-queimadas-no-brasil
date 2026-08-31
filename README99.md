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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69066787-6842-35a0-9ec7-13232842755a | -11.3611 | -45.2185 | 2026-08-31 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d9ae577e-018a-3089-9b52-719eafc70244 | -8.7442 | -46.4437 | 2026-08-31 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0c2964a1-d2ca-3e17-9200-db6175d139ea | -14.6535 | -53.5642 | 2026-08-31 15:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 42d106ad-735d-32f1-b75b-45bb5bdb95b1 | -7.9907 | -46.5177 | 2026-08-31 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 6cc50678-c747-376f-b989-6707608937c6 | -6.9177 | -55.6967 | 2026-08-31 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 940c2cd3-9a62-389b-bfcf-a40773cc41d4 | -10.8804 | -50.4965 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3b6594be-ff6e-35cb-b2f6-c30b63b1e95e | -6.9368 | -55.6161 | 2026-08-31 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b1fef751-1f8c-344f-b431-caf6370707bb | -5.8537 | -57.5576 | 2026-08-31 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f5796757-983a-33b7-87e6-7e4c7e7469f0 | -11.5475 | -45.4906 | 2026-08-31 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 084f0971-b567-3c00-ae76-eb6375dd313e | -18.2695 | -52.7284 | 2026-08-31 15:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2791f7a3-2d90-3606-918d-b62818ce6a96 | -3.6076 | -59.0769 | 2026-08-31 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 047707d9-13a9-3bc1-b590-7f508028d5ce | -15.2475 | -53.8876 | 2026-08-31 15:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 26fc30db-62c9-338d-a89b-6754dfb8c888 | -5.2363 | -55.8914 | 2026-08-31 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4f75b6bd-4661-3122-ae2a-c64b0712fc29 | -10.8614 | -50.4985 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| bd80de8c-534d-354f-8d78-e36a91f503fd | -19.4706 | -57.5636 | 2026-08-31 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.5 |
| 0d1f8cbe-a955-3ad0-9ac0-621e40a47d66 | -10.8463 | -50.2224 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ac48c56a-957d-31d3-85aa-36aa33bc5512 | -10.3394 | -49.9547 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 796e6b9d-e803-33a0-a052-83f75d2c2a39 | -14.5674 | -54.1176 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 247.6 |
| 46707af1-b350-3c0c-95ac-5e27d42ab45e | -10.8046 | -50.5046 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9c01c95d-d023-3963-b071-058af40efb1f | -13.8563 | -54.0967 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 4abebb81-3b6d-3ed5-8cfa-8705c2b0f87f | -9.7126 | -65.0951 | 2026-08-31 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a640e66b-9fbd-310c-afeb-6d237c1c5929 | -2.6741 | -59.382 | 2026-08-31 15:10:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| aa06d0c7-21c1-35c1-b50c-dbbb6b132cc3 | -11.2125 | -54.0181 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 63062134-f396-3c66-bee9-0e574346a2cc | -10.7431 | -50.8514 | 2026-08-31 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 455f889d-4fff-3c33-bf65-0190707435df | -11.0054 | -49.6893 | 2026-08-31 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ba0bbbb5-0ac6-3e6b-8531-cdcb71d72eae | -11.8218 | -50.9896 | 2026-08-31 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ed163724-01de-3933-b78f-aa51b40563de | -11.1723 | -51.294 | 2026-08-31 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 7c58af55-2fa6-398f-addd-8408fbda1335 | -14.6899 | -54.912 | 2026-08-31 15:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0f6ccf96-ee14-3422-ac23-21bf6c80dfdc | -15.2465 | -56.39 | 2026-08-31 15:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e91b6e9c-cd57-325a-a857-bb547a679a71 | -14.4644 | -53.3361 | 2026-08-31 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ef77b55d-f9c8-3b9d-9bb4-0a915acdfdcf | -13.4899 | -57.0556 | 2026-08-31 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 5f68d484-7c9f-33dc-976c-624870d07fc5 | -12.9056 | -59.8661 | 2026-08-31 15:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7ccb6e87-eeca-3362-8614-06c29bcac5cd | -10.3202 | -49.9782 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 250ce37c-23a9-38f0-9349-79640abb5735 | -10.1087 | -50.2776 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d4865351-7f24-3334-893a-54d254b89103 | -10.7598 | -54.0179 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 913a8f57-6306-3b53-a9e6-a645a1a3eeb5 | -13.967 | -54.395 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| be542363-32c0-38ba-80c8-69d2901a665a | -15.2669 | -53.8851 | 2026-08-31 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 258.4 |
| 9a7253fb-ade7-36bd-9a69-5a385595d363 | -13.4707 | -57.0574 | 2026-08-31 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 153f0e5a-0b5a-3c26-9543-cb97d3d115b0 | -8.7439 | -46.4661 | 2026-08-31 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c6d161a7-dffa-37e7-9825-451beca8b621 | -5.4876 | -57.1416 | 2026-08-31 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bcefb8f5-8d39-3712-a118-7653a9d12d9c | -14.5678 | -54.0968 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 5f05d81a-b889-3240-8a51-fee830fc7f9c | -13.8567 | -54.0759 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 06bc544a-6403-39eb-ba94-6039367c955d | -11.2503 | -54.0146 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1befbd90-d83f-3bd1-8054-bd5e6e4de2ed | -19.4907 | -57.5609 | 2026-08-31 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 54ffc7b5-730c-31bc-bd7f-2e7f52f18d0d | -8.9481 | -62.3704 | 2026-08-31 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7aaac537-885f-3995-91ec-13caffe7cafd | -9.6939 | -65.1145 | 2026-08-31 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 264.9 |
| 3f0186d1-e44d-36b3-870f-fbee112b89e8 | -8.7631 | -46.4418 | 2026-08-31 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 54b65daa-44eb-36eb-97b5-64ff90305f53 | -9.196 | -64.4568 | 2026-08-31 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 96132fc3-8f17-3a7f-b348-ef141eb317d7 | -4.1515 | -60.7068 | 2026-08-31 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 088f8620-096b-39c0-a94d-0d8a5646734c | -10.5607 | -50.3595 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 48bf6632-5c9f-37d5-95a5-ef508dfbdb65 | -12.1714 | -50.5217 | 2026-08-31 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e72cfcad-f4f9-39e4-9339-59c6abfb08b6 | -5.2548 | -55.8907 | 2026-08-31 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 6f731ab8-da3e-3093-9e65-b26117b6db3b | -18.27 | -52.7068 | 2026-08-31 15:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 02d37e87-755a-3a77-8869-623d997ce502 | -14.2985 | -52.8733 | 2026-08-31 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e306aaab-06bd-333e-9d00-68e54b61d1e9 | -3.6216 | -60.547 | 2026-08-31 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 26e1f3cf-589c-3816-a22a-76b55091ee2c | -7.2934 | -60.5713 | 2026-08-31 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 971fb496-2e00-3598-8b71-810f4a033457 | -14.5871 | -54.0944 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 71fb8874-32e0-3b8c-8be8-983923c5ca09 | -7.9794 | -44.3193 | 2026-08-31 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 97313127-d024-3b47-ba15-2271f945f21b | -18.2704 | -52.6851 | 2026-08-31 15:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 3a9b8c11-f539-3905-9fec-d6308e2234b7 | -6.1295 | -57.6637 | 2026-08-31 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a8b570fc-f350-3a2f-997e-a2cf019cf3f9 | -11.6247 | -50.1783 | 2026-08-31 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 8c8bf211-dfd7-3d95-bbc1-9a26128deae3 | -15.4231 | -52.7049 | 2026-08-31 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 17714ceb-2791-3cba-a456-01c85234fd7c | -8.799 | -62.4905 | 2026-08-31 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 95ec0d7a-5482-3c0c-9bf6-bd60c1c59010 | -11.0057 | -49.6677 | 2026-08-31 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5e2e613d-0da2-3881-bc47-c747ab447488 | -19.17 | -57.45 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 75361009-776b-3c2c-890a-ece462700ee3 | -19.14 | -57.43 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4f1d0ab0-50b9-3b80-ab7b-3ad89cb5f6c6 | -19.17 | -57.38 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 537c828d-3505-3874-8275-89431a739d3f | -19.2 | -57.4 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4ccdb193-0a27-3cb9-96dc-053e052b2186 | -19.17 | -57.3 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 608a1c6b-b6f9-390b-a03d-76c5c5da5150 | -7.98 | -44.32 | 2026-08-31 15:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 94a442ac-d36c-3bb0-9b8c-4e69e440878e | -19.14 | -57.35 | 2026-08-31 15:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a1d29bc5-4b83-306c-ad96-d32d49853bff | -9.196 | -64.4568 | 2026-08-31 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5712ea1a-19cd-38e6-bf15-2dc0915ec6a1 | -19.4907 | -57.5609 | 2026-08-31 15:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| c4d46cc6-8977-3ce6-97b5-1a1cc619e4ef | -6.5234 | -51.4279 | 2026-08-31 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ab4076f6-fc6d-3ecf-b6a7-55112587cbe9 | -6.2847 | -53.5792 | 2026-08-31 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 118c930c-5d91-3acf-bf62-6f27a1a9415e | -15.6336 | -56.3876 | 2026-08-31 15:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 32a8b899-605f-3e80-82b5-8abb8c4ff531 | -13.471 | -57.0373 | 2026-08-31 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b2a7538f-eac1-3586-9e42-7b6da3e5df41 | -5.2363 | -55.8914 | 2026-08-31 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| aad7f618-c65f-39aa-a2ec-9d3d9f3fbfe3 | -9.4156 | -45.6499 | 2026-08-31 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 8212d481-1d55-35c0-8370-02e7bf9ef1de | -10.7409 | -54.0196 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 2b7ed418-4677-3ae2-a058-107fbd368bf9 | -10.7856 | -50.5066 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 137c5526-9ac3-37f0-8a8e-9450ac720377 | -9.5967 | -47.5983 | 2026-08-31 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 130ded38-7334-38d0-90af-f921b80a4f7d | -11.3423 | -45.1982 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| e15ce9ba-76a0-35b6-a8ee-30b396543c64 | -3.6398 | -60.5656 | 2026-08-31 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 3cc7ae04-b227-35e3-ab8a-cda27a5cd6c1 | -10.8215 | -50.6519 | 2026-08-31 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7e9121c2-6e73-3a70-a793-60a5e593b72a | -8.6156 | -54.7743 | 2026-08-31 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7461ea13-1a76-392b-a8d6-d38226b87b8b | -10.8425 | -50.5005 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 22546dd1-ab29-357a-9500-cd4cd85bf1f1 | -5.9636 | -57.6704 | 2026-08-31 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ed079c16-62b3-3499-90c0-aba596a952ff | -10.8807 | -50.4751 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b564c7b8-e737-354c-a072-4eb72e8705d8 | -11.1349 | -49.9117 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| d52c39e2-434f-3046-85a2-2d3cad4ec2f1 | -3.6216 | -60.547 | 2026-08-31 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 796021fe-5dd9-33b5-ba80-e006c89c9acc | -11.3806 | -45.1928 | 2026-08-31 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.2 |
| b70594c8-e656-38fa-b6fe-979218714bed | -10.8617 | -50.4772 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0042c2bc-b158-3c23-9913-cfccf355fd7b | 0.1914 | -60.4878 | 2026-08-31 15:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9ed3d54a-a064-3ad5-811f-535b6726a071 | -6.8751 | -56.5116 | 2026-08-31 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7ae42c68-a5f1-3814-9a08-5b25f552acfa | -11.1824 | -50.5706 | 2026-08-31 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4a50a661-cbce-302e-ac8e-5d3d95728ca0 | -12.1714 | -50.5217 | 2026-08-31 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f10b2a52-6d37-32f4-84ab-4451d3dd4965 | -12.9054 | -59.8857 | 2026-08-31 15:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 6301a9c2-f2a4-308d-b1fa-ecfa22963e02 | -6.9177 | -55.6967 | 2026-08-31 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 210f87f6-791e-3329-beca-8df14b9d79e5 | -10.7407 | -54.0401 | 2026-08-31 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 246.1 |


[Clique aqui para ver as próximas entradas](README100.md)
