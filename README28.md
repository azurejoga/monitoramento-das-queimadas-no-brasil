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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2423be0-079f-3f41-8306-9298463594a1 | -3.9686 | -47.8684 | 2025-08-12 05:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8972214f-5b31-3688-a772-9a9e708eb89b | -16.3157 | -52.8988 | 2025-08-12 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 70f251cf-8705-3a68-93c9-639b36bbdb91 | -16.2957 | -52.923 | 2025-08-12 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 55ce317b-d0d1-366d-8732-98e2bb7fb861 | -16.3153 | -52.9201 | 2025-08-12 05:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f351d5c8-2388-33c7-b266-3fdabf640ee7 | -8.9401 | -60.7288 | 2025-08-12 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| bbb753ec-51e3-30b0-8622-1a3088fc82e0 | -3.9684 | -47.8901 | 2025-08-12 05:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 5e693ba9-97f1-3832-b060-a976821687b4 | -17.65374 | -46.66472 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d36fa073-2df0-3d3a-a26b-71a21cf35dee | -20.34882 | -48.92839 | 2025-08-12 05:01:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c573a7e8-3b5f-3ad5-ac67-fcbb233788ab | -22.19656 | -54.76392 | 2025-08-12 05:01:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e472f823-3d6c-387d-b10e-13740cc61a6c | -17.56452 | -45.32405 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae90bcab-bf42-38a0-b421-364192aca524 | -16.30448 | -52.91949 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 32fe49cd-45ee-32a3-b1ce-ac57b5bdadee | -17.64084 | -46.67909 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce90af27-49a8-36dd-a604-4f4fc8884e74 | -16.29967 | -52.91693 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 021d04e5-21cc-3501-ac73-191da45a27c9 | -16.29655 | -52.91204 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cecb5ab-6ffa-35de-82d6-fc8d80272010 | -19.3877 | -48.89894 | 2025-08-12 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d71a2f4-cf42-3652-b3bb-6f2ffe44e0fd | -16.30078 | -52.91891 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 46567169-a0d1-394b-8440-bab75ae142e5 | -16.39662 | -50.89593 | 2025-08-12 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eddfb21-e9d4-35ca-8ea1-90afc34260f3 | -19.71481 | -46.22497 | 2025-08-12 05:01:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2e841b5-bdc8-3d86-8897-ceee5f0b550a | -17.65896 | -46.66947 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8eb6b82c-a497-39f2-9ea3-dd782e8ef549 | -17.65608 | -46.69712 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7570fed-7f7c-3fd5-a4e9-017344527e38 | -16.38887 | -50.88973 | 2025-08-12 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbbb3e89-feab-38f1-89e3-040453b74002 | -19.08213 | -48.14793 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc7888e5-a8ea-38e1-92a9-df40f0427e62 | -17.65128 | -46.68848 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a5476f3-faf5-3a13-99c2-252829c796df | -16.38782 | -50.89802 | 2025-08-12 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ad75e98-7306-3d1a-b237-2891a8e4d160 | -21.28525 | -50.38938 | 2025-08-12 05:01:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d816a1a7-9dbf-39f6-93ac-9e2323a057dc | -18.63459 | -46.83033 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2796fd6f-d285-3e68-a3a9-65cd740bb60e | -16.30509 | -52.91515 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e8d20001-5e28-34ec-8c13-189ffb3cc9c0 | -18.62029 | -46.86037 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25044513-ef31-358b-8167-0fc35d721e64 | -17.66335 | -46.68209 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 28409c10-467e-3938-be24-7fa224ab0c66 | -17.64688 | -46.67583 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bbd5b55b-e6cf-321d-9fa7-ff356258a41d | -17.65649 | -46.69319 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9c6ddfbd-32ff-3e65-a6bd-f60187400c8a | -18.63718 | -46.83081 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f2f4293-b3f6-31fd-9078-4e4fae1006cf | -16.30017 | -52.92327 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4d76789-dd9d-3148-85b1-9e3d9bb479e2 | -20.56265 | -54.65609 | 2025-08-12 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c9ff521-08d7-35a7-887c-e3016a2c3fbf | -16.30573 | -52.91068 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a0c57a41-bdcf-3bdd-b4e1-81d42014a8b1 | -16.29398 | -52.91352 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b1530e5-a00d-3879-84e4-b36eaf5ea18d | -17.57018 | -45.32956 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| f417bad6-1e31-3096-a5d9-bf6a7a8ca83e | -16.9875 | -49.20815 | 2025-08-12 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3701a399-d8f5-3c9a-8bb6-bb9bede590f1 | -16.29647 | -52.9227 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a085dbf9-3038-3e7e-b6f9-418ec09bf4f7 | -17.65937 | -46.66553 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3b9a429-cb99-3af4-9dc2-265ad4dab3ba | -16.03434 | -51.39009 | 2025-08-12 05:01:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9f5feab-70f9-3d75-8d66-4b7a8fb075ed | -17.56922 | -45.33943 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 00f6f9c8-7c66-3a36-a2d0-e32a6530970c | -15.30015 | -59.23733 | 2025-08-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c1bce4-5cd6-31e1-8de9-aec4df543f48 | -16.39198 | -50.89892 | 2025-08-12 05:01:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e88793c1-63a9-30b1-9cca-066f071cd94f | -21.12517 | -48.82652 | 2025-08-12 05:01:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5433ec39-9cb3-3c5c-b4e7-deab661e8ef9 | -17.66294 | -46.68604 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| eba44f4a-9822-3c88-ae0a-91a186b20ae2 | -17.64729 | -46.67188 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d6a74dd6-a60f-36eb-9807-42562d3f8215 | -22.98284 | -49.02953 | 2025-08-12 05:01:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10faed0b-d79b-3110-86fb-cdfe240b18c4 | -17.64125 | -46.67514 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3c4f7f69-4567-3c2d-a8c8-bd414dd3fa00 | -19.00172 | -57.62401 | 2025-08-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d87df9a5-f991-3a1d-9f94-686c5d5530a4 | -16.29848 | -52.92567 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a2f8494-a807-3342-8a22-efbee188dfc4 | -16.28722 | -52.90779 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b59c727a-3630-3afd-84da-44f14e2d6610 | -23.26995 | -51.98863 | 2025-08-12 05:01:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0285d475-3d29-3624-85d0-e08a0d259bf3 | -18.61242 | -43.91142 | 2025-08-12 05:01:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4c06242-be20-3ada-a0c9-d42de16501a5 | -17.64565 | -46.68771 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d68d8d7-a780-3ee6-86dc-b88fe9762ed1 | -16.30139 | -52.91459 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4812b637-4e28-3cc1-83a0-86d46917a761 | -19.29583 | -48.43605 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d2a7f15-dcc5-3f26-89b9-d2f3d1c1c183 | -19.29651 | -48.42976 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 799deb43-163f-35aa-a2e3-ee8ec58e1b14 | -17.64647 | -46.67979 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ccad4aca-2673-3d0f-9c65-f47621ec19bd | -16.31137 | -52.91433 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a78cfdf2-2b48-3ac3-b714-4be4f73c2119 | -17.64165 | -46.67119 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d7161b8-e68f-3482-9e27-7adfb71d1c79 | -22.98658 | -49.02651 | 2025-08-12 05:01:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd41664e-17cf-3d3a-aabc-e939138cdbfa | -17.65731 | -46.68529 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 3184a7bc-4f5a-3134-9d97-07d527f1944d | -16.30278 | -52.92184 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 77fcf140-37a1-3f4f-814f-66a50055d17d | -18.63421 | -46.83425 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 229ef8d3-df7a-38d9-9a5a-79434ef1d2e6 | -17.65169 | -46.68454 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4fd317f6-e77f-3bbc-9f26-91c33d03746b | -16.29337 | -52.91786 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b50bd0f9-28fd-3b47-a4d4-a80916fbf2c8 | -17.65251 | -46.67661 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 64049bb3-8cfa-3a47-9e69-ad7f39758057 | -19.07854 | -46.18484 | 2025-08-12 05:01:00 | NOAA-21 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3dd248c-fd3f-394d-8ed2-a68c7e907e7f | -17.5697 | -45.33452 | 2025-08-12 05:01:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 31c42982-7e82-304a-93d3-9235123a8619 | -17.64206 | -46.66722 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 706e106b-0b32-3d67-87a7-b7b79fe999f2 | -17.6521 | -46.68058 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e10e0356-e09f-3b45-bbfa-938ee0c49e5c | -19.47351 | -55.40911 | 2025-08-12 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 9e261f10-8008-3e67-848b-ae8b9072e481 | -16.30202 | -52.91011 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ae0b205-4508-3520-aa1a-51afc4454fbe | -17.65772 | -46.68134 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| dbf41396-f1da-30bb-9d29-8988dd923016 | -15.30367 | -59.23798 | 2025-08-12 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42047cc6-558b-3631-b345-4b8bef345f63 | -16.30387 | -52.92385 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38b6fd5b-7ea6-3c00-bdaf-5b6ae82ad265 | -17.66418 | -46.6742 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2371c4a4-0068-33ca-ab30-e2ebb2878017 | -18.60948 | -43.91022 | 2025-08-12 05:01:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| da544159-64e9-3898-9a7d-fe446fd3d0f7 | -17.6477 | -46.66792 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8226598-812c-3496-8b7e-c4fe9241a8f8 | -17.66253 | -46.68998 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c8afb0c7-4e8a-3d8e-b7cb-1648262deedc | -19.38715 | -48.89777 | 2025-08-12 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b2c47ac-ed40-3792-8615-9b6327dc5a70 | -16.29596 | -52.9164 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 22fc6a1f-fac7-3ea8-a0fc-6b98b6100dea | -17.65333 | -46.66868 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ecbfedf-a6d9-3c3e-8053-649441d53849 | -16.30396 | -52.91313 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2a810fce-ce7c-33e7-8b6c-aa72b79c3efc | -23.26945 | -51.99295 | 2025-08-12 05:01:00 | NOAA-21 | MANDAGUAÇU | PARANÁ | Brasil | 4114104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 30733d42-cc6f-3eef-a920-31dd57d40d34 | -16.5067 | -47.76823 | 2025-08-12 05:01:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9c2427b-52b0-30fc-b758-9a8f60915da1 | -16.29537 | -52.92069 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ca6225-583e-3191-974e-c3455552feb5 | -19.29617 | -48.43291 | 2025-08-12 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8239d650-f6b4-37ae-8286-d67b1c56597a | -16.29907 | -52.92125 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4074652c-72f3-3d4b-a8cc-c24403fc4016 | -16.28658 | -52.91235 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 23230859-64b3-3c31-bd84-a4fa70e5660c | -21.12006 | -48.8258 | 2025-08-12 05:01:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b8742e5-4edc-3751-82c1-5bd8ade256ca | -22.988 | -49.03029 | 2025-08-12 05:01:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa7b4ac4-8f57-3baa-81e0-b2fce82fa8c1 | -15.71342 | -56.39075 | 2025-08-12 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec2ad07-034e-3b5e-878d-7c3af646a12a | -18.63111 | -46.8343 | 2025-08-12 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d905f6f6-420b-3250-8760-9d5fae5c4195 | -17.6569 | -46.68924 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c8e54de3-ee44-3ac4-985f-4d820458bf48 | -16.30648 | -52.92244 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4dd07769-fe02-3d5a-851f-4c08912e2963 | -16.29461 | -52.909 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd10e7a2-5a67-31b8-bd73-d97870b21571 | -17.65814 | -46.67739 | 2025-08-12 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0887d0b5-58a2-3407-a3b0-b4fe280c0e4c | -16.31198 | -52.90978 | 2025-08-12 05:01:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README29.md)
