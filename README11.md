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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17af9ea2-e84e-3ce8-b39a-308c33494ee5 | -15.53498 | -45.69751 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f682e410-5f8f-318e-af1e-5ea6836ba101 | -19.17674 | -43.52596 | 2025-10-25 03:32:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87428a28-83b3-3290-9835-95c3e031dcc6 | -18.42056 | -43.28609 | 2025-10-25 03:32:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d96e3955-b7ca-3939-ab94-1038c52c7f36 | -14.15427 | -44.32047 | 2025-10-25 03:32:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| acb409da-2807-3b46-8900-c92fc23778e2 | -15.2457 | -47.92842 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd81270e-7ca5-3833-a0b4-6d969b358d01 | -12.04578 | -46.4123 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44523513-91c0-3ff8-bd88-5a524c302172 | -19.27823 | -43.29088 | 2025-10-25 03:32:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 48260967-7483-3304-9403-7316402d246b | -12.24993 | -47.44559 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83c70e14-e1c6-3bb9-be80-6bf428404473 | -17.37909 | -45.48618 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6c8201b-dced-3872-ba43-98404ad9963f | -14.93348 | -48.13607 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 45fa5709-b558-3f98-9587-53166ebd7c94 | -14.86506 | -48.08084 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 38b20239-d3f7-3e9c-94ee-6599f9a3f3ef | -19.86123 | -44.3074 | 2025-10-25 03:32:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09bbca2-24f0-3243-a560-3d5fd79a4e1a | -19.28067 | -43.2901 | 2025-10-25 03:32:00 | NOAA-21 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 61a39efc-f1d4-3f6b-ba5e-7200d50de2e0 | -16.2172 | -46.47396 | 2025-10-25 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2f4b403-c680-3f93-b47b-35198ce78935 | -15.57587 | -43.22413 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 833991cf-4779-3865-8802-10f96728c9cb | -12.48119 | -43.86291 | 2025-10-25 03:32:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0992254e-bc75-3761-9608-cbc64dd070c9 | -15.01827 | -46.20546 | 2025-10-25 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6795639-d286-36c7-8113-d8479c6143f7 | -15.20254 | -43.78572 | 2025-10-25 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3227fc0b-7e54-37ac-ba4c-af7e851a9036 | -16.17328 | -45.07975 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a231f633-3955-383d-8657-3d12df40a84a | -15.53398 | -45.70215 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd7364e9-cc7a-3092-b4ec-d25e4342f739 | -17.41893 | -46.88409 | 2025-10-25 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7906d95-8745-3f91-a8ad-d4b5a9b64c49 | -18.24792 | -44.19337 | 2025-10-25 03:32:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eb1a324-e4ce-3c88-a4e2-3cf749cfa573 | -14.75001 | -46.60327 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7147391d-92bd-34f8-9ee9-15530b5d490d | -12.25706 | -47.44676 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3b368d7-9f39-332f-8482-db5f04dbcb0c | -14.54364 | -48.0171 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d626dec-0eec-3490-ad85-8682849e3b88 | -14.93139 | -48.13459 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea6e9328-e85e-3b8b-a897-74be721b1b94 | -15.23198 | -47.92504 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce37af8b-3371-3783-b86c-b36716bfab6e | -12.46794 | -44.53648 | 2025-10-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdc514aa-e34b-3082-ae10-ad58a7b157de | -14.75064 | -46.6015 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7ab8ff6-85d0-3a34-9bcc-6c9d2a6c4163 | -12.05419 | -46.40551 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dfc1bcca-acac-30d1-9e80-2acf82f21bc0 | -14.98274 | -43.54812 | 2025-10-25 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 348ddf89-5119-3f08-9339-c3ddc22b5c28 | -19.63378 | -46.13196 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f23218e1-a850-315f-935c-ffebabbf9b54 | -15.52598 | -45.70993 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab27bcfd-2c80-37dc-b02a-72ab3bfdf4b7 | -14.92835 | -48.1261 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 89a6daf1-7f3d-3885-959d-b379ea1e5a4c | -15.23029 | -47.93245 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 242e4289-390e-3c44-9ec7-6630d1237365 | -12.29755 | -47.4648 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| faaa7ae4-deb5-3898-99d6-8de47ef0aef2 | -19.62809 | -46.13039 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 303d5e93-1794-3c9a-afaa-96b267aea3bd | -14.91996 | -48.13071 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fec42eae-6b8e-3372-999c-279b97db47e8 | -13.94551 | -43.81476 | 2025-10-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ad1ac26-f84d-3d47-b336-fa5762dacce0 | -17.41539 | -46.88428 | 2025-10-25 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57a82f1b-5975-3a74-b1a5-57b63ffef925 | -14.54761 | -48.02081 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efa4daf8-f3b3-36e8-958f-76669ecd4f1d | -13.94451 | -43.81399 | 2025-10-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9072d74f-c2c2-3f4d-bde1-20a5e3f1c9a7 | -15.22352 | -47.93035 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73e9c002-465f-34f9-95db-2ebf6e4b9ecf | -17.47411 | -46.00008 | 2025-10-25 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1887ca2-ce99-3fca-958f-d81a011935a6 | -14.74396 | -46.60004 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d327cc1f-0488-3955-ab0b-f16f9e4eeb90 | -13.64821 | -44.22994 | 2025-10-25 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a98d32c0-72f9-3f3a-bfbc-049c5223ce55 | -19.62718 | -46.13453 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ba23491-9cb8-355f-8360-c1b7a81b6235 | -15.98696 | -43.90263 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8524229c-ab94-385b-86b0-3d4ea7cc63e6 | -12.3026 | -47.46025 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5e3edc0f-038f-32fc-aaf9-d0fa0c47f780 | -14.20451 | -47.30484 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0213b3c5-b9ad-3de3-bc0c-5e8367d31f46 | -14.86324 | -48.08881 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5ec79469-a395-353d-9bdc-b633e3ed9391 | -15.24381 | -47.93965 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30a9a0a4-8c91-377d-a8e5-808a24a93dbd | -15.58299 | -43.21532 | 2025-10-25 03:32:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e44adff9-903d-330b-9ea5-0680d05d65a8 | -12.77407 | -47.3726 | 2025-10-25 03:32:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 424234b6-9db1-3b8f-bc2f-3e0fd7a91a3f | -17.36954 | -45.50209 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2568483-f13b-3016-8aff-3c015f378df3 | -12.05556 | -46.39896 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2073bb64-b35c-37e4-8020-ab7acf401f8b | -14.86999 | -48.10306 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6feac4be-38f0-3246-88fb-b8a03803828a | -12.06069 | -46.40784 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b3a25b4-e6f0-300a-9b38-2d34ea22bc13 | -16.21609 | -46.47915 | 2025-10-25 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f32ed057-1f7f-3e17-b707-59a4d70d7b17 | -19.62149 | -46.13296 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f06d50-86a0-3ab1-8872-3d37521a23d8 | -16.17241 | -45.08395 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4d4283e-9e76-31c9-8a70-7d5392139d25 | -12.25828 | -47.44108 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6532872b-e3e6-3930-9b22-4f8124a8f086 | -19.31802 | -42.28177 | 2025-10-25 03:32:00 | NOAA-21 | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93c67d83-e602-34cf-998c-77adf68e5299 | -14.93504 | -48.1291 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 493905e6-71e3-3b6f-ad1a-845bbecfb64f | -15.56458 | -45.94801 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9630a8b8-ab65-3054-acaf-a9bffa667ee8 | -14.86659 | -48.08518 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f6bbf712-a126-3d7f-a4ed-0dcfc935d6a7 | -17.36993 | -45.50121 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcd390b0-1036-3540-aa53-69afac906294 | -14.77193 | -43.08525 | 2025-10-25 03:32:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a64f1237-17bc-3371-8de3-c40136ccc1fb | -14.89215 | -47.86611 | 2025-10-25 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9fb1a8a8-50a9-3336-9511-29332f4ef0f2 | -14.15512 | -44.31638 | 2025-10-25 03:32:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54efee91-c2cb-3457-ad50-2d5210cefccb | -15.2371 | -47.93724 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 26c9f75d-b654-3c7c-98a1-eab9012c0ec1 | -13.64738 | -44.23399 | 2025-10-25 03:32:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37fba8a0-937e-353b-ac34-163856e5cdde | -15.98414 | -43.90559 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 53c0246e-a4e3-3349-b2cd-09236b11cac6 | -12.29945 | -47.45584 | 2025-10-25 03:32:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d02eb6df-a924-31a8-ad87-5a62d07be30e | -12.0836 | -46.41315 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c0c6f15e-76ab-3d39-aae0-935ee9fe3e5a | -14.87922 | -48.09451 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a69da709-d4e5-3146-981d-a0d7c9246bba | -14.87015 | -48.09076 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2dee5b3b-901e-3b02-8b2f-72692f11ac33 | -15.52697 | -45.70531 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87701937-e771-30d1-86f0-8d1082d4f57f | -14.93292 | -48.12791 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 491540df-97fd-3edd-9125-5164eb233a59 | -12.06394 | -46.39222 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be77768f-1c9b-3264-8f5c-619a6a81621f | -17.37327 | -45.48516 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1737b457-6f9a-3e73-951d-cd06d3afaf9d | -15.01197 | -46.20417 | 2025-10-25 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24ab0c29-15c1-3f1a-b22b-50ede32fda36 | -15.22489 | -47.92697 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8650075e-94d1-3641-9b3b-11685bd6d7a1 | -14.87374 | -48.07499 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 59050bef-8312-359a-8863-126e571a7a60 | -14.76672 | -43.0841 | 2025-10-25 03:32:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c9f7f0da-4342-380a-9975-2f9e4501df90 | -17.37051 | -45.4977 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93f0b5d8-d5e9-3b0b-9eff-1b04325c877e | -15.56445 | -45.9451 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c7da2a2-f758-33ba-be3f-4d6f172d39b8 | -19.63383 | -46.13313 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 709e3443-c5aa-3de7-be8d-cbc8434f898f | -16.21345 | -46.47755 | 2025-10-25 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 096c866d-4ef9-3b7a-ba37-75c5b08f920e | -13.54299 | -47.5693 | 2025-10-25 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f249b072-7b6f-30fc-b3ef-890fa9bcc5be | -14.92483 | -48.1418 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e127b449-d4e7-3547-ab0d-b8afdb38ec74 | -18.79048 | -48.0397 | 2025-10-25 03:32:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7aef1610-f861-3df5-9ca9-6b2ddbbff7f4 | -14.33759 | -43.73656 | 2025-10-25 03:32:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f17d04c1-08c7-3d93-90f4-630dc09a9ca7 | -16.17315 | -45.08101 | 2025-10-25 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f067504a-3fb4-3d9d-9136-e32d6b48c6cb | -12.46198 | -44.53524 | 2025-10-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f641c0-d8d5-3802-820a-aa60e82732bb | -15.23869 | -47.93004 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 977a835b-baf4-3b56-b762-8c99b750cd05 | -13.31434 | -42.42184 | 2025-10-25 03:32:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| fa9101f9-bcb5-38e3-8ba3-0a206d3e89ed | -19.85615 | -44.30612 | 2025-10-25 03:32:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a8ef33f-fa79-3f81-a14d-fc28475eaa79 | -15.23892 | -47.92637 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 556b9684-b547-39e2-ad4c-aafe62629114 | -13.45231 | -44.06894 | 2025-10-25 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README12.md)
