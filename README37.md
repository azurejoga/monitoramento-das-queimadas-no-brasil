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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6497bb82-2df0-30d4-a967-14b10903083a | -11.89272 | -50.52633 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d47249d-faea-3f26-b4db-791046162621 | -12.71329 | -47.31866 | 2026-09-27 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 759926d2-c2ac-3bec-b1c5-3d7d84cdb6bb | -11.23943 | -49.85434 | 2026-09-27 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d538a65-f12f-3d69-b69d-92a22e47804d | -11.98359 | -50.56922 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 859d5e64-d60b-310f-9b3d-cc17894ad885 | -13.85809 | -43.99645 | 2026-09-27 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7602c940-573e-3bae-9759-816a0a2c5e0b | -12.66269 | -47.31627 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3042c8b8-7293-30ba-8220-5fd2f1aa243a | -11.04473 | -51.32695 | 2026-09-27 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74748d1d-0640-3eac-8258-31a176e68253 | -12.76517 | -54.04406 | 2026-09-27 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8fae29-7cc2-39b0-9212-5d851fdf216d | -12.90172 | -52.0598 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9922a683-4c3c-3963-a64f-3aec60ccc11a | -12.76124 | -52.82166 | 2026-09-27 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10e539af-776b-324b-92a8-4363a0cd7535 | -12.28823 | -50.2889 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1771c3de-f5c1-3504-b71d-c08650a4232f | -10.82568 | -60.72164 | 2026-09-27 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bddff04a-a567-39f3-b0b8-9815fe12f57e | -11.03429 | -54.04064 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab9332be-bbbf-3fb3-9b30-30a27b506c3c | -11.89337 | -50.52193 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7858f055-79d6-3c09-af26-16bec00bd06c | -14.52842 | -48.32711 | 2026-09-27 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283bd6a9-e17c-3ae4-a152-9c30debda6bb | -11.7732 | -51.01741 | 2026-09-27 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5102291-a992-31ec-938b-191498f82b1a | -12.6689 | -54.63789 | 2026-09-27 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c293290d-9712-31c0-bfbd-fc67e1f62c3f | -11.88858 | -50.50328 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e96192f-4ed8-34a8-ac74-647e5b92b278 | -11.28132 | -54.43979 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 541cb109-81f9-37db-abf8-ddb937e5dc5c | -10.88196 | -54.03762 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a840d1d-66ac-338d-a18d-df2176893249 | -10.0188 | -52.09573 | 2026-09-27 04:53:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe39406-ce17-3927-8a33-53c0f71fdd7e | -11.27581 | -54.4317 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df7008ea-02e8-351f-a7dc-73e4dc1229dd | -11.71047 | -59.13598 | 2026-09-27 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28e58cf8-ec1f-3784-9008-025eef232e52 | -11.24011 | -49.84966 | 2026-09-27 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2041a8c4-b25a-356c-9475-1481d32ff966 | -14.68979 | -59.60613 | 2026-09-27 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f137366-e8d4-36ab-99f9-bcc984c87b4c | -10.04168 | -53.77689 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1ddf4f-bb3a-393f-b032-e999774b73d0 | -12.89847 | -61.71538 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da63c0f0-703d-320c-b373-7abbfb9c1e73 | -11.28243 | -54.43276 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a03c3c77-6442-31bd-ba7f-aec77ad130e3 | -10.22215 | -49.98415 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbbb623e-a40e-3c94-b941-8218e4012cde | -10.89395 | -53.93937 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0aea74d-b48a-394a-a21e-3d2be5ae1866 | -14.11896 | -46.33491 | 2026-09-27 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92666ff7-33aa-3f2e-bdc4-f5fd907a0b9d | -9.57223 | -62.7015 | 2026-09-27 04:53:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d20504f4-9f58-352d-8e00-7d0647aabb67 | -14.12037 | -46.32322 | 2026-09-27 04:53:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68dde163-40ff-32e2-90b7-4e6aedb1c02d | -12.59775 | -51.95979 | 2026-09-27 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ed87c8a-962b-3b59-80a6-205168154268 | -10.68026 | -57.63869 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7583aab4-b5fd-3e05-850d-7ab30b5ad7cf | -10.67728 | -57.63349 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9474fad3-0bbf-35c6-889c-9a9bb149132c | -10.01787 | -50.15263 | 2026-09-27 04:53:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ded43b7c-ff7e-378f-a53e-6aee18520b7b | -13.7016 | -48.81649 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9baa12cf-3a0e-37b8-b6bd-80eca34774a5 | -12.13931 | -50.33428 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2daea2a6-a6bf-3016-8b33-e86dfdf3edda | -12.29582 | -50.262 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff3049dc-a246-3604-a033-f1a26067c79f | -12.89381 | -61.71449 | 2026-09-27 04:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e86c462-4906-30d9-b05b-3b21fb39334e | -11.0553 | -54.19089 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddccac93-857e-3064-8501-ee6b280f1959 | -11.05475 | -54.19439 | 2026-09-27 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba9dc9e8-c802-327b-887b-ab4ed2317d02 | -11.9007 | -50.52304 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25c64d8b-f087-3aa9-abed-cebce3d26542 | -14.68884 | -59.61137 | 2026-09-27 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d546cf4-c291-334e-9a51-130e797fd4e3 | -10.41631 | -53.81569 | 2026-09-27 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a08811b1-31e5-3cd2-8e08-c433538bc969 | -9.04543 | -66.1077 | 2026-09-27 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93cefe8e-b2b2-359e-83d4-eb2f86b082f1 | -11.89815 | -50.51159 | 2026-09-27 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ea6f9b-a09a-3f31-9fee-4f4c90a98b45 | -12.66507 | -47.29736 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 996e205e-7432-3de7-a53b-c5a53d615cfd | -12.66681 | -47.31081 | 2026-09-27 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e15e70a8-0f2c-3a6c-88c4-22b4f88e30b3 | -11.9891 | -57.60118 | 2026-09-27 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e6996ce-bb2e-3edc-b95d-ab5776be7589 | -14.79967 | -45.96217 | 2026-09-27 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 246bf491-5409-3b70-aa4a-05e4e609a28f | -19.64106 | -49.68653 | 2026-09-27 04:55:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6eb862ee-a833-3b34-b18f-835043436d73 | -17.05238 | -56.58247 | 2026-09-27 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 6840d266-17b0-3a16-ac16-9becea2d681f | -21.63797 | -53.70049 | 2026-09-27 04:55:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c8d777b-0bd3-3721-b866-9066e85c6760 | -18.24001 | -55.38201 | 2026-09-27 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 471329da-902d-35f9-bb50-dbdf13c1336b | -19.20041 | -46.52387 | 2026-09-27 04:55:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 664ccb31-318a-34a0-97e5-48b6cbcb058a | -19.64054 | -49.6908 | 2026-09-27 04:55:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b91b51e4-4c98-38f2-8bef-e8d7d8ca5624 | -15.29375 | -59.2619 | 2026-09-27 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ebb23cb-a861-3412-aabc-cdcb4162b32a | -17.05178 | -56.58617 | 2026-09-27 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2fc4a8b5-c862-3712-80c2-a84d6a2f0cd5 | -15.99281 | -54.93937 | 2026-09-27 04:55:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 074001df-7aee-3b57-8531-5f41556efbb7 | -21.56567 | -56.73417 | 2026-09-27 04:55:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67d296f2-2a15-3571-95dd-2a79d4e20c17 | -21.5242 | -45.11419 | 2026-09-27 04:55:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 578b95c1-8ed6-3080-9875-1b10c22f6085 | -21.28862 | -57.89977 | 2026-09-27 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bb2a3d40-3575-3c9f-8a60-19030c87810a | -17.3859 | -46.73727 | 2026-09-27 04:55:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e4099bf-3902-3629-a148-064ed17b29e2 | -15.99336 | -54.9358 | 2026-09-27 04:55:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e749afb-e9bb-327e-b254-b7d7ded139df | -17.79024 | -47.16472 | 2026-09-27 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08e1051e-bee4-3ab9-9d69-bd42274f9553 | -17.04628 | -56.57759 | 2026-09-27 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 65edbb3a-a851-3a03-a7b9-f593c958eef3 | -20.19494 | -46.20108 | 2026-09-27 04:55:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd3f9dc-1279-37ea-b8ad-55ae4e2f51e5 | -23.00166 | -48.61957 | 2026-09-27 04:55:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952dc6d9-f509-38f1-9bff-0f0c8e8a8bc1 | -18.03396 | -48.10201 | 2026-09-27 04:55:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49c7eca5-76c7-311c-a0f7-1919c65b5cd1 | -23.00227 | -48.6142 | 2026-09-27 04:55:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26ec517e-26a7-3c04-88fd-2825431b1ef7 | -16.57051 | -53.06775 | 2026-09-27 04:55:00 | NOAA-21 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79e012ff-5bb2-3419-9207-44b668ae7b6e | -17.05298 | -56.57876 | 2026-09-27 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f0dc6c11-a16f-3e6d-b37c-58f949b4161b | -18.79942 | -48.04179 | 2026-09-27 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8b03d227-e564-30c5-8ea0-b33d3077bc7b | -16.86095 | -54.93317 | 2026-09-27 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64224714-54dd-30ef-b72a-756bdc7a0607 | -15.9776 | -55.62002 | 2026-09-27 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74938133-f7b8-3885-88a9-48ff80b1ea0c | -23.00586 | -48.62571 | 2026-09-27 04:55:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e4a12fa-a6d0-33a6-bd88-599b752dff2c | -17.78959 | -47.17043 | 2026-09-27 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d71e52e5-36ff-3c2c-9abe-5e015c96811e | -23.00595 | -48.62588 | 2026-09-27 04:55:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6b7ab51-b0f5-3d6d-b99f-081ad8796d6b | -18.79761 | -48.04097 | 2026-09-27 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 368437c1-6ffc-3211-b55a-aa67728d6574 | -17.54918 | -52.80326 | 2026-09-27 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fa9b899-f266-33f6-89d9-fe6aa8164dbf | -23.00225 | -48.61405 | 2026-09-27 04:55:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d51f414c-9e26-30ee-a141-3bb57b4c664e | -21.52552 | -45.1155 | 2026-09-27 04:55:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 92900146-4069-3939-aa34-b6b8eb50cc25 | -15.9895 | -54.93882 | 2026-09-27 04:55:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f06b7cf6-fe6c-3bf8-af26-98a6677e575d | -20.84053 | -57.69871 | 2026-09-27 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b775241-ea96-357c-9916-3a85be85ea14 | -19.64002 | -49.69504 | 2026-09-27 04:55:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cf874d67-8b5a-38d6-9aab-46b8bffec4a8 | -17.04963 | -56.57817 | 2026-09-27 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3e99e488-326e-3ded-b23d-3be64a4afd70 | -17.04293 | -56.577 | 2026-09-27 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c2796b4d-d97b-3e78-8a41-99326bcbb6f4 | -16.85641 | -52.78841 | 2026-09-27 04:55:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e470b0d3-babc-386a-8f7d-38ba098f4b47 | -19.64481 | -49.69141 | 2026-09-27 04:55:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7ffc43e-65ef-312d-b20b-ce4cd90d5167 | -17.83195 | -46.56408 | 2026-09-27 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3fcb2ae-5908-3d35-93fc-d32c5777c597 | -17.57555 | -46.90608 | 2026-09-27 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1eec2b6e-a004-3080-934d-008c5d072eee | -17.83229 | -46.56092 | 2026-09-27 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 989538b3-a848-321f-be12-6efe86f91808 | -20.8541 | -49.06612 | 2026-09-27 04:55:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 5f454c07-88f7-3045-87db-562f8db22dc7 | -17.39094 | -46.73797 | 2026-09-27 04:55:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c321737c-e26e-3586-a666-71d288fd9571 | -18.797 | -48.04613 | 2026-09-27 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d4ea75ff-15ab-3f38-9267-9780761fc2f2 | -15.99006 | -54.93525 | 2026-09-27 04:55:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b63485aa-3ebc-3efa-a82e-003a15bdcc19 | -17.79092 | -47.15881 | 2026-09-27 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f449af4-216f-3d90-ac0e-df1382667145 | -18.79885 | -48.04694 | 2026-09-27 04:55:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
