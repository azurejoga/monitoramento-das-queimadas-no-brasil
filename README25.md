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
| dd7906ac-0c01-37e0-b6da-08ea10f8da4a | -7.84931 | -44.20084 | 2025-08-02 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b6e15c6a-85b4-3818-bc39-398b4f165b71 | -6.07346 | -42.33387 | 2025-08-02 11:51:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f7981af5-e72e-3478-8f57-5b8032d25bdb | -5.10144 | -41.70926 | 2025-08-02 11:51:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 93898649-e49c-34dc-8ac8-93c92c55968e | -2.93866 | -40.09685 | 2025-08-02 11:51:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a9e2e87e-46cf-36c7-b9b2-6a424301969c | -7.86015 | -44.20269 | 2025-08-02 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c367efad-0d67-32fd-89de-3e8b39997bd9 | -2.94171 | -40.01292 | 2025-08-02 11:51:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8cc73ed4-3366-39eb-af77-31bfb37d0b08 | -8.02281 | -43.14924 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 72c83121-bec9-3ff7-9ab3-2539a73be9ad | -8.02637 | -43.12593 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| 344178d6-e66b-383b-b4eb-8e7133009c33 | -3.9546 | -41.48442 | 2025-08-02 11:51:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| af38e734-6f90-3fb0-a8e2-4d738b37bd1d | -8.03816 | -43.11579 | 2025-08-02 11:51:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| dd33b36c-cf15-37e3-b32f-30467714291d | -6.49883 | -43.67309 | 2025-08-02 11:51:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 3007976a-95f9-30c5-ada6-a55f195b2943 | -6.40419 | -38.13726 | 2025-08-02 11:51:00 | TERRA_M-M | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 887355f6-0dd4-31b9-a5f4-065a01c9daf4 | -14.17782 | -45.45821 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 272.5 |
| 99a935aa-ac3d-381f-a804-139fcbf2f1d2 | -15.05105 | -41.97949 | 2025-08-02 11:53:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4ffe1063-a80c-305a-b041-e4984e3d69b3 | -11.94465 | -44.91839 | 2025-08-02 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a9bd5bb1-b9fa-37f7-bf50-00b009409e2c | -10.46454 | -46.93046 | 2025-08-02 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| c8705bf6-2932-3454-abe5-0779c02b499c | -14.17148 | -45.42907 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f12d7e55-baa2-34a9-bbb5-e26d2285624f | -10.6507 | -44.47855 | 2025-08-02 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d26dedc4-870c-316c-a33b-6dfff88dca9c | -14.18123 | -45.46488 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| efa174e3-f0fe-39ee-b4cf-45978189bbc4 | -8.4416 | -47.46968 | 2025-08-02 11:53:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a337ff3c-0eb1-319b-9ca7-6d774e052879 | -14.17564 | -45.4719 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 95bf2166-f26f-3519-8377-cd254c5d49f4 | -10.65528 | -44.48525 | 2025-08-02 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f799f34b-8739-301f-9252-fde5fd8cee3e | -14.16493 | -45.4701 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cb4eefad-2d62-3588-882a-7325fdbe203a | -10.6278 | -45.29821 | 2025-08-02 11:53:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| de915cd1-6b52-3e19-b71b-76125d27d1fd | -12.48298 | -41.05295 | 2025-08-02 11:53:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| ef8f537a-2ddb-3b75-a84f-6395084211cf | -11.94018 | -46.67841 | 2025-08-02 11:53:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b863db7e-b4dd-3ae7-8b78-23ca3666217c | -12.48558 | -41.035 | 2025-08-02 11:53:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 18cfe185-40d4-37ac-8bc0-6a025da8a1c2 | -10.47069 | -46.97333 | 2025-08-02 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e49000e6-1710-3b4a-bc9f-e362e64b513e | -14.16712 | -45.45638 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 3133a3b1-0fd6-3454-adde-f4c33a4d693b | -12.48428 | -41.04398 | 2025-08-02 11:53:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| fea74162-6fee-33c1-a54d-f620f12836e9 | -10.64868 | -44.4917 | 2025-08-02 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9840579d-62d4-336f-bdbd-f5c28297d162 | -15.27791 | -41.69025 | 2025-08-02 11:53:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 469499e8-63a8-3cdd-992f-1c15c855f6e5 | -14.1693 | -45.44274 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 62411e65-3d80-36b5-b8fe-c72e886d8bea | -9.21443 | -44.53579 | 2025-08-02 11:53:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 59e71ed7-5806-3b30-8d69-5fc9e3de5f97 | -14.17999 | -45.44454 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 9a04c0e6-e786-3034-91f2-631ab12a8147 | -9.1889 | -45.28617 | 2025-08-02 11:53:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f6a62326-82a4-3f8d-8024-87438d87e51a | -14.86369 | -42.43674 | 2025-08-02 11:53:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8c54e0cc-4200-3864-8fda-bdcbda8a0143 | -11.94263 | -44.93118 | 2025-08-02 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9a792d0e-e63a-3953-bf1f-fd3fb7b3eafa | -14.1835 | -45.45123 | 2025-08-02 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6ed56e82-e0b9-3df8-b5a4-3328eecc0255 | -12.82261 | -45.43135 | 2025-08-02 11:53:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5b59bb5b-aa3c-3aca-87cd-53228c914065 | -11.22427 | -50.50445 | 2025-08-02 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 9588a89f-e802-37c4-b63e-c2dc0459858e | -14.86507 | -42.42749 | 2025-08-02 11:53:00 | TERRA_M-M | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 5f0b288c-3c8e-34c7-857f-8a4a4f0a9d51 | -11.92314 | -44.8468 | 2025-08-02 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e332d96a-7a0f-3ade-ab0f-cd1902384461 | -10.46117 | -46.95074 | 2025-08-02 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 93e77594-56da-3fc7-8a6d-2db2baabafbb | -13.18387 | -42.36966 | 2025-08-02 11:53:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b98a9890-284e-3439-a00a-9d41fde38985 | -11.22013 | -50.49616 | 2025-08-02 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| dff3444a-e6f3-30c7-b850-c4a2088ece03 | -12.67205 | -44.53297 | 2025-08-02 11:53:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| abf8022d-9a0b-3bb0-8fe7-2ed2a918040e | -12.66564 | -44.5064 | 2025-08-02 11:53:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f3a5618d-dad0-3f42-8aa8-6591e8ddf11c | -16.71034 | -47.58063 | 2025-08-02 11:55:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 870aa50c-26a6-347e-92bd-87a474eb1b7a | -15.58309 | -47.51544 | 2025-08-02 11:55:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 975b3b94-06e1-3a9f-8b3f-8dcbfe44b2c0 | -18.74402 | -47.52211 | 2025-08-02 11:55:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f44e994b-fc57-3c1a-af35-d454e16a16b3 | -18.72962 | -47.53647 | 2025-08-02 11:55:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 939e54f9-863b-3c9f-91c0-420de23df409 | -18.46611 | -42.35762 | 2025-08-02 11:55:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8e6057e0-bf7c-34cc-985d-1486cf37842c | -17.2936 | -46.04927 | 2025-08-02 11:55:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ed502823-b204-3c07-aeb6-729facdf62fe | -16.71339 | -47.56321 | 2025-08-02 11:55:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b9a041aa-4ac4-3b25-9870-2c5e3aeabf15 | -18.73312 | -47.5302 | 2025-08-02 11:55:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e7409486-c74a-33e4-bd3f-22bdda206a20 | -18.74738 | -47.51586 | 2025-08-02 11:55:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8a17f8dc-70e5-361b-8053-7eeecfe21c44 | -17.90024 | -44.26148 | 2025-08-02 11:55:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 68cb2744-549d-3aaf-b49c-07e84b9f35cd | -21.04174 | -43.72328 | 2025-08-02 11:57:00 | TERRA_M-M | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 5b080d99-1af6-35b6-a8be-0adced6cfdd0 | -21.04028 | -43.73299 | 2025-08-02 11:57:00 | TERRA_M-M | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| c3a8abe9-ac2a-3723-ba9b-971420b4fc89 | -20.33237 | -46.61926 | 2025-08-02 11:57:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae9e402b-196a-35c3-81a8-231f647e90c8 | -8.0324 | -43.1022 | 2025-08-02 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 149.6 |
| 6088a05a-2c3b-3f36-a655-0b118248f584 | -8.0321 | -43.1257 | 2025-08-02 12:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 207.1 |
| a1fd3649-0bf3-3e52-b13c-0c99023fd737 | -14.1672 | -45.4673 | 2025-08-02 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5cc03cad-691d-3a04-9f7b-12b6a49d1ff8 | -14.1672 | -45.4673 | 2025-08-02 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| a6b9ca12-1e6e-393b-9102-13805df954ba | -8.0513 | -43.1001 | 2025-08-02 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 46449afa-608b-3502-89b3-97ce85b7cc53 | -8.0321 | -43.1257 | 2025-08-02 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 196.5 |
| d9ea7746-9fbb-3dc4-b372-da76a911b9ef | -8.0324 | -43.1022 | 2025-08-02 12:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| f692eb76-aed8-3113-9a40-907a2e666a38 | -8.0321 | -43.1257 | 2025-08-02 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 222.6 |
| e327f3ca-795d-3fcf-af04-e43eaa8d65a5 | -8.0513 | -43.1001 | 2025-08-02 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 68179ac6-13fa-3aeb-a514-7b3cfbb3eca4 | -8.0324 | -43.1022 | 2025-08-02 12:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 5b9023a7-90cf-3c73-9880-59fab30811ba | -11.9403 | -44.9264 | 2025-08-02 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 2063d97c-910c-3693-9188-ee40900182dc | -14.1672 | -45.4673 | 2025-08-02 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c7e84f75-40d3-3f55-bca3-b6f2a822a1f4 | -12.6784 | -44.5085 | 2025-08-02 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 809d0258-f128-3bd8-94c3-c35baabf893d | -8.0513 | -43.1001 | 2025-08-02 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 1162a76c-e71a-30bc-aaf3-e2958d86a04b | -14.1672 | -45.4673 | 2025-08-02 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| c95da75a-08e4-3e78-8eca-5ee80f8c6822 | -8.0324 | -43.1022 | 2025-08-02 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| e4bf5a16-7145-366d-86d3-ce8238121d80 | -8.0321 | -43.1257 | 2025-08-02 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| b767171f-4ee5-3191-8723-99439a420163 | -8.051 | -43.1237 | 2025-08-02 12:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| a611ee0e-316f-320a-9b71-2f38f56b55bd | -14.1672 | -45.4673 | 2025-08-02 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8e1b55a0-86ff-32b2-96c5-a8205acb6361 | -8.051 | -43.1237 | 2025-08-02 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 8a452018-b15c-3abd-b2b5-718cd90f21f4 | -8.0324 | -43.1022 | 2025-08-02 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.0 |
| d2dc56fb-f38e-3b10-a1a4-aee9554fb82e | -8.0513 | -43.1001 | 2025-08-02 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 2e6259c5-86fd-381e-a1c6-2bd2e9cb8693 | -8.0132 | -43.1278 | 2025-08-02 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| b112a06a-fb65-3347-8630-1c2e58fb6afd | -11.9403 | -44.9264 | 2025-08-02 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b95fae71-7779-3774-ba5d-4c6a4245d018 | -8.0321 | -43.1257 | 2025-08-02 12:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 236.0 |
| 6042ea35-63e6-38cb-a9b4-07e9222cdc8d | -12.6784 | -44.5085 | 2025-08-02 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 4de623e9-4273-3a85-9202-a1603ccbe3e6 | -8.051 | -43.1237 | 2025-08-02 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 8303b94d-fed6-35dd-89bd-706755128559 | -12.6784 | -44.5085 | 2025-08-02 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 210add5c-35c7-3daa-85a6-dd6d7ba27db7 | -8.0324 | -43.1022 | 2025-08-02 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.6 |
| ae2ae25c-bd56-3ab5-9ff3-d1696227c586 | -8.0321 | -43.1257 | 2025-08-02 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 380.7 |
| 19d4a0fa-46d1-3d56-bc18-80286893cb01 | -12.6591 | -44.5117 | 2025-08-02 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c956ff56-5c16-3fde-abe7-3741138f4e30 | -14.1672 | -45.4673 | 2025-08-02 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 1508ef07-222c-3de7-ae18-036c4ec79f17 | -8.0513 | -43.1001 | 2025-08-02 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| b691a917-c878-3e73-add2-930c8d47c974 | -8.051 | -43.1237 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| 9cbda831-5364-3ae6-884f-c4ec4478f519 | -10.4764 | -46.9654 | 2025-08-02 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9b77eef1-d983-3ed6-8e4d-d7d9c6974363 | -8.0318 | -43.1493 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 7279c6ec-96a4-3ada-85f3-4e25bafff387 | -8.0324 | -43.1022 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 197.3 |
| 620a4131-37ec-3aad-bc38-42a167f9a980 | -8.0321 | -43.1257 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 478.3 |
| 695d4fb3-2fd3-34bd-9fc5-6b594b392e96 | -8.0513 | -43.1001 | 2025-08-02 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |


[Clique aqui para ver as próximas entradas](README26.md)
