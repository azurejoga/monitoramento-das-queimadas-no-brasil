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
| 653e1257-d8ed-36ae-8441-5cf48932ae30 | -6.13384 | -41.74165 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c32d5db2-4ca5-352d-929b-3ef9d557b76a | -7.05592 | -45.06251 | 2025-10-17 03:28:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73fc1602-3789-3f59-81fd-80d8979215df | -8.23867 | -44.02486 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 223fffe7-1537-3d2e-b46c-4c522d5c958f | -7.04104 | -42.74083 | 2025-10-17 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c459a95-80f3-3177-97e5-ede883922c8b | -7.46082 | -42.16278 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c23d1081-ec61-300a-88e9-977e4e3cbfbc | -7.28053 | -41.95593 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4f0b304-547c-3660-9acf-40d934af2e55 | -8.30544 | -43.43438 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f3d93c7-1c49-3246-aafc-3d8831bfd042 | -6.3866 | -41.47626 | 2025-10-17 03:28:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bf3e9db0-4a52-3049-801f-86f13ba8b6ee | -7.74627 | -42.50753 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 43fdf8bd-f239-3e7c-be2b-f74fa421b4a6 | -3.97491 | -42.4914 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2115682a-6e38-357b-8c49-ece40ce33831 | -3.97411 | -42.49611 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2918c3f1-7fa0-3132-bd75-e2a942aca8fa | -7.0418 | -42.73658 | 2025-10-17 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff6a7559-c979-3f52-83ab-867892d11598 | -7.46773 | -42.17201 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 86ee6296-baf8-30e2-a291-0560667e86ed | -6.18498 | -42.62066 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d1898e2f-84d0-3f00-a159-6dc26228e019 | -6.81507 | -41.71043 | 2025-10-17 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24a1f890-bd1e-35b3-86e7-8a2f39a22674 | -6.03744 | -41.90576 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 232a56fe-332a-3a0d-8b7c-59516b49fb4e | -8.2604 | -44.08167 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1790b5b7-22a4-37d3-8a45-73732dd7037f | -8.20774 | -43.3146 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e07ba6f3-df65-3b16-9906-e13af9115779 | -6.23819 | -41.54526 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a13b2598-119c-3bba-b3e9-6aa7f2b72e60 | -7.04458 | -42.74181 | 2025-10-17 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2729b5f6-4523-3d8e-a208-8b1b516ab2c2 | -8.40268 | -46.2419 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a71205f-81c4-3199-8a32-6b27367c087a | -8.18797 | -43.32074 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e58b4712-ae7a-3b9e-ac30-55351db8dffa | -8.48218 | -40.60813 | 2025-10-17 03:28:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0519da30-ba2b-3090-b42d-1f57c615fa4f | -8.2545 | -43.34005 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12e57f91-8f96-38e6-a557-68be547c767e | -7.73976 | -42.51055 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 4087be08-bf48-3f9f-8a1b-891244c51411 | -7.16889 | -42.52514 | 2025-10-17 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 275d4561-8c13-3b9b-a366-ff0a29e287c8 | -8.39115 | -46.24408 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 195a6564-11e0-31d2-832f-3d13ffa3dae7 | -8.38321 | -46.32016 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d2dc71f-a1fe-36d2-ad5b-ab5fc186da75 | -8.12314 | -45.55103 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 744bd8a2-8fdb-3a71-959a-374f09675ef0 | -6.13037 | -41.74319 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e724c5d-74ed-3a05-9888-b57f07c9e298 | -7.95062 | -44.15649 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 005a0b4b-d816-30a6-b2c6-6b31e17b383b | -4.40099 | -43.40495 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f10c18ef-32a0-31f6-bece-d3dba1acf72c | -6.20653 | -41.75667 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d3f72a0f-52b5-3dc2-84fc-199b9dac4b60 | -6.20229 | -41.7479 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e7ed634e-9b1d-3fe5-99c6-9b51949c0471 | -8.5211 | -44.58246 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d8fa2ad-2843-3c6d-909c-761d6546d56b | -5.5274 | -41.33376 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a7ebcf45-e712-3493-883d-c6a8dc4802d6 | -6.35587 | -45.48976 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1b4953c-e057-3ca3-a6e0-05030e7e64da | -5.57388 | -41.32513 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7803072-19fb-370c-9357-d083de12af42 | -7.17977 | -42.36532 | 2025-10-17 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 166e3670-d0f8-3917-8217-5ab06fca2dfe | -6.07363 | -41.9002 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e76e54a3-daa0-3b7c-8389-e2e33ea8b83c | -7.40774 | -44.7582 | 2025-10-17 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c5783d5-0c99-30e9-8075-a3ebda5ff1f2 | -4.00137 | -43.28344 | 2025-10-17 03:28:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f045754-81a0-33af-9c9d-203ed4c2a19f | -3.56405 | -40.52206 | 2025-10-17 03:28:00 | NOAA-20 | ALCÂNTARAS | CEARÁ | Brasil | 2300507 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0a43616f-c452-3c0b-9833-b402f91d958e | -6.0821 | -42.38929 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c55ea6cb-4765-399c-87a6-5166f4ff8f57 | -6.20518 | -41.76432 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1139c058-b581-39b3-b8ef-cfa89ea0b810 | -5.29278 | -41.08347 | 2025-10-17 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9dbee73a-c80b-3d35-bd78-eeaadcb59f9d | -6.99962 | -38.36246 | 2025-10-17 03:28:00 | NOAA-20 | CARRAPATEIRA | PARAÍBA | Brasil | 2504108 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a7cc0a4-4aba-39f7-ad6c-82efcad43457 | -6.31179 | -40.9416 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f280219-fa92-3323-8503-d2d50365444e | -7.68055 | -44.63124 | 2025-10-17 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6504182a-1093-3715-beb4-447071341a92 | -8.29838 | -43.40508 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ed86fee2-93b6-3faa-a740-249d09df09f8 | -8.25642 | -44.03389 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6e2466e-8221-3390-b32f-1752be9a77b5 | -5.51411 | -43.8718 | 2025-10-17 03:28:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b738354a-ad5f-375f-a33d-8dfbc54afdf8 | -5.90435 | -44.75223 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 433c9cbc-c134-30b9-8d2d-a8a198428cac | -8.44833 | -46.25323 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8b1dc623-4cfb-368a-8f6b-ab73871bff65 | -4.41564 | -43.39679 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c0cbee08-9cb3-32c4-ad7f-3e16f574b04a | -5.45826 | -41.01515 | 2025-10-17 03:28:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e752660e-2062-3cd4-8f9a-44ea5f71efe8 | -5.08824 | -45.43627 | 2025-10-17 03:28:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4beaecd-8939-3e5c-ae20-0352f495a853 | -9.15838 | -41.0589 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| e45b77ea-d03f-313a-b40c-939a16d77a40 | -7.90258 | -44.98601 | 2025-10-17 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f7368bf6-4b4f-36ae-8c08-c300984c3885 | -5.8861 | -42.81475 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c8ff8dae-f01c-3a30-b9ea-d908494f4288 | -8.59818 | -44.94448 | 2025-10-17 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff3159c2-b903-3f4b-be9e-d4c2ce0b8ea9 | -8.45678 | -46.24778 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90e42e69-82cf-3ec0-b930-0da8f84d34a6 | -6.32726 | -44.31879 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38871714-10db-3766-a18b-fd961c2ae4ac | -6.03671 | -41.90982 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2a7fbdf-9124-3ad0-9100-6a13f8d481e0 | -5.48961 | -42.16297 | 2025-10-17 03:28:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4cdd9042-ff78-3b94-8557-951a84f660c8 | -3.8496 | -41.57448 | 2025-10-17 03:28:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e05c7a8c-a0de-3239-b8d4-05ae6284314c | -8.26999 | -43.35686 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db0b7e54-f93f-32ce-83b6-7e8e98535a2d | -8.45659 | -44.17953 | 2025-10-17 03:28:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 96b42c4f-6c94-30a8-9d55-5c1b91bc9b34 | -8.37075 | -46.25437 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e70437b0-e7f9-3bb8-9673-bfbc9605b26f | -6.17898 | -42.61993 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c0bf03b2-7eed-315b-87af-3d217f90d6db | -3.62982 | -42.77358 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb8bd812-4570-3b1e-af2d-c80e9cf93334 | -3.98101 | -42.49249 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7683b192-f39f-3cde-81f8-abce9e239bee | -6.22651 | -41.54668 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5a5dc61-3638-3939-aaaa-b9ff23c5f14b | -4.42015 | -43.40876 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| be87fdcd-bad6-34fc-91ef-e88dd8f76fbe | -6.56118 | -42.96171 | 2025-10-17 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53521d06-6177-32e1-bf51-82eae1e1cab0 | -8.23242 | -44.02361 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bb323e3-d042-3ef4-a145-168ad2cc2104 | -6.31956 | -44.32359 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 198d6c7a-bf79-385f-806b-faa50d3ac686 | -7.34946 | -43.85881 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5de8f0f-88f7-3f31-a009-20cc782aa9b1 | -7.48379 | -38.99649 | 2025-10-17 03:28:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 18e3edb0-a706-3a0a-8c87-3a0b1297c189 | -4.9688 | -44.96481 | 2025-10-17 03:28:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3dd6393-470f-3abd-9778-c36a8bc448cb | -8.52117 | -44.57963 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9967b1f6-4e5b-31ac-8dfe-b3830347e511 | -7.56947 | -43.8287 | 2025-10-17 03:28:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1feaabf5-5f55-3591-be65-6c8dec0b6417 | -8.20084 | -43.31833 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 59f63e87-d5cf-3d60-9f82-a094880cbadf | -8.18713 | -43.32521 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 130e1085-4d33-3390-b9c6-5c4223c4e1e8 | -8.1219 | -45.55755 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb5a8a72-2431-3db5-bbc2-8ad293c30b61 | -9.30706 | -40.22844 | 2025-10-17 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b007aa5-4f2f-385d-a82a-6a8aceede3d5 | -7.95387 | -44.11767 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| baf5b10c-caf8-32ee-8823-660c9c0b80c9 | -7.97866 | -44.15936 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e84efcb-870f-318d-8143-aec3890c2ac8 | -5.86043 | -35.4767 | 2025-10-17 03:28:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 21.6 |
| a4f85b05-0e8f-302f-a444-dec8dad9cdf7 | -6.14988 | -40.9163 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f86f9fc6-7abe-3777-9f73-9dcd9ced38b5 | -6.13451 | -41.73797 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f18075c7-b574-3ed3-8db1-9cb7f49a9f35 | -6.335 | -45.4847 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ac03826-2368-3854-86f4-01d0cf146595 | -4.40193 | -43.39959 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c17052a-20f9-3a58-bf7c-a4c30a1a2787 | -7.82649 | -44.14222 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c11262fe-996e-3f62-b379-2b8c577071ef | -6.46101 | -39.42886 | 2025-10-17 03:28:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecf5aff5-8abf-34e4-81b1-d0b79c0cc1f0 | -6.35134 | -45.48963 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 19ab0c29-ecdc-3cb4-b4ea-eb64ceb8ceaa | -6.31977 | -43.6298 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e34aa36-8499-3a46-8237-a71f98ca6e05 | -6.21479 | -41.54824 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c246d7a9-80fc-368b-ab94-1df90c5222a9 | -7.68253 | -42.56048 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aaf3a56c-f7e0-3096-85c3-5dacd77c4d17 | -6.2045 | -41.76815 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README26.md)
