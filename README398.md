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

## Dados Diários - Página 398

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4498980-4ebd-33fc-a3fe-44ab4c0d8aac | -2.4804 | -56.1662 | 2026-10-08 18:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8963531d-4f87-3c02-8840-50c9d9f1a739 | -4.0628 | -51.0508 | 2026-10-08 18:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 5b423270-bd77-3909-81ff-8f6387fb0b37 | -11.8696 | -43.5568 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| aad6727a-424c-3c45-bb87-606a99d15155 | -3.1114 | -53.7839 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 4960a005-8c55-3e4d-b3f8-4487d09f8e0b | 2.0047 | -55.8786 | 2026-10-08 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 78ae2791-5ed5-34c9-a39e-70afd737cd60 | -1.4771 | -53.6134 | 2026-10-08 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 38aace14-caf0-3925-a95c-8bc6c5dee151 | -1.3447 | -56.3979 | 2026-10-08 18:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 51eaae06-88c6-36c2-b10e-744c9b7689f8 | -7.7025 | -45.4436 | 2026-10-08 18:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0b1585bb-a8ae-34b3-829c-0e1f71dcd2db | -6.1429 | -47.9432 | 2026-10-08 18:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 20ff2450-260c-3419-804c-1b578ab8675a | -5.5146 | -42.8399 | 2026-10-08 18:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| d5668270-ef91-3d06-8869-d2513ff6ae69 | -2.5492 | -58.0373 | 2026-10-08 18:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 26997f11-437c-39d4-985d-c6748fb0daaa | -3.724 | -57.1189 | 2026-10-08 18:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 819da168-405f-3c4e-8706-672e9fa1cc99 | -3.3134 | -53.8592 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b242a030-48fc-3ca5-9723-5152b7be290b | -3.1874 | -58.8358 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cf990ff0-c1a1-32b2-b6f4-e0804f360c39 | -13.3671 | -43.8742 | 2026-10-08 18:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 486fddf9-a574-3e7a-b9b8-7435583f7e20 | -11.619 | -43.6196 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 357.7 |
| f3760f97-6f31-3255-b36c-08e4dba76daa | -6.3351 | -43.3598 | 2026-10-08 18:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| dabd8ada-15ab-3403-ad30-c1a4c0610a7a | -3.2633 | -57.8883 | 2026-10-08 18:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| b0e2fece-5cc0-321a-9fa7-14b2270b8582 | -3.86 | -44.1274 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 44a10c60-afdf-3aee-8ef2-7c3393aaec98 | -2.7797 | -54.0736 | 2026-10-08 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8e779004-2afb-39cf-985b-17553e03fcef | -2.7613 | -54.0941 | 2026-10-08 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 64444d39-a2b3-3813-8132-c8bda7888d7a | -5.6932 | -53.487 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 314.6 |
| 37180874-d2cc-38f8-8066-ff5d6b8276bf | 1.7488 | -55.5663 | 2026-10-08 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| a0378a98-181a-32fc-802f-36d5beb469e9 | -3.2533 | -50.3899 | 2026-10-08 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 470659be-0c61-324e-9fa7-2930087a3bee | -8.0947 | -39.8753 | 2026-10-08 18:50:00 | GOES-19 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 39aac324-b25f-323e-857a-1fb1d52cdf47 | -3.1879 | -58.6433 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 84149807-7859-3903-b1ac-888c0c210304 | -13.8855 | -44.1127 | 2026-10-08 18:50:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 21e1a212-b16f-3b94-9d08-80c70a948a7e | -6.0609 | -42.608 | 2026-10-08 18:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 5818eb9a-278b-3081-9fe7-834a52cf1789 | -2.7796 | -54.0937 | 2026-10-08 18:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 07de1296-ea6d-3776-a95b-79ff201e725c | -2.3115 | -57.9829 | 2026-10-08 18:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5b71e6b2-6e00-3bc2-9af6-35d5152b1887 | -5.7304 | -53.465 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8c256e67-8b20-3e1b-a43e-1b11adc59fb2 | -6.6224 | -53.0105 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0637d3cc-f274-3b36-b8f2-e806ca5c0c94 | -3.2031 | -53.8621 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| aec7c9c3-052d-3bca-8d87-5f5c39c0a71d | -1.5307 | -54.5159 | 2026-10-08 18:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2449e741-4999-34fe-ad27-184a2ed2723d | -4.7404 | -55.6522 | 2026-10-08 18:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 3c98e9cd-f558-31cd-99be-b2da0448cf53 | -15.1057 | -43.6168 | 2026-10-08 18:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 133.2 |
| a6b0c778-5718-349b-b327-8f10ce8053a9 | -5.3953 | -45.897 | 2026-10-08 18:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| dccb79e8-a8d6-3c15-8944-df7a355ae9eb | -2.7152 | -57.472 | 2026-10-08 18:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4a174b5f-2ed2-345f-8cd3-e2abff046171 | 1.7671 | -55.5661 | 2026-10-08 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 5092a15a-3832-3c38-b1b0-cdeed423aaee | -3.1602 | -50.5812 | 2026-10-08 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| c0d17b6c-d851-3b35-93c3-6db52d12a704 | -2.1361 | -54.4671 | 2026-10-08 18:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| c22ea3d1-f02c-39cd-b583-23c7c71f12b9 | -6.0744 | -43.1478 | 2026-10-08 18:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 89cb2e30-27c7-39db-ab8b-1518058a47be | -11.1992 | -49.408 | 2026-10-08 18:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c580e893-bbc1-37cd-9fd2-20d47be60153 | -3.1787 | -50.5807 | 2026-10-08 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 704bfc3d-22e4-3500-af10-fb84ba3b5bc7 | -3.1601 | -50.6021 | 2026-10-08 18:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ea791a0c-181a-393f-a946-503e7aa37fb0 | -5.4958 | -42.8413 | 2026-10-08 18:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| 11cf595c-91cb-3667-9591-8c86eace5bbd | -3.4068 | -58.9083 | 2026-10-08 18:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5c3183e3-8d30-3771-b440-1e4fcc1899ce | -6.1242 | -47.9444 | 2026-10-08 18:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0f8e4151-b45a-384a-9232-e15efe38b9b5 | 1.6937 | -55.6263 | 2026-10-08 18:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 31a5daaf-0262-352d-8666-220ba7513d0c | -7.0892 | -52.6753 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 281.9 |
| 55a4fa5c-26b0-3fc8-bc7c-16fa38b98cc7 | -12.2508 | -44.7397 | 2026-10-08 18:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| fa8657a9-f0e9-3e6e-82ed-f84d39cde626 | -14.4345 | -43.9157 | 2026-10-08 18:50:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 9ef8bf2b-d107-31b5-a021-c5ca52c371da | -3.1114 | -53.8041 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 065cb0d9-9673-32a1-b2b1-84983f014045 | -7.4694 | -42.8551 | 2026-10-08 18:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 93a091cd-2913-3278-a81d-180e078436da | -9.1294 | -45.8405 | 2026-10-08 18:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 081dadd0-844b-36d8-a534-39de148403e9 | -3.505 | -44.2818 | 2026-10-08 18:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d1333aa6-1a1e-34e2-88c2-08f5a4f606c8 | -6.0076 | -53.4919 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 655dc502-46c2-3942-805e-a2f2841219a7 | -3.4312 | -56.9502 | 2026-10-08 18:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 47c34529-527a-31d6-a81a-b84e150adfb3 | -2.8897 | -54.1514 | 2026-10-08 18:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| be741338-1416-3673-885e-df78b20e26c1 | -6.1431 | -47.9214 | 2026-10-08 18:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| db327980-2c02-3447-9b2a-cf8ecf47edfd | -2.572 | -56.1842 | 2026-10-08 18:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 291.3 |
| 3de94ffa-3c22-3668-8ad4-adea7b1d0fdb | -6.0447 | -53.49 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| a33f1372-7d3e-3d6f-85ad-e971ca35337b | -7.0281 | -45.3008 | 2026-10-08 18:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c48ce42f-d461-397e-a9c8-6abe7db83d53 | -9.9208 | -44.7893 | 2026-10-08 18:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 10608623-a3e1-36de-9e2a-3225503c05b3 | -1.6213 | -55.1321 | 2026-10-08 18:50:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 86802f8c-b7ec-3d22-966d-39d073afe4e7 | -6.1484 | -51.927 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| f0c263eb-2f22-3e07-a163-345c7e206258 | -12.7678 | -44.8671 | 2026-10-08 18:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 40730aaa-1c99-3b23-a78b-fe0796991743 | -3.3128 | -54.0202 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| fad7d84b-bb71-3bd2-8ee7-beb969f50dc5 | -12.2311 | -44.7661 | 2026-10-08 18:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7789818c-d304-33aa-a9a2-0473ad907740 | -6.3134 | -54.7884 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3f17727b-cde5-3246-94a9-750979a1fd70 | -5.9649 | -40.914 | 2026-10-08 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 0a47647a-7053-3174-b824-1d7efd27dc89 | -3.7057 | -57.0998 | 2026-10-08 18:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f7923dba-177e-35e1-b800-1660706200e1 | -4.0838 | -44.1159 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 275.1 |
| e12c6013-7ad8-336c-bda4-f2500b3a2b4f | -2.5903 | -56.1839 | 2026-10-08 18:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 9a7228e4-aef5-385b-90fb-fef79e6799d7 | -7.591 | -47.0201 | 2026-10-08 18:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 3ad2d5af-4bbb-3786-b3dd-f92ce7184d37 | -1.383 | -55.1944 | 2026-10-08 18:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| dd3b1900-b04b-3c8d-8404-f8078969190c | -7.4697 | -42.8315 | 2026-10-08 18:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| bc20868f-84fd-3ae6-8765-26864f0451c9 | -14.4585 | -41.2104 | 2026-10-08 18:50:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 325d67bb-3e4f-35d0-a86d-77f2d91c924d | -3.3723 | -58.1957 | 2026-10-08 18:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 67ebe9ab-be5e-395a-8c15-42409c592919 | -11.8503 | -43.5598 | 2026-10-08 18:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| f86fb603-79b4-3e0a-b809-430038f6340f | -6.4752 | -55.48 | 2026-10-08 18:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| d2b7c721-5355-359f-8cde-f40435b6d103 | -14.0873 | -43.7671 | 2026-10-08 18:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 98886631-47cf-3832-9bc9-38306facf124 | -5.3905 | -44.1968 | 2026-10-08 18:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| a6017766-4c90-38fb-9197-dd6cbd04a9ec | -6.1501 | -51.6992 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 923109bb-d52e-3e57-8a87-f207e12c60f6 | -4.084 | -44.0929 | 2026-10-08 18:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b4e64b0b-a138-31bf-959e-e28359aaa158 | -14.0472 | -43.8222 | 2026-10-08 18:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 81e2815c-95d9-3f1d-9714-bd0921c77d4e | -6.2529 | -52.847 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e47834cc-e13a-3c17-a50d-b98ea6227897 | -6.2158 | -52.849 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 60e226b1-0a24-3476-bed0-e0e67e9e4ccb | -11.2849 | -45.2063 | 2026-10-08 18:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| fbff1c77-000d-37d2-a691-94bf310c40df | -6.6814 | -55.0903 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 1243e26d-9d62-34c1-a616-952c73e86cda | -9.3394 | -65.4638 | 2026-10-08 18:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 01634d97-b8ad-3159-913e-0d40256e4dff | -5.9647 | -40.9383 | 2026-10-08 18:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| b6715d8e-ae50-3ccf-a796-94197c5ebd6f | -3.2761 | -54.0011 | 2026-10-08 18:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7bad037e-820a-3083-9625-0653b56a6248 | -6.9328 | -43.6799 | 2026-10-08 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.1 |
| a4d9cdcd-cb41-32e8-8406-6b8537190f04 | -1.8233 | -54.9307 | 2026-10-08 18:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 552414ff-eca1-327d-9ec9-9006a0db0167 | -6.0075 | -53.5122 | 2026-10-08 18:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 0ccd172a-f2ce-3fae-a4aa-ace6dcd5033a | -6.2355 | -52.6841 | 2026-10-08 18:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| fa68b763-06d4-3f0e-9dee-99d4ef30cd7f | -6.895 | -43.7066 | 2026-10-08 18:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 22b95e18-20dc-3afa-b92e-c7b885939f84 | -2.8433 | -57.4891 | 2026-10-08 18:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7cf12e56-6a32-3831-a221-2d19737a9167 | -15.0346 | -42.4941 | 2026-10-08 18:50:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 113.5 |


[Clique aqui para ver as próximas entradas](README399.md)
