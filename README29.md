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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eafdd9fd-146e-3245-85ce-b1949b07ab3b | -11.14338 | -46.17726 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25efd2c9-3a40-39f8-9c39-75cf1d56a987 | -11.55159 | -46.96474 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f13c0d4-22f7-34a5-a7a3-ba299bb8afec | -12.86303 | -48.48557 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5a60b04-af70-3bac-8855-5ea7ce036beb | -15.31816 | -46.06012 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e0374d0-4cf4-367f-865d-454ab54ab416 | -9.46417 | -56.93019 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca212e8e-b428-3681-8cc1-ad10c3343ff0 | -10.43526 | -50.4411 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6bb0a5f5-3689-3f85-995e-57ac523628bb | -7.49479 | -55.34837 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d64b985-51f0-39f3-9755-e8ca45d9bb2d | -9.50091 | -60.50517 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcb5ab1e-7068-30e3-9292-cfd54fd87508 | -10.62971 | -52.24767 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6927ef3-1eea-304a-bcf7-4b56eebc0ffb | -8.54375 | -54.85311 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c66d39d-f417-38fd-8e9d-37c995bb607f | -11.84444 | -51.68052 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db4d4286-5a41-3c32-ad3b-6359a8436375 | -6.63232 | -58.4823 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70a994b6-98c7-3702-a708-fb8a35ff583f | -12.85841 | -48.49254 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed2f97d9-e888-3d90-acbf-108ff7ffca58 | -12.89125 | -48.48941 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6bbbcbba-c748-36cf-b1d7-64c959e4f6e2 | -12.86477 | -48.47375 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40da89d4-a47d-3159-bb9e-c8ec36ca529a | -6.79053 | -59.65495 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddbf2b3d-b7c6-3994-a084-4fa9504579b2 | -8.35185 | -49.17611 | 2026-08-24 04:46:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcccf5d2-e802-3dd5-9ce9-7be050c812a9 | -11.60199 | -46.94179 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 939b2d6e-8e87-3b3d-ad61-60811849357f | -14.32956 | -51.75756 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22725cf0-5892-3a81-bc8f-68ab56afaffd | -10.29639 | -48.20903 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0e4b9ca-4188-315d-b2d3-8ddae1840a5e | -12.11438 | -50.62518 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f6342c9-cde8-36f9-9ad9-2a668e68beaf | -8.59581 | -54.7353 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a41f09-6c98-37ab-93af-24093020d651 | -8.37278 | -46.47379 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f08f6cb7-ba04-3fde-b1b1-0b5bf919cd2d | -12.89417 | -48.49395 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8822162-c997-3591-8317-e110692da160 | -9.05819 | -50.76973 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93fbd539-a0be-3da9-807c-6bf9bfdd50ee | -12.7462 | -46.46541 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b9d1ce52-7a1e-36b5-bfbf-d74f7e303978 | -19.15648 | -44.40322 | 2026-08-24 04:46:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 151bda11-2794-3734-95a4-0533743b6dbb | -11.9164 | -55.90596 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f6fd39-ac54-314e-b963-6950261e882e | -12.74829 | -46.45046 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb345bf7-4bec-33bc-b8c9-194567594301 | -11.60207 | -56.28805 | 2026-08-24 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29a14721-64c8-3057-8d66-ee826819ff75 | -14.31906 | -51.75945 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e44f3173-d63a-3fba-ba76-767a03154ed6 | -9.38666 | -60.58357 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c4a092d-daa3-3aa4-af39-b8d52a0b8e8f | -6.80256 | -59.58803 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f182e195-1da5-3c80-959e-154783ee11eb | -6.68686 | -58.72472 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 00854a10-16f9-3123-82af-26220ec57ff9 | -7.48897 | -55.34515 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d5f925-8b1e-3b6d-9be3-64ffb8ce1802 | -9.03174 | -50.72242 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 657c2247-54a7-322c-b7d1-7009556c0a5f | -8.31096 | -47.58633 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdf92552-40e3-391a-a995-6e08fd22b4e6 | -14.40384 | -51.78082 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22689c2b-291f-37d9-a21d-2ef88d97fa02 | -10.80697 | -50.94606 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af72ea59-acb3-37fa-a4f0-89295aad51a8 | -12.07125 | -50.57529 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecae5637-fd15-3e09-b1f2-1d22464bc2a5 | -12.10996 | -50.61001 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 6ba51682-1894-3ece-985b-e433e31875df | -12.10057 | -50.62656 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d56e18-7e6f-394a-a667-5609b58bba6a | -12.86416 | -48.47792 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6639adb-cc09-35ef-8178-f4273c24d564 | -9.02727 | -50.75037 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cfd301-683c-3c06-a1d9-98c4e1a109a0 | -12.75224 | -46.4508 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01be1c2a-b154-3aea-94f5-9ba90e45cfaf | -14.29932 | -53.21461 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f9f4ac6e-c01c-3d28-8dd1-827b5a3864f9 | -11.38243 | -47.1978 | 2026-08-24 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7aa121e-9ac9-3ca6-8619-e5ae51fea7bf | -20.59798 | -52.4627 | 2026-08-24 04:46:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d6a9eb5-945e-3aed-8a7d-ba9efbec9206 | -10.28999 | -48.20434 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 255a4ce4-c615-3ea9-b16b-dd2a82ae6bb4 | -12.1177 | -50.60404 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 363586d8-c601-38ac-bef9-c9df051d1caf | -10.52234 | -50.76993 | 2026-08-24 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fde61dc-853e-3e78-9949-0c6c2e4e5d08 | -8.97949 | -46.00715 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76d54b29-f7ef-3b70-8112-19aab1fe0c24 | -12.12157 | -50.60105 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d3ba370-0e58-3c28-8718-d5d153099ff9 | -6.63378 | -58.48066 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2748886-7317-395b-b024-d4010706edba | -8.52491 | -54.84468 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5d98f72-4873-396c-a362-0cfa611104a6 | -19.01388 | -42.12583 | 2026-08-24 04:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 831f99e0-1f45-34f2-ade0-148998a6a8a5 | -14.7775 | -48.77075 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b21820d7-bc91-3ee1-ab7b-fc1a7c401e24 | -12.48128 | -54.17862 | 2026-08-24 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae236c94-a901-3914-b03c-4dad12ec4bab | -9.36898 | -45.41509 | 2026-08-24 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fd120b3-8e4d-3dd5-9a91-9cc57151a4ba | -8.31179 | -46.89798 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cb06eb1-6995-39b0-9fde-a3ea4a212e3e | -12.09228 | -50.59277 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c42fd89a-6baa-3071-98c9-58c2743318a3 | -6.68744 | -58.72149 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ff9d5ddc-3068-3d26-abf9-8f9b1b308ec6 | -12.1072 | -50.60595 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| afb19156-66fc-372a-bfd3-5c5c292781c9 | -9.5045 | -60.502 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33901575-d1b8-37d0-bc5e-f98a88bdbb8c | -6.81295 | -58.6543 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77748404-77c5-3c0e-ac46-f6171ecba4e9 | -19.01345 | -42.12996 | 2026-08-24 04:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e6400751-10c9-3bf9-be82-0910233979b4 | -9.06691 | -60.44021 | 2026-08-24 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be4b3801-0a50-3403-9fed-39e2e2e56de5 | -11.90842 | -55.90451 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f1328de-3f93-32a1-8a92-d6a9274ca569 | -8.08505 | -50.05285 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba1a34bb-a214-3611-b07e-4aec132d7145 | -8.98125 | -46.02217 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cbd110d-ad7c-32a4-abd7-a73211adf5ba | -20.42435 | -54.61497 | 2026-08-24 04:46:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 343800c0-a4a1-3387-b5fd-fbf7a585108e | -11.84777 | -51.68107 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1de13a5-441e-368f-bfae-ab9e878b1908 | -8.31334 | -46.89642 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dfab984-2485-3f46-9f99-acb2c7859f9d | -7.49131 | -55.34392 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18494b9e-9bbd-30d4-b185-250f4320ad66 | -8.79412 | -48.3116 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d15845-e90c-3604-bec4-575799296313 | -14.78041 | -48.77561 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3186f71-487f-3844-871f-f10c8fba7606 | -10.731 | -47.98035 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b3d0cf2-21af-3da9-98c3-08e6d444cb44 | -11.68974 | -54.59087 | 2026-08-24 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e12aa92d-3e35-3f86-9a5f-c31919adfc7a | -12.10222 | -50.59439 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99fa72d2-0e4a-3b0d-a8ac-d0130e5df961 | -6.53664 | -56.1753 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edd9814c-7867-34bb-a1fa-335b9d1ef5bf | -10.52565 | -50.77047 | 2026-08-24 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03239a39-c8b4-3035-aa98-38939426c9bd | -13.14485 | -51.39011 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55443174-f5dd-378c-95fc-43381611fdf9 | -6.86241 | -56.41398 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f4626d1-27a5-30e5-b575-79228c4629ec | -6.81234 | -58.6588 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b8e541-2d2f-3f9a-930f-bbc28707905e | -8.10804 | -51.66051 | 2026-08-24 04:46:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a1edf07-be13-36a1-92a3-e1fc2287470a | -10.7006 | -47.74783 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e70009ee-92ed-3554-95fd-84907356351b | -14.30436 | -47.23615 | 2026-08-24 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69dc8e1a-c0b3-36a0-a164-4c09ff432996 | -8.79241 | -48.32278 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 984bb36a-bf91-3a5b-8198-ccf24b3e4401 | -8.79298 | -48.31905 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b29d30-f019-3eb2-9f2c-d0866aa6bf3d | -11.65461 | -50.54721 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4aef3f9-8bd3-3398-8869-81f30d96e403 | -10.70355 | -47.75246 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409e6549-c5cb-37d3-be07-a1f857ce9af4 | -14.28368 | -51.78983 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 888c9ac0-9ddb-3211-a3bd-20d2b6b23852 | -15.03182 | -48.68484 | 2026-08-24 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffe3e393-1be1-3801-880f-f2c2a1576bf7 | -12.10609 | -50.63469 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f562062-fc72-3628-9ba3-b6259b7a8975 | -9.39233 | -60.58467 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee770a63-36c6-330b-848c-6b8a7cc3611f | -13.16792 | -51.39378 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bae70365-e35c-39a0-a99f-887b7b2cbd3a | -12.10112 | -50.60135 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e2c3e2f6-c159-3426-99c4-b78159a1af5d | -18.32161 | -47.20125 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fd946b71-f934-3680-8530-1e7452849ab6 | -12.0956 | -50.61491 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce0388f2-a424-3f6e-b03b-f5b24c122361 | -11.15861 | -54.00858 | 2026-08-24 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
