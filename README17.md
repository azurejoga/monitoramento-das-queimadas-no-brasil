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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa5d39df-2fd3-3fe8-99dd-6a8a68e8f270 | -8.50233 | -46.21724 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e4bc499c-a02b-3f18-b594-c45f6f69bc31 | -5.41894 | -41.34378 | 2025-10-09 03:57:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b34273c3-94cb-307b-9bc0-347920c8e4c7 | -8.53247 | -46.21141 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fd18c6e7-91f7-3147-b570-b3c59900936c | -9.21887 | -47.84495 | 2025-10-09 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb4c3778-a9d0-3e16-8b2f-0d1dc8daae8a | -6.20831 | -44.06477 | 2025-10-09 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b76f6f76-fb60-38ec-b216-f81ccc86165c | -5.39197 | -40.9813 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7b4bdc9-3234-30f6-a959-69ca36c96018 | -8.54663 | -46.21368 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8ad04278-cbdb-326a-90c4-cc55182622a9 | -4.25527 | -48.56724 | 2025-10-09 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbdf30d-d3f6-3676-9ce8-06ad83d594c4 | -9.29757 | -40.23632 | 2025-10-09 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38ede675-cdda-3a34-90e2-123320c7bbb6 | -9.09129 | -47.95292 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0f7a222a-754a-38d9-933d-2adcfff31593 | -8.50704 | -46.21805 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| d9b073bf-3322-3e6e-b7b9-6f64d4ce00ec | -7.734 | -42.39992 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63e8cd5d-4644-3d7d-9300-238d82bb4137 | -6.69116 | -46.30296 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| d9b85e6f-3dd8-3335-8aae-e4d43d35c488 | -4.89268 | -42.25262 | 2025-10-09 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d260a71-eadb-36c6-9560-2cd1a271bb67 | -8.22412 | -44.15624 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2550dd59-e12e-30f6-899d-4f1a866374c2 | -6.69207 | -46.29763 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6d7b7b3d-fe53-30df-ba34-b9b7b419c5a0 | -7.0223 | -42.75282 | 2025-10-09 03:57:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8660ef9-e7e0-3578-98da-86a880151577 | -10.0946 | -40.77544 | 2025-10-09 03:57:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84461758-dad8-3dd2-9886-18b39fd4e7ba | -4.81506 | -46.82044 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e301e79f-602e-31c9-9293-85beb76d1a09 | -8.61148 | -45.10382 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff2ea001-54d7-35fd-83b3-bf285397b42b | -6.6915 | -46.30968 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c4d3293b-3ae6-3551-8b75-e42a0437f400 | -9.08554 | -47.95767 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ad810b69-114d-36b1-a7f3-47959474b126 | -7.15659 | -39.43188 | 2025-10-09 03:57:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eff40f3e-3034-3074-a1c7-14a15fc106c9 | -3.11036 | -47.8 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ae0efc4-0a7c-30f0-bc59-8eae69a084c5 | -7.78126 | -42.41937 | 2025-10-09 03:57:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ea59337e-8039-33b5-aa9a-89dde4b0dea1 | -8.17639 | -43.32227 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f083b0ad-3c6c-3467-b5b5-dcd67ac13134 | -7.0854 | -40.61387 | 2025-10-09 03:57:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fcc542b8-4dba-33c0-9a36-0506176d50ae | -7.692 | -42.9645 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34f6900e-d0c5-3445-a9de-0fb50ddfefe1 | -6.74458 | -42.83564 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| c0db23ce-4cc3-3935-b546-0b7bd1800148 | -4.44383 | -43.22787 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a8dd80b-dedd-3735-b8b1-fe0fd667d65c | -10.19967 | -44.56748 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af482c97-0028-337b-a5c6-373417ac546a | -8.54272 | -46.21592 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 064379a7-13d2-3f59-a52f-cc9dc0b9052a | -7.48678 | -43.08494 | 2025-10-09 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7acf5a16-4466-3211-9742-3486431a3f6a | -9.0861 | -47.95455 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f2bbb8e-657f-37c6-89cf-72f9a23bdb88 | -9.17101 | -40.30848 | 2025-10-09 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8811c310-c38d-362b-8983-a640ce072059 | -4.89468 | -42.25122 | 2025-10-09 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c903f8b-3fcc-3e55-99bf-46413f9350dd | -9.16109 | -41.0568 | 2025-10-09 03:57:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 49af11dd-abfd-36c6-bd4c-cc71942003b1 | -5.54868 | -41.30447 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7f261930-bd9b-37ed-95b0-f685efe7b22e | -4.84304 | -42.77722 | 2025-10-09 03:57:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06c8b48c-21ee-3b40-adea-122d2865b848 | -10.18583 | -44.54984 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03ec6436-68e3-3984-b458-98b2a93936c0 | -7.76452 | -44.04069 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae7b2954-c1d2-33c0-8c49-c6ea477c21e3 | -5.40135 | -40.99121 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 467c46a4-505d-34b3-b094-068200529b3a | -4.71847 | -42.94979 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9945ff2f-e051-3f9f-8e08-7dab5641f005 | -7.75823 | -44.02796 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f3ea973-0ea7-37b1-8c82-3181490f2358 | -6.69341 | -46.29893 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 80ddfe3e-8c8d-3b37-8cbb-de3b077b93bf | -6.68853 | -46.29806 | 2025-10-09 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 25194bb9-daaf-30b2-adce-5326f6fd27bb | -5.48275 | -42.90467 | 2025-10-09 03:57:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 18ecd0ea-8401-3c23-be00-1afc811a3707 | -8.52951 | -46.20845 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 003359fe-d5ef-3cfa-967b-d07bad090cb9 | -5.35949 | -41.00099 | 2025-10-09 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 580f68a3-7e90-3ab0-a26a-cb484af49431 | -7.25827 | -42.96747 | 2025-10-09 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e5f8de08-e656-3b71-97e3-314dccbdd91a | -3.85416 | -41.53488 | 2025-10-09 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 952eed0e-4594-3946-8d01-f116023d951b | -8.49114 | -46.22559 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 19217b87-f0ee-3ef7-b419-258597cf5032 | -7.24637 | -43.98489 | 2025-10-09 03:57:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7590560c-cbc7-3485-94d8-aa9d0c583541 | -4.77122 | -45.59497 | 2025-10-09 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0915e0ec-a173-39b7-a4c7-9ebca252e10c | -4.45328 | -43.22191 | 2025-10-09 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cc0ffa3-3102-306b-ae67-e3a97dbd1638 | -3.55836 | -39.10847 | 2025-10-09 03:57:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bdeb18cd-a073-3c92-9623-3e9e658e711d | -8.67396 | -47.07596 | 2025-10-09 03:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8a47c9e-8dc0-3f9a-9541-5cb4e45a4d45 | -4.82045 | -47.34424 | 2025-10-09 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cc4209b-5d9b-3d6d-9df3-7b0ec9255617 | -6.27576 | -44.30065 | 2025-10-09 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f089ec4-cfd0-3442-b149-1feac38fcb55 | -6.64976 | -40.87882 | 2025-10-09 03:57:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ddf2426d-0cbe-370f-a05d-421ec14bf4db | -9.09021 | -47.96181 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3067669-8fef-3181-a281-a9f6a09dd8de | -5.47181 | -42.19843 | 2025-10-09 03:57:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f3f64a6e-8b2d-3577-90b7-0811bc7b2467 | -7.73326 | -42.40437 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e26845a-f6ff-3328-897b-301e5884f384 | -7.76866 | -44.04129 | 2025-10-09 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e82f6a71-1eaa-3fee-a726-6696c254e78f | -8.62757 | -45.1394 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1df57d-cad9-3b70-9f3b-3069143095f3 | -8.54835 | -46.21162 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce55b240-85b8-3cd8-8b96-ed8b6ace420b | -5.14217 | -44.96307 | 2025-10-09 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5408a78-04b3-3b33-97fe-9e72fe376614 | -7.8437 | -41.34469 | 2025-10-09 03:57:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 646aa869-9b4d-35ce-a198-0e5bdd77f047 | -8.59457 | -48.24712 | 2025-10-09 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fe6adba-9d10-3642-8e77-af0528ca46b8 | -8.53422 | -46.20921 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2999711a-4a62-36e2-a0ba-64076154c4ad | -4.37515 | -46.75507 | 2025-10-09 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 550f58a8-1912-3648-80e4-ce6bb50d5f3a | -7.28623 | -41.97355 | 2025-10-09 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dae6b5d8-71ee-3056-97e5-3ed1e989afb9 | -8.54493 | -46.22348 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 215e08e5-1b97-3739-ae19-ff7cc052eac8 | -10.02945 | -42.31452 | 2025-10-09 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 87a012bf-0de8-3a15-bcf8-8a09583b457a | -6.50996 | -44.15014 | 2025-10-09 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e461ebc-a1ce-3959-be2c-12fa864885e6 | -9.09189 | -47.95244 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49fc8b55-b3ff-352a-a41f-a77487fc4a81 | -4.80984 | -46.81955 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8d3a862-745c-32f4-b175-b96afbcb80c4 | -10.19055 | -44.54697 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 719f3989-e4fe-3514-a2d3-497cded62f43 | -8.18972 | -43.33695 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 1a308361-c6ea-346b-9a71-be2d54bde484 | -9.7917 | -47.75115 | 2025-10-09 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7c08c22-1988-355c-9860-93c34ee63257 | -7.05537 | -37.69051 | 2025-10-09 03:57:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7c1346c7-7a30-3281-ace3-7eae22b3d315 | -4.60692 | -43.15011 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af35109b-622c-3db8-9854-fd518a37c60b | -7.90833 | -43.17539 | 2025-10-09 03:57:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e14067f-73d1-39e7-b634-4cd21c5c3359 | -6.7312 | -42.22418 | 2025-10-09 03:57:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 46aa7738-d154-36e0-a9fb-4a746fff479d | -8.61075 | -45.10808 | 2025-10-09 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b29720c-dd09-38f8-8fd7-e9eb22876591 | -3.10528 | -47.79503 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b266aef5-8afc-345e-8b75-ca42ac26948c | -8.67166 | -43.91861 | 2025-10-09 03:57:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d1db832-1700-33a1-961e-8d0a2c09a382 | -3.56763 | -43.51373 | 2025-10-09 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c14a718-8c1b-3837-8e91-784849e874b0 | -7.63652 | -45.2312 | 2025-10-09 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae0f3a2f-8504-34db-a985-7bc4be59b2e1 | -7.68024 | -42.40031 | 2025-10-09 03:57:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2a12f617-64a1-380d-919a-5cd5f97c28d8 | -8.54928 | -46.20646 | 2025-10-09 03:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48818b2c-89ef-3ccf-9e69-200a74ed49b2 | -2.37756 | -47.71368 | 2025-10-09 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b008eaf-8e91-3eaa-8224-6630394e1702 | -4.61042 | -43.15441 | 2025-10-09 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13785a0f-b673-3a03-a2b6-c7650b40004a | -9.09012 | -47.95916 | 2025-10-09 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 59b1273d-2c93-3690-8250-69b55b69a28b | -10.19338 | -44.555 | 2025-10-09 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 450b4c26-b112-345d-aa46-d744e9a358be | -3.09779 | -47.02318 | 2025-10-09 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb0b01a6-538e-3c96-91f8-b1a4f2cb3504 | -8.18274 | -43.33067 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 805d4972-7882-3c28-8882-d2d8f5d38f39 | -8.1967 | -43.34322 | 2025-10-09 03:57:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 52766aa7-681d-3030-820e-ca52a12f553e | -7.9939 | -44.4672 | 2025-10-09 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed663cd0-8c21-3158-a43c-3d54a376d81f | -7.52765 | -42.72784 | 2025-10-09 03:57:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README18.md)
