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
| 763b0d2e-e765-3a0d-bfbc-f33bae0a9c11 | -21.35489 | -44.83333 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| d7cc4d61-e7ba-3242-b3d4-00c466613be0 | -21.35662 | -44.82226 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ed57371a-fc70-365f-81a4-7f6ff9393298 | -18.80052 | -42.03224 | 2026-07-30 04:17:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b6b508c-1fdd-3afe-a6ac-f2585cb6bf1e | -19.27112 | -42.14365 | 2026-07-30 04:17:00 | NOAA-20 | SOBRÁLIA | MINAS GERAIS | Brasil | 3167707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5be6874a-9730-3d96-9708-e9ba5631e04c | -18.35471 | -47.19306 | 2026-07-30 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 744a0ec5-9635-3bad-96d8-a5671fa12283 | -20.3471 | -40.93596 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bfeb9a41-0a91-3586-8b64-a70663571ae7 | -17.39697 | -47.32883 | 2026-07-30 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f98b1fd-b0df-3f5c-87b1-e361b8bc9594 | -18.4146 | -40.02139 | 2026-07-30 04:17:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f077e000-1293-356e-ae8b-354df39f7f92 | -18.807 | -53.14584 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71675344-d78d-30a8-b253-deb03b408dbc | -20.7744 | -42.97715 | 2026-07-30 04:17:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40aed155-3b4b-38dc-96bd-6f23c67c4845 | -16.79175 | -49.26262 | 2026-07-30 04:17:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 588f9348-6373-3b3a-8e71-9f4ec7fd4f05 | -18.22717 | -42.20714 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0f6d7c63-caae-36c2-b71c-7ff94383fc8a | -18.47177 | -51.72551 | 2026-07-30 04:17:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f342e24d-a12d-3434-a696-50fcb618807d | -21.35388 | -44.81798 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ee7ee425-a303-372c-8cd7-d3b05106e6c6 | -17.21936 | -41.53349 | 2026-07-30 04:17:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a6f9e42a-8165-38af-81d8-669f6c1d6ff7 | -18.47628 | -51.72657 | 2026-07-30 04:17:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7bab766-fca2-3145-84ec-9d88e298b313 | -20.03364 | -46.3667 | 2026-07-30 04:17:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb24650-ae45-3bc5-99ea-87a4bd8b7881 | -21.59226 | -41.30254 | 2026-07-30 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aae85293-19e4-3250-8d8e-75b239528ac1 | -21.59599 | -41.30309 | 2026-07-30 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb5d3f48-9af7-3f46-b47f-e4ad9f0baae2 | -20.34402 | -40.93813 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5e179993-9ae0-36da-b95a-e507311de571 | -22.76236 | -43.74305 | 2026-07-30 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 737c0c1e-a7c3-3af2-befa-4003442828e7 | -17.3984 | -44.03829 | 2026-07-30 04:17:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbd9d0d7-4479-3154-8fc7-be42eef76097 | -18.37729 | -51.4528 | 2026-07-30 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a7d9260-02ea-310a-bfef-65706a534bbe | -22.28406 | -45.38162 | 2026-07-30 04:17:00 | NOAA-20 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32d7bec2-029b-3e34-94c8-edf23e8c5e09 | -18.47082 | -51.73029 | 2026-07-30 04:17:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9425cb3b-b2f2-3177-b785-0e8c4176a31b | -21.04123 | -48.46791 | 2026-07-30 04:17:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d7ed145-37c8-30a7-9b84-b375fb4513a2 | -21.43901 | -41.10063 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| dbebe1c3-94fa-386a-ba3c-3a7578e290bf | -18.53397 | -46.34529 | 2026-07-30 04:17:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 319fe853-67c6-3a5c-a2a4-4b6424cea24e | -20.56151 | -41.70309 | 2026-07-30 04:17:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| faa751d2-fb23-3049-881b-0a703e5a67e5 | -21.34553 | -44.82786 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a16d28ba-9fd4-3095-ac22-c44794973d16 | -17.39978 | -47.33378 | 2026-07-30 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f35d702c-22cc-3a8b-a515-3fea30ebbae5 | -21.35504 | -44.81058 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 415305f1-405a-3ce4-960b-d15174786609 | -21.5203 | -41.21357 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64b837fd-2583-3ad1-ae9a-5c4f1f6e702f | -21.48304 | -41.20094 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 80d29c68-db31-38bf-9dc0-d02a6fa9cf98 | -22.93728 | -45.37439 | 2026-07-30 04:17:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ab592e43-1fe4-3ad4-a4e8-81c617e18ba7 | -26.48184 | -53.57957 | 2026-07-30 04:17:00 | NOAA-20 | SÃO JOSÉ DO CEDRO | SANTA CATARINA | Brasil | 4216701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| aac9734f-70e1-3cee-bcd1-67e2c4c00aa5 | -19.17704 | -47.35351 | 2026-07-30 04:17:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fadecff6-a134-3083-8c2f-e0b6aee97267 | -20.34336 | -40.93541 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 700aab67-b6fd-36fe-9fd5-009d7ead8657 | -22.76268 | -43.74244 | 2026-07-30 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eb4cb34-69b1-3b6c-82dd-7353fbcdb256 | -20.60134 | -42.14981 | 2026-07-30 04:17:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dffc582e-dcc0-31ae-a84c-a48c81c47227 | -18.22029 | -42.20587 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7bdb1e8c-bc63-356a-9f5e-5e28578dcf98 | -21.35114 | -44.81368 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c7ebc677-97d7-3ed9-acae-b62aab3ec3c4 | -18.80086 | -53.15051 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ace9266-0ec0-3acb-a059-dc2501f82fd7 | -18.59108 | -48.20359 | 2026-07-30 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de0de2fe-b9b9-3dba-a53c-44231a355082 | -21.35446 | -44.81427 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6e9270a8-8ac7-3efb-888f-36cae2bae1db | -21.43448 | -46.66185 | 2026-07-30 04:17:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42982501-a83a-3714-bca9-b67eefa17637 | -15.77079 | -48.03822 | 2026-07-30 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce65d4b6-ed83-3979-adec-1917640f7fbb | -21.45983 | -43.78447 | 2026-07-30 04:17:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2e2a685b-f8c5-3cd7-95a1-207345981e31 | -17.21994 | -41.5295 | 2026-07-30 04:17:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d04fee4d-9057-3c8a-94f1-591a885beb10 | -20.56086 | -41.70048 | 2026-07-30 04:17:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c421b0df-d41c-3038-a977-6f64df968200 | -18.80038 | -53.14956 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42b8b184-d80a-3e4b-bbc5-30a78f4f854e | -18.22775 | -42.20314 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 70548905-d309-35cd-b60e-622db6890dbc | -18.80531 | -53.15063 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e7b0a6f-a6a5-3391-8f39-763a0ff03ffe | -18.36173 | -47.19432 | 2026-07-30 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c8152fe-ca68-310b-ae06-acbc329dcb9b | -20.7069 | -47.28946 | 2026-07-30 04:17:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 030e520f-67c9-3d78-a8c7-a88266bcb818 | -17.83608 | -41.96545 | 2026-07-30 04:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba24f5a8-a3de-33f0-be2b-30c6f67deb05 | -21.51655 | -41.21301 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8ef8ba8f-b88c-36f5-9221-1836c9b363ce | -22.67583 | -43.47665 | 2026-07-30 04:17:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8bb864a-260a-347f-9ebb-de0baf48cfaf | -21.35719 | -44.81856 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6b3daba8-b926-3556-9d8e-aca5f1a69d47 | -21.4604 | -43.78063 | 2026-07-30 04:17:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 81673412-3d33-347d-99ca-4d875f45377d | -18.59474 | -48.20432 | 2026-07-30 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3580dbf-6c36-3a35-9898-70f8a1db2a24 | -15.7746 | -47.99531 | 2026-07-30 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d23ec9-ffcb-3499-9257-aea4764caa71 | -18.36454 | -47.19909 | 2026-07-30 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb6f941b-6bbf-3841-9135-d8a3a609b89d | -26.48241 | -53.57689 | 2026-07-30 04:17:00 | NOAA-20 | SÃO JOSÉ DO CEDRO | SANTA CATARINA | Brasil | 4216701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 271ca1f8-b793-3a17-a480-c48d5ea6d606 | -18.22128 | -42.20667 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a7672edb-355f-39cf-87f3-a29ac2a809f4 | -21.59326 | -41.3053 | 2026-07-30 04:17:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 55241cc2-a005-3176-addb-9ceaa67a4362 | -21.35835 | -44.81115 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 442a8ad5-2fb9-33c0-83a9-5b22e4903b41 | -16.50031 | -43.1335 | 2026-07-30 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7140c97-4963-3719-8f5b-392da9de7400 | -17.22346 | -41.53001 | 2026-07-30 04:17:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c2e67e04-adf6-35c4-b467-3ccb21168c0f | -18.35822 | -47.19369 | 2026-07-30 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15372c3d-7ae9-3cdb-82c5-2e96e4c871a1 | -16.85952 | -43.3152 | 2026-07-30 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0bad789-eff4-3853-9d41-17386962f31c | -21.35331 | -44.82168 | 2026-07-30 04:17:00 | NOAA-20 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 69396022-8a4e-39ee-b925-6b9ee8d03945 | -19.38565 | -41.44361 | 2026-07-30 04:17:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6611d7e4-121a-3d26-8869-d504d2b2a9c8 | -20.34865 | -47.5317 | 2026-07-30 04:17:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cac1c79-edae-3dfc-bfe7-2804f9929a41 | -16.75983 | -49.30094 | 2026-07-30 04:17:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b65e61b9-0ea3-3c09-a5f0-f75dc95c73b5 | -18.39939 | -43.95378 | 2026-07-30 04:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22d01be8-e05b-3044-a505-5b346fc24984 | -22.05162 | -45.08807 | 2026-07-30 04:17:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf436800-a86e-31b1-9410-915fc9e6f1ef | -18.37987 | -51.45152 | 2026-07-30 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a31d318-d763-3813-942a-46bbb6a399cb | -19.83129 | -48.20584 | 2026-07-30 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1acf1ae4-f3eb-3c6a-ae43-f997cb7086d0 | -17.8326 | -41.96497 | 2026-07-30 04:17:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73598508-ac75-39bc-af34-9e78cb75105b | -17.01914 | -41.22233 | 2026-07-30 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0618456-856b-3512-8b7e-ad99b12d5a45 | -16.49975 | -43.13712 | 2026-07-30 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1effbcc6-9dea-3fdf-9117-0927f7f8cc57 | -20.47787 | -45.18372 | 2026-07-30 04:17:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45461dda-ce42-3d25-956b-18d893fd436b | -21.44277 | -41.10119 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cc4ec977-e263-32a7-b427-1bb7dcb98f96 | -21.45383 | -43.76877 | 2026-07-30 04:17:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e6028a1-305e-3d6b-8a08-a0e3483d1169 | -18.23062 | -42.20776 | 2026-07-30 04:17:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| e927278d-2327-3556-9c6d-55bc1b77c056 | -19.69324 | -44.92551 | 2026-07-30 04:17:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0116be0e-c58b-39dc-89a0-3039816cac0c | -16.63467 | -44.46247 | 2026-07-30 04:17:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d8eece4-b311-3d7b-89b5-67a1bb8b8b99 | -20.34776 | -40.9387 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ac4ec5ea-1e3c-3710-8050-83705dc34989 | -23.40048 | -45.94682 | 2026-07-30 04:17:00 | NOAA-20 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 16cc4d7a-6cf6-311a-911c-7d73895594be | -18.80207 | -53.14474 | 2026-07-30 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a93cf1ff-ef5f-3528-b004-798ea3991d46 | -22.28075 | -45.38102 | 2026-07-30 04:17:00 | NOAA-20 | MARIA DA FÉ | MINAS GERAIS | Brasil | 3139904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 942d949e-082f-3278-afc8-bf2d12062bbd | -19.82768 | -48.20515 | 2026-07-30 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d820e08-c329-3fc7-91ae-4abb607937ae | -22.68444 | -43.79854 | 2026-07-30 04:17:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f6363e1-56ec-318e-9362-3bf0482f921e | -17.39815 | -47.33025 | 2026-07-30 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9576609-9fce-313d-8591-758c5e583e65 | -20.31798 | -42.00898 | 2026-07-30 04:17:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a56dafb7-3b9e-3813-9e06-8189fe814ca8 | -20.35015 | -40.94151 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ab4427c2-5f05-343e-9c80-8e8a56b45e2d | -20.34642 | -40.94088 | 2026-07-30 04:17:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9dc3748-bb75-35a2-852b-cdb411e3de74 | -21.43837 | -41.10548 | 2026-07-30 04:17:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 41de1877-747d-3a34-8a13-84afc0505dc6 | -20.72818 | -42.04554 | 2026-07-30 04:17:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)
