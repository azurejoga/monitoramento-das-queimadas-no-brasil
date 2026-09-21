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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc8bc98-025f-38f3-b85c-55e19da780c4 | -15.03162 | -41.50234 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 407657ad-4924-37d4-86f6-bf7b47746619 | -15.5262 | -41.63223 | 2026-09-21 15:58:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 843a818c-17c7-303b-9f88-789de80442d0 | -15.25661 | -47.60787 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 0a33c951-681e-3878-b749-08532e7ce4ba | -15.57701 | -40.75741 | 2026-09-21 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 01ddb595-edb9-3ed1-af47-9fac93fdc83c | -14.69713 | -41.944 | 2026-09-21 15:58:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15c4dd14-bbb2-3a32-811b-439098f73dc1 | -19.12281 | -46.60442 | 2026-09-21 15:58:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a8575027-4c39-3f73-8f71-1471c596af58 | -15.78294 | -42.50542 | 2026-09-21 15:58:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 44707df0-61b3-36da-a3ae-8e9870073dca | -15.53469 | -41.03947 | 2026-09-21 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4ae3fcf0-0d9d-36e3-9b0a-86e4f885aa72 | -15.25597 | -47.60201 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| bb78f310-428f-3305-b4cb-c737910b0cf4 | -14.66523 | -45.67924 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 642af348-e89f-33af-8b20-45d8fed43096 | -15.73016 | -41.806 | 2026-09-21 15:58:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 1c1dac0c-818d-37ec-803f-3695b963dbe7 | -14.62918 | -41.40529 | 2026-09-21 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4613b93d-f807-3881-96c8-bde6f20683d0 | -14.53047 | -41.57041 | 2026-09-21 15:58:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 667cc15d-6115-3fd4-9259-992b00e5f1c2 | -18.78399 | -39.94407 | 2026-09-21 15:58:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1189ff12-9e86-3aaa-a07f-aef437a5f45e | -15.68077 | -45.381 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5ff2a24d-7c7a-3429-add6-438588bd00f5 | -14.48004 | -40.92801 | 2026-09-21 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 74f6d380-bfcc-3c52-8505-3c4ca2a2ff33 | -20.11899 | -47.8172 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0e4bf691-41b9-3ce4-bc45-d18ba506934c | -14.68861 | -41.98172 | 2026-09-21 15:58:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2844cfde-9d0f-38a1-bd45-ac948c5de5d5 | -14.9037 | -41.10294 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| aebc2cc1-d7b4-3b68-8d4d-cd19351d8eb8 | -15.26217 | -47.60169 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 00bcf871-6769-3f99-b35b-a762ba412128 | -15.02274 | -40.98423 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 3ac00a33-b5b7-368e-9423-f33079e8b023 | -16.30758 | -49.36076 | 2026-09-21 15:58:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6a5d15b9-e55f-33cc-8b58-318fce51953a | -16.36214 | -45.97448 | 2026-09-21 15:58:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d572b78-6035-35bb-b6de-115e306fd4c2 | -14.64383 | -40.80868 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 42.7 |
| 179044e9-8a16-3f52-82d1-b97d9725dbcc | -14.54061 | -40.3082 | 2026-09-21 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cde3e7ba-2371-38ff-a827-6b2b049947ff | -15.14888 | -39.89769 | 2026-09-21 15:58:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 52922f79-deff-31c6-a9ef-6d380017ca40 | -14.67645 | -45.68155 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 33c76607-e6da-3242-ab9b-8652ace7fd3a | -14.30704 | -40.80242 | 2026-09-21 15:58:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 77a5d142-954f-39da-ade5-4f5f460d8735 | -15.05359 | -41.15998 | 2026-09-21 15:58:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 815ab93b-ca63-3e5c-b302-b61fa1e20a4a | -15.77929 | -40.2997 | 2026-09-21 15:58:00 | NOAA-21 | MAIQUINIQUE | BAHIA | Brasil | 2920007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 550c103d-f2d0-3713-aa09-c0fa36e5bea0 | -15.68038 | -45.37751 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8a390d8-6c28-3a45-a8e0-1d5130637ad3 | -15.23202 | -41.48186 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0081ee1b-b861-3605-81b7-1899c644cafd | -14.58103 | -41.70852 | 2026-09-21 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 05a02a99-c042-36dc-bc63-0eafe3f184f0 | -17.08096 | -46.17214 | 2026-09-21 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ab6e18a5-a6a0-3374-87fb-bd111fddd44f | -15.25653 | -47.60706 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 902cd68f-3a41-3a8e-97b7-006469484c26 | -17.37755 | -46.76061 | 2026-09-21 15:58:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50d4dce9-ab4d-3328-b514-2113619bf9b7 | -14.64779 | -45.67039 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b0ad98f1-aaee-389b-b511-6e9521200220 | -17.27972 | -42.41435 | 2026-09-21 15:58:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b859686b-4b8a-3a81-b642-4b6ff7c36917 | -1.3557 | -49.3157 | 2026-09-21 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ffb9d7c1-d954-3cdb-b96f-450cd4de855d | -11.8014 | -49.8129 | 2026-09-21 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 76e1ebca-e06c-30f8-8199-cfbccd9b9d04 | -10.6691 | -50.7316 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2ac66653-9bb0-3ad9-86f6-b8c447dcbbef | -10.2979 | -50.2372 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 672213f2-309c-30fd-bc4e-6c9ed2288c34 | -2.8974 | -57.8181 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 2038adeb-2cd9-3742-9f17-84e928fb28de | 1.1319 | -51.019 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 8c7eff56-e9bf-3af9-b46c-b015d0cc544b | -10.809 | -50.1836 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b0e9d309-7521-328e-8286-52ee33ac2044 | -0.803 | -48.6825 | 2026-09-21 16:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1259dab3-4d3a-393e-b556-32c0cc414cb7 | -10.8093 | -50.1621 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 175.9 |
| f35b56ee-a223-3d9a-99f4-1faaf6ad7248 | 1.1503 | -51.0188 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 29de27a5-b3f0-374f-9d93-067658de0521 | -1.1345 | -49.2123 | 2026-09-21 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 493a401d-27e0-390a-948a-dee807d3eb58 | 1.2607 | -51.0175 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 4897cee0-4640-3e5a-8c80-8d0637351be6 | -6.8468 | -55.2617 | 2026-09-21 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 9520e559-d09a-31f8-9c81-5fa2e869a1ce | 1.2424 | -50.997 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d4e2713f-1e21-3e31-be0c-3d73b9ab4b2c | -2.9157 | -57.7983 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 2ba84865-95f6-3c45-9553-52d85abc6589 | -6.5634 | -44.9084 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| b40c4b2f-d02c-3918-9d1e-d4f0b198248e | -10.8279 | -50.1815 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a954bb90-49d3-36a3-b409-663ab1ad7856 | -6.5567 | -45.5886 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6678c47b-a76c-38e4-910c-bf4d1fade279 | -8.1686 | -54.7634 | 2026-09-21 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ff49faba-1274-3ea5-adf0-8085bbe87760 | -10.67 | -50.6678 | 2026-09-21 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| dfd53570-101e-3d45-a470-33b3c70f8cac | -10.09 | -50.2581 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 6b4cf88c-f507-33df-bd87-8f254f9e5dbf | -6.5759 | -45.5419 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| da7d7fb8-51f4-3b4d-a285-b9895a482973 | -6.2832 | -59.9202 | 2026-09-21 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e8087346-3d55-3d9e-9fb7-e4e6408d5775 | -10.3916 | -50.2916 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 9dc2ccdd-6264-3324-a715-c9610358b1f7 | -2.8974 | -57.7987 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| ea30f0e5-0035-3903-b8a8-d07e8a4020a0 | -10.2545 | -68.7679 | 2026-09-21 16:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e7467b97-23ad-32a3-959c-fd23e5e3c31d | -10.7061 | -50.7915 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 438.8 |
| c50d6cb9-7ffa-3c64-949c-45d7853da81a | -6.9225 | -42.9088 | 2026-09-21 16:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 6f083d16-6d42-36b7-8b5f-4c24b4692071 | -3.5893 | -59.0773 | 2026-09-21 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 79393a40-8331-3899-962c-5e61e8e85719 | -9.3986 | -48.3213 | 2026-09-21 16:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ed03e292-ef5c-3630-b2a8-a00bfa072f1f | -9.8689 | -48.4252 | 2026-09-21 16:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 37b11ed7-542a-3630-aeef-deedd41f756c | -10.126 | -68.2891 | 2026-09-21 16:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f0c3e6f1-5d17-36e7-aec7-ec713df43a90 | -2.9156 | -57.8371 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 395d6c14-3259-348d-b6ff-d758fb777dd0 | -10.0898 | -50.2795 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 4fced09f-77f4-3fe7-a84c-6f4de37ae115 | -7.5477 | -61.3247 | 2026-09-21 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5bb01029-1892-3122-b139-dfc70e1e9f5f | -4.0925 | -62.0874 | 2026-09-21 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 66743820-7e6e-3ae3-a65b-fc87dc51b86b | -6.2949 | -57.7545 | 2026-09-21 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| aa048593-e5dc-3b68-b932-9e5345acd4bc | -4.0944 | -52.1252 | 2026-09-21 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c6c05092-77f7-3d4c-ae71-8a6bbb4e9478 | -8.6606 | -68.692 | 2026-09-21 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 3d009edb-65da-33a5-ba49-8970f7b6a7c9 | -11.8559 | -49.979 | 2026-09-21 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ff4a81ba-6f8a-3a74-a68d-03e12f150674 | -10.4108 | -50.2683 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 984577f4-b1bb-374b-996f-9e2dfef710d7 | -2.9157 | -57.8177 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 270.2 |
| b31e7474-8b94-39ec-a9fc-7fdbb7aaee49 | -3.3322 | -59.4086 | 2026-09-21 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e8c1a5ce-49d5-372a-943c-cc8229ae399e | -3.8651 | -58.7056 | 2026-09-21 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 72942f62-b09f-3d55-92a7-542a9cb50f4f | -8.0708 | -55.3321 | 2026-09-21 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b6906697-bb9c-3e67-9d20-158793008b9c | -6.5444 | -44.9327 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0baba942-9466-370f-91ea-9480dc405709 | -10.3549 | -50.2099 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 7a477b23-bf56-3542-88ab-9bdde6a9d49c | -11.0223 | -54.1379 | 2026-09-21 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| f9fc1b72-8bc0-3732-a79b-be4335dc6e00 | 1.2055 | -51.0182 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 950b81a7-9fa6-39a8-b592-dda251888ede | -7.3289 | -55.2155 | 2026-09-21 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b21383ff-4502-37b0-9e05-1287d623c214 | -3.4828 | -57.9803 | 2026-09-21 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| aa0acf2a-16a9-3b72-a692-2a2b1babd50b | -7.566 | -61.343 | 2026-09-21 16:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b03f2e73-d2be-30ca-83bc-d98b5b10df6d | -6.6015 | -58.9651 | 2026-09-21 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1a727f1d-3095-3970-8a9e-a47e3f8040b5 | -10.6883 | -50.7084 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 57163537-565e-3f1b-98fb-31d2027a2d7b | -10.279 | -50.2391 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 44682037-d8dd-321a-9f47-127bc12251fe | -2.9526 | -57.7006 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a1e6c4d7-062d-3e65-9497-9263b8945b60 | -9.8686 | -48.447 | 2026-09-21 16:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d4586358-1e9b-3ef3-bebf-2451a81a5f1a | 1.2056 | -50.935 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7e4eee12-d0df-378a-8791-0c2cc15887d4 | 1.1318 | -51.0398 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5fca6e7a-0d90-30f4-ad9c-525f3bec9767 | 1.1503 | -50.998 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b9bb1b4c-1c7a-3cd4-abbc-d1c141dcae63 | -8.1688 | -54.7432 | 2026-09-21 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9b505a30-6024-3417-b128-895387556e39 | -7.8632 | -70.5959 | 2026-09-21 16:00:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 161.1 |


[Clique aqui para ver as próximas entradas](README149.md)
