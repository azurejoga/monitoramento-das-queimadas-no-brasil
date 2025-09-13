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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe32cd7a-6e9a-32ce-b7ce-fd91231d4bab | -9.4819 | -55.9601 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a3bfaebb-42db-3288-8497-6cbd96c2085c | -13.9379 | -48.2076 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ac905199-d849-3cc2-b1b5-f7c79754ad9c | -7.5269 | -44.3644 | 2025-09-13 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0c74ead5-c770-3f60-b384-2e5fb69c4732 | -12.0682 | -51.0465 | 2025-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f434cdd1-726e-3bed-a03a-9618c3d32a53 | -11.1498 | -45.294 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8813bd24-db77-3662-bc81-9db92c819996 | -14.4939 | -53.8973 | 2025-09-13 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 53914e0b-ca20-344a-b302-956080848e0c | -13.2535 | -43.752 | 2025-09-13 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 0356ad8d-f628-3306-b105-29db7b5fdf86 | -9.8646 | -50.1951 | 2025-09-13 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c0fb7bc8-7338-38df-8ac0-c11e7ecca011 | -7.3954 | -44.3539 | 2025-09-13 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 33181b55-27d0-3ba2-a32f-8b5e98cc94db | -13.49 | -51.7688 | 2025-09-13 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1561f93e-4b08-3a6f-a6ae-5e6aae684b02 | -15.8845 | -47.2286 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 4acaad30-f97a-36e2-8073-f56cf2c144f2 | -12.1044 | -47.5816 | 2025-09-13 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 208ee031-7bf7-3026-8ff3-32f1b15866a3 | -14.4588 | -47.3174 | 2025-09-13 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| aebec71e-e133-3ffe-affb-d4bbaf92b139 | -16.0796 | -49.993 | 2025-09-13 14:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 55ecc1f7-7c2b-3b51-8ae1-f18a2ae27689 | -9.9757 | -50.3548 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a2172425-8444-3c08-a5c9-aa552f7f04aa | -14.7176 | -55.6295 | 2025-09-13 14:20:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ec32b138-cfcf-3006-a130-89d32d464093 | -10.3397 | -49.9333 | 2025-09-13 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8693fba8-b319-3c11-b12e-16209b75c1ce | -15.1165 | -52.4918 | 2025-09-13 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| b157a732-9d93-3a71-977a-16744fda3088 | -10.5295 | -49.8704 | 2025-09-13 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1841e898-6c87-32fe-bb02-1e75c07484d0 | -16.4906 | -55.1276 | 2025-09-13 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 175.5 |
| 479f9f75-3104-380a-9646-4f004fa07e5b | -15.6013 | -54.7613 | 2025-09-13 14:20:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 07cc81e8-4ef1-38ce-a422-18257904d3bf | -15.1363 | -52.4679 | 2025-09-13 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3f63c1ad-d385-3d44-ae17-70c0b72ef982 | -5.1746 | -40.9545 | 2025-09-13 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| d6ec887d-f321-3eb7-a8c3-89e3ddae7db9 | -14.4133 | -52.9221 | 2025-09-13 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8b9107a5-11f2-3a6f-b2ae-71c359a10145 | -11.7579 | -46.5979 | 2025-09-13 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 279.3 |
| bf62d156-1f20-34cf-b4a0-4d5dccdf335e | -9.2505 | -51.2261 | 2025-09-13 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d9343b16-0097-3b61-be27-596219ae5100 | -13.9172 | -48.2775 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 427eb1b2-4ac0-31ce-b81a-1675ad233985 | -12.8263 | -47.9263 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| ffc87d7b-3e8b-3876-a74e-05896be03f78 | -9.9946 | -50.3529 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 50f3b6f7-782b-3f5a-a88d-cd536a09f0b6 | -13.9366 | -48.2745 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 3a7d8900-c971-3c58-8af8-d84b26233d87 | -10.8785 | -45.5597 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 203a8975-8ace-31c0-be5b-682028b4680b | -9.976 | -50.3334 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4bcd3533-4089-3ea8-b52d-cf7cbe25ab11 | -11.3117 | -50.8122 | 2025-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4bb10873-c00e-3ecd-98fb-94bfe92afec1 | -9.2472 | -59.4007 | 2025-09-13 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| cd47c719-2f89-37ce-82a2-365543152b71 | -8.9749 | -46.1054 | 2025-09-13 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 205.0 |
| e3dc99ee-6852-3457-80ae-33da0b86cc78 | -9.9948 | -50.3316 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0c73df82-8e0c-3133-a92b-3f628a7e7c4f | -10.4438 | -50.6272 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fc8b5491-b15e-39a7-99ea-ece26455c222 | -15.1169 | -52.4705 | 2025-09-13 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4b8bf70f-783c-321c-a4ac-d09b7afbd1b0 | -16.4903 | -55.1484 | 2025-09-13 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| e96a4063-9591-3d78-9535-6e9a48f9eab7 | -10.4441 | -50.6059 | 2025-09-13 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 857128f1-c95c-3919-b44b-ac67fe123fd0 | -11.3835 | -47.3206 | 2025-09-13 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c810deca-d0c0-391a-87ff-b67e48f51d27 | -14.4327 | -52.9197 | 2025-09-13 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| f1c79b04-3924-3b40-afa8-d3747911fd29 | -13.8979 | -48.2804 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 84b6bf00-49e2-3cbe-834c-3163977739bf | -14.29 | -46.0924 | 2025-09-13 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 156.4 |
| c46d334e-a987-32d5-870c-0389d02009e7 | -12.998 | -47.9908 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 858eaae2-3fda-3d4d-9d27-8b6151e241aa | -12.8452 | -47.9459 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 5c6a775c-316b-3d33-8ec4-7d8c3d310611 | -15.8648 | -47.2322 | 2025-09-13 14:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ff4888c6-ac2d-357f-9e75-c0593fb833e5 | -18.0466 | -45.418 | 2025-09-13 14:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 177.5 |
| a7702e64-099f-3815-97a3-482692bf8e27 | -8.9979 | -45.7871 | 2025-09-13 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5b82ff88-a996-3a3f-8043-fe2e14fedb97 | -12.8649 | -62.1268 | 2025-09-13 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 156a8b2e-1c8a-397a-a18e-1334d1373516 | -11.1152 | -51.3211 | 2025-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d489ac14-1930-32ef-9e69-fe02cc76d53a | -11.8698 | -46.7627 | 2025-09-13 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 671dc265-2973-3b4e-b6b3-5e63c4a557b1 | -12.9294 | -54.7333 | 2025-09-13 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 191.5 |
| ab1c94db-95ba-3eb3-b5da-d9576e40673d | -8.9982 | -45.7645 | 2025-09-13 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9b951dc2-231a-3e61-b28d-f3a2a4560b70 | -8.9365 | -46.1545 | 2025-09-13 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 57346e65-191c-37c2-8f7f-568032fb4801 | -12.8456 | -47.9236 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| cd156b35-33eb-3358-a582-13ed1c21af1c | -11.7391 | -46.5779 | 2025-09-13 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5d657a0c-16d9-338a-82da-0c1d749f0cca | -14.2088 | -46.2669 | 2025-09-13 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 30208c52-7012-3034-be86-ed3a6d776406 | -14.1703 | -46.2505 | 2025-09-13 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 129.3 |
| b402b1ee-ffdc-3a33-b36d-e6a4471f7b42 | -19.3508 | -44.798 | 2025-09-13 14:20:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d0ee33be-eb79-36cf-b798-39208c0c7706 | -16.3422 | -51.5217 | 2025-09-13 14:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1c825ee8-eb8a-3f94-8d08-519cdd5169b1 | -10.5484 | -47.2242 | 2025-09-13 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 530350e7-bf72-3c0d-ab2d-523ab890f6be | -16.5679 | -55.1801 | 2025-09-13 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| fcb54d39-665a-3483-96f4-005e1537a5de | -11.8853 | -50.5554 | 2025-09-13 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6127fd48-7a9b-3b62-ac51-827eab73793c | -16.08 | -49.9709 | 2025-09-13 14:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b6e26356-3aa8-34cb-887c-4f44e216872d | -5.1934 | -40.9531 | 2025-09-13 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| c0f802aa-5312-3c48-83ec-f3356c486519 | -11.2882 | -51.1334 | 2025-09-13 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| acb6ce0b-cbff-35bd-8534-505371a4b93e | -11.0953 | -51.3866 | 2025-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 0016b217-fe31-3fbb-b51c-1d7b443015a2 | -11.1237 | -50.7049 | 2025-09-13 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 9ada13ad-00b4-3077-8d8b-92272d42e8aa | -12.9787 | -47.9935 | 2025-09-13 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 50e034ac-cd67-3f80-b30f-98828fb2c18d | -13.9185 | -48.2105 | 2025-09-13 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| bb73136e-0ad0-3469-ac77-dbeded1881ee | -9.0169 | -45.7851 | 2025-09-13 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5006dc7d-6518-3e49-b5b4-96a72f9576ae | -18.0065 | -46.9499 | 2025-09-13 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 290a27fd-90f1-3636-b0fd-77096893af01 | -22.1964 | -49.6194 | 2025-09-13 14:20:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| 059fccee-84ca-31b6-b8e6-71def62d4d35 | -14.5244 | -53.2027 | 2025-09-13 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f557de6c-bceb-386d-9382-e46da3ef6213 | -10.3361 | -48.8106 | 2025-09-13 14:30:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 74846755-3b0b-3932-8d0a-286a39710466 | -7.3954 | -44.3539 | 2025-09-13 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 4f5e389e-b05b-3c27-b25d-ac42557f415c | -12.0498 | -51.0061 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d3b64d14-524a-3790-b47c-cd4c5aac101d | -11.7204 | -46.5579 | 2025-09-13 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 7f694b5f-c2ed-3fe2-b235-315dc3cba383 | -13.8979 | -48.2804 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8ea24939-e921-34b9-91e4-2b4dd352ba69 | -11.3835 | -47.3206 | 2025-09-13 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e49e2e1e-655c-36ff-99ee-b56e694e7713 | -12.0314 | -50.9656 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ece4bdb7-06c0-3dec-9159-3fad0acd768a | -10.8567 | -48.1827 | 2025-09-13 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 016d959a-9330-3ab8-af5e-ef3e5f1db399 | -11.7703 | -50.6115 | 2025-09-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d622b054-4edc-3716-9049-7ecc18c1afdd | -12.9482 | -54.7519 | 2025-09-13 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 4921f86f-9fdd-3afd-bfb1-7c8ade3fe3a2 | -15.8648 | -47.2322 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 71f05a13-82cb-30e2-a16f-5d9c87ae8208 | -15.4713 | -47.3256 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| e1524dc7-bbc1-36cc-8f73-4db6d41e09f7 | -12.9402 | -47.9991 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 074bcbbf-1579-3881-abf6-8bfd1272cfeb | -15.6013 | -54.7613 | 2025-09-13 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0a5fd093-4064-3599-a3e0-b051ca3846e7 | -12.8647 | -62.1461 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 157.0 |
| dabb7d2d-128d-338a-a8f2-58198bd3553a | -13.9379 | -48.2076 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 3bab26fa-2ea2-3536-a871-f247b4a47b12 | -9.4819 | -55.9601 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 02a18e21-56d4-3fa7-806b-ce59c4ead89d | -11.2882 | -51.1334 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 244.4 |
| d7621305-33ee-3b96-b8c1-ef68600761c5 | -22.1964 | -49.6194 | 2025-09-13 14:30:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.8 |
| b430f24d-6f20-3593-b367-318d255a466a | -16.5666 | -49.2247 | 2025-09-13 14:30:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 3dbf37f7-1eab-377a-aa39-70cafa0412cc | -15.4517 | -47.3291 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 8ed29851-ceb8-348a-a900-3751a70b33d4 | -12.8452 | -47.9459 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| db5e7358-7e36-3023-9538-de617e0115d9 | -11.2695 | -51.1142 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ab39232a-8550-3bed-90ae-510846dfed1e | -12.9101 | -54.7558 | 2025-09-13 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 254e3357-b37d-3fbb-8f03-79a9f3bd9544 | -9.9951 | -50.3102 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |


[Clique aqui para ver as próximas entradas](README134.md)
