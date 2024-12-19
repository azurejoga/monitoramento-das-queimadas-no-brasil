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
| 7c525fe7-c488-3666-8683-9a48d860fae4 | -5.47733 | -46.36038 | 2024-12-19 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e68ea91a-4b05-38ef-9f3b-5f79760ccbde | -5.21151 | -43.30266 | 2024-12-19 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99dcdd10-e6cf-3162-98b5-f21b59fa76c5 | -7.79047 | -34.98919 | 2024-12-19 04:08:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0dd6f679-fff0-369e-8f18-3a53511dc9db | -6.68032 | -41.03629 | 2024-12-19 04:08:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9d7dfc0-2859-37f4-93ac-354747f466a9 | -9.4288 | -35.83335 | 2024-12-19 04:08:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f70e552e-653c-3389-9cb0-546ab16e551d | -4.35443 | -48.19479 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0211145e-8262-38c3-9c15-811575b280de | -7.81608 | -35.23205 | 2024-12-19 04:08:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 388a17f2-5812-3960-aa43-52942d549aeb | -10.20031 | -42.05307 | 2024-12-19 04:08:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3038a918-acb8-3f75-a474-9441808a3120 | -9.43325 | -35.83397 | 2024-12-19 04:08:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5fba2406-010a-3290-b8c2-8a387ca481d4 | -4.78496 | -46.40187 | 2024-12-19 04:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 253825a1-266b-3f94-acb2-ce0b5feb8acf | -9.68238 | -36.20047 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 235acc32-46ac-3104-8bc2-47f69ea3e702 | -4.35027 | -48.47746 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df8dfc41-33f1-3c0c-812a-2dfd2d6189f0 | -4.0427 | -49.76642 | 2024-12-19 04:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76ed4e77-0f8c-3303-809b-9ac6e4b5a2e0 | -12.13353 | -39.76591 | 2024-12-19 04:08:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36d900d8-ed25-3fb3-944f-552c0dc2f730 | -7.81671 | -35.22755 | 2024-12-19 04:08:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ffb0a860-728e-344d-b951-c9d77cd15afb | -6.14454 | -42.45137 | 2024-12-19 04:08:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e48bda5-04c0-31b9-82bf-11ff4165343b | -4.3317 | -48.30036 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b95ec0b5-5e3f-3b44-9da3-d0ad77b2461d | -4.03648 | -49.77161 | 2024-12-19 04:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a559b309-40cb-3b31-aa4e-ed3ed64b148b | -5.86513 | -39.16815 | 2024-12-19 04:08:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7170a6c7-46fe-3d70-9fe0-a3fdb2b18f84 | -5.30567 | -46.06442 | 2024-12-19 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 286d6d4e-e957-330a-8e26-0b2c21db8ea7 | -4.03751 | -49.7655 | 2024-12-19 04:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 936f9315-6914-3e57-a1a7-11a7f05de1ab | -4.79956 | -44.02856 | 2024-12-19 04:08:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 23f89e43-4b60-3fa1-9003-77848c7aaa5e | -4.78557 | -46.39819 | 2024-12-19 04:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e02ba8ac-92c6-3fb8-809b-02e7119fa167 | -4.04219 | -49.76944 | 2024-12-19 04:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8c159ed-9b3b-385c-8146-f3b1a5c73f37 | -7.84519 | -38.41807 | 2024-12-19 04:08:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f76ddbb-6d35-35a0-9520-2e828571e1dd | -8.47565 | -40.67302 | 2024-12-19 04:08:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68d7e04c-7dba-31bd-95e6-7e63bc1176e7 | -9.22221 | -35.64426 | 2024-12-19 04:08:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6105ba8b-e914-3c49-815f-5aaa6c5c2aee | -6.40735 | -39.9468 | 2024-12-19 04:08:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a2f6bac-f45b-352b-bd41-1e0745db8f8f | -5.39111 | -40.6709 | 2024-12-19 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb78a72e-39d8-3585-a3e2-1cd99530d26f | -6.21222 | -39.39858 | 2024-12-19 04:08:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6d0bd263-0855-36e8-8269-7a65927db42b | -4.3472 | -48.46669 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04a138c5-a399-309e-942f-188ac5402f33 | -7.58749 | -38.32023 | 2024-12-19 04:08:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b32670a6-ab4a-3ea4-ab53-bceede4e227e | -4.32703 | -48.29957 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97a5790d-e7de-3fb7-ae48-c683cf7203df | -6.29817 | -46.04237 | 2024-12-19 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be0da279-2d89-3057-b3e8-ea5240db1aa5 | -9.68296 | -36.19624 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6101fc58-30ff-3140-aba7-0b85c24bbba0 | -4.35195 | -48.46738 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d8775e7-f213-3b39-b544-babf5a347ad4 | -5.34666 | -46.66684 | 2024-12-19 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7277b882-bfd7-3eb7-984a-da8226208ccf | -6.00212 | -41.55998 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89a53aa2-8f48-3aee-b4bc-edd66eb54aa8 | -5.219 | -43.29998 | 2024-12-19 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4f43a48-360a-363e-a804-c6c015e5d0a9 | -5.34468 | -46.66729 | 2024-12-19 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dff9cb8a-0625-3a65-a9fe-03925c33cb4d | -7.92885 | -35.19455 | 2024-12-19 04:08:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0c79b019-2124-3582-9a60-8fb81e4af645 | -5.97229 | -41.59792 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cdd318fa-fbcd-3fae-903c-dfa834c26228 | -4.78617 | -46.39455 | 2024-12-19 04:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8abc4307-e212-34bc-b28a-d5bfbe47916b | -8.87667 | -41.10263 | 2024-12-19 04:08:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2375f507-8b1a-3169-8ecb-7dec37aea763 | -7.41006 | -35.23366 | 2024-12-19 04:08:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 17ec1e03-80d4-349c-9073-a9605df96899 | -6.50022 | -39.58803 | 2024-12-19 04:08:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1f07f3cb-a5ec-37f3-8d51-909e341b1615 | -4.35364 | -48.19944 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c00657b9-4672-3279-8190-0273e76dade9 | -8.83939 | -35.70771 | 2024-12-19 04:08:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a07beb8-d4f5-3fd9-bf6c-8c5c5119b74f | -5.95154 | -39.66706 | 2024-12-19 04:08:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8841bff-ccf4-378a-94b7-8ad70b16fdd3 | -6.21164 | -39.40237 | 2024-12-19 04:08:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ad5a0ba1-71be-3a95-95ef-a9f645845727 | -4.13035 | -48.13257 | 2024-12-19 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb875520-77ee-3c8a-9c09-dffb869fae4b | -12.13291 | -39.77013 | 2024-12-19 04:08:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe39d2b0-5701-3676-a9ff-834981154d40 | -6.78919 | -39.41297 | 2024-12-19 04:08:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 18a521ff-be55-303b-8cd3-99fef580bbdf | -4.32998 | -48.298 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 181e99d5-1f17-3339-9872-fad73400109d | -4.80558 | -44.02912 | 2024-12-19 04:08:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 20802a36-f803-3355-ac77-b10af92f1576 | -5.81566 | -39.21159 | 2024-12-19 04:08:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cd7576d-ccd8-3fdf-82ed-7c331c1087c1 | -6.49601 | -41.60242 | 2024-12-19 04:08:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 662fdf50-3ce2-30bc-b5c9-abbc9ad1a238 | -5.2589 | -41.38291 | 2024-12-19 04:08:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca1f4839-17e3-384a-aba2-1dab6dc5a5e3 | -9.67859 | -36.19575 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 917d817f-c584-3616-a3ae-5d184fa48891 | -4.4789 | -47.98708 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c354afb7-315c-31c4-b323-9111ae1989be | -4.48348 | -47.98479 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9102a83f-b77b-3437-97c7-cb10524160c4 | -4.78087 | -46.40126 | 2024-12-19 04:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ed3780f-c5e3-32cd-9301-ea3f9fdcb999 | -9.67748 | -36.19741 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29eb8370-6002-36ed-b48f-3cb4efb8ede4 | -5.53004 | -39.59624 | 2024-12-19 04:08:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 23f31052-d96c-32a3-bf1c-584027635299 | -6.76087 | -39.05865 | 2024-12-19 04:08:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f636ad5-21eb-3421-98c7-a0352e94bf90 | -4.47889 | -47.9842 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8ba9003-f4cf-32e7-8bdf-a60447ae52b3 | -4.80313 | -44.02913 | 2024-12-19 04:08:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ec9063fe-bec0-3a4a-8494-f823b0646f8d | -5.92196 | -42.34729 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cab4f41-f7e8-38e0-ac15-5648faa21b5c | -4.7777 | -46.44572 | 2024-12-19 04:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d3bbe28-2e6d-3e5e-8bb7-76e6805e5e5c | -6.06759 | -44.63855 | 2024-12-19 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cab8042-8207-33a4-96d0-71b3cbb70af3 | -9.67801 | -36.19995 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8e368cf5-d806-3eb3-802f-34df6f59ec1d | -6.00103 | -41.56691 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c5228f9-dffe-38d1-ac77-4528d0473342 | -7.84412 | -38.41595 | 2024-12-19 04:08:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c4b2ea1-6a2b-3246-9ef4-7c2111663983 | -9.68676 | -36.20095 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0b002ed3-a664-3f39-9c47-25dc9ef8c020 | -4.80201 | -44.02855 | 2024-12-19 04:08:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 01fb0fb1-ccf5-325d-a30a-20b451ca958e | -6.26117 | -46.19432 | 2024-12-19 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5424558f-560c-38fc-9bf5-8cf2987cc91e | -6.00157 | -41.56345 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9091fb9c-2849-3890-b4e4-fd009d633197 | -7.68597 | -35.26681 | 2024-12-19 04:08:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 60bc4aba-4a5e-34fc-963f-2d57325c926a | -7.71161 | -35.08337 | 2024-12-19 04:08:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46471fbc-d922-3dfd-820f-4f9aa7a53e31 | -5.02695 | -42.8622 | 2024-12-19 04:08:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a56f0d26-71de-3cc6-939a-daaa17c4c3d9 | -4.99797 | -48.26878 | 2024-12-19 04:08:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90532541-5e5a-3410-a13c-1d406ea82fe9 | -7.58379 | -38.31967 | 2024-12-19 04:08:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab68a1c4-b4b6-3ab2-91c3-8322f75d3221 | -5.21496 | -43.30319 | 2024-12-19 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1de2b56-ac53-3e2d-a053-e0bcc29dd824 | -4.037 | -49.76855 | 2024-12-19 04:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 361804fc-778e-3175-a80a-adf73783621f | -6.00435 | -41.56744 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 113216bf-c427-3569-bb0b-900aa2e4142b | -5.39057 | -40.6744 | 2024-12-19 04:08:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d49a6ad-1d72-3b7b-9bf0-d2f9b8f51f95 | -13.30778 | -52.43576 | 2024-12-19 04:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff375555-cb9f-34cf-8598-31318376bbe3 | -13.30713 | -52.43904 | 2024-12-19 04:10:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff7b873d-e93d-3c7b-aa3f-10e2d86ab606 | -13.92739 | -54.61038 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9b7c5af-bb13-3b43-b040-e8f9877c8bb4 | -17.18262 | -48.83144 | 2024-12-19 04:10:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a56cc1a-9ab8-30c6-b2f1-7a0e136a3e88 | -17.29868 | -53.76957 | 2024-12-19 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c055fa-fec3-3ee6-a4d8-a442a6663227 | -17.29943 | -53.76591 | 2024-12-19 04:10:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 802dae2e-4ff1-3009-a30c-5d1893cba85c | -17.97519 | -54.00268 | 2024-12-19 04:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7808589-a503-3bf8-83bb-e6a70e2cf81b | -13.91839 | -54.61522 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f333cd8-d5f0-3b9d-aa95-39ed7e94d40a | -19.83808 | -40.08292 | 2024-12-19 04:10:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 063ad971-f019-37e3-8a83-130627908320 | -17.75522 | -42.89625 | 2024-12-19 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6cf74d49-e858-36c8-9ca2-dc9cd3efd5a2 | -17.75428 | -42.89676 | 2024-12-19 04:10:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fa05ec2-f557-37f3-b5bb-a71668314112 | -12.23571 | -54.30983 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7bdfdca-d6bc-3532-8e7e-832743c59b29 | -13.92527 | -54.61205 | 2024-12-19 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af836f90-81e0-3839-8875-7301c7ba5a89 | -12.22769 | -54.31517 | 2024-12-19 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README9.md)
