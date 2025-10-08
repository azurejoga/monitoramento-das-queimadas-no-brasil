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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7427c9f9-097f-34f6-9149-59c71c380ac0 | -3.23197 | -46.78981 | 2025-10-08 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 36191e3b-66a2-3ff4-86d3-34c49591ebfe | -5.14876 | -44.99858 | 2025-10-08 00:54:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 563fc24c-6bab-3a05-af75-154eca77c122 | -5.13167 | -44.9336 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 378a17f8-c682-37b6-9366-fec6a4a678b8 | -4.07795 | -48.05046 | 2025-10-08 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0a90eebb-0247-3ae7-b64e-70b6092b2ced | -4.51011 | -46.36645 | 2025-10-08 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cdececf5-8156-33d3-aca0-01b6f8549add | -4.86019 | -45.76143 | 2025-10-08 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| d73e123e-3412-3027-985c-46776ff834f1 | -4.68829 | -45.8325 | 2025-10-08 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 2f677a7e-2f91-3cb4-afd7-192400420128 | -0.90339 | -47.54756 | 2025-10-08 00:54:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 5654b695-192d-3e3a-9883-424a92e185d4 | -5.16314 | -46.92904 | 2025-10-08 00:54:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f3c5b2db-e1eb-3ce7-97bb-379ea389a3cb | -3.45705 | -45.5942 | 2025-10-08 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2b79b787-582d-362e-abe7-63fa94e097ad | -3.22366 | -49.35579 | 2025-10-08 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f4e1451b-bad5-3468-b03f-77d1a48c088b | -4.71942 | -45.82763 | 2025-10-08 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 9e1edacc-5e53-3caf-9e2f-9fb3d13f849f | -3.09117 | -50.56821 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 3a5616ef-eaa8-3af0-a792-1ea0a14f758d | -4.053 | -47.50808 | 2025-10-08 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 70ac1354-bfd8-395e-a270-6f8fbdba333d | -4.84445 | -45.76298 | 2025-10-08 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 75be4247-540c-3e79-adc1-6e5b20e9be22 | -4.50592 | -46.33852 | 2025-10-08 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 5c7e920e-0437-3e56-b113-fa8ede4e62a5 | -3.44953 | -45.6023 | 2025-10-08 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 10fc94f6-3a3c-360f-9fed-c819b06845d8 | -4.01814 | -48.9669 | 2025-10-08 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 412654b3-1e9b-37d2-affd-3ee0e8dd1728 | -5.17134 | -45.14049 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| f296c5a8-06ce-3acd-80d4-c3a5b48b1d55 | -5.71607 | -45.68928 | 2025-10-08 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| bcfd4117-ce75-371d-9793-efdc25757765 | -5.1432 | -44.96368 | 2025-10-08 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 12f32258-f8c8-3a92-a043-2a911e92d20c | -5.58899 | -45.84549 | 2025-10-08 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 927bb982-3053-3005-81a7-b8751399de3c | -3.14577 | -50.30605 | 2025-10-08 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bcbf73d0-fca0-36c3-9bcd-6e8bc682749a | -5.13236 | -45.00144 | 2025-10-08 00:54:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| afd2f278-cb47-3d33-af12-b5d609d75328 | -12.031 | -45.2132 | 2025-10-08 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e84f4a3a-7663-3954-aa26-616c751e9d69 | -11.4531 | -50.2195 | 2025-10-08 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a670a1db-88d4-3808-940e-70ca01c9d309 | -5.1227 | -44.9682 | 2025-10-08 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3eda531a-2ad4-30dd-abe3-e12283204298 | -4.8557 | -45.7511 | 2025-10-08 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e85beb8d-e323-3581-9543-bdf0a3309ec7 | -12.3971 | -63.8811 | 2025-10-08 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3dc7327a-b703-3d44-a1bb-39d9d9ecfc9e | -10.93 | -51.0229 | 2025-10-08 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.6 |
| fe4b7f3a-c687-3bb2-9976-1c8b2cefe6cf | -13.7918 | -45.809 | 2025-10-08 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| d44c8eba-a1b3-326d-9719-4eb6abbe95e6 | -13.7165 | -45.7064 | 2025-10-08 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 618d60c9-d654-36ad-807b-f487262d06d5 | -10.911 | -51.0249 | 2025-10-08 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 53b649a7-ae86-349d-918b-3af81ea9e605 | -7.017 | -42.8762 | 2025-10-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 6d810f6d-2724-3982-8c2d-bcb78e489294 | -11.6888 | -50.9833 | 2025-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 339.5 |
| fc88bc67-2f3e-3a3e-958e-ed985826df0d | -3.4422 | -45.598 | 2025-10-08 01:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 34ffae6e-a11a-3042-b2a6-ec9bcbe89953 | -11.6891 | -50.9619 | 2025-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9095c54d-7eeb-314d-a38f-fdcab4746d8c | -11.7079 | -50.9811 | 2025-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3902e781-c456-33bc-b588-be64cd2b69c0 | -12.0314 | -45.1901 | 2025-10-08 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ce838740-b311-31bd-9229-a6c94a92b221 | -13.8112 | -45.8057 | 2025-10-08 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| b9d962d1-9e6e-3260-87ca-b3afa687fc3d | -7.0167 | -42.8998 | 2025-10-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| c90132f4-c1f1-3747-9be9-dc2a5e354fe6 | -19.8584 | -46.1569 | 2025-10-08 01:00:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7b8dd028-ae56-3778-8a11-2d20f13de6ad | -11.6698 | -50.9854 | 2025-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d7dc717d-883f-37b2-bbc8-9834dd6dc729 | -13.8117 | -45.7826 | 2025-10-08 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cfb5eefc-e132-35b9-8dbe-43f422a00787 | -17.982 | -57.485 | 2025-10-08 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 364be7f0-1041-3905-a258-33de3d6e155b | -19.514 | -44.0768 | 2025-10-08 01:00:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 37dd6984-ee6a-3653-9a14-08b87c633329 | -4.6873 | -45.8504 | 2025-10-08 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a25294ff-deed-3fcf-bded-d556f0bf452f | -4.6875 | -45.828 | 2025-10-08 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 0a818f89-8d84-37e6-9262-24a63c3cb028 | -13.7923 | -45.7859 | 2025-10-08 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 42d9d74a-c0cf-3519-9385-36926b9a82a6 | -17.9817 | -57.5056 | 2025-10-08 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 3e559501-d04b-3711-ad69-92bee6532220 | -9.6295 | -40.3392 | 2025-10-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 24e85950-8d4e-3160-8488-4e2eb61eb7a7 | -9.6299 | -40.3143 | 2025-10-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 8de734db-89ad-3e2d-a823-77ee3f831cfb | -4.4977 | -46.3731 | 2025-10-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4f51e343-7584-3911-9462-6eb2e0e3ab7b | -4.4978 | -46.3509 | 2025-10-08 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| dd3a6794-f3e2-306a-8128-d5867b07def1 | -4.5331 | -43.9067 | 2025-10-08 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 07a3cc45-99ce-3fd3-ad06-17d1c1874f5e | -5.1414 | -44.967 | 2025-10-08 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 274.1 |
| 99f25d0d-65e1-3c4b-b3e6-006705f640af | -9.6108 | -40.3171 | 2025-10-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 6fb42704-74f9-338f-9909-5784983fe2eb | -3.7937 | -49.4211 | 2025-10-08 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c1188d0e-56c7-3a50-8481-5d0902f6749f | -5.1416 | -44.9443 | 2025-10-08 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6ab3b7e4-0bef-3831-ae9f-1ae161c4283d | -11.4534 | -50.198 | 2025-10-08 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 495e0229-0e7d-3627-bb7f-f41b9b1c6dc5 | -9.6104 | -40.342 | 2025-10-08 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 196.1 |
| 4ee9c23d-7376-3c27-8e93-4ed28d92d5e4 | -7.6474 | -63.4584 | 2025-10-08 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 85db48fe-eec5-3fab-bce7-ddaf7fa0a368 | -13.7364 | -45.68 | 2025-10-08 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 89449497-0c68-33fa-aaad-c3f812bc5cc8 | -13.7359 | -45.7031 | 2025-10-08 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 01b47c1b-b0d6-33b8-8fd1-9ec66ad04167 | -4.6504 | -43.2038 | 2025-10-08 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0b5409cc-de44-3122-be87-8913103f83ec | -6.9982 | -42.878 | 2025-10-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| a9edb4db-f24a-3459-9355-138cb6117de8 | -11.6885 | -51.0046 | 2025-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 79bc2632-9d7f-357f-8c73-44374f78f944 | -4.6505 | -43.1805 | 2025-10-08 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| b5398df1-244a-3b3d-bf38-50470097d0c0 | -9.6104 | -40.342 | 2025-10-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 7a17cfc3-245a-3748-91af-6633309ff8aa | -17.982 | -57.485 | 2025-10-08 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 7d6f6d66-59ca-30ab-8c37-20ea34fe5532 | -9.6295 | -40.3392 | 2025-10-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.0 |
| b4440db7-25b4-3923-ade3-0eb9af8cba99 | -7.6474 | -63.4584 | 2025-10-08 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7300944d-6994-3f0c-9008-cd1a282f1a70 | -11.6885 | -51.0046 | 2025-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| dfdc0719-45f3-35e4-835d-2253ccb91a0e | -4.533 | -43.9298 | 2025-10-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 6c9dd909-c378-38ca-b14d-31a0dd36e1fd | -4.5331 | -43.9067 | 2025-10-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| df8cd095-a9e0-3251-813e-3a986195c52d | -11.4534 | -50.198 | 2025-10-08 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 26aeb384-52d3-33a7-b1f4-7c88c45c5956 | -10.911 | -51.0249 | 2025-10-08 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 13cc0b16-21d1-3097-9e70-4b8cd2c95020 | -4.8557 | -45.7511 | 2025-10-08 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c0241a06-f4d5-3648-996f-7df9de3188d9 | -12.3971 | -63.8811 | 2025-10-08 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3f82238c-5fd8-307f-865a-3c8c19319186 | -14.6988 | -46.0671 | 2025-10-08 01:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ba1b1443-9a92-3423-bd03-9ddfe1e722ca | -5.1227 | -44.9682 | 2025-10-08 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0a1cf7e3-d1e0-36f4-a108-9c2a69ee8cc3 | -5.3063 | -43.0897 | 2025-10-08 01:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 09a1d7f0-2564-347b-aed9-5dab15ed1d24 | -4.4978 | -46.3509 | 2025-10-08 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ff7928b1-ddae-3bfe-ab69-361c2b81817d | -11.4531 | -50.2195 | 2025-10-08 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dcfe6274-3dfa-39a8-89b6-8691ed359105 | -7.0167 | -42.8998 | 2025-10-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| a325ce75-ec37-3248-90cb-7ccab74b4e36 | -11.6891 | -50.9619 | 2025-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d43b47b3-c693-3ab9-8ebb-85c0e03b129e | -7.017 | -42.8762 | 2025-10-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 59da142d-08e0-3fa5-bca9-17450788c16b | -12.0314 | -45.1901 | 2025-10-08 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2bdff0f2-e51f-3305-bacd-3954a2b1d99f | -17.9817 | -57.5056 | 2025-10-08 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| cac605e4-38ab-349e-81bb-619a0de0b40d | -7.629 | -63.459 | 2025-10-08 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b7fdc98d-b533-3e9e-af4f-76e3dc038b17 | -6.9982 | -42.878 | 2025-10-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 379d9d4c-a6cd-350a-beea-12c33f28c4eb | -11.3378 | -56.1997 | 2025-10-08 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a98355e5-9e51-3b39-85dd-8e967e5947a7 | -19.5148 | -44.0522 | 2025-10-08 01:10:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 6da2eb93-7233-322a-a25f-17abe5b8f940 | -4.6504 | -43.2038 | 2025-10-08 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6332a7ed-d8e3-3e70-845a-3efe8b165a7f | -19.514 | -44.0768 | 2025-10-08 01:10:00 | GOES-19 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 239.5 |
| a5f97029-60d0-3d0a-9be1-2d28463d26ce | -17.5356 | -40.163 | 2025-10-08 01:10:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 13250a70-e0d7-3499-abec-633d4a87f0af | -2.519 | -44.1139 | 2025-10-08 01:10:00 | GOES-19 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 48c614bb-71ae-31e7-816f-4d1395018d18 | -12.0036 | -46.7667 | 2025-10-08 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 05a2fec2-de9c-3447-9590-295ea31021f6 | -5.1416 | -44.9443 | 2025-10-08 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 01db5754-84bd-3b0e-a31a-be4d3301b8a2 | -4.6875 | -45.828 | 2025-10-08 01:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README9.md)
