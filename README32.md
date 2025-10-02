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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79f53967-5fce-383d-aa1b-d2de7ab46a59 | -9.79916 | -45.95068 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4faf42f3-6acc-30c5-908a-2d1b8926588a | -9.94563 | -43.65771 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0035414f-c4f1-3591-aec0-dc3baf999312 | -9.33477 | -45.70403 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 827d848b-783c-327c-8dc5-edb76d0bc0d9 | -6.322 | -43.03534 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5eff5fab-2e4e-31ce-a468-b05c1bda4f36 | -11.79184 | -47.56447 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b17c5b59-4fcd-392e-9df0-1d191eb5a78e | -7.79239 | -42.50085 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8a782080-3207-314b-a3e7-25626db4e489 | -12.85167 | -46.93836 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb65f451-c2e3-39cc-9d8e-4c384b6609d7 | -11.09721 | -47.84505 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e2093bd-da0a-3c49-8cb5-7b0e2f7f4f36 | -13.34548 | -43.67313 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01bfbab8-6846-3d9b-8f12-c9101abba8cb | -10.83513 | -46.61459 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6fc7daf8-7dda-336a-959a-0d7523218d5c | -9.92588 | -43.73384 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a70718a-0d4b-3abd-8009-e8340fc5c189 | -9.9022 | -43.70046 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1154dc33-3f0a-3ad9-a505-f42120fa41f8 | -10.23121 | -50.31859 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 179d65bf-cdd9-3a86-831a-1e211d0b4fcd | -11.01038 | -46.59014 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fd61f28-7fe8-3c9a-a68f-5c48bd9c827f | -8.87726 | -46.5875 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3533fbb8-90b6-341b-8856-0af302eddb9f | -11.78668 | -47.56831 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1ccff20-4a1c-3e6c-b7cc-c08264e1bd4b | -11.86979 | -48.01418 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea107aa-7d48-37dc-910a-6d9de62d147e | -10.27153 | -50.34047 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fec03414-59fc-3767-9dab-9228a6f6551e | -9.43304 | -47.3265 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e595ef1-ed39-3ad4-8593-47b4b2a89790 | -6.48842 | -44.28276 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 616980ed-235b-33b3-be4c-ba858c5dbef1 | -12.43219 | -45.16858 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81284fbd-1d30-33d1-8934-b4a150a9ff4c | -12.26505 | -47.8111 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e6120de4-5e47-3e57-81bb-b6ea1f61eff0 | -11.53769 | -46.95434 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b05da7e2-d9fa-39c4-8a7e-93fe5770f6cf | -8.89514 | -46.61159 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e24ac421-4ad2-3a53-8357-d2e1d7be08f5 | -5.64173 | -45.96413 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 383ef099-c409-3a4c-9f5b-d6b9a653db5d | -10.82112 | -47.95216 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d93c9b8-c52d-35b5-bea4-aac9a1ad7d18 | -8.84806 | -46.57822 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c97a24b2-cd2c-33c7-a655-14ce64804d38 | -11.46142 | -44.96104 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc5ada52-747a-3c0d-a3cc-794ceba82d15 | -12.0789 | -47.83648 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f757840-4415-3bce-958a-e55ab11c55ca | -11.21947 | -41.60165 | 2025-10-02 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 310469f2-ed2a-315a-b9ea-bf91fb275431 | -10.93424 | -46.67097 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a4ce89-d060-3c28-8e73-d4da4507dcb4 | -7.77593 | -45.71182 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f35fd491-85f8-3781-bc11-8e809fe295d6 | -11.81176 | -45.00251 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d497908-ffce-38d4-9a7a-bd477785fd98 | -11.94543 | -43.91036 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ac827c-3430-3ec3-a8be-b37c98156991 | -12.41783 | -45.17249 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b49416b-1ab9-3383-a8c5-4f078a08b0aa | -6.77401 | -45.58082 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 699019f5-d1fd-37a0-a6ca-55317e4db4b6 | -6.35226 | -44.57986 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c968d86f-a392-3228-a076-9c63c9b3c0fd | -11.19195 | -47.75408 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e535fa-3a46-3136-83fb-7a73926b785b | -6.18175 | -44.0652 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bdebeb8-dc6c-386b-bf3a-ee1a75eedd33 | -6.0524 | -42.43679 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2f5a769c-8358-3e9e-95f0-8450b06c295f | -6.18557 | -44.06569 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1e85df9-d7d5-3b1f-a0a7-e2fef55ac189 | -5.97957 | -44.59163 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9aeb95a-0d87-37c1-89de-b85e3ede6fe0 | -10.85555 | -46.66956 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1e83c10-d5f4-3515-8423-6aa103359b7b | -7.17732 | -41.69387 | 2025-10-02 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6c611f5-3f8a-346d-b01e-99fa1530fe45 | -10.11071 | -45.69572 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c614216-9f03-3e1a-aef4-8d649f2b9672 | -10.55062 | -43.64647 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2fdb6af-d68d-39ba-90f6-bc616f0d5dce | -11.4695 | -45.00399 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86684e18-6404-3c8e-a6d7-5425373b769b | -6.32358 | -43.04832 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7e428dc-d099-3ed5-9e20-4b5ca96d5313 | -8.16219 | -44.13164 | 2025-10-02 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b424b0f-4309-3971-bf1c-405995164279 | -6.53826 | -43.37097 | 2025-10-02 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4c179dc-2cbb-37f6-ac25-346fede3fbc5 | -11.98971 | -50.56935 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99018c3d-6017-3655-9800-dd57d2c83ffb | -11.82562 | -44.97984 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38b3cf72-dfa1-3fb1-82f7-fa2be9d11b61 | -11.46797 | -45.0131 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ff12515-60f2-3f5e-b5a2-a74d28246729 | -11.81618 | -47.68526 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e73640b2-88bc-35f2-bcb1-e617681c4b7b | -11.43051 | -47.28524 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fd6c5c0-ea8f-35ee-a4c3-3e4c09ea581b | -11.53279 | -46.95761 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47a018d6-8ef1-355b-ae4e-936858b61995 | -11.43282 | -43.49903 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2609111-c66a-3dad-8733-03dd133f74d5 | -6.48914 | -44.29534 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 365bfe51-d7be-348d-aa0e-4d7032e06ee1 | -5.6381 | -45.95924 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 015eed10-6a2f-3568-83c3-5e85ba234ef4 | -10.80441 | -44.23976 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbed6667-9093-31aa-87b1-e04d6e9ce3c2 | -6.66542 | -41.40175 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 97103ce7-7143-3cd5-a7f2-6ea83c29b749 | -6.2301 | -45.33053 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 67cac7c9-c82f-3a51-8f3f-cc7160870f1c | -7.03122 | -44.47273 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58e4b567-67d4-30e2-9457-df8a6154ec8c | -12.36676 | -45.7893 | 2025-10-02 04:02:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a689f65f-3cce-3189-8036-3df569ba1d6e | -10.84542 | -45.38329 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f2296978-3736-30fe-8ec0-206e0f7bcc79 | -12.03039 | -47.90598 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ecc0e08-4efa-30f1-b198-3f45d7fcee83 | -6.70165 | -48.70586 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a14f7835-ca5f-35f7-b22e-b530f03c5fa7 | -10.26144 | -50.33499 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1b90576d-87f5-3da1-8e69-c2b7c5051caf | -12.2402 | -44.03953 | 2025-10-02 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c6ab272-0af6-3ee5-92e0-00fd8f2ccbf6 | -10.35196 | -48.1989 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50dbe68f-1fbc-381b-998f-7ac02107fbbd | -10.20792 | -50.27847 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c476f86-323b-3d99-b695-79f1cedfbbee | -12.2532 | -47.82668 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43b47383-0446-36b6-8d16-371bf7181acb | -11.94478 | -43.91431 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f9aeb6d-4ba8-33ff-bf0b-d4d4627eb362 | -9.71114 | -48.95444 | 2025-10-02 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df835cc5-dda0-3b24-b07c-1a2363a902c7 | -8.66027 | -47.69682 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5516b5-9aa2-3fb8-a928-d893edbb6ad0 | -11.89179 | -42.82341 | 2025-10-02 04:02:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f50674b-cdb7-3682-814a-46cff38efc0e | -10.83109 | -46.6377 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dd7cbf0-f306-303d-a81f-205a0375a5fa | -10.82896 | -46.6254 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e46aedc6-faae-3137-bd81-a3775225dbb0 | -13.37671 | -43.76114 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8087679c-d1a4-3e77-af1e-f7e4f8175083 | -11.66963 | -44.2794 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34eaa0e0-6ed3-3bfd-9b19-da9a702c0e36 | -10.21229 | -50.27235 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 11dbfc31-1337-35f5-b52d-ab19512c170d | -11.82529 | -45.02597 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bf88700-176a-3fa9-a153-78f0322faa22 | -9.47454 | -45.47662 | 2025-10-02 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf613460-df72-3b33-af7d-e4dfb3d1b7ec | -7.55068 | -42.64672 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 844239a0-451b-36d3-8558-cfd09f66c32e | -11.05929 | -47.81022 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a041e4ab-a216-36fe-b73c-8d92d3b31ed7 | -10.22256 | -48.20777 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 946bbfc5-63de-3c5f-85be-84b34e82ba3c | -6.54973 | -45.22239 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dde0467-db36-3c56-b70b-f81237a0a9a5 | -10.2206 | -50.34524 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38862133-655d-3a78-9138-8862ada74331 | -6.48309 | -44.28457 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e3777dc-789c-30e5-b782-5906e846d964 | -11.71095 | -44.46283 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 485fbb6d-de70-3669-b92e-bec23ac6a8c9 | -7.77934 | -42.53764 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5d94edf8-5972-3be0-921b-464b978e2154 | -12.81526 | -47.02397 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04329c30-1df4-303c-9917-9aba0749c766 | -11.58227 | -50.17194 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe5528a8-302d-3678-b136-54fef31db262 | -11.21378 | -48.214 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 504f49a7-2c1c-3a8a-85f3-583b60911415 | -9.92895 | -43.75967 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38b62190-297d-32b8-b949-58d66717600d | -7.7887 | -42.52356 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 190dc9b8-90db-3e07-a9f2-c071d076f716 | -8.5596 | -44.65968 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 045a491b-2ce5-389d-9039-95d61ca69935 | -10.25867 | -50.32017 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 31663bca-28cb-3ebe-8f8a-e7a7b21ca95a | -12.07916 | -47.83678 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c88a323b-1d8e-3a8a-9c5c-35be92f13bd0 | -8.57157 | -49.6054 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README33.md)
