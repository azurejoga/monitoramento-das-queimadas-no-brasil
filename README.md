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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b64f4211-8c67-31fa-b328-d58c3ab8dfb1 | -7.5807 | -44.589 | 2025-09-17 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 4b5a1e2f-8948-3e08-ade3-e9ed1f433b78 | -6.8734 | -43.9636 | 2025-09-17 00:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f992a3a1-bdb2-3fd1-bcd7-685ada26de32 | -15.3996 | -46.1477 | 2025-09-17 00:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e064207c-a9f0-3a09-b53f-7c2bdd27057f | -11.0164 | -48.9297 | 2025-09-17 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 28821c1f-0a24-3e6a-811d-f0254fb9495e | -9.104 | -44.933 | 2025-09-17 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f59192d9-5c56-3307-9de7-0f86a3af88b2 | -11.0393 | -45.0564 | 2025-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f95da86d-d016-3bfd-a232-75f373151217 | -6.6806 | -46.3184 | 2025-09-17 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 5f0da3b3-84d1-392c-bf43-928ce2badd34 | -15.1518 | -49.5691 | 2025-09-17 00:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 421b1d08-6d08-3df0-b783-72929f373d74 | -15.1713 | -49.5661 | 2025-09-17 00:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 3768c0dd-2a2a-3be2-8690-fd24576e0845 | -15.1709 | -49.5882 | 2025-09-17 00:00:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| e1cac020-9a55-320a-bb47-f14417cdf79d | -15.4192 | -46.144 | 2025-09-17 00:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 1f101c27-e587-392c-bdbc-e1764da6c682 | -7.581 | -44.566 | 2025-09-17 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9a0aef8d-da26-3b3b-8c72-50cac578531b | -4.0634 | -47.4943 | 2025-09-17 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 9d73a9e9-f3a5-3447-b254-fd4365180563 | -11.0201 | -45.059 | 2025-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5102cf3b-e6cf-31c3-91d4-21c9f70cda91 | -6.6808 | -46.2961 | 2025-09-17 00:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 46533996-9687-3457-9f22-91879dbddd8e | -6.6129 | -45.584 | 2025-09-17 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5cd40246-7f27-3835-b21d-a2ae6069d0fd | -6.6314 | -45.6051 | 2025-09-17 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 3a7ccc8f-5aae-38a1-af22-bd63170616ff | -2.3763 | -47.6419 | 2025-09-17 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 206c36e7-d414-329d-9b4d-55687b5d3844 | -7.5998 | -44.5642 | 2025-09-17 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 65423d62-7a1f-3a03-b89d-46ffa10307c2 | -7.5996 | -44.5872 | 2025-09-17 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| a65d7724-d51b-3708-b6ce-c84a816da080 | -6.6316 | -45.5825 | 2025-09-17 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| acb6a864-c692-333e-b38f-05bd7978c174 | -15.40132 | -46.12555 | 2025-09-17 00:09:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f0f94842-ca59-3e71-92d5-e6d704a64444 | -23.42209 | -47.15526 | 2025-09-17 00:09:00 | TERRA_M-M | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| fe49a63b-f445-31b6-8cd8-7a68032c5fce | -14.85981 | -45.1233 | 2025-09-17 00:09:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 30.3 |
| df48de37-e46d-3f8e-9a80-0d87124d47bd | -18.36283 | -43.31765 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 0a78f99f-84c6-3842-95c1-9b942ab7ed05 | -17.05415 | -45.8909 | 2025-09-17 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4ed3281e-bd04-3102-8d8a-cebc34894533 | -18.37216 | -43.31646 | 2025-09-17 00:09:00 | TERRA_M-M | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b2f9e128-479a-3297-9898-eac05ea4637a | -15.99872 | -41.86584 | 2025-09-17 00:09:00 | TERRA_M-M | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7fcee142-db77-373c-8c85-1126ee5fe64a | -18.78146 | -42.0215 | 2025-09-17 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 70703dfc-f7c7-34d3-ba03-c3d72492817c | -16.48053 | -43.68371 | 2025-09-17 00:09:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ee5afb82-d9f9-3733-843f-78e828a08b38 | -18.36155 | -43.30769 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 55b74578-6e4c-3d95-a5fc-1bcc56b59308 | -18.46091 | -40.57003 | 2025-09-17 00:09:00 | TERRA_M-M | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5f738f29-f2d7-3dc0-a597-353d689cff19 | -18.16657 | -45.19258 | 2025-09-17 00:09:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 897f3adc-f5f0-3b1b-80e7-36c5b2212437 | -17.95896 | -45.67719 | 2025-09-17 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 954aa527-474d-337a-93ac-65d40824855a | -18.33372 | -43.31221 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 1f73a4c9-81f7-3308-8dae-3665d567a33f | -18.48417 | -42.69532 | 2025-09-17 00:09:00 | TERRA_M-M | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0a9eccba-dda2-39f0-baf1-5af63065358e | -15.26399 | -40.58377 | 2025-09-17 00:09:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| daf8c9f9-d69b-3057-9610-32ec638c95f5 | -15.09013 | -47.34567 | 2025-09-17 00:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3cf20b09-0ea1-37b0-a75b-4abbe01d46a1 | -18.97155 | -40.99134 | 2025-09-17 00:09:00 | TERRA_M-M | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 03d4aa13-b282-3536-8ad4-84b9ffafbafd | -16.61456 | -43.37423 | 2025-09-17 00:09:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 619efda8-bc89-37b7-b6c3-33136a5f06a9 | -20.18937 | -42.31231 | 2025-09-17 00:09:00 | TERRA_M-M | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| eedf9ee8-3310-3249-ba9d-1567ffb35044 | -18.6212 | -43.90345 | 2025-09-17 00:09:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ee5f52dd-2807-329f-a700-44e06b7d9053 | -17.05587 | -45.905 | 2025-09-17 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 94669956-92eb-3e81-ad71-ea99360943c4 | -18.33236 | -43.30162 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| 807d2c09-1e68-3d90-84b3-f05a7a4a2616 | -16.48845 | -41.55615 | 2025-09-17 00:09:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 159cb2d7-01b8-3242-8954-8022140bb909 | -16.49106 | -41.63979 | 2025-09-17 00:09:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b509be44-db1a-3651-8b7a-54edd83b5dc0 | -16.61326 | -43.3643 | 2025-09-17 00:09:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5518bdcf-b9e4-331b-b06a-dee2c48ac1ce | -17.04814 | -45.89971 | 2025-09-17 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 09fbe412-39ed-3859-ae12-d521283048d8 | -18.74173 | -44.54569 | 2025-09-17 00:09:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 484ab3d1-b479-3edf-809f-3200a55a5d9d | -17.19658 | -45.91786 | 2025-09-17 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 24162e9a-53fc-3a0a-9081-092add5cd7f2 | -19.4838 | -43.4651 | 2025-09-17 00:09:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 8441213a-37c1-3de1-8dc4-a515bdedc852 | -16.42474 | -43.6916 | 2025-09-17 00:09:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 54e03d0f-5d5e-3ec4-8d0b-2e1257a957bf | -16.81151 | -41.2294 | 2025-09-17 00:09:00 | TERRA_M-M | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 9604fc13-b8ac-3b65-a071-09daed2cd89d | -14.98967 | -42.23884 | 2025-09-17 00:09:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0df04489-e36e-3975-a339-d28f371fa2a5 | -18.13268 | -44.64536 | 2025-09-17 00:09:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 18716882-b97e-3b54-9eba-c6ac2403d577 | -18.46593 | -43.25705 | 2025-09-17 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 8f2fda9f-ea9b-3b24-a4a3-05dcc8bca4d2 | -15.40309 | -46.14006 | 2025-09-17 00:09:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| dab5c39e-d988-34c0-ac70-e739addceb80 | -17.3324 | -46.81012 | 2025-09-17 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 44ff59d4-8cac-3cfa-be89-15bb0f923c96 | -18.36564 | -43.33929 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bff67194-0dac-38d9-9c04-66b30315d46c | -19.48252 | -43.45484 | 2025-09-17 00:09:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2a95e456-c77f-322f-be4c-adea1f825192 | -19.47298 | -43.4559 | 2025-09-17 00:09:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b72659c8-0a54-3f7c-9609-c0e3d319689e | -18.75178 | -44.54434 | 2025-09-17 00:09:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c2afcbca-c932-306d-9620-5c318b83de06 | -16.04079 | -42.72221 | 2025-09-17 00:09:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9409302-d15f-3ae9-82e1-988a00f57adf | -14.87954 | -45.5264 | 2025-09-17 00:09:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11164e2c-f1be-3ea9-b3cd-f6460d742e3d | -19.47426 | -43.46614 | 2025-09-17 00:09:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c87116ae-f814-3daf-9ef4-f0d871ce16d2 | -16.48973 | -41.56528 | 2025-09-17 00:09:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 8813323c-b902-3d5d-9710-64f1cfe6d1b1 | -15.40481 | -46.15415 | 2025-09-17 00:09:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 43.0 |
| ab02bbef-71bf-31c9-84ae-d7267b15d7ed | -18.36419 | -43.32814 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.1 |
| 3684f9f9-ef96-3247-82c8-34ea88e7af8b | -17.00481 | -41.68391 | 2025-09-17 00:09:00 | TERRA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1ae9fb9a-651e-3657-86aa-42102f444acb | -14.60995 | -46.39481 | 2025-09-17 00:09:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f65508ec-73bc-35fd-bcf9-4e8adf687634 | -19.44069 | -42.34797 | 2025-09-17 00:09:00 | TERRA_M-M | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 489fca14-3b18-3ef9-a75f-f89f753d30b8 | -17.00607 | -41.6931 | 2025-09-17 00:09:00 | TERRA_M-M | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| d093b2c7-72b5-3997-8223-500e50946f83 | -17.3361 | -46.81591 | 2025-09-17 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3e9acee1-9a86-3e61-b57f-faaa8779690b | -17.04334 | -45.89216 | 2025-09-17 00:09:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7119c7bb-6fb3-38f0-a181-22e8ab60fb2f | -20.48444 | -42.39135 | 2025-09-17 00:09:00 | TERRA_M-M | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| f8c091da-570c-390d-8414-05acedfdbfc0 | -14.61159 | -46.40827 | 2025-09-17 00:09:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e178391f-2e2d-3a70-b3a1-93f7a712286f | -17.33418 | -46.79944 | 2025-09-17 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8b233734-989d-3621-9a21-94031f91b677 | -17.96231 | -45.24999 | 2025-09-17 00:09:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 76494dd9-a0b2-30bf-9ad2-37a06e9c2d60 | -17.32451 | -46.81767 | 2025-09-17 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9b8a9d65-e814-3dbc-b1b9-05f48d55557d | -16.94421 | -42.87434 | 2025-09-17 00:09:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3899b6ed-55c9-330a-960b-b58e89ebe88b | -15.41546 | -46.15213 | 2025-09-17 00:09:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 103.0 |
| df1a07f5-3d1a-3e24-9e15-a5b423a2f085 | -15.41372 | -46.13795 | 2025-09-17 00:09:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5ee1c455-7754-3f8b-b5f7-716ff39bc986 | -15.77069 | -41.61491 | 2025-09-17 00:09:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| a45c7f96-4eea-3f42-947f-da87bdebb3c5 | -14.39982 | -43.52883 | 2025-09-17 00:09:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58936dc5-8ac7-3647-98fa-b55f957bc9b3 | -17.45556 | -41.81022 | 2025-09-17 00:09:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3e1a137e-fa28-3d28-8b9f-2d1b562575a9 | -23.42417 | -47.1773 | 2025-09-17 00:09:00 | TERRA_M-M | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 544c53ef-6f8f-3238-b32f-6ab682ad7119 | -17.6839 | -44.21915 | 2025-09-17 00:09:00 | TERRA_M-M | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0931536a-ea90-317f-869f-8cc2c545ee33 | -18.37348 | -43.32673 | 2025-09-17 00:09:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 86022369-7e5d-3916-8897-bcfbc2a84959 | -15.3996 | -46.1477 | 2025-09-17 00:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 9f9b37aa-e9b2-399b-98f6-ffc919240452 | -15.4192 | -46.144 | 2025-09-17 00:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 4487d112-6a88-3db2-ac0c-83256aa5df1f | -4.0634 | -47.4943 | 2025-09-17 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c42ff035-0232-3eb6-aa20-d8c4600e6f35 | -6.6316 | -45.5825 | 2025-09-17 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 490ea67d-b2c4-34ec-8f09-65efe7f490f6 | -7.581 | -44.566 | 2025-09-17 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 359bf0c1-015f-38a0-a76f-27d6191da055 | -7.5807 | -44.589 | 2025-09-17 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 1a9199c1-d6fd-3789-9397-27ab9b09f30b | -8.6693 | -46.4067 | 2025-09-17 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 664fa48c-0c41-3ee7-8bd4-da8657ec8817 | -15.4198 | -46.1208 | 2025-09-17 00:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5d130624-1199-39b4-9782-3e7256145875 | -4.0633 | -47.5161 | 2025-09-17 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 849b59ee-b3bb-3ef3-96fc-b9cde5485684 | -6.8734 | -43.9636 | 2025-09-17 00:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9f8a8d85-5143-3c64-a6e0-50024d9666c8 | -15.1713 | -49.5661 | 2025-09-17 00:10:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cbb3e961-863b-35a4-b063-da64f1173dc3 | -7.5998 | -44.5642 | 2025-09-17 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.7 |


[Clique aqui para ver as próximas entradas](README2.md)
