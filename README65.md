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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d741fd1-ce6f-3ea4-befd-10689a053839 | -4.20169 | -49.75784 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 964ec994-3425-3e80-ac2e-60fc8b2b01b1 | -2.82684 | -49.43827 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d17741a-f658-35f6-9150-ac933d360e2a | -4.82451 | -48.09833 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0226ce1f-a052-3296-a61f-5c950fce6efa | -4.18619 | -46.58411 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e268087d-8ee4-3512-9812-78c87434e8e0 | -3.2704 | -51.06023 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6b17da-5ea1-3b6b-99d7-3b0c5890fdc0 | -4.12323 | -46.02074 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f0088be-53fb-3acc-98f4-93c784618ec6 | -3.24796 | -46.4709 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14d26892-17cb-32e2-af28-592628e21765 | -5.2648 | -46.31153 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e92bebd-b004-32d8-963b-1f76af703549 | -3.30067 | -49.17448 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 968c57d7-5862-3c74-8531-556b9a6c55d4 | -3.21809 | -50.30614 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 31ef7523-8531-323c-a2f9-553c13d0a54c | -4.07229 | -48.3176 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c02bc27-e8f0-33b4-b937-0af530373e2f | -11.82888 | -44.22813 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1866b77-82f0-327d-b05b-10f082c58ecf | -10.52976 | -49.354 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e52f3bbd-026c-3f6e-b1c3-59d50ce6ace8 | -15.31928 | -42.83241 | 2024-11-09 04:36:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4603b8a8-cdb3-3cb1-9b18-4926b94528ae | -12.00733 | -44.14497 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e85e64a2-ba8b-3343-8986-4b8d71ff8051 | -12.11131 | -51.39829 | 2024-11-09 04:36:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a1498f-04e8-3efd-a776-fdad103fcdfb | -10.73395 | -49.82782 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10c96732-bb8a-3327-b1f2-b3a45137701f | -13.4062 | -43.01347 | 2024-11-09 04:36:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2cbae29-8c1f-3bd0-81ec-c5eb40288c0c | -14.80157 | -42.8689 | 2024-11-09 04:36:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4bbb9caf-8926-325f-bfc3-493dae038a01 | -10.52866 | -49.361 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62cc4a4f-7cd2-3d61-9f65-b7249cf6b62b | -11.37158 | -49.79753 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f459df11-d004-30d4-a086-625aee1c4159 | -11.3655 | -49.79293 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bde8b716-340f-332d-b8a6-c473f3faf5a4 | -14.80117 | -42.86774 | 2024-11-09 04:36:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71e0cb60-68c8-3f5f-93b0-dd21fe370373 | -10.73334 | -49.53108 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a23fb679-8867-39da-b9e5-01dbf59f19df | -11.59188 | -50.90026 | 2024-11-09 04:36:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a2d645d-3ce9-37db-866b-699025c855a6 | -10.67533 | -49.42457 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c233506-4c66-3070-9acd-520f606a2df2 | -10.7273 | -49.82674 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cdd29c7-5a41-3322-a5cc-7592cf58c609 | -11.56039 | -49.91567 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e5e8745-4fff-3e95-8065-84f1d6d72d0e | -10.53212 | -49.36216 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94be0c11-3e91-3704-a457-95ff3faebfcd | -10.5259 | -49.35697 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98589534-70e8-388e-9cfb-5a0c59b34917 | -12.01184 | -44.14213 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0df500a2-5b03-3372-a123-6bb259b0d0e4 | -10.53267 | -49.35866 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89a194ef-d935-3ee1-a619-609107e5bafe | -10.98121 | -51.47189 | 2024-11-09 04:36:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7992634-ea0a-31a0-8724-bea2575dcf86 | -11.36494 | -49.79646 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92b88c74-7250-390d-934b-7462f95963ac | -11.23448 | -49.78263 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72d5fbec-f0e3-3fb0-a8fe-65e90860ad68 | -10.73002 | -49.53055 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 15d266cd-33e6-3b7f-bd34-2680632188bf | -11.53193 | -45.00861 | 2024-11-09 04:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23fcba40-9630-34dd-afdb-d13a8c96419c | -13.53865 | -42.40413 | 2024-11-09 04:36:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6da13027-2dba-3041-896d-47bf7c19a4b0 | -11.26402 | -49.9399 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03b43c46-310c-3378-8afb-9c3b187cf2ad | -12.75426 | -51.52821 | 2024-11-09 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8e6908a-2506-3231-9d68-099824bba17a | -10.73007 | -49.83082 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fd9ebdf-e6fd-35d8-b7fc-ac85a2866350 | -12.01136 | -44.14561 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79154b46-69f8-3b87-8465-0da7b877ffcf | -12.00782 | -44.14145 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| defaa636-7742-3ff3-a7c5-b463f5aa210d | -10.52921 | -49.35749 | 2024-11-09 04:36:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9350bedf-6d16-3606-9779-d57484e02829 | -11.36826 | -49.79699 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eccbe905-2d4b-3433-ae26-ac0360563b83 | -11.37214 | -49.794 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db1b1e5c-44c9-345b-a217-dd6f699f78fd | -10.73222 | -49.53811 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6270ad56-7d9f-39f0-b8cc-d29279b7c1a7 | -10.73278 | -49.5346 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac919eec-f064-3fac-98b8-24417f1d6485 | -12.11411 | -51.4027 | 2024-11-09 04:36:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c58c6505-027d-35f4-82b5-9db49ec0b3df | -11.36882 | -49.79346 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfcffe25-4b3a-32a6-833c-6994b2b00b75 | -10.73063 | -49.82728 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 732426c4-38fd-3d3c-bb69-fbb9d911f29e | -14.9559 | -42.30141 | 2024-11-09 04:36:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7696a56c-79eb-39be-bdf0-4c93e4004082 | -12.0083 | -44.13794 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2482a6c5-c8e3-3bd7-91d9-8f70797c3a80 | -11.66298 | -49.76195 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aae9e0f-eb15-3a96-8ab1-f49fc3fbdbb0 | -11.86194 | -42.65373 | 2024-11-09 04:36:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b0008e8-435a-371a-8ab7-0b51ff98aaac | -10.72398 | -49.82621 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0896e2ea-ee8e-38bf-afce-4255f695df70 | -11.58227 | -49.77782 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657ce739-f3e8-3318-9eba-3b348090cc28 | -11.66353 | -49.75842 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e351309-e3c0-33f5-9736-dc6f8fe48125 | -10.4612 | -49.66005 | 2024-11-09 04:36:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe5ee35-8fa7-35a0-b439-6e3aacc7f426 | -11.59114 | -50.89978 | 2024-11-09 04:36:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ce821b-0715-392e-8aa8-93da97edc309 | -10.46452 | -49.66059 | 2024-11-09 04:36:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bda0a1f-1979-3b3c-87d5-fa40c24ad27d | -11.27095 | -49.81028 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ce7e065-af3e-3359-a72b-2a79ed68eaac | -11.27039 | -49.81381 | 2024-11-09 04:36:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 711570ee-99d3-3150-985c-7e66a3c50108 | -11.16414 | -45.09301 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88dbd52b-efb0-313c-888d-d5787371789f | -12.01231 | -44.13869 | 2024-11-09 04:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7dac6b0d-7488-31d9-8787-21619b8fe331 | -11.65966 | -49.76141 | 2024-11-09 04:36:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 333ef3d7-b3d9-35b2-8c52-00f2a979bbeb | -17.29946 | -57.49814 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2456b78f-6210-369a-8b8a-cfc8c59db65a | -21.13711 | -55.80833 | 2024-11-09 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97f1ed27-7a8f-3f63-85d8-50ce428d2496 | -16.09773 | -60.09095 | 2024-11-09 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73270232-1532-39ef-840c-c5475199a23f | -17.29745 | -57.49551 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f849c9af-401b-3007-b977-5d214869c130 | -17.29498 | -57.49721 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e5a9ed22-e906-3787-aebf-3357799466ff | -17.24485 | -57.49174 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8391a76c-1e61-392f-8f66-874fb26b40f4 | -20.28297 | -52.96375 | 2024-11-09 04:38:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 974a2fb4-0df4-3b0a-9ee0-5e3c9a3d2317 | -19.83158 | -55.30638 | 2024-11-09 04:38:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afdab04d-64fd-3a6b-9f62-2294b0ad63eb | -16.097 | -60.09451 | 2024-11-09 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b96e9be-dee6-3aec-901c-b1afe76ae0f3 | -17.24575 | -57.48706 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0de93da1-ae28-371b-a229-bfcb1c113912 | -17.29051 | -57.49629 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 96cf8547-c4e0-3b8e-941a-0eae2d58cc8a | -17.40325 | -54.71547 | 2024-11-09 04:38:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1479f188-2d11-3aa4-a756-01e1fdbf924e | -17.29653 | -57.50018 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0b9bf4db-8f51-3ea5-b882-fada03c5ab1d | -17.24395 | -57.49642 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 157ea60a-b921-3aae-9fa7-23ea8aff8680 | -17.40702 | -54.71619 | 2024-11-09 04:38:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3be3a494-341b-33ab-a681-b4a1f68d22d1 | -17.29297 | -57.49459 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 09e7784b-950e-3a3b-94ed-6fae594a52a6 | -17.28962 | -57.50097 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e757ec25-dea6-31e0-bcb2-8a9db7c44dab | -17.29206 | -57.49926 | 2024-11-09 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e25f324a-5a20-3a84-b27a-e5a65a8846c3 | -4.2484 | -47.5947 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 55a82233-0be4-3534-9b42-a9b93d0d9ff5 | -4.2033 | -45.8538 | 2024-11-09 04:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.5 |
| bd8ab08c-04f2-34c6-bfbf-fa965b576c35 | -11.1068 | -43.3428 | 2024-11-09 04:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 53b928a6-0203-3b4b-ae93-2b8e550d8430 | -2.2318 | -46.5508 | 2024-11-09 04:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f13d53ec-6ff5-3737-a3f9-2399e9a56a2d | -4.2671 | -47.572 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8859b50a-16c6-31e1-aec1-e47aec7be521 | -3.6004 | -47.3395 | 2024-11-09 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| ac76e429-b1d6-3a88-beff-8beb65708f70 | -4.2058 | -48.5491 | 2024-11-09 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 20ce7221-bfca-36f8-b2e1-0695a15e6b9f | -3.9668 | -48.1932 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 10991886-c5a4-35fb-ba86-7d69dcdbd20e | -4.2219 | -45.8529 | 2024-11-09 04:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 7ab0af35-df59-3f64-b1c4-1e5c8da3dfa5 | -3.6003 | -47.3614 | 2024-11-09 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1391f012-c19f-34b0-a947-b8004c1390c5 | -11.0877 | -43.3456 | 2024-11-09 04:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 481a9222-8ad4-3490-8187-3610bf5d270a | -3.0865 | -50.5625 | 2024-11-09 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a23b23b0-eebe-38dc-8288-916d94a827fd | -3.9669 | -48.1716 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 197.9 |
| bc66955a-5923-3f21-a303-62ee65e56ebd | -3.9853 | -48.1924 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5928ae35-cfd6-3ca7-9385-c2ff9c2988cd | -3.5819 | -47.3403 | 2024-11-09 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 72fe66a7-430c-3d6f-aac4-b90f7bbdabf8 | -3.9854 | -48.1708 | 2024-11-09 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |


[Clique aqui para ver as próximas entradas](README66.md)
