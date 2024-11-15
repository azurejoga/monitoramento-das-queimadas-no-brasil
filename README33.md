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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 099dabd6-b70c-3bd7-832d-f4346a652641 | 1.29932 | -60.41157 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ae14620-19f2-3a2f-82c8-aa0ab90c1186 | 1.29976 | -60.41441 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55a8fbf5-f591-394d-b918-35b617c717af | 1.30429 | -60.41076 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 237aff39-2d3e-3f0b-88b3-e955cec44d92 | 1.29887 | -60.40871 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55a5a35a-0f58-3966-864d-5aa1e8672b33 | 1.29799 | -60.40304 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba889bc-f779-36e4-947f-2d5230a0136f | 1.29843 | -60.40587 | 2024-11-15 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74a959cc-e29a-3215-866e-a9a4ba40fa4d | 0.4325 | -50.9203 | 2024-11-15 06:00:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 01ab0c11-9edc-37aa-aa6c-618922a53dee | -8.83777 | -63.02961 | 2024-11-15 06:03:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a561cbd8-3e45-3a39-a090-dafd2be7c9a4 | -9.53167 | -66.63158 | 2024-11-15 06:03:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d259c6dc-93ab-346f-94ae-47eb43d92e6a | -9.59865 | -63.22148 | 2024-11-15 06:03:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6e5f8b1-0417-33de-8faa-ccc6e40c235a | -9.61772 | -66.29998 | 2024-11-15 06:03:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b6d2e67-a45c-3304-bbf7-05768c16115b | -9.53706 | -63.56897 | 2024-11-15 06:03:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed440fcd-23fc-346d-bbe0-2cacb5a368cc | -12.79796 | -62.0107 | 2024-11-15 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 675b4a62-afbf-3dad-b8f3-72c77b8219d2 | -9.5337 | -66.63033 | 2024-11-15 06:03:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775361f4-0304-3bd8-bdbd-9aadfa4e2a84 | -9.59073 | -63.43085 | 2024-11-15 06:03:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96e98fb9-356a-3b1f-9e9e-1acee93035e7 | -8.83477 | -63.02715 | 2024-11-15 06:03:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1a4b57a-ecb2-3508-acb9-66ffd261eb17 | -16.01849 | -59.38178 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f38516e9-8a87-37dd-aaff-543d2641fd7f | -15.89628 | -59.27417 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f066292-48c0-3d12-b66a-9ef5390b7f8e | -15.47959 | -60.04996 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11306d53-b51e-3d03-a39d-30cba94cf572 | -16.02351 | -59.40047 | 2024-11-15 06:05:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 929bee8c-7ba8-3f80-9377-e48348eb801d | -16.02404 | -59.39494 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8609879-eaf4-38f0-8016-35dad56d9d44 | -16.10169 | -60.09606 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3a6bcdc-2c78-320a-ab93-312780d42270 | -15.47316 | -60.04922 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f21f1ec2-82bd-3184-bbbf-5e822a3048c2 | -16.10054 | -60.09701 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c68a92d2-b8b4-3843-98b2-1cb6e50a00c3 | -15.88916 | -59.27731 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7344f9e0-129e-3776-b150-23df42a3d698 | -15.89386 | -59.2745 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| daac4482-9d9b-3cd7-826a-ac080b40b831 | -15.48106 | -60.04905 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69993092-cf3d-3597-9b58-20946dcad26f | -15.47463 | -60.04828 | 2024-11-15 06:05:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d6c63d4-902f-320e-bb04-f3da5053bc56 | -16.02459 | -59.38923 | 2024-11-15 06:05:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 480209a2-12f4-3e95-9c0d-095a41f169a6 | -2.96894 | -53.85484 | 2024-11-15 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| c5f40394-80bd-3c2a-a252-75b2aae5f92c | -2.98039 | -53.85653 | 2024-11-15 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 810d08af-89b6-387b-b551-b2ae3f53a6b1 | 1.30072 | -60.40674 | 2024-11-15 06:14:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 7d30bcb1-dfa8-366a-8dda-7a3dbe589d7e | -3.23539 | -54.15682 | 2024-11-15 06:14:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2d4c18c3-bf4a-35e7-ae7a-8cc02ab3775c | -2.84821 | -53.97185 | 2024-11-15 06:14:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| ff878014-6d90-310a-b8d4-0ef1906abafd | -17.24075 | -57.45484 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| a741fb49-1445-3565-9f99-4f86ca2cff65 | -17.55114 | -57.52859 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.7 |
| ca077e7a-15e8-3405-ae48-7679aa903720 | -17.57113 | -57.54585 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| ee518455-f6a2-3deb-a25b-a0ebc5fbcd42 | -17.57856 | -57.48818 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| b24f1963-2b01-3842-99b4-592146925c7b | -17.57077 | -57.56738 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 70952f1d-034c-3011-bda8-d4845bba4d91 | -17.62889 | -57.54595 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| c867b4bb-d9cf-3e3c-8dbd-c3abfa50d4ef | -17.24989 | -57.47066 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.7 |
| cd3d997e-600e-3db8-8c0e-5bca4a542a9c | -17.58167 | -57.56883 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| ce3a7ecf-72df-3e28-96a2-5ea58a28af50 | -17.57428 | -57.53867 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| 0ed5f35a-5ed6-38e7-8151-e446e7403391 | -16.94533 | -57.62561 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| c329e52c-8835-3133-8e8c-5a2661a9ccda | -15.31173 | -56.51052 | 2024-11-15 06:18:00 | AQUA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 98a4d927-a2d9-3257-a7da-36f8ad812165 | -16.94359 | -57.63945 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 710f8f0e-ed67-3c59-8ee3-359d68b01dda | -14.285 | -57.63655 | 2024-11-15 06:18:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 55bec0a5-4419-3ed4-b063-89f519386223 | -17.56928 | -57.56018 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 23a14e72-d0b0-3b62-9d35-16f22cbf9125 | -17.57298 | -57.53148 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e3a3263e-3062-300c-b69a-138a2b7a41ba | -17.24254 | -57.44043 | 2024-11-15 06:18:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 35690944-5692-3966-a842-b0fb7621b7e5 | -16.10246 | -60.09779 | 2024-11-15 06:18:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa86eff0-4012-3547-98fa-d05791765e92 | -17.57253 | -57.55304 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 9afcebb3-2d70-38c1-b4c4-b44b03325e4d | -17.5639 | -57.51564 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| 46ebc835-a81f-3246-80f2-99f2d2fe668e | -17.61796 | -57.54449 | 2024-11-15 06:18:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 73af878a-a215-3eec-83d6-f16302566768 | -2.8534 | -53.9915 | 2024-11-15 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6a16fb4f-6dac-3356-b030-312f6a43ebd7 | -2.6596 | -46.1843 | 2024-11-15 06:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2368eda9-d1f0-3eae-89a4-443c7b86634b | -2.8535 | -53.9714 | 2024-11-15 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6cd9fb69-bd48-36a2-983f-0b934a803f4c | -2.8534 | -53.9915 | 2024-11-15 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 463a916f-eb52-3432-8445-8b86197048e4 | -2.8535 | -53.9714 | 2024-11-15 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 348f28db-99e1-397b-a1e1-c39e8861c4eb | -2.8535 | -53.9714 | 2024-11-15 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 656ec801-2c21-3de5-b9c4-e469d341469a | -2.8534 | -53.9915 | 2024-11-15 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2a6922a5-218a-3281-9593-28782844ec6b | -2.8351 | -53.9718 | 2024-11-15 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| fcfe1a27-cacc-35ae-b2e2-62be73ca11e6 | -2.8534 | -53.9915 | 2024-11-15 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 28573215-012e-315a-bb1f-ab5e5dc2b217 | -2.8535 | -53.9714 | 2024-11-15 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cfa5f643-a29e-3245-8087-4b011c6d9482 | -2.8534 | -53.9915 | 2024-11-15 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 758e4b1e-fc4f-38d0-a9cf-49ec626b9b1b | -2.8535 | -53.9714 | 2024-11-15 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6b07d720-0689-31b9-808f-2efb2372c3f8 | -2.8535 | -53.9714 | 2024-11-15 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4fc4b08f-d880-3980-a1c3-331f6f7ffb69 | -2.8534 | -53.9915 | 2024-11-15 07:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 99526349-9847-340f-b8fb-56edb5453dc0 | -17.5672 | -57.5557 | 2024-11-15 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 131a9ffc-b4bb-3b38-b6a0-90f3d4a135b2 | -2.8534 | -53.9915 | 2024-11-15 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9c71b9f0-aedc-3937-b04f-b79aa5938bba | -17.5869 | -57.5533 | 2024-11-15 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 112a8f35-ad97-3435-ac0f-fefee1da0975 | -17.6263 | -57.5486 | 2024-11-15 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| cb26a7e2-2bad-367d-980d-4eaa95d677ea | -17.5865 | -57.5739 | 2024-11-15 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| a685931d-e1b0-36b5-87a3-70fed536700d | -2.8535 | -53.9714 | 2024-11-15 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b5bd7380-2cdd-35df-9b14-4fd54684b43e | -17.5675 | -57.5351 | 2024-11-15 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| ead8ca50-0c07-3fdb-a136-501f649ae2ad | -17.5869 | -57.5533 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 1fcb348b-17a2-3258-b7ce-9455c3265e5a | -17.5478 | -57.5375 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| dd203bca-823c-34c7-8129-cede5e33bd54 | -17.5882 | -57.4711 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| aff3d7f1-cb96-3b43-ab37-7c927a132e66 | -17.5672 | -57.5557 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 27e4f97e-bdfe-332f-a62d-c6b1049040fe | -17.2547 | -57.4493 | 2024-11-15 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 610990ea-f778-3b93-a87f-12f610b74c40 | -17.5879 | -57.4917 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 87308a18-9890-3b89-a8f0-cf0454f99d40 | -17.6263 | -57.5486 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 92a59575-33c2-3118-bb50-790a680ac63d | -17.5865 | -57.5739 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| bb48430c-9798-375a-b543-f6cf0dfcdade | -17.2543 | -57.4698 | 2024-11-15 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| fdf57d1c-da7c-3f0a-95f7-8a23ac575e43 | -17.5675 | -57.5351 | 2024-11-15 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 50f2fd21-b4d3-39b9-9fdc-e68e75362837 | -17.2543 | -57.4698 | 2024-11-15 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 375df424-421a-38eb-9301-526d2dfb4550 | -17.5869 | -57.5533 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 38490b92-fe6e-3ccf-a8f3-3ade0fafd38b | -17.5675 | -57.5351 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| d898767b-4f00-3fd0-831c-10a7dc7a45bb | -17.5882 | -57.4711 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 155dcb9a-a419-3c4f-98a3-99254af3a917 | -17.6263 | -57.5486 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 7a546365-a5aa-37ed-be5f-5dbc900a422d | -17.5865 | -57.5739 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| e6cb3bee-6219-3fbc-83e7-1922b5630b03 | -17.5672 | -57.5557 | 2024-11-15 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 0821a95d-4655-3ef5-a399-6d149306f09f | -17.2547 | -57.4493 | 2024-11-15 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| e9b861f9-5937-304f-8548-4d7d2b07e684 | -17.5672 | -57.5557 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 315c6e0e-2254-3451-96af-901fabf9214a | -17.2543 | -57.4698 | 2024-11-15 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| fe62ab84-1693-3fae-8a27-052bba587acb | -17.5869 | -57.5533 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 7befb8ac-f20b-39ef-940b-e74682d62181 | -17.2547 | -57.4493 | 2024-11-15 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| d5019d09-fac7-3a5a-9c50-761a6db66fa6 | -17.5882 | -57.4711 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| c0be69ac-fb75-3043-b198-1e6fe0074eb4 | -17.5865 | -57.5739 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 6b311dc8-d720-39d9-bc2b-393a2d65d9db | -17.6263 | -57.5486 | 2024-11-15 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |


[Clique aqui para ver as próximas entradas](README34.md)
