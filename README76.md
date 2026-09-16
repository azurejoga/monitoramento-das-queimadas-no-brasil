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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14ec5711-51c5-3ef0-9501-19eeb9ed3f37 | 4.1516 | -60.6878 | 2026-09-16 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d85fdf77-09f3-3610-9d2f-59b31ffe3788 | -9.7793 | -60.4744 | 2026-09-16 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0e61c239-922b-3d8d-b814-e5f0170abac8 | -10.6829 | -54.1475 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d71fb8ab-b2eb-3fa1-9c43-bbdc70c2fbe1 | -10.876 | -50.8163 | 2026-09-16 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5413a185-ff06-3781-b526-0d8d02a8eb8d | -1.6206 | -55.5679 | 2026-09-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0f057a56-09ec-3fd9-8440-702abb846019 | -7.3561 | -44.4956 | 2026-09-16 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 977aa907-0d89-3cd1-9195-5e39388e0928 | -11.2578 | -43.4621 | 2026-09-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| e94f46d8-29ad-3859-ad41-40d3c1922010 | -9.7909 | -45.8782 | 2026-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| c626fe26-db32-3f11-b545-62c7dfc9f1c5 | -12.6821 | -54.7174 | 2026-09-16 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c4a3b803-4489-355d-8d8f-1cac00f35076 | -11.2117 | -42.8275 | 2026-09-16 14:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 146.2 |
| 8e674324-15f8-37e8-96e4-458ddef5c5a2 | -7.8654 | -55.4446 | 2026-09-16 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b7736ad3-89c9-3b76-b6d7-a2338ba5c785 | -1.6022 | -55.5682 | 2026-09-16 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 96c9f161-1020-3aa9-a99d-5532f17434dc | -11.8941 | -47.5876 | 2026-09-16 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0eed4c24-a558-3db1-a0fd-4e549bf4e8ea | -10.9108 | -48.3739 | 2026-09-16 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1ec178fe-5e10-37ae-817d-355a6c3552ce | -6.8032 | -59.1693 | 2026-09-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 389.2 |
| 188b12c7-c23e-3e45-a3c3-3e13947044cf | -10.3953 | -58.3159 | 2026-09-16 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 289.8 |
| 6c9faeaa-401d-37df-bdbb-73105637d079 | -10.3766 | -58.3171 | 2026-09-16 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 83a37609-dc77-307a-911a-9608b87c0cf8 | -12.1265 | -44.199 | 2026-09-16 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 41cb2121-af20-3526-b97f-cf5651ebe43b | -8.5617 | -44.5112 | 2026-09-16 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 388.5 |
| 7a95a3a1-0344-3975-a9c8-f7aea909be17 | -10.7267 | -46.7332 | 2026-09-16 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| a73244f0-16d0-35ed-a799-174ca7075e1f | -6.1177 | -59.9069 | 2026-09-16 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6b493bbc-5e0e-387c-8ea4-fe768b62e3fd | -14.4479 | -40.8379 | 2026-09-16 14:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 151.5 |
| bcbe533a-1866-3e52-89c6-4bc02ce1013b | -6.8216 | -59.1686 | 2026-09-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 333.8 |
| 50b59be4-93c8-3938-b7a2-dd55b89776b5 | -8.5428 | -44.5132 | 2026-09-16 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 557.4 |
| b85177e6-eb32-343e-9be6-9eb750e73238 | -11.9033 | -43.8112 | 2026-09-16 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| a8cbe385-0001-3d72-a099-deb226f5b73f | -12.4145 | -48.4701 | 2026-09-16 14:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| af3742ad-c950-349e-ba5a-f88c5ab07349 | -7.0428 | -59.2173 | 2026-09-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9f29c924-f097-338b-b563-2c444d0840fc | -9.7877 | -46.1045 | 2026-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 063174ba-5210-3f24-8378-8751b35fa9a6 | -13.2867 | -51.3046 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 916fac3d-441d-3a77-947e-50e8ef4ab8ae | -9.3893 | -60.3022 | 2026-09-16 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e23d7d2e-3c69-3a8f-95c0-f66de4491fbb | -13.287 | -51.2832 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 58badbf4-8b15-3a8d-9434-5637069ab358 | -3.7129 | -60.6022 | 2026-09-16 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 105f09cf-64b7-37f0-9c0e-af9e1bf8609a | -10.9111 | -48.3519 | 2026-09-16 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| cdb81fbf-fe84-3cb2-b037-fcd883f2c8df | -7.0242 | -59.2374 | 2026-09-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 671b2375-2237-3caa-a9a5-fb4e8a2b2521 | -10.8919 | -54.0062 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 56f7f149-6172-3aa0-a7b2-9698aa503d70 | -13.2678 | -51.2856 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 4af94061-c58a-3086-ae6b-4aff756aa87f | -12.6826 | -54.6763 | 2026-09-16 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 55f67600-1ad2-3bce-a76e-c16ede9096f1 | -12.1453 | -44.2195 | 2026-09-16 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 0215c4d7-68f4-3a85-b3e5-064b20c433a7 | -5.6611 | -43.2272 | 2026-09-16 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 46b576fc-9522-3a6c-b360-e5acc36fc48b | -10.0293 | -52.12 | 2026-09-16 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 178.7 |
| 867fc232-0807-37ba-8b1b-e20663a139ce | -3.1174 | -57.6779 | 2026-09-16 14:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| abff9a09-7f32-34d4-9626-935d642947b8 | -6.1178 | -59.8877 | 2026-09-16 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 08e1ade4-7d61-3b09-bf5e-7d4ac11de1bf | -8.5431 | -44.4902 | 2026-09-16 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 09f3e4c2-77ae-3360-9377-6c30e737ad15 | -13.5127 | -51.5532 | 2026-09-16 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 89a400bc-372a-3791-80fa-01bb655510e7 | -6.7839 | -62.9782 | 2026-09-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| db7287ba-c495-3fc0-b8df-b71cee484652 | -11.9715 | -52.4715 | 2026-09-16 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 3f1e5585-9363-3357-a421-7174dab2304f | -9.2311 | -46.7055 | 2026-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 2dea27cb-58c1-3d92-8269-2b4bb2efe260 | -12.126 | -44.2225 | 2026-09-16 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5bea6ea3-3409-3c78-91e4-ec26b4525a80 | -15.3804 | -52.9227 | 2026-09-16 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4a791b7a-5c44-35c2-9e1b-b9689e0700b2 | -10.3955 | -58.2962 | 2026-09-16 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 4bd519af-0dd2-3baf-bebf-825aa9ec919b | 3.8957 | -60.6174 | 2026-09-16 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c951fd4b-8684-3d3d-bf40-5e9b8a3cbd20 | -9.7608 | -60.4561 | 2026-09-16 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 753bda8a-d8f9-3d82-a35f-d0a700d9aff7 | -10.9105 | -54.025 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 988652c2-dca5-30a2-9e45-421f0069bc06 | -3.4461 | -58.0005 | 2026-09-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2d708ec6-80b6-36d0-8efc-d994b8e9e75c | -11.5436 | -46.852 | 2026-09-16 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8434cac2-c2b2-3df8-9e4d-68931f91a5f7 | -10.9107 | -54.0045 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| b8af7f38-9f66-3861-8055-1781a9ddc01c | -13.3754 | -51.7406 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 060bbb1f-8b00-35c1-8bad-17c52f35748a | -2.7149 | -57.608 | 2026-09-16 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| bd3c3ebf-f6fb-37a7-8491-8851eb8d3d76 | -10.8916 | -54.0267 | 2026-09-16 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 87e9ef1a-be8d-3fca-b9d9-5186f6170e9e | -6.7705 | -48.6577 | 2026-09-16 14:30:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 0774e3d6-e3ea-3045-b539-92e39a407b4d | -10.0295 | -52.0991 | 2026-09-16 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9744664c-2f09-30a6-b558-3ee99e552183 | -13.2874 | -51.2618 | 2026-09-16 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| bf0ef7ab-2101-3e93-9433-26a13ffedd8e | -11.5624 | -46.872 | 2026-09-16 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e63b3ba7-c54e-311a-9ca3-71ff6e8c0fcc | -11.4167 | -51.4371 | 2026-09-16 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 0e0bfdd4-3bf7-305f-8828-a5c6755e7d6f | -11.2386 | -43.465 | 2026-09-16 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| ffa43934-2ee6-3c08-89a2-2377277492e6 | -5.144 | -55.9345 | 2026-09-16 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 55ad15bb-c2c0-37fd-9713-a204aeb0701e | -12.6255 | -50.7667 | 2026-09-16 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 2ea1ae74-dc29-3b05-a526-67155c1556b5 | -10.1179 | -45.5662 | 2026-09-16 14:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 185ae2d6-ff83-3047-87d4-b3f5741e3570 | -9.8099 | -45.8759 | 2026-09-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 24fe5675-0172-3fce-bebb-390123ba394b | -6.6021 | -58.849 | 2026-09-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2aabcd11-1928-35da-9a5f-02357e779b43 | -9.3892 | -60.3215 | 2026-09-16 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0d803d33-f463-3638-b912-4750f63413c0 | -6.75 | -58.8043 | 2026-09-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| b773669d-e75d-3d4b-bdf9-39503b710835 | -9.2308 | -46.7278 | 2026-09-16 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| eb9273e7-8d19-3120-8de7-60108dcf8c73 | -12.6628 | -50.8264 | 2026-09-16 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 58c25657-ffd2-3b78-b501-f3c3a3f38f2c | -6.7684 | -58.8035 | 2026-09-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 18c75e2f-d4a5-331f-8ee7-c24f2b381d31 | -13.3758 | -51.7193 | 2026-09-16 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 87c52135-4cd0-34d9-b2a6-4c689c1d5dcb | -6.8579 | -62.9007 | 2026-09-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 6a8f7fef-8117-34a7-a06d-e31af5db577d | -10.8571 | -50.8183 | 2026-09-16 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a797c51c-6678-3619-9f10-048c23229cf2 | -11.417 | -51.416 | 2026-09-16 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6ce906d0-9c4e-31fa-b973-97d818b814e9 | -8.8456 | -45.8939 | 2026-09-16 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 6a2acfce-363b-32a0-8cd0-8d2d2e067e6b | -10.0104 | -52.1217 | 2026-09-16 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| fe00a100-2688-395b-a8ef-3c383bd263ab | -3.4645 | -58.0001 | 2026-09-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6acb001d-d848-3057-a57e-e6e922b79257 | -12.0488 | -47.4777 | 2026-09-16 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 271.6 |
| 690aedfe-fd25-3b9b-8b67-86a1ee7fdb71 | -6.5837 | -58.8498 | 2026-09-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dfaed639-a9a4-3a86-bf3e-dde6bf52e8ea | -13.3387 | -51.6389 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 487913ac-cb12-3e29-b0e7-54c7862ba6e3 | -5.144 | -55.9345 | 2026-09-16 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 51d5e0b1-679b-3354-aaaf-9110ca2883dc | -9.7877 | -46.1045 | 2026-09-16 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| df29c90e-66a5-3e00-ab14-753945a3e4ab | -3.1604 | -42.4386 | 2026-09-16 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 64359f5a-2405-316a-a196-4dfcd5b7b77f | -10.3205 | -49.9567 | 2026-09-16 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| fb1e8298-64a1-3e99-a28a-80254e080d9c | -10.9105 | -54.025 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 43ff15a4-fecd-3154-a23b-f7d447bd9eed | -13.3758 | -51.7193 | 2026-09-16 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a3580a79-5e5a-3436-9321-4b9453aec056 | -9.0866 | -61.0287 | 2026-09-16 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a560af7c-cabb-3843-bd2e-26b62056fe56 | -11.4905 | -50.2581 | 2026-09-16 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b92839f9-28ca-31f3-93b8-1997311222b2 | -10.8919 | -54.0062 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| f1c2782c-ec66-3a6b-88e1-19be66d70e75 | -6.3196 | -59.9956 | 2026-09-16 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f2107b0d-d915-37f6-bdd3-1bd4803b81da | -10.876 | -50.8163 | 2026-09-16 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 70311044-4748-35d3-ad41-c21ed18a9210 | -12.1265 | -44.199 | 2026-09-16 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 06444d99-514e-3bfb-8b40-d1e1cab6dc98 | -10.3766 | -58.3171 | 2026-09-16 14:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1e52c08a-02d8-3363-8886-04305ef38bc1 | -15.6557 | -52.7366 | 2026-09-16 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 86397187-8b99-3879-9470-c5501968c811 | -10.6641 | -54.1491 | 2026-09-16 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |


[Clique aqui para ver as próximas entradas](README77.md)
