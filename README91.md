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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d0c512-f390-34f3-89f5-f60cceb80da9 | -13.33758 | -46.83852 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71aae283-ba27-3612-953f-ae22e2f13978 | -11.12181 | -45.11083 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f970482-1f33-301a-8d80-b8de4092fbd9 | -14.57166 | -53.00336 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b89f1dcf-f3a1-3c82-b75d-02c2d5544230 | -12.8697 | -48.03093 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ac15852-8c03-3a6f-a70a-1a97e7046483 | -12.93956 | -56.95124 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f50bfb0f-d8f7-3931-b97c-cb7cd8a1f02d | -14.56794 | -48.05981 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98604459-7357-333f-a294-24de20360604 | -12.93785 | -56.96257 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe611490-4545-3f09-bfb1-df19687c6941 | -12.93899 | -56.95503 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6b765250-5187-3d8a-8d5d-04a7ceb3b7b3 | -8.05458 | -52.36606 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a3c8782-9c69-318a-9732-3923fb5ff305 | -13.00161 | -48.0933 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd0c26c-70b7-3304-adb5-0d3fc28e807e | -11.66859 | -57.35386 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 965c67ec-9e5a-3f84-8b7e-96120f85239d | -11.6012 | -52.12569 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e466a9d3-8a0c-3ffd-a29d-a99caa46c2d5 | -14.78648 | -48.15693 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aad1408d-e459-31cb-adde-ca206cd3973c | -11.31317 | -55.22379 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47cb7913-fb7e-39cc-9350-7cbe0a03339c | -9.63942 | -47.86453 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0de1aea8-ee5c-3262-8e00-6b368d440f87 | -10.54548 | -50.44161 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a8d1cb6-3ae7-3da7-96cc-6327517843c2 | -10.95322 | -50.76931 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b13e6fca-975a-3a62-ba65-e6c6b9e5175d | -9.62445 | -47.06916 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6328a956-7cef-3716-b759-06847fbadf0a | -11.60273 | -52.08143 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8b1db56-66d3-3557-b452-4d1ee0be633b | -10.14874 | -46.27877 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f4869b4-e880-3fd5-997c-46f93af200a1 | -12.6351 | -57.00518 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 644d5f70-4b26-335e-8701-b28c3642c1bf | -11.61779 | -52.07026 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9682a6c-77f3-33e8-9dca-c52f7fb132ca | -14.54892 | -51.9399 | 2025-09-03 05:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be2ef763-c615-399c-bd0c-9ca04d2784d8 | -10.44885 | -53.62246 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 945ff2b1-2a8f-3829-b46e-446245f54b08 | -11.60357 | -52.10835 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5518d519-64e0-3d17-b3e4-ace492b1399b | -15.09981 | -48.12578 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3237f142-ac4e-39fa-997d-9f5210d7eb22 | -10.43916 | -54.76968 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51fcec53-ca6c-37d5-80b9-f9ca83ee506b | -11.01956 | -51.47352 | 2025-09-03 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10de3f4e-aa22-3ade-99f9-bbfcde672d8b | -8.85783 | -47.9289 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2accde2d-b3c0-362f-9a6e-47ef2a9b5d78 | -13.73225 | -46.93813 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fd7540f-128b-361a-a959-c9b85599fe07 | -9.33066 | -55.22084 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c646d1d1-36da-36e0-9419-d7823d5ac57a | -8.14236 | -54.93301 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96ccea93-5208-330d-8ff7-f01a55c5bcac | -13.44436 | -58.07254 | 2025-09-03 05:14:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a233870-98a3-3686-be40-07a336f289c7 | -14.56636 | -48.06314 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65124d32-4d33-32da-8d5d-31ca4107833d | -11.86063 | -51.47549 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6c5c8bd-ff6c-3f05-8b45-ecdc9fdc6e3b | -11.85363 | -51.42035 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69a50eba-337c-3b28-8291-74a904ca7ef8 | -8.08237 | -47.60295 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b266c5bb-cedb-3ca6-a04c-de7278d03e47 | -13.46312 | -46.93257 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 403183e6-7fd4-3f5f-af06-3d3030ea68f1 | -7.09237 | -63.07087 | 2025-09-03 05:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 325946c4-302f-3ff2-8f6c-af699a834d48 | -12.99938 | -48.11291 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6560a9aa-c850-3249-a5d6-4e39cc976511 | -13.70948 | -51.94024 | 2025-09-03 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7831402e-93ab-3a4e-a9cb-ecf2fd521677 | -15.09209 | -48.12384 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b00ff6ff-b921-3b75-bc6d-e12a35f65a7b | -9.61694 | -55.37205 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35efcb25-418d-36ed-9ca4-bc599d7981f3 | -9.14125 | -49.6604 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba0c48f4-7260-3870-a29c-5d8213e857ac | -9.63471 | -47.85557 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b607a4d4-05dd-3bb6-98ae-77030b4b557b | -12.94416 | -56.99054 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9a17a41f-f9d4-37cc-a0f6-3ac2633250da | -13.00757 | -48.09354 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f133a67-4300-3270-a473-0024bdfb7654 | -7.97013 | -55.29108 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d7762c9-a740-3180-962e-7ddf6ecf4c11 | -9.60746 | -55.387 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a01b82-0350-3a89-adac-13e16627fa73 | -7.71786 | -50.29401 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7945db7e-aff9-30d3-8adb-b8faff2e145c | -12.93617 | -56.997 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1abca656-de35-3e11-b36d-5d8fc9efacc3 | -10.45195 | -54.78502 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 909bc197-17ee-3fa9-b209-9495b070948b | -8.30875 | -55.095 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6a6fdfd-e43e-32de-a71a-b54e0858aa28 | -10.44828 | -54.78444 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1883044-e34a-3e0e-a71f-382df0607f07 | -13.10011 | -57.13339 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed28f6c1-8900-3186-b35c-aef16f5f5648 | -9.63235 | -47.8629 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65c97748-e160-3b04-b25f-428b03b86d6f | -13.69783 | -46.95678 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe015c47-5a6e-3dd1-83a6-aaae0612de13 | -11.62767 | -52.12941 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbfa080c-a71c-3efb-91b9-73d12174dca7 | -14.57376 | -48.05173 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac3019a5-351e-3694-8916-2da2ef5e41be | -13.5126 | -47.02126 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e52506b-21c8-3620-a802-ffbffe9cef04 | -9.62812 | -47.04845 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee87c90f-ff45-3061-883b-d0bd934afe2c | -12.94187 | -56.98248 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd435831-6e93-3652-a746-cb28b124931f | -6.44252 | -58.13708 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a51e90db-ca6a-36b6-a5e1-53ad72a7e5ff | -10.48231 | -50.34348 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc23d968-b1ff-3618-be72-eb4281c5e918 | -12.95214 | -48.0712 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee9e77c-72db-3567-88dd-24e438a91e9f | -12.99984 | -48.10889 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19e924f6-acee-3374-a68c-a01c5fad1030 | -14.79773 | -48.20465 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35003e1e-5ff8-3fcf-b6dc-126a6de348f9 | -12.9047 | -56.94955 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428e063b-a8d5-32c0-a9d9-3e9fb0af6ad3 | -15.00041 | -50.04934 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1631e725-db4c-3c75-a492-d11a53b1ea3d | -9.99522 | -46.8928 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2f2477d-3477-37db-94af-eb897b456a89 | -12.86931 | -48.03423 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cc621cc1-f178-365e-b86e-14b49e84c9ab | -12.90372 | -48.09666 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c2d3011-56f8-398c-8ef5-d051beda89d4 | -8.36606 | -48.30138 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1efa5a34-0a2c-33f9-bcf0-9b65deeac2f2 | -9.25919 | -56.89823 | 2025-09-03 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 071a17f8-05d7-349c-8b7f-fe17c5770de9 | -12.92419 | -57.00665 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24834ba3-b354-3e0e-bce0-0d65337aec7b | -7.53756 | -61.33346 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f0ba9729-3256-3cbf-b204-8b3e5499a615 | -11.42314 | -55.18372 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90bb6734-6a1f-37a0-befc-1707790b1abd | -10.48589 | -57.94296 | 2025-09-03 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b796287a-ee10-31a2-ac67-a73ec8fcc957 | -14.58172 | -48.04515 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff05abe9-4bd0-3b6c-80cc-220d139bd4d7 | -10.95672 | -48.14722 | 2025-09-03 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01f6e3fd-7107-355d-9bc9-c5f5797e8de1 | -10.27409 | -46.49252 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bf8fb08-be19-327e-a1c1-3b33ed4b6249 | -12.48735 | -53.82769 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b381083-bec5-3a45-9b28-bd42376f9943 | -10.93883 | -50.76733 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422caf48-a2ef-38ca-a287-8890e0970974 | -12.62997 | -56.99286 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8754c192-210d-364f-b223-1aef9a9600da | -13.45678 | -46.93149 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f309538f-b586-36e0-978a-2a09c71be0bb | -8.36718 | -52.54025 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf780015-6bb1-370f-89a7-5503b2196144 | -9.64244 | -47.03183 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ca63bda-f065-33f1-bda3-8f44e8aa5ece | -12.97515 | -54.75957 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d7e0700-e3fb-304f-a3ef-1e995c5906a8 | -13.00258 | -48.09999 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18c910dc-b4b8-356b-a0cc-b5d36a6ba690 | -11.61061 | -52.12261 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b898045-d6c6-3f75-860c-df3ffdb47fe9 | -8.08158 | -47.60073 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5a02217-9cc0-3f29-b22a-41e20ab4e4aa | -12.94586 | -56.97926 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcb1e3cd-0b56-3573-abf9-fcb177ca2567 | -12.60434 | -57.00036 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9c6d0b7-506d-3aec-90ee-65128efcd3e3 | -11.61002 | -52.12696 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8a942c6-b3b1-35fe-a461-4e24a58f7924 | -8.08958 | -47.59216 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0e8b0ec-62b1-3c5b-a38c-fc665559615b | -10.49585 | -53.65178 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6bc0c56-d406-3641-9764-d5a460bd0b75 | -9.39508 | -48.0511 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d0035f1-b5f1-3180-a2b6-c1c063043c06 | -11.62724 | -52.06722 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bb32ed1-321a-3b35-877f-38b8f8f01ff2 | -10.30265 | -46.36354 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ce729f1-0c11-38a2-8c3c-2b45da5dad69 | -7.72463 | -50.24865 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README92.md)
