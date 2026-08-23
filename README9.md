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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c1a29b1-ead5-32be-8e5b-26aada437b4b | -12.24146 | -43.18657 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d79cee2b-3e07-3818-b341-98acd812a3b8 | -11.43682 | -44.53625 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3dd1b421-131f-3e20-af8b-e5c617028586 | -12.21839 | -43.17568 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b50927de-49aa-3fff-bac4-65a7416d03ed | -11.43478 | -44.53449 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13c2a45f-2c9b-397d-8946-93d0dd597c3e | -12.66612 | -42.28982 | 2026-08-23 03:23:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7910d92f-92c9-38ce-8f97-9623adb9aca3 | -11.44192 | -44.53612 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d7c4ccf-b63a-383c-8c65-2adbdf69acf6 | -12.24794 | -43.18832 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c020025-9ab2-3289-8a2e-93f6e2ff0ca5 | -12.22498 | -43.17687 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d22bb103-37dd-3d4a-9540-6f2da9fccfb2 | -12.23579 | -43.12468 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bfdc563a-e226-34e5-a0bd-428f3f7e1773 | -12.21968 | -43.16942 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4256d517-efe2-35e1-b5cd-61d7d504e489 | -10.45743 | -37.14368 | 2026-08-23 03:23:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| da637c06-9af8-314a-b6e8-deb825b73c6f | -13.43604 | -43.85559 | 2026-08-23 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5bac9819-247b-30a9-bc79-0c4f0aa8d491 | -8.81915 | -37.35079 | 2026-08-23 03:23:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0f369e0-2fb3-39c6-89e9-f6455cd736df | -13.09034 | -43.35122 | 2026-08-23 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c835c6b0-5a79-3eec-a9ef-699fc44c2a19 | -9.4753 | -40.35877 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee875fd3-91dd-3a91-88cd-c6ca237a291f | -12.26846 | -43.12382 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f194563-c05f-3cfe-98ff-d9f8e7607bad | -13.09683 | -43.35276 | 2026-08-23 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29bdc1ab-216f-38e8-a194-6d4e1d08e706 | -13.09802 | -43.34702 | 2026-08-23 03:23:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86e52927-8ec5-3bb7-841a-1ce71008fb21 | -12.28788 | -43.16119 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bca72a41-fc90-3714-b362-bcf8c9797c9a | -12.28276 | -43.15304 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc7f4a29-ca59-30ad-9886-b80f0c011924 | -10.45655 | -37.14856 | 2026-08-23 03:23:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 860b71dc-605c-3fa4-98ba-14382079169c | -13.42808 | -43.86026 | 2026-08-23 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 308f525a-88a8-3f05-9b60-c299fa6f6a81 | -12.22112 | -43.16247 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 42e133f1-47dc-3da8-a35a-20d0356e1bae | -12.26211 | -43.1216 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 199c5ecd-8a53-3279-9609-e8cb3039f4aa | -11.42968 | -44.53466 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa1fc0bc-959e-3051-bf13-d7a9a1833f10 | -12.66008 | -42.28784 | 2026-08-23 03:23:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77a6e499-b4d5-3382-9fe0-77e0f39f3873 | -11.42764 | -44.53289 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3519ac95-4032-3a80-9707-91e0f1a16d1f | -9.451 | -40.32822 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bf872acc-3f66-331e-9f79-f47bb10bb0ca | -9.44598 | -40.32298 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 802a71db-b84c-331b-bca9-0a94a7582f86 | -12.24232 | -43.12603 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4621bf18-2032-34ee-a7a2-8280cf99e0e3 | -12.26237 | -43.12795 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4cc3cf59-2e71-32f9-9dfe-9979b8d8ed5b | -9.48079 | -40.35949 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 96bad711-842b-3851-926d-36817f1a7323 | -12.26735 | -43.13694 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1c64d682-e873-36f6-9a86-1320e1583ef5 | -12.25437 | -43.1903 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3073181-b516-361c-a00f-82cb74d81efc | -13.559 | -44.09888 | 2026-08-23 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0016fee2-9bdc-301a-b4f7-4ed2f32567d1 | -18.03608 | -43.03906 | 2026-08-23 03:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38f1787a-2776-33af-b0f1-bb2319508f55 | -13.55757 | -44.1054 | 2026-08-23 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d041d9b-85ec-3cca-987b-9b0e416975e9 | -15.93906 | -44.04917 | 2026-08-23 03:25:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f77a99fa-41fb-3575-9a26-8bc297726a44 | -18.03027 | -43.03756 | 2026-08-23 03:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8490f283-57f8-3bc7-a935-76bc6e56eb2f | -15.93961 | -44.0485 | 2026-08-23 03:25:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca14d616-23b9-3317-9b25-ae6de09baf82 | -17.06711 | -39.42972 | 2026-08-23 03:25:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2d064487-2fbb-382e-93d3-170280a1156f | -18.0319 | -43.03885 | 2026-08-23 03:25:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d26b27d3-9477-3150-8253-befe505c9295 | -19.78673 | -43.69767 | 2026-08-23 03:25:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d918a1c-3f33-3452-a656-ecd8c1c1a372 | -13.55623 | -44.10476 | 2026-08-23 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bc85ffa-6fcd-3bf3-813d-6efa40096828 | -19.7856 | -43.70266 | 2026-08-23 03:25:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e6f3e6c-ae09-3e5d-b3d7-deb2175ea24a | -17.25265 | -44.8832 | 2026-08-23 03:25:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5783ef63-6f8f-3041-9a0c-3fa191aeaca0 | -17.25402 | -44.87717 | 2026-08-23 03:25:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78faf32f-276b-326f-973d-756d0b2a8dbd | -13.43261 | -43.85193 | 2026-08-23 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1810cf2-a761-3783-84fe-bbce1fcb3137 | -13.43129 | -43.85806 | 2026-08-23 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 444c2c81-acfc-37ff-846b-f97c4b271324 | -19.64208 | -45.72671 | 2026-08-23 03:25:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e17b26af-f3f7-3ccc-badf-0392aa9fd1f8 | -13.55762 | -44.09826 | 2026-08-23 03:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfbace34-9021-34bc-8ce1-66393915cfff | -17.25757 | -44.87856 | 2026-08-23 03:25:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 395eb07a-6b9a-3579-be23-3b3e0c3b9bc5 | -19.93331 | -40.79062 | 2026-08-23 03:25:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84efcb30-6485-329e-9cfe-8b2f6ad7a16b | -17.06816 | -39.42445 | 2026-08-23 03:25:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4da2dfb5-1b7b-3d82-b742-1053ea9674ee | -18.27742 | -43.30648 | 2026-08-23 03:25:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03d88e30-ca45-36a5-9b1a-bf407f96daeb | -15.78166 | -38.92241 | 2026-08-23 03:25:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c55502e1-2582-3152-8049-b907f52e0e4f | -21.4563 | -46.144 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 65ebae06-36ff-3aa3-94fa-f57dc1197982 | -20.66179 | -46.5658 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90069b00-f020-3a89-8db6-7940069c60db | -21.4449 | -46.14157 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 10a54755-f55b-3536-be34-b373e4ee9a86 | -20.6536 | -46.57317 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a20082b-947f-3db6-be0c-d969bc5a4464 | -21.45143 | -46.14322 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| c9a3b005-1040-39a4-9767-23b0646d73be | -20.65327 | -46.57125 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e63d6491-5de3-368a-b4b4-ee11b3b5863a | -21.45482 | -46.14998 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 89259b69-431f-387b-9380-9b92bc796e63 | -20.66364 | -46.56189 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d2c3151e-d632-3fb0-be10-c56eac624318 | -20.66318 | -46.56016 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d6ad6dfc-6f49-3591-9122-8e4cc232bd07 | -21.44995 | -46.14935 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| e69415a2-a330-3133-b4a1-3e72693c77d3 | -21.44341 | -46.14772 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a92fa8c0-ced5-3cf6-8dd7-16b9e09d4c71 | -20.66037 | -46.57162 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2374dca3-60fe-3a37-9956-583c76133f76 | -21.45645 | -46.15112 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 91d69186-8531-3671-9746-f4308df24ecc | -20.65162 | -46.57798 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cbc82e61-8e7c-3a60-8442-dcd88a6eb699 | -20.65632 | -46.55878 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0bfe7156-efa5-3cf4-9c05-b8bcf6f05bb8 | -20.65482 | -46.56495 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b766d8d4-810a-368e-a4d7-172b818c5ff5 | -20.65522 | -46.56673 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 479defd4-08d7-3e03-bd94-a88e978c0e22 | -20.65188 | -46.58002 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d63186f-01f8-3b01-82a9-2f5872b62f5a | -20.66227 | -46.56737 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 14461c3b-d0f4-3327-9b63-a0c4f2f31c54 | -21.45787 | -46.14522 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 599786c0-0038-3253-b182-3177d7a7eef5 | -21.44832 | -46.14822 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 5f9b5eb3-db41-30cd-b54e-f97a28c124a1 | -20.65675 | -46.56066 | 2026-08-23 03:28:00 | NOAA-20 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 828ec29e-afd8-3ae0-8957-15dd8d77359e | -21.44982 | -46.14215 | 2026-08-23 03:28:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 3e373f0d-baf7-3166-8620-61ca439841a6 | -6.8027 | -62.9024 | 2026-08-23 03:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fe98f9ac-7c71-317e-af6c-e6054f75b14b | -7.2626 | -49.9066 | 2026-08-23 03:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 37bd646e-37c5-36de-9cb4-55a4ec334903 | -13.1889 | -51.4234 | 2026-08-23 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7fa26211-a9b2-3ebd-ace9-5546479793d6 | -9.7996 | -46.5977 | 2026-08-23 03:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d74b42b0-fdd3-3689-8132-1346b92fd7dd | -10.8358 | -50.9903 | 2026-08-23 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 49bad317-7df8-3267-a7f3-303d3d78c908 | -21.454 | -46.1371 | 2026-08-23 03:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| 8aa4b0b4-977a-3b53-ad46-8bd252111f28 | -6.9699 | -59.0658 | 2026-08-23 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| c68b978f-5763-3cfb-a296-d451e5b124a0 | -6.8062 | -58.6469 | 2026-08-23 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 705977dd-32a6-3db4-977c-0fd88a9c6f98 | -10.8361 | -50.9691 | 2026-08-23 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e8edb85b-93f2-3f82-97f0-4ac1a1410942 | -16.0509 | -50.4363 | 2026-08-23 03:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0262533f-fde2-371c-8bae-809aef8881ef | -16.0706 | -50.4332 | 2026-08-23 03:30:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 77576bf0-d627-3e95-9fc5-e8c7df057e0b | -13.6806 | -51.8511 | 2026-08-23 03:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9a3e70e1-01a4-3b11-aca6-7f189cac1106 | -5.7799 | -57.58 | 2026-08-23 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8da7e113-7c1f-3a62-a1db-a558d2be7f52 | -13.6614 | -51.8535 | 2026-08-23 03:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 21a9c4c0-ef41-398a-ba95-40ffe86ae391 | -6.8188 | -59.6696 | 2026-08-23 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 59f4dea3-2fb0-347d-9dca-b0a1d2fbe0e5 | -6.1285 | -57.8393 | 2026-08-23 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d6f74b8e-2dc4-369d-8cf2-4e95c8ba38f7 | -8.1017 | -50.0546 | 2026-08-23 03:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 04fe5933-a6b2-3006-a8c3-7dd34c0d9330 | -6.9514 | -59.0666 | 2026-08-23 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 1728c929-1c40-3dea-b858-87361a53fb67 | -13.1697 | -51.4258 | 2026-08-23 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 68085d38-4a3b-3d68-9c42-1062b0e35d8a | -6.9514 | -59.0666 | 2026-08-23 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ba7a660b-b49f-3ef5-a4fa-9e98e4c92f2e | -6.8188 | -59.6696 | 2026-08-23 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |


[Clique aqui para ver as próximas entradas](README10.md)
