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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f8af380-4048-3e42-9759-098b6dd10d21 | -17.57762 | -57.5558 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 199.8 |
| 6a5a09e3-7f28-39ca-9ea8-9c0b32598379 | -16.02282 | -59.39312 | 2024-11-15 01:19:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b63dbd0a-b655-3668-b20f-e11487a8a532 | -14.28043 | -57.64111 | 2024-11-15 01:19:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 00e2f34c-c780-32a9-8448-af7dabb547c7 | -19.77333 | -55.40581 | 2024-11-15 01:19:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d537b28f-3a51-382d-879d-86d5b3f79f17 | -16.94707 | -57.6334 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| c377ae4b-49ff-390e-beac-e76dfc02ea4e | -15.31928 | -56.52095 | 2024-11-15 01:19:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9ced423f-bf19-304b-9135-790eaa831214 | -15.29929 | -56.5237 | 2024-11-15 01:19:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4f1f25b2-0faa-35a6-929a-0a83feba9973 | -16.95989 | -57.64683 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 5777e8b7-e6f7-3df4-9556-fba07fee9453 | -17.57591 | -57.54082 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 5226f20a-b8cc-312c-bbc0-52a7e2e6b0f8 | -17.70221 | -57.54948 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.3 |
| 6541247c-a323-3cfd-8d20-66c80e6cf076 | -15.30078 | -56.53543 | 2024-11-15 01:19:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00d7fe56-2e44-31cb-97cf-fe81e801963d | -16.13013 | -54.02737 | 2024-11-15 01:19:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c103ca57-e84d-3b34-9a49-3f5b4a336e83 | -15.40469 | -58.61769 | 2024-11-15 01:19:00 | TERRA_M-M | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6f969a2d-496e-3047-9d7e-4f150f66e880 | -16.10304 | -60.1016 | 2024-11-15 01:19:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ba75516f-d640-30a4-b542-514765c4b7e6 | -17.5742 | -57.52588 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 8614a8fa-8cc1-3a00-814c-e254b9aad26e | -15.28931 | -56.52513 | 2024-11-15 01:19:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c373e193-ee37-3c8b-bbff-a7dae3fc6471 | -17.73028 | -57.50027 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0bf54426-6958-313d-b22a-8ec7a62925db | -12.32638 | -57.74784 | 2024-11-15 01:19:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b97a45f7-3d8b-39e3-9dd9-3a368cdff1a7 | -17.59295 | -57.49327 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 041f2018-2603-33e9-ae9e-beed9abc2984 | -14.28466 | -57.63434 | 2024-11-15 01:19:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 09b558f5-7ae0-3517-a7ed-a974091cd979 | -17.4031 | -55.18533 | 2024-11-15 01:19:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| c65abfcc-24a6-3fd3-8663-d15aee2717a3 | -16.95817 | -57.63198 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 312b0e72-70cf-3d95-99a1-0aae41cd9ec3 | -17.23458 | -57.45889 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 5453c86e-6be4-303d-8068-1a6e56a54cc9 | -17.56309 | -57.52729 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| cd213c91-288f-3638-88f6-4703edbdf2a6 | -17.24558 | -57.45748 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 182.1 |
| 29404d48-c2b4-3c03-a4d4-d5b16ebf5aaf | -17.6023 | -57.47703 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 4b10ad73-da15-3426-98a8-e274c3ce12ae | -17.56648 | -57.55721 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| b16098bf-045b-3f4c-95e5-45a2de794a0e | -17.57933 | -57.57081 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 940.9 |
| cf7d178b-8bad-3dd6-aad4-c9821789137d | -16.02416 | -59.3871 | 2024-11-15 01:19:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 07e823ce-4b28-3475-a275-ffcdde34da4a | -17.22567 | -57.1995 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| f31d82b6-4007-3eab-85d6-061776973426 | -19.77482 | -55.41766 | 2024-11-15 01:19:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| fff1b68e-2a59-37cd-a78d-a14a78e35c81 | -17.65852 | -57.46413 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| eee65617-2efd-3c37-b093-ffcc674725a3 | -17.56819 | -57.57225 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 163958f2-de71-34af-91c4-03ded93f5d05 | -16.94879 | -57.64825 | 2024-11-15 01:19:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| dc7e6b23-2d65-3730-aa9f-215d28c56e20 | -17.64301 | -57.44184 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| cb7b0ee0-eaee-3b2a-bda2-4156c2501847 | -14.28627 | -57.64771 | 2024-11-15 01:19:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 69127b38-4a86-3989-a991-5ba9c921e69f | -17.57674 | -57.45028 | 2024-11-15 01:19:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 31023cf0-2751-3494-b7a2-99185a0dfcb2 | -15.30928 | -56.5223 | 2024-11-15 01:19:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8a50f055-8857-3a1f-a0b6-213620cfe52b | -3.27446 | -53.0162 | 2024-11-15 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cfcfac07-55ef-3230-bb91-474e3951903b | -3.71984 | -54.45541 | 2024-11-15 01:21:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 21a9822c-aa2a-3e63-94c4-d77d446dcb82 | -2.33493 | -46.87644 | 2024-11-15 01:21:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b2a2faf7-09b4-3d1e-ab74-44361064d927 | -3.34299 | -53.28841 | 2024-11-15 01:21:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d69d6520-4c74-3dad-b9f0-fcc876cc9e92 | -2.3273 | -46.87221 | 2024-11-15 01:21:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 1063a357-2949-3fd8-bf27-2c21e3ac702c | -3.72888 | -54.4541 | 2024-11-15 01:21:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3999dcbb-e2d2-3174-a505-024c57d2f832 | -1.84425 | -53.69128 | 2024-11-15 01:21:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b98176c5-2517-353d-b652-1dfc1173c304 | 1.59214 | -55.86534 | 2024-11-15 01:24:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 615dee91-f62e-3107-a8ee-f5fc41b94a6d | 1.2996 | -60.40142 | 2024-11-15 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 37568499-f685-3226-b96b-5f518c8799a5 | 1.05471 | -60.60701 | 2024-11-15 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d748fcd7-3b61-38df-a0de-b0ca40ed1957 | 1.04899 | -51.09111 | 2024-11-15 01:24:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c9444b1f-503a-3d96-8c88-019fb3017e2d | 1.29789 | -60.41357 | 2024-11-15 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| fd3768ab-4900-3923-8029-57aede2d6c4d | 1.05652 | -60.59436 | 2024-11-15 01:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4e8bc024-e886-3434-8257-cee16312e09b | 1.3035 | -60.4074 | 2024-11-15 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.9 |
| ecf17cc2-1ac4-397d-bf30-681382d7b5a7 | -17.274 | -57.4675 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 813cba1a-a3cc-314a-88f7-b93f36b74d16 | -17.7052 | -57.5392 | 2024-11-15 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 931bff19-7cb2-3864-a072-077ad2f03e67 | -17.7048 | -57.5597 | 2024-11-15 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| d0a9d4a2-c057-36c9-ab26-c80f57fd97d1 | -17.2347 | -57.4721 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| ebf5ffc0-a8ea-3fb1-ac10-f2c925f9a3e5 | -2.6596 | -46.1843 | 2024-11-15 01:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dfa84cba-da5a-3182-838d-27f113e5bcb7 | -3.7866 | -43.9241 | 2024-11-15 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| cc711443-09c4-3a89-9f85-8d0a6e464ba0 | -3.8054 | -43.9002 | 2024-11-15 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ab85ec4a-af99-3d7f-94a6-8189278a6940 | -17.235 | -57.4516 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 6569214f-5c49-30ea-bcb9-619d2cf1f43e | -17.5879 | -57.4917 | 2024-11-15 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 54c32fd9-d6b7-3e83-9198-4d1043361440 | -17.2547 | -57.4493 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 44b2479e-dce1-3baf-9b14-1c1abdb3f628 | 1.0765 | -51.1234 | 2024-11-15 01:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 45.2 |
| f5549a0b-f229-3dfb-997b-4c1a6c1650fd | -16.958 | -57.6269 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 897fe116-474a-3cfd-b744-5a6eb429b06d | -3.8053 | -43.9232 | 2024-11-15 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f5bfbc6f-5f72-3299-82de-646c144d751f | -3.7867 | -43.9011 | 2024-11-15 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 59c16bb4-7b8a-326c-9660-62a8e926023c | 1.0765 | -51.1441 | 2024-11-15 01:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4c54f807-a270-34e9-b190-4b6ded330083 | -17.2543 | -57.4698 | 2024-11-15 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.1 |
| d49a76da-2bbe-3c78-bcd5-769a7db46d53 | -17.5882 | -57.4711 | 2024-11-15 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| aa9ef0ad-5f5b-31a1-9072-775a365f2325 | 1.3035 | -60.4074 | 2024-11-15 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| edfae85c-9f1c-3497-a969-a8b763654420 | -17.274 | -57.4675 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 48449ae3-9e50-38be-94eb-05bb126fb0a1 | -17.5882 | -57.4711 | 2024-11-15 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 702fb28c-ffc3-3792-b9cc-cf85bd421faa | -16.958 | -57.6269 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| aa29bf85-2d9f-3521-9576-a52d63b7924e | -2.6596 | -46.1843 | 2024-11-15 01:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| f10b0dbb-2ada-3f66-84d1-bc79fbebee45 | -17.2543 | -57.4698 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.3 |
| 1909e98b-8e65-3f84-90ae-f4edfd9ced51 | -3.7866 | -43.9241 | 2024-11-15 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9b55b69e-720d-3e61-8ce5-6f5336b3adf1 | -3.7867 | -43.9011 | 2024-11-15 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 14aa1eca-75e7-3202-ae82-aa5e8d0057f3 | -17.2547 | -57.4493 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.6 |
| b1c371d2-da79-3fd1-8f69-5484471300cc | -17.2347 | -57.4721 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| b8476f4e-0e87-3123-b579-1fa744c22ec6 | -17.7048 | -57.5597 | 2024-11-15 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| ffd72c9c-d7f3-3a7b-bb1f-1e5adec92a7f | -17.235 | -57.4516 | 2024-11-15 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 032a40d7-e9c5-35d9-852b-a412a6c0733d | -17.6851 | -57.5621 | 2024-11-15 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| adaf90f9-c889-35e3-8591-307ac632e96e | -17.7052 | -57.5392 | 2024-11-15 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 2b986b87-7e35-3734-98b7-2e2a3bbe350e | -3.8053 | -43.9232 | 2024-11-15 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3394db53-2ee4-37a0-9498-243aa60ae3af | -3.8054 | -43.9002 | 2024-11-15 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0c15eb48-97d3-3635-8d8c-ae99302bd4ff | -17.5882 | -57.4711 | 2024-11-15 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| fc4d2664-7a90-3c35-ad1a-c5190ea2560b | -17.2547 | -57.4493 | 2024-11-15 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 2b1304d4-ee79-3f1e-b270-14639249ee77 | -17.7052 | -57.5392 | 2024-11-15 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| eec30ca0-1b4e-3ca1-ae57-d3e61cfa223c | -17.235 | -57.4516 | 2024-11-15 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 607b54f9-6058-3895-8ddd-7426ea3e058f | -17.2347 | -57.4721 | 2024-11-15 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 923ccb4e-97aa-3509-bb76-d40a20416804 | -17.5879 | -57.4917 | 2024-11-15 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| d8f32ccf-7ebd-3c35-a4c7-ca704488774b | -3.8054 | -43.9002 | 2024-11-15 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5ae76769-db5a-361e-877c-e4d47017a236 | 1.3035 | -60.4074 | 2024-11-15 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 61ae6cea-003f-3163-8dfd-67388b99d47a | -3.7866 | -43.9241 | 2024-11-15 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 58185c94-c95f-3671-9e44-1683d9d19020 | -17.6851 | -57.5621 | 2024-11-15 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| e3d60c01-5a62-35dd-92f4-e34596358079 | -17.7048 | -57.5597 | 2024-11-15 01:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| 85cdaf86-1f2f-35e5-8bb9-34b8053285ce | -3.7867 | -43.9011 | 2024-11-15 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 86ce1dbb-2208-3629-a847-f34bed283af1 | -2.6596 | -46.1843 | 2024-11-15 01:50:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 9563fa12-d99d-3f82-99eb-bac1edbc7d33 | -3.8053 | -43.9232 | 2024-11-15 01:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a4eb5a85-8faf-3bf0-96be-d728b1f1f241 | -17.2543 | -57.4698 | 2024-11-15 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.0 |


[Clique aqui para ver as próximas entradas](README8.md)
