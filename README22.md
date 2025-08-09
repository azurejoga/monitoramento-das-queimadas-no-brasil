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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22527be8-1cba-31be-8537-c7548e808639 | -9.70584 | -61.30505 | 2025-08-09 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba604557-89f5-36d3-8d67-23d0797f9345 | -7.0744 | -59.17379 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 7ebae52c-1180-33ac-a043-320a919cd518 | -11.08338 | -50.46412 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f14469b5-c40d-3404-8ef2-d29d1d28acdb | -11.72082 | -48.34397 | 2025-08-09 04:42:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2aadd28f-c5ed-363c-874e-b3b9348bed2a | -7.05949 | -59.19315 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 98628eb5-09be-36ee-8e0c-6eee36f0bbae | -9.71185 | -61.30637 | 2025-08-09 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e2e5224-4f56-3a26-b255-00b7a5dc7715 | -7.07928 | -59.17834 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b4b1b5fb-5a8a-37c7-8682-93fefb0d9dec | -13.62051 | -49.01011 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74b7fb45-7f8a-3c9b-a396-6b3dcf4966c8 | -11.79915 | -44.92968 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 522655cb-6130-3d9a-a79b-fee5d248ab03 | -7.05679 | -59.20798 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 861bd521-9242-34ce-bde3-0b825324aab5 | -11.08947 | -50.46871 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7b8602c-92ee-331e-be8d-f7fe4dbd99a3 | -9.86115 | -44.6918 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac8923d6-dd0a-3597-9b62-273692dbdc3e | -11.3782 | -54.35661 | 2025-08-09 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6628f126-e820-3652-8434-49a5dfc5ff54 | -10.63367 | -44.75851 | 2025-08-09 04:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da95b273-3f45-302a-a8f8-de8d995e109b | -11.74313 | -44.96403 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0100a0d9-d327-3248-9dd8-c4d404d17b30 | -7.06367 | -59.20153 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a6c10468-a39f-3847-a839-3f98def10adb | -7.0608 | -59.18595 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 6f961a09-c387-307b-936d-bbef248fb450 | -14.37983 | -50.32113 | 2025-08-09 04:42:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32879402-595c-349d-86d5-b1a13d6f0383 | -9.5503 | -62.72583 | 2025-08-09 04:42:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ea91121-73fb-3cee-bd9b-4f585255b0e2 | -7.08964 | -59.18407 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 38540e54-2556-30d5-8d80-024d05c91aca | -7.07376 | -59.17737 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 5b19e443-da94-3509-9979-ad39ef2e804b | -13.63311 | -49.02011 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4473eb02-70c5-3522-868e-b92542a38443 | -7.07571 | -59.16658 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5beaa5c0-bee8-3cbe-8981-8ebd351013f0 | -13.18192 | -43.68272 | 2025-08-09 04:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d899b630-7e24-3285-999a-cf25ed88e0de | -12.71174 | -47.79353 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95b7e936-4d15-3a6f-9757-992797ff9981 | -9.51729 | -45.43059 | 2025-08-09 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a475a5df-5089-35d9-99a5-1e37f0bcc027 | -7.063 | -59.20523 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 90c8a78d-9432-3058-9072-89f122a2192a | -10.00391 | -48.12656 | 2025-08-09 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edf34c29-f576-3cbf-b7fb-a1c0990abf05 | -10.44307 | -50.97771 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa9fb41c-219a-301b-9944-95592d9a75a0 | -9.86605 | -49.96667 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6910965c-0768-3cd0-9201-1d92840aea99 | -9.65726 | -43.84687 | 2025-08-09 04:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4f5b700-12f7-31f0-b859-c61fbeb12ee9 | -12.71711 | -47.79531 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9ad0f1e-7e93-3baa-aa80-049bac82d83d | -12.71414 | -47.79063 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44ccec81-da7d-3cee-9360-0377a89b13af | -13.7792 | -48.88052 | 2025-08-09 04:42:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608a4e5b-795d-32bb-b452-e6a4662c855b | -7.08124 | -59.16746 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 00fad282-0b8f-3f17-9533-ad690fc035e0 | -9.86788 | -44.70412 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39758ef5-9696-37ef-8155-673f02c68216 | -13.55791 | -55.25548 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1de6a68f-0648-306b-9866-694583eee838 | -19.47178 | -46.89567 | 2025-08-09 04:44:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f0d7c19-be23-3a4c-9568-a7b876548362 | -19.96797 | -42.12105 | 2025-08-09 04:44:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| f9ea1073-eb43-398a-95c2-74219db31cb1 | -14.49867 | -52.11401 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7598ce8-501f-3574-8d56-1e9267d29033 | -22.14704 | -49.44824 | 2025-08-09 04:44:00 | NPP-375D | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5b583b73-ccaf-3682-be59-fa701ce9c01f | -14.37053 | -51.11539 | 2025-08-09 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93ccbfb-406c-3eac-b925-b824d2e77db8 | -20.57763 | -41.686 | 2025-08-09 04:44:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c34bd7f6-eff6-3f3a-98dd-16c5f068dde1 | -20.04291 | -44.97821 | 2025-08-09 04:44:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 416ab693-f82a-3408-acd5-9c0af0b02935 | -20.58388 | -41.68248 | 2025-08-09 04:44:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3e24390b-2a5e-3a29-aa02-f1643050203e | -16.79443 | -47.51075 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c08f99f1-d260-3ccc-9f0c-08b4d8670cff | -16.96066 | -51.0493 | 2025-08-09 04:44:00 | NPP-375D | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31aabd6f-31e7-32f6-bed1-b5e0de13c24e | -17.75871 | -48.45159 | 2025-08-09 04:44:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40879b46-376a-3dee-bea4-b0767ac40233 | -16.17912 | -48.72071 | 2025-08-09 04:44:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 683cfc73-994b-3368-81ee-8315d8c5202d | -14.52428 | -52.12579 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 654a0614-91a9-351d-855d-c562502a56b9 | -19.58999 | -42.68428 | 2025-08-09 04:44:00 | NPP-375D | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ce8cf383-7e29-3c91-9cd7-84f6be23c160 | -22.15008 | -49.45343 | 2025-08-09 04:44:00 | NPP-375D | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 802faf75-d7a6-333f-b461-f8858a6481bc | -17.79776 | -48.59629 | 2025-08-09 04:44:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6a18a7a-3ebc-3832-bc48-067057bd78d2 | -14.49591 | -52.10983 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c99f329-ed5d-35e9-9464-5ae55d322826 | -16.09237 | -49.31902 | 2025-08-09 04:44:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c34d227-bfce-3614-8678-eab6b87df217 | -19.73693 | -42.07274 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 4ed27866-fefa-363a-ad06-65e767da1a68 | -19.8123 | -47.06213 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 738a49f9-ac5e-394e-a35a-01d195643018 | -16.79937 | -47.53158 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| def2afde-4257-3b89-8f80-87faab8c7c2b | -18.31005 | -48.80827 | 2025-08-09 04:44:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3cae89e-1449-3221-95f9-ff7030d6d14a | -17.7919 | -50.12049 | 2025-08-09 04:44:00 | NPP-375D | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83c7c433-ae55-3d46-9b94-408706d7c90c | -17.6204 | -46.70885 | 2025-08-09 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dbb8a0b-f8e4-3f2a-8cb7-510e4f2a04e8 | -19.7317 | -42.06802 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e0c5bb4d-56cc-38f5-82d4-4a654986c398 | -19.8159 | -47.06662 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e683dadf-91a0-31ca-9a4e-22f35b6b3660 | -21.37737 | -44.96932 | 2025-08-09 04:44:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db08d22a-25eb-319f-9f6e-fa8aa23652e8 | -19.96827 | -42.11806 | 2025-08-09 04:44:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 7491715d-b25d-3f41-9cb0-4e46d68e6253 | -16.70444 | -49.31599 | 2025-08-09 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96fc5b6d-ee93-33cf-b7ea-d4b311bd93f5 | -14.52821 | -52.12274 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 681ddae0-16e2-32f7-97aa-12fb681ce558 | -17.52733 | -50.28369 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf632a61-4c47-3793-aae5-fd281d7f882c | -19.85311 | -41.43516 | 2025-08-09 04:44:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| aaed2ffa-bcdb-3e4d-87d2-e781830031c9 | -14.37109 | -51.11183 | 2025-08-09 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20854a8b-939b-38dc-9f53-5b5e0bf4d547 | -22.18257 | -47.08904 | 2025-08-09 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5eb0bc2-9ab6-3134-8f88-67a2173966aa | -22.14641 | -49.45282 | 2025-08-09 04:44:00 | NPP-375D | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 14583fc7-8e57-3eee-9d40-bd69bd7bd9c7 | -21.17994 | -48.02759 | 2025-08-09 04:44:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e23b25d-02d0-37a0-8bbb-632f6e73c25e | -17.61635 | -46.70824 | 2025-08-09 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdff5be3-b1b5-39a3-aacc-ba95af7a8cae | -20.2287 | -50.90334 | 2025-08-09 04:44:00 | NPP-375D | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3fa916ff-4c32-3a96-b6eb-f90087056afd | -19.81639 | -47.06265 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 89810995-2452-3d1e-b30c-320f9006b438 | -19.73125 | -42.0724 | 2025-08-09 04:44:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ccd590b2-2c4a-397d-9f67-d37209c2c7cc | -22.46924 | -47.58285 | 2025-08-09 04:44:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e98fe279-7531-3430-a69d-30220cf12798 | -19.85353 | -41.43085 | 2025-08-09 04:44:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e83a7212-cc6f-31f7-bcb0-dfd53aefb58c | -15.91531 | -48.95496 | 2025-08-09 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| efb413e7-1797-3162-b2b8-f0fedae1d437 | -15.70845 | -49.7971 | 2025-08-09 04:44:00 | NPP-375D | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de1e62f3-b217-3ee2-bee6-eebe55277baf | -17.78848 | -50.11992 | 2025-08-09 04:44:00 | NPP-375D | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10aba745-9a3b-3c77-8a00-922888de8b1b | -22.15071 | -49.44882 | 2025-08-09 04:44:00 | NPP-375D | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 714b2ce2-0994-3ed1-9deb-88ee4d816d1c | -19.80772 | -47.06548 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| af860061-d86b-319c-a9a4-ca116a392d6a | -17.79247 | -50.11664 | 2025-08-09 04:44:00 | NPP-375D | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7418bb99-8ba8-3b6d-a2de-ae1acbcbda6d | -19.81181 | -47.06607 | 2025-08-09 04:44:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 22e16fbf-ff40-3889-9cae-34b8ad4cb374 | -14.52879 | -52.11913 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4ff363-c0fd-3ec8-898a-dc4511ffd9aa | -19.859 | -41.43586 | 2025-08-09 04:44:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6118880b-0269-3c99-bb8c-015d8bb3f043 | -17.68946 | -51.96988 | 2025-08-09 04:44:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae0ed24d-8213-3063-9204-022e9d8ccd01 | -20.04174 | -44.97703 | 2025-08-09 04:44:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 170e4899-1d3a-359a-9a1a-6d5bd4ccd69d | -16.79062 | -47.5101 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 047d206f-5d7e-3ed9-98e4-3e9a9a19f9ed | -14.92241 | -56.36605 | 2025-08-09 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f81e1158-f11c-3990-ab56-cba54ced71ff | -15.18155 | -48.71214 | 2025-08-09 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aedd55c8-94a1-3253-93da-48a6b7cc08e9 | -15.1839 | -48.7209 | 2025-08-09 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4097ecc-0977-35c2-ad0a-abacde8fb863 | -16.76056 | -49.69868 | 2025-08-09 04:44:00 | NPP-375D | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80666e3f-6ba8-35e1-93c9-5654e32a1a3f | -17.5086 | -50.2923 | 2025-08-09 04:44:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197a4572-2031-3223-9e89-d4e9ad431439 | -14.52937 | -52.11551 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 312ec0e7-e701-36a0-93eb-9f4bb1011728 | -16.79421 | -47.54079 | 2025-08-09 04:44:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e75bc02-7ee2-3bdc-b111-a9486ecea8e9 | -20.57803 | -41.68184 | 2025-08-09 04:44:00 | NPP-375D | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 05bce58f-8644-35a0-ba26-2efb95e12c9f | -14.50478 | -52.11877 | 2025-08-09 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
