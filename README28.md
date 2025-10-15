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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c36f764-1641-3b5a-b99a-6656c48fad08 | -6.02654 | -43.39451 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c4f6ae-4820-3243-98f9-6966a3e38e7e | -6.23063 | -44.16758 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3416ba3-343d-3ea0-9120-f86bf9be58b7 | -8.21215 | -44.0197 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e88e0633-3ff1-36c5-bfe1-44e144cc4655 | -8.48692 | -42.59565 | 2025-10-15 04:06:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 464eebd4-f012-378e-aca6-7e6190afe7ef | -10.05682 | -42.61538 | 2025-10-15 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b66e1a8c-c9db-33d4-a3cb-08606a4dfff4 | -7.53857 | -43.92989 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e450e1d-930b-3660-96c7-1e30b7d0d11f | -4.30744 | -48.23925 | 2025-10-15 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fcbc6c8-1517-3ee0-a1ec-5ba684d9ba8d | -5.43755 | -44.22812 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 11fa6487-7f21-3af8-a881-05f8330ac9b7 | -6.06643 | -44.5289 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a2ac463-3d91-3e1f-a22d-a3f1f888c213 | -8.2594 | -43.3598 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82c0c223-4afb-3422-a144-55fc26da0162 | -5.15449 | -45.69716 | 2025-10-15 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11d787d5-7f26-3ec6-9597-2daca89548ef | -6.14237 | -41.7623 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 901bf6b9-f41d-36b1-a3ca-f7673e8d89d3 | -8.05923 | -45.91941 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 423173e6-d6f3-308d-81b6-6952ecebfe55 | -5.90808 | -42.82423 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3d50acdb-ea2a-3de4-abd0-6a89a64ff13b | -6.14016 | -41.75484 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8a938909-8b4c-3db0-a776-bdc118422d54 | -5.85828 | -43.87291 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 653dc5ef-753c-3ee9-96a7-3ab56d3d9612 | -4.8816 | -45.94054 | 2025-10-15 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffa7e6c2-67ad-37a2-82cc-d25906dca4f9 | -6.41244 | -43.58735 | 2025-10-15 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73b90dcf-bd49-3d10-a6e2-27d6fade9f2e | -5.00351 | -44.49899 | 2025-10-15 04:06:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42dc36ca-b18a-3d78-8086-6ff5428006a2 | -8.22132 | -44.0726 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 513fb095-2a62-339f-ab1b-27c466e960e9 | -5.87892 | -42.78965 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e41f4d9f-6b9a-3b88-a110-2f723220e70b | -8.25998 | -43.35612 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 462bf16e-327c-36c0-bce2-d8dc5c06429c | -6.25065 | -44.02273 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 646d92e4-5f7b-379f-b766-60a49a26e5ab | -4.81362 | -43.21389 | 2025-10-15 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96695289-0b85-3c44-9cc2-b08c391273b0 | -9.25804 | -44.36145 | 2025-10-15 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb8eb326-10ee-333a-af16-9ef2b86d7b60 | -6.22276 | -41.55503 | 2025-10-15 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 82fbc3ee-9408-399a-9b27-2d1d0ffc1ce3 | -5.47427 | -44.64279 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4b55d5a-52f4-335a-893e-0014528be2f5 | -10.16259 | -36.17817 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5245cfb0-4d9a-30c2-8eaf-aee1cbef83b1 | -5.95024 | -43.75373 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3433b08f-d733-3c0f-be8d-91446875b8dc | -5.31987 | -42.92761 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f1733cb-d24d-3b57-965f-8c27e7b06e77 | -5.40599 | -44.23995 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eacf906-e70c-370b-9a94-ebf8a09fe479 | -4.9305 | -40.13961 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 90e0b47e-f72e-3300-82e1-a3b0d8cdd743 | -7.2939 | -41.95671 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 29511f7c-b301-3c58-ba27-b3212e64a4e1 | -6.41111 | -42.57172 | 2025-10-15 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 625b2a96-f9cd-38cf-8f92-3f35d1c1e7f3 | -8.20994 | -43.32169 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6a9af772-1006-3982-8155-c477fc5a120e | -10.16861 | -36.1663 | 2025-10-15 04:06:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c71cc4c-2f84-38aa-8a50-03a97a983049 | -5.95734 | -43.17234 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a36301c2-43d7-35ee-86e2-85cd430897da | -3.67182 | -45.22661 | 2025-10-15 04:06:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e9966d9-58ab-3d9b-a34e-24d27ecf3b3a | -7.28673 | -41.95913 | 2025-10-15 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 33bdb7fb-de9a-3441-8a97-90181b0d4b3e | -7.55455 | -42.06935 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f9f8d5b-0acc-3f24-9bfd-5fd6ba219efe | -6.17338 | -44.29269 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 486db58e-4b89-3681-afb6-1ff3d6215485 | -6.05393 | -41.89053 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3c8d9ea3-cf62-3318-92f3-5435f48c3e21 | -8.17965 | -44.02247 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4497393-2580-3e99-8e23-d162b213f2be | -6.45098 | -44.58549 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bcf64e1a-8817-33e9-9dc6-f722697595ed | -6.14348 | -41.77668 | 2025-10-15 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa3368b8-658a-3f45-9b9f-e78a189a5581 | -8.72596 | -43.86116 | 2025-10-15 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ddc6c09-da42-3dab-9f4b-bcd852aac6f6 | -8.22291 | -44.08476 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad57d454-b1ae-35e5-ac7a-3b19167e5cae | -7.54744 | -42.70964 | 2025-10-15 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b954a76e-1ae7-3b96-a19e-64d88d58e161 | -6.05614 | -41.89801 | 2025-10-15 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ddb99aa-fb03-341a-9b0b-747e72551338 | -8.20616 | -44.07806 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd083310-7476-3f7c-a40e-59c023f1f609 | -5.86566 | -43.84966 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35e098aa-ba10-37d0-a860-ab473e871b0f | -9.34158 | -35.50331 | 2025-10-15 04:06:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee2eceaf-26ea-372a-8ef8-9bc2bc71f033 | -6.59274 | -43.92494 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a995c1c3-39d4-3747-a430-f60588e0b030 | -5.25105 | -44.47432 | 2025-10-15 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 968562a0-0f93-34b5-8a70-26831928cdf1 | -7.9531 | -44.14178 | 2025-10-15 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df9d2ad8-4446-35bf-8933-e6c1df1862a2 | -5.43327 | -44.23166 | 2025-10-15 04:06:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5fd32b04-0ef5-3753-bb7c-b510984020d1 | -6.20285 | -44.31495 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64a4509b-bc7f-32be-84f4-95e59454c836 | -4.43691 | -41.93234 | 2025-10-15 04:06:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94adcee3-0398-35cf-bd40-41084ff4e6e5 | -5.02188 | -50.00068 | 2025-10-15 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc0139b-88cb-3163-a790-3dbd6b25eb52 | -5.56307 | -42.98521 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ff4f02a-2f16-3836-99ca-62d879e00959 | -5.88636 | -44.23308 | 2025-10-15 04:06:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e3e7536-0282-3407-a36b-a37456f689ae | -5.32684 | -42.90614 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfff11f5-fb7a-3448-8cdc-c17586f68fd6 | -5.87362 | -42.82241 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 14aedecb-6c06-3904-bc79-2439236e3a43 | -7.15887 | -42.50584 | 2025-10-15 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49f78be8-fdfd-389d-a587-fc45a3730cff | -6.059 | -44.08827 | 2025-10-15 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bed5412d-5d18-3d11-af57-38ad8223afcb | -4.20234 | -44.7056 | 2025-10-15 04:06:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 856630d2-1c0c-36bf-9c99-b1f93ff16564 | -8.1766 | -43.95479 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9486e91d-6b83-31a2-9b05-149c9096326a | -7.00236 | -41.99545 | 2025-10-15 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e5a754d-341f-331d-a5d4-04d7aa22e05a | -6.17268 | -44.29692 | 2025-10-15 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 009554ea-ee2f-3111-851c-4c65c07c09a4 | -6.58349 | -43.91541 | 2025-10-15 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e68f6f1c-82cd-32a5-a833-966ebe38c926 | -5.718 | -44.4159 | 2025-10-15 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05d2d6fa-1ebb-3661-98dc-14b39d7d56c8 | -5.5989 | -46.24646 | 2025-10-15 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3dc022f-bbfa-3191-94a0-496ee50f7be5 | -5.48288 | -43.92946 | 2025-10-15 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36ade1dd-923c-3ef8-aaae-b5b633d1ec5a | -5.63152 | -42.68823 | 2025-10-15 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd2e9e28-150a-35ee-848e-97477237112d | -7.79493 | -46.02086 | 2025-10-15 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e7f98d7-d4b9-35b6-8a6d-b361f63d1092 | -5.57692 | -44.74769 | 2025-10-15 04:06:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41b46de4-58ae-31a7-83fa-242baacbc5be | -8.2765 | -43.41079 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b387621-d2d8-3ecd-88c7-5b09ae54b660 | -5.88288 | -42.78659 | 2025-10-15 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 775be444-91b4-324e-9736-c608278d83d2 | -4.98093 | -45.38016 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79f2ecc4-8701-3465-83d6-331af85576d0 | -5.40861 | -40.88139 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 293306e9-a710-3db7-8c1a-e518ec0772ad | -7.50202 | -42.14308 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4bc7a12a-5c1f-37af-b2e2-22c0e3cfc174 | -8.28273 | -45.40396 | 2025-10-15 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff826dbf-63d5-3c6a-aaa2-962c1f69827e | -8.27949 | -43.39249 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32e649ab-5227-3e69-97dd-bb221959ab25 | -5.28683 | -43.2408 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93778acf-08b0-3d09-9a3d-e4dd5eda572a | -8.28549 | -43.41972 | 2025-10-15 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02bf14d7-2ba9-3272-a1cf-b40e495962c3 | -8.46242 | -44.1909 | 2025-10-15 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c664bd1e-20a1-39a1-a092-e13a4ac6e857 | -2.94616 | -49.34036 | 2025-10-15 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd914761-eafc-31d6-b4b4-da4964fbe835 | -8.19074 | -43.97676 | 2025-10-15 04:06:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3cb3482-afd2-305d-958e-32d7bd9993e1 | -5.31764 | -42.91975 | 2025-10-15 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c17cd0c-61e6-3e1d-98e9-7e36104f782d | -7.16284 | -42.18226 | 2025-10-15 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8b2e4ce0-86b3-3f4a-831d-176ee959e690 | -7.56701 | -43.8436 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| deeaedfb-1166-36d6-9694-7ac47c7a64a2 | -7.56637 | -43.84749 | 2025-10-15 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 12c7ac87-8a70-30b8-a329-8c29bf41627d | -7.49926 | -42.13907 | 2025-10-15 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 871685e6-e808-3406-8424-a73a94f32553 | -5.43728 | -42.71722 | 2025-10-15 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 88cf736f-7048-39c0-9e9b-2d2d7f40f5b3 | -5.5736 | -43.0288 | 2025-10-15 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8a65c414-f3c0-35e7-b135-2886b6e4aff5 | -5.85956 | -43.86503 | 2025-10-15 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2e5f18f-ddd8-35b7-8898-7c49bd11c4e7 | -6.35415 | -42.6692 | 2025-10-15 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 642b8b2d-a064-39b0-91cc-16c7257c7ee0 | -4.13986 | -41.66236 | 2025-10-15 04:06:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e9338e88-fa7f-3117-9801-f24c40f3c12f | -8.73251 | -43.86098 | 2025-10-15 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56a4c0fd-680b-3949-8c4c-406590bc9105 | -5.42536 | -40.66479 | 2025-10-15 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |


[Clique aqui para ver as próximas entradas](README29.md)
