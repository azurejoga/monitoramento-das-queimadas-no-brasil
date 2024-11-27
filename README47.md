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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a758ffdb-181c-3908-a882-c2be60093982 | -9.81453 | -48.16174 | 2024-11-27 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a467b075-1f4c-3a85-b360-2154d2ab9569 | -7.98068 | -49.69101 | 2024-11-27 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132287e0-31aa-3886-9fc1-73c0ae59ca47 | -5.57942 | -49.45446 | 2024-11-27 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253c1816-6db8-3280-a421-cfb26019dcbe | -6.73173 | -39.90346 | 2024-11-27 04:21:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7181eb8b-aed6-31c9-9e10-463314f8dab9 | -9.51777 | -42.99501 | 2024-11-27 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dab9e715-423e-374a-9bd7-2e8ecd708d11 | -7.07642 | -35.26316 | 2024-11-27 04:21:00 | NPP-375D | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d1a3e5b3-2e61-3442-9848-8bfff0511465 | -9.12413 | -47.7084 | 2024-11-27 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4f3ef3d-4fa6-336d-921a-86bbd8f8da79 | -9.726 | -50.34513 | 2024-11-27 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 459f5f72-60e8-30b4-b63e-e9eff629496f | -5.49422 | -47.65928 | 2024-11-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e4729f6-d50b-3402-a75a-d951c32d31b9 | -5.73773 | -46.51498 | 2024-11-27 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cbe542f-030c-3d9c-a105-55701b264890 | -6.90464 | -35.04167 | 2024-11-27 04:21:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a41cdec1-65c0-36fa-ad7a-45cb95873187 | -5.50094 | -46.25175 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3c64c6-9e0b-3269-ad4d-cfe8e0f10e29 | -5.70681 | -44.95914 | 2024-11-27 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a144d8a8-f56b-30df-99b5-d3524ba9c621 | -5.52461 | -47.58662 | 2024-11-27 04:21:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bc3ce69-2dcd-3b1c-9dc5-7529b55d08b1 | -5.89862 | -43.409 | 2024-11-27 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f8960d6-02b7-3cb9-9cc1-0ed474431f72 | -8.38428 | -44.47731 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b9041da-3ec5-3eb6-9c06-342293b7c1e2 | -9.7305 | -48.05793 | 2024-11-27 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91ed8acf-1a3c-306e-8fa8-1d7d43d5d9ef | -8.13047 | -44.47638 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6820f9ae-e5ac-3eef-a4f5-dbc2dd082e46 | -6.82722 | -44.3964 | 2024-11-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee391897-f58a-3896-aca7-b47cfcee925b | -5.75854 | -46.2584 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b17d3076-f663-3d46-9c05-d47d29a1341d | -11.70261 | -44.61967 | 2024-11-27 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0410df0-2809-3a52-9a56-d04e70d6572b | -7.26158 | -49.51313 | 2024-11-27 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78fcd1e5-38cb-3602-bd85-4b27544b8a5a | -5.63833 | -46.96861 | 2024-11-27 04:21:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dde72bb-87af-3a01-ac1b-40f8a48a2322 | -8.10932 | -38.9622 | 2024-11-27 04:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a46f2fa8-651f-3212-b735-e4a3ef288688 | -6.69463 | -43.06372 | 2024-11-27 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64c93df1-99e0-3681-92d3-c4bef7cf427e | -9.7254 | -50.34865 | 2024-11-27 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98e08c08-5332-30d8-91d2-6dc206ef923c | -7.85415 | -48.71065 | 2024-11-27 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d4172b8-e195-361d-baca-cd8cb502b9ec | -5.50212 | -46.2444 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9f25953-792a-31b0-b8b6-1695e2cb2f15 | -5.98462 | -45.36526 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f08a7f34-c595-3254-a206-6061bf0073db | -5.98239 | -45.35771 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2335d01-a9e0-32f1-b0ed-a75766332272 | -9.53187 | -43.20921 | 2024-11-27 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 61e11680-8716-365f-8651-abc2d5937f1f | -5.20096 | -48.18055 | 2024-11-27 04:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a83d8841-18ed-3b47-b9e2-02a662052401 | -6.70141 | -47.26895 | 2024-11-27 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 355ad2f5-8d66-339a-870d-ecd9b67bdc9a | -5.80325 | -43.00641 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86d24993-5908-32c4-8bfb-55cbb64b0a00 | -6.96441 | -45.07304 | 2024-11-27 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29c8a8a9-d6e9-335f-848d-a3bf371cbb1f | -12.02639 | -49.54218 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bd73e2c-9778-3a46-a673-8fb9d6162af7 | -5.50231 | -47.16703 | 2024-11-27 04:21:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10940a11-fc09-396c-b6a9-d82e3bf2c24e | -6.34542 | -47.30849 | 2024-11-27 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fbde9cb-3ebe-3af0-ac6a-e104e1444d7c | -10.52827 | -49.05066 | 2024-11-27 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc507aae-3c65-3719-b7b5-4a13f4676545 | -4.0663 | -54.38459 | 2024-11-27 04:21:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df063630-dc96-385f-9e39-4373f61ba81c | -6.63384 | -43.86251 | 2024-11-27 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea154f92-e0d6-35eb-bbb1-55ff0bb4ce88 | -6.1964 | -44.42872 | 2024-11-27 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57124f74-27f3-344d-9fd3-d6ccae88486e | -12.02715 | -49.53773 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06c13c18-093c-3f52-9cf5-c7dd4bdd8e0f | -5.50153 | -46.24807 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c92e94da-4e1c-30cd-b8bb-099cfe114a38 | -7.68306 | -49.12747 | 2024-11-27 04:21:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35620697-80d0-3e1f-99c0-8b1c7ad18542 | -7.7299 | -42.95391 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2ada645-b8df-3767-90a1-6bc063ceb522 | -9.5165 | -42.99516 | 2024-11-27 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d564036d-5ddd-3826-b1b7-bb1795ba4ce6 | -5.59598 | -49.86219 | 2024-11-27 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e244d44-0427-30c4-a673-10363683ad15 | -5.75432 | -43.07634 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3b2c2b6-900c-3299-977d-a546923308b7 | -5.97849 | -45.36069 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e3a69a4-59a4-3ba8-8aff-dec9bb768372 | -6.13052 | -41.98338 | 2024-11-27 04:21:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c44c4ec4-edd3-3f63-986b-a7944360ef20 | -9.81165 | -48.15712 | 2024-11-27 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0067309-75ab-37cd-8433-34e42b6acd1c | -5.65074 | -46.64534 | 2024-11-27 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97be74e4-365e-3209-b0f7-c0812c3d4ed5 | -5.75453 | -46.26153 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c271f7f2-fbe7-3be4-a7fd-d7d7fcbe17eb | -5.90197 | -43.40952 | 2024-11-27 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85f829eb-b25b-3f19-a9bc-ae80398518d7 | -6.3774 | -45.68446 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 844b3cfb-2953-3f6f-bb36-60046c119caa | -6.38075 | -45.68499 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 122afbe0-ce41-38b4-a757-e77629c3a152 | -8.13822 | -44.47042 | 2024-11-27 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a16a8d31-dc1d-3244-baac-e5a19d68c919 | -6.48001 | -47.4983 | 2024-11-27 04:21:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc7e444d-68c2-3967-ba79-2571a4d34a49 | -6.13071 | -46.91649 | 2024-11-27 04:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f7f2402-b3fe-3841-9d50-f4859b9edd9d | -7.69209 | -42.97132 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9d4ad232-fda3-3b6f-8289-7756dfc471e2 | -8.1099 | -38.95811 | 2024-11-27 04:21:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d1385791-5873-318e-ae58-5aa3532655ac | -6.6867 | -48.8732 | 2024-11-27 04:21:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7e7a89f-dbda-310f-8ea3-79eb0224b71c | -6.1342 | -46.91705 | 2024-11-27 04:21:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6653b259-bb00-3763-82f1-8190feb60c29 | -6.83054 | -44.39692 | 2024-11-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c638e7c-901b-3254-948e-441c29cad633 | -5.98127 | -45.36473 | 2024-11-27 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6122db51-d41e-3d28-90a2-88b0dece5f0a | -7.54524 | -47.58373 | 2024-11-27 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c0c0a5-1e0a-395c-8e66-a52168d99c27 | -5.8643 | -42.77036 | 2024-11-27 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb03deeb-0bca-3a94-aa5d-227780066a6f | -6.92967 | -37.13794 | 2024-11-27 04:21:00 | NPP-375D | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31d83e30-8445-3595-994c-e9da7e56666d | -7.69153 | -42.97507 | 2024-11-27 04:21:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5c92219a-7c5a-3fe4-9b46-35f1b470d157 | -6.83441 | -44.39396 | 2024-11-27 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a98d728-b20b-3124-a3a4-2316c89e8600 | -5.61838 | -43.95092 | 2024-11-27 04:21:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ca5ceda-d1e3-3352-b24a-350c9945da89 | -9.8152 | -48.15772 | 2024-11-27 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aaaa07f-3c9f-31c4-9f41-efd27b91aed4 | -9.17277 | -47.83021 | 2024-11-27 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca2d4497-4a88-3bf8-8b34-30bcfd9a6e3a | -5.4981 | -46.24751 | 2024-11-27 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c46569-2a19-3492-8960-7a8b9a9f1343 | -9.25343 | -50.66275 | 2024-11-27 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6c5ae5e-9765-3dc8-88c2-d5ff175b4f04 | -7.68387 | -49.12271 | 2024-11-27 04:21:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2b4c00c-b689-3ccc-8e47-b153fbb748bb | -5.1972 | -48.17992 | 2024-11-27 04:21:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e73ea92-663b-300b-a52e-2339c97f3424 | -12.01899 | -49.54082 | 2024-11-27 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 53fd4e6e-f769-3f8c-b6d8-d390d9cf498e | -15.29093 | -56.51972 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e4b3c83-df48-3e50-b00f-6a15fb876da4 | -17.75151 | -42.8914 | 2024-11-27 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eaed155-b7cb-3f4b-8c03-80357648a5d9 | -19.27566 | -51.46836 | 2024-11-27 04:23:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e45d1ea-77e6-3c64-baab-f1899d95cea4 | -15.29568 | -56.52439 | 2024-11-27 04:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51495456-12e8-3f13-9bfb-1c23055b83a4 | -23.83572 | -47.05496 | 2024-11-27 04:23:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8ea1ed6e-4ba9-313c-9cca-699b075cc58d | -20.01785 | -44.59526 | 2024-11-27 04:23:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c13f5adf-edc7-3179-b940-cbe3ea3389ab | -22.97896 | -50.39769 | 2024-11-27 04:23:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4d678315-5357-3011-9471-8a1f0003db91 | -18.59355 | -46.55134 | 2024-11-27 04:23:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 228b60aa-9f29-370b-b69c-356d4df7179c | -18.30144 | -50.90069 | 2024-11-27 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566369cb-edf6-322f-b8f6-e293fffbf56b | -16.67901 | -43.88534 | 2024-11-27 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67a2e82e-ecf5-3906-86a2-a4c7c0f2111e | -20.15484 | -48.91434 | 2024-11-27 04:23:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23c473cc-dfdd-3de0-8139-588684cceb19 | -19.45378 | -45.30779 | 2024-11-27 04:23:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe855226-08e6-3a3c-a690-c65967876655 | -19.1687 | -45.33912 | 2024-11-27 04:23:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa8ee8b0-e10d-3aeb-9426-707e6e9cd93b | -20.38346 | -47.47855 | 2024-11-27 04:23:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3c5fa8c-57c4-3172-9941-baf984e679a0 | -23.46876 | -46.29924 | 2024-11-27 04:23:00 | NPP-375D | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e4d500a9-34f2-3dab-b777-2c821003125f | -12.68226 | -52.26963 | 2024-11-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4107e54b-f523-3f27-9a5d-e0ac1a7ceaa2 | -12.6866 | -52.27039 | 2024-11-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4644e399-4ed9-3cf0-9a53-f66af36ee6e7 | -23.70297 | -46.47736 | 2024-11-27 04:23:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51510850-4ce3-33ae-ba54-e2d4d670992a | -19.2062 | -45.37387 | 2024-11-27 04:23:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8029abf8-9661-325e-a720-1d53f66e9165 | -18.70878 | -47.47897 | 2024-11-27 04:23:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9349b91-d376-3d65-a985-0671f7ccbe6f | -18.29777 | -50.90002 | 2024-11-27 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
