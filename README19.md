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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33965895-55aa-35f1-9b83-e25fe039179e | -4.36892 | -47.77276 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55f42a88-1583-3103-9b8a-599bb04f9514 | 2.5215 | -60.64804 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab7825d8-afd7-3860-a6f5-f5157b9cb5fd | -3.90638 | -54.57808 | 2026-08-07 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5e9288f-ca1a-3b6e-a8f2-3323ef56f3e8 | -4.26783 | -48.19507 | 2026-08-07 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd6039bf-a658-3553-bf30-ea1485cf4a02 | -6.13243 | -47.17765 | 2026-08-07 05:01:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7b323eb3-6308-3165-9c34-a4e35725a85e | -4.13983 | -59.49843 | 2026-08-07 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9bd05ef-71ef-3578-8581-7cc8bde2b6ff | -4.27627 | -48.1963 | 2026-08-07 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 633474c5-656b-334c-a0f2-167bf422d99a | -3.02791 | -54.52464 | 2026-08-07 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3484eb1-7620-3bdf-af39-a237b60470f3 | 1.93752 | -60.84723 | 2026-08-07 05:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df3d3845-37a7-30cf-8b2f-98fa22d2ef70 | -4.48641 | -49.82167 | 2026-08-07 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d369717f-67bd-3e74-ba1b-3b11021ebd81 | 1.94302 | -60.84933 | 2026-08-07 05:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a18e1dcc-3d56-3dd5-b9a5-1aad0113abad | -4.13652 | -59.49762 | 2026-08-07 05:01:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f515818-1199-3afa-9882-a7e9cfd45c35 | -6.98458 | -42.91469 | 2026-08-07 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1397773-a13a-3dbe-b8fe-00ea245403e4 | -2.81667 | -52.29047 | 2026-08-07 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87935b2c-aba1-3355-8c94-c71a82035288 | -6.98728 | -42.91319 | 2026-08-07 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5eee6a05-460a-31ad-b846-b68509862a8b | -5.42719 | -43.43161 | 2026-08-07 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a00516f-77ec-3376-9362-3dd82a558b77 | -2.48076 | -49.32286 | 2026-08-07 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb1b441a-6c12-3e96-95ca-9752a84cfc0a | -6.91559 | -41.94679 | 2026-08-07 05:01:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50b4ccf3-a742-3be3-bb3e-be27267550f1 | -1.52222 | -54.67906 | 2026-08-07 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5c64a8e-fe06-3cd8-ab58-281d7a756c06 | -2.08912 | -54.44502 | 2026-08-07 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2655a4bc-2395-3fd0-967e-21e6a18123fe | -2.48002 | -49.32754 | 2026-08-07 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe29ebe6-3193-36e2-8408-b4c6eaf29d23 | -2.69034 | -47.35837 | 2026-08-07 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 025ebbcb-353a-3086-962d-b9468edc83e3 | -6.98795 | -42.90834 | 2026-08-07 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a16a5153-6432-3899-9ea6-f00db347c246 | -3.53311 | -54.49 | 2026-08-07 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e6cc677-9c16-328f-aea5-88aed785ada9 | -3.95691 | -43.10861 | 2026-08-07 05:01:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f3f10aa-ff00-3c6a-a238-3f6b4c63ffdf | -6.47954 | -42.22564 | 2026-08-07 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2feddf3f-8168-3799-bfe2-a2eab086bded | -3.1761 | -49.53165 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12413bda-ed8b-37cc-82a3-15694eaeb551 | 1.02697 | -60.39085 | 2026-08-07 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b61b57f-ebab-35ed-80dd-230e71c73af2 | -3.59577 | -49.07301 | 2026-08-07 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c4f929-26ac-34d6-b2bd-93b26820e53b | -4.36518 | -47.76794 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b01cff3-72d1-3b8b-8955-c82f40bf6596 | -6.13313 | -47.17284 | 2026-08-07 05:01:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57fdf209-9deb-3e57-b8b9-82ac707527ae | -3.26465 | -49.53304 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9176c430-0c91-326b-acd6-f016417529e7 | -4.29941 | -47.57365 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22b3a052-c13c-3629-9ef9-e910d2c5c66b | -4.27265 | -48.19178 | 2026-08-07 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1946d4e0-71e8-39a8-ac98-8b56a3f349e6 | -2.50522 | -51.81278 | 2026-08-07 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28e855fe-88f0-3a7a-9ff0-839a3b984359 | -4.84413 | -45.22159 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa4175f-d89c-3eb3-84c2-140be2c9e753 | -5.42349 | -43.43305 | 2026-08-07 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53785394-f83a-355d-aa00-7673181cef6e | -2.6936 | -47.36035 | 2026-08-07 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adb2d92a-ce2e-3991-98f7-7e18fa505295 | 2.52193 | -60.65095 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5695414-10e9-3ed4-b019-df268603c5f4 | -4.84461 | -45.21839 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef781691-cea3-3d58-b279-bca2224bfecf | -6.06974 | -49.48563 | 2026-08-07 05:01:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b7488987-33e9-3db1-a41d-9fcb55c8d458 | -4.45979 | -47.9195 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b358bd77-b35c-3a92-a367-262766d8dbee | -3.96284 | -43.10949 | 2026-08-07 05:01:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8057fbdd-2035-3132-948a-f52f2ade63e8 | -5.42412 | -43.4287 | 2026-08-07 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9ca0a63-7b1b-3fb9-adbf-7dade84d5b10 | -2.4762 | -49.32695 | 2026-08-07 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65028c85-e4b0-3c30-91f1-1aace7497590 | 2.52249 | -60.64964 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc1064c-3400-3f82-9c22-afebd4ca6a24 | -2.41923 | -48.63585 | 2026-08-07 05:01:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6db100a2-e79e-3ad5-9479-cd1b2834223c | -2.79823 | -48.57618 | 2026-08-07 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb52572-6289-3800-97c4-554f628b989e | -2.71675 | -54.62289 | 2026-08-07 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac8fb31d-2637-3047-83ab-2d4dbbf6bb42 | -6.91333 | -41.94443 | 2026-08-07 05:01:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5dd315d2-8c6a-359d-8c7e-e49c8f6c7eda | -5.42779 | -43.42723 | 2026-08-07 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c64fd45e-1e76-32a4-9326-bb92a921e87c | -4.84531 | -45.2181 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b114355-81d2-3c47-9dd2-d7ef207ba9a4 | -7.07669 | -42.26586 | 2026-08-07 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| db10d910-dde7-3a66-a68b-e65968a32a3c | -2.69406 | -47.36326 | 2026-08-07 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88036bda-f60b-33e7-becc-84966d4cfbf5 | 2.52158 | -60.64384 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0813665e-fdf8-3316-8304-25a6c44c2835 | -3.09824 | -49.35879 | 2026-08-07 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b42a8b9-a340-3476-825a-8f5c178509ba | -3.02736 | -54.52814 | 2026-08-07 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f9b6ba1-a9ae-3f99-bbbf-6fdc4cb83ec0 | -4.46039 | -47.91542 | 2026-08-07 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bccca255-2433-3cf5-b0b7-1d268806f59d | 2.51699 | -60.64748 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bed61b9-2e5b-3855-a135-72b7e6140d69 | -2.69294 | -47.36456 | 2026-08-07 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 337a45be-2347-3dde-b74e-f00cc13622e5 | -3.51226 | -48.88755 | 2026-08-07 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91208379-00ee-3956-a566-0866b0f9effa | -4.84576 | -45.21493 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4a29c36-2872-3f11-9c65-d2be3540dbdb | -3.40031 | -49.78289 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 137a93ad-24ce-3cab-92f2-fdde1facb7bc | -3.26535 | -49.52847 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4c9594e-f7f0-3211-9b61-e8e831607f89 | -6.13709 | -47.17825 | 2026-08-07 05:01:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 74804687-4488-34e0-907d-c2195a83f895 | -2.46941 | -54.68148 | 2026-08-07 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6a38d5d-d7ba-3987-bf3d-7400ae845328 | -4.4852 | -49.82382 | 2026-08-07 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de989367-ecba-380a-a9b5-a8e9f78f299c | -1.46566 | -53.59698 | 2026-08-07 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19e60c12-de21-38d6-bfaa-7c27208f33f7 | -2.87008 | -50.4723 | 2026-08-07 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb73986-4585-3b18-bb19-88ab33eb96a3 | -4.84508 | -45.21521 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db76183a-7c44-3f99-8024-eccbe479f837 | -6.98522 | -42.90983 | 2026-08-07 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17a5ed09-92f3-3e7d-85a8-a94b632b701d | 1.93796 | -60.85017 | 2026-08-07 05:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5493fc1f-7bb0-3355-9a49-b6b96d6db7a2 | -6.06899 | -49.49079 | 2026-08-07 05:01:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d589a08e-faf4-3dfa-a59b-c21d466dab7e | -4.05692 | -56.33304 | 2026-08-07 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48aaadb5-1e88-3d4c-a7e4-5fe72e836fc2 | 0.9414 | -60.40673 | 2026-08-07 05:01:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2c7a6db-9963-3db5-9eba-83c2d7ad73a6 | 1.94258 | -60.84641 | 2026-08-07 05:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5b0b84c-b503-3a5c-a750-a7d4277f454a | -4.26843 | -48.19116 | 2026-08-07 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c9e3098-6994-3d10-8bcb-6e433ee3bd1d | -3.02787 | -48.41108 | 2026-08-07 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90670258-bafb-3597-845f-7a697f1a0b18 | -7.07743 | -42.26047 | 2026-08-07 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc5928f0-94e8-3667-a391-70dcc09ace7b | -6.99149 | -42.91062 | 2026-08-07 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de5516bf-8f33-3863-af82-2eebcefa844e | -2.08968 | -54.44152 | 2026-08-07 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7a51809-ef49-3cfd-a72f-46c33d834b65 | -6.91924 | -41.95084 | 2026-08-07 05:01:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 19c01ab9-5493-3612-87bf-e9aee1f55f42 | -4.91281 | -49.23953 | 2026-08-07 05:01:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47e842b4-9a25-3c6c-b0ee-363d24a12c87 | -2.67447 | -54.29035 | 2026-08-07 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd299aeb-0fdb-36c1-9590-27a18e860c5b | -3.40107 | -49.78078 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56c56cc7-781c-38a1-8c6b-ab068cfd92b9 | -3.15445 | -54.60541 | 2026-08-07 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c541fc-d77a-38a4-978e-8ca8d300dcae | -2.6947 | -47.35903 | 2026-08-07 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e89b74df-d213-33ad-9087-2b5d9515e73c | -2.08634 | -54.44099 | 2026-08-07 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 431a4970-b644-34ae-b520-22a559ca5945 | -7.07592 | -42.26692 | 2026-08-07 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ece4d8dd-6aff-30d6-b075-2c7194de6350 | -5.02953 | -56.19347 | 2026-08-07 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4f559ed-6c22-3b1e-b152-d01443b57241 | -3.12163 | -48.58643 | 2026-08-07 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 859fc7fd-455c-3116-b0fd-9d24896c4e73 | -2.46606 | -54.68096 | 2026-08-07 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b2ff4e5-19ca-309e-aa79-e72e6080adfa | 2.52294 | -60.65255 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4b51f7-e85a-3ea3-832b-efdd4aa327d0 | -7.07662 | -42.26155 | 2026-08-07 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4176491f-6f6f-3068-b29f-ccca3d9e950b | -6.92148 | -41.95311 | 2026-08-07 05:01:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 77a916de-8072-3952-b09d-c486fdb31b47 | -3.16289 | -52.18347 | 2026-08-07 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab827d1d-fe87-3acb-a281-0aae1c3c1cc4 | -3.40102 | -49.77832 | 2026-08-07 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81bcfa90-9f87-3f7d-aac8-f7fe1e00a263 | -4.84486 | -45.22129 | 2026-08-07 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d2d8074-57fa-3be7-9705-1cc0416ef7b9 | -2.94573 | -50.3177 | 2026-08-07 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7008805f-1b07-3680-bf04-f31a93b29bbf | 2.52204 | -60.64674 | 2026-08-07 05:01:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
