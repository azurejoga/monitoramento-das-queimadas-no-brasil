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
| 0c8f70e4-2155-3326-80f8-07238ff1e0e3 | -5.4028 | -44.9725 | 2025-08-24 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 361e12d7-d747-3a25-a575-cc5647db5f6c | -14.7984 | -59.6145 | 2025-08-24 00:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ed8d7941-530d-31f3-8231-78f22d3f437e | -22.0856 | -53.7984 | 2025-08-24 00:40:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 206.5 |
| f6431fe0-f3ce-3a39-beb4-028705e54237 | -3.5083 | -47.212 | 2025-08-24 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ccc015fc-6b07-3bd6-8791-aa2e41f7ddfe | -5.4026 | -44.9952 | 2025-08-24 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d808e4af-2466-321f-8d8d-e8583876a49c | -10.6009 | -50.1843 | 2025-08-24 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b530efe9-764e-3c86-8665-a79fa3702851 | -11.9867 | -61.0214 | 2025-08-24 00:40:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b3d6e3a5-1130-371f-a2b4-91ecc3b4e8be | -8.6314 | -62.63 | 2025-08-24 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 33d14a5f-0108-3ce5-b0d9-32154be105c8 | -5.4181 | -60.1784 | 2025-08-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 163.8 |
| e9ca471e-3fdd-3072-ae08-078c7919701c | -14.7981 | -59.6343 | 2025-08-24 00:40:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 543f67af-0874-3779-ad8c-834288cae5b9 | -20.339 | -51.7062 | 2025-08-24 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 870334ef-9e66-371e-8a02-74dcaac4d9fe | -3.5994 | -47.5359 | 2025-08-24 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| cb40134d-155f-3d73-a4a2-b89e12d124ad | -20.3599 | -51.68 | 2025-08-24 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 75b50444-b207-3a27-b8fe-54142018f79b | -5.4182 | -60.1593 | 2025-08-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 6195eac6-9c95-3389-9f54-51e23ef2f351 | -5.4364 | -60.1779 | 2025-08-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 5866d623-9f25-3c6d-b977-9e10d2c3ab22 | -23.55024 | -47.11018 | 2025-08-24 00:45:00 | TERRA_M-M | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 18da74b9-fc31-385f-b2d7-f3a288d906ab | -23.26754 | -47.24823 | 2025-08-24 00:45:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 0f2c02a9-5727-3337-aa5a-4e588857a2fd | -23.72865 | -47.43746 | 2025-08-24 00:45:00 | TERRA_M-M | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e99e6a0f-fcb7-37d4-a7d5-d13b9e7768fc | -23.3119 | -45.53178 | 2025-08-24 00:45:00 | TERRA_M-M | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| b98b3e0f-a7b2-3264-8223-bd99ccbc1d34 | -24.78017 | -48.21062 | 2025-08-24 00:45:00 | TERRA_M-M | CAJATI | SÃO PAULO | Brasil | 3509254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ab1d8f36-986a-3cc6-829d-1edb0c29644b | -23.11778 | -47.30227 | 2025-08-24 00:45:00 | TERRA_M-M | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| be43befe-5a1e-3a95-826e-e528cdf56399 | -24.75509 | -48.5595 | 2025-08-24 00:45:00 | TERRA_M-M | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a5062147-a161-3da0-af51-64c81d9f63c2 | -23.42069 | -46.74251 | 2025-08-24 00:45:00 | TERRA_M-M | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 588903d2-df32-3ba2-a7c1-3cda2d9f8bea | -22.13816 | -43.64791 | 2025-08-24 00:45:00 | TERRA_M-M | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| b1d36d04-a98f-3715-add5-e300dd430497 | -23.72716 | -47.4274 | 2025-08-24 00:45:00 | TERRA_M-M | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7a8539e8-01e8-33bd-9bf2-b355beff6fc4 | -23.36849 | -46.94233 | 2025-08-24 00:45:00 | TERRA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 952589c4-4ebd-3cf6-a90a-23acd8868343 | -23.32738 | -47.84421 | 2025-08-24 00:45:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 744f12a1-12c2-314b-8964-416cee466b33 | -23.35627 | -45.80615 | 2025-08-24 00:45:00 | TERRA_M-M | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.0 |
| 876a9efb-41fd-3e5b-af5e-acd00ab7e402 | -22.65997 | -47.44151 | 2025-08-24 00:45:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f69d6532-f8a5-3624-99f4-8e1b6bfeb161 | -23.46911 | -46.81024 | 2025-08-24 00:45:00 | TERRA_M-M | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| f3da9aa6-a63a-3fc6-ae0f-250732622d8b | -22.14891 | -43.65739 | 2025-08-24 00:45:00 | TERRA_M-M | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 9b82094f-b9b9-3161-a2d7-f9f89d4815ac | -24.56635 | -48.12999 | 2025-08-24 00:45:00 | TERRA_M-M | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a7f31875-aecd-395a-b9a4-d71d3810cd9e | -23.11625 | -47.29214 | 2025-08-24 00:45:00 | TERRA_M-M | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 7844a68c-301a-365b-b4bb-8f0e09093d0a | -22.66147 | -47.45172 | 2025-08-24 00:45:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e792c6e4-7928-382b-a5c7-86fafc3a6e21 | -23.13402 | -47.03538 | 2025-08-24 00:45:00 | TERRA_M-M | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 49594908-884e-3f53-a64a-2d31ceca0898 | -19.61341 | -47.60906 | 2025-08-24 00:48:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c20e8c76-1861-3bc0-9304-f453ba148aea | -20.94293 | -46.83698 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 838243eb-5d6d-3e2c-a111-d25887508f8f | -19.63228 | -43.19307 | 2025-08-24 00:48:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.8 |
| cd01390d-b434-3fed-9ce7-5025739a4ae2 | -17.39641 | -42.63508 | 2025-08-24 00:48:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 11053d4b-4314-3066-a026-6c0c5aaf5934 | -18.70921 | -40.02165 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 281b8d7f-bb06-367b-bbd7-c021ee44ae84 | -14.79505 | -47.94319 | 2025-08-24 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bc4f3f7b-6d2b-3b61-93e9-2c4f0f4dcd94 | -18.66344 | -47.36366 | 2025-08-24 00:48:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3a6be4e2-da3f-3923-bb14-d736e6439197 | -22.81525 | -54.01451 | 2025-08-24 00:48:00 | TERRA_M-M | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| a7731c25-1c9f-3939-b861-18d50daa9289 | -16.41381 | -49.94392 | 2025-08-24 00:48:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ab242a0-0677-3980-8309-1b302551a7d1 | -22.29637 | -47.60301 | 2025-08-24 00:48:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e2bd7591-39ed-3901-ab60-179f622ac2a2 | -17.78506 | -40.17803 | 2025-08-24 00:48:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| bb6087dc-6542-3252-93c5-124b8bc1099f | -20.07885 | -46.1096 | 2025-08-24 00:48:00 | TERRA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a425f346-9b16-351e-be2e-c0c0a41ea859 | -22.08592 | -53.81843 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 623a84c3-85db-3d14-90a0-fe8e281f5522 | -20.9413 | -46.82649 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| a0dca848-4d1c-3a64-9d72-79bb9f552e42 | -20.35403 | -46.73975 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 707b6894-d6b1-3fa7-befd-ba4d62529fd9 | -17.59488 | -46.10685 | 2025-08-24 00:48:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3b3c139c-dc4a-349f-ad3d-de0393b5c327 | -22.81359 | -53.99922 | 2025-08-24 00:48:00 | TERRA_M-M | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| af66aee7-aa25-33fc-8a15-9985c385dce0 | -14.81793 | -47.9441 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 59981cbf-407e-32d1-884e-9c7a8f6ae89a | -15.06062 | -48.49025 | 2025-08-24 00:48:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 44b9e341-7faf-3d8e-8dfd-f4b06b76eec5 | -17.39201 | -42.61053 | 2025-08-24 00:48:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9e2cab7b-5efd-3f5e-8e4e-d37aed6a3233 | -22.82473 | -53.99767 | 2025-08-24 00:48:00 | TERRA_M-M | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 9223694a-900e-3726-a012-b69fe65df1bc | -15.11019 | -48.65369 | 2025-08-24 00:48:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e4cc549-fce2-32b9-9c3c-f2949354f1ed | -15.08465 | -48.65369 | 2025-08-24 00:48:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c5f84ad9-f704-3594-85fc-33c7d17506f1 | -22.00882 | -47.96759 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1cae1443-de81-34aa-a50d-0c53fe7f66b1 | -14.93804 | -47.99722 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 57b8d392-1476-3625-b17b-61f06058a2dd | -20.35613 | -51.69868 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7797d0d6-89f6-323c-ac16-46c6e0f6b968 | -20.93343 | -46.83875 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e413c79b-7a53-3307-95b4-46805844c901 | -18.71626 | -40.01506 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 989990d9-ee39-3278-8367-a31489bfdc90 | -20.3548 | -51.68823 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 65dbefcf-6440-3801-b21e-35f670006640 | -14.85144 | -48.32209 | 2025-08-24 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0de4e243-dd97-3268-81b6-fbbc2328cc7d | -16.80078 | -51.35286 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 44b0c8cd-313e-391a-9109-829fecefefdb | -16.78412 | -51.36479 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 02d9b653-4515-35d2-8734-36f534d7ea07 | -14.79668 | -47.95405 | 2025-08-24 00:48:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 32c3c899-ae79-3b91-aded-40d12e75d520 | -22.08261 | -53.78912 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| e29ef947-8ae8-3aed-a39f-f37f5312bbd2 | -14.80486 | -47.92381 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| fc1b0b8d-5e65-3b13-a13c-1bedb5fb0523 | -20.35579 | -46.75092 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c0e30b0d-9683-35a1-8a05-26d613f0f880 | -17.41161 | -48.11391 | 2025-08-24 00:48:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2ee94cf-4876-3fa9-9e6b-7708a648c550 | -17.79137 | -40.17121 | 2025-08-24 00:48:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| 18220554-c39e-3634-8979-932664d022b0 | -20.19985 | -47.02488 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 41dabeff-1468-39ae-bc9b-baa12a6b5839 | -17.03743 | -47.18387 | 2025-08-24 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5838d1cb-8312-326f-a54e-f696edbb5a73 | -20.36366 | -46.73798 | 2025-08-24 00:48:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 8f3f4a51-1c1b-339a-9d82-d4c863a02cd5 | -17.60877 | -44.30739 | 2025-08-24 00:48:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 185.0 |
| ba50a4c4-e2eb-32fb-9030-7982cd227e69 | -22.08758 | -53.83314 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 48.8 |
| ae402c9c-7e1a-3165-a3f6-195a00ac0728 | -20.9729 | -42.8549 | 2025-08-24 00:48:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| afbebaa9-e4ca-33ba-a360-66ed26f6a11b | -14.80474 | -47.94152 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d39d327c-1fe8-33e0-b3d2-a1c40743dc95 | -20.34679 | -51.69997 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| dbaa8678-1cd6-3d8b-80a1-352dcfe4a0b4 | -22.07176 | -53.79065 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 492.9 |
| b9f0284e-e1a9-36d8-ae32-b19d87e37d73 | -14.80656 | -47.93486 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e45046ce-b53f-38b2-b62a-2356d8febe5b | -17.8012 | -40.17423 | 2025-08-24 00:48:00 | TERRA_M-M | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 2ce65008-3d10-3cb4-97dd-d4fce457caf1 | -21.41221 | -47.6157 | 2025-08-24 00:48:00 | TERRA_M-M | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6f7c406-3907-3ab6-a820-5b94770ee0e7 | -17.04728 | -47.18217 | 2025-08-24 00:48:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 30d82ee2-1a6d-3ff0-b062-66e7e23752ca | -18.39928 | -46.84359 | 2025-08-24 00:48:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a88e2b70-8a3e-3cec-9eb3-2199505a4f4d | -18.60877 | -46.54316 | 2025-08-24 00:48:00 | TERRA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6c261f4d-f115-3a0e-b528-4b835a38cba1 | -18.75818 | -45.11077 | 2025-08-24 00:48:00 | TERRA_M-M | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 940b4189-62bd-3fea-a4ec-0e2e9ab3145c | -17.60578 | -44.28967 | 2025-08-24 00:48:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 65b4c09d-24b0-3d67-abd5-d062fc6a43ed | -19.83223 | -47.54189 | 2025-08-24 00:48:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 73c32f30-6048-321e-b23a-be45f457c332 | -20.34547 | -51.68953 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 35f0052c-3481-3c9f-93ed-5599c5101dfe | -20.97562 | -42.88159 | 2025-08-24 00:48:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| d81e1724-da71-3c4e-ad5d-52c1afd1cf3f | -16.79308 | -51.36353 | 2025-08-24 00:48:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 675a860a-822c-356d-9d37-6ebdd03d1e28 | -20.97658 | -42.87484 | 2025-08-24 00:48:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| b184d00f-2046-3089-bd79-569806cdf3af | -14.80144 | -47.91935 | 2025-08-24 00:48:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| da97838f-10a9-3319-9c52-8072c01a066e | -22.05487 | -53.83727 | 2025-08-24 00:48:00 | TERRA_M-M | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 9d77bbf5-0534-36dd-97e6-edab086832d4 | -20.97211 | -42.8618 | 2025-08-24 00:48:00 | TERRA_M-M | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.7 |
| 22392815-fd90-3094-a785-f8463b04a683 | -20.36413 | -51.68693 | 2025-08-24 00:48:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ece1d42c-c226-31dd-a633-289e1021e1d7 | -15.23048 | -48.22852 | 2025-08-24 00:48:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README9.md)
