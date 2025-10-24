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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a14bdd5-ad0b-3422-9363-0028af829ea9 | -15.60983 | -45.91721 | 2025-10-24 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 451f3750-215f-3c35-b287-f5faabbaac97 | -19.98865 | -44.22995 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 658b9414-e22f-3ff6-82e4-26c5f6c66122 | -17.07383 | -45.69048 | 2025-10-24 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b17e839-8c62-3535-9f43-e283de3369f8 | -6.10084 | -48.20068 | 2025-10-24 04:19:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e29f0de-ad1b-3aeb-9398-2311861bb718 | -6.76588 | -45.48573 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fb4537a-934a-3833-a625-7def3663db25 | -14.76853 | -49.29575 | 2025-10-24 04:19:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5e05b25b-7fae-34d1-9f02-ac77c6ed3abb | -17.46647 | -48.40097 | 2025-10-24 04:19:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78905601-838f-3fc9-8e54-32b59255c079 | -15.59656 | -48.04634 | 2025-10-24 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8176f14c-a20a-3ce9-9060-a709ba55632a | -8.19322 | -44.43358 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18b7bace-8d19-30ad-af38-f12910ebb246 | -12.73028 | -46.95689 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff05ffd1-a365-3bdc-9a26-bc71ba91c255 | -6.81192 | -45.46584 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e610702f-e625-3f1f-81e0-3e0570b14941 | -12.77185 | -47.37901 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cfe76332-e1c0-3563-ad0d-09de141644ad | -7.3003 | -46.95076 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce8aa96-65d9-3ee1-aa14-9efa22cb6132 | -12.76967 | -47.37026 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee08063a-178a-3ec8-b21f-9ca787532517 | -11.48558 | -54.01965 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74304257-531e-3072-85fd-f16d4a3f347c | -6.77121 | -45.4749 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 892429a2-d1e5-3c60-8361-e5b6c266ff7f | -6.93316 | -44.88781 | 2025-10-24 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 631d1516-9cd3-3301-ac10-6cf9cf4687dc | -6.76872 | -45.49014 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c49e45-eba5-384d-b143-affbe67ce88f | -12.83024 | -47.24716 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfb70d73-f72c-3910-87d0-0e80b4c29124 | -8.09012 | -46.91874 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f53ec8-3cf2-342a-8077-17cc0e618afb | -17.09612 | -46.18844 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aed540fd-8c8a-36cd-ab8d-b35f99923475 | -8.46917 | -45.5612 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf390cf1-f6fc-3cf0-b162-f6adf4a6ed9a | -17.65788 | -46.6489 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f04ca916-cd3e-36fc-b3b7-53344e031318 | -8.74057 | -45.83413 | 2025-10-24 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b00b634-9188-358c-ab51-69266480c670 | -6.10843 | -48.10666 | 2025-10-24 04:19:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 996d64da-09a2-3e23-b7ff-7681b92081a6 | -6.81255 | -45.46198 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28fb5a13-640c-3f4e-a817-aed87fe98f48 | -13.88612 | -48.36521 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e1daf4c-d56c-3190-ac26-019a168e31e4 | -7.29586 | -46.95459 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51f20ea4-5bfb-357e-9298-9ede43fa3414 | -14.20634 | -48.35 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d68d740d-16fd-33ef-9423-9cde31dbdd30 | -14.44097 | -50.94385 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ccce4ae-8a0b-3833-9da3-36e9ee8afdcd | -7.38316 | -46.54125 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14437212-8abc-3f32-bf7d-1c17b24f952d | -7.62933 | -42.19015 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0398a4c0-b406-35d7-9413-82af4984d557 | -12.36753 | -51.47757 | 2025-10-24 04:19:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed8db739-2b7b-37d5-a4e3-383e319f99f0 | -14.92299 | -43.4492 | 2025-10-24 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0cdbd91-f52b-3b5d-959d-a5b17efef03d | -13.2881 | -47.48807 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a00e83-34f0-3854-8fcf-3288f186953f | -20.20294 | -41.71516 | 2025-10-24 04:19:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b48a401-d65f-3b18-9689-43c5d0dc1dc5 | -11.32668 | -54.2599 | 2025-10-24 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9471990c-6f87-3745-96f5-59a98733abe3 | -18.20235 | -47.64971 | 2025-10-24 04:19:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d471fec-4f18-36f2-b7ba-89a564d21801 | -7.45646 | -49.40705 | 2025-10-24 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18db766a-be2c-3622-9311-1de467bfb000 | -12.53737 | -49.61051 | 2025-10-24 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a606dcf-b96e-3057-a023-0f225e1cfb1f | -17.59087 | -46.62608 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 274c5d9b-fdb9-3b5f-9e8d-5d375eb17e08 | -17.24099 | -44.11277 | 2025-10-24 04:19:00 | NPP-375D | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8601dfcb-27fe-3c67-b5e1-591ddb48cf82 | -7.14102 | -45.04871 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fddc8791-fbec-34af-a178-f876c2236e6c | -6.85188 | -46.92906 | 2025-10-24 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78a0a769-ee88-38f8-97fe-a6c0434a4d98 | -6.79606 | -45.43184 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa9ab415-d4ab-39ed-a51a-1e9acaf4518b | -7.61891 | -41.85174 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3bba06ca-ac52-3a7f-a656-1d8fcf365cd7 | -17.59421 | -46.62666 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c61063-4731-3b88-a099-a004db794722 | -7.82871 | -45.37838 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bddfe41-7757-32ac-989f-96151c91b885 | -17.6009 | -46.62784 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c862b6f2-ef39-3f3d-af3b-7ef495ede529 | -8.32149 | -46.78397 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 255c4a26-67c6-30ef-b2e4-1a4ee3dba8ac | -13.28226 | -47.47946 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b00f7b76-77c1-37c8-9f2e-461e0f4914c4 | -14.74283 | -46.60443 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 691b1652-eb59-3a9f-b93a-df8618309899 | -12.92393 | -48.50816 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a4a7157-b695-356a-aa2c-94ae1690e070 | -19.77393 | -46.19478 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37d4c788-ae58-30bf-b63b-fe25e80ff6cb | -7.62822 | -42.19732 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e94a2cfc-4e2f-36a9-8c46-f90710f3dc76 | -8.34832 | -46.18202 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3cfb991-f6f3-3e23-a3fd-b86866b37294 | -14.69607 | -52.82822 | 2025-10-24 04:19:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd0b6a28-31d1-3ae3-88f2-628a884cfbdb | -8.2731 | -47.79416 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71a6464a-a7de-3055-a479-9c9a3f17f958 | -17.59756 | -46.62725 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2ed5569-9409-34ad-b247-630e8e10efcc | -8.11057 | -47.04715 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd78ff6d-1b2f-3198-96c7-7a6449e53e6d | -7.40236 | -46.96632 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 584e132b-0c75-3d95-912c-a605e9d608de | -8.0915 | -46.9104 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96ccb37b-be3a-3bb5-a9a9-d0e76df8a087 | -8.64664 | -44.791 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf38b293-968e-3517-be46-46265e054f69 | -6.9503 | -44.01416 | 2025-10-24 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf9ffaa1-6657-3e28-a7c1-5179face189b | -13.64442 | -44.44377 | 2025-10-24 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b3c217f-1ccf-3938-b991-7fbe9bfe87b6 | -15.83655 | -49.10627 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee4e416d-2406-3031-b1b2-0c03a50f592a | -12.9562 | -48.49971 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b2a0d0e-c6a2-31ec-8a09-4614b001416e | -20.36304 | -45.79922 | 2025-10-24 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eaed903-1ee2-3148-be24-a525b0ceb64e | -6.79086 | -46.4673 | 2025-10-24 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fe5ff8c-40ae-37e5-88d3-ab58021596b7 | -12.77608 | -47.37556 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82c56215-3c45-305f-a390-3bd9122aad4a | -8.19657 | -44.43412 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12444f6c-c5f0-353f-bac2-f800025a96f3 | -13.89131 | -48.35703 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfac3fad-0e75-3527-ba12-3e7699783eb4 | -14.20547 | -44.59694 | 2025-10-24 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdff608b-a106-32b4-8298-a890b3f8e96f | -14.76647 | -49.29317 | 2025-10-24 04:19:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 296a4574-7b9b-3e28-a79e-21292a571976 | -14.46984 | -47.90818 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64289ece-6b11-36da-80b1-8987de1271e3 | -12.73093 | -46.95304 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5a5ca4d-42d2-392b-9b9e-fc0a8e6c9473 | -13.3348 | -47.96241 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aaa1110-b925-3144-be85-e33479000091 | -6.02416 | -48.91009 | 2025-10-24 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91c31333-d026-35ae-975f-4ef5449a29b6 | -6.77158 | -45.49451 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 642548c9-1be7-3c4b-9bd5-e2087983c966 | -14.27033 | -48.06507 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ac7e1f5-5654-37a0-8cd8-c60fa28a1031 | -16.95311 | -53.22676 | 2025-10-24 04:19:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 729e6247-96f5-3d1f-9158-2c5d71e295ac | -15.31455 | -47.85737 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 993dec31-c61e-363d-9e0d-b5c050f24667 | -8.34962 | -46.17397 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8730f6ca-0430-3710-97d2-642e1237bf71 | -18.35049 | -51.69211 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dd04893-70df-3e95-a959-655cfd6ad695 | -11.55276 | -54.51759 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91eda732-ee47-329e-99cb-fe344e692f6d | -20.21113 | -45.80388 | 2025-10-24 04:19:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4fe9cd46-c8c6-3149-84e2-08621d1208bd | -13.0366 | -48.70732 | 2025-10-24 04:19:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12126ee3-7221-35f1-b0b1-b11de957b727 | -13.90084 | -48.38949 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acfd1d2d-5169-3d99-8b1b-5ae5012ac7d5 | -15.21082 | -47.95802 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73753a6b-32c8-3bca-bd7d-06b94c62c6c7 | -5.97744 | -48.9267 | 2025-10-24 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeb8e32c-0b3e-3df1-971d-2638377a6607 | -18.46916 | -44.44983 | 2025-10-24 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e103350-ee20-3c4b-a0fb-7c7bf84591fa | -13.48384 | -48.00868 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ff6688b-024d-3b53-b92e-5d57100a111d | -7.43905 | -46.88252 | 2025-10-24 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 287e3d63-a8cb-3c83-ac28-0fe9305e4ebf | -8.32874 | -46.78523 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce94ae89-d22f-3517-8c88-fbe3ba9a9561 | -12.8152 | -50.95593 | 2025-10-24 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5ff255b-b88d-385b-af9b-e1efdc1fedf3 | -13.72872 | -48.37196 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4618e85-dcd9-3c01-a33c-23b209da690d | -11.48696 | -54.01244 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 430182f1-4901-35f4-beae-06975f80346c | -18.46577 | -44.44927 | 2025-10-24 04:19:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c57a27b5-4aa1-3144-8238-1c7061ace4bd | -14.76468 | -46.62008 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0a9b56c-591c-3300-8578-9bb78adb3911 | -7.78202 | -45.40544 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
