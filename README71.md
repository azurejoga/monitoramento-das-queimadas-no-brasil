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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d944d78-e855-3730-8250-ca7433b4e1c7 | -16.83855 | -41.04253 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e15690b6-6063-39a1-84a5-1eaa22764a98 | -11.38985 | -46.69746 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b67123b0-eb0f-36f0-a1b2-825b293f5e66 | -12.37174 | -41.484 | 2026-10-08 04:04:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cd94c719-e5b7-3d8d-acfd-0d0ffcdcbe19 | -12.23788 | -44.73385 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee1c92b8-4a70-3a4a-bbd5-a4925ff5c11d | -18.02572 | -46.20786 | 2026-10-08 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9628bc7f-6fba-345d-aa8f-7aef11ad3851 | -15.45178 | -42.02692 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2109d5e5-4d30-3404-b6bb-b56ac575ed1f | -12.15576 | -44.71326 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77896a26-bb41-3850-b9de-5ba664431b8e | -16.01037 | -43.6008 | 2026-10-08 04:04:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb2ebbe6-4971-374b-9a63-96b586c70df3 | -15.30039 | -41.14294 | 2026-10-08 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a0b41d67-03dd-3e29-bc43-630bcadffdd3 | -11.76271 | -44.94767 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87067e99-3ec0-3239-b69d-8440bf89b372 | -13.1687 | -54.32747 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 123fb935-36a1-3022-9b05-b489b488dbc7 | -11.78771 | -46.56693 | 2026-10-08 04:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 654e7919-1aee-300b-88c5-2eff8fcf2b19 | -14.06603 | -43.75606 | 2026-10-08 04:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f75a52b-fa3f-3636-bfd0-f2f8c7f5d600 | -11.77203 | -46.7766 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f72c271-a156-3301-be03-d116d1107fce | -14.62964 | -54.25906 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8672ad64-dac6-3aea-9031-71608b8c0646 | -18.98615 | -46.57743 | 2026-10-08 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 058ea5e0-bab6-317b-b1c4-fa3b643f1909 | -11.32524 | -46.68961 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00c2e518-27a6-38f1-8497-3e60cbdd436e | -17.12038 | -41.34121 | 2026-10-08 04:04:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a32079b6-de51-3fe9-8ddb-bed59d3ea9e8 | -17.87583 | -45.99 | 2026-10-08 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ae941d3-d318-3761-a44f-e76aa62c29a0 | -16.89999 | -40.89074 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 943c2ae2-4109-30f7-a7cd-41a6e5de0c57 | -12.15721 | -44.75118 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc037cdb-a14f-32cb-a80b-f21ef248ef9a | -12.22727 | -44.71724 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30bfce88-30f4-35a3-a629-f400602abfc4 | -13.36325 | -43.87582 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29ebb9c5-b7aa-3482-98ac-ca7d7a301aa5 | -15.3159 | -43.67075 | 2026-10-08 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc78a81c-a606-3110-a394-66f096889de3 | -12.15933 | -44.76233 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 259f5cf8-045b-30e0-84af-1ac6714b5af0 | -15.42233 | -43.70612 | 2026-10-08 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39a5d704-6481-3078-85a7-4b81a42c16de | -14.04878 | -47.01011 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43a8c982-39d3-30b2-8989-eb6606135c4b | -10.88126 | -49.15195 | 2026-10-08 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ff8b76fe-9101-34d2-b65d-edb680b99ffa | -11.31995 | -46.66674 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a51f67f-9832-302f-914a-8d70ae919017 | -18.04416 | -44.59595 | 2026-10-08 04:04:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47286baa-7355-3cdc-824c-716b20f40e9e | -15.41081 | -39.25019 | 2026-10-08 04:04:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f483ab6c-9fa0-3a0d-88f0-137b354ff5cf | -15.48225 | -40.76998 | 2026-10-08 04:04:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 752e6257-0d6b-3849-9293-38337390856b | -11.77287 | -46.7721 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b2d46e5-c6f7-3be7-b233-3ce06bb3bee2 | -11.78029 | -46.78289 | 2026-10-08 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d0c19d1-8b63-384e-ae3c-9d7cb9ead0a5 | -12.19515 | -48.42439 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e73d72f6-a0a8-31c4-bafc-b93d71004520 | -12.19916 | -48.42388 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f32631f2-5bbd-3375-af5e-178ccbe3c623 | -12.0364 | -43.44342 | 2026-10-08 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7410812-b574-37c4-bec4-5afb366c232d | -13.16491 | -54.32815 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a1a391-7c67-3747-8091-b31c5af8b2c4 | -14.92185 | -48.09153 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0c1fc87-7e16-3fa6-bed8-5714f7606272 | -13.19431 | -47.87634 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9be0afa1-e561-35c5-aa4b-3115e15fb948 | -17.11145 | -41.3545 | 2026-10-08 04:04:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8204ddf0-a967-34f9-a2c8-4ac4d09dabad | -14.92275 | -48.08687 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa796c2c-8941-3aaa-951a-f4e6a11c78b5 | -14.92553 | -48.09773 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62f20e90-1d89-3d28-b934-dd47ba6f6258 | -16.77492 | -42.79025 | 2026-10-08 04:04:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc912593-b435-3f87-bb48-2557d7b7736d | -12.9779 | -41.02098 | 2026-10-08 04:04:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be9af65b-ffb9-33e2-9fcb-82c121c04102 | -15.5619 | -44.52128 | 2026-10-08 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d00ea156-c633-3d44-a1f4-02df7a79a652 | -19.3117 | -40.90128 | 2026-10-08 04:04:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3839a449-fc46-3305-bd87-2a98b66e9fde | -17.43288 | -43.64848 | 2026-10-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a03d51f-b60b-3379-90fa-0bb0b110ad6a | -10.88197 | -49.14831 | 2026-10-08 04:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89b7a69d-e377-3843-a04c-dc996576466c | -12.2282 | -44.71206 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8e61777-769b-3cb5-ae9a-9298f0b5040a | -16.58751 | -41.84162 | 2026-10-08 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 88169f33-7462-392b-b126-bc11243e9d70 | -15.66311 | -43.31673 | 2026-10-08 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d27d3ba7-336e-3ff7-8b2c-4733a737b6e5 | -11.39477 | -47.55127 | 2026-10-08 04:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1bccd83-5c1a-391d-a08b-7784ac4a200c | -14.92243 | -48.11383 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a2a4a5a-8600-39b3-8805-04e779a5e9bf | -13.19531 | -47.87112 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d8a54a59-116e-3c3c-a7db-32cf86256dff | -15.6797 | -50.57106 | 2026-10-08 04:04:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24af509a-74df-319c-b2da-fb4a212dffe3 | -13.50688 | -44.37177 | 2026-10-08 04:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28951b93-6247-35f6-b8fa-af27c6d522e2 | -13.80395 | -52.79139 | 2026-10-08 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30cc85fb-7826-3f5a-8937-6d684a3f9d9f | -17.09072 | -41.75603 | 2026-10-08 04:04:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc23ffee-af18-3bb1-8105-c106572a125d | -18.26092 | -42.16996 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d4ab6b29-bda5-3f5f-a3a3-f9a934e5141a | -15.04126 | -42.0028 | 2026-10-08 04:04:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 23a07b3f-f9db-3b32-a5ba-d2560f3520c7 | -19.02671 | -45.64856 | 2026-10-08 04:04:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 531b486f-9514-3c4b-b48c-410d690d1b5d | -14.08839 | -43.80082 | 2026-10-08 04:04:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a156f688-9540-3187-86c9-2b005816ca8d | -12.20017 | -48.4255 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3af3cc13-1a96-39ae-b42d-8ce0fa1a205d | -16.89499 | -40.90094 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 980a5938-0c6a-33e0-a291-6e6d8d2459e0 | -15.42493 | -46.1104 | 2026-10-08 04:04:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d87cef3-b681-330a-822b-9c699a00ba52 | -15.76867 | -43.96544 | 2026-10-08 04:04:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b28a2f29-69c7-30fe-863e-3bd6bfc5030a | -13.68961 | -49.12398 | 2026-10-08 04:04:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d888aac-72cd-303d-8f40-e582c3908bab | -13.37138 | -43.88359 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5207faf-e911-364d-969b-8e4b3aadc8c5 | -11.76937 | -45.53527 | 2026-10-08 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0009a96-419c-30a3-bf27-f0f8d4b36e78 | -15.41948 | -43.70124 | 2026-10-08 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8e0ca762-1d01-362f-88ea-1aaeaaaeeabf | -13.80272 | -52.79705 | 2026-10-08 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73e1664e-f1ac-31a7-93bf-c652bab43340 | -16.13072 | -46.88735 | 2026-10-08 04:04:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddc89d94-f593-3da1-b0eb-e4d6682d8710 | -16.90112 | -40.88356 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 495edcd7-6d81-3779-a828-c6c243422750 | -15.56273 | -44.5166 | 2026-10-08 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6a44465-469d-3bf8-917c-02e12cccf4b4 | -14.96568 | -47.53946 | 2026-10-08 04:04:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e3318f4-c641-37eb-aa32-ec9989b9f73a | -14.62811 | -54.26595 | 2026-10-08 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ea8a529-41a9-35b6-b673-caf56c44e364 | -16.75513 | -53.38354 | 2026-10-08 04:04:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 73a22ec9-9ff3-3380-9aa8-83ca6c39dfcd | -13.50393 | -44.36627 | 2026-10-08 04:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7175a7ce-5060-3c7c-8f32-38cb89dbba03 | -13.5031 | -44.37097 | 2026-10-08 04:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0ee80fcb-21db-3719-9889-113039485dd3 | -11.80784 | -47.34979 | 2026-10-08 04:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71bdad69-ad7b-3837-9d8c-5fba95d16a52 | -12.19857 | -48.42687 | 2026-10-08 04:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1dc4cdd-c474-307a-b79d-b666884789a9 | -16.84186 | -41.0431 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 385696f7-3f83-3efa-80b7-7eda7d0151ab | -13.50223 | -44.37583 | 2026-10-08 04:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7050d0db-d32a-3d50-a471-1822126bdf59 | -14.83112 | -43.57069 | 2026-10-08 04:04:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6f37954-3f7f-3732-a869-85d37440115f | -13.18903 | -47.87962 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bfbc568-d3b8-3ccf-8937-817f374bdaf2 | -12.23571 | -44.72273 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1a0baa1-0707-3e68-9901-311be69de52f | -16.91523 | -39.65118 | 2026-10-08 04:04:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbd3a71a-5701-3b02-b2ee-07efef414eec | -15.62428 | -42.99043 | 2026-10-08 04:04:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28b3c164-ec9a-3ae1-ad48-f433c6639df0 | -13.1792 | -48.13809 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d45ffbe-ae1f-35ec-9f79-2019219fba0c | -12.23425 | -44.72385 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 748741c1-dd1e-3dc0-9b67-e2a483591d77 | -16.87349 | -40.60555 | 2026-10-08 04:04:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5227c637-f507-3261-bbc2-c2cbc93fb349 | -13.18794 | -47.88552 | 2026-10-08 04:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 824b4287-af61-3d9b-a92d-f2f1a573f888 | -18.10419 | -42.54619 | 2026-10-08 04:04:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 11c9f105-f418-32a8-bfc2-1c953a52894a | -18.26032 | -42.17361 | 2026-10-08 04:04:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4bdc2bff-6125-37e3-ab30-11eb59478a97 | -11.74504 | -45.28176 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40fb9894-66da-338b-ac61-d8eec94e8b56 | -16.7607 | -45.23932 | 2026-10-08 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea4b0d3c-60e7-3408-8a86-b6da17ce9340 | -12.23482 | -44.72792 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be711a34-b5cc-3bc7-bfcf-50044bf459e4 | -13.37217 | -43.87906 | 2026-10-08 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d94b4137-1111-30ff-8a46-8233b0f269dc | -13.23118 | -43.39581 | 2026-10-08 04:04:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README72.md)
