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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68f68a24-f3e7-34d3-84bd-25113cd7d6c3 | -12.60887 | -45.74553 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1e39d6d8-7d16-3c57-9c9f-07e93bb25c43 | -7.99886 | -45.65016 | 2025-09-16 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0058747a-3375-3a57-b8b7-452939050b0b | -7.98623 | -45.64801 | 2025-09-16 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 20a1b302-86fa-37af-8b58-920c3833321e | -12.05077 | -46.55827 | 2025-09-16 05:27:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a53d3bee-0d2a-34ab-9354-6eaf085f0603 | -9.06773 | -47.02745 | 2025-09-16 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 49a0fae5-e957-3972-a0ca-953d484a6e16 | -10.70928 | -44.73525 | 2025-09-16 05:27:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 7506dce3-a6f5-3239-ae7d-9be5c5f1956b | -12.65701 | -47.70503 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e8226e88-222b-3163-a57d-18cb13131bc4 | -7.99568 | -45.66965 | 2025-09-16 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b298602c-6431-317c-846d-2dd22d1b4d82 | -12.62594 | -45.7709 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| f5b570f6-a789-373f-b09b-97808e527bea | -9.04224 | -44.83351 | 2025-09-16 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 93d59901-5446-3f56-bfae-274b2536a4d5 | -9.09716 | -44.8494 | 2025-09-16 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 0e2dcc05-2bac-3f72-be7a-352f46ea827f | -10.71552 | -46.49808 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 331.0 |
| e4db0e0b-d123-338a-ae03-d0639262735c | -12.75073 | -47.97927 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| b7ad430b-b6f1-33c0-aa9e-2279f99e1bb8 | -12.62052 | -45.7475 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 690.3 |
| a1894e62-5078-37f0-8cdf-ad513b28d339 | -12.83471 | -47.20068 | 2025-09-16 05:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5a83ea1c-5ad6-3661-a6a6-8d867c892f0f | -11.69418 | -46.86666 | 2025-09-16 05:27:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cf25fe85-636b-381a-96de-b12be1089cf8 | -10.71189 | -46.51856 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 0f0bafad-a1b5-3b30-aff5-3236d6f38dba | -11.12751 | -45.33724 | 2025-09-16 05:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 7d1336ab-a3ee-339b-a95a-cab8a5033969 | -12.6288 | -45.75442 | 2025-09-16 05:27:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bc6ffecd-69d9-32fa-88f7-700fa96bd191 | -8.61047 | -46.39806 | 2025-09-16 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 804a8491-9898-30a5-a61a-6d6e86efcf73 | -12.76884 | -47.95776 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| ffc18832-e9f7-3d8c-bc97-b937f3066236 | -10.64441 | -46.45197 | 2025-09-16 05:27:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e66383dd-4193-31ae-96aa-1d84611661e9 | -11.69512 | -46.86133 | 2025-09-16 05:27:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6f9e70a7-d86e-3a95-8c8d-49c391fc8473 | -11.12468 | -45.35376 | 2025-09-16 05:27:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1cbec2bd-90fa-3c7a-a294-38219c185e27 | -9.06096 | -47.02094 | 2025-09-16 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6a41eeea-1142-38b8-9d70-8739b731d39c | -12.66884 | -48.00819 | 2025-09-16 05:27:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| ff6caf56-809b-3eb9-8f50-456a4151d664 | -13.20107 | -47.29397 | 2025-09-16 05:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 66b9f03e-8b3d-309f-aea8-61106bfce93d | -17.72569 | -46.77227 | 2025-09-16 05:29:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1f259528-c54b-3b56-b45e-7e2c2ad33199 | -17.30331 | -40.68185 | 2025-09-16 05:29:00 | AQUA_M-M | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| bda824c4-ead6-300b-90be-441d42da6a59 | -22.32553 | -46.52562 | 2025-09-16 05:29:00 | AQUA_M-M | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 1b53db24-f60b-3320-a57d-d04b053a7df3 | -17.07285 | -45.81839 | 2025-09-16 05:29:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 757caf18-b41e-386a-bc63-ba0489aaeb40 | -19.84484 | -46.45167 | 2025-09-16 05:29:00 | AQUA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 31557c36-63a0-3660-ae7a-071e8e9dfd49 | -16.51079 | -43.54008 | 2025-09-16 05:29:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8f0c7260-b5d9-3b6a-81e8-1bb31ac6bf3c | -21.21851 | -46.9453 | 2025-09-16 05:29:00 | AQUA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 78c91dc4-aec9-3733-924d-b76fd629b504 | -18.61453 | -48.19611 | 2025-09-16 05:29:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4d7ef3e9-cbf0-359c-9b59-21eb6f5edc5d | -17.08111 | -45.83466 | 2025-09-16 05:29:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 98057e72-d0fa-3804-b8c0-ab77112edbbb | -16.58575 | -42.90445 | 2025-09-16 05:29:00 | AQUA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f1ab7ab0-e166-3d9e-a793-daf64ef2294e | -16.50909 | -43.5505 | 2025-09-16 05:29:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 45239903-d364-3a5a-9094-6dc3b191b740 | -17.08357 | -45.82045 | 2025-09-16 05:29:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7968542f-de98-3d98-81a4-4f6e03129bef | -21.93596 | -46.57017 | 2025-09-16 05:29:00 | AQUA_M-M | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 684e778c-71bf-3ed2-a867-3ed1e0457f38 | 4.30754 | -60.95887 | 2025-09-16 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db90d0a0-08c6-313a-b962-dce0029ec67c | 3.85882 | -60.06897 | 2025-09-16 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd2d855c-40d3-33d2-831f-a2d350502065 | 3.84319 | -60.06282 | 2025-09-16 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14f248d7-79e8-3ab7-9e24-57137980d49e | 3.86077 | -60.06581 | 2025-09-16 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f2dcbae-bb5c-3faf-aab2-d6328a6072cd | 2.00525 | -61.4598 | 2025-09-16 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05b65074-edb2-3ace-ab74-2e44ad9ce68c | -3.65362 | -54.0563 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612513f7-00f6-300c-9404-76c206a2df6f | -3.65301 | -54.06065 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bbe6040-4003-3200-a2cb-52cc28d1ba21 | -3.6549 | -54.06232 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20df9f28-868a-3164-a31f-060d180e4077 | -3.65554 | -54.05798 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a52ab5c5-d2ab-3f61-8072-165d5e783db0 | -3.6477 | -54.05532 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a641ec3-ad74-32c1-9bc1-b85fb1e77cbe | -3.64961 | -54.05707 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70bfc5ed-928f-3082-8ef6-fae3e722baa3 | -3.64896 | -54.06145 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eea24d5c-4241-36e2-baed-17aa93ed50b6 | -3.65028 | -54.05252 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d2d7342-f0d8-35e3-92b4-3c93fde47bc7 | -3.6524 | -54.06501 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d3e30e3-d235-39b9-ade9-07b71f556907 | -3.64832 | -54.0658 | 2025-09-16 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a551b2-892d-3542-8748-6bace04b3514 | -15.82634 | -53.46987 | 2025-09-16 05:44:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6168f56-d925-3cce-a48c-9c8a494f4883 | -8.84651 | -62.93217 | 2025-09-16 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91a1ed63-9b09-3578-bf17-b87c3acd5ec6 | -8.06069 | -71.30303 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a3bcfd-a6dd-3164-8e9e-0b909d4f73fb | -7.90919 | -71.73878 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f36cb4e-c6aa-36ff-a783-51449a28e613 | -13.29224 | -54.23789 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 040d538b-0f42-3813-9dce-d1c13d9af11d | -13.28363 | -54.23284 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f9ca21a2-b7e6-3a0c-ba39-801f33246f27 | -13.28964 | -54.23975 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f33f7319-69ea-3ce9-869c-30da785a5850 | -7.91345 | -71.73957 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0d7b954-d095-3cf4-b2a8-3086068ca718 | -10.36963 | -61.25723 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6c41323-7681-387e-9dad-3810f36a8878 | -13.2764 | -54.2378 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5dcab2ce-bf37-39fb-85c1-3bc1b6d74e4d | -9.23561 | -65.32281 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 101c4844-09eb-3062-8a24-dae18a635661 | -8.84914 | -62.93084 | 2025-09-16 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8adb45-52ba-393c-b397-8c8630a79437 | -9.69019 | -62.00134 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 095ce83a-37bd-3215-bf58-a45b3cea2faf | -9.23506 | -65.32635 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0bc2157-9de5-36b7-a5ff-decba3dc7f78 | -9.45219 | -63.2132 | 2025-09-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0714d7-76e6-384d-b005-c3236aedaa02 | -9.30705 | -65.5854 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a168c7c9-345a-34c2-b56c-f3d4f71b43d4 | -9.0067 | -67.49429 | 2025-09-16 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d598733-94e5-3047-b9e2-447ae94891ae | -9.77032 | -63.40954 | 2025-09-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65729270-d50c-3c25-988b-d29ef8cd32c9 | -10.37014 | -61.25365 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aded7905-6b55-3925-8579-786acfabd1c5 | -10.36509 | -61.2603 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 066d885e-2b12-325f-8441-29a52d5d4bbd | -9.01006 | -67.49483 | 2025-09-16 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b05f872-d689-356e-891d-ef71591cfdf8 | -12.40916 | -63.88803 | 2025-09-16 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8260052b-4eb8-3b3d-9419-bdbad68333ae | -13.28627 | -54.23101 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9bbfdfd6-6699-33e0-9be1-25b36f649fad | -9.76974 | -63.41356 | 2025-09-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2782a4cf-bc29-3821-a12d-444f595eccb3 | -9.63644 | -58.94445 | 2025-09-16 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc53a43a-3615-3518-ab0d-809ea53cb396 | -10.36106 | -61.25977 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fd631ae-13b8-3be5-b4df-507dc9a52962 | -10.36159 | -61.256 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e46d084-18bf-37c0-9ab1-ca9f343b31b3 | -15.83347 | -53.47062 | 2025-09-16 05:44:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 363cd32b-799b-3e68-9271-00fd86d703e3 | -9.74866 | -55.37703 | 2025-09-16 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 34c35af5-db17-3e68-a56b-d7c5b19a910f | -9.23838 | -65.32689 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92a286f8-9935-3e5c-9027-850cacf03373 | -9.53831 | -62.381 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f17b5893-c1b1-3784-8fbc-8dae7cb52838 | -10.37364 | -61.25792 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a959bce7-0db4-35b7-bb1d-6e0a812de932 | -7.80344 | -71.97993 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c2ccd27-54a8-309d-a1ed-15075feb1714 | -9.54203 | -62.38153 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1c3dd18e-0a56-373d-992b-199ac3528687 | -9.31366 | -65.58643 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f3b9df1-8a95-3e71-a16f-a8e8bdb5b2d5 | -13.28301 | -54.23884 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a712b51-a167-3868-a05b-9f9f0347468e | -13.29026 | -54.23378 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e8e9ffa0-acb7-35cb-bb52-da3a6dbb3fbf | -9.74273 | -55.37633 | 2025-09-16 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 865dbe56-6852-35e8-a719-9077a9ee1ca4 | -9.628 | -62.40561 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49f9c877-bd6a-368b-ad68-6b8fadba6e05 | -10.15047 | -64.2524 | 2025-09-16 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 275b9563-bfea-3d29-a258-aa35f5523247 | -9.7968 | -61.50815 | 2025-09-16 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9b7cc15-007b-31dd-b86f-e8bf21490260 | -9.23893 | -65.32334 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd6f6e0-9e75-3464-a50a-9f840502836c | -8.84556 | -62.9303 | 2025-09-16 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13c92469-ed9a-39e7-b453-f2306a877506 | -15.86998 | -59.39244 | 2025-09-16 05:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b10d9dac-a787-32b3-9c7e-631387ba7e04 | -8.03335 | -71.36481 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README83.md)
