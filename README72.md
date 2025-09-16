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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 092f64af-5363-39ca-b761-705f9c9a4e96 | -12.75791 | -47.97142 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3c131028-8a04-3256-b27c-3d846ddd6e8f | -10.21316 | -54.30085 | 2025-09-16 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f4b7488-d012-3496-8f7c-fd9b6cbcbf0f | -14.84567 | -51.6281 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b36900ab-1e50-36eb-a2c5-25772c280439 | -10.71703 | -44.76187 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51d6cd64-1b16-3e71-b177-11aabdb49d98 | -9.69018 | -62.00367 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c40d136-4417-32c1-b66f-94130cc776dc | -12.0516 | -46.53527 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10c1b12f-58de-3ac6-afd8-67131551f6ef | -15.16144 | -52.46368 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5f08583-2baa-3d0c-90cc-4152c9e74a4b | -10.71856 | -44.74973 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b909b9e5-51e7-3583-8e28-f789f07665a1 | -9.15178 | -46.97557 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9c9e1d9-c0b1-39e9-b5e5-6a7c8ce2c573 | -14.65981 | -52.06893 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 478a3bb9-d2ee-350b-942a-2662f8a64b68 | -10.36208 | -61.26081 | 2025-09-16 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b18b12f-e42b-355b-baba-2c464aab3cc8 | -10.78525 | -45.97667 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fb5b2c2-36a8-3800-a1d9-40c3909c421b | -11.48423 | -43.60487 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea43c32b-3b7d-3375-ba3c-77eb99e8685d | -10.70898 | -44.74169 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 998db2e9-59ca-3e84-a4db-83c11d0d9b91 | -10.16321 | -46.1411 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9e8e55a-85fa-33fd-835a-05a27308293f | -11.1268 | -45.34601 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b2ec8a78-1ccb-350a-82a5-2e4d9fbc7b75 | -15.62412 | -47.3732 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d5447ce-55b7-3fda-8c7a-6a91c1722f06 | -8.99412 | -47.03835 | 2025-09-16 04:51:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 764cdc00-86d0-3468-aa78-5d5560cb25d6 | -12.95708 | -47.96067 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4cc6e112-218a-312f-877f-8cee125fd688 | -14.41955 | -47.36411 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85c89d5c-1a2d-3118-af2a-874105d8871f | -14.35878 | -52.92386 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf54dad-b0d4-33ff-9ee3-efc4a373ed92 | -13.20067 | -47.30546 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89c98d20-94c0-3e76-9f76-c85268c6417f | -11.45217 | -46.93229 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1af0c6da-2fb6-3064-bce1-8cd517b2ff3a | -9.69074 | -62.00061 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7658644d-a0c9-322b-8c8c-79395a1c08d8 | -12.17861 | -44.09958 | 2025-09-16 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d554c106-daff-3e8c-b47e-7c5d0e203a02 | -10.65095 | -46.46732 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ffefed52-5bab-3aa5-8e6d-1f50ce7c4eee | -12.61024 | -47.97512 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4135eb54-10cb-38d2-aacf-2212514a3cd8 | -12.73741 | -47.20129 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb9854ef-d290-3bb7-a646-0fab982ab885 | -8.84273 | -62.93347 | 2025-09-16 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f8028c0-ed92-3812-ab96-69f1fa0f266d | -9.87313 | -46.45241 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91d28aaf-7080-3909-a966-8a3038fc7fa6 | -9.04775 | -44.84167 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 073451fd-28a3-3248-a6f8-ec6a90d14dc1 | -8.70327 | -49.41899 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9a76b59-e95b-3686-944a-078b3ad2b845 | -8.58932 | -46.34144 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 848c6a7f-a920-3bb4-9c27-cd117e421fbd | -9.73317 | -48.12515 | 2025-09-16 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e8f858d-a31f-310e-9316-0b04c435f9b5 | -11.11475 | -45.32063 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31da24ab-e04d-3b8c-a8eb-83c54cd8a55d | -10.7463 | -48.1802 | 2025-09-16 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218247b5-c42e-390c-902c-15be684e3437 | -14.61077 | -46.3895 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8aa69e7-5ced-33dd-96fa-23bcc32c0bd9 | -12.66298 | -47.92712 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13be8826-d7cc-37f0-9b1b-454a8e92f512 | -15.09461 | -52.46991 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ae62fa2-2cc2-336b-8c03-00f3dfc6b22e | -10.71727 | -46.49363 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a6e0fcee-1e04-30e0-8385-8bc9004491e8 | -12.96508 | -47.98129 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bc45e3f-279d-37a4-ba5a-b95e76092d09 | -13.28328 | -54.2415 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a659e21d-075f-3e97-b1f9-5ad63a1ae391 | -8.78535 | -46.00519 | 2025-09-16 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 552dfe09-3794-3695-83c4-d927ca3e77fd | -8.12663 | -50.16526 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e48acaef-d038-3617-a768-f3e654d26f3f | -9.04736 | -44.84458 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a0161b0-6311-35fe-9420-231b7ff45114 | -9.09489 | -44.8729 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ffd5442c-8435-35a3-9035-51da021daf2e | -9.13393 | -46.94324 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ee3ae52-d853-3ce2-bdf0-15b147187a87 | -12.68221 | -47.98053 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae4a5110-f014-3920-9d1e-dba429c95a60 | -12.68592 | -47.98547 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c70372c-ddbe-3e82-8a89-86fcb8e73041 | -9.79075 | -61.50783 | 2025-09-16 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ed87586-247f-3c2f-9b6d-65a5e4af5572 | -12.97584 | -47.96607 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98786e48-7c8c-3c90-a3dd-44379e1620be | -11.70697 | -46.87716 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 240e5a03-b79d-3681-9adf-538142ff53c8 | -14.80191 | -51.66084 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3720c71f-2c26-3e61-a7b0-deb9ce403e97 | -12.61305 | -47.95446 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfff8cc1-3b48-3a31-b005-0ed51a306d0c | -8.43077 | -55.64315 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0019b8fb-006f-3857-806d-1b5253776fce | -9.05163 | -44.85104 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb3ec4b1-c85e-352e-b77b-241020ab86d6 | -14.27459 | -46.14337 | 2025-09-16 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 305cca26-9949-39fb-8b4d-e995411e9602 | -10.41765 | -50.64584 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72804f7b-295e-3342-857f-3a3044748125 | -14.19848 | -47.00894 | 2025-09-16 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fa019ad7-fb78-3ad3-8544-81262bea94ef | -12.61248 | -47.95863 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c47017b7-3f59-37db-adde-387a9f62ebc7 | -9.70342 | -47.40508 | 2025-09-16 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f1a9589-3de7-31d4-bc26-ea51d14282ff | -7.71157 | -55.45406 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78bfcc82-b32d-3b40-acc8-9abc8dc40d49 | -13.75709 | -48.76234 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d45d73-3c95-38cd-9839-8497548f962e | -8.97027 | -45.76113 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41716756-08de-3f39-8434-80950eabde7c | -11.69393 | -46.87045 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f68344c-1c5a-30d2-93f7-ac5527c1ca79 | -8.66852 | -46.37885 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cb800cb3-32c7-35ed-ac26-78689bd0e421 | -11.12605 | -45.35175 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5774e07-96de-3e4a-8fc1-e4bbe0385ad9 | -11.71862 | -46.47413 | 2025-09-16 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d167c59e-fae9-3bb1-81d8-fbf06170704a | -12.76092 | -47.96566 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a930dabb-a009-3acd-b4ed-3b063abbc77c | -8.6029 | -45.73795 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f64740c4-5264-3084-971e-cbd3ec5cdab6 | -9.10116 | -44.85711 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bdd44f2e-92ce-33c9-9029-f6da4d81b1d7 | -15.158 | -52.46308 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b8a9226-2054-3f16-92b6-89e16909ed40 | -9.68563 | -61.99964 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 149bae3c-017d-3bd4-86c5-217ea08354a6 | -11.44982 | -43.55668 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f04a1b1f-ff46-31f5-8608-75cc6d2dacff | -11.01993 | -45.06475 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90a20781-0382-363f-ab69-dd0073ffe94f | -9.09609 | -44.86428 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b7bc51c-2a98-31f9-84b8-21271f9f0348 | -11.27772 | -50.80585 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e1a31f2-908c-3537-86c4-5f9b965dd858 | -10.71601 | -46.50309 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1e7a0ca0-9f72-3cd7-b44e-56b0c1924991 | -11.45553 | -43.55722 | 2025-09-16 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bbac19b-7e50-3fdf-bd00-4e9a20b71373 | -10.71827 | -44.74383 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ff3533d3-cc3b-356b-893b-0da3d65c9e0d | -9.74093 | -55.37004 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ec7031f-bd10-32b5-af32-80066d78a849 | -11.46536 | -48.69717 | 2025-09-16 04:51:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9460fc67-5716-3483-960d-3178cf8e4248 | -12.06306 | -46.55687 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77c80e7d-6497-32bf-a77d-4ac2f1c3b174 | -11.15971 | -57.18734 | 2025-09-16 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f4b14ea-be7d-3b2b-8995-d9727ce3ce43 | -8.66913 | -46.37432 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65c7c302-f824-311e-bdcd-1261034ccd62 | -10.6516 | -46.46251 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 50a0d210-3730-30a2-8ee8-cabc8090eda0 | -13.19562 | -47.30888 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf7a12a9-e8d9-382b-a648-4e546f66ab5c | -9.70715 | -47.40972 | 2025-09-16 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4da9b56a-da59-3aad-8a3a-70a09afe1b35 | -12.85717 | -47.14891 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b4c3bc-3214-32b5-b706-4e0d40d6d9b0 | -12.76838 | -47.97562 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9379c944-b736-3f0c-a089-70a22a432941 | -9.18971 | -62.52566 | 2025-09-16 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2841d1b0-7243-3392-a6f4-b5790b028fb3 | -13.76123 | -48.76292 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47802300-94a0-3484-9b86-c2e4490aae71 | -9.74436 | -55.37063 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| edcfd496-13b4-348c-9228-984a499a6f7b | -11.11601 | -45.35035 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9f724cf-2911-338d-b7b4-55e108c19c48 | -13.74006 | -48.76352 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f3d6ffc-cffb-342b-bc3b-ea29f72969c7 | -12.83859 | -47.21426 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e6f50852-1a6f-3405-a3c9-a0b7cf7611be | -11.11638 | -45.34749 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de15b49c-137d-3be0-b5aa-b38de0087142 | -10.70833 | -44.73886 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f8c49c1-0caf-3316-82a0-f68cfafb30c6 | -14.91917 | -51.67319 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 572becc6-49e0-3b6a-ae75-23e4c41b10b0 | -9.21526 | -44.50935 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README73.md)
