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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63ee057a-54c7-3c7c-8368-cbce1e53973b | -7.12561 | -47.50144 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb9ea2e3-d0df-341f-b8a2-22e671f57558 | -6.17142 | -39.3873 | 2026-08-20 04:00:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 24602c05-3cce-3191-8f19-7e62fbf536ad | -2.57126 | -47.20525 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a271bbb5-65c9-3cd7-b22e-a2e590f69028 | -7.34198 | -45.83317 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e77f429c-bc0a-3faf-bdac-f0bdf4a0618b | -6.78317 | -42.89062 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 20d9fa0d-6b05-3623-8d94-c67ac3830d1b | -4.39524 | -42.34412 | 2026-08-20 04:00:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a618f963-e0b3-3280-bacb-0a35ccab583d | -7.00748 | -45.8953 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5adfa56-3bbc-3378-b509-248f8b4dde40 | -6.33895 | -44.08032 | 2026-08-20 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c3e23e67-5748-3e89-902f-9978ca7fac9a | -5.5262 | -44.11198 | 2026-08-20 04:00:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0abd9f7f-efe1-325b-8181-f2b391ca8697 | -7.63535 | -42.78857 | 2026-08-20 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 344162b4-21e3-39b9-8322-127cf1b3877f | -6.29104 | -43.64211 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ac90ca8-bddb-3612-b7e5-b80e7ad6d465 | -2.64267 | -47.98272 | 2026-08-20 04:00:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f43dda5c-ee55-352d-8312-4d94b3420585 | -5.53878 | -42.27698 | 2026-08-20 04:00:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6415970b-7334-3a91-86c9-019e1774dfd6 | -8.8117 | -44.21114 | 2026-08-20 04:00:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a81384d6-62c2-32fa-96e9-46c3775e15bd | -7.44885 | -47.17012 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffa824bb-5c4f-3dfe-8cc7-32fac9a7b466 | -9.3978 | -37.81137 | 2026-08-20 04:00:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 11dc4f09-3d43-3f85-9873-1e61445c504d | -6.29522 | -43.64586 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31140a75-ff66-3fdf-970d-7ca49c19e484 | -7.35513 | -45.81953 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8ad254e3-bf15-3c09-8f13-4387d4a5801c | -7.96405 | -44.6663 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2c22b20d-87e7-3db3-95cf-5044d50543a0 | -7.61111 | -45.16317 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f3f927d-78d1-3dd9-8f65-77146b92119f | -7.6457 | -42.7783 | 2026-08-20 04:00:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9bb68f1e-01fa-3ebd-8f0f-012b64b1a412 | -4.05542 | -38.28851 | 2026-08-20 04:00:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 46c44f11-031d-355c-8f44-90ab7f171075 | -6.27049 | -43.2769 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 289e8a64-ed64-356b-8698-42db83bb9848 | -2.57049 | -47.24795 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 61a0e9aa-5443-3d53-a9c7-448c8c16c034 | -7.34715 | -45.83412 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8423d296-91bf-312d-a583-b94319bd1b9b | -6.42038 | -35.08699 | 2026-08-20 04:00:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7905f5a-a74d-3ae9-8ae5-f263a14a1996 | -4.93573 | -41.98007 | 2026-08-20 04:00:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 427c2b0a-858c-3f14-8778-d4ccdb365687 | -7.61013 | -45.16871 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0ab8fb6b-32b8-3e1c-93bf-56b9266cc66c | -5.73948 | -43.27604 | 2026-08-20 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dd989976-bce7-3ca9-90ad-d87532eebbe0 | -7.60318 | -45.17924 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6a08e19-ac19-3a74-8551-935049dfcc7d | -7.96756 | -44.67001 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 13856f45-9a28-317d-ac7e-6f2b5e09f223 | -7.34996 | -45.81858 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6badf182-57e1-31ab-949b-4e39cba858a6 | -6.28727 | -43.63678 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b492a647-88f8-317e-bd51-0e00e1d4c94d | -6.34155 | -44.07785 | 2026-08-20 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 151e05e1-17b1-38ce-887f-6b796aabcd92 | -2.56973 | -47.25259 | 2026-08-20 04:00:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 22feb5c8-fee9-351e-b752-fc49b1eb87bc | -7.01852 | -45.89396 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fbd6a9a-a8d2-3ec9-8a2f-7fc1be01ec3f | -2.57125 | -47.24339 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33eae5c0-cd79-31b1-8401-d5938aefdb4b | -4.09465 | -42.49983 | 2026-08-20 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4b28905-e525-344c-b52d-faaf5364a1fe | -7.35804 | -45.83303 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8e6fa2c-c48f-393d-82df-0492e049f80c | -6.42343 | -43.06902 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74963849-942f-3d3b-8cd4-c51214c2d38e | -7.96879 | -44.66711 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 56dc7c0f-4fc3-3aca-968f-bf8a42ff93df | -8.4566 | -46.94995 | 2026-08-20 04:00:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 862dfb77-00c2-366c-85ef-a8734f2949c4 | -6.14519 | -47.22791 | 2026-08-20 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6805bc89-585b-34d7-b61e-dce1aef8de0c | -7.97316 | -44.66582 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b12f49ec-f2ed-3a7f-b44b-033492a10750 | -7.01727 | -47.9722 | 2026-08-20 04:00:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77a37a65-1215-3421-b977-8dcfc2d0c00f | -7.34828 | -45.82788 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 55e22dce-9711-3cb1-8f7f-fc3739af68d3 | -6.34068 | -44.08282 | 2026-08-20 04:00:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 131b0419-4d21-3781-8563-8a280fb3dcf2 | -6.29181 | -43.63752 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf4e8cea-fac9-3d3f-a1cc-12415ecea544 | -4.05424 | -38.2916 | 2026-08-20 04:00:00 | NPP-375D | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a0182a7-41a9-33d2-bf8c-329854e4428e | -7.76062 | -49.20342 | 2026-08-20 04:00:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80254456-5796-3756-840e-44018ac0b89b | -7.35457 | -45.82263 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3443b35b-63b9-3619-9338-6bd2c8d68969 | -7.34771 | -45.831 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8468272-8bc7-3fb6-9c3a-549ce905315d | -7.27318 | -39.32092 | 2026-08-20 04:00:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3c6d678-9e08-3bbd-bd76-6a24c925b45d | -7.34254 | -45.83006 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5af85739-ebce-34a4-9749-3fa5b69f9075 | -8.46139 | -46.95464 | 2026-08-20 04:00:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64f589d2-162e-3ca5-b3c8-338248e43c1e | -3.96565 | -43.11311 | 2026-08-20 04:00:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e8bc7c51-c26e-3e90-812c-35981cc23285 | -9.38617 | -37.82024 | 2026-08-20 04:00:00 | NPP-375D | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 771ce64a-2bfb-38a4-a9e3-a0825f42b38a | -8.46618 | -46.95933 | 2026-08-20 04:00:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 434cdbe2-526c-3972-b260-b386fb62fcbb | -10.45703 | -37.14377 | 2026-08-20 04:00:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d7bf55d1-03e6-3582-ae39-60a7da1c9000 | -7.01274 | -45.89607 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5b8100b-8f3f-3c92-8c61-aea4960622e9 | -7.97057 | -44.65722 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b7882cd-0fec-3d81-8de7-6cd301c24508 | -7.96283 | -44.66917 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d9e9dfd8-3e27-37d1-b96f-9384f9480f8a | -2.57056 | -47.24531 | 2026-08-20 04:00:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f34f107e-a29a-32d5-b623-473234a99dca | -4.09396 | -42.50402 | 2026-08-20 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9eecc7db-fa6e-344b-810e-eba5d0cbf865 | -6.28802 | -43.63233 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ff0c90b-dd97-3e45-b582-d2142aebcd97 | -6.1394 | -47.22692 | 2026-08-20 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 91812c79-84b5-361d-97c7-9fe21830f5b6 | -5.73501 | -43.27525 | 2026-08-20 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb05909-7aa6-3b81-b32f-e5e70e0e557d | -6.29403 | -43.65211 | 2026-08-20 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f8dd623-64a9-3f0c-b935-64e324e396fb | -7.4545 | -47.17112 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d853b55-4da4-3d32-964a-46a92661a1bc | -6.4278 | -43.06968 | 2026-08-20 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e956f46-3b7b-3798-9e0d-cab59e0b14bb | -7.96493 | -44.66139 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 33823652-4fae-3109-b64d-a0823df96e4d | -7.95856 | -46.91992 | 2026-08-20 04:00:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97f19bca-6768-38cc-8196-93107f3fe8d0 | -9.93037 | -37.29113 | 2026-08-20 04:00:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d94f682-1b2d-35ac-87b1-1eece81d0a41 | -5.84097 | -42.63452 | 2026-08-20 04:00:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 498443bc-6aba-3b93-97ab-ee41e743f3d2 | -8.35914 | -46.33916 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 625884c8-93a7-301b-85ae-9448f82f13ad | -7.96788 | -44.67214 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| be7af902-7c51-3ade-81b4-13633af0633d | -6.78031 | -42.8817 | 2026-08-20 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d177cceb-bcdb-3749-b0dc-3840bd8b3c75 | -7.96315 | -44.6713 | 2026-08-20 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c365bd00-2dbb-39e2-ba32-72c2b7f571d3 | -7.01907 | -45.89091 | 2026-08-20 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac2e02bc-0a4c-3a0a-8300-cd5f14a79f78 | -7.61704 | -45.15836 | 2026-08-20 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b851653f-155a-3cf6-9695-a5263ce050f1 | -7.34141 | -45.83628 | 2026-08-20 04:00:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b51170a-09b7-3bbf-ad0d-f7b2b8db9d18 | -5.42525 | -43.43829 | 2026-08-20 04:00:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68837c49-4b90-3ec1-848c-c0345c306d80 | -15.37874 | -52.73282 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e3edc51-7320-3601-a774-7a7bfab3e0b0 | -11.31955 | -45.20642 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98145281-4166-3f8d-8f12-c60b0a24ae90 | -14.03539 | -43.85182 | 2026-08-20 04:02:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7918f7b4-bb82-3e2a-a2cd-b744d3992b17 | -13.43934 | -43.84621 | 2026-08-20 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08566403-140b-3ccb-8792-f9a65518fdbf | -15.36923 | -52.77543 | 2026-08-20 04:02:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 981d685b-1ba8-368b-9cbf-0fcd737faf60 | -14.19811 | -52.88787 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8668d0ae-a79d-3112-b3d8-9927b4c3e65b | -14.44937 | -45.61536 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 32bf6441-9e34-3c45-ba7c-7cd6e3b7cca9 | -11.80995 | -44.81424 | 2026-08-20 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ba27497c-7cfb-38cb-ae17-52c8c06a04d5 | -13.56553 | -51.66925 | 2026-08-20 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0845f895-706d-3493-8028-4e5a20f0c19c | -15.58925 | -43.73947 | 2026-08-20 04:02:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c12603e7-8649-3920-b64a-f135d0b1f7b6 | -11.31543 | -45.21238 | 2026-08-20 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77be9a1e-0852-35ed-a151-f690e187c01f | -12.84427 | -48.42642 | 2026-08-20 04:02:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df058a77-9ef2-3b17-b513-9251b25def2e | -15.53036 | -40.85619 | 2026-08-20 04:02:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 234f30da-c3ec-3cca-b694-8c639b4ab7dd | -12.1427 | -48.26402 | 2026-08-20 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10ff9249-287f-30f0-ac4f-eb5312812541 | -12.84504 | -48.42251 | 2026-08-20 04:02:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbf0f799-8630-3015-85c2-aa2f06eb41ab | -10.74262 | -50.36033 | 2026-08-20 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16f3530c-4525-316e-aea5-1ff16f319312 | -14.20503 | -52.89003 | 2026-08-20 04:02:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d980131-b46f-3725-906a-24bfa018def1 | -14.44764 | -45.62462 | 2026-08-20 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README26.md)
