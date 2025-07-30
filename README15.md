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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bff063d-740e-3133-b0d1-7c455a3420a5 | -10.93576 | -45.78425 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e6e940e-4171-3bc8-9141-635c8e0f3f2d | -7.94654 | -44.08685 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d9d1034-d65b-3d3b-9791-67d8630a55cb | -4.30394 | -48.10131 | 2025-07-30 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0af4aa30-c6d4-3bbf-a2d4-bb7c2b4cc487 | -8.62306 | -45.88935 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf057c0f-e152-3d3c-9a52-d34073fbc04e | -7.78355 | -45.0014 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8e7728e-0cde-3002-aa9c-a60b7cea05f6 | -10.62463 | -45.2446 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19fd4e55-7952-3600-8d49-a032e5fe832f | -16.10839 | -47.91508 | 2025-07-30 04:04:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22382af5-70fb-3288-9a39-d7d9b71cf596 | -14.23137 | -43.96033 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ef66719-b914-3971-8e16-fd822cb03b5a | -18.66774 | -47.58198 | 2025-07-30 04:04:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| befc3a90-a105-37a0-8cb8-536d89bc9be3 | -12.9516 | -46.89769 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9da42b4-72e1-3457-99d8-57f9ddf4250a | -11.97498 | -46.68776 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c12d3817-c628-3e15-a779-c15ff81c3ff5 | -14.84545 | -49.28085 | 2025-07-30 04:04:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30127689-191c-378c-96dc-6d79bf84a88d | -14.76313 | -47.54459 | 2025-07-30 04:04:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49c71f73-5425-3276-baed-19ee3b23b6e7 | -17.87808 | -48.1053 | 2025-07-30 04:04:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a159fd3-b513-31e9-8fc1-de34f6b360cc | -14.23263 | -43.95267 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78989b1d-a9fa-37df-87b1-70c3c0298365 | -16.89008 | -49.07338 | 2025-07-30 04:04:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d28bc973-b32b-3ac7-badc-3f373624999b | -16.69407 | -41.00989 | 2025-07-30 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c59e0fa4-5a71-36ee-aff0-f521edcdee70 | -12.47881 | -47.27732 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25a6fa80-3796-3978-87fb-057f1f14d574 | -11.32681 | -48.91639 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 366c3b3c-7e49-3620-999e-9056f920f8af | -14.84618 | -49.27866 | 2025-07-30 04:04:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4da45cd-82f0-34bc-9615-43200053b3a8 | -16.21643 | -40.1356 | 2025-07-30 04:04:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6bc07db7-7ed6-345a-9841-e82e7abe500c | -11.32108 | -48.92065 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94ec2462-0e0b-32a6-b27c-56d9835986fa | -18.41128 | -44.19202 | 2025-07-30 04:04:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7253f8e7-4516-33e0-a8c8-a44c6c9ded20 | -12.82374 | -43.09237 | 2025-07-30 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6584b416-d4bd-30cb-9000-a703c850b172 | -11.99214 | -46.92598 | 2025-07-30 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6bbb4ff-127a-33a5-9b69-7e36871a8ad3 | -11.32426 | -48.92964 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e535b84-4482-31de-aed2-0053b38a99ad | -11.33974 | -51.25175 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03f36621-0f20-33ac-b9a9-c561b27e0c94 | -13.06979 | -47.3846 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a202083-d3a5-3ba0-94f0-9e1475837539 | -12.70506 | -47.79206 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9402433c-1210-36ef-b24b-27fff43081c0 | -17.4878 | -46.7406 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70d778d3-c2f0-376c-989d-07de5986d977 | -18.56744 | -44.42028 | 2025-07-30 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8a6ca48-39a1-30e1-add0-fb1947877ab5 | -11.34059 | -51.25402 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9eacd3c-aa3b-35ed-bbc0-f38c574a2c05 | -13.34079 | -40.04666 | 2025-07-30 04:04:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6434d876-d110-3932-96d1-41428f43da3a | -18.67363 | -47.04436 | 2025-07-30 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e898eb73-e6c0-3ae1-a8e7-922b61e192e3 | -19.10765 | -46.57563 | 2025-07-30 04:04:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5fe1875-7eb3-3b06-9b45-efc01d022086 | -11.32866 | -48.93283 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5e40fa8e-443e-3aeb-94c6-dad73dad40fc | -18.4119 | -44.18827 | 2025-07-30 04:04:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e1f0c84-ac40-3840-915a-8557d7f11543 | -15.41582 | -39.39668 | 2025-07-30 04:04:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d4fc584-8002-3eac-8ffd-170aae0433c7 | -11.34529 | -51.25284 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b453696-3308-390a-a268-ed25a79dfc0d | -13.39693 | -40.11956 | 2025-07-30 04:04:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d0726219-ff2f-3883-9c35-220eecb84828 | -13.41745 | -47.29177 | 2025-07-30 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3f705e0-71ad-324c-8471-f1c22f2cf38c | -14.46335 | -47.87073 | 2025-07-30 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b45e25e-ae12-379b-b8ed-360f8de450d2 | -18.17956 | -46.99428 | 2025-07-30 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fa9cd39-aa1e-3b49-a522-7f1b2885fa14 | -19.99455 | -42.22739 | 2025-07-30 04:04:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ea2d6093-9fc4-3393-8f09-c57a338f301f | -11.92222 | -44.54511 | 2025-07-30 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a4b3266-2d91-3e80-9733-1642cea9e961 | -17.04919 | -43.77487 | 2025-07-30 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1545424a-fa4c-377d-84f2-61c3c45c2ec5 | -12.81976 | -43.0955 | 2025-07-30 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95f253ba-8fac-3802-b45b-5254c37a3bfa | -14.45902 | -47.87057 | 2025-07-30 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df9c7874-55b4-322d-80f6-923b69080def | -12.81639 | -43.09494 | 2025-07-30 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc8c52dd-2fdb-361e-98b8-c670ee95057e | -11.92653 | -44.54152 | 2025-07-30 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 563cc92c-a966-3406-8f62-57310fa97ad0 | -12.54812 | -44.73209 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 543408df-0c56-34ef-a8e2-4140a982714b | -12.81677 | -45.44204 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6245b7f0-1e57-3ac8-8114-c8c721707a97 | -19.16927 | -44.11483 | 2025-07-30 04:04:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d3e5320-125e-3b2b-ab76-327b68b51866 | -13.54391 | -44.14316 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f53f5ea8-9e50-34a5-8e33-4015f7055594 | -12.19736 | -44.48953 | 2025-07-30 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b728eb1a-326f-3bbe-9741-53e483fd2fca | -14.74118 | -46.30701 | 2025-07-30 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e61ba5c-15a6-3469-8cd4-5e7c8fcaec12 | -13.06541 | -47.38495 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1160bdc1-0f59-38ba-a92d-1a1510c11e7e | -13.5321 | -45.64302 | 2025-07-30 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d91d50ab-cc51-3304-8abc-0b00a2a205dd | -17.48487 | -46.7352 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e5f0ce70-d2cb-30fa-a13b-ba8aa620055d | -15.84052 | -41.85225 | 2025-07-30 04:04:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8348c752-121b-3eaa-902d-74b03f57f096 | -19.74617 | -42.09912 | 2025-07-30 04:04:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 283c8c33-6345-3bd5-b24b-a1dd27f0204d | -14.74201 | -46.30219 | 2025-07-30 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba0e5d7d-92e1-3923-a85c-46246c68a842 | -12.61981 | -48.06457 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c25efb8c-3665-3af3-a7cd-23275fc748bc | -12.95505 | -46.90181 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65708f51-c77e-36b8-b95f-d240653fe602 | -12.95566 | -46.89835 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c454ae54-664d-34b9-adea-e15a6fd3537d | -18.66904 | -47.04834 | 2025-07-30 04:04:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 103635d3-1a2d-3d9a-be04-40ea4cae80a4 | -11.98651 | -46.69373 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbdec166-2be6-33a1-86ea-1486f2801dc3 | -14.91641 | -45.1452 | 2025-07-30 04:04:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecf70b62-27c6-3371-8fe6-5d09300eb982 | -11.99057 | -46.69448 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fc18a28-72f4-33db-9f8f-765df75bba23 | -17.04859 | -43.77855 | 2025-07-30 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96957e9b-d6a9-395a-a5e7-15115309a4d6 | -11.32205 | -48.9155 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ea93af-3e62-3b24-8ff8-06e232425df7 | -12.47462 | -47.27657 | 2025-07-30 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 509d5a5d-1a8e-3d1a-86a1-4ade16843f00 | -12.46466 | -44.08175 | 2025-07-30 04:04:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0df22f4e-2bd9-3b3b-9070-f5cf82e0b00a | -11.34129 | -51.25028 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f32259c-0134-3fa0-a028-89d93755a205 | -12.81699 | -43.09124 | 2025-07-30 04:04:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b617f3d-3311-3084-b80a-7e1f856eecb9 | -17.59501 | -43.19708 | 2025-07-30 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd0ba76e-96da-3cbb-a104-c64831b67d3e | -12.73194 | -47.00338 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4bcb279-063b-3e0a-bad4-b5936d50d731 | -11.98585 | -46.69743 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c9bc89-e543-370a-b116-da686d602721 | -11.32902 | -48.93058 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 19f91e6d-9cda-3198-bca9-7ad987a4937f | -13.08289 | -47.31174 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a50f876-90e9-3c75-b716-6d5f9f12e087 | -15.71516 | -41.93821 | 2025-07-30 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 70c0e931-ae6b-3cce-9b7a-27b0094f3004 | -11.34048 | -51.24802 | 2025-07-30 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de6e6175-9ff6-37ae-aee0-070216ba5f90 | -13.08911 | -47.30101 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e052bc8-b0af-3bfd-8b25-a4ca98cc7a0a | -11.32963 | -48.92763 | 2025-07-30 04:04:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fd72a392-5454-34f2-8cb5-9b9a373d3ceb | -12.81131 | -45.44302 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11855c7a-505b-3762-9298-586b970f5cc1 | -13.53349 | -45.65745 | 2025-07-30 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81a44551-8ebe-308d-bc24-874e91c32c31 | -13.53505 | -45.64827 | 2025-07-30 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 520697e4-f942-3eee-8031-8e7c24094094 | -17.49237 | -46.7366 | 2025-07-30 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9b2a8b8d-1bd1-3e04-b4ae-b014550f5e0c | -11.98179 | -46.69669 | 2025-07-30 04:04:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e12a9bfb-e7c9-31a6-962e-76b7e8a05e57 | -14.22081 | -43.93882 | 2025-07-30 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5db3181a-c5b8-37bc-b678-dec3e29cf1b1 | -12.82049 | -45.44267 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b688981b-9e25-3b8a-9b88-ca8f7699c95a | -15.49681 | -45.92678 | 2025-07-30 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1c68809-1a17-3a1c-8f9f-45505ba7f17d | -13.98906 | -44.63287 | 2025-07-30 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9530f12-de1d-3357-8cd1-aec09feeec9b | -11.92293 | -44.5409 | 2025-07-30 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5af5f953-3e64-36a1-8d6a-eb2a62f873eb | -12.81876 | -45.4443 | 2025-07-30 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3ff78d6-0fe4-3524-b872-d732b4d64233 | -13.08848 | -47.30448 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a86ed72c-91ba-347c-9888-6ebc014835b9 | -13.08426 | -47.328 | 2025-07-30 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2c35659-da8f-33e1-91ee-a73d08013034 | -16.83012 | -49.24715 | 2025-07-30 04:04:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 721e3b4b-c230-3962-a1c4-09cba3113895 | -15.98605 | -42.25058 | 2025-07-30 04:04:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d7840812-795a-3e8f-9c90-d7eef9ffe0d9 | -14.74078 | -46.30437 | 2025-07-30 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README16.md)
