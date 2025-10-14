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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ece4dc0-a787-3693-b7fd-e3a0ef0b6caf | -3.4343 | -50.25511 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b847ded-91c4-3f6c-b175-36913288e089 | -4.74069 | -45.65448 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 186d7399-5f4b-3ae9-b1c8-35f1f9b568ca | -5.42116 | -40.98743 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c216973-d7ba-3851-9729-763c55620760 | -5.03495 | -49.22057 | 2025-10-14 04:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629d5043-a65a-3a1b-a266-62f1449fa9b5 | -3.36233 | -50.28186 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99be030c-7457-3f47-bf3c-4d078cf73016 | -5.90044 | -42.83892 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c84404f0-9a97-3a7a-a936-ecc004698089 | -6.29352 | -42.9861 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f54b3b-9130-3c31-9941-0d774be26b64 | -4.1066 | -50.05431 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59e5885c-8d79-3e73-b243-5fa6c2c59284 | -6.30715 | -46.94018 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e646247-a4b6-3b3c-9b89-8e57d52146c3 | -6.29666 | -43.00027 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c60bca8e-c019-3571-9782-10e6999fffae | -3.22645 | -50.05605 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dbc30ac-2d9a-3049-901e-9604ad945f44 | -1.10136 | -52.26791 | 2025-10-14 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c53fe0ad-919a-37d6-ba17-2ab53e9d9a7c | -5.15136 | -46.06511 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22d2c83a-df5e-361e-8b14-b8635cd1df59 | -2.52894 | -47.80566 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 664a5c77-6c88-3fe9-a9a1-106de706df99 | -5.73958 | -40.77053 | 2025-10-14 04:23:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 549910ea-155c-3338-b0a7-00afc3457cfd | -3.06886 | -49.40955 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0b0d749-0868-3e6e-ad98-e454f41d120c | -4.55793 | -49.64713 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6975e838-1082-32fc-bc34-af7c25323b5f | -5.31269 | -42.90736 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bed012f-d94e-3a16-87fc-ebe650070fb3 | -6.4441 | -41.83841 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2bd7e20-fde2-3bba-9a45-337da0247821 | -4.42719 | -47.60288 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11ef4c5b-6f52-34c0-96e0-43476702970e | -6.02505 | -43.4038 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48788a9e-de15-30a9-b108-b0ae1bb3c934 | -2.72509 | -48.34999 | 2025-10-14 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93b4079d-ff41-3867-b737-684b2fa25508 | -6.14425 | -42.55705 | 2025-10-14 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d5abfeff-300c-34f7-ac43-694c9ff222b8 | -5.73606 | -40.76631 | 2025-10-14 04:23:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8422c72c-0793-3c60-b1ae-0aee0db5a9e2 | -6.44099 | -41.83306 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7564d903-62e8-3bf9-b996-5e68c4916558 | -3.53831 | -49.40769 | 2025-10-14 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41cd869b-403f-37e8-a3c6-cec3541f8a6f | -5.88112 | -42.86963 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de4f30f8-8594-3d71-b780-b24fa78d2309 | -5.91498 | -42.81572 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03f20fe4-e0df-3b1d-a9c6-0251319c16e9 | -3.15319 | -50.23413 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e5a677c-4f3a-327b-a1d3-a45136ca45c3 | -6.44731 | -43.99213 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0cdfc17-1c21-3110-8a59-f2f149185c6d | -6.50323 | -44.44275 | 2025-10-14 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83efbd3a-c34b-311b-adc1-5400eaf2221d | -2.52957 | -47.80173 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00a651ed-1468-3f6b-9275-ed37894fa2fd | -4.55868 | -49.6425 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a5195e4-fac5-3d69-bced-eea40fca600e | -5.48902 | -44.9984 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45762db4-733a-3975-9bc5-8a2b991dae14 | -6.23944 | -44.90979 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33cf1d80-66f4-3800-8f75-7e7b247cd354 | -3.67573 | -48.31074 | 2025-10-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07c99861-1470-3bc1-b79a-3070ceec7313 | -3.13543 | -50.21717 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d853c18b-25e0-36d0-8e53-8d1be7578a93 | -3.5064 | -49.71936 | 2025-10-14 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c465f916-9140-39d5-be95-b2dfddb8b487 | -5.70408 | -46.33017 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a3864c-3a5c-3829-b6a7-125546a9c223 | -4.66062 | -43.12574 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f2a63710-c6bc-3e10-9cfc-05e6e3e831fc | -4.07805 | -48.03667 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe0b880-1705-3f44-b93d-5eccfb4fdcee | -3.22047 | -48.9292 | 2025-10-14 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a52970f-6d41-3fbc-a2ff-051b57707dfd | -3.24654 | -50.81376 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c4f5ed-f21c-31f9-9afa-139b346937d9 | -6.63423 | -41.72462 | 2025-10-14 04:23:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d16a786-42cc-339e-a83f-bd56f65e2966 | -5.01632 | -46.76725 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cd55b555-b68b-3e83-b7d3-9c9e107e18be | -5.93739 | -42.3217 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4c4ceab5-b910-3341-b411-0d78c5a662f3 | -6.18568 | -41.75161 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 20ba8c1f-6676-34a5-8937-d9ab654d5016 | -4.7467 | -45.8953 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fd7453e-32bd-30b6-94b9-cfcb86905115 | -6.29946 | -42.99549 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41d63817-b6a8-31d5-89ac-1faeea80193b | -6.44482 | -41.83366 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc3d5fac-e410-302b-815a-09a2ee2a37c0 | -6.43857 | -41.82309 | 2025-10-14 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d6f1196-bbeb-3b2d-989d-4744b91306e8 | -3.6247 | -41.62795 | 2025-10-14 04:23:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38619bcb-1a1a-3254-afba-739b136fa31e | -3.15374 | -50.23069 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60e8c008-1261-36a8-9886-f5b30552c57f | -1.36984 | -47.16507 | 2025-10-14 04:23:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f134cd9c-78ea-32f0-a321-08387cdef4bc | -4.59441 | -46.3425 | 2025-10-14 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ee97f53-b904-3bfa-99c4-f3b529891fd9 | -5.99092 | -42.87345 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91fbdf6d-25ef-3a33-81b2-81c1deb5b7c7 | -2.53308 | -47.80231 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3865ef1-6137-3d2e-92a5-2ad849fb8cb7 | -5.49212 | -44.63438 | 2025-10-14 04:23:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea01caba-e65d-3960-8a93-6b2bec85f4e8 | -4.5336 | -47.4005 | 2025-10-14 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fba0be5f-f4e0-34fd-b0b2-f5d1998f7d7c | -5.85497 | -46.45017 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 060bef2c-6094-3afd-a3e6-a39c78e09f07 | -3.0658 | -49.40432 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 133cafdd-3516-37df-ad09-23a5a2623902 | -6.38906 | -41.48644 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 239e9547-066d-3895-9940-1087c099e29d | -3.99721 | -48.33931 | 2025-10-14 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8187ddfa-d807-30d2-a1ec-9e8883a594b8 | -3.37832 | -50.28444 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 126bc1c1-7bc1-3253-89ee-07c105e78687 | -3.8865 | -44.909 | 2025-10-14 04:23:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b05ef457-a4c1-352b-8a66-8b0f3aff6068 | -6.2203 | -47.03458 | 2025-10-14 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9fd31ba-8af2-37f6-808b-7bb5763b1eab | -2.88145 | -50.73358 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66804a46-1cfc-3757-b884-3d36adfc6d13 | -5.0191 | -46.7713 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0890770-8491-3dc8-9977-68f7648bb6e9 | -5.33319 | -45.19196 | 2025-10-14 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a183f55-63bb-31b0-9eb8-ee6bae90d2b3 | -3.70251 | -43.21412 | 2025-10-14 04:23:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1542dfbb-d375-3cf8-9e74-5ddd1fb61a9f | -5.11903 | -45.49563 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc0f143c-d748-34bc-b192-ce3411611d6e | -5.88146 | -42.87905 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a5cded0a-18ca-3516-ba55-5ef97bd65318 | -3.51873 | -49.71646 | 2025-10-14 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9435a55-42b7-3a9c-8319-319599354ed0 | -4.57325 | -48.02445 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e66b4a5b-9097-3149-8e93-482bc04d9752 | -5.59652 | -44.89686 | 2025-10-14 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 516af170-5c17-3984-ba1d-be735f1f21f8 | -6.15267 | -41.7738 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fedd98a6-3304-356e-a207-ca7fe6acef07 | -4.23246 | -43.01252 | 2025-10-14 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d82d6c83-7645-3248-8fb1-dd664c4d53d0 | -4.11131 | -50.05004 | 2025-10-14 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 789982aa-392d-3c10-9323-22e1977a12f5 | -5.40382 | -46.01744 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6af07c5-f65b-34a0-98c7-7e178f034113 | -3.72458 | -47.50269 | 2025-10-14 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3380f1b-aab2-303e-857a-381b740a348a | -2.53245 | -47.80623 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eac4a8de-0089-32e9-bb63-615b09ecb275 | -4.84797 | -42.77476 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 79ee9339-a2af-3a90-831f-43b00d7b818c | -3.03994 | -40.11209 | 2025-10-14 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7a729750-7381-3161-bb4b-e6d59008d4f3 | -5.99155 | -42.86937 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef69b7fc-3a4c-36c1-a98d-f9de8d882cee | -4.65943 | -43.13354 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 581acb20-297e-3f1f-9d83-7ee3645384ab | -6.15227 | -41.725 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a94515ea-78cd-3041-8821-8e26683db307 | -5.38654 | -43.22372 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7fd9451-f0b4-367b-94b6-505ebe36e822 | -4.63932 | -42.52682 | 2025-10-14 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 72a82c30-13ac-34f3-a4bb-db7e94966663 | -5.87629 | -42.87743 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2b5ad406-e7c1-3f47-99d4-a231143afbc9 | -5.49446 | -43.06497 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 08d84750-1a9f-3a32-a2d2-8f4baed55565 | -4.85115 | -43.2054 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 364bedcb-d82b-3656-a813-0aa7064b71c8 | -6.15146 | -41.77097 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 472d0bfe-24fa-36f4-8c22-7e6e1a22fc7a | -5.65332 | -43.60287 | 2025-10-14 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 096e0c95-2381-31f6-a89b-5ead23775314 | -5.59145 | -42.57919 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22acab25-d272-30f5-9b82-48bee6d6b4ee | -4.62232 | -45.78046 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a3bdc96-94e6-3249-96b6-893cf1fcae60 | -5.94412 | -43.73561 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5403a156-ef5d-3be6-bfcf-40312e00418f | -3.69963 | -43.20981 | 2025-10-14 04:23:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c047796-37f5-32d2-b128-44ca42302e8d | -2.87731 | -50.73291 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b4fbf6b-d0f0-3de8-a1e9-cd34131dc8ab | -3.15824 | -42.89161 | 2025-10-14 04:23:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aabb9c3-b1ee-3f15-87e9-4e8c485a6e2e | -4.90755 | -45.50096 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
