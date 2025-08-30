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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab659fba-98ac-3470-912a-03e01ecadf7f | -7.89162 | -45.17366 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52fcb006-694d-36fb-956c-2e95445eca75 | -8.05846 | -45.41523 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22f79618-5d97-3ce3-83cd-371b98094218 | -8.34788 | -47.4429 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 777fab1d-741d-3493-9fb0-899ff15aee9d | -8.1229 | -45.05764 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6af59b58-424c-3c12-84b8-e8df83274085 | -11.31844 | -43.62575 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9df321b7-1ffe-3279-936b-d31415d10653 | -8.11203 | -45.00768 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8daa19-5abf-3fb8-82b2-375ddc0fffa3 | -9.4385 | -62.35203 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cacf92aa-526b-3af4-95b4-92dc1fcca6fa | -9.6358 | -48.29877 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 009df68e-cb62-3ada-ba1f-2f1be7280290 | -7.40641 | -49.52106 | 2025-08-30 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4ee6ddc-fd83-385e-877d-ec1445ae8af5 | -10.65033 | -48.65952 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d9f29fe-2d4a-318d-9cd0-976b97f209f9 | -7.74883 | -45.17112 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 054acba8-5f51-31d7-9e84-8c4c8fa250d9 | -9.69735 | -48.31328 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b767fd8-0c3a-3383-a3ae-a1eb4cdf6c1f | -11.91445 | -46.70342 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87151e33-4aac-3a12-bdec-afd4eb3307c0 | -9.44194 | -62.36579 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 229f89eb-df4b-3860-b397-3d228f791ab0 | -12.36858 | -46.39409 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| daedd573-bc76-3733-93e2-d2a1e345ecb2 | -7.41536 | -42.05664 | 2025-08-30 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d97465f-e136-3038-be5e-4faaf9ad801d | -11.33757 | -43.5983 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77fe4707-461e-3cd5-9cc3-71a18416beae | -6.94747 | -44.31079 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c909fea2-e1ef-33cf-a2fe-a7f70d070fd5 | -9.08319 | -59.48582 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65417f43-efdf-39ea-aa55-a6dd9920cc9b | -7.34832 | -47.53321 | 2025-08-30 04:49:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4ec049c-e1c0-3a84-9aea-dfd9c1da0115 | -10.02126 | -48.05401 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f082fdd-882a-357b-a177-a487f46cf271 | -12.01121 | -43.99397 | 2025-08-30 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 478d05c9-f79a-3335-81bb-b21907547d1f | -9.44363 | -62.33763 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9b0b70a0-8123-30ef-b85b-ef2bad642787 | -10.49094 | -51.62926 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5371027-e486-3431-b250-76de6cfff06f | -10.73118 | -49.57866 | 2025-08-30 04:49:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d527a065-44d0-35b1-a21d-a4837c31130b | -9.43429 | -62.34234 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b621543c-96a6-35ad-ad98-3849632848b6 | -11.82792 | -46.45678 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d757126-5bf0-3c43-862d-15938cae804c | -9.4475 | -60.54753 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 453708df-ef4d-3303-bb74-1fd8d2ea5210 | -7.75318 | -45.17168 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89ffc175-d52c-3807-a1c7-88fb2e25c936 | -11.73033 | -51.72291 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb08c499-7d13-3611-842b-f88c5d0cbfbc | -11.14664 | -47.1499 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 690249cc-84b3-35ed-bcbd-ac4c6ab5dc21 | -9.43769 | -62.35623 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 406399cb-d6e9-3e94-a7a5-1a2544c0769c | -9.44769 | -62.33588 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 953ac0ff-601f-3f5d-bb2f-d389ea632dcd | -7.74444 | -50.26979 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e95d376c-b86d-3b76-a761-45d967ec2709 | -9.43806 | -60.56905 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1c5bfeb-9bc2-3642-8a02-6d3730c53edc | -9.24893 | -60.93135 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e72b3a5-437f-3c28-a272-c8707c48009d | -7.60709 | -42.71923 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cbd9daf-c7f4-38e5-a281-e354b075b95d | -10.07048 | -58.36284 | 2025-08-30 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b996a73c-0973-3c42-845b-670a3e436476 | -11.40455 | -46.90343 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00c76158-5e04-355d-8e31-384baee8577d | -9.17911 | -59.587 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a27e60f9-9fa3-3e50-bdee-9763dc2fcd29 | -8.54132 | -54.75148 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6563e754-06bf-3a3e-9bdd-22466629e8e0 | -11.30429 | -43.57502 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59cd8eb0-8bf4-3d00-a904-9dffcca2b8cb | -10.44354 | -51.35176 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5daa0153-63cb-3945-9c99-811133529fa3 | -11.01679 | -52.47513 | 2025-08-30 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c58c07a-d324-307f-a5d1-44b9dba46c56 | -11.36423 | -43.57074 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ef111d5-45b3-3499-81b6-3220708070a4 | -7.39577 | -45.93325 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50b66804-06a4-35be-8c25-d98e4f26c435 | -7.34379 | -45.24659 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12143d13-315e-3b12-8ee5-d5b6c6152e50 | -6.88702 | -44.44247 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 913ceb1f-2555-3c2b-8c5c-2bb9b9d80be4 | -7.62314 | -60.85449 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be2228f2-8d24-32fe-aee7-6f791cbba663 | -11.72481 | -51.75827 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3258a0a-b963-36cd-98bb-4d57d0479d25 | -9.4591 | -60.5433 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 80d88b2e-113a-3cf2-8b79-73366092c98c | -6.86833 | -44.44468 | 2025-08-30 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 574a31a7-a91f-3999-bc5b-5634d5408ec6 | -8.50985 | -54.71551 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c27adc-8b2a-3b68-9e20-cc92d8e7ce18 | -9.70243 | -47.05149 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ee638ad-7a77-36ee-b35e-59da603f4c05 | -9.45331 | -60.54539 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67089b7e-a8c8-3cad-b05d-1159bb86776b | -11.85304 | -46.39282 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bb1bdb1-0eca-331e-9b63-962a38ff183f | -9.45355 | -62.337 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9d820fa8-5a2a-3c94-a759-da4e20f01fcb | -8.87585 | -60.73981 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27ca4036-aa65-315b-8172-43e0d56a63fe | -11.83206 | -46.45283 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 033fe502-7749-37bb-8073-40e8d2f6d023 | -7.76539 | -51.10957 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64be5ad-d354-33d4-91f0-3784e420f22c | -8.17299 | -61.37249 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56478c2c-9e6e-3890-93a6-e016b10db8fb | -9.69368 | -48.31271 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd0c494f-38ff-33d5-bb1b-32fe6c7c72c9 | -10.38256 | -57.83041 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dacb7b6f-bc7e-37ab-9efe-3724e66f709f | -7.78033 | -45.46904 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e58a11c-e6bf-36e7-a130-a168ce527b0e | -11.34347 | -43.5929 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b2017da-b20e-3351-9e5a-39afea4d9cea | -9.45552 | -60.5625 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b62eda61-f10c-32ef-920d-2d1e51aae184 | -9.44603 | -62.34452 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bbc899a4-b1f4-3369-b469-a059771679c0 | -10.08296 | -48.86686 | 2025-08-30 04:49:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9ec213a-e08a-3739-be98-9301230caf68 | -11.89033 | -46.71301 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f3884f2-87d3-3bcb-bbee-cb0be1b9db9b | -7.39367 | -45.93025 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91f28848-1907-352d-b6b0-b76970469a89 | -9.41627 | -60.57141 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cd2e731-e692-3b44-8f16-76f1d17cca3a | -10.67503 | -47.06885 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e6e0048-5289-3086-a113-f839e8d5f0c0 | -9.17138 | -59.57383 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43280336-987f-30dd-bcc3-806955240578 | -11.88616 | -46.40365 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0611e10-634c-3419-87a4-b50f8cfd8806 | -11.82682 | -46.46462 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 63eac9c5-7f5a-3bf4-8d84-4c64ce1b4b71 | -9.46521 | -62.33959 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 84499c5c-1236-3e0e-9e09-6364819d901a | -11.9216 | -44.86226 | 2025-08-30 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97c7daeb-e489-32bc-916d-04f09a997d02 | -8.28247 | -47.19962 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f394cea2-05a7-304f-8a56-351b75423f51 | -9.21601 | -60.86872 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffe1aca2-cdac-3be5-b860-a4e38167c4ae | -7.72765 | -50.26735 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a87944ae-dbed-33d1-83ab-222f0f4de049 | -8.56094 | -63.02192 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80af6d58-3094-3419-ba0c-27691c6c30d1 | -11.84095 | -46.79423 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ac5e617-2a6f-323c-853d-07487d7192f9 | -7.959 | -46.38792 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 820f932f-f910-38ce-9dcf-7f1d40c5f1a7 | -11.86162 | -46.39331 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 869e9cde-bc3e-3b98-9142-1263161ae6b9 | -11.32861 | -43.62712 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 650d1cd0-b7d6-3720-b5dd-9efd4e51e9ce | -10.9398 | -47.42897 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e79e9d2-3311-366c-874f-194847c7402b | -9.44765 | -60.54733 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ee3c2bf4-2dba-3df8-9785-0dd6a4b7fcb2 | -7.73826 | -50.26536 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1be0bff-7739-352f-b83b-4acccd9b50c1 | -11.87267 | -46.37561 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9670b24d-0ca6-3de5-8c62-8d1546d20b1d | -9.11491 | -65.74387 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b67baaf-c8cc-346f-849a-0de6d8e8ba4e | -9.43837 | -62.32119 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a08f1e25-fa55-3f60-8708-59a43fb58edc | -9.44699 | -62.37118 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03716d7d-25bc-3b35-a067-02822cfade9e | -7.71826 | -50.30587 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68eb40f4-4644-3a51-bc69-b2aa613ab955 | -11.07606 | -52.03701 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e770f1e4-9042-3324-b109-caddda5e91fb | -9.44347 | -60.54024 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 76c9806e-6020-34a7-863b-b9f2f851dc7a | -10.68775 | -47.06527 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2cbfcd0-1386-3970-997c-4dc20427236a | -11.72814 | -51.7588 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d5c422-5053-3bd1-b81e-081da0039485 | -7.6064 | -44.72504 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba4ec777-8970-3677-b918-5e2a973f27eb | -7.78395 | -45.46829 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 904ed416-2bd3-33a6-a445-8b70234b440c | -11.87697 | -46.37581 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
