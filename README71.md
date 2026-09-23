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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bf8404d-fc3e-3830-a41a-c0209e9e8ae3 | -12.7854 | -50.90313 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6500676-8212-3edd-aa73-00755e53ee8c | -14.698 | -45.60199 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 212544da-13f7-3215-be29-70b6e5681d51 | -7.64638 | -45.45399 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5602f854-7a17-37e0-ab64-ae649b6ff111 | -11.3022 | -51.36966 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c3b5412-893d-3d31-b4c9-f4d5b81a28ac | -13.4262 | -46.27527 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c559fcb0-4e9b-3260-8e56-e5da725fcc71 | -6.67675 | -55.05131 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97042f24-e413-3439-b0c4-c4a453a62f0c | -12.41298 | -46.9757 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f6d2ecc6-4acf-3e96-ad48-5a6fe405d0fd | -11.53524 | -45.34881 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee49110b-735d-30f2-9091-665fea51ff09 | -12.12035 | -45.63556 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f1d0d8d-ad7a-301c-b7de-455077d1b2ab | -6.6752 | -47.73635 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc2fa187-8ec8-33c5-97d2-f10faca9eb70 | -12.40796 | -46.96396 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef0e2aa-3427-3c78-8ece-68c772140ff1 | -14.59223 | -45.63281 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dde56ef-bcb0-3a7c-9e78-527ac24a10b0 | -11.87839 | -49.94854 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e83c92d-7ada-3814-9211-9cd52a9a5661 | -12.50701 | -46.96108 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cd9434f-6a58-365c-8eed-2866ee44181c | -11.74919 | -50.05095 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d3e1b03-e06f-3af4-8aaa-9ef2190615dd | -7.49764 | -44.33089 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33125505-f395-3f3a-b621-9ba097c9b2cb | -12.81141 | -50.85672 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f53875e8-50ff-3afb-9c4b-1d7ae20ce493 | -8.83941 | -50.48561 | 2026-09-23 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89c9351d-47ae-3f6f-8be9-3d5c4c4e21de | -5.92288 | -59.91948 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 09a542c6-1cab-3318-9b7c-8d03ea04169c | -7.093 | -52.74896 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68760e42-8dde-361f-b977-57ba22826708 | -7.39785 | -44.78341 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec42cb8e-d2cd-3048-bd79-dd1cfb10c95a | -8.82311 | -47.25375 | 2026-09-23 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae306ec-3f14-31f5-a90e-43b286bce26c | -9.34889 | -50.10003 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 266fd870-eabe-328a-bab6-488622ac02c3 | -8.81692 | -44.27162 | 2026-09-23 04:27:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ce88b422-4622-3c72-ae3d-111b86cece67 | -11.30673 | -51.34264 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24a5e7e8-2572-35ab-89c2-c26358705c73 | -8.25218 | -50.86925 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73ab055c-b77a-3806-bd22-214074483de6 | -11.4625 | -46.70226 | 2026-09-23 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308424ca-ec17-35c9-adcf-25f7008f13cd | -8.33641 | -50.87406 | 2026-09-23 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba062e0a-87b2-3ac4-8755-adef3e49222d | -6.88718 | -46.56265 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe444e7-c854-3a0e-a406-d9c6e9eac251 | -14.60749 | -45.62677 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 2f35e7cd-1044-3b67-945e-e3f66506812a | -12.1261 | -47.3829 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a269800a-cbf6-3182-9647-1e65db9fe17b | -10.25731 | -49.98682 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9857ad9a-124d-3611-b3a7-c989c8700abd | -7.46079 | -45.49161 | 2026-09-23 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fae4c8d0-c0ce-3d6f-a3dd-d1571a1ad7e6 | -11.45064 | -50.23616 | 2026-09-23 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 066c2e33-9407-36b9-b612-360ae5ba236b | -9.8923 | -48.47593 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74506795-4d3e-399a-8d34-2cc080d9cb94 | -8.37355 | -45.58791 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0a9ac07-b351-33ee-b57b-876b2c9a9e25 | -9.52194 | -46.54531 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1bcd529-a7c6-3602-9c3d-360fad8ecf5c | -6.10342 | -57.67276 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b00e64e5-dd03-3acb-ad66-ae73a8cf514b | -14.618 | -45.65332 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3887fa53-36de-373c-b461-baf1c73b66b3 | -11.40284 | -44.03068 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24199f90-aa8b-3a97-b33d-9f076f79ad72 | -11.66229 | -43.47548 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c245ea0-1cf0-36f1-8688-5ff0b08649e7 | -6.67421 | -55.05508 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d59717aa-2ee3-35dc-91c7-18b7666a5f14 | -6.59441 | -51.32426 | 2026-09-23 04:27:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b263020-db9d-3b08-9591-aa595680848f | -6.17257 | -52.05133 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03ecef55-9d18-37fe-b3be-48cbae79b5b0 | -10.69699 | -48.72049 | 2026-09-23 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83c5852d-4696-3b2d-bdb1-d028cf3cd1a9 | -9.58482 | -46.5336 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 194cf7f6-68f0-33cc-bd5d-dfe96705c11d | -14.67507 | -45.58594 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07664941-b12c-3f7d-9b8a-3d9c3605481b | -6.73627 | -59.42576 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bae2c2b1-8347-3004-8459-de4082a625ee | -6.17779 | -53.29009 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13635e41-b37f-37db-967a-5188cf78bba0 | -6.82014 | -59.45869 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c576b93d-e8bb-3510-807a-e7b48c7dd463 | -7.55513 | -48.67704 | 2026-09-23 04:27:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478f3ba3-0674-3e81-9723-e6276a9ade42 | -8.60291 | -54.60452 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4334a1d-46c7-3647-ac49-50ec0c137190 | -8.59888 | -44.53933 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bfb01b8-31e1-3d17-9eda-7913de440c1c | -12.80786 | -50.8561 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7012a7e4-4455-3c9f-a253-853ae60e4454 | -8.32115 | -46.87491 | 2026-09-23 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8fb8cda0-acab-3d57-96ff-8e4e750daed0 | -7.17296 | -48.6279 | 2026-09-23 04:27:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e98c3412-3dbb-3817-acf0-24ffabe98927 | -6.45611 | -54.9852 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdd21732-8aae-35b2-9ba8-2766043a7f60 | -12.74478 | -50.88338 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a5d81ec-0bbe-3cd3-bcac-dd35296329cb | -6.10867 | -57.67859 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6ee5ecab-642f-331a-a707-1240ed746494 | -14.66743 | -45.58895 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38d98476-da5b-3ab6-8529-74940e7e0f10 | -12.47342 | -47.02509 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd8a6d1-16ee-3a4b-8593-a4d54dabc48a | -9.71381 | -48.33662 | 2026-09-23 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59241537-86f9-3500-88da-6b5bc44134aa | -13.45886 | -46.27187 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d997ff6-90db-3344-8a4f-28f4fce7c643 | -8.46121 | -44.68333 | 2026-09-23 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efaff897-5d9e-3db5-b728-1af09ad5af4c | -9.7104 | -37.27186 | 2026-09-23 04:27:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e9fd142-8134-3a2e-86cd-2d4ac1c43d7a | -6.66526 | -50.94588 | 2026-09-23 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a765b9bb-8fd6-374d-97f7-18b9acf7f846 | -6.18419 | -52.79591 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71f45147-9378-35d5-b95f-e62bf687ca52 | -12.81851 | -50.85794 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73277c59-d6d1-31fd-b93f-42b23dc3374b | -11.18175 | -48.04935 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8231389-d48f-3cad-85d4-b907b273a011 | -12.7327 | -50.88979 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d57efec6-e576-38e8-8831-fbd97bd861a1 | -6.74238 | -55.30918 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34a063e7-f7b3-31f4-aac4-f17e7d835abd | -12.73696 | -50.88628 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1e9b22e-7005-350d-b55d-c094d6986316 | -6.44837 | -59.96375 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2526f15-7386-3c39-8572-5a56661b6a58 | -12.81934 | -50.87503 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b582a4ad-b3e2-3ac0-bd7c-15c4acfa588a | -14.60805 | -45.64766 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f60c6a48-adbe-3eeb-a44c-93285cab617b | -6.9295 | -46.55156 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e028790-a12b-387b-8c7e-c874f9f9a081 | -11.30522 | -51.35163 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7b8ae0b-18bb-30d4-9c6a-73088d306e7b | -10.26665 | -50.23638 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 50c28194-f28e-39b8-a1d7-ae471d14d04f | -10.03635 | -52.10798 | 2026-09-23 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ff84d38-21bb-36d2-95f3-c471a0a298e6 | -12.41183 | -46.96092 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c095291-8a1e-3007-8090-857f6d2e4826 | -12.05535 | -50.35903 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a5867e5-bc5b-31be-a9e8-4efb062a5b98 | -11.40652 | -44.03122 | 2026-09-23 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a3393f4-9957-3feb-a5e2-250342d019bf | -11.28447 | -51.33885 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be561915-bf2d-37cb-8d08-2426ea8d9feb | -11.10735 | -48.30463 | 2026-09-23 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9378486-22b4-3924-94b0-2f86e68145e2 | -14.63878 | -45.6639 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df662f72-65f5-318e-a0df-c1bec652739e | -12.78173 | -50.88126 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bac5bf5-73f3-39f7-a887-4661546a9662 | -10.0432 | -50.22577 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c3b7bbe-c660-3d87-976a-f17eee2f6d1b | -14.61215 | -45.64414 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59f062ee-ffa9-302a-9b11-997fbdbac52b | -14.66332 | -45.59254 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f310ff97-1579-3c07-ae52-00189986b6e1 | -7.41405 | -49.85859 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42ca9b40-09e8-390f-8b5f-6c9e78963506 | -12.80045 | -50.92275 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57ee1875-65f6-3d5c-b1d1-a100bd54dda5 | -13.85586 | -48.58904 | 2026-09-23 04:27:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b2860d2-d1e2-3176-84ed-35cd5d4c55a6 | -14.66038 | -45.58788 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8865e0d-37ac-3875-a507-f0c1b6b6a7bd | -12.67144 | -45.04159 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 693f3afe-e5a4-3508-bddd-b2c27d5bc999 | -7.27305 | -45.53839 | 2026-09-23 04:27:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4cf3af4-9d5b-3567-9242-5f535ff85eb2 | -11.88908 | -45.77555 | 2026-09-23 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7019ee88-b3f3-3f52-a830-f448e90a0c8d | -11.52664 | -45.35928 | 2026-09-23 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e17c0b33-3abf-31d8-ae2e-4d268d088fcf | -12.07015 | -50.04352 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1d5b0f0-78df-3d17-912a-421a090e74d4 | -12.51645 | -46.96624 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a3e301-54b9-363e-9e95-558e06148b7a | -14.37854 | -47.23452 | 2026-09-23 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README72.md)
