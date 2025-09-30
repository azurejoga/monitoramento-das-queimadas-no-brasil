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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56f5ce82-cb71-3399-a84d-99622856aa35 | -12.79495 | -46.89451 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e66f6db5-ce0b-3e5e-9d78-f2e5e5cd89d0 | -15.8542 | -46.23925 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 517d2e55-bbf5-3fc9-81d4-4df8ace474ff | -14.58875 | -48.16827 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 650e4371-ee5a-346b-841b-c7320b2af097 | -6.03457 | -43.81562 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dda9815-e7d5-3c2c-81fe-491ac25e9e4b | -6.50837 | -45.21591 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef00877-3ba0-3ef5-9545-d7a36489d845 | -14.38431 | -47.14606 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68171936-407d-34a5-8b21-91d6d49249f9 | -17.09766 | -48.56853 | 2025-09-30 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb61ffa-5a4f-33ed-83f0-ae653d6b475d | -13.84052 | -47.48696 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41871b0c-dbbf-3681-8f8f-0e7d6f8103c1 | -13.21533 | -50.94956 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4737b2c4-a197-3d9b-bd36-1cab67618f41 | -6.55458 | -43.41916 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 67e813cd-c2d2-3e59-a4a3-4d71360354e2 | -6.36884 | -45.64341 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58fefed2-ec67-3271-af3b-bc34407bdb1e | -11.87568 | -48.05797 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 464376f1-22a1-320d-bc35-c351648efc62 | -13.80734 | -47.48869 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a7e0356-4774-33a3-88c8-e002255f3848 | -14.54133 | -48.48687 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73739dad-4779-37d6-af2d-ae1c76303309 | -16.41017 | -47.04496 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e54576c-03b5-326c-b679-a2a30597bf1d | -15.33384 | -40.06273 | 2025-09-30 03:49:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e4acce9-6b3c-3efd-8ba2-58a6b83ba3cf | -15.2697 | -47.88707 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc8e86c3-bda2-376d-8534-68e375851825 | -12.84385 | -47.01052 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65788392-a6c4-3534-a2fc-98b14a48408c | -14.68712 | -48.13521 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd18ff36-c7a6-3542-9001-375fece50b65 | -15.24999 | -49.72308 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 014055b2-99d2-3405-b268-d899454c87d7 | -12.89711 | -46.76406 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b83d9e7b-08c5-3893-af38-1c053ebda45c | -11.20077 | -47.21428 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 695a9510-d831-338f-a747-4686f7ca8f35 | -11.05835 | -47.83214 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79eb7db1-aaf1-3870-a646-d319b8c852cf | -14.52908 | -48.37926 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3512aee8-0028-3b9f-a66b-17c35b9ab3c0 | -11.19003 | -47.24125 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12f75d37-f699-3182-be52-a31e84324d8f | -12.83417 | -46.99534 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 641982ad-c249-3e33-9a32-8cd368aa907f | -12.85372 | -46.98727 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb9307e-401c-31e3-b363-8766e78fa594 | -13.38347 | -48.06109 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a42f1594-edf3-314f-b0bd-5f98de57c0ca | -14.50941 | -48.41704 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdfa3402-d1da-3489-bcb7-f3e994a7b1bd | -12.74698 | -46.85546 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf594f6-0778-30e7-9744-28324ac1d432 | -6.08266 | -42.47116 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 596cad00-a362-3f7b-a2fe-9c20e7202881 | -13.59715 | -48.04289 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a2e9880-e812-3ecb-954c-2a4fd66ac592 | -13.84879 | -47.49981 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af858f45-65d9-3cc3-b886-329fc02e310a | -15.23383 | -50.09504 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 556aa553-fcfa-3c5f-b227-f295304721e4 | -5.87915 | -48.11967 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f9c11414-5d5f-39bc-a8b7-b4c439a28ea6 | -13.8154 | -47.47735 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a97ff2-7236-3470-8a14-1998a1038b05 | -13.5248 | -42.60661 | 2025-09-30 03:49:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1cdce24c-e51c-3d15-964a-ab9feffae1fe | -15.419 | -48.24715 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa32c368-d13a-3d3b-924e-9a62cbab56aa | -17.71597 | -46.66955 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6ac2997-60d0-3833-ace2-bdf920f45641 | -17.75648 | -51.34171 | 2025-09-30 03:49:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a836288-8a77-3df5-a03d-c6a61b15a4d6 | -13.17068 | -40.24273 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 092254e9-6f37-3bdc-96cf-c602b8fcf6aa | -11.05998 | -47.82381 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 67e1faa3-62f5-344d-9223-4d67669276f6 | -6.42619 | -43.07709 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0b7165d1-4da9-390d-bb8a-6fe1e73b9e6c | -16.8384 | -48.90243 | 2025-09-30 03:49:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b783c02f-e0d4-36c9-8c7e-e80332fcdb63 | -5.73257 | -42.82758 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 053d7c9c-c690-3265-b08e-e17c6b30e5fd | -6.42963 | -40.62047 | 2025-09-30 03:49:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ca2b2f5-cf79-3258-95f0-b33e7a31aeb6 | -19.42177 | -44.17747 | 2025-09-30 03:49:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35438657-3ba5-3850-a212-56f24bf4ca3f | -14.70777 | -45.70418 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fce67e88-8004-3b11-bf29-ff46d6349934 | -13.80976 | -47.94866 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aa9d494-1c36-3131-ae49-360aa04e4522 | -6.04822 | -43.60623 | 2025-09-30 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50b97352-8417-3282-9c16-181424a7dbaa | -5.92612 | -42.91116 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ada68db-1913-3d5c-9d54-979ed69c7ac5 | -7.01575 | -44.47412 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a771c80-6843-38f8-8167-f243a4dbf1ea | -15.47435 | -43.23732 | 2025-09-30 03:49:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2d6f548-fb1d-3e94-a7b6-59197a2ccc56 | -12.01712 | -46.61974 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff33bee4-690b-3e24-8958-7da226f90216 | -14.52114 | -48.44604 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 89cc3966-f7cc-37ad-8cf8-23d212fcc6ef | -13.58405 | -48.05232 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb0e0216-4a18-3277-a371-6b3b47241abb | -12.7962 | -46.888 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e58e3ffe-d0cc-394e-9fbf-c9ceb7a394b9 | -7.30241 | -42.84681 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6972d8a9-8df2-35e9-a8e5-9b2d60b50700 | -13.35297 | -47.81252 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 693cedeb-6616-3d2f-b9fa-a1f861989e17 | -15.05218 | -40.78889 | 2025-09-30 03:49:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b1babd2f-de55-311a-a545-6acc940bdba5 | -6.05256 | -44.18966 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3c385c0-dc73-3c34-9e33-5e8ace1a0e41 | -15.78612 | -43.66167 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a64fc1b-65e5-3e3c-a2be-d78eed2270da | -5.52517 | -43.88221 | 2025-09-30 03:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 95829843-d109-3905-a73d-bb4d7a294dee | -14.7286 | -45.66949 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a107cd19-7bf8-3281-862c-370777254db1 | -7.55957 | -42.4082 | 2025-09-30 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6a9b35d-4496-35a7-980d-5f5ffeb7a03a | -17.40695 | -47.12874 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f82ceb3f-0ebd-3bf5-8f41-a4d33866bf37 | -18.01653 | -44.37452 | 2025-09-30 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1415c24-9a89-3981-9c86-298e3bcc7fda | -15.11971 | -46.45918 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 870a09fa-3b79-3f1b-a83b-e5af4acd2976 | -6.10251 | -42.66689 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 909a25cb-29b6-3c2b-8bf6-23c46f8585d3 | -15.1264 | -48.3856 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66f66a3d-777d-3ee0-a682-7d3fd9644c12 | -15.71896 | -47.59118 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 34540f86-2050-3a91-8750-d91b8038f975 | -11.21751 | -47.21392 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a94d91a-1cd4-31ec-83f7-6fa212e16b2a | -6.87376 | -45.09753 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf9dc5fb-033f-3b3d-82e9-70c04ec847da | -13.41779 | -48.20232 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 493b355f-d894-3902-baa3-2fa837abc962 | -18.47668 | -44.02361 | 2025-09-30 03:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6e78a5f-2d83-36fc-b98a-fc24b7aa0b14 | -11.19406 | -47.22026 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5f63cf-4e16-3f22-938a-d3b64a4beff3 | -13.59116 | -48.05074 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ceea2314-a7a7-3e58-9ae8-b9b7cc8c9e8d | -6.09389 | -42.66538 | 2025-09-30 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a11d2df9-e6c2-3e86-872c-f7f914ab51b1 | -14.7126 | -48.25798 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74f31f1c-6cd6-3d37-a9dc-e3389f0a5b61 | -4.9559 | -47.60451 | 2025-09-30 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69062b31-bf1e-345d-b2b5-155750e260e7 | -6.7895 | -44.08086 | 2025-09-30 03:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f68d1108-3b80-301d-bbf6-0fa08ada1a5f | -13.34762 | -47.81139 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0498f10c-b9c5-34a2-b388-7b33cc777903 | -14.56402 | -48.23516 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1df5c822-edc1-3c5c-8527-3e93e5447a6f | -11.06553 | -47.82507 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11ed14ab-f092-3a89-aa11-6761e32a6294 | -11.2543 | -47.22497 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d9446a32-c8c5-33b3-ba41-829d2ab29da9 | -5.52042 | -43.88149 | 2025-09-30 03:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1570d809-4174-3d22-8be2-eda1d49a0ba9 | -13.73771 | -47.90513 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5851e920-c238-3c32-b1f6-cda413223fba | -16.82779 | -39.33274 | 2025-09-30 03:49:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d0f175f6-6bd4-3d6c-988c-405f69eef6fe | -13.85971 | -44.41802 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 830502f7-ea3c-3e20-8288-dfcfa8f495f1 | -15.91858 | -46.24544 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 374ebe7a-d517-3ed1-8ff9-547d49eae522 | -15.27043 | -47.85355 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1585b1c-76a1-3fad-baf3-90569f026c72 | -13.36359 | -47.31833 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cfb1993-e204-3fb8-a362-b8a33b8c8560 | -7.69969 | -41.28575 | 2025-09-30 03:49:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75fc6d82-def8-305b-a21c-caaabf7d7ebe | -14.53726 | -48.22886 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4869039-5810-3d9d-9f30-82edf672931c | -13.15084 | -44.53619 | 2025-09-30 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f331397-9212-364b-bc9a-a79e32d39809 | -14.51735 | -48.01097 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8894a32-53d4-3a51-ad51-a02f5af9ed0f | -12.84637 | -46.8743 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42226fbe-4a45-3425-973a-27af35f63f98 | -12.84648 | -46.96985 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3abaa7a3-a8a2-3beb-9f25-b84a9a468e23 | -14.73945 | -45.662 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 12db6cc1-2fd6-3fcb-b163-87f76aeb4f42 | -11.21993 | -47.20124 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |


[Clique aqui para ver as próximas entradas](README35.md)
