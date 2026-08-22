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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 647c2b7b-9345-36d6-beff-648e478ea286 | -6.77154 | -58.68023 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 048bb189-e69b-3cee-b55a-3033b200b4a7 | -6.85385 | -59.43258 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 350f6f18-8ccf-3850-a5d6-473a8d8d6cc8 | -9.17904 | -57.06255 | 2026-08-22 05:04:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d872093-1d70-3708-b842-7ad583f4b76e | -6.77292 | -58.6723 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5d4e01a-5ad0-3196-96a6-9d59243d81fb | -6.8 | -59.66751 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8934c6ff-c9be-3d91-ab4b-cf841ad15687 | -9.21007 | -59.77381 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679c5c25-0a08-3eb2-b630-107b78369223 | -9.40468 | -60.42053 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce65764-ae8c-379f-a698-d0325ecc4a19 | -7.48055 | -45.14449 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 306f4bec-e32e-33f3-98bd-1026df3af52d | -8.52417 | -55.31927 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6691604d-05b5-35b1-87db-7447e5303793 | -9.44683 | -51.59701 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54d300fd-8054-3f89-8d15-508909e1b4c1 | -9.2137 | -59.77895 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae045c2a-a35b-335e-ab18-b9019ac6c2ec | -10.80675 | -50.97483 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| cf9cb6a4-830e-3a8f-8b6f-0a6b01c222db | -7.18001 | -42.75406 | 2026-08-22 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20142603-82c8-3b60-847b-88d6da2d31ad | -7.60118 | -60.94948 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1d7df2b-df86-330c-8860-c8b1fe60325f | -6.76077 | -58.65113 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb431d5-9ca6-3aaa-96ef-909d99edf817 | -9.52542 | -51.6508 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4ec92a7-1039-3363-9ea1-9d94374d7959 | -6.48332 | -51.59821 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5dd7644-44e2-3dae-8a1a-61589b5cbc6c | -9.44624 | -51.6008 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f6575ce-7c60-36a0-8d58-e2181cd39aca | -6.3988 | -49.8143 | 2026-08-22 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a300faa8-8dc8-3a10-a2f3-e11e013df59e | -11.39736 | -47.20654 | 2026-08-22 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c14938b9-4c34-3d23-ae9b-fed8edbe1a0e | -8.61558 | -54.73192 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e05e80a-a0ad-347a-abe2-83d0565bcd3f | -7.68856 | -48.42066 | 2026-08-22 05:04:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3a15c1-555e-3716-8509-c1c8126f3fc3 | -6.38817 | -54.95689 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7612aee-a549-32d3-b456-9b682989e6d5 | -6.74958 | -58.66552 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe761449-307f-387b-8c23-3d8715a2f45b | -6.9092 | -58.9985 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c112110-cc64-36b7-bab5-83197ce59ed5 | -8.52702 | -55.32361 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4078c54d-a3ec-3961-9c89-a7078d889863 | -6.94569 | -59.30986 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa63c8e5-7b52-3eeb-b9b4-edb9dc55c6cb | -6.78877 | -59.43514 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f2d909d-c4e8-31bc-a350-5aff80d7975c | -12.79646 | -51.48051 | 2026-08-22 05:04:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4f2fc0c-9851-3db7-9665-0f6aa088f592 | -10.73837 | -58.90574 | 2026-08-22 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1debf135-3013-3ca3-82d8-894ce51099b9 | -6.8901 | -56.43371 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ec4085b-77a3-3556-9bbd-f5d4d28ff060 | -8.53036 | -54.84919 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 93b5f6a5-3381-361d-b347-23bb80baab85 | -9.44273 | -51.61895 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb31c8e-5056-3ba1-a797-c904c66d182d | -6.15692 | -57.73598 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 215c80f1-ab75-3b3b-9b53-dc6cb7e42693 | -6.79932 | -59.42759 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 3fabac13-e3c0-38ae-a4cc-ec360a16d97f | -10.89558 | -50.27938 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d55ba79-ce16-378c-a0f0-a35cb683cff1 | -14.40209 | -43.79482 | 2026-08-22 05:04:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b959c2-3f45-3f26-bdc0-d793e3045ca0 | -7.68345 | -46.17054 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 343521de-b7a1-3c46-9106-a1abb7670c4d | -6.85829 | -59.46093 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 292b7016-cbbb-34f0-a82b-f3690c060821 | -6.13372 | -59.90406 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 409a14c2-209a-3828-9f4f-bc1edbf1e010 | -6.78663 | -59.42088 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c2f3ed31-f279-32ae-a619-6dc3b6f0f7a2 | -6.11113 | -59.94321 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8297b2a8-2a66-341a-bf2d-565a44e6fe5b | -8.49955 | -54.86669 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0424a8-1c56-3319-b0e7-b6cb8172cfe5 | -6.66173 | -56.34463 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbebf31f-3baa-319a-b3e0-c485eb57e5b8 | -6.76237 | -58.66769 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ce27000d-d33b-31e8-9800-84514e9892bd | -5.9982 | -57.81533 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c098fbba-803e-3cbf-9196-e8bab740bd2d | -9.40182 | -60.41019 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa8110f5-f0f1-38c7-bfed-d4b8fb5cfa09 | -10.52741 | -50.7735 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 273b9065-02fc-3292-8789-3f027a6584d1 | -9.17566 | -59.46012 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b8230cd9-4cf8-3aa5-ad8e-6cf1a5a00ac2 | -12.55303 | -54.76837 | 2026-08-22 05:04:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa9ac35c-cd60-3325-a07f-21dd12005061 | -9.0546 | -57.0666 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b28c49c-f03e-3d01-89ac-c76bb3d18825 | -7.51233 | -47.64138 | 2026-08-22 05:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e3274ab-bf84-3ad4-882e-17ced94d5fc4 | -6.77542 | -58.69458 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2929e19-2769-313d-8ed1-d17be747062c | -11.99795 | -53.4234 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0381bf82-bbfe-3c60-84ed-84ab189bfe69 | -6.75585 | -58.65433 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 45a594c5-ec95-3084-b4a1-9a051f42f67f | -8.39638 | -62.68248 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 52f96f30-77e2-38df-8b7b-d8482858c348 | -8.59128 | -54.73164 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9c763c0-c569-34c6-8734-c05612612a18 | -8.6917 | -54.63227 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a90536-c830-3db0-bb77-55ec06f610f0 | -10.52679 | -50.77762 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f099fffb-fa8c-3201-807f-cf599f5b88f5 | -12.26191 | -43.135 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2bfdb35-5888-3235-94c9-1b3e87737937 | -9.06772 | -60.43518 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7233ee3a-387e-34d1-9860-7bd0cad92db1 | -6.26483 | -62.52671 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a7844ae-79ae-302d-99dc-8b72d3c03e19 | -8.99898 | -50.7136 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1bebc14-f800-3bba-b20e-cfd7527f56cd | -8.03818 | -51.79482 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4018170b-1f52-34bf-b430-d3dfaa37b9d9 | -6.76928 | -58.65262 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d62ecfc-0a97-3c0b-b297-525582021e35 | -6.22063 | -55.48055 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a20a710-3b21-3619-9020-17372e3a8512 | -12.82417 | -48.45963 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6a30bdf-3470-360e-9c30-bdfb112e744d | -6.66317 | -56.33599 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe9b2a5-3fe1-388a-8044-0195cdc66e87 | -8.57505 | -54.78886 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5070d276-7191-39f6-8429-d5dcd5ef03cc | -12.65534 | -47.09017 | 2026-08-22 05:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec4adba9-a52a-347b-a107-e0c136410d72 | -6.8032 | -58.6241 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80d2cbb7-65e2-3abf-a205-f7e2a3264387 | -12.82834 | -48.46066 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 645c4247-97b8-3847-8a1e-c035f9a0fc23 | -6.12435 | -59.90245 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82b2306e-bebe-357d-bbf1-d94c9f1c9654 | -7.73635 | -46.16021 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 447d86c5-9943-314c-a5e9-3a34cdc61581 | -6.86433 | -59.02507 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9244a2ce-9305-363d-914e-0c969900f751 | -11.48839 | -49.69316 | 2026-08-22 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30f92aca-a603-378c-ac2b-fc5dfa804b1c | -8.54558 | -55.31052 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1bdb716-2c71-320a-a673-179edf5dc6ee | -6.11779 | -57.69658 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ecaace6-1366-3a57-9ab0-bd9d0f6f8069 | -7.01743 | -59.54896 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a3216d0-0ed0-38ed-87dd-c1a32b18c820 | -10.81325 | -50.97997 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fd0f352-4bb1-301b-b919-7de23505eee5 | -6.12171 | -59.90928 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b5ddbed-5aed-33b8-84a2-7b4fcace28fb | -12.24419 | -43.18209 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8654a36a-bc8b-34a8-b1b1-5588d91c5475 | -9.522 | -51.65026 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2929b6c3-2f85-3bbd-a247-924642767811 | -8.10233 | -51.67118 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5495e20-931e-37d5-a7ee-f8381565607e | -6.90415 | -59.00191 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 92105fb1-36f0-3c32-8d5d-06ab7fa1acf6 | -6.76793 | -59.77232 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e33269-b12c-3317-b2c6-8b89fb50da49 | -10.27113 | -50.37644 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a146e4f3-76e7-3988-8c1a-9e32efec97e4 | -6.25117 | -55.398 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21ec9a85-92b1-360d-a450-0702cbc32028 | -6.85948 | -59.43575 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 746ee227-34df-3343-8a93-09b4effbf55c | -6.75944 | -58.65903 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 807f5b16-541d-3aad-add3-957066c0606b | -6.67753 | -58.75234 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 627c713e-b2a0-3a73-bf26-a33b60e475ec | -11.13417 | -49.04035 | 2026-08-22 05:04:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8426b95c-2a16-3682-a0e2-bfa7b0351014 | -6.81058 | -59.41583 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb5915ab-fe1d-32bb-a2f4-b31ba17c8c5b | -6.22593 | -55.48417 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9dc30ff-5598-3a8a-a40d-97c891a1e24e | -9.45351 | -51.59407 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5040de79-eaf9-3d9c-8b9e-ebfedec9d4f6 | -9.06056 | -60.43229 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ccc6313-8e6c-3aae-8650-ac1f178788b4 | -9.18215 | -59.44852 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 855daea6-f996-35e7-ba8e-f4245cba35f6 | -6.38879 | -54.95308 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e78405da-e584-362f-874b-2abb8ee53f3a | -10.51962 | -50.77662 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13e462ca-4d53-31e2-b3a4-d4e9edec61d6 | -10.52382 | -50.77301 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README39.md)
