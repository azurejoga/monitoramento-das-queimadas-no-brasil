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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c8ac54b-7d4e-3e30-9e77-c5b09082d9de | -20.39645 | -41.21366 | 2026-09-12 03:32:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0601d4af-da14-37db-9256-cc32e5a3d823 | -18.9348 | -46.83338 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 475922a4-0b59-35fd-8430-9dd0bf34754a | -18.66796 | -42.00463 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| e33c9f37-1644-3410-9f30-23ecbdb07bb1 | -18.66249 | -41.99441 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| bc9ad18d-fea9-32e9-b641-48eb1ac3c6fc | -17.71149 | -42.35277 | 2026-09-12 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a26ad88-2a75-35e1-80f4-5ad3082c8f5e | -18.86333 | -44.08782 | 2026-09-12 03:32:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d235c9b-cb5b-30ac-9e5b-c78a5c11b505 | -18.66723 | -42.0081 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 559142bc-ce9e-357d-bcba-1b958b3e6b98 | -15.44877 | -41.38567 | 2026-09-12 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f0e4b71-77a6-3592-ad4e-3276f24078fc | -18.66162 | -42.00727 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| c2605802-2d98-3292-b281-a1a2fafc7dbd | -18.9367 | -46.82561 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| afb367b3-394c-3558-878c-5da6c0148979 | -20.38177 | -40.59357 | 2026-09-12 03:32:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 121f9c21-3142-311f-a77b-a469e48c203c | -16.62695 | -41.91976 | 2026-09-12 03:32:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fa527571-68e4-3b2c-8227-ab2f97e72d32 | -19.10936 | -46.75078 | 2026-09-12 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e45d1795-37d1-3d39-bb7a-b11d77bb7588 | -18.94389 | -46.82734 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80db3974-7dfb-3484-9d44-6c409fa7045d | -19.11634 | -46.75314 | 2026-09-12 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e0276bc-c4e4-317d-b5ac-2ef8f566a786 | -12.85643 | -44.3941 | 2026-09-12 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1cbec4e5-6cfd-3b9f-ad92-addb6f782f08 | -13.43849 | -43.81686 | 2026-09-12 03:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0430391-ace7-3d08-8fb3-16ec0220a430 | -18.66169 | -41.99803 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 975796dc-6863-301a-9d4b-729f71b15e82 | -18.66788 | -41.9962 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cfc66f1e-7299-3b6c-935c-61cb5c699199 | -18.40842 | -46.05513 | 2026-09-12 03:32:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3b3ae7a-b5ca-3524-bd79-1fc27ceba7d0 | -18.66397 | -41.99618 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c07cf545-491e-3168-9a02-8bbd909f59f2 | -14.38804 | -43.7891 | 2026-09-12 03:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0ec7088-434b-346f-a56f-d0f9ece6c951 | -18.66639 | -42.00299 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 474d277f-5655-3d79-8ff2-5e982594c4d0 | -18.87802 | -46.97248 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e293a1c1-0eb7-30f1-8cac-f2446c18adf7 | -18.88293 | -46.98271 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7c074e5-3912-3eb2-86b6-fde35f1084b8 | -18.6712 | -42.00745 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| d7ff93da-af88-3272-9d94-702596b4f331 | -18.70473 | -42.62141 | 2026-09-12 03:32:00 | NPP-375D | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8cc02d03-e956-3063-96d0-b6c1d89b6b46 | -12.8494 | -44.39254 | 2026-09-12 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd4c9f0f-a68a-3b80-a9b8-352960b16bcd | -18.94493 | -46.82808 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3521b36f-fa9a-3889-8ef1-677b09c316cc | -15.44619 | -41.38639 | 2026-09-12 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cb4d54db-ceb4-3e35-939e-b7d574c127d0 | -18.6632 | -41.9998 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 26c6bb3b-f3eb-37c5-a6e7-e91e67ce5365 | -18.65846 | -41.99496 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 65cea46b-babe-35c0-9e03-aaecf3378d88 | -15.4432 | -41.38414 | 2026-09-12 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ef5f06e-df59-33db-a389-242a0c5ec1b4 | -18.86447 | -44.08277 | 2026-09-12 03:32:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0804d65-35ab-37f3-9dad-f1c681449906 | -18.66562 | -42.00652 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 697883d3-b8d2-36cf-8064-37ce20b75bcf | -18.65765 | -41.99879 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 25e75046-13d6-3928-9403-5126f992f822 | -18.41365 | -46.06403 | 2026-09-12 03:32:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0213f740-5fcb-38cc-b65f-470c98355ff8 | -12.85242 | -44.39335 | 2026-09-12 03:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8d91cb65-290e-3c7b-bc8c-e4ad7dcdb18a | -18.66938 | -41.99794 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4fcdc1a0-6aa6-3f25-bc77-ed3bfac2b95b | -18.94201 | -46.83504 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f50b5769-da84-302a-bc80-67d8b9d4f402 | -14.39464 | -43.79065 | 2026-09-12 03:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31cda951-61d2-33f0-af06-07402524cdbd | -18.87585 | -46.98024 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17d8c7e8-1d64-30d4-afac-2eca164f03d3 | -18.66714 | -41.99955 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 1cc65e4d-5cf5-309b-84c3-3a838bc715d3 | -17.67886 | -44.20233 | 2026-09-12 03:32:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 682f8a2c-b5c1-3da7-bf11-60c620ab4bf6 | -18.66085 | -42.00187 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 93b61af6-5d4d-306e-aa68-aac8da244589 | -18.66868 | -42.00124 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| b5ac97e5-14ed-381b-827a-3ba6ab46239f | -17.7114 | -42.35234 | 2026-09-12 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dff6048-7f47-328b-9aca-361f6fdbbcb9 | -17.71719 | -42.3542 | 2026-09-12 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4310fb0-548c-32d2-8bd3-3da4393046b7 | -20.39578 | -41.21679 | 2026-09-12 03:32:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bee7d46c-f539-3703-8f4e-b5acd3fbbfdb | -20.37681 | -40.59283 | 2026-09-12 03:32:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 976fc0c7-e8d3-3f65-95d8-89c27f82094c | -17.67994 | -44.19756 | 2026-09-12 03:32:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16b2cd87-15c6-3e6f-bfff-1601bd0b98a2 | -18.87593 | -46.98074 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bf0d6bb4-97ef-3d8e-b57d-6afd36dc7aa3 | -18.93774 | -46.82637 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de015046-5dfd-3fdc-8749-cfd48c171638 | -18.65612 | -41.99707 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f9b9043b-c235-360c-9913-d92bf1f78534 | -14.3909 | -43.7888 | 2026-09-12 03:32:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 512231af-f907-3860-8969-b0af18dde88a | -13.43172 | -43.81549 | 2026-09-12 03:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d2d76d5-077c-3741-9837-48915ec2fdfb | -18.7038 | -42.62567 | 2026-09-12 03:32:00 | NPP-375D | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 796a3ddb-82c2-3039-a847-87bfe46f95ec | -18.9358 | -46.83411 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e4db4e3-c771-38ff-8c03-16a8f37ef83a | -18.66241 | -42.00354 | 2026-09-12 03:32:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 5b3bebd2-174e-352c-8275-19874064f33d | -20.37784 | -40.59452 | 2026-09-12 03:32:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1dd242ba-9e59-3ca3-8891-8dcba94aedc1 | -19.87118 | -42.63606 | 2026-09-12 03:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d79d46ca-01d4-316b-932b-0c47765187aa | -18.87789 | -46.97198 | 2026-09-12 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d52c3924-bc8d-3297-9dca-b4e6d12e41ce | -16.62578 | -41.92044 | 2026-09-12 03:32:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| afc51476-2872-3041-8e00-5f3b308d626a | -2.7148 | -57.6274 | 2026-09-12 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 37fa2c6d-1cd7-33df-b7c0-b7d9f68f06ac | -10.6827 | -54.1679 | 2026-09-12 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 06862deb-dc93-31d9-b9b5-1f1aa02cad72 | -6.6206 | -58.8483 | 2026-09-12 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 4b7b301a-7a97-3966-b202-71ee4d371ab9 | -2.7331 | -57.6271 | 2026-09-12 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c11b6d53-ae1f-3312-8243-d91d2a1a6871 | -2.7148 | -57.6469 | 2026-09-12 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 275bded8-d7af-3e20-8c9c-04252da4a774 | -10.7015 | -54.1663 | 2026-09-12 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| df52b3f2-bead-36af-99b8-948a4233c7ca | -2.7331 | -57.6465 | 2026-09-12 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 141dc6e2-72b0-3a08-9f7d-1f35e3e347a0 | -5.12227 | -41.08652 | 2026-09-12 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9abfa50a-3cdd-3a63-9796-01bd2ea5e889 | -5.47906 | -45.12778 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 154fe236-67c9-3d1c-8d11-c10f5cdcbeb9 | -7.26456 | -45.34914 | 2026-09-12 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc172a7d-8aa4-34dd-8266-cb2cc08f8b38 | -6.50878 | -47.60756 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe29d037-3907-3f27-ab55-d9a41107fedc | -7.25901 | -45.34826 | 2026-09-12 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c91ab376-34da-3c5f-898f-229d025ccd68 | -5.6129 | -44.84997 | 2026-09-12 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a5dc87f0-d274-34fa-be75-68e7ca56a2e1 | -7.26897 | -46.80995 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26e2d77b-c966-3e5e-b47a-5fbac102023a | -7.27587 | -46.80645 | 2026-09-12 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cdf68cb8-d630-3f28-888c-493d970ff196 | -7.05328 | -42.72494 | 2026-09-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 26e7a5eb-8172-309b-ab17-69c0611c2d3c | -4.83294 | -46.78137 | 2026-09-12 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 700c6f27-b206-34c1-91ae-2a3d14216055 | -5.75816 | -45.09132 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cd6a1cc5-d16c-36e8-9a75-38476012b6b9 | -6.50327 | -47.60135 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed425f6c-2d49-3d8e-b47e-46d1ca84cd1b | -6.61697 | -44.20419 | 2026-09-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8247a110-e589-3a93-9f32-cd4fb8bb87ce | -7.12752 | -42.10163 | 2026-09-12 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5025eaf-264c-3db7-b3cc-40103aeb7976 | -7.46243 | -42.11673 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e90f423-9aa2-34a4-b442-f1cd71827c40 | -7.4491 | -42.1221 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 16c129ad-85b6-3215-bf63-fcfc84b56167 | -4.35945 | -47.78704 | 2026-09-12 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e8376e38-0526-3d2b-a447-47f721305070 | -5.76158 | -45.09609 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| f5bc8880-1440-3409-b0fc-e251ac7d874c | -5.75665 | -45.09151 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96707a24-49a6-3f8a-9bdb-44da224719e7 | -5.79114 | -44.93133 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8bae73e-8b90-3262-8f68-3b8d63e641a3 | -7.27502 | -46.81116 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4811947-2e27-3e06-ab19-51e03c6048e2 | -5.77209 | -45.10162 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7344d57b-996a-33a4-988b-ce8628b37320 | -6.85557 | -47.43717 | 2026-09-12 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56398eb3-5735-3e8d-b749-3f947acc2924 | -5.47836 | -45.13176 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fe03fef-78f1-34ea-8c1b-dd34c93ff7df | -4.91556 | -40.66049 | 2026-09-12 03:47:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 238a0dd8-3531-394a-ad86-bde1a8aa9f9a | -7.19532 | -45.92627 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5634a004-afcc-386f-aba4-36801e0bfce4 | -5.76312 | -45.09594 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 02a76d4c-60cd-3292-b7f3-741f759389d4 | -6.50978 | -47.60218 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ec89e9c4-a1f1-3b45-8da1-9b330c9473ab | -7.27709 | -46.80389 | 2026-09-12 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e84bf080-5ee3-3a06-965f-86959ec7c7d2 | -7.41753 | -46.14997 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README12.md)
