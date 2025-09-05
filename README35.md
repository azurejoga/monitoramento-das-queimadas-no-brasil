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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1424becf-00ac-3e07-a13c-84e4e0a1d1a8 | -15.61374 | -52.91285 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4218f09d-ac82-3064-81d3-e7b715810028 | -12.98926 | -54.83085 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6ba3c59-60e9-32a6-a0eb-5defb53ced40 | -12.98646 | -54.79882 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fe2f567-2a69-3921-ac12-e6e56b6703df | -14.52272 | -48.08048 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 069387ee-a67f-3a04-b044-42b5e430a0cd | -15.70891 | -53.61784 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dfddc3d-4c2e-3e2b-8f0e-9c501d504cbc | -14.98053 | -50.07961 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06b6d211-7dc9-3451-975a-178932e04c44 | -15.75838 | -53.64812 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 960a07f7-2a3f-3488-bc90-f3a27c7b9de2 | -14.59013 | -48.00378 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28fb2c0a-c38f-3a96-9ae9-74a46665775f | -16.31472 | -52.94985 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a898f406-0add-3ff2-aa59-6ecbd6b2a268 | -15.21582 | -52.70324 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1d43f3c-5b39-3996-a140-2e6869e4efde | -12.97132 | -54.81173 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b1283ba-2d0b-37fa-bfe6-01ca6aef7951 | -15.86405 | -48.9833 | 2025-09-05 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 479e9c52-9004-326b-ac84-9856b958372e | -15.6202 | -52.89663 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 321c86fa-0165-3702-98de-94fb0a25852d | -15.13728 | -48.16388 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92fdf820-9a68-30ba-bc72-65f63c5c5afd | -20.75532 | -47.13175 | 2025-09-05 04:38:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2606ced-ed0a-3eca-8cdb-2dbb41b16181 | -14.43959 | -52.9798 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bdc64991-8d44-3b63-93a2-20dea71ca2df | -14.58503 | -48.0374 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eefecc0a-659a-36e4-b2cf-353b16819057 | -18.98808 | -44.22971 | 2025-09-05 04:38:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1a3e176-c700-32cc-8150-9cb318c4fbdc | -15.05422 | -50.08052 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ad4d296-0b55-38c6-b6d0-fcd798b960a6 | -15.60944 | -52.91643 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 049414c0-5da8-3638-b4af-b35c82f889b1 | -16.89946 | -45.74132 | 2025-09-05 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61901415-b378-36e7-80d1-583f29a699ea | -12.98719 | -54.81852 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a1e8a3f-123c-39d3-a981-79efa3eedfbc | -20.93995 | -47.40842 | 2025-09-05 04:38:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b1cad00-0dfd-3f62-b42e-f1f4003123b5 | -12.98029 | -54.80938 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3afe3ec8-ba5e-3a33-8d61-c4a8e5c7d15e | -12.96171 | -54.79401 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6e942333-f305-3153-842b-d37b18acd2f2 | -17.6665 | -52.29204 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac073da1-4f1b-3a0f-8cde-4a9bb14e86ca | -20.23808 | -51.30767 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d62bec6b-eca7-3146-a2f5-57d1c34f19cd | -14.99603 | -50.08961 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd1a310e-f771-381e-be2e-597d254405c9 | -18.73484 | -46.88961 | 2025-09-05 04:38:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8463b541-cff3-3502-a599-b2719e97ce6c | -12.88574 | -56.95142 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76d6c2e9-cf7f-3ffa-9656-7d6e90617e8e | -14.56013 | -48.08664 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3926fd79-b0de-3f85-8765-8425f8127d6d | -14.58558 | -48.01075 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 083088bf-8bc9-3137-8b42-256c4b847d9d | -15.85447 | -52.30009 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e2968e7-fe7c-347e-af00-cb5825109bbb | -12.96583 | -54.79482 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 52ce4e66-e4b2-312d-9b69-4e04c7006340 | -16.3183 | -52.95041 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b740e240-2044-3110-a8d3-8fefa4ca136a | -14.54164 | -53.05709 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a13082-861d-3fef-9b11-baffa8a8a2da | -15.06822 | -50.05703 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 178abbb2-e5b6-3ad4-b26e-d4772c025d8e | -21.33939 | -43.7565 | 2025-09-05 04:38:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 21d440dc-b001-3852-b9e9-deba1fafc69e | -15.14736 | -52.38109 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cffa91a-8de8-3cc6-8fd6-a7756ff5c1f6 | -14.58558 | -48.03374 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5661250c-a219-3c64-8c76-739c341ee1e3 | -13.28161 | -51.78874 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9141d8a5-796c-3488-bf50-0996b1e065ac | -14.4845 | -54.02645 | 2025-09-05 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022ac085-465a-39b0-9ead-b886e428bf86 | -14.58843 | -48.03798 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeef0833-fb80-32f0-853b-00b6297db183 | -15.9965 | -55.95171 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| eddc1807-05a4-32fc-a208-afbdba79dc11 | -15.16775 | -42.59855 | 2025-09-05 04:38:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6ff5ee1-6a17-3b0f-b6bb-b457faeedce0 | -20.93719 | -47.4109 | 2025-09-05 04:38:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c75c858-9477-3de7-990d-7802f1f9ece8 | -18.61509 | -44.26069 | 2025-09-05 04:38:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e81c9e9d-b934-335f-b492-45342102406b | -15.74077 | -53.61015 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a33ac13-69de-3681-a9bb-90581072f185 | -18.73548 | -46.88503 | 2025-09-05 04:38:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 340dcfa4-9027-3de4-a2d3-cb6df67d3c7a | -15.56537 | -46.49563 | 2025-09-05 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e78acc-d372-3b50-8ef4-bde2871310ec | -15.20157 | -52.3815 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29549812-9fe2-3a71-b26a-0c9302a68b32 | -14.53803 | -53.14217 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 910ecd6a-01fb-3833-9487-cbe5f9edf9f1 | -16.37567 | -43.03564 | 2025-09-05 04:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c81f25a0-03bc-330c-a878-e4465618a8f6 | -15.07706 | -50.0659 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d5d131c-ce3f-3a5a-8a42-87611286fdd1 | -13.87417 | -48.01501 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f03950c-211c-3e74-bd9d-d68f239bea4a | -18.68368 | -51.80725 | 2025-09-05 04:38:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 156eb68d-5ea3-3f44-a9a6-9a82ac06e4d7 | -15.05064 | -48.11589 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c71c6bca-a431-3fb5-ba3b-5648d504f549 | -15.22353 | -52.38022 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 494385c3-adc2-3678-8e58-a212752791f1 | -15.03134 | -48.12827 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef731238-8f7d-3911-bc0e-a3c1d0ab77a4 | -18.87009 | -46.37374 | 2025-09-05 04:38:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ed0ddf-230a-35e7-9676-02bb9a3ac5db | -14.58615 | -48.00698 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d95359f0-9dee-332d-9f59-dbb1d6b0b784 | -15.31677 | -52.74566 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e851980a-f626-3499-b061-aa5bb5342851 | -14.13533 | -51.71888 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7232f6b-bde6-3d3d-bf9a-d53bb139693b | -14.9966 | -50.08603 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6626b28-f4fa-30e2-9a18-7c6351d9db07 | -20.7549 | -47.13465 | 2025-09-05 04:38:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef89f1a6-725c-3c0c-9265-46c2bf8e03ce | -14.59694 | -48.00489 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45837650-04d6-3e1d-a917-891400c9b87a | -15.71867 | -46.22876 | 2025-09-05 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a9098e6-cf57-3691-bbf6-a75502f3874c | -18.95534 | -44.68269 | 2025-09-05 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2187de4a-ccf8-3ca4-a63b-9c42d5001b04 | -15.22286 | -52.38415 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dae26ec-8510-340d-972e-39181c109506 | -15.22636 | -52.38482 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47e8574-db17-3554-9dc4-7e8816502209 | -12.99891 | -54.8247 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1a7bf003-0a53-34e6-a42a-a6627ce508bb | -14.56308 | -54.53709 | 2025-09-05 04:38:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419b02eb-bb6e-3ef4-96b8-1b254ea2596a | -19.50862 | -42.56894 | 2025-09-05 04:38:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8071b166-314a-3db5-b870-de41cbf27bc3 | -15.02848 | -48.124 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc12bb36-9cfd-3690-8119-f56ccdbe2011 | -12.98097 | -54.80559 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3fc9956-899a-34e4-9511-2bb8b9f682bf | -12.9865 | -54.82236 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b3842a2-9fc7-3755-abcc-4004a7ca0a1a | -15.13947 | -52.34225 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 962ab8f9-6897-3d25-8601-33da4eb7bf32 | -18.61944 | -44.26135 | 2025-09-05 04:38:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fab617b7-697a-39b7-90a0-fbc32372308f | -15.20072 | -52.36499 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4852cba4-f251-3806-b0f2-6ca6040502e8 | -15.05088 | -50.07996 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b31a14a-4ab6-37d3-80de-410684ebd6b6 | -15.60445 | -52.90247 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef09810d-77e0-3ae6-9113-a68043d4b205 | -20.93623 | -47.40779 | 2025-09-05 04:38:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea08af1d-2f74-3998-bfdb-07d9a25e2c05 | -18.57757 | -44.02474 | 2025-09-05 04:38:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2278d3f9-11db-34c3-aa37-010d8e4244a8 | -17.53233 | -46.61774 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4734bd6e-7f51-358e-b5ee-de9ab41af43e | -12.9672 | -54.78727 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4ab8d83f-3e6c-38a1-bc5b-efe392d8a462 | -19.79487 | -43.55196 | 2025-09-05 04:38:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 876fa9f7-7051-3347-8b49-a8bcc3ed6b4a | -16.59944 | -50.82971 | 2025-09-05 04:38:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd41daf3-71d2-3ab0-8c8c-8fc3f5ae6d13 | -18.98805 | -44.22835 | 2025-09-05 04:38:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e76fb15-a529-363e-9929-5e088cc18f3c | -18.54342 | -46.69239 | 2025-09-05 04:38:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e05c1037-4b8a-38a2-8cb6-5349cba61805 | -13.88095 | -47.99314 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49339af7-de10-346f-9d5c-6ac808d4555a | -15.19939 | -52.37292 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7623efc3-cd16-3ef0-ac1d-a83debdd1626 | -15.71123 | -53.60451 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ab4684d-c4fc-3e5f-857f-4fbe8d71b19d | -19.50917 | -42.56937 | 2025-09-05 04:38:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c46e89bc-d95e-3244-aca1-811072e5ec73 | -15.60373 | -52.90667 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaa216a3-3384-3d7e-8eb6-68172c4a6765 | -15.71336 | -53.61417 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db1ff8e9-ba6a-3763-8642-da72b68679a0 | -15.04698 | -50.08298 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d78da5-dc7b-388c-9793-5189044ba0ed | -15.54886 | -48.39309 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23777fbf-f39f-3d0c-b822-e85b8617ebb5 | -15.05651 | -50.06614 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd38c8bb-a2f6-361f-9370-f59c1951eced | -12.9782 | -54.79728 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ad12e64-705a-342c-8a59-16f0b0597215 | -15.14506 | -52.33065 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
