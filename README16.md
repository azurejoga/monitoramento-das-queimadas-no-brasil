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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe0ed2cc-7e4d-3c28-b57c-12981ff8e79b | -14.68808 | -48.78598 | 2025-10-22 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f917479-8ef3-3eb9-aa73-df2b36ef168e | -12.37987 | -63.87446 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8a09fc7-6192-33fa-adee-f6a8b9e345ca | -18.67002 | -47.05444 | 2025-10-22 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 123edfbd-9e4c-3e40-a015-f5c2f8709247 | -20.98131 | -47.2057 | 2025-10-22 04:57:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1c9d686-cd78-3214-b67c-94c0345acbe3 | -20.56787 | -45.89288 | 2025-10-22 04:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7544829-2ad4-3bbb-ae86-013c96ab1cb1 | -14.53918 | -53.7641 | 2025-10-22 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb22cd1e-1a5d-3a90-9d4e-2e2e54c9d051 | -14.8745 | -56.24855 | 2025-10-22 04:57:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84ab749e-4c0b-365e-8a06-d3357a184278 | -17.67307 | -54.21908 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f0f4141-3961-3c89-ac7b-0dbb8edceaf8 | -18.94687 | -55.0741 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 565a5ab9-bd78-30bd-877c-efd742cdfcd9 | -19.26301 | -51.97466 | 2025-10-22 04:57:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 577897ce-b25b-3323-9edc-48ed2d674b5d | -18.64511 | -49.09142 | 2025-10-22 04:57:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b0b57b-9e1d-3497-939a-dadfee889fad | -12.12857 | -63.21236 | 2025-10-22 04:57:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b428ceb6-5a1b-369d-85be-dc576db76e9a | -19.06435 | -57.48452 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d4187bff-9e21-3d04-879b-333f18d8fb6c | -12.27166 | -63.87514 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3a5e54e-78dd-335f-89fe-eda962aba58b | -19.30891 | -52.76628 | 2025-10-22 04:57:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ebf06ee-e99e-3f34-9441-957990c7cc46 | -16.24003 | -49.59335 | 2025-10-22 04:57:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 178d9131-0d88-30e8-b13e-fdbde350ec6e | -12.3751 | -63.86966 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f83fe306-7623-3f4d-a12d-1f75ce613b44 | -18.64999 | -49.08797 | 2025-10-22 04:57:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f44893b4-3e6c-3cf6-ac9a-c434992a67c9 | -16.23954 | -49.59704 | 2025-10-22 04:57:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e75b9e26-9690-3b0b-a4b9-b05d8df656bf | -19.05555 | -57.49493 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| b783f565-97b2-315d-baec-d4c1382b1ce6 | -17.02058 | -55.91009 | 2025-10-22 04:57:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 63dfcb70-dadf-3dea-80de-502c2c6ac9fa | -20.5619 | -45.89677 | 2025-10-22 04:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ad6fa22-533d-3eb6-b74a-f69bb85d11f9 | -17.83759 | -50.8131 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f7eeb8-bd12-34a0-8285-3886daf80fef | -15.86999 | -48.81095 | 2025-10-22 04:57:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 080626dd-edd4-302c-8466-69dc2f4e34a2 | -18.34286 | -49.49913 | 2025-10-22 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c52e1b4-c061-3003-b2e8-86b853a1f7f4 | -19.08587 | -44.34332 | 2025-10-22 04:57:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34a3ad52-eff0-3e8c-9cd3-07ff01f1c84f | -16.24077 | -52.9086 | 2025-10-22 04:57:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 054163c0-34a2-3e2b-a04f-8532560cbcbd | -18.94906 | -55.08201 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| feae46a0-aaa9-3b64-9682-60fc9b2d42df | -18.16682 | -52.97012 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45eb9039-5780-3d25-9623-f47a22255bf6 | -19.48581 | -54.92895 | 2025-10-22 04:57:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd56703e-3466-39f6-a9f2-c30d37984ceb | -19.10504 | -57.53199 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ec9f5eab-7ff1-30c6-9fc8-32b1774216f8 | -17.33939 | -55.04039 | 2025-10-22 04:57:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 205865e0-8d56-3b3f-8457-85d4e8db7b8a | -19.90784 | -46.11035 | 2025-10-22 04:57:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0906f5c6-590c-3d59-ac49-e948ccb0607d | -15.61858 | -48.90767 | 2025-10-22 04:57:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d528c24d-b0ca-393b-bf76-f54415e016f1 | -17.62686 | -46.61394 | 2025-10-22 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00441303-f120-3f13-b043-8396bcfcfb9c | -17.67364 | -54.21538 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e7cd61-25b0-3c9c-b72b-3b98a8513e7f | -19.06093 | -57.48389 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1d3af3fa-2761-384f-94b6-c2c2e514e199 | -17.62176 | -46.6133 | 2025-10-22 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87a5f698-dd39-3f45-a948-7144551c03e9 | -19.48915 | -54.92953 | 2025-10-22 04:57:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af11afcc-7ad1-3095-b071-3ddbe42f54df | -15.48717 | -50.45438 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c026a626-f611-3842-b22c-659f8ddc019a | -20.5623 | -45.89259 | 2025-10-22 04:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0851c76a-53c7-3a84-984a-8885318ef2e6 | -16.82257 | -47.63943 | 2025-10-22 04:57:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f1a71aa-13ff-3d21-a7ee-7a235d11839d | -12.13451 | -63.21009 | 2025-10-22 04:57:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afaac6e8-3305-337e-90d6-631176effffe | -19.08245 | -57.524 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0e8fe075-729b-3962-a0b5-ab0dee2a9a9f | -14.69279 | -48.78304 | 2025-10-22 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e8e7b7e-4e3e-3292-98bd-471c0ba5ee69 | -21.0564 | -46.9872 | 2025-10-22 04:57:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c6b4ec4-e36d-33bf-9d35-9922010dee49 | -16.63043 | -43.48661 | 2025-10-22 04:57:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a1b6620-2005-356c-ad1e-a2de5527c216 | -17.61829 | -46.61596 | 2025-10-22 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88e2bbea-3805-3020-99e9-82fe6ebdf4be | -17.67028 | -54.21484 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ae12f24-6fdb-313b-a5f3-9a2375a7c239 | -17.67421 | -54.21168 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c4ad50e-e4a2-397d-8d26-9803d51800a6 | -12.13386 | -63.21342 | 2025-10-22 04:57:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d7b6a0-202b-3957-a176-09534d76dfeb | -15.0717 | -56.4298 | 2025-10-22 04:57:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265c23c2-df0d-3875-a03b-cb307f8bd394 | -17.62141 | -46.61644 | 2025-10-22 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77a538c6-06ea-3cb0-947e-80abc5e8d724 | -12.27786 | -63.87268 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea63a720-a5fb-38e3-b28e-fc58dc92e162 | -14.53583 | -53.76356 | 2025-10-22 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f71742d-7c2b-3178-887d-c14f8c0fdd33 | -24.77111 | -47.59662 | 2025-10-22 04:59:00 | NPP-375D | ILHA COMPRIDA | SÃO PAULO | Brasil | 3520426 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7330d226-a139-3963-8273-d4cdf9ecc251 | -22.37975 | -46.91733 | 2025-10-22 04:59:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc662ab0-04db-364c-8270-838e00f77305 | -25.00718 | -50.8649 | 2025-10-22 04:59:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fa183974-0f58-37df-b667-2851096a93d1 | -24.98461 | -51.52771 | 2025-10-22 04:59:00 | NPP-375D | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c871c05-c044-390c-8f99-7d652886a834 | -22.38009 | -46.91381 | 2025-10-22 04:59:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57bef8f2-7b09-3bc1-a04b-cbb7a3ddc597 | -24.38097 | -53.48353 | 2025-10-22 04:59:00 | NPP-375D | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c875189-de35-39d2-8717-64e8e06f81c5 | -24.77079 | -47.60005 | 2025-10-22 04:59:00 | NPP-375D | ILHA COMPRIDA | SÃO PAULO | Brasil | 3520426 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 90daa54a-bae9-3d66-b3e1-439df554f7bb | -9.0036 | -65.9226 | 2025-10-22 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| a5437804-9f3a-3bc3-87d2-30c258632099 | -4.4445 | -43.2397 | 2025-10-22 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 5f5085df-1384-3fe7-909e-f407cb17e815 | -4.4446 | -43.2164 | 2025-10-22 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6d98eaee-0c12-3438-a519-5f6a88195631 | -4.4632 | -43.2386 | 2025-10-22 05:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 50ede35a-e3a4-3a10-a516-8d90afdf5114 | -31.8704 | -54.1617 | 2025-10-22 05:01:00 | NPP-375D | ACEGUÁ | RIO GRANDE DO SUL | Brasil | 4300034 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 95e64c28-f686-3e34-8509-d668a705e5f5 | -29.65061 | -53.92625 | 2025-10-22 05:01:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 82e0a93c-a6d2-3dbd-bcf2-4b065c1d6d7e | -29.65441 | -53.92682 | 2025-10-22 05:01:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| a9f3a99f-230e-3b64-8130-f5c572eab36c | -4.4445 | -43.2397 | 2025-10-22 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.0 |
| d66494a1-70c0-37ca-9efc-3fc2e9d13f7a | -4.4632 | -43.2386 | 2025-10-22 05:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 74aab7e1-a947-3240-8833-4e54e9194cf9 | -2.25665 | -51.92936 | 2025-10-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b580b605-7b4b-3d54-9181-ca992685aa78 | 1.67839 | -55.72229 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b4861b9-8087-39c2-a91b-0ab40bc8a9a0 | 1.53159 | -56.06218 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18eb5f3e-c0b0-3c80-ba92-5e915ab06268 | -3.02775 | -49.45983 | 2025-10-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fec6c5dd-e9b7-3632-a8c6-cc938cb6e2ad | 1.54514 | -56.02039 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a45f1f2f-e58f-3ff7-a981-2665e946416a | 1.67393 | -55.73749 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d4cd9e-2a85-3050-98e3-87d377770f06 | -2.92652 | -48.30028 | 2025-10-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bc77024a-3e26-3781-9c7b-2b99eac64ce9 | -3.99167 | -48.32986 | 2025-10-22 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf23b09-2a15-3112-8c67-c3f2eb525a51 | 2.11622 | -55.93487 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7f502f9-3878-3688-a373-925d174349c9 | 1.52826 | -56.06269 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03683edb-b32a-399f-8b15-04dcdde0710f | 1.69402 | -55.71262 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e73c4b9-79cd-3973-a7c4-d34cfe11ef82 | 1.53214 | -56.06567 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50e1f763-bd26-30b7-8811-5f69854d9235 | 1.67616 | -55.72989 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b3aa959-1d8a-306c-8c61-575fb7e9c422 | -2.92598 | -48.30397 | 2025-10-22 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 429dc03a-f4be-3e30-9fc0-faa0e7eff7ef | 1.53792 | -56.01793 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b142001-8fca-393c-8525-894c106876d5 | 2.05278 | -55.70768 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 645ba192-4695-3cd4-b704-8a30cda20d4f | -2.47899 | -49.25642 | 2025-10-22 05:14:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7f6c362-0532-3b1d-b694-6b902fb661d1 | -0.169 | -49.96682 | 2025-10-22 05:14:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae7128b2-7642-37c2-b3fc-598a2cc4216d | 1.67895 | -55.72583 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ea94a7-bb08-3b43-a18a-927182e852f4 | -3.02306 | -49.45606 | 2025-10-22 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7c80e8-fb9c-3738-bf25-0e62e92df1e3 | 1.51775 | -56.03927 | 2025-10-22 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bb19589-2a6a-3862-bd8e-083adf48c8f5 | 1.6756 | -55.72635 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f443a418-b694-33bf-bf46-1b579e93be6f | -3.51872 | -49.44807 | 2025-10-22 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c91c72ec-a4dd-3263-8ab7-e7811990b485 | -2.48861 | -58.06232 | 2025-10-22 05:14:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6bb876c-d385-3f77-9af3-c0bee8dab9fb | 1.67337 | -55.73395 | 2025-10-22 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e3c449-7f8a-3690-9d91-c03f0ff535e5 | -1.4626 | -55.23189 | 2025-10-22 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9332baa7-9316-3106-b827-8a591b2c113e | 0.59581 | -51.57086 | 2025-10-22 05:14:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9949e40f-bcf1-3a5f-ab13-1aa81bd1b1d0 | -2.25519 | -51.92808 | 2025-10-22 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fefe0ad3-a762-31dd-adda-c104979f4e05 | -2.48915 | -58.0589 | 2025-10-22 05:14:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
