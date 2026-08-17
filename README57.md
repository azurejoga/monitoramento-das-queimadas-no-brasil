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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47783576-04ee-3a0f-8483-1f4dc1f0f6da | -14.75 | -56.34343 | 2026-08-17 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31bdabec-afaa-31a2-9230-02605037123a | -14.49289 | -59.31717 | 2026-08-17 05:18:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 064a6000-2524-304e-b2f7-3420a63cf11b | -14.47766 | -51.98283 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a94585-c96b-3843-b1cf-b2158e60c535 | -11.71329 | -54.59399 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed10cae2-2635-3764-8559-982a16f15801 | -11.46716 | -46.59333 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6befb4ad-c1be-34c4-b44a-783d7d151d77 | -15.91991 | -56.48108 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7310177f-eef4-3ebc-97a6-2d7c8808e41f | -15.23846 | -56.46754 | 2026-08-17 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c712dde-fb8d-33c1-b4aa-6daab7f418e0 | -11.88726 | -50.21971 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0051e497-78d0-3f43-9430-d247f5f3b7b6 | -13.51357 | -46.2968 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e07f5b22-eb6a-3c5b-ad16-cbf4eeb0c9bb | -11.78965 | -51.78713 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28d3bab8-cdad-3e4b-971a-d2ecb1f28a48 | -9.2038 | -60.78983 | 2026-08-17 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cb2185d-b8b8-3329-824e-8e4a217a8832 | -14.44287 | -51.97709 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87161916-dfce-31ac-a7e5-b47ed08faf5e | -14.08555 | -58.45026 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54599f3f-6d5b-3809-8393-9c15109c8e94 | -11.73065 | -54.57479 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78b3c75f-d955-3e2e-96ad-fc113a91d82f | -9.37215 | -62.36075 | 2026-08-17 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b0e7dd7-8977-3c75-b44a-f6bad66744f4 | -11.32133 | -46.21412 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcb5686c-25e7-3b69-8c5e-f2f19a0c05ba | -11.88055 | -50.23123 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5430bccf-f06a-30e4-999b-5d90079e0964 | -11.22064 | -54.01622 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 054c04bb-4a0d-3b78-85da-8cce51bb2f72 | -14.50075 | -59.3326 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dde115b2-d678-3656-b4b1-f4243b945d9d | -14.31928 | -53.05151 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d64641-9460-31a9-8b53-066d3a1c57b8 | -11.88135 | -50.22513 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b61b00d-1211-3714-9a65-5d82765aaaa1 | -15.02784 | -47.03804 | 2026-08-17 05:18:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 423c7ecc-23ab-3648-888b-e7e6f4b8a461 | -11.7289 | -54.56713 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1cb265b-72a9-338d-abb3-11a4206eac66 | -13.51927 | -46.24181 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c4dd4c98-f7bf-3398-90d8-04a4cf7c3c4b | -9.34993 | -63.56232 | 2026-08-17 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| befd7692-b51f-3291-b1b3-ccd3cc6722b8 | -11.71675 | -54.62365 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b58dc18-a49e-3831-a286-b04ad1fbc296 | -14.08499 | -58.45385 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d538d345-5c28-30cf-856a-b44f06b5df4c | -13.63262 | -56.99546 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0a78642-00ce-3fbe-8f86-7639e4c8596e | -11.7157 | -54.60415 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11d1b3a9-9c5e-3410-85fe-bed122b41684 | -11.33017 | -55.21996 | 2026-08-17 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d0dc29-21e0-3747-892f-bb0c8f90ad61 | -9.3452 | -63.56528 | 2026-08-17 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e3ca211-9bf2-3a50-96ae-4363ec87f2ab | -13.6332 | -56.99161 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ee8879b-46bd-3a8a-901b-a90bfd952963 | -14.30152 | -47.1868 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7af68b71-b54c-34c2-a04d-e31e6f38b501 | -15.91327 | -56.47566 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bacfd84-fffb-3f12-8562-37cc71d03ddc | -11.73202 | -54.57244 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da33cb3f-886b-397c-ac13-2c6175a26601 | -11.69529 | -54.61071 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64b1d287-c065-3239-a2c7-ada1827cb611 | -9.59886 | -60.50233 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4822b4ac-5223-3409-9b50-21477701937a | -13.42386 | -57.05884 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1bebff3-09cd-3581-a28d-6eb2d0904fee | -10.05989 | -62.45007 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 732ea9f4-b67f-353a-a120-8eef96dfb127 | -12.65775 | -48.48709 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e6d797c-029b-3b47-8e93-19e22060853f | -11.49249 | -46.61205 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68ab0845-bdb1-3832-9f73-c7afb96077d4 | -11.44847 | -46.58588 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b7066fd-a447-3986-b696-f22130a42b17 | -14.09764 | -58.4329 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| efbe3189-6d97-3dca-b317-6af0cd7312b1 | -10.94646 | -57.1499 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 822d2fae-1b11-3369-b10b-82a186480634 | -11.69978 | -54.60659 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5aa16de-e9bc-3ae9-8d69-02c4126015f6 | -12.02078 | -46.43151 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88d51bb1-a0fe-3185-b071-7f325d070597 | -12.72537 | -48.46405 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e517a65a-a98f-3b9e-8acc-976711709d84 | -9.47516 | -60.50625 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 883ca440-1cfc-3c62-99af-cac073e59a92 | -15.81616 | -55.53196 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e4d96d6-8128-3ecf-bc5c-69276c06f403 | -14.30736 | -47.19295 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 388c80e9-0075-312d-afa4-3e93769b3886 | -11.48945 | -46.58157 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df6e6f54-5def-30a9-862e-228ec017efb7 | -14.36639 | -51.89923 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9658ab8f-39f7-33ef-bd00-901a7f0dd3a6 | -12.7453 | -59.77386 | 2026-08-17 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e33a8a95-269c-355e-95cc-92e9b3dfbe91 | -13.41871 | -57.04622 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eca2e440-d773-3dc4-928d-6375dac5cadf | -12.74473 | -59.77742 | 2026-08-17 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d06d0838-06f6-33c5-ae98-a920746fd038 | -12.65615 | -48.5 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22e56163-5a2d-3aa5-9dbf-7b38740b86b0 | -13.78842 | -53.80177 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9686fda9-5255-31a7-a287-1ce151a12472 | -11.49102 | -46.6118 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdeed2d8-fa08-3837-94d3-2c808f371c29 | -13.78453 | -53.80996 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3db18dcb-97b9-3653-8448-434ce0927332 | -10.07567 | -60.50075 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6364a64-c0a2-34fa-9c90-3d8fed50e22c | -11.32774 | -47.01302 | 2026-08-17 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3499625d-abee-3060-9ccb-ee805988c244 | -14.10042 | -58.43704 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a63e10b3-e0de-3666-8109-cb8619c7fd14 | -15.90728 | -55.51971 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 936a1e1a-8390-387d-9c6b-4339fe682beb | -11.216 | -54.02073 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60c35c03-5365-3262-9667-186f060c644d | -10.07848 | -60.50511 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf4eff73-d6c4-31b1-b5d1-a400f7c9da56 | -13.51418 | -46.29089 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 57841129-f271-3d10-850d-a559c08cac1b | -16.75261 | -49.36824 | 2026-08-17 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5b8dad3-99f6-3bc9-b8ed-b4b138003af0 | -10.0763 | -60.49696 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3abd64c3-408c-3aaf-bfc3-40f1fe5d492e | -12.66087 | -48.51164 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 538a580e-7895-348b-b1c8-b3744cea2d85 | -12.67199 | -48.51699 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b2badb7d-4001-3528-aecd-5909ed21694f | -15.9187 | -55.54345 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| fff168c5-7d74-3d55-acab-a46a6a335937 | -9.34929 | -63.56599 | 2026-08-17 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c36f9d61-2999-380d-acf2-d4822692bc7e | -15.81753 | -48.16904 | 2026-08-17 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8413fe3-20a3-3e10-a2b5-8bfc640ea489 | -15.16157 | -48.62127 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 364da13d-1266-303c-8622-f6ff434f757c | -12.74415 | -59.78098 | 2026-08-17 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98e878af-3e30-32b4-a6b0-aff3dce6b4b0 | -14.14478 | -52.88352 | 2026-08-17 05:18:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7498ff86-a1c8-3c1e-804c-ceb93e192671 | -11.7171 | -54.59456 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c18ff05d-13a2-3990-ab01-0cf9c26cd75c | -15.28574 | -56.11656 | 2026-08-17 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8be62af-3389-3e3a-b07d-fb4c9e8f7e90 | -13.51855 | -46.28482 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04460270-f9c2-392d-bd5b-89f12c57452b | -15.91487 | -55.54299 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b4ce9889-820e-35d2-bab1-484be1f3d336 | -9.47108 | -60.50949 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f806a7f-0827-3d36-b139-22a26f0a54ed | -11.79541 | -51.781 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bcb2e87-e88c-3c23-a9b0-111a10c93d04 | -8.65882 | -64.27574 | 2026-08-17 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab69915e-c7f4-3271-b687-e1bd902640c9 | -12.06188 | -58.03925 | 2026-08-17 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 011e77d1-0b23-3b38-b075-ae0fbab9db69 | -13.78891 | -53.79804 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86198235-e7ec-3f95-bef6-40442cbad1f4 | -12.6894 | -48.51872 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3965bea3-10a1-3c8d-ac57-4a6fec3462d8 | -12.72592 | -48.45951 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24680b8b-85ff-322f-9a25-480e45fd5a10 | -11.72091 | -54.59512 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a22300e-4c56-305a-b2d9-f4096e9c9d10 | -15.85543 | -56.33076 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76e44627-ec95-3dc4-97f4-6bb3bf795810 | -13.51052 | -46.29599 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 666c591d-c346-30eb-93c3-c636e588eb3a | -9.37135 | -62.36543 | 2026-08-17 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 237e69a9-1866-3fd7-839f-d4883ac2e983 | -14.07795 | -53.59354 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f25a2f4-b939-35c3-8f68-a9dd324160b3 | -15.91025 | -56.47078 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36e773aa-f590-3c02-8947-91dffa58914b | -14.36533 | -51.89742 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8552be8-9084-3f4c-b9f4-fd2f16ce9921 | -11.72194 | -54.61476 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa45cafa-3c6e-333d-a04b-28a82b883ed4 | -14.18293 | -53.06856 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1366c7ee-fff9-37c2-8416-ecaa725cbcb4 | -12.13064 | -57.21092 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5a1680e-8252-3e4d-a3f6-6422f2554ac5 | -11.53669 | -46.22326 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94c11e77-eeeb-3305-bcc1-75cadab03887 | -11.39078 | -46.40427 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82736315-5897-3fbc-b369-149c93b8feb5 | -15.81355 | -55.52943 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
