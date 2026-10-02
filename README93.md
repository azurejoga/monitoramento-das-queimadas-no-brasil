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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 154348ac-e505-365c-a311-5264aa8e4348 | -16.84874 | -41.78499 | 2026-10-02 15:52:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 3862fa1e-df6f-35f2-b653-6751d4117b2c | -16.15272 | -43.63471 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a3535fd6-331c-3105-a936-fd80dc9eae1b | -13.88633 | -43.63868 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1d5e145f-bab9-3c07-8738-96db95c9561c | -17.5164 | -43.75772 | 2026-10-02 15:52:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91e07cd3-1f93-3f08-92db-8a51193b7252 | -14.81577 | -42.80707 | 2026-10-02 15:52:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f7d58409-77ec-3188-8df1-80a916a46cf9 | -15.23426 | -40.93869 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 95bda5fd-271f-30d3-ac80-2a269e4072d8 | -14.48114 | -40.71871 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 636adc95-9f75-36a9-b56f-6a6e28e405bb | -14.48837 | -40.21157 | 2026-10-02 15:52:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| eaa7f8e4-bf91-3711-a3f0-4f7e538032f8 | -13.29196 | -41.00594 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5912a73a-b500-339f-9f60-82c6297627c8 | -15.16995 | -43.66665 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 91f20ca8-10b8-3ac5-a2eb-5fb4729666f9 | -15.78237 | -43.65197 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| df13f544-f374-373e-9346-61f41cff4aa3 | -15.03845 | -41.12391 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d632d459-cfb8-3c6d-9364-9567c9bc111d | -16.83116 | -43.5689 | 2026-10-02 15:52:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a347e48-5467-3370-9497-3a67dfbbc735 | -15.3008 | -41.42253 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| d9789338-2fb1-3e0c-9a29-d33c1648f620 | -12.92692 | -40.01905 | 2026-10-02 15:52:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| aa0f534d-31bf-3e00-a9e6-b4d24aa2204a | -15.38766 | -40.83968 | 2026-10-02 15:52:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 07bbf7e5-59af-3de5-943f-ac76cc3d5666 | -13.50934 | -40.8304 | 2026-10-02 15:52:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 2bae193f-a73f-3132-a60e-657043146760 | -15.77452 | -43.64281 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b874213c-fc63-360d-b96c-622b29bbff40 | -16.53142 | -41.90148 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3e5fd71f-e04b-31e1-9aa5-74805ef2d66d | -16.15805 | -43.634 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 62541b0b-1f5a-3e00-b634-c4ce428d702a | -15.93603 | -44.51182 | 2026-10-02 15:52:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d3abb1c-1dbc-34a7-bb57-6db1768d444d | -15.33626 | -41.73983 | 2026-10-02 15:52:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 769c13b8-bc1d-387e-b52e-67e9c1b40300 | -15.52809 | -43.01806 | 2026-10-02 15:52:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 96557008-b6e5-3b3d-aca4-0948351bf292 | -15.76918 | -43.6433 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4100eee1-d5cb-3466-9f35-736c9287819f | -15.79074 | -43.96099 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 275a67cd-e9c5-30ed-92f5-a70e7a6d86d5 | -15.82758 | -42.61626 | 2026-10-02 15:52:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 447b03b3-ebea-3cd7-ac5c-1580588ab2e6 | -16.08909 | -41.61436 | 2026-10-02 15:52:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 75db2dfc-3ff3-3049-8a72-29738da0cbce | -14.43946 | -42.44373 | 2026-10-02 15:52:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| b61b92fa-61de-3782-a1ec-f88d0542d1eb | -15.02032 | -41.45177 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d9f09f1d-0966-317a-958f-89ae0c151d42 | -13.86481 | -43.63475 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f477f389-db69-3692-abd6-b9734d3bbc98 | -16.52491 | -41.7183 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 70483b87-9e00-3e52-b77e-e1411fc677d9 | -15.13868 | -43.57886 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 18.2 |
| fdf60f1d-51a7-3677-8045-19fd58319d77 | -13.8268 | -45.23963 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8acbca67-6e79-34ea-86e1-94bfba2e3a14 | -14.51617 | -41.31442 | 2026-10-02 15:52:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b1bb1db9-49f1-31bb-a7c3-fc7c71c391fe | -15.68616 | -41.32756 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 1bc871dd-6dcc-3665-84c2-899f27bf56d9 | -15.78159 | -43.64524 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7fe3e8c9-a818-3674-ab5f-10b634278522 | -15.91555 | -46.01656 | 2026-10-02 15:52:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a8f0bf7a-74ab-3ba9-b466-cd6b9156dbd2 | -15.51116 | -41.57204 | 2026-10-02 15:52:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 687f7268-105a-3dc6-a039-386b2f639fd3 | -14.53393 | -43.79385 | 2026-10-02 15:52:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03d80732-ecd0-3697-aeb6-b50c2b7bd402 | -13.55183 | -43.52035 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e11185b1-ca20-35bd-9e7c-11b1bfb5c18f | -16.52964 | -41.71775 | 2026-10-02 15:52:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a501b985-7743-3e67-8e67-2c0a38e80d31 | -15.20275 | -40.90207 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a95a4f70-14b5-3485-9818-53f6d8616a6f | -14.49249 | -40.2108 | 2026-10-02 15:52:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 66bd8d36-7998-329e-90eb-ec1bd022483d | -17.99171 | -43.65511 | 2026-10-02 15:52:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e7ae3973-ba44-3476-ae4c-0e697f8485b0 | -15.10563 | -42.88627 | 2026-10-02 15:52:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4fe8bd1-628c-3dc7-abfa-eceb2c14720b | -13.81003 | -45.24603 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a9191f75-e69a-35f4-b0a5-ec3cb2ef2e05 | -15.23313 | -40.92988 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 99c1278c-691f-3aaf-bfe1-b6fac8c738e4 | -13.82632 | -45.23553 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 737d05e5-a3c0-3535-bb2b-b100a46da8a5 | -14.25632 | -41.6138 | 2026-10-02 15:52:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| ca9a9a85-0a69-3f55-bb3d-c479d236c8ef | -14.31655 | -43.805 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e5664271-1fb0-304b-8ccb-b2804b138174 | -15.16504 | -43.67061 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 10c84a47-0a14-3cc0-a947-ed90bd47426a | -14.53896 | -41.315 | 2026-10-02 15:52:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 529cdeb5-7fc7-3d5e-b73a-6ffcb1d4b84c | -15.7806 | -43.64913 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6fdecfb7-36b3-3bd5-9cc2-2aebbe37fee4 | -13.56802 | -40.68321 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 110f6130-4d2b-3207-98c7-9b454ec2e3c8 | -15.68221 | -41.33298 | 2026-10-02 15:52:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a29dc8db-0969-3094-9015-1510ab5f5ff5 | -15.12938 | -43.59011 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| cc8d4fb2-8d96-373f-9058-b5c84db48440 | -13.44428 | -39.2607 | 2026-10-02 15:52:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e2a5acbd-6231-35ad-97c4-668f93f4d6db | -14.91531 | -40.64542 | 2026-10-02 15:52:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7218ce87-23ff-357b-8e7f-741862961c08 | -13.50513 | -43.50364 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 7ca6d93b-6665-3db6-95f4-8ec4915bd9de | -15.60789 | -41.67798 | 2026-10-02 15:52:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 226.8 |
| 5e59c30e-e94d-316b-9068-28a67940ce46 | -15.87236 | -42.51501 | 2026-10-02 15:52:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c030f60-4a9b-3cdd-9660-a8db432e8292 | -15.85643 | -44.30005 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 2af2d84d-33ed-358a-9589-e564c28dfb00 | -14.36456 | -44.72027 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ce19d61-4b01-34c2-b6dd-224ae90b6cc6 | -14.09774 | -43.93505 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3883fa3c-44f2-369f-b1b3-7e29ec0f8051 | -17.29288 | -41.92953 | 2026-10-02 15:52:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| aaeb78f2-8652-3871-9672-6013672c74a3 | -15.30535 | -41.42189 | 2026-10-02 15:52:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 30443c11-d3d6-3ee6-b3b5-f74ad229e8fa | -14.0734 | -40.55997 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 83c48692-e2a0-3d8e-9acf-c410b0bee92b | -13.79135 | -45.23587 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b89e24a-31cc-35f4-9334-2cc6897f9b12 | -15.91465 | -46.01586 | 2026-10-02 15:52:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cd7c36a6-14f7-3d33-af3d-1b0e54d8bfc5 | -17.30499 | -42.31974 | 2026-10-02 15:52:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 98977a88-8e79-3364-8df5-fc5d854fafea | -14.78418 | -39.8476 | 2026-10-02 15:52:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 941daa6c-089c-3ebd-8835-579889d690c7 | -13.38961 | -43.6881 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de7c7d06-c3e8-3686-85e0-7c6e02a2c044 | -14.07762 | -40.55941 | 2026-10-02 15:52:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 3967518f-b55d-3517-8824-c5d466a510ff | -16.98549 | -45.47541 | 2026-10-02 15:52:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1c5efebb-8bad-348d-aeee-9c533de68228 | -14.82777 | -41.16651 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9d6f1fe3-e8d2-3b61-823e-39c5dd771706 | -14.35893 | -44.72075 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fbb21848-3bb1-3e4b-8dee-ae2aa532ba5b | -13.83546 | -45.26359 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6dcd3e93-246f-3925-a7f0-70ded57c5c11 | -15.03903 | -41.1284 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c5256ea2-a1f5-36a7-ba2a-05d524941230 | -15.23337 | -40.93124 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| bf1215dd-d131-375c-b3d5-3976ab963b42 | -15.85561 | -44.29237 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b3aaace1-b414-3e77-9166-48e5c254f70f | -13.32 | -40.4729 | 2026-10-02 15:52:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 6f9ea94d-c51f-3e99-8bf0-7f8854f401c1 | -14.97938 | -41.34273 | 2026-10-02 15:52:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9a98a2f3-832f-3403-b120-90b73aabe872 | -15.15975 | -43.67122 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 801c67c6-62e7-3c58-aec9-155f7f3f5331 | -14.49407 | -40.71741 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 054f550c-a2ed-31a9-ba67-590638250569 | -14.81506 | -42.80127 | 2026-10-02 15:52:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 95b729a9-427e-373d-a050-6f186a29aeef | -15.17109 | -43.6767 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| fdc748b7-d314-3a44-ad20-0c2dddd478bd | -17.76639 | -44.35212 | 2026-10-02 15:52:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 572a825a-ac3b-3cd8-8f61-01cbee117769 | -16.7037 | -40.22059 | 2026-10-02 15:52:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 44e9fca3-ac90-3848-917d-00408e0f0c52 | -15.16542 | -43.67396 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d3c3ff53-3862-3834-845c-dcbf572c5479 | -15.13416 | -43.5861 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.2 |
| cded7bda-e53f-372e-aaec-53614aed5718 | -13.63738 | -43.83826 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 1ca38073-6a4b-387c-8a3f-f568fd905410 | -13.82747 | -45.2359 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4f4ac5fd-61f3-3fa3-94cc-6d1890407e72 | -14.76974 | -40.62141 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 963f37fd-41df-3485-bac1-a2483c196273 | -15.86117 | -44.29172 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| aab3f04e-f54a-307c-a0d9-a2d8d13ce2d1 | -15.12927 | -43.59002 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e2fc0b4d-efad-3770-b42a-78469b9a7a04 | -14.5508 | -40.52168 | 2026-10-02 15:52:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5081698c-4600-3b5b-a9e9-85d968bdaa9d | -15.02408 | -40.97679 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.4 |
| 59118939-7ddd-3ec7-acd5-7e2ef4cae984 | -13.69514 | -42.17328 | 2026-10-02 15:52:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ac0130df-1f2f-37ce-bf17-bc2af1bd6d3d | -14.33778 | -44.73484 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c65f36bc-6077-36b8-a689-0c80db90ebbd | -15.17601 | -43.67276 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 46.3 |


[Clique aqui para ver as próximas entradas](README94.md)
