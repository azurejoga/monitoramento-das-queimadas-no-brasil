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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 634b596d-13f8-3b46-9f67-4a6a151fc319 | -6.41641 | -47.71187 | 2024-11-10 04:16:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 767bc081-f544-38ab-857a-36ae9eaba4c3 | -8.40602 | -44.1552 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10096eb4-f386-3ce2-bbfc-3ec5c3f46eb5 | -8.39115 | -44.16356 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9f1591b-fbd8-3f0a-8329-9019d6230fcb | -6.27291 | -44.53917 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6090f2ab-e265-3267-9b0f-45b68e6c7b8a | -5.90872 | -50.21298 | 2024-11-10 04:16:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c521a07-a6d0-3a3f-8d62-444bab1857da | -8.3911 | -44.12078 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04bf8fe1-70ba-3b6e-b587-8599cc9414fa | -6.27566 | -44.73857 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b7ad995-48f8-3658-aed0-f24b91935347 | -8.37095 | -44.13842 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38145f99-c82b-34c5-a1fa-2df9f8637b72 | -6.31737 | -44.28096 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78888a1f-e119-3d8e-996d-f3728f2b4db4 | -8.40709 | -44.12686 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7b1abb0-9d8b-333a-87d3-548e1fdca775 | -9.08512 | -40.87951 | 2024-11-10 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 997a6def-5b8a-3354-8092-07cda3c008aa | -8.38891 | -44.13469 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9c95899-a51d-3ead-b698-3fa0d3f422e2 | -8.39279 | -44.15312 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85259627-c0b9-323f-9895-8d3bb3286199 | -12.62198 | -48.52191 | 2024-11-10 04:16:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dacf1bc6-0ed2-3c6d-a915-68557106128c | -8.37757 | -44.13946 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f5c01ef-9e2b-3d51-8189-8085326e2751 | -8.39829 | -44.13972 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3025a8a3-6e66-3fc3-b0af-d9d23f23857c | -7.20569 | -45.03089 | 2024-11-10 04:16:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fc720a0-557b-3f77-b29c-514b0a5df2b2 | -7.17254 | -45.39184 | 2024-11-10 04:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6316817a-27e0-3441-832c-c664c644e000 | -8.38394 | -44.12322 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 152f3c42-25ad-39d9-ab30-c696cf90f019 | -12.45708 | -46.81826 | 2024-11-10 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024538c5-9dd1-3f08-80b9-df4274faf9cd | -6.23196 | -47.2789 | 2024-11-10 04:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6ededc9-55cd-38ac-af14-54537a374f68 | -6.57392 | -46.75996 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3065b00f-5067-3cbd-87c2-e7dcbb84f602 | -6.73354 | -46.38363 | 2024-11-10 04:16:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d1a0dbc-f5ea-3c61-83e0-4402cffafcc0 | -8.39831 | -44.16112 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d440e204-338d-33e9-9812-6b13ff83eed4 | -7.20511 | -45.03453 | 2024-11-10 04:16:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26208564-0603-328c-9e8a-e35a678162ee | -9.21502 | -40.90073 | 2024-11-10 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c5870fc-602b-3a50-80d6-9f9e0a0741f3 | -11.76928 | -49.91793 | 2024-11-10 04:16:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c40e7f6f-7be2-3db2-865b-23d469bbfaa1 | -9.12638 | -43.17536 | 2024-11-10 04:16:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b68bff5f-0db3-3150-96f8-4398422a7789 | -8.37041 | -44.1419 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a08d41e8-3ecd-3112-877b-d3acb5257286 | -8.38563 | -44.15556 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c6b1d33-e034-3746-bc2d-5b065b9a43b4 | -7.225 | -44.99666 | 2024-11-10 04:16:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce96957a-7add-3c99-af7b-2a27d06b3548 | -7.45999 | -43.59174 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f254260-6d99-3af4-951a-6b4cd56e90a0 | -7.45668 | -43.59122 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0a14d90-e657-3cc5-a205-31918acf937b | -11.0266 | -48.79436 | 2024-11-10 04:16:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63f472a0-fcd4-3eea-b9df-6b52f2a87326 | -8.39553 | -44.13573 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fbff007-a486-38cf-a2af-c57046c530a2 | -9.13024 | -43.17237 | 2024-11-10 04:16:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f624621b-9ee7-302f-a2d3-0d3484104548 | -8.38177 | -44.15852 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5a21b29-666d-3106-8993-1e258f4b5774 | -8.39334 | -44.14964 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10c3f0e7-f31b-34dd-b344-0335770a03a1 | -6.18085 | -45.44445 | 2024-11-10 04:16:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09270862-ef28-3835-98b5-f7ae38527a18 | -8.3856 | -44.13417 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5c08422-4df8-30d4-8172-5f1d6cf1bab6 | -10.69483 | -42.69022 | 2024-11-10 04:16:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db312167-4bae-366a-9732-ff8b45c31227 | -8.39774 | -44.1432 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef44ac2-41b4-3348-acf1-1af8f6d3b22c | -8.3823 | -44.13365 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 500089a3-f68d-30f8-b863-9db3b97e6fb7 | -8.40107 | -44.16512 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 841caafe-f2c5-336b-a8c1-c93257729fcb | -6.63573 | -47.56831 | 2024-11-10 04:16:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a46ae841-2098-3c7b-aa6a-88c821306d5b | -8.37901 | -44.15451 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 375c80ea-cf37-3e8a-887b-5f737f459f33 | -7.92521 | -43.79372 | 2024-11-10 04:16:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2b37af77-b643-3d51-be59-7da27aa25c70 | -7.43135 | -39.7706 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6ec94495-0edd-3bac-b443-d1b150e32185 | -7.46713 | -43.58931 | 2024-11-10 04:16:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80c3e1f5-8cbb-3105-ad13-d6d7d10e7c2c | -8.40105 | -44.14372 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5563a810-0735-31bf-8cd1-93d4c263b3eb | -8.38672 | -44.1486 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d211ff0e-7ba7-35a2-b175-c2165cd84f0f | -8.40876 | -44.13781 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 759823a3-a5cf-310b-be4b-4398a24c5507 | -8.38893 | -44.15608 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba940e87-4234-372f-bc77-91d01f58b7d9 | -8.39277 | -44.13173 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf9a15a5-2da0-3e62-a9fd-59619967d8b0 | -10.9994 | -49.35588 | 2024-11-10 04:16:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e456861-5187-3d06-a6d5-3ee043ac76e1 | -6.27904 | -44.7391 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 469d0453-d999-381a-aff0-29cc94b418ce | -8.39222 | -44.13521 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53e14e55-ba1b-38b9-8f33-7170b95ee078 | -6.98839 | -40.03825 | 2024-11-10 04:16:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8db3eb78-411d-3cc9-b2c4-d46dba5f4e0a | -8.38011 | -44.14756 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e4c6220c-27f4-3d5f-8429-c2f53921b8f7 | -8.8114 | -44.08467 | 2024-11-10 04:16:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dea6456d-39d5-3839-a62f-6811e83baa13 | -8.37589 | -44.12851 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7e6046c-c23d-3245-89e6-d48ca31b1711 | -8.40712 | -44.14824 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e3dd65-597c-36fe-b404-ada64b6d27f9 | -8.41207 | -44.13833 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdd5d303-7b1d-37ff-8569-c13f8bacd630 | -13.00621 | -42.67134 | 2024-11-10 04:16:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 94cf4d05-0a21-3594-ac42-f6658cde32ab | -8.40217 | -44.15816 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59a6b23b-b463-3d6f-88cb-00fddf074c9b | -8.37975 | -44.12555 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b428a246-f7a5-39b2-a24a-d6bf549b5a74 | -9.59731 | -36.0318 | 2024-11-10 04:16:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e967f236-acab-3bb2-8a6f-c6e7472e3795 | -8.40657 | -44.15172 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa9cefc1-7b46-37dc-8341-634d465b973e | -6.32898 | -46.71968 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 555154bd-73cd-3534-b2e5-259cc8e5a263 | -12.47066 | -46.95165 | 2024-11-10 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5f9fe36-ad23-3817-8b25-509dfb1fdad6 | -7.94651 | -43.17596 | 2024-11-10 04:16:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e982c236-7d46-3e20-b86f-169a0f58dc9b | -6.26955 | -44.53863 | 2024-11-10 04:16:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b065320f-ac44-3241-81fb-b39bd8f13d13 | -7.43508 | -39.77104 | 2024-11-10 04:16:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 380fe8c3-fcf1-38bf-a3b9-4544fd285a62 | -6.48134 | -47.51043 | 2024-11-10 04:16:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bf761c6-946a-3771-8105-8247aff9ec7b | -8.41209 | -44.15972 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43908d7e-de80-3904-9e32-10e5fe8d03a8 | -8.39224 | -44.1566 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c6351a0-9225-319b-ba16-736edab3f621 | -6.67257 | -43.53794 | 2024-11-10 04:16:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e844172d-400c-3b3c-b45d-784331148434 | -8.38506 | -44.13765 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2926ffd5-06cd-3897-8ede-db15c80a6d72 | -8.40436 | -44.14425 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9aa59de-d9cf-36d9-9f05-8d534540e7f5 | -9.16349 | -40.48215 | 2024-11-10 04:16:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 85ea8eaf-c4fb-381a-b47d-88a27d3123f2 | -12.15607 | -48.95214 | 2024-11-10 04:16:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ab10ab-c81a-3663-9257-36050bbe0d66 | -8.40103 | -44.12234 | 2024-11-10 04:16:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c9919d-63c1-3282-aab0-d51e8501d969 | -17.61961 | -57.51538 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 51c1e4f7-67ed-39b9-8602-943117f9f31c | -17.62064 | -57.5107 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 5ebd407c-b9d8-3d23-8dd8-2070d78b4b5f | -17.61548 | -57.53413 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 070cd315-ff29-3000-a930-c0d62b62694b | -17.63071 | -57.49346 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1a56e111-8147-3457-890a-1c1bc425d0a4 | -17.24935 | -57.48727 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8468733e-46b6-35c0-801b-3d0123c7a0b8 | -17.62372 | -57.49671 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7b35826a-9d07-3673-8d59-a3fb51bdc31a | -17.26006 | -57.48983 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ff85cb41-d51c-3047-b46a-0acc1da80ef2 | -17.30054 | -57.48424 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| fa7bc5a2-5e6a-37c5-9cdf-d27834bf7273 | -17.62661 | -57.5121 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 04561be3-c7c3-3886-a8dc-8c4a79125fe6 | -17.6032 | -57.46692 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8cecf4d5-34d0-3626-b953-ccdb73c14018 | -17.62305 | -57.44283 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 52d758d6-3c7b-3f28-9b64-2bf37186d11c | -17.63361 | -57.50883 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| bcee120e-8468-3aec-96ea-6379bb5734a2 | -17.29349 | -57.48756 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| f4cff509-0f64-37b9-bf32-ab56a6b517aa | -17.63156 | -57.51818 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 11f89eb4-8d5c-3dbb-8415-bca67e206b7b | -17.24333 | -57.48589 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f9027a17-b733-303e-b532-1126699c49fb | -17.2995 | -57.48895 | 2024-11-10 04:18:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| d783bcf6-a6c2-3938-9eee-4e9b3c3236e2 | -17.62249 | -57.53083 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| cce0ef34-f39e-368b-977c-9044b3a0cb3a | -17.61363 | -57.51398 | 2024-11-10 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |


[Clique aqui para ver as próximas entradas](README54.md)
