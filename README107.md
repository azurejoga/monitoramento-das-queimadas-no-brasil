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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c413895-b4fc-3f84-a72d-0cfdb99cfbc6 | -11.3709 | -43.5631 | 2025-09-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 4026b560-37e0-359c-bc00-4705fb252c00 | -11.7993 | -46.4114 | 2025-09-01 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 29222c85-a16b-3490-b547-7b1f25c675b9 | -6.185 | -43.3491 | 2025-09-01 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 2bbab45f-f2d2-3395-920b-42273480b0e4 | -7.3992 | -47.4333 | 2025-09-01 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 6fde949c-0960-356a-a4e2-e271bd002967 | -8.8625 | -47.5198 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| a8dfa088-158e-30ed-925d-5178c123c4bc | -13.2876 | -46.894 | 2025-09-01 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d06a52bb-4e86-350c-9fca-23ff8e184492 | -6.8281 | -52.8143 | 2025-09-01 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 5a227387-caa1-31a4-b23a-3e8e948391ff | -4.9122 | -43.2103 | 2025-09-01 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d418b0f8-5e94-36a4-9780-537b1f830982 | -6.7438 | -43.7898 | 2025-09-01 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 23ff48b8-7753-31a8-95ed-239fa0afb159 | -7.9536 | -46.4765 | 2025-09-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| da2efdc1-1c3a-3524-a4c1-59ad8edc12b5 | -6.1853 | -43.3257 | 2025-09-01 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 79d516ec-d0a7-3f86-b563-5814252088e2 | -6.8237 | -43.3402 | 2025-09-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 07762731-83a0-32d1-bbbf-db7799a0c3f1 | -11.0377 | -45.1487 | 2025-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 3be6872c-fd48-3041-a135-54c397edcb0a | -7.076 | -44.3376 | 2025-09-01 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 44fe6f82-dd93-3bfa-89e1-765852fe1b00 | -8.8439 | -47.4996 | 2025-09-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 681b53e8-e54e-31cf-af4d-db8c1d46337b | -12.392 | -46.4626 | 2025-09-01 13:20:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7eb795a9-56a7-326a-ada3-38041f4d3098 | -7.0948 | -44.3358 | 2025-09-01 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 77919341-ec61-3e99-924b-bd5c1cf17f76 | -6.7038 | -42.2665 | 2025-09-01 13:20:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 413fa553-27ac-36f6-bce1-e2bbeac75a76 | -7.0757 | -44.3606 | 2025-09-01 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 1e25918e-075f-3c78-815b-e552c9790ccb | -6.1853 | -43.3257 | 2025-09-01 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 54e9d642-91b6-358c-8417-daf01b5f1222 | -14.6478 | -43.97 | 2025-09-01 13:20:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 87.5 |
| dda281bf-6429-3034-89fb-2fe3faee2cbb | -4.3197 | -48.0908 | 2025-09-01 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| de91f2e1-07f5-3755-a9bd-ecf75c20f8e2 | -11.8185 | -46.4087 | 2025-09-01 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f174b23d-eae7-3013-a7f0-bdd04a448bbe | -6.8281 | -52.8143 | 2025-09-01 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| dc7eb541-d8ef-3e47-b37d-1c9f67c22cf2 | -11.0654 | -44.637 | 2025-09-01 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f5188ca6-67e1-3997-941e-61b9e852049d | -4.9122 | -43.2103 | 2025-09-01 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 15cd4e98-a64b-380b-88cb-edeaf76a3277 | -7.3992 | -47.4333 | 2025-09-01 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b4abff74-d549-3787-8fef-9d03b9489c98 | -14.0502 | -44.5779 | 2025-09-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| c6167e54-bf85-3761-8d50-3e46a0a5c3b5 | -12.996 | -48.1022 | 2025-09-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6907aeea-8557-3fcd-bbab-91a1a3afdfce | -12.9768 | -48.1049 | 2025-09-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 9e785cfb-60dc-313c-9cad-6d9b66fa8b15 | -12.9764 | -48.1272 | 2025-09-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| fdc850da-bea1-38d7-98f2-f414098cb2e5 | -8.8622 | -47.5418 | 2025-09-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d899568a-2bdf-314a-893d-c1e575c4d803 | -7.9348 | -46.4783 | 2025-09-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 04fdc878-db01-31c9-8202-ddb0c582a6cc | -11.0845 | -44.6343 | 2025-09-01 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 445.4 |
| 7121ce7c-d25c-33ca-b9d9-2a011cc8c5c1 | -12.9956 | -48.1244 | 2025-09-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0b7b24dc-31e0-32ae-ae31-b1758d9f6ebe | -6.8428 | -43.3151 | 2025-09-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 6f4c33e3-67d4-342c-a30c-f6d68652804e | -12.9575 | -48.1076 | 2025-09-01 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b07e4c9e-e2f6-357d-8ad3-b328f96ff47a | -11.3709 | -43.5631 | 2025-09-01 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 3b33e152-cb21-39cd-9ffd-932063c65b0a | -8.8437 | -47.5217 | 2025-09-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 385.8 |
| f0f360fd-1237-3b1e-810a-d01f009b59fe | -11.0568 | -45.146 | 2025-09-01 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 5463ea70-0f83-338b-8138-e10352f7dd8a | -9.6127 | -47.8169 | 2025-09-01 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e3485645-9265-3a6e-b97a-a8702ee0b8e1 | -11.3901 | -43.5602 | 2025-09-01 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| afd0e246-5ca2-3c2f-902a-17294239b388 | -7.0572 | -44.3393 | 2025-09-01 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 2deec0c3-8e76-3ff7-a96f-1e0448142920 | -13.3245 | -46.9787 | 2025-09-01 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0643a5f2-a0c2-349b-9b79-ef66c6bc6947 | -7.0946 | -44.3589 | 2025-09-01 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 1fb31f1f-f80f-3467-afb7-914def9bfa4b | -11.3705 | -43.5868 | 2025-09-01 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 338.6 |
| d1a4b5b8-63be-3fc9-a072-601e67a8a1dc | -7.9539 | -46.4542 | 2025-09-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| 3068951c-b87d-3ea3-89e8-c543acb5b493 | -14.6483 | -43.9461 | 2025-09-01 13:20:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 9cf2e2bf-335b-3daf-bd51-5cf224fe0cab | -11.0849 | -44.611 | 2025-09-01 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 40431b48-1167-3d45-bb42-4085686cd5a6 | -8.8625 | -47.5198 | 2025-09-01 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 168.4 |
| ae8ee6c3-355a-372e-b502-cb48538bd0df | -11.7989 | -46.4341 | 2025-09-01 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5e8c63ae-32d7-3d7a-a1a4-c796c67d66dd | -6.824 | -43.3168 | 2025-09-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.8 |
| 0164477a-ddb1-3323-8a28-5ee8e0f9f723 | -6.8426 | -43.3385 | 2025-09-01 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| f170b8a5-10d2-37da-82a4-27f084de14f5 | -8.1943 | -46.788 | 2025-09-01 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 10531d82-fafb-3dd4-8a2c-ff7730e876fb | -11.7993 | -46.4114 | 2025-09-01 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a847b320-4b12-38d7-a0d7-02a27a2f91bf | -6.2038 | -43.3475 | 2025-09-01 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5fa42415-2694-3ae0-bbbf-822f383ded5d | -7.9536 | -46.4765 | 2025-09-01 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 40831974-517d-36a7-b722-65547d02e480 | -6.1665 | -43.3273 | 2025-09-01 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e3e19652-c267-3504-9a14-a6cc6533f397 | -11.3701 | -43.6104 | 2025-09-01 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 9c16f2c6-8c1c-37e0-98be-d70ce6a75667 | -9.2825 | -47.1007 | 2025-09-01 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 6781e469-b0c4-37ab-a576-5fe978dadd9f | -14.0508 | -44.5543 | 2025-09-01 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 07e901be-e5ec-38cf-8a72-7772a9055e8c | -7.9348 | -46.4783 | 2025-09-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 324.8 |
| e0502b9d-6fa5-3375-bfba-2f8245191054 | -7.0948 | -44.3358 | 2025-09-01 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 87b7c623-2815-315c-83c5-44978f803dd8 | -4.8936 | -43.1882 | 2025-09-01 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2e8f4dcc-b591-37e4-aef7-0315347e7a54 | -8.8437 | -47.5217 | 2025-09-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 359.9 |
| 5110c826-21e7-3cc6-ab5c-f6b6b8780c4f | -14.0502 | -44.5779 | 2025-09-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 528cbc83-aedf-3d5d-ad09-41d395d72f1b | -12.9764 | -48.1272 | 2025-09-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cdf00331-0783-310f-9d1f-4a3c3f6bfcdb | -13.5171 | -46.994 | 2025-09-01 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 0c1790ca-38e8-38d6-b8c9-dbed18617ac8 | -6.744 | -43.7666 | 2025-09-01 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| bfad639e-6a67-3682-bc7e-712e3130d5d8 | -7.076 | -44.3376 | 2025-09-01 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 54e92c45-fd46-3c71-9df9-4b6ab132a0e5 | -14.6478 | -43.97 | 2025-09-01 13:30:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 0cf4088f-663f-35a5-bc15-7528314bbc8d | -11.0381 | -45.1256 | 2025-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 93a472eb-b6c4-31c0-a138-152fed220c70 | -7.9449 | -63.0151 | 2025-09-01 13:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e509b052-4fa6-3eab-b3d8-b555e6aa6b3b | -7.9536 | -46.4765 | 2025-09-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 333.9 |
| 623e4809-7eb8-3766-a1ad-0fc63c130a60 | -11.7989 | -46.4341 | 2025-09-01 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4e8ea16e-8a21-3d10-95a7-a07eb331ecfd | -7.9539 | -46.4542 | 2025-09-01 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 7ceb2609-15f2-3ac1-9289-59d06048001c | -9.6607 | -47.0597 | 2025-09-01 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3ee968ea-6c23-35fa-afff-c35cfa0a5efb | -11.0845 | -44.6343 | 2025-09-01 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 577.2 |
| c2256f57-7612-310d-ab5b-8c1430933be2 | -4.9124 | -43.187 | 2025-09-01 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 306.3 |
| 5449a680-261a-3066-a1d2-46a9466750c7 | -11.0849 | -44.611 | 2025-09-01 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 283.7 |
| df457b99-9448-382a-be28-497e00dad29e | -7.3992 | -47.4333 | 2025-09-01 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d6569c17-65ae-3b23-94c7-35adf193ca4f | -6.1853 | -43.3257 | 2025-09-01 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a9f4ae41-19af-3f5d-b415-12cdb9e21a4e | -12.996 | -48.1022 | 2025-09-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8bc903d4-c303-3ad6-bdc4-6c3f3d2ec815 | -7.0572 | -44.3393 | 2025-09-01 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| f96d1dd9-ae6f-3283-bd51-c52e0ac4ccb0 | -6.8466 | -52.8132 | 2025-09-01 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d7b35bf4-e9c8-322f-aee8-6d2957760e4f | -13.3245 | -46.9787 | 2025-09-01 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 447ec4a1-2af6-341a-ae7e-801726646403 | -7.0946 | -44.3589 | 2025-09-01 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e23fc9dc-e19f-3166-80d9-459be851df51 | -6.7438 | -43.7898 | 2025-09-01 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3198a11a-001c-3188-925e-ca34f5933add | -11.0377 | -45.1487 | 2025-09-01 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 159da2d1-0837-3971-a49d-1af58a50c554 | -4.9125 | -43.1636 | 2025-09-01 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 55c26ca1-97dd-3acb-9828-89102d5c965d | -12.9768 | -48.1049 | 2025-09-01 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| e89ac7ee-8f4e-391a-a5d8-3dab6af02c5e | -11.7993 | -46.4114 | 2025-09-01 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 83f638ae-eab5-3ac3-9863-2dc52f56e772 | -7.0757 | -44.3606 | 2025-09-01 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 0b7d173f-7cd9-329b-9f71-38da34fa1ca5 | -6.8428 | -43.3151 | 2025-09-01 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 6874dc05-5b76-35a2-8444-b0de101711a9 | -14.7427 | -46.7472 | 2025-09-01 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 227204bf-69f9-3a61-b20d-b81d6cb5cb59 | -11.7798 | -46.4367 | 2025-09-01 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 95e2c1d9-a392-31a0-bb89-c0405f2f18df | -8.1943 | -46.788 | 2025-09-01 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 1a58d197-2f5d-3abc-8fa0-e65c7cad0de3 | -8.8439 | -47.4996 | 2025-09-01 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| bd20c226-2d1c-33c8-be52-a82c279a0df6 | -14.0508 | -44.5543 | 2025-09-01 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| da96d0eb-ec4d-35c4-ac3c-14eea09d8234 | -6.824 | -43.3168 | 2025-09-01 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |


[Clique aqui para ver as próximas entradas](README108.md)
