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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| befa6013-0fdf-34c7-87cd-088a2701eb30 | -11.82415 | -46.77851 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b401f8b-7a71-3ed0-8348-bcb53fec823f | -12.83986 | -47.97949 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 575590d5-44f4-3d2e-a29a-7bdd7433ec19 | -17.72258 | -44.47755 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef479324-6cdd-3c60-90e0-359be3d31a78 | -14.35655 | -47.31912 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc2beedc-6233-3346-9292-609b352300d7 | -14.26766 | -45.03733 | 2025-09-09 03:45:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d679a651-4212-3808-b583-a343f5593a64 | -19.51382 | -43.98803 | 2025-09-09 03:45:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99895379-f2f0-378a-888a-f6d219f9fbd7 | -13.80051 | -46.28469 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 604ac251-c1bf-3060-842e-7eb95dbd108d | -17.29683 | -46.72379 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 804503b7-841f-3faa-8bb4-b711f797a0c3 | -14.5344 | -48.75962 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dc9ca44-6d73-39c3-8bc2-35c28c47f854 | -14.41212 | -48.46627 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e00022a-27f8-3e8f-b452-b5ea94bae4ec | -11.1705 | -48.37141 | 2025-09-09 03:45:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55a687f0-ee7c-395c-9e4a-3fa442adb9ff | -18.01062 | -45.6428 | 2025-09-09 03:45:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36ed9151-a9eb-3f62-893a-2620797b5872 | -15.53114 | -48.38506 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4344564-357b-380d-99fa-46f5b93c3d99 | -18.00866 | -47.12137 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b91c6b0-d261-3401-be36-b0d8a2a0b0b8 | -17.2591 | -46.68818 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e768f28-ca93-3923-8eef-c0476444db8e | -15.53395 | -48.40062 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70a04b7d-25b4-3545-9f32-898e8bdbf94b | -11.4497 | -49.27703 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 412c7f61-c5e5-38c5-9c8e-caede14f128a | -17.2687 | -46.7309 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09581094-8ef7-352a-94e0-1a7829d0b36e | -15.82978 | -48.94979 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c38cfa9-6cde-3581-b59b-5ad09b8d6331 | -14.55322 | -48.75994 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6e39f9b-eabf-34cc-8a74-005da76ba50e | -17.29428 | -46.71029 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d9fa794-b785-3ba8-b3e8-f46098714179 | -11.84093 | -46.76457 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d819e0b-41bc-33a2-9544-4c3d9644eee2 | -16.69356 | -48.64191 | 2025-09-09 03:45:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e204694a-7e83-36d0-b971-c7287cb13b83 | -14.78888 | -48.23176 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3628b650-1c3d-3f6b-b226-ed010b1fc76c | -13.04394 | -47.15122 | 2025-09-09 03:45:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b109a3b-fc32-32fb-aa65-2766fd9fc073 | -14.54585 | -48.76455 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdbfecb8-34ab-361b-8208-d12c437a1509 | -13.93505 | -48.24106 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4807f42c-37a3-3bf7-aa29-7fb495f6bbfa | -12.88462 | -47.98413 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dba2039-0ff2-3bf7-8c27-b1eca06bb47e | -14.34949 | -47.3251 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 134d720c-8106-3434-98f1-de6637422ca4 | -15.52558 | -48.39152 | 2025-09-09 03:45:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 442aaf60-6480-326b-a9b3-17824d3c6dca | -17.26699 | -46.68784 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f33499f-0b9a-354c-885a-d8ef01b26c38 | -11.83943 | -46.76019 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9cc67d5-be5a-35ca-848f-935b5736b525 | -18.66475 | -47.55101 | 2025-09-09 03:45:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9af2074d-9b06-32d9-8a55-551ef6ba7731 | -16.89925 | -45.8271 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d98a918-c00d-3776-a00c-02af7d3eccde | -16.43753 | -49.29525 | 2025-09-09 03:45:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98b36428-b87f-34e1-8179-d9c7b734bb4d | -16.43049 | -49.29832 | 2025-09-09 03:45:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7011b62-1c52-3a8e-8e42-affb623a08c7 | -14.55272 | -48.7633 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 199ed528-616d-313c-ab29-d79a7c51cc34 | -18.03779 | -47.0845 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c72db8c5-5480-3bc8-a06e-f39bb69cf850 | -14.32368 | -47.32071 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52c70d92-bf81-3b5a-b331-80a7d4c139f7 | -17.7182 | -44.47822 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e745e10-d2b8-31dd-9f16-192765f3e8dc | -14.33503 | -47.31022 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 108b06f2-9d97-3f38-ba8a-b755589afd75 | -17.27823 | -46.73642 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a66497-a5f4-3d0b-a2fd-d149ca9cea9d | -11.16448 | -48.36861 | 2025-09-09 03:45:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 815cec3b-4769-35d9-a986-59ee4cf3c0f9 | -18.02814 | -47.13157 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| defc6ce3-e978-38ad-af34-d62f5fbfe16d | -15.24867 | -48.81142 | 2025-09-09 03:45:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b3a4fc9-d2bb-3321-98a1-25e687df47fa | -18.02288 | -47.1309 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e89d8309-6886-35fe-b816-4a0cb91dfd13 | -11.8369 | -46.75526 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 514c1bb4-8e3d-3262-a380-00206f34aa17 | -14.34627 | -47.31232 | 2025-09-09 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7083886-02d3-3d45-af00-f64a7474c909 | -15.22043 | -44.0382 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df6972cc-f4ea-3e19-8e1a-85e0e384b668 | -17.34 | -43.5846 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a525fab-9fd2-3dd9-93aa-d8561b9e5d3a | -18.76442 | -47.10046 | 2025-09-09 03:45:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 725d33dc-d89a-352d-8ba7-b71d19968e7b | -15.82955 | -48.95581 | 2025-09-09 03:45:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f72ab3d9-39c9-3ee8-abe8-6a4cc81dfebd | -13.82075 | -46.23815 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f53c87b-8e9a-3b9b-85ba-e5ee528e9377 | -18.03839 | -47.08162 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2743e229-3bf3-32aa-b87c-74e9c8377ce6 | -13.72467 | -46.89266 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d11180ad-a781-392e-ba5c-4b7cb042c872 | -13.04627 | -48.02656 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f67d28aa-20df-3acd-8d41-4a1d002041e2 | -12.87126 | -47.97843 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62b99463-1930-39c5-93e1-d74851a0acf6 | -14.54042 | -48.76126 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41efadc8-a8d6-34da-a429-79940d200170 | -17.27489 | -46.75254 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c3062d7-7e95-3a91-b34f-914b1dcbc3db | -14.79674 | -48.18482 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 852a6059-3189-3c33-8fc6-fce4d27b389e | -13.27656 | -43.7409 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfad1ed3-1e5d-3a9c-bd3b-b8effe5fe15a | -18.67002 | -47.55202 | 2025-09-09 03:45:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b3da26e-68ab-332f-9a0a-2fabcf65b05d | -13.82141 | -46.2348 | 2025-09-09 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d26eedb-e0e3-38c6-a128-6dc1d901cbe2 | -13.80707 | -46.27942 | 2025-09-09 03:45:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97a40041-9338-372b-a31c-d03b817dd16e | -17.72346 | -44.473 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02645897-9df5-39b8-bfc6-941256a0e090 | -13.02756 | -48.02651 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36055f7e-9843-3a3a-b92f-cfaf4b589523 | -13.73065 | -46.89146 | 2025-09-09 03:45:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c4e24fa-7053-35a6-ae3a-7d0fb32491e9 | -18.11852 | -45.32894 | 2025-09-09 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24e98306-0218-32d9-954a-59c051092da5 | -17.71471 | -44.47254 | 2025-09-09 03:45:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36f3c910-c5a1-3bf4-8510-dc225a226c82 | -17.34428 | -43.58846 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d2c2d42-1ef7-3204-add5-96f5d8cb2cfc | -18.01316 | -47.12572 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcefd0ed-8319-34ce-8a76-37088f37246d | -18.02737 | -47.13533 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca737d6d-bd59-3674-8534-0cd26e8ae345 | -13.94321 | -48.24302 | 2025-09-09 03:45:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 230aba0a-789a-36a3-8e97-f39aa9922184 | -16.34741 | -43.03551 | 2025-09-09 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c636cd2-e494-390a-addc-386531ecdab4 | -14.79323 | -48.23035 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 447a140d-4615-3a61-af5d-5643a5c24da7 | -17.33929 | -43.58846 | 2025-09-09 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fdec19b-1ff4-342b-8c88-08668dc47cbe | -18.01543 | -47.11465 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1a992de-cd3f-30f3-b17a-91f4538d12ec | -13.28738 | -43.73328 | 2025-09-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeb97681-b197-3694-9f4b-e25f88f4c90e | -16.98443 | -45.88235 | 2025-09-09 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac1b8e4d-d798-34eb-9a9e-02c3d5427de7 | -14.79738 | -48.19017 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 635d6dc5-7e61-3e5f-b836-b39089b21e47 | -12.84611 | -47.97943 | 2025-09-09 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9227f45-7826-3d73-a6db-6fc511729939 | -16.70025 | -48.6391 | 2025-09-09 03:45:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a4e71a6-6470-39f1-94fc-1839060b6b5a | -11.8435 | -46.76962 | 2025-09-09 03:45:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 960ca8e4-21b2-3d0b-9bdf-0a5773da1646 | -15.11836 | -48.06026 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce752564-cc71-3849-9b8b-c57efb0998ac | -16.62323 | -49.1428 | 2025-09-09 03:45:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c63b7b0-3359-37fd-8d37-ebc12e958444 | -15.09748 | -48.07364 | 2025-09-09 03:45:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eff25b6a-6985-30a4-96b4-9a2220710b54 | -17.26484 | -46.68607 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 992c24ba-8bd2-393e-8e0f-2e9ad3c4b920 | -15.20304 | -46.24757 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 407bf6cc-8d41-3c10-a449-2098c95abcf5 | -11.45758 | -49.27235 | 2025-09-09 03:45:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45c5a732-1dab-3b26-b1c3-1818c3e5bb03 | -18.03336 | -47.13244 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8bffe1d0-8509-3028-8ed7-515dba1899df | -14.99471 | -44.45695 | 2025-09-09 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e3142a4-bbaa-3d3d-8142-152a85ff8cf0 | -17.08146 | -49.23108 | 2025-09-09 03:45:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c877dfbc-0d61-380f-870d-ab36d117facf | -18.03411 | -47.12875 | 2025-09-09 03:45:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 91ba4541-d489-3966-9ec8-3d8cbeec5b8a | -14.53836 | -48.74065 | 2025-09-09 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d86d8ac-4e82-332f-8140-d4a0cd4fa5c3 | -18.46525 | -43.97558 | 2025-09-09 03:45:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9ed54ac-9e11-3169-b1d9-cdef2b568db1 | -17.27045 | -46.74821 | 2025-09-09 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b9954dd2-aeae-3cd7-b1c3-1dcde7d52e19 | -14.25856 | -47.10432 | 2025-09-09 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71aef2e7-4d36-3220-a13d-f2fd5afed6b7 | -11.30751 | -46.50597 | 2025-09-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2927b565-ddec-35eb-b8c2-855bd58dbebb | -18.75941 | -47.09903 | 2025-09-09 03:45:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac5e2631-a11a-3dee-9a7d-ed93d4d7245f | -15.29264 | -43.38063 | 2025-09-09 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
