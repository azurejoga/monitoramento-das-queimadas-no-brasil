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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c480b619-5df3-3dbe-8c42-fa9fad01cb62 | -5.46256 | -42.84127 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 102755ac-04ab-3e56-ad53-c6a60dfa3f86 | -5.15619 | -46.42249 | 2025-10-02 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 313b16d7-454b-319d-8c48-f850a0c88aa4 | -3.46261 | -50.09055 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0acc64e3-9243-30b1-8f7d-e7dedc73866b | -2.26555 | -47.84939 | 2025-10-02 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 229a6f18-6fcf-3488-92fb-51d1669b3542 | -5.45099 | -42.84378 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 994ae607-3eb5-3102-b967-b5fb6c2fb62a | -2.9252 | -48.30368 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d9f43eb-cc01-3aa2-81ec-d0e4e605a011 | -5.89324 | -44.72758 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 704b5e15-1864-32dd-a09c-9cd95be25677 | -4.39561 | -49.77142 | 2025-10-02 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54a7580-d40c-36d6-aa88-a8381d322c92 | -6.08455 | -42.49023 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d18d663-49be-3686-8d7c-06b85051d2c1 | -3.34308 | -43.1929 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 63d35c03-017b-32c0-a0ad-8580fa41c656 | -4.31176 | -48.09242 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949fa972-acfa-30ee-a074-a28951193dd2 | -5.45828 | -42.84492 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95d33395-08f8-310e-ba53-f12524244b9f | -3.09297 | -47.01196 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f7a65e1-e4a1-3581-903b-e3c4af1f98e6 | -5.40784 | -41.33155 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8be1f57e-fa06-333f-8c89-e7417f254416 | -5.99704 | -44.5752 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dd5b26c-77c0-3991-9b52-3740e815797a | -5.70543 | -42.66014 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e622b28f-2799-3978-aaa3-40376945fcdf | -5.13229 | -46.01744 | 2025-10-02 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c206b700-4654-352a-a928-b9bff868ec97 | -4.62616 | -49.36919 | 2025-10-02 04:27:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b393d87b-b861-3a38-ab7b-bc4efe38b151 | -5.26426 | -42.77469 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09ac0713-db0d-30c6-b9c9-ce56dda273fb | -5.24475 | -42.9776 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d401764f-ca29-3e4c-8d0f-5e7435e054b8 | -0.90385 | -47.54581 | 2025-10-02 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 990a9708-0098-3017-971a-ef2e045a9775 | -3.80835 | -52.15734 | 2025-10-02 04:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42181297-cc17-3f6a-b55c-12a1e102a2b4 | -5.24413 | -42.98172 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a14b9951-f39c-3b39-8d6d-b415137ff2f4 | -2.92456 | -48.3077 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 326d9f4d-985f-3dd4-9922-4f1f51be8dfd | -5.81817 | -42.8513 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 79393aa0-d09f-3a80-94c3-7c82d8859e99 | -5.82786 | -42.86149 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 84c55f68-2f8f-3acd-bf28-9115fd73e580 | -5.28445 | -42.76477 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fbf3be5-b2e2-311d-9c62-c4385eaf41be | -6.04624 | -42.43823 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 495157c8-ba49-3298-94cd-363e6693ba76 | -2.74257 | -48.67488 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9c74fed-79a7-320a-9167-e7be82a8eb2a | -2.96405 | -48.59629 | 2025-10-02 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fddb902-fa1e-305c-9cf6-9cd0c4adc3d7 | -5.59267 | -46.24977 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea4efb34-87cd-3d10-a128-acf3620df348 | -5.24836 | -42.97818 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cb37d974-2862-335b-94e9-19a1f413d868 | -4.60391 | -43.66024 | 2025-10-02 04:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00b2bd85-0667-3d42-859e-4599729bc7f1 | -2.92099 | -48.30713 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 565fa66b-ba91-30be-a268-428261ff800f | -5.97942 | -44.59882 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7c1605c4-9ca6-3d60-ad73-824baff481f4 | -5.48692 | -42.75386 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 90350596-66fe-3d80-9056-c5493839b70a | -4.89151 | -43.2885 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b647713a-4b0e-328c-a5b5-d93e90ab82db | -5.97317 | -44.59409 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61648fd0-cf57-325d-88d8-9bd2d63dac17 | -5.78962 | -45.75083 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8930587c-0beb-34fe-8a8c-4bd19fb33dd4 | -3.812 | -47.58075 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 471fe32d-4ee8-3572-a6e8-b2bf68ab8c51 | -3.09354 | -47.00837 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae519b1e-b6ce-33e3-ad29-c6ca6036bf70 | -5.24283 | -44.46894 | 2025-10-02 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4618ad7c-03cd-3384-b610-f50d127af84a | -5.89201 | -43.19926 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e5994d96-8e0a-3017-b582-eca0c607bb90 | -3.09693 | -47.00888 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d049fb72-70af-39b0-9b8e-fec7189752b2 | -5.98965 | -44.60037 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98442d70-2193-39c1-9f1a-43dd0bbb99e8 | -5.82721 | -42.86575 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8a375467-d690-33e8-a73e-5e0463c1dc6c | -5.99761 | -44.57152 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d6799ff-65a6-3b8c-8ffb-f17b29665b30 | -3.87037 | -42.51911 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d47fc9e3-7655-3ddd-81de-d97172fdba41 | -5.98396 | -44.59202 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68922513-6535-39f5-a334-99c462f52f83 | -4.40606 | -50.84452 | 2025-10-02 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65194730-4f4c-3382-9e1e-1be94469d2d2 | -3.80806 | -51.3178 | 2025-10-02 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb334f26-8584-39e2-80d7-01e8f58fc99c | -4.25789 | -48.55671 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f887e4b5-a652-371b-b261-e1dd567b196c | -6.11416 | -43.43369 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e948189f-a3d1-3652-b1dd-a80b5a27aca8 | -3.81827 | -47.58555 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faca6ef0-f72c-307f-b694-69171fac7122 | -5.2717 | -43.16222 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6752c05e-9aa4-3e7e-b6a0-f91ac01fa606 | -5.82656 | -42.87002 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| aa5935b3-f211-3fc2-80e9-ca779eb901f2 | -5.63812 | -45.96199 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c43a7fd3-c2bf-3409-93dc-24397fd6a5f3 | -5.98737 | -44.59254 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2b8c8fa-b333-3120-9c4a-dae134471e94 | -2.42596 | -47.14341 | 2025-10-02 04:27:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 48c32682-ae80-3ab6-afbd-ad507936c657 | -4.53563 | -38.03753 | 2025-10-02 04:27:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e7c0c9f-73d0-3074-bed0-c5e81748b46d | -4.95851 | -43.0433 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d41bf9f0-5d00-38b9-9701-243e7f8da109 | -6.1119 | -43.3889 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1698810-6436-3b55-b270-50ab7164e215 | -5.51132 | -45.15858 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1791a51-c1bd-384c-8dd8-420a897f0788 | -5.25309 | -42.89806 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 91cd765f-4481-3bb3-89fd-213fe8ff280c | -4.44561 | -43.23652 | 2025-10-02 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bb58ad7-38dc-3e40-b755-c3fbffc80376 | -5.35446 | -45.95979 | 2025-10-02 04:27:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be04aac2-072d-3204-bd6e-395b39db9d63 | -3.33695 | -50.09834 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeda6a2c-d9bf-3477-80d8-dc0892ce6320 | -3.51698 | -44.03588 | 2025-10-02 04:27:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5a27d3e-5cdc-39e0-b980-53c356425376 | -5.20597 | -43.67843 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5da8c62-eb99-30d6-879b-3dccda764192 | -2.92228 | -48.29912 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24cae61d-1d19-36d9-91da-eb3d9890a46b | -5.24099 | -43.09926 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2c64d0f-1b6d-3424-92ba-618305b751cd | -4.48076 | -47.67623 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 123fef03-573b-3bcd-b371-ba350fe0de92 | -5.81151 | -42.84579 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4ec5706e-21ea-3381-aaf7-c4aa632ceb27 | -4.26629 | -48.54988 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 250fff60-8cc2-361e-bbe5-b0b89072a891 | -5.33723 | -43.76461 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6386d6c6-7a2b-3e18-bdd6-0505001ca9c3 | -5.70537 | -42.83585 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c8e4d213-2117-35b5-ac31-48560a78095d | -3.69482 | -49.56936 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 10eee3ef-3808-3d02-b6a3-8559421659ef | -5.7924 | -45.75483 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1661321-6020-3ce6-81b4-e4a61ba6b2a4 | -2.63527 | -48.04047 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06654b80-e864-3902-82d6-6fc7d9925628 | -5.82438 | -42.4524 | 2025-10-02 04:27:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60c072ba-b5ff-3637-ae5a-6233cb70d451 | -5.23648 | -45.20293 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23dd4b6b-bf30-3904-b343-d6d8ef5a101c | -4.83247 | -43.50877 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 098ea240-2e6a-376d-92f2-26d214cd7b5c | -5.73864 | -45.51787 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20139a3d-fa98-3a36-a568-875d027211c9 | -4.8628 | -47.40731 | 2025-10-02 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dfad9a5-d90c-3775-8fee-837cdee310e7 | -5.99249 | -44.60454 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 002955c3-ffb4-376c-8573-3210f812b402 | -4.25369 | -48.56013 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b51be30-b296-3fec-8b8f-2f5ef528d08e | -6.04586 | -42.44073 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 07eac05a-5ed0-342a-97b9-51b4a4bc13d9 | -5.31919 | -43.76573 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 695692e5-b0f8-3471-9546-f7224b1afcc1 | -5.74008 | -45.42127 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2faa984b-bc79-3173-8de0-644e98cd9e49 | -3.46653 | -50.09113 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71d93724-30f0-3be6-8c4d-c6ce1fbb75a9 | -5.98624 | -44.59986 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96f63798-22fb-3e0c-a4d2-f578d10f9116 | -5.83152 | -42.86204 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e5575444-ef51-33ab-9c59-48696d94d0af | -3.49809 | -50.26897 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ac456b14-934b-3f7a-bdbc-3c8cffe269e4 | -5.37439 | -45.70348 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6706310-3d7f-3d0d-b13e-53c8321f856d | -3.87749 | -42.51845 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec68d69e-d540-37ba-9f31-5646c4409ebd | -5.41109 | -41.33703 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5890be5-d428-3f90-a3e0-d6538642450e | -5.45464 | -42.84435 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb436fd4-ccdb-3895-b63a-fd1f55dd4878 | -5.48564 | -42.76238 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 97788532-082c-32eb-b121-57e9bcf6765f | -5.6926 | -42.64472 | 2025-10-02 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9133a07c-2fa7-3712-a146-3ef7d7ce9617 | -5.69377 | -42.64693 | 2025-10-02 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
