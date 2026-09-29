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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187b6335-f1a9-3ec9-b730-0f4333cf27a1 | -3.71145 | -54.21328 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bade1d49-51b5-31a3-8f94-4db5520e1df8 | -5.74152 | -45.18048 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7190b596-36f8-3d0d-9740-ca4e3289efcb | -6.13634 | -44.1392 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abb62233-e8de-36ab-8c8a-2cc88465d674 | -1.7853 | -47.83454 | 2026-09-29 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 615702c9-5261-39a3-9f83-5bf045596f4b | -1.99283 | -47.63216 | 2026-09-29 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2721590-c7bf-3225-9579-e7b7e5d182ae | -3.51101 | -50.31826 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26ad08f8-b8dc-3b09-a0f5-368dc833f62d | -1.02379 | -49.23292 | 2026-09-29 04:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e0221f7-ac2e-32fe-9cb1-97bcae228786 | -5.73324 | -45.05452 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1970e3db-ff47-3aea-b3a0-0ebb81d221d5 | -4.81188 | -45.01382 | 2026-09-29 04:49:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b460f211-e3a3-3257-a471-5150449f5423 | 1.82262 | -55.62957 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ea56607-a5cc-36f1-8346-27c656403598 | -4.55892 | -44.07858 | 2026-09-29 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4a345bd-b387-3543-a44f-cadc6f77f2de | -3.25416 | -46.61053 | 2026-09-29 04:49:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beb23fce-211d-3d2b-9149-e2bb314925fc | -6.12572 | -43.72713 | 2026-09-29 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d964da0a-f87f-3feb-827b-f26afc6eeb5c | -2.90963 | -54.12492 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dec0b00-2b53-394e-8ec0-bd9a4fc92d59 | -5.61102 | -44.99498 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d476346d-80dd-3434-a6ba-308ec0ae8d91 | -3.15128 | -54.09695 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b15072cc-4969-329b-98cc-cf426a6afba1 | -5.01075 | -48.04724 | 2026-09-29 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a06adc4-592b-384e-9f97-45a80c264787 | -6.94961 | -41.60593 | 2026-09-29 04:49:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b3750a92-bd0f-3edd-b46b-961b446a03e0 | -1.78197 | -47.83401 | 2026-09-29 04:49:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 70a962ad-da98-3604-83dd-ddeeb05b8900 | -4.45748 | -47.91832 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c2e3894-4e40-3997-bb13-fc3ad19b1535 | -5.74223 | -45.17585 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75f330fb-7e0b-3ebf-87e1-94fcb53c90f2 | 1.71446 | -50.94939 | 2026-09-29 04:49:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c0a709c-6c9b-3a7a-90d0-f159b2422a14 | 1.68126 | -55.90973 | 2026-09-29 04:49:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a175dad2-211e-359b-bd36-d39e4ca1de3d | -2.94542 | -48.98418 | 2026-09-29 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a49776e-1e30-3df3-b71e-f9d30f90bf90 | -3.49882 | -48.56853 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| deabf406-3749-36fd-833c-b4269d413091 | -5.43839 | -47.27467 | 2026-09-29 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f706fbed-6af6-3cab-a201-aa32a520b03b | -3.60482 | -49.45206 | 2026-09-29 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5244e01-fdd4-3ff2-a899-8cf852a15a35 | -5.73349 | -43.28122 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6305f538-4f6c-375e-bd03-0d9a95998e37 | -5.42771 | -43.44736 | 2026-09-29 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7742d557-3bc0-30c1-99b5-c6ab663b5555 | -4.82244 | -45.63841 | 2026-09-29 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0983c87-e453-3f30-88f3-81b541c20713 | -4.71349 | -50.63738 | 2026-09-29 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a87379d0-3bca-37e6-b02a-39660245e76b | -4.3592 | -47.76881 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eff3918f-05b7-3a93-8c93-c94d0b490148 | -5.8574 | -47.42461 | 2026-09-29 04:49:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77dfa9f2-c021-3484-a656-2ebe4e2063d9 | -6.14311 | -44.1432 | 2026-09-29 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a35cc53d-9828-306c-bc08-5e394082dab2 | -5.73927 | -43.28025 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e4b153-8d8d-31d9-b6d3-349b7cdac02f | -6.95171 | -41.6017 | 2026-09-29 04:49:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a62f1d7c-cbee-39ae-b93c-cf3ad92dc409 | -5.48319 | -45.1266 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4eb2865-7104-3de6-b292-271d9719f606 | -3.35771 | -50.46663 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ed11f32-39c7-3709-b8c6-8d8aef4e1420 | -5.73076 | -45.17414 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f37df6f3-2328-3574-9ec9-394042c53bfe | -3.95747 | -47.63748 | 2026-09-29 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f00ea92-4cfb-35a8-b04f-02454c228863 | -5.73911 | -45.17067 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8dcc95a6-d879-3216-bf42-a51027825a45 | -3.9574 | -49.0484 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41e535ab-528e-3995-b11e-86c1513bd69f | -4.67565 | -44.57901 | 2026-09-29 04:49:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 689dda8c-6d21-3383-a48a-e58b252f9ec2 | -5.60717 | -44.99438 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7ef74bc-e61e-3cc0-b1cb-b5ae7d99c723 | -4.81572 | -45.63318 | 2026-09-29 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da86d3c4-2dc7-32f9-a6ef-d97d41833e60 | -4.295 | -49.0914 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427758f1-fadd-3be2-93a7-d31c47aa9915 | -3.04638 | -46.92881 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8a1a788-d4fc-3494-b7a0-d2f57abe01f9 | -6.95095 | -41.60718 | 2026-09-29 04:49:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4bc8aff4-489f-3bda-b966-6fdc7e1deed1 | -4.50004 | -42.55159 | 2026-09-29 04:49:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83f3e3f1-9582-3853-9dd0-f763a8fb3268 | -3.02042 | -53.8709 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68e14678-3bea-340d-b11a-b5c532ca55a8 | -6.1731 | -46.74818 | 2026-09-29 04:49:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e03d6d-159c-3405-9cd4-4efd1d2290ea | -3.14477 | -54.08436 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ede910a-023c-337d-b67d-e481cfad5134 | -3.85249 | -52.20763 | 2026-09-29 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e8eaf27-fbbb-3985-99cb-7f340363d455 | -5.73387 | -46.39431 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d815c0a1-6381-3464-8c39-b4644b90f2c4 | -5.72917 | -43.28057 | 2026-09-29 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eca3105-44c2-3774-ab32-b14875a7950d | -4.08024 | -40.51497 | 2026-09-29 04:49:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f92dda02-abe1-34f3-8be1-be578ca16695 | 1.86465 | -55.57393 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87b2ff6c-5b75-3729-aa13-449cbd486d1a | -5.73253 | -45.05921 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b4c07114-8a3a-30d8-a885-b5b5346225ef | -4.32424 | -48.63128 | 2026-09-29 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60db8e6c-7d33-3dd2-a6ec-dbd4912b2731 | -2.57679 | -50.79109 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d1d6313-62f8-3937-9646-6159081724ed | -3.15187 | -54.09325 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 611fd9b0-5d01-3c9c-a1c2-51af6f279302 | -4.37053 | -40.61778 | 2026-09-29 04:49:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 735bb9ad-435c-3d6c-8e57-91931a674c96 | -3.70666 | -54.21638 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9252a59a-2b9c-3e7e-8d32-0ab21c581cbd | -3.14597 | -54.07687 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9554670-e96d-32ce-a80a-3b200d60c89d | -6.12461 | -43.73473 | 2026-09-29 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8cf6d69-d79b-34dd-a247-47b86e58230c | -3.43441 | -50.6643 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4032dead-7b06-3bd8-888c-cb85b002e7d7 | -5.091 | -44.84118 | 2026-09-29 04:49:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88e069df-cfbf-33d6-a00a-ebeae3799535 | -3.51275 | -50.30738 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9d03c2d-884a-3737-8d1c-19e7df59cbc8 | -3.15627 | -54.09762 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6fe57d0-1d91-3ed4-a62b-1d6c6955819d | 0.69887 | -51.43258 | 2026-09-29 04:49:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20aba11e-c61e-3ec7-baf9-5760515fcfee | -3.15306 | -54.08585 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab64263e-079f-3ede-9497-0e7497013f62 | -0.49154 | -49.12444 | 2026-09-29 04:49:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dee4f950-016c-3727-85f5-0325e5584a05 | -3.95691 | -47.64104 | 2026-09-29 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01881d29-15a7-314c-9dee-8f844387f89b | -4.29555 | -49.08794 | 2026-09-29 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27fe5dd6-4601-3177-8c9d-c3baa50612b6 | -5.63586 | -43.72448 | 2026-09-29 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 096f44fa-507f-3b16-8119-5b9b64663edb | -4.49938 | -42.55594 | 2026-09-29 04:49:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 629c89d9-f787-33ec-9b64-c8b6e5413bcc | -2.5756 | -54.74569 | 2026-09-29 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fed68920-fba1-3a62-a062-8511c819a3f7 | -6.17303 | -46.74714 | 2026-09-29 04:49:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f11974-aab7-3378-8f14-736d49e5c40b | -1.4283 | -48.90534 | 2026-09-29 04:49:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5738756e-f5fa-39ab-ae53-e889d5413805 | -5.52516 | -43.95581 | 2026-09-29 04:49:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d8abae6-805e-3072-b1da-2e8bde7ca1a4 | -3.59611 | -50.68168 | 2026-09-29 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1f7fdb1-cf1a-3456-9ca5-fc1251e47b94 | -5.73758 | -45.02585 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 360d435f-084b-3895-b178-1dbb67164d97 | -5.12453 | -47.76171 | 2026-09-29 04:49:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f5fcf19-41eb-300d-b72f-668561fa0e32 | -5.73299 | -45.03012 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb1b31ad-1092-343b-a6cd-74eb010868b5 | -3.15011 | -54.07764 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdad59f5-35e5-3c99-8bc3-8e7762aaf2d1 | -3.02101 | -53.86729 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a885a8d2-c810-3939-ab5a-af0c60b7f9ae | -3.70541 | -54.22389 | 2026-09-29 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e10cc1d-8491-34e6-bb30-e65a863ca201 | -5.03021 | -43.57233 | 2026-09-29 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 196bdb81-9642-31fd-9692-05ca1cf3ba0a | 1.82583 | -55.62098 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9fbb612-39a3-3fd0-8e83-805fe1b59d23 | -4.35864 | -47.77237 | 2026-09-29 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad111552-30ca-3e63-a3e7-5a0f4a09574d | -3.23499 | -50.57961 | 2026-09-29 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c766c905-b428-3a36-81c0-b367920aa732 | -3.71309 | -54.22912 | 2026-09-29 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 136de884-3bd0-39e2-aa37-01ded078baa9 | -4.81875 | -45.63788 | 2026-09-29 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2816c830-0440-3873-b52a-4fa09deda7f0 | -3.6809 | -47.49195 | 2026-09-29 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee4a6680-9188-36f4-8831-3096dd6e57f7 | 1.82256 | -55.63326 | 2026-09-29 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2884e255-e8de-37e2-836e-e73237e29975 | -3.42075 | -48.33651 | 2026-09-29 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b233559-b82c-3676-8c0c-5a83c1c5a9cb | -2.2718 | -48.75439 | 2026-09-29 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 439cd0ca-29c8-392b-9db4-1aa29c17d5b0 | -1.06634 | -50.6053 | 2026-09-29 04:49:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e39a79-52b9-30f9-9602-66d1ea4ea809 | -5.73325 | -46.39835 | 2026-09-29 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e45adca7-0e5a-3a53-a5c2-74dd929e9132 | -5.7377 | -45.17989 | 2026-09-29 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README37.md)
