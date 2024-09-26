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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3757eda2-0bc2-38a7-b8b5-43f24d9d9c1e | -22.28601 | -44.05486 | 2024-09-26 05:01:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9d1e8366-1107-33e4-83c5-7025e6ed3cda | -22.74498 | -44.7915 | 2024-09-26 05:01:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5628ffd8-4cc6-3efe-a29f-542e618f0039 | -22.73976 | -44.7885 | 2024-09-26 05:01:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 243c312e-36b4-311a-89e0-97413efa702d | -22.73855 | -44.78867 | 2024-09-26 05:01:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3e161b34-dcda-3936-998d-282416b17d77 | -19.59712 | -44.9273 | 2024-09-26 05:01:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92a299af-1391-34f9-af2b-e51f6935e472 | -18.4339 | -45.09847 | 2024-09-26 05:01:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a664235-99e9-30b4-992c-2e1318b98674 | -18.42774 | -45.09757 | 2024-09-26 05:01:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83e7178d-91dd-3d4c-bb10-9780e440b63d | -20.54221 | -46.36824 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98b44ee2-45a2-3348-907b-d76dbd608371 | -20.54183 | -46.37212 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b385317f-3259-3678-a793-3cb93cba0813 | -20.54149 | -46.36855 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebcd7070-d0fe-36b4-b931-4c58ec18435f | -20.54147 | -46.37585 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb2fb874-13a8-3c2d-ac2e-e2c75cb10a5c | -20.54114 | -46.37245 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f91b8ca-138b-3f63-9283-00bd9c8d4c9c | -20.5408 | -46.37622 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1adc42d6-61a8-34f2-b5b4-061dcac9dfd2 | -20.53596 | -46.37169 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fc3a03d-0c53-33d0-abc5-64ab0b20cec2 | -20.43011 | -46.24931 | 2024-09-26 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c874deb-c256-370c-b50d-526ab1eacb6e | -20.42886 | -46.24554 | 2024-09-26 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f7be92c-26e1-3155-aeaf-233d3b152619 | -20.42846 | -46.25009 | 2024-09-26 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eac016b8-c240-3a13-9876-13be7644f36a | -20.42423 | -46.24855 | 2024-09-26 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90ee349c-d4fb-3c10-b032-284354f59c97 | -20.4199 | -45.90551 | 2024-09-26 05:01:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7df91ba6-cd4b-3d9b-ac0e-efc5f1560f8c | -20.34237 | -46.16541 | 2024-09-26 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7d59566-2be0-3375-9876-1f5985204b50 | -20.15648 | -46.58991 | 2024-09-26 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e87cb5c-3cb1-36d9-8846-ae963e00d11c | -20.15607 | -46.59419 | 2024-09-26 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dea03f3-2987-3834-92ba-de63ba654a89 | -21.20881 | -45.75528 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e505ed4-af6e-34f3-8bf8-730494c36bba | -21.20833 | -45.75591 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7809175f-815b-3ea2-a4f5-72185d33978f | -21.20229 | -45.75952 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b103f509-5b16-3c9f-acbc-94691e3ea517 | -21.20179 | -45.76 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b37f8129-9a0d-39f9-bcf3-dcd327924971 | -21.20847 | -45.75943 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 270e3d39-06bc-327b-8c33-c4f2549f8962 | -21.20812 | -45.76363 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| cb4cd94f-9d5d-3683-acca-753d8d0f9e60 | -21.20797 | -45.76 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e7661048-1e44-3b1f-87c4-c294dcdf6f57 | -21.20759 | -45.7642 | 2024-09-26 05:01:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 81307e5b-a611-3f55-bc80-a38de84c693c | -23.56858 | -46.0506 | 2024-09-26 05:01:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e648ea5-0cb2-3863-b181-e0a3eb5184df | -23.56243 | -46.04976 | 2024-09-26 05:01:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 63c85723-7d90-3166-99bf-7dfd5a420c6b | -23.5304 | -45.91264 | 2024-09-26 05:01:00 | NOAA-21 | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| de59a47f-a80f-3498-91b9-4c8b650ae45a | -23.35766 | -46.28724 | 2024-09-26 05:01:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0d992d10-8024-3ae0-a9a9-74fe4901d9e2 | -23.17538 | -46.33234 | 2024-09-26 05:01:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c89ed3b0-0491-3201-a8d7-fccd17c4e9a7 | -23.17004 | -46.32269 | 2024-09-26 05:01:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fee85a36-0c56-3ca6-a02e-b902154d5c06 | -22.72701 | -45.73532 | 2024-09-26 05:01:00 | NOAA-21 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 27bfd698-1e34-3553-8b66-4958977fdc3d | -17.89371 | -47.03125 | 2024-09-26 05:01:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a544e4a6-6594-37c7-a3e9-e45f99032d12 | -17.89333 | -47.03485 | 2024-09-26 05:01:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c2daecd-f551-3a4e-84ba-117d4e89dfe1 | -17.41745 | -46.77815 | 2024-09-26 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63aa2121-fd1b-336f-aea9-840a32db9471 | -17.41721 | -46.77801 | 2024-09-26 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57fba180-5872-3dbf-8028-a0cc2eb59b12 | -17.41707 | -46.78185 | 2024-09-26 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a92c1621-b146-314a-a3bd-39b3dfd2d378 | -17.41681 | -46.7817 | 2024-09-26 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7285b82-bc77-30cd-8682-a8eb4c697600 | -17.23815 | -46.28696 | 2024-09-26 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 226238e7-2429-33ee-a8d2-371ded2a98df | -17.23555 | -46.28508 | 2024-09-26 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fbd16e6-6686-3821-a5cb-f94ceaa909ef | -19.27623 | -46.51211 | 2024-09-26 05:01:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e45bd1-054b-321d-9f79-4681b84fe5a6 | -19.07134 | -47.28695 | 2024-09-26 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb5decf3-b80c-3b08-ac5f-2d449344881f | -19.0414 | -46.80284 | 2024-09-26 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 549361b1-56f1-35ed-85e9-1ace14e176bd | -18.573 | -47.23344 | 2024-09-26 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c639330c-80c2-3785-bb3d-8b73561a52d9 | -18.51385 | -47.09601 | 2024-09-26 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b08f4b8-1e0e-391e-ab24-8d65e94b736e | -18.51346 | -47.09974 | 2024-09-26 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3eb61529-c152-3a29-bbbb-a56da1ee9b40 | -18.50765 | -47.10242 | 2024-09-26 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec5c11d7-b206-3a28-8d39-b48d3ccba4bb | -18.50726 | -47.10614 | 2024-09-26 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ab3c9572-ee76-3dd3-a636-cb95bd32b432 | -20.82658 | -47.21444 | 2024-09-26 05:01:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1404fac-6ea4-3f31-8705-485b70227fd6 | -19.98949 | -47.15429 | 2024-09-26 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43104629-4f4f-3adc-8595-6a9745bd40ad | -19.87641 | -46.88105 | 2024-09-26 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7496b9a-eb3d-3af1-a152-24813c510e92 | -19.87604 | -46.88493 | 2024-09-26 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a7bb911-295c-3062-9e42-b3cada2cdf4b | -19.75867 | -48.01115 | 2024-09-26 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6bb87dc-fbca-326e-ac20-bcf48421c14e | -19.75379 | -48.00703 | 2024-09-26 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e20eba9-614f-361d-9f1a-2b484395d491 | -19.75345 | -48.0104 | 2024-09-26 05:01:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6f7318b-8092-33a8-ad57-766b4a7034a2 | -19.54792 | -47.21181 | 2024-09-26 05:01:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce0859b7-61c9-3a3c-8825-a3cdab6e2899 | -21.93806 | -48.55694 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 06613a8b-672d-3bce-8887-57f1fbbf2a91 | -21.93774 | -48.56015 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e39512ac-aba2-3f9c-b978-30ccc1ae2e26 | -21.93319 | -48.55304 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7e81266-e747-3ba3-b924-d428c87f3228 | -21.93287 | -48.55636 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cacae26e-747c-3db0-a947-b9270743b40c | -21.93255 | -48.55966 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c30bc9db-7057-37a0-afeb-7a5aa6909082 | -21.92769 | -48.55567 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ed515a3-3322-31a2-84ea-bc18d94166b7 | -21.92736 | -48.55905 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67e458ce-e7f1-359c-aba5-1202757a0b06 | -22.3711 | -47.63931 | 2024-09-26 05:01:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 00e94358-3d18-31b4-8e46-8d916608a3f3 | -22.36555 | -47.63899 | 2024-09-26 05:01:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da8e3f28-4355-3cb1-8a2b-1cb36280634b | -22.36519 | -47.64284 | 2024-09-26 05:01:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a0af75e-d4d7-3539-89de-3a91595ce185 | -22.36001 | -47.63847 | 2024-09-26 05:01:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1370989-fb59-365b-8f95-51654352351d | -22.35839 | -47.77615 | 2024-09-26 05:01:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05deae7b-3c68-3c18-a5b3-89c9a66aa742 | -22.35807 | -47.77958 | 2024-09-26 05:01:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e2ecd93-267c-398f-a22e-3ae9eea4e930 | -22.35311 | -47.77345 | 2024-09-26 05:01:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4c570bb-af0a-3aaa-8acf-7e4569c5838b | -22.35281 | -47.77665 | 2024-09-26 05:01:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51de5cce-cbcd-3e30-9a24-6bfb95b5bf7f | -22.34922 | -47.75563 | 2024-09-26 05:01:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc208c60-8409-33bf-92c5-29c0ba2a9752 | -22.34875 | -47.76077 | 2024-09-26 05:01:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 876bb835-3b59-3dda-8920-da74732c5269 | -22.34331 | -47.75963 | 2024-09-26 05:01:00 | NOAA-21 | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5688ad1d-d011-3658-bcf2-5fc13a6fc66e | -22.23138 | -47.57909 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8377377-32e2-338f-8063-daab9961f944 | -22.22657 | -47.57571 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a398523-8267-3fab-ac6f-52bfdf9abe4f | -22.22622 | -47.57935 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7b37d0ce-151e-3655-9a13-81f1752bcf4f | -22.22615 | -47.57511 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 041470dc-da16-31de-8f6f-6ee74ddc2c54 | -22.22582 | -47.57877 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4227b193-f24c-3f82-a894-0119e43c209e | -22.22165 | -47.5629 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 55a889b6-59c5-3bf4-a184-535ae8c9fdd8 | -22.22129 | -47.56692 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 532feca4-7ff1-323c-b223-575b0e6a30d9 | -22.21694 | -47.55943 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 400d5820-0c9e-30bd-b87a-d5da93de01e0 | -22.21657 | -47.56327 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 8fd5eac3-e313-3ab6-9fa0-b7d4b5669d5c | -22.21642 | -47.55875 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| b513aa52-f53a-3f7f-bd1d-5f67df1946c5 | -22.2162 | -47.56715 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| b06446c7-a7ce-3eaa-81e1-fffaf457a5b6 | -22.21607 | -47.56258 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| c13463c5-6371-31b0-8f9c-e2c6337805d7 | -22.21583 | -47.57106 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 8a83d235-6494-3a2b-91a4-8556b0f90d53 | -22.21573 | -47.56646 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 1ae2de7b-cf12-3d3e-9e1f-f3305bd32566 | -22.21538 | -47.57037 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| e5b1862d-d0a4-352e-be56-397d35d168a5 | -22.21137 | -47.55913 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 7c45105f-52be-39a1-a945-2488690ea117 | -22.21101 | -47.5629 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 13bef4df-fa6a-36b2-80ff-5345d9538fd6 | -22.21085 | -47.55841 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 0b9f03c3-a900-348c-aca7-94ea8b5539a3 | -22.21065 | -47.56666 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 974195d0-eb87-3d09-b870-f703f50294d8 | -22.21051 | -47.56218 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 0705a4de-9f53-3f65-af67-85e2b59147e2 | -22.21018 | -47.56595 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |


[Clique aqui para ver as próximas entradas](README143.md)
