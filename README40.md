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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70488ebc-124a-30ef-9f0c-e6510eb81763 | -17.96223 | -44.40577 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07a003d4-c496-3042-8879-65ff3725da28 | -13.85887 | -43.98846 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8653dfb5-cc91-3d74-ae7a-b487170c242c | -15.79274 | -49.39507 | 2025-10-07 04:10:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffb800e0-397d-371b-97ac-9b49eff5bb3b | -15.61118 | -52.56382 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a10aa5da-de7d-30bb-a8bc-cefafab8f8e5 | -14.73452 | -46.0222 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| afd094d6-5075-3d30-a6e1-2a652f397124 | -12.3844 | -51.08584 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea94eafe-8132-365e-9060-83c7d9b45d28 | -13.26857 | -47.16329 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f0002ac-c286-33e8-afed-568795d295f6 | -17.56838 | -46.07818 | 2025-10-07 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bebded7a-6e36-319d-a019-0db49749b3f7 | -13.52175 | -48.61792 | 2025-10-07 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7f3821a-41e3-3be8-911a-373e5375cd38 | -18.56781 | -49.25918 | 2025-10-07 04:10:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 91ad9c97-b0f0-3f38-aaba-92ab546db519 | -13.73028 | -48.06184 | 2025-10-07 04:10:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f55a10dd-661d-3a26-a71e-fb3cad8e832f | -10.56176 | -56.5508 | 2025-10-07 04:10:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2276c05b-acc0-3eae-83dd-1cbd960b5009 | -13.21686 | -47.81345 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e216c89-f9e3-3524-97c1-4a3dc797abdd | -14.61777 | -52.4905 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10a8a84f-2ddf-3e60-bb34-125b3208beb7 | -15.60345 | -52.576 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6a50a684-d770-3275-a24d-c0b7a4088181 | -13.34857 | -48.03009 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c4203533-d22d-3bab-94dd-fc15f25430db | -13.72329 | -44.21851 | 2025-10-07 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a051d9-08ab-393e-9890-5dc72bae2be1 | -15.22392 | -56.7746 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55048e3a-e26d-3cb3-845e-f2e8f7daea6f | -14.75904 | -46.04705 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af97b60f-16e7-38e7-a2e5-20ebeb55248d | -14.16002 | -44.75838 | 2025-10-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d79f342-a34b-30fb-912f-44d4ba4b4981 | -18.11577 | -53.34731 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40230919-3e36-3cf5-8ca7-3ea7a3460041 | -18.27176 | -53.33978 | 2025-10-07 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9faeb82-ec27-3ebf-aca8-be7459817d0d | -14.92044 | -51.44772 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c5f3cdbe-a068-3921-af5d-1ac7df8a41b8 | -13.60009 | -43.66829 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e874a46-fe3a-33a7-b115-f04a8096bf92 | -17.29564 | -49.27686 | 2025-10-07 04:10:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ff8c0fb-c2a0-3ca5-be6b-dfc607623c17 | -15.19889 | -44.50798 | 2025-10-07 04:10:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5744bc29-b8b9-33c0-82d6-8d5d18d42d80 | -17.55126 | -46.7618 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 837cf1c6-5ac9-3bb0-a1f8-da15942a4d99 | -19.96437 | -47.2073 | 2025-10-07 04:10:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8aaf80f-8110-3305-9c91-aa3e41903b0a | -15.48127 | -47.94407 | 2025-10-07 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbcd88b1-d894-3514-b576-6d4e16bedfeb | -13.23605 | -43.40835 | 2025-10-07 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e90b275b-cfe1-3c4b-9f6c-acf8ea8fc8e2 | -13.37246 | -47.2379 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5685ed2c-3068-3446-b0b8-8e49551d92a2 | -14.73664 | -46.03087 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5a3e713-76fa-3387-9b5b-eda4b23124cd | -15.20794 | -48.2515 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39982feb-d2b7-3a23-b048-ddc6a91a5d87 | -14.764 | -46.06025 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe661b06-d79d-3d8b-91da-bcdd3160f30c | -20.36801 | -44.75215 | 2025-10-07 04:10:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8689c882-2b32-30fc-b2b0-10a6b04db3f3 | -15.8042 | -43.67425 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11c06604-8052-34fb-baf7-ac863e75e59a | -14.92071 | -46.80617 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d0911fd-3089-37ec-85e1-44dc9697cba4 | -13.25954 | -48.05579 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53b428aa-d23b-364a-88f0-612cfcafbcec | -14.81245 | -44.89506 | 2025-10-07 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 463a8442-efbb-357a-b9f4-2aa1dd1a14cd | -13.76461 | -45.72925 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 573e62b9-4b9a-391d-9ce6-dcb89c0337f3 | -18.39878 | -45.23475 | 2025-10-07 04:10:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bbad918-cbf9-3e6b-a15f-42037a4d8bef | -14.92278 | -51.40904 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93faf2bb-e053-3c62-9270-76d250f31ad9 | -15.98404 | -50.8531 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 908cb787-35ef-3dfe-8002-adb0dd95d878 | -15.20127 | -46.37983 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7df70b0-f92f-3b00-8ea9-22165bf4cf64 | -13.24419 | -47.2374 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d81b31c-76c7-35b8-be54-4fc375247b50 | -18.2724 | -53.33667 | 2025-10-07 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4cc5bc9-0297-3ce4-a5dd-119020ebd9fd | -12.46106 | -48.00366 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f1abb2a-2328-300b-93fd-ec9a6b4bad0b | -13.07812 | -47.84432 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f837fecb-646d-343c-aaf8-095a351349a4 | -14.90128 | -51.44386 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f52e2599-adea-3a1d-9983-45362921a9c1 | -15.3957 | -48.01047 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8317e62d-e13a-351e-b8c4-ed2aa1971496 | -13.22731 | -48.45966 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f27d55f-5aa1-33f7-85fe-e89c505379cd | -16.95942 | -44.24974 | 2025-10-07 04:10:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf6e794d-b439-3e98-a84f-88f575b4b0ca | -14.29206 | -47.41662 | 2025-10-07 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9277576-437c-3e96-b323-1b8197825f4e | -12.72655 | -47.93389 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fdfa144f-45c9-376d-8214-eb22871102b1 | -13.60339 | -43.66883 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 717efbf4-9a79-3480-ade8-f091ee4df407 | -18.51278 | -43.90609 | 2025-10-07 04:10:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0101718-00cf-3afe-a744-7e0b661c7dc0 | -14.9352 | -51.47105 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de34b140-9155-398f-ac62-18822c6fa8d3 | -14.90751 | -46.83948 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 034a166a-e761-3853-bdde-9bea23477b46 | -15.76083 | -47.77404 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9b2cd45-2d24-32b2-adae-9ac6ecde84c4 | -14.62484 | -52.48987 | 2025-10-07 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ebb4d12-4238-324f-9b8b-bd8f4a9622bf | -15.8293 | -42.62675 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 6a730d2e-dde4-3a29-9574-d06160f729c9 | -13.70068 | -42.23254 | 2025-10-07 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d9e7188-9fac-381b-a381-fcd1c923aed1 | -20.0909 | -44.19027 | 2025-10-07 04:10:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd8c8425-592b-362e-bca1-3dc733aa2a9e | -19.58992 | -44.85339 | 2025-10-07 04:10:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ed72a02-847c-3061-b64f-744a3b86dc72 | -13.3358 | -48.03329 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f128bea-982c-3101-8620-10dbb3c5ec8d | -13.23871 | -47.2466 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79f30369-0799-31bd-9909-917857fbea24 | -15.99141 | -50.93866 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d69dcde-47ae-3912-a08c-ccd362889c30 | -13.09586 | -47.99572 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eb3b100-59b9-3782-8837-f05d082a7a4e | -14.9293 | -51.4271 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3fbfd4d7-3863-30de-ac6a-8c241030db62 | -15.59414 | -42.36471 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60d638dd-e3ca-3922-967f-92e5ce9273e4 | -16.0134 | -51.04827 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 656437de-e482-39af-b695-2fac3cb067f3 | -14.91942 | -51.45313 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d683b026-0a95-3de5-83c5-6ae8dd2f8e3d | -15.99572 | -50.84087 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b793943-088d-3a29-882e-01b5cd312766 | -13.25191 | -47.17019 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a76c17fa-2ef7-3e76-99e3-4eadcd107948 | -13.36953 | -47.23241 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a45eee81-eb54-3ac8-8411-068f0cc8192f | -12.3445 | -47.05844 | 2025-10-07 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4190d666-309d-39ad-94b9-d6bfaaed11ae | -14.52669 | -46.92958 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e51f0ff-574d-32af-ada3-afb0f271613f | -15.99965 | -50.94842 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6e81498-a961-3e25-aa37-2015fb36249c | -13.50109 | -43.66965 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5e460a03-92a4-3aa4-af33-b7fb006999f5 | -15.96307 | -50.84012 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9330a238-7b17-3010-8f99-35b613b09f25 | -19.93599 | -44.64061 | 2025-10-07 04:10:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8491bd05-447a-313e-9775-35983e17b4f5 | -15.59955 | -52.56902 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bc605775-1ea5-3a6a-b5e0-81a5e9572939 | -13.93927 | -43.7393 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83392489-c130-318c-9477-5ed86e366b2d | -14.51288 | -46.92255 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17532523-6a97-3fff-aefc-eac79bdf2d1a | -14.7695 | -46.04882 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| afb81f93-2b60-372d-b21b-4e486e057725 | -15.22113 | -56.76687 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea24ebe1-11d9-39c5-9c32-e72c163f99e5 | -15.65117 | -43.67465 | 2025-10-07 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ceea245-5236-3544-8103-de8e8fe6e585 | -15.3906 | -47.99474 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa166512-8d3a-3643-9035-6b25bd103d3e | -12.38025 | -51.10839 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23ce587d-3b6e-34c0-bbf1-ce5cdf2aeb0d | -14.9107 | -51.4437 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 042e7759-a891-32ab-8739-483731d55a05 | -14.91854 | -46.81873 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5a85173-b655-3c70-a608-cc7d8f35a4cb | -14.73588 | -46.01415 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f6f212d9-e9ce-30d2-9b04-ca09fa508f9e | -16.29928 | -50.99031 | 2025-10-07 04:10:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8a52e5b-7cdb-3602-a295-53a453470652 | -15.98037 | -50.8477 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6601219-3830-39f2-8830-8e56746f46ed | -13.22324 | -48.45898 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9da1e82-0865-3069-a94b-0dcfb5e97478 | -13.2498 | -48.0649 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d17c2a77-8749-33b2-a84f-95e60631b335 | -13.97013 | -53.89534 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc4a3f54-45e8-320c-ad7c-d181f982d0b7 | -15.07701 | -46.63945 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37d0bed0-d1ba-378e-b030-840c40d51ffe | -19.88981 | -42.62874 | 2025-10-07 04:10:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8047f98f-fe83-3331-a292-22ffe1ea40eb | -13.27609 | -47.16447 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README41.md)
