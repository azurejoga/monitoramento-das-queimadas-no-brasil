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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6cee557-ba75-3861-989e-4365c7631323 | -9.57091 | -55.37434 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2bc0506-61de-3840-9be0-12c591229a06 | -8.12544 | -62.87714 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88d091cb-126c-3502-9212-b68878b4f33b | -12.28702 | -49.13291 | 2025-08-25 04:42:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 378e2f99-ec06-3a89-b34c-2e04d88ab1ba | -8.80921 | -45.46111 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 528c2224-8d1e-3a6b-830e-27b49cb9e71f | -10.61628 | -55.05265 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 75fc819a-c520-397c-a27c-60267100c942 | -9.22436 | -59.67318 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e086d509-2c75-3d7f-b962-6ab16654d989 | -9.16228 | -60.82307 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b06533b-1d62-3019-8455-00110ff87c79 | -6.83433 | -58.94704 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 365d6581-1f2e-33e1-a209-b902aaaa2878 | -11.26468 | -44.98371 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a71de53d-8a90-3208-b5c3-4969fba8a94e | -11.18043 | -55.03753 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d49659-788c-31c3-a3a1-19530bf974dd | -11.5994 | -46.33014 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63909793-5676-39a9-8604-6156674b5956 | -12.74941 | -48.12978 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee49de3-e4ad-30ca-8faf-1e069c27e5c0 | -9.20573 | -59.49573 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 918203ce-a1ed-39ca-ad0b-9f467a6af928 | -7.84859 | -50.00037 | 2025-08-25 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d50ac43-1b95-3e91-915e-bfd57b7e36eb | -11.45669 | -55.471 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 91aefe7c-fed7-38e0-8836-03ea83b5a57c | -8.06392 | -49.68447 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4e0f7fe5-2d4d-303b-96a1-be94eded6ecb | -10.76838 | -47.07771 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23b8f262-6788-3ad4-b35d-edd16b9ec684 | -13.43107 | -47.0242 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f97af5a-c813-381c-b7f5-6ccf85ed7f72 | -9.19871 | -59.4724 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1585d284-a70d-3ef7-bc65-3f3961f8a0d8 | -10.7295 | -47.11522 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c85f09c1-795c-395b-991c-e2039e59e7df | -8.88426 | -62.45312 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a9a3d223-feab-3f41-ba6d-21c866d5f419 | -9.20443 | -59.47712 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15de5f1-d77f-352d-bab5-3a97620b4622 | -13.40709 | -51.7864 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d87e28b9-d454-3a77-bb3a-ad86fa48633c | -11.67218 | -51.58422 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0e023d8-1662-3823-8aef-fb7bf6ced236 | -8.8772 | -62.42928 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb2999b-1b84-38bd-a3c4-e99b3e6b8cfc | -6.79864 | -58.64372 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e84bd9e-be55-38a8-9811-5dc1a311eef0 | -9.19712 | -59.45023 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e941493-ccf5-34e2-9c05-efdde5bbc666 | -9.19406 | -59.62217 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db4112e-7b66-3aaf-9aab-79fd459f22e6 | -9.16287 | -59.48379 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57838bd6-b70c-3f2f-89a5-8d8bd558cd4e | -11.60687 | -46.36026 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 45e8eadb-aabd-3ba9-8cae-f2635a2337df | -6.3598 | -57.9691 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f98ec26e-cf6d-3906-ac6c-1b0ff304111f | -9.19647 | -59.51577 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5d36337-973a-3074-a385-e0b0cd33997e | -11.19858 | -55.04336 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3797dc7-b4de-3d45-848f-f7a896db0d00 | -11.47211 | -55.47739 | 2025-08-25 04:42:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c71020e-cd3c-3cb9-bd76-eda450544f55 | -12.1855 | -47.20208 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10efcc2e-25fb-34c0-9d25-4ed60fe12128 | -12.02713 | -49.70989 | 2025-08-25 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa14d351-d416-33c9-94e1-cdac443651f1 | -11.62434 | -46.23634 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c9997d-55f7-34a6-8454-2ccda1f5575b | -10.10712 | -57.76663 | 2025-08-25 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4403ca6-22a0-3023-8cf5-7a71facd1043 | -11.19547 | -48.46681 | 2025-08-25 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8aec4a3e-aec3-3408-896b-9e41cb3343e4 | -8.87292 | -62.45194 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 48ef94d3-fb9d-3f36-b80a-396b5b5ad9c3 | -6.82885 | -58.94609 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e94f35f-00c1-319b-a0bc-4e440b56238d | -8.54138 | -48.85845 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f6273f7-1156-3c2d-a32b-86671db13de9 | -6.82081 | -58.95921 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 868b5daa-de99-3611-b374-3b933c504b2c | -9.79979 | -61.20857 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb358acb-d9b1-3c96-9dab-660898d645ee | -8.50374 | -63.87763 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8c9f43b-e846-35ce-a3b6-6b5cffa1fac5 | -9.16739 | -60.82847 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5f6768f-5c8b-343e-82bd-fecfbfadf7a2 | -12.48985 | -53.8295 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bde2b61-dd68-3c52-afde-495a40bcf1f8 | -13.40361 | -51.80796 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ae8e81-07ee-35fb-bb8e-f1987c16393a | -8.91163 | -62.41753 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6baeeb7c-e7e2-31b1-a594-6a6ed4c392a6 | -9.1713 | -60.82389 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69f7f0f1-cf6f-3b01-9051-5d42afef727e | -10.10141 | -57.77088 | 2025-08-25 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143cea34-5b3b-3091-9e11-6d9339a49aa5 | -10.71204 | -48.32584 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26b4de67-1560-3267-9342-02230c2820b9 | -9.17219 | -59.46367 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 151ed029-3fe0-3044-bb77-11c0973655b4 | -10.02574 | -51.06956 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10ad852b-e4b1-3ebf-a6eb-a411d2f7f990 | -6.83177 | -58.96109 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 91566bbc-5c08-38cb-939e-b81207163129 | -9.24533 | -59.6213 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8da1dd86-d697-353b-858e-b0ef905189f4 | -8.0617 | -49.67698 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e59f712b-9303-32fe-82c5-c36db304075f | -9.18435 | -59.45864 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5d90b46-0b2c-3164-94fc-fcda8c6ac918 | -10.77533 | -46.39621 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bdfde33b-5811-3b42-b9e2-f087fbf917e0 | -10.59918 | -44.32864 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e70f9427-2b66-3514-a828-d3a2fc5ff919 | -8.90739 | -47.33209 | 2025-08-25 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4d63943-371d-39d8-86fa-5248cf9b0b11 | -9.96466 | -60.18765 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5240268e-15a3-332a-b8f4-47dbe67f134c | -6.82758 | -58.95307 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22caf607-443f-36d0-8351-fbb5adfa1ce2 | -9.15809 | -62.35278 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dba7247c-6c53-32b5-bd70-1e249bd4cdb0 | -9.26512 | -59.78385 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8b89d62-4875-3fc7-bfc3-39039bb2f489 | -8.31833 | -47.25229 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a06b15-8a1b-370a-b816-799040288518 | -10.71678 | -47.12632 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e15fd333-f596-3fdc-83af-1076aaccf0e4 | -13.44766 | -46.88146 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86a09dd9-af0f-37d4-b610-f45e5dce1cce | -9.16353 | -59.48021 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ce38064-cc2b-38c9-a5d8-ad694f781095 | -13.15683 | -53.73322 | 2025-08-25 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 151464e7-39a2-328b-8df3-69422974b1e1 | -9.712 | -54.98958 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58fbbc9e-7c25-34bc-8540-516036fdfc3f | -10.61322 | -55.0467 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67a64f2d-8ca8-338a-9a98-00bdd41888e9 | -9.52415 | -60.52738 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d38c3f5b-b0f3-3511-bf2e-0ee7294b7191 | -8.68691 | -62.87819 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| faf6b573-121c-3b81-9c96-831ef8d77a86 | -13.45146 | -46.88201 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 524fbdca-a719-3f6b-bde6-13f9cfb93ce6 | -6.81576 | -59.43329 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4adb2cf8-7a37-362e-bf54-237102bc9b66 | -13.4432 | -46.88552 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffc81e8f-8eb3-3796-8d69-78e8f383c737 | -9.50343 | -56.10427 | 2025-08-25 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c340679a-5a20-3dbb-973f-092291be884f | -9.17307 | -60.76721 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77270ace-2758-3d24-9ac0-085af26f2818 | -6.91175 | -63.00044 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efdbcd9b-007a-3426-be9e-f625490170cf | -12.93981 | -46.31271 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbc09aba-190e-387e-86a6-67c2c0270fad | -13.50797 | -46.91618 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f0655dc-ffe0-372a-bf8c-0b17d7971040 | -8.05892 | -49.67665 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 733fd47d-8550-3017-97b8-f4589074c5a7 | -9.19808 | -60.9257 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f841639-5479-3c70-a0a9-4a000ec7a4d0 | -10.60237 | -44.33734 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16a3dd16-cb42-3627-945d-4da801b28d5e | -11.69862 | -60.1886 | 2025-08-25 04:42:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c6e3099-6be5-3a04-aeba-9cc58bac39a2 | -8.68565 | -62.87953 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73c5d527-bf5a-3279-b44b-0f18a1eef02b | -8.13525 | -62.86692 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3b5ed46-e10a-389a-8587-d5648ff40bce | -7.62293 | -62.72259 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 749f1839-129a-3b0a-9e03-dc97a05d370b | -10.71085 | -48.31039 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98c45c23-ffdb-33de-bf66-414dbe40c654 | -10.82261 | -48.33105 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c14189ba-05a7-387f-ba9b-5b23788fef4c | -12.95661 | -46.33465 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed77c02-1b66-3f45-b790-836c34633da7 | -10.72101 | -47.1227 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3aba185-48c1-3636-9144-8af20d51ddd1 | -10.73012 | -47.11093 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd3101e6-5d33-328c-8ebe-2f8b1f6317f5 | -8.06002 | -49.66969 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 678132da-672d-3324-96dc-40c9dd83b181 | -8.87077 | -62.46329 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 3f511346-149b-32c1-9b2b-67198757613f | -10.62512 | -51.61733 | 2025-08-25 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a6ad0dc-2aa4-3383-8684-7c9a574a1bc1 | -13.65868 | -47.98469 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c3fcf65-8602-3fa1-be2d-c44f61b5e69e | -9.18925 | -59.61754 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1186dfd-d3dd-305d-8783-37c1786c9256 | -9.10079 | -61.4361 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README47.md)
