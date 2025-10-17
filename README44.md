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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b697cc-d148-3cd2-9647-59fe7eeb00dc | -7.17614 | -46.93827 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a24cdaf8-094a-3b5e-b139-f0c88bd30d51 | -5.87096 | -48.25967 | 2025-10-17 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba23231a-6464-3797-86dc-f94e86c03b05 | -10.57003 | -47.42633 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a070f405-4baf-30df-8fe6-6a7da6edd6a7 | -7.69666 | -49.54986 | 2025-10-17 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcf4bcb7-b35d-3739-b167-95712cd4136a | -6.95457 | -47.71951 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb33863a-5aba-33a9-ac4c-55c730a1333a | -6.46227 | -39.42918 | 2025-10-17 04:19:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39151808-74e7-3f55-9162-bd2930173167 | -10.50445 | -43.43474 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cde0a8f0-1b1d-3395-a3ad-18ca28a3cd6c | -10.50897 | -43.40481 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdba9b84-5a16-3bc6-b7fb-8c28ab431148 | -10.52969 | -49.55098 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 20ff7f80-430f-3505-9221-b2fed0123169 | -7.46082 | -42.67072 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdd4a14c-108a-3df6-8e8c-f58df06d64fc | -5.87682 | -43.85712 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1908176-57b6-36c3-a578-7d7421072598 | -10.50609 | -43.40055 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 880ab0df-d3a2-3727-a0b6-d2af33be9369 | -8.25853 | -44.02779 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c32f726-a99c-31be-a1e1-2b611f273e3c | -9.65212 | -48.71845 | 2025-10-17 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4627648-931c-3209-be97-f0e0ceca6982 | -6.44766 | -42.52833 | 2025-10-17 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef618477-283b-3b3e-83a7-76aab506e545 | -8.70264 | -46.97556 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c113e0e-eec5-3a59-ae79-def3f43e5d61 | -9.29008 | -46.90498 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff90ee79-a867-3b49-ba5b-a9bee76c65bd | -6.29509 | -45.53131 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59336d62-dd76-3de8-b8a6-b142afd9ee21 | -4.33031 | -49.45795 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 526073c7-6f24-30c2-b230-ece9f97ab011 | -6.20142 | -41.73443 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e3073c9-27fb-39e0-8f8e-4b9e4287db7e | -9.34956 | -46.91074 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ba60417-e6f3-356e-9e11-bcced2fcbbdc | -9.26709 | -45.27031 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfe87067-1e46-3e28-b35f-df7f63584c58 | -5.28731 | -47.92719 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b36adfe3-53a8-3d96-95af-324ee50dfcbd | -3.50613 | -52.49019 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1d1b81de-cf38-35bb-a086-1b6e636febfe | -3.33231 | -50.10513 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dd2a238-d23e-38b6-ad54-f448fbdce41e | -11.37894 | -44.18835 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85d690dd-f01d-3f2c-89a5-93bd0bff12ff | -8.17971 | -47.03603 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fe669c5-f7e7-38c2-b4e1-b79d1de1b503 | -8.09033 | -45.41516 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ede5c2d-986f-3c0c-b940-d1a4d4b09e3e | -8.45216 | -46.24559 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57ca0092-13fc-3bc3-a531-747128d61187 | -5.29209 | -43.54841 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4206c7e2-7f9d-3d37-abf7-fd54d32e935c | -10.58232 | -48.64505 | 2025-10-17 04:19:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6aa6ef5-d63f-30f7-8e3b-57d7c0a737cb | -7.48694 | -44.66021 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4cf3b50-f5a0-33ba-8834-99672ab0d4da | -5.41802 | -44.24854 | 2025-10-17 04:19:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 943d0b18-73c0-33cd-b89a-ca7c5054479a | -4.2595 | -48.55326 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0eeaf3d2-158a-3b52-9e07-01d47c221072 | -6.09403 | -42.38803 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ad162a5-ab52-36d3-9da1-85159dfe0dcc | -3.05958 | -52.65651 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65281657-1574-3b25-a077-2e468a6817b7 | -10.13705 | -44.57067 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 189fef72-9b88-3eb4-b7d9-8d62844668fc | -7.07505 | -44.24792 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfea5a38-0124-3a01-a6b3-431e0c593697 | -9.71317 | -44.4972 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d636e8c9-94be-3e75-9598-0cf17c672888 | -8.06336 | -45.41453 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bb88207-fdf0-3c9f-920c-8b4fe5b9c5ec | -10.58144 | -47.42056 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac498fe-ccf9-39f6-a515-e79b55849ab8 | -10.64629 | -45.30239 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b134efe3-4de9-326f-a722-a0c8927e9858 | -5.68467 | -42.67779 | 2025-10-17 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2ca6f9b9-bcdf-3664-b835-c3fdc149f74e | -6.91006 | -44.08289 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d95c67ff-1521-3805-8ae6-62fdeb950c88 | -11.39139 | -44.20848 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c2ce31b-7d2a-3bbf-98d4-9c91ae83f03c | -10.01753 | -37.38916 | 2025-10-17 04:19:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40ac0df3-7ff6-32cf-93df-fed4107a0220 | -5.71533 | -46.51675 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa7ccec-5a58-3b06-a132-634ecd5961d8 | -11.28281 | -44.03747 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece02f45-1f23-3c57-acad-922c5fca3946 | -6.715 | -44.37558 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf8d1ce5-e0ba-3b0c-bc2f-87616b4a95dd | -2.87612 | -50.74371 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b76b43fa-57f8-3338-8a0e-a1873eb05ec9 | -10.27515 | -44.02359 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c54336c0-6876-37ba-a8bc-b5295b26c7e1 | -10.10356 | -44.61256 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c334e49e-4c18-3c44-b986-f9b8a1bf3adf | -6.20729 | -41.74352 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4d6aec13-ee50-323a-9ba8-afa173edc2ce | -8.45336 | -41.26521 | 2025-10-17 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 489206df-2986-3fc3-a644-36f6944e1618 | -6.23664 | -41.54264 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 994c86e5-9c86-30f8-b9a4-a9e82d8bbb0b | -5.17003 | -42.92612 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52344cde-a12b-35ff-815e-b5ab2ddad505 | -7.6656 | -42.56744 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 991a39a2-23e2-3bfa-8c28-53431878a6ad | -6.45465 | -43.88361 | 2025-10-17 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 412d7c8d-9721-3739-bb16-82f3f9447365 | -10.53264 | -49.55619 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d576b70b-d789-377a-bb04-5c27c2274464 | -4.42549 | -47.75565 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 837122eb-9d93-3e77-b2fe-6faf92adb266 | -10.13161 | -44.54108 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 857668cb-5a67-326f-9992-89c5aac006ea | -8.45016 | -44.74564 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1838a080-3fa6-3950-a301-f38ae81261a0 | -8.73169 | -43.86787 | 2025-10-17 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4742ccb9-2c47-308d-a91d-98a0691bf95a | -9.15694 | -46.62655 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b169f34-b3c9-36f9-af01-cab9fc8fd788 | -10.06824 | -48.32986 | 2025-10-17 04:19:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e28688d-c0d9-3267-97ce-b1004b60ed5a | -8.46042 | -44.17513 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 115e71cd-958f-3d2e-8712-c117501a5d1b | -8.40969 | -46.27896 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d7a3d1b-38b5-34d5-9f64-91664349d70e | -5.35877 | -44.82058 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d0fde5b-0df2-322d-9fd0-48c11efeea3c | -10.27183 | -44.04544 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6de6ff78-cad0-3df5-b04a-1960862315d8 | -5.87899 | -43.91093 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f41dffed-4ea9-3991-9858-063266fbe763 | -8.31786 | -47.86572 | 2025-10-17 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebcffd4c-7347-3442-a51a-83ddd09ee81e | -8.18924 | -44.10378 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9122d862-724a-36ae-a821-1627d3548b68 | -5.17779 | -42.89791 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a77d3cd2-f9c6-329e-85c3-9831950d6595 | -5.57635 | -41.31736 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da669a9c-76fe-3b25-9690-834283b6ed67 | -7.05494 | -46.68578 | 2025-10-17 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60eea8a6-72c9-3914-931b-b7c258a8e58c | -4.36847 | -44.77678 | 2025-10-17 04:19:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ba8dee-1560-3688-adca-42147cdc2257 | -3.86624 | -50.04855 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f401987-355e-3394-ac05-fe991bc9d04b | -8.07382 | -45.41261 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc312fe0-c892-32fb-b4b0-d660141af88f | -7.62198 | -47.83587 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd0b5df5-b034-3948-ae1a-668500c42c7c | -9.14005 | -46.65331 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5f0e4fe-f910-3cb1-9aaa-31a16cc3de7f | -10.28414 | -44.03249 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e72314b-4b59-35cd-b077-57d34ace7c9b | -8.29736 | -43.39774 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ececbbc6-668f-3066-8839-edcd4ffb4992 | -10.6766 | -45.32862 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72c1b72e-6d9e-37a1-820c-4afd52d00fe4 | -6.22555 | -47.03975 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1da792cd-1825-33da-be57-16e7e613d4ea | -6.38847 | -44.63461 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dc75488-83d8-398c-8002-a6f5b5044ae6 | -10.29199 | -44.0262 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 45336128-99f9-3ae3-b4ce-e11c271fa84e | -4.41058 | -43.39684 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7340e37f-b98b-3e4d-86f5-09483cc16c4a | -5.29872 | -43.54944 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 303a4548-bd7e-322e-af8c-ddf23ea1e00a | -6.16837 | -41.71297 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 639412ec-47d6-3819-8a0c-96597cec8cbd | -9.84022 | -47.54675 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cb69f46-043d-3752-9741-75c8ba1b3621 | -4.36516 | -44.77626 | 2025-10-17 04:19:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 748af8b0-6892-3f5f-9af2-04694249e7c9 | -6.69356 | -40.87773 | 2025-10-17 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fa47c202-fb6b-38c9-9905-ed853c2006c9 | -9.24336 | -44.36914 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f00d3167-deb2-3b25-bdb7-d3a75f47493a | -7.46307 | -42.15786 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0424a469-f988-37b1-8ea2-8a8a631addf4 | -10.13858 | -44.53843 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9feb0b-4366-3191-a5c6-f0623a5b4ceb | -10.66282 | -45.32648 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3a05d80-af82-3289-93cf-cd068665f025 | -9.64479 | -47.12786 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7148a3d0-fbd3-305c-9c4d-85e3d2c3a305 | -10.51078 | -45.03738 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b8ea391-6ba8-380d-9b28-3c3bf7a214c5 | -6.1931 | -41.74137 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5dd56a16-ae06-3ca9-a9f6-bc29d53cb1ef | -7.17269 | -46.93781 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README45.md)
