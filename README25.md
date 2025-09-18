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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c134d2d3-590f-3199-9f5c-4059b35db922 | -15.96886 | -38.95152 | 2025-09-18 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 619242da-a3ca-3bb4-81e7-b2603102d870 | -17.16012 | -49.37197 | 2025-09-18 04:17:00 | NOAA-20 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2863f38c-3c6c-3aa5-90df-0e657e533014 | -21.19308 | -50.15233 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d94db003-4056-34f0-baae-f2e62c31d29b | -17.69018 | -44.08462 | 2025-09-18 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6793e9ed-c7e1-3345-9a36-6ab22742f0f4 | -17.18754 | -45.90899 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a7271da-80ab-3c32-810a-7b6ca56de288 | -17.32154 | -42.63411 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c43dab3a-574b-398c-b841-2c4a859f8b64 | -19.7763 | -48.31141 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c52ccb3-336c-35aa-a7dc-3b15fbe64787 | -18.53279 | -46.05672 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de8cc5f8-50ae-34fa-9c0b-e7c16503fea5 | -22.17767 | -42.46795 | 2025-09-18 04:17:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a1498ee8-df71-3c40-9b4c-bb71e496e873 | -19.03423 | -48.27531 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fbd81fce-2d6e-3426-8e83-976da5d92063 | -18.53668 | -46.05367 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c667193-e517-36d8-aadb-af5adb548d6b | -16.62289 | -47.01618 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e83e7c05-7e24-3b6c-a4ed-10d06180cc46 | -17.19921 | -45.89989 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afe103b0-049c-32a1-b831-305d93ff08be | -16.53438 | -44.90189 | 2025-09-18 04:17:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 122f05bf-95f4-31eb-825e-fd004b0b8411 | -16.53494 | -44.89828 | 2025-09-18 04:17:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4462f65a-0280-3015-81eb-b076fd3742c2 | -18.63168 | -43.88845 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56f1ebce-08bc-3fd7-9c3f-547afd9b7b33 | -17.77374 | -44.43294 | 2025-09-18 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c35c5c8-dfd1-3416-b5e0-c8f68e929357 | -21.9224 | -48.25047 | 2025-09-18 04:17:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc9e8021-0a2b-30ce-ba80-735273df822b | -15.88775 | -43.46414 | 2025-09-18 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7ac5588-2251-3276-b3f0-c266b3326fcf | -18.87934 | -48.24011 | 2025-09-18 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae2ef319-bd4f-34d9-80d5-abf35525fcbd | -19.34152 | -47.93466 | 2025-09-18 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 974db6b5-98df-384f-ada1-495443cac21a | -18.11842 | -44.65869 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2965b73-0c6e-3f86-a73c-1307999b6b78 | -17.68455 | -44.14528 | 2025-09-18 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99ed8c78-1042-357d-b0b0-c5d28802bac7 | -18.61513 | -43.62069 | 2025-09-18 04:17:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98496f0e-45c0-3c93-ae78-98d7aa88695e | -20.01531 | -47.68578 | 2025-09-18 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e8bb187-7bf5-362a-bd81-62772ae7500a | -18.98194 | -46.98435 | 2025-09-18 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 312b8cea-347f-337b-9948-9658929bf992 | -17.33918 | -46.79998 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a78d9ec-bd3c-3bf7-b1b1-298127fcb20a | -17.68961 | -44.08842 | 2025-09-18 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d6ee3b9-4b5a-3c90-8190-fd8fd824802e | -18.97921 | -46.98006 | 2025-09-18 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bc286ef-80fe-3837-b4a6-fbb7b937e3c8 | -21.17691 | -50.15843 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 2aaea9c7-fc2f-3aa0-bfd3-4039e9677b61 | -16.22862 | -40.11778 | 2025-09-18 04:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8a4a1a14-fdd3-3a6f-88b5-3e74265d3608 | -19.26588 | -47.24487 | 2025-09-18 04:17:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91d11013-0f9b-3f76-8326-412e874c67f1 | -16.28222 | -45.68477 | 2025-09-18 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4751007-b8e7-376e-b95a-db851ae19a31 | -15.74372 | -43.93173 | 2025-09-18 04:17:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1098184d-96f8-39f3-8961-af0053027abe | -16.02732 | -45.17172 | 2025-09-18 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a05324-269a-339b-8860-587121fc208a | -20.34807 | -48.78735 | 2025-09-18 04:17:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7dd33657-eda8-3f53-81b3-d9dd4a96a9d4 | -16.53826 | -44.89883 | 2025-09-18 04:17:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0e2fa5d-e695-34ba-86f9-93ec7c81bb71 | -19.19319 | -47.20487 | 2025-09-18 04:17:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53f70f97-1f96-3b8e-87a3-25b5adb0851a | -17.38254 | -49.23722 | 2025-09-18 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f81c91-2519-3f63-98b7-1ebeceeed002 | -14.64614 | -46.38322 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79367495-90d0-34f3-affc-51f3ef4284e1 | -17.33759 | -42.62368 | 2025-09-18 04:17:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d9d5c6f-b11f-3306-90a9-05424ca5dedf | -19.63784 | -43.73914 | 2025-09-18 04:17:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d5e4c73-79ae-336b-8e43-19f64bfa1783 | -18.63225 | -43.88455 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c75915f-6049-3203-b5a5-2c21db340a3a | -17.0122 | -41.24878 | 2025-09-18 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e604f1cb-1b96-3da8-a8b8-07447d32e580 | -15.51068 | -47.84094 | 2025-09-18 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f59edae-4164-323a-bb04-4814851631f4 | -19.69247 | -43.63153 | 2025-09-18 04:17:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb287f13-89f7-32d4-a743-09872327beb5 | -21.23658 | -47.12209 | 2025-09-18 04:17:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21d43f16-30ae-3c86-b603-3e6005763751 | -21.78065 | -47.79097 | 2025-09-18 04:17:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dfb71252-2637-3459-bb4f-3f3fa1a14455 | -18.89738 | -47.2487 | 2025-09-18 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79e633bc-2875-3a93-851d-7f848d68c4d7 | -19.77178 | -43.73411 | 2025-09-18 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a261687-dda2-3fbf-9734-3ce80df65052 | -19.97796 | -46.75029 | 2025-09-18 04:17:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82aaccb6-bcc8-351f-a200-205a040d5a71 | -18.13743 | -44.64659 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1be60fa5-61c0-3e32-882f-d7edcbdf08d0 | -18.898 | -47.24495 | 2025-09-18 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f0d8603-1efb-3c65-8e73-94e64ca32d11 | -17.83564 | -44.73777 | 2025-09-18 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b32648c-90e8-3d19-b713-a18b12cdb0ff | -19.91714 | -44.58018 | 2025-09-18 04:17:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4663c06-6efa-37cc-b0ea-6f25f4cdab89 | -22.17099 | -44.74963 | 2025-09-18 04:17:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1a823409-2c77-3d37-a96a-2c911ef61a4f | -22.15185 | -46.96481 | 2025-09-18 04:17:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6e70320e-ecbf-32d0-93ea-08e567341752 | -18.54114 | -46.04699 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d24c524-6227-343f-9420-3917c89aaecd | -15.83133 | -42.71191 | 2025-09-18 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| eeccc3f3-e709-333f-9b55-131c104dd53a | -20.00641 | -42.23709 | 2025-09-18 04:17:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c0a5f40-0778-3559-8c36-30c67eeec7e4 | -18.64029 | -43.90162 | 2025-09-18 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5db7cc8f-596a-36f8-9795-b60a0d2c9be6 | -19.63842 | -43.73505 | 2025-09-18 04:17:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ded92ab2-330f-3cd6-b651-a0915991c288 | -18.11727 | -48.09187 | 2025-09-18 04:17:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29203a05-1f3e-3af1-a83c-0089443717db | -18.12073 | -48.0925 | 2025-09-18 04:17:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cbd40b3-cd9b-39bc-9bd9-4208b5dbef20 | -18.76121 | -49.32331 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cbbe2adc-711b-3722-8377-e4d409ef4603 | -18.5882 | -46.56007 | 2025-09-18 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85cd33cc-e348-3942-8189-e67c4419c799 | -20.18048 | -44.62125 | 2025-09-18 04:17:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 702cbae5-6f71-3186-8a38-54077de48efc | -16.71823 | -48.48132 | 2025-09-18 04:17:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84dd4e29-bdbc-38e8-8495-6a49fbb3780d | -17.34011 | -46.81535 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a441b263-f66e-3da6-b817-7ae46ca77ab0 | -18.69123 | -43.74522 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b7308e3-21c0-3d70-92e7-0c563133f9de | -15.88602 | -47.30818 | 2025-09-18 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be489aa3-eeb4-392a-860c-58dab8b9ed0a | -17.41402 | -46.98505 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0185d051-c125-37f3-8889-0a71e12747cd | -17.2417 | -43.43344 | 2025-09-18 04:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404e7c4d-9dfa-3cb8-9e02-fa18f58da717 | -21.10214 | -49.12929 | 2025-09-18 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4ebd6cf-9a1f-3520-abfd-048f4f30c450 | -17.32212 | -46.81989 | 2025-09-18 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4476b5b9-284b-3b00-ada4-c6f644f69cca | -14.60478 | -46.33129 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585a55e6-fd60-3f3e-8210-571f1822054f | -15.77819 | -49.80058 | 2025-09-18 04:17:00 | NOAA-20 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28682c6b-e129-32f3-90bc-df31500df9ad | -21.18865 | -50.15609 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3e0a6ff0-539e-3ffd-a907-bb3efd8c9a24 | -21.18056 | -50.15916 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a6063ab8-5e57-3794-b147-c6c2e8b05f0a | -18.33982 | -43.30508 | 2025-09-18 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 401c707f-e53b-3c3a-9af7-31db856ce523 | -18.75036 | -49.32131 | 2025-09-18 04:17:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5232b7a8-be8e-376c-8f6f-d76a268ed949 | -16.28554 | -45.68534 | 2025-09-18 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7d4174b-18f7-3ce7-b08b-cbd8b5db997e | -18.39841 | -44.0976 | 2025-09-18 04:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9733e20c-01ea-3c70-ae5a-aa2a723b5a9d | -21.23598 | -47.1258 | 2025-09-18 04:17:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07e11877-ba23-3afc-977e-949a83522f63 | -20.47829 | -45.36891 | 2025-09-18 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b343d5d6-7c5d-3248-9940-d44519726a71 | -16.22897 | -40.11726 | 2025-09-18 04:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 066cf71e-d9ea-37ee-a925-71c0d622b780 | -17.71718 | -46.77823 | 2025-09-18 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4faf5ae0-d4c1-36d2-aac1-6943758036bb | -17.1848 | -45.90482 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a334857c-eb15-3ee6-ae8c-3e32d4784be0 | -18.7892 | -44.61747 | 2025-09-18 04:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d67cfb0-fb5a-317a-b54d-0c5bb1ffeac6 | -17.76729 | -40.18778 | 2025-09-18 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| b8782e6f-2c8a-34c6-a572-d04c0ea5babe | -25.17344 | -52.39938 | 2025-09-18 04:17:00 | NOAA-20 | LARANJEIRAS DO SUL | PARANÁ | Brasil | 4113304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fff512d6-88f1-33c4-84e2-281017081bf0 | -14.64554 | -46.38684 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 093fbb83-916c-3aa0-94f2-6fac47be8e43 | -21.19297 | -50.15006 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d16159b0-ef6b-375a-8a34-9fdade2e230a | -21.30582 | -48.55455 | 2025-09-18 04:17:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 572d7987-1e63-32cc-8d3d-251ac35e15c2 | -21.18487 | -50.15309 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| dea76f62-f395-3f51-b463-cc469fda495c | -21.05386 | -48.83835 | 2025-09-18 04:17:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d12e600b-3c42-32b5-b57f-0c2ace095307 | -16.5377 | -44.90245 | 2025-09-18 04:17:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43c8a0db-3c12-38e2-addf-ac4ba544c91d | -15.81304 | -59.41657 | 2025-09-18 04:17:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84753747-6e49-386c-bad7-e65c646669b9 | -15.91355 | -43.87823 | 2025-09-18 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4f6d5ae3-4723-39a6-8a35-74b4e45464b3 | -19.83536 | -44.9635 | 2025-09-18 04:17:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
