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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3365998-9286-306c-9e00-644da14861e3 | -19.05721 | -53.45488 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd1a6c56-20ee-3da4-b90b-80881fdabcef | -22.67785 | -42.85196 | 2025-05-22 04:25:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f0eb4bbe-40f6-3fb4-93af-b5c60ddea293 | -20.60559 | -48.87037 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 191ee688-a8e6-35bb-b32d-1a0ad9d7f1e4 | -22.5399 | -48.81221 | 2025-05-22 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b96a5c-6d7c-36e1-aefd-8887535573ad | -19.0606 | -53.45977 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 028d8962-3427-3413-8a7b-1ab84bf879ab | -20.61016 | -48.86349 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| c1c74cb1-373d-3464-a068-e307f75a7b59 | -23.29495 | -51.58953 | 2025-05-22 04:25:00 | NPP-375D | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d1d4fc0-f5f0-347b-9370-39427882ec28 | -19.50825 | -48.66419 | 2025-05-22 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f58849e1-2cb9-302f-939f-33a17c259c8c | -18.91424 | -54.48084 | 2025-05-22 04:25:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ad59d7b-7211-3126-8066-ba00304084f0 | -22.78572 | -43.75715 | 2025-05-22 04:25:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 949d28b4-cf6e-3330-8d25-ec65796667c2 | -19.06474 | -53.46066 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8d45ce1-0002-3bdd-8c9f-33caf116b1dd | -20.95909 | -48.63072 | 2025-05-22 04:25:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8560e4cf-b01b-3d84-beee-69d780f87f8e | -19.11718 | -52.69036 | 2025-05-22 04:25:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32e83f82-f0bd-3bb0-80a6-f80e3095364d | -21.46767 | -47.1345 | 2025-05-22 04:25:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc141ee4-1cd1-346c-ac08-d273d8cce767 | -21.29589 | -45.13484 | 2025-05-22 04:25:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9b9d8c0-e45f-3175-8c13-ade1343003ae | -19.73337 | -54.50968 | 2025-05-22 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00c71545-8cdb-3ab8-8657-06072b0e9acd | -20.94631 | -56.5911 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 38.6 |
| ccfb368f-c693-342a-b4c1-9814433123d4 | -19.11616 | -52.69577 | 2025-05-22 04:25:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11c5a100-e05e-3d82-9954-3caed638474c | -21.25161 | -50.30713 | 2025-05-22 04:25:00 | NPP-375D | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34752cb7-45b6-386e-8c88-410e63ed2d14 | -20.60955 | -48.86723 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 5c915ca6-c2aa-35dc-9748-51c8880495e5 | -22.16326 | -42.94517 | 2025-05-22 04:25:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d91b66c5-78b2-3301-97bb-1cd8d312a63f | -20.83494 | -43.21789 | 2025-05-22 04:25:00 | NPP-375D | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9fa8c31-6ea7-3bad-96be-d4b53a42d05f | -23.98487 | -48.9177 | 2025-05-22 04:25:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 779ed6f5-8ea5-386e-b145-aab9f1eac297 | -19.975 | -47.18819 | 2025-05-22 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83ae3ebd-fb07-344a-a25f-70ff89b97bfb | -20.94774 | -56.59279 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 9c3697bf-2cdf-36dc-9e13-c9766532d704 | -19.05646 | -53.4589 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70c49bc3-e786-350c-8a60-15fa32c63d2b | -20.83715 | -43.21948 | 2025-05-22 04:25:00 | NPP-375D | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1bdb58f9-a047-3fd6-b893-8e2ccafb256a | -22.94967 | -49.1067 | 2025-05-22 04:25:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2e01a3e2-9057-30c2-8291-d674e7ff7035 | -20.05205 | -45.42546 | 2025-05-22 04:25:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 049bdfc3-8202-3261-8a80-589c6b3611f8 | -20.94361 | -48.51324 | 2025-05-22 04:25:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63c810f6-8d2d-3324-a558-8b0604dd4719 | -21.36377 | -48.76396 | 2025-05-22 04:25:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27e18181-5b4c-3f9e-ad24-65490cda8c56 | -23.29142 | -51.58881 | 2025-05-22 04:25:00 | NPP-375D | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0e005a7-f349-3fa5-8cd0-144b207dfdb0 | -22.16372 | -42.94133 | 2025-05-22 04:25:00 | NPP-375D | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e20cd461-8a76-369e-8760-2a9815b958e9 | -20.6062 | -48.86662 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| c651510d-0e5f-398b-9a1f-ff1cac453850 | -19.73773 | -54.5107 | 2025-05-22 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af0064ef-a977-358f-bbcd-49e58b193653 | -20.95232 | -56.58669 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 646dc1c9-d862-35b0-b1c2-d82191856747 | -19.97443 | -47.1919 | 2025-05-22 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 238a494d-d8bb-3ae9-a5fb-32325a7733d7 | -19.11959 | -52.68941 | 2025-05-22 04:25:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bce19949-a3b1-3b4c-b28f-915b743bb947 | -23.54787 | -47.63621 | 2025-05-22 04:25:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ee5b7d6-bff9-3e1c-a827-d478433999bc | -21.48235 | -57.1221 | 2025-05-22 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3ac15e-b9bb-39a1-a49e-3b88b7410dc6 | -19.11464 | -52.69407 | 2025-05-22 04:25:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ed51478-fed0-33cf-b363-3d127ec6cdf4 | -21.21979 | -48.61183 | 2025-05-22 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5480cf24-8760-3007-89b4-51f6924f6683 | -20.60894 | -48.87097 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4674814-52aa-3c08-bbee-d4275091953d | -21.48364 | -57.11592 | 2025-05-22 04:25:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc744d9d-2e3b-3bd3-a9b1-086b1b1e3c30 | -19.06136 | -53.45572 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c108dc2-9d0b-3acc-91c1-813d6d59230a | -22.95301 | -49.10732 | 2025-05-22 04:25:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 520597e3-b213-3fb0-9a8c-c3a310733b2f | -20.95115 | -56.5924 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c5be0d7e-4d9f-30ed-a1a3-04521e07d55c | -20.60681 | -48.86288 | 2025-05-22 04:25:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 24b7b87a-d752-3e6e-bd6f-32570d7a0d22 | -22.67735 | -42.85596 | 2025-05-22 04:25:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 72048828-415f-33cf-90ba-4f8621e06b6d | -20.9475 | -56.58533 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 38.6 |
| fc8e1742-094e-350b-8178-de67fc653094 | -23.33844 | -46.77094 | 2025-05-22 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d9409ca-fd1d-3b34-bd34-face7546dadf | -21.47104 | -47.13507 | 2025-05-22 04:25:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7aa180d8-ea86-3b09-baea-628a20369f9a | -20.94897 | -56.58706 | 2025-05-22 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 9aa7f277-1bc1-3fe7-b188-6fad04138b4c | -20.32783 | -54.2402 | 2025-05-22 04:25:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6de481b4-2751-3193-8295-51f791ea5a14 | -24.24314 | -50.74081 | 2025-05-22 04:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e924e92-826c-3413-a571-dfdcb48dec23 | -21.53211 | -49.53042 | 2025-05-22 04:25:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 58efeba2-31b5-370d-8122-1e955d657283 | -19.05306 | -53.45405 | 2025-05-22 04:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d86f209-ae9a-3697-8110-affcd0d62869 | -23.63461 | -46.28713 | 2025-05-22 04:25:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dd3600dd-2aa1-3c30-8689-0da8fec9da42 | -20.57928 | -44.57449 | 2025-05-22 04:25:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4cc3985b-0dfc-3631-950c-fd407816a4b9 | -19.50764 | -48.6679 | 2025-05-22 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0867d30-85c9-3ed7-bc4e-4b5a6ec220af | -23.31157 | -49.29293 | 2025-05-22 04:25:00 | NPP-375D | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0fa68369-0d16-3091-a334-095d9b876f5c | -21.67031 | -43.44094 | 2025-05-22 04:25:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c2cd1785-d3ae-3beb-b441-a42b9f2c970a | -19.73248 | -54.51428 | 2025-05-22 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23a53ff5-c6e6-3974-be01-b29524e72e6d | -30.15159 | -52.02491 | 2025-05-22 04:27:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| a9dba1a8-3192-34ee-acd2-fc58888c8de6 | -29.77764 | -51.17731 | 2025-05-22 04:27:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 989c24a7-5543-3c06-9c97-9421ad09fc9f | -30.66993 | -52.80161 | 2025-05-22 04:27:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| acc86c5a-af23-3f22-937b-45f8cc34f43b | -11.5719 | -47.4521 | 2025-05-22 04:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 255cb28d-6d54-3a70-8cf0-6ad47ed4f590 | -11.5528 | -47.4546 | 2025-05-22 04:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7ad381ba-f067-308e-9e1a-1d704877206a | -11.5528 | -47.4546 | 2025-05-22 04:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 60fa2ed9-891a-35f2-897d-0a9e3f508cf3 | -11.5719 | -47.4521 | 2025-05-22 04:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3c5e37d5-90d5-31ef-9463-5d54ff01636a | -12.0799 | -47.34308 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c12df208-5c61-385c-b310-f01697425663 | -7.80285 | -46.21976 | 2025-05-22 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b26e852-8dc0-35f7-bbdc-414ae971fea1 | -11.64596 | -48.10108 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 55c5527c-a66b-38c4-bc3a-b8e1ac3e0d3a | -7.31047 | -55.30823 | 2025-05-22 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbdc3c51-b637-3c49-bd07-db12f88e55ba | -9.85986 | -60.31794 | 2025-05-22 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bc49590-b732-3540-8274-1a6a47d5e077 | -10.36671 | -47.97718 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15ca28de-8f70-31dd-9fc0-19e84a1eff75 | -10.29518 | -57.14188 | 2025-05-22 04:44:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ff15c1-a838-3b1e-86c7-cb280d4ba183 | -11.59953 | -47.62336 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ae2b82e-fffe-346d-bed8-336a3059b268 | -11.60809 | -47.61935 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff679d1a-1fd3-3d68-b2e6-7ccb0d37cf82 | -10.3702 | -47.97496 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a34a7559-9352-3e3d-a37b-5b22d161c99d | -6.63429 | -55.01055 | 2025-05-22 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47af7f1d-6f79-39ed-ba6a-7b010e70d4bc | -10.37488 | -47.97374 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50cce57d-b806-3f29-8f11-5134a3d82eca | -10.36644 | -47.97439 | 2025-05-22 04:44:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 10b4a088-0f79-39d4-aa23-e7e0a8ae6f00 | -10.96029 | -49.41243 | 2025-05-22 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a10c454-6456-3682-99fb-3d06f62c2461 | -11.64527 | -48.10361 | 2025-05-22 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f9526a6c-16d0-313f-a1d3-d2a16f865819 | -11.59635 | -47.61778 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73f7ce4f-7d02-3af9-8c5c-ac12ff1a3ff4 | -9.72415 | -48.32586 | 2025-05-22 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5edd4b7b-4455-3f5d-a13b-5feb7c95c438 | -11.60344 | -47.62392 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c06f13c9-3aad-303e-95a5-23785a73c8ea | -10.62065 | -51.79149 | 2025-05-22 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2afd8fe-9bc7-30c8-9d83-a4f5e262f991 | -7.96598 | -49.69205 | 2025-05-22 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c4e8232-e059-39ce-b4f8-e90f2e29edf3 | -11.5637 | -47.45303 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 585edfd4-df5e-3651-addc-fcf27facf4c4 | -11.55653 | -47.44675 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 39bee4c3-8321-37eb-88fd-45fe4cb765b9 | -10.37844 | -57.64237 | 2025-05-22 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff123cad-cd08-3b4e-868d-4be5663cfa91 | -11.51486 | -48.55641 | 2025-05-22 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34bf7cb3-319b-3a95-96b3-6a468c96158b | -11.57086 | -47.45939 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ba21c5d5-6c6e-32eb-8ffa-cf71d427767e | -11.57232 | -47.44897 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03584b10-014c-3d6a-a981-736b5d7d91db | -11.58463 | -47.61615 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 895e9823-d47a-3580-b568-8d62f0395ce2 | -10.07922 | -55.49058 | 2025-05-22 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b36071-bbd9-37e7-895a-c4dce854749c | -9.79634 | -48.2639 | 2025-05-22 04:44:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4db83a6-5931-33a3-a111-2622ee7fb07c | -11.60026 | -47.6183 | 2025-05-22 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
