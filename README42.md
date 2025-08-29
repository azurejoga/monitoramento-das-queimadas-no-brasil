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
| 965113d3-6f1b-3869-8dda-197f75c73d06 | -9.93816 | -46.70398 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e12c1b7-b714-35e4-9246-ef4e9be746cc | -10.95255 | -46.87812 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97341d03-2ef7-348e-9528-9b0bdbe12002 | -6.27491 | -43.82138 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e1adcc6-e25c-3a2a-a9e3-6d258b86d937 | -6.44937 | -44.57302 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f097a34-bc1f-3f3f-8e36-7206455b897a | -12.84044 | -48.11114 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4be38531-3cb0-3940-bc8c-ca07ce3a2e7c | -12.8132 | -48.17315 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae8086ac-4db4-3ae4-98db-a1e8c7dcbf1f | -10.95208 | -46.85511 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e8c32db-a1a2-3039-a80a-ef4f85408d40 | -12.68436 | -48.18813 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec6e9153-ba6c-35ba-9f6e-c551be594944 | -12.85299 | -48.1249 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ecd881c-20f0-3e01-83ac-1c00df58df71 | -10.37082 | -45.17714 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6f39e4e-6198-3759-8dbe-53c12b5c9077 | -7.72593 | -50.28569 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 475cd032-16f8-35c9-9834-5dca195d7728 | -13.18695 | -45.27494 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99ecb77a-44c8-3207-a33e-186e3a4b5f68 | -9.40156 | -48.22739 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efafd462-a177-3457-aeaf-bc99effc9c55 | -9.67428 | -48.32555 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf3a84d4-9aa9-368b-b4f5-90e6aa0bd203 | -6.56157 | -43.69468 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15e88f73-d0b8-3255-8afa-defc48b08e5d | -7.39538 | -45.92645 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 998deb3c-c1fd-31de-878e-60f9fd0af51f | -12.80965 | -48.17261 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 918a1dc3-45cc-3f7e-a948-a3a5fb5a60bb | -9.45674 | -60.55799 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1cf0b690-ac34-3dfb-b830-4f4bcdc43c92 | -10.61477 | -54.90793 | 2025-08-29 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 560daca5-f4e3-35b4-b9c5-2d2482ae5629 | -6.20144 | -43.32582 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 173eb827-7857-32cd-a820-7fe56e3f95a1 | -6.77999 | -44.64561 | 2025-08-29 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7702d246-3625-3c82-a178-9598ca7f87e6 | -11.3466 | -43.52854 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a27dd05a-558f-314b-baa7-eb32d0ce886e | -7.16533 | -44.15422 | 2025-08-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67e1032b-ba80-3442-8257-ed9992aa8112 | -12.3248 | -47.04784 | 2025-08-29 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faca9df6-70d2-39aa-9a9e-446705b50090 | -7.04953 | -44.38919 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ff0148e8-8a6e-3085-bbd8-5b3be3044c1d | -7.55248 | -47.4716 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bed3d12-2c62-3078-9edc-8b0be99f3c7e | -8.18981 | -61.37692 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7630cb9a-a698-3455-a9f0-33928caf07a7 | -9.15393 | -60.9297 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1dbf5d84-e5fd-31b4-80e5-280a8fb8ecc1 | -9.50372 | -45.37822 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc0a5fc5-7d10-3b06-929c-f0856fa36c7f | -7.61342 | -42.67466 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 072272db-1686-3a55-949d-19110926b753 | -6.97935 | -59.33337 | 2025-08-29 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a6a20be-56cc-358b-8cdc-b4aca1ff10ba | -7.53685 | -47.48103 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69416c70-1850-3803-a03c-c92f7be3a283 | -7.15858 | -45.16331 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1781aa06-8558-38e1-8920-4aff13f65437 | -11.33794 | -43.52222 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8792918-0ce9-374e-be38-db065f842dfa | -9.69542 | -47.06719 | 2025-08-29 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ddff223-260c-3e3d-aa88-79233fd1fe87 | -10.94398 | -46.85848 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94256679-f9ac-3240-9a70-7ba04f4e70ab | -11.22181 | -55.06402 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80b952bf-9a8a-33c6-9dbf-69d7c465da8e | -6.70996 | -49.45473 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12c4d812-a70e-38a0-a26f-0d5fb67b80f6 | -6.81408 | -44.34748 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84b6d8ac-c8f2-3340-8162-ccd96d5832e3 | -7.72978 | -50.28275 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 521ccb58-1c59-335f-876d-39d0ef9e21c8 | -10.83948 | -47.50247 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cc3c843-b5c8-320e-b03f-c3122920990d | -9.71598 | -48.32779 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0709bcaf-e493-3d66-8333-d0075ea54e32 | -11.24242 | -45.01055 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 02c3534e-f3ba-341c-9050-1d55651af77f | -12.40323 | -46.49141 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4421dfc2-8e35-3a83-b96f-6d7bcbe3581f | -11.55539 | -46.3671 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1b80fd85-ebd7-3598-9bcc-2f6e31af5aeb | -6.38892 | -45.58448 | 2025-08-29 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cdd2a94e-9b14-37a3-9446-5ca140cbd962 | -11.22536 | -55.05239 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4afc772a-7f88-354e-a96d-39a741fd0f59 | -10.36466 | -57.80962 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 12417723-762f-3b13-9722-81e0653a79e7 | -8.55664 | -51.31589 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78f9da43-0661-3a74-af70-0103d5eb0835 | -7.08726 | -44.30259 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec1597b0-be27-32dc-8e68-490168507300 | -9.86308 | -44.68544 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0cd5485c-843f-35a3-81ec-0a7b726e8c32 | -11.02877 | -45.06742 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0f07b32-ad8d-381a-a5ea-2a7164351927 | -7.04647 | -44.38118 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb33369d-d635-3ec2-b98a-4ae48d8aa250 | -8.44474 | -43.71028 | 2025-08-29 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12109d36-34b4-3fe9-80a0-0614cdd89211 | -6.16572 | -47.28058 | 2025-08-29 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| af52aae0-cb63-33c8-a025-05c78fbea3dd | -8.43418 | -43.65643 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 969e98a6-89c7-3594-98e2-141c494b8089 | -6.44822 | -44.57349 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 186fa52c-759c-31e8-a998-f91565e318f6 | -8.06756 | -45.03221 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 927ca9d8-cfb2-30de-99f3-052852472c9a | -12.91294 | -48.10692 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 416928ea-4483-35d5-a688-46ff4a87713c | -6.81675 | -44.3286 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424dbbe6-7c27-36bb-8134-bd4c6baf6c53 | -10.60325 | -54.90602 | 2025-08-29 04:40:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dbfc827-3c4f-3dad-8aa9-7c2f4188b1b4 | -11.07448 | -44.7566 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0acab225-405f-3ef0-8748-ee234e34b6d0 | -10.03131 | -48.07348 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2dc1486-fae9-3eac-9ef0-8045ca96844c | -11.58952 | -46.37652 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c50c8d10-1e91-3268-947d-25891d214e99 | -7.39471 | -45.93095 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2852391-6f69-3495-98aa-188e35cca595 | -9.16236 | -59.56499 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ddad597-6eac-3478-8078-73ff0445453b | -9.178 | -59.45042 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d7adc1da-fb83-314f-8807-0fb539113b4e | -6.14955 | -44.4304 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 251a0929-c649-394c-bc9a-0daedcd44877 | -12.87602 | -48.13572 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84f27398-b832-3e58-9d9c-cc61789a162e | -11.32702 | -43.57101 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c18f833f-00af-33b3-b070-907fc5982a87 | -6.77427 | -44.82758 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc032e60-af0a-3b9d-94a3-bd7d2fb0d577 | -7.39863 | -43.38276 | 2025-08-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3dc2241a-5ff3-3a40-8697-90db072d0f37 | -10.02029 | -48.07588 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cebdcd7-cf80-36f7-94cc-6879d9b462de | -11.57789 | -49.51485 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ab722a9-1606-3489-bfeb-b8011d665334 | -11.57176 | -46.27909 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10fdee4e-ee00-391e-b5ce-b67234585021 | -10.97772 | -46.91382 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 009c052f-18b2-31ac-9806-2eb6bfdd95df | -8.47692 | -43.64062 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 03abb552-4d7b-3e90-ba89-a61f62bb1204 | -10.47035 | -57.93295 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 56b398f9-738d-3f4b-b489-395014fe3dad | -8.13179 | -61.21096 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae825a70-4c22-349e-9e9a-c92b8c019c49 | -7.61133 | -46.23915 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d83eb068-1f60-3ee4-a339-700077765284 | -11.94414 | -46.70606 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83b5772b-b245-38e8-8785-c51f1047f69f | -10.81036 | -46.36133 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 607f2139-61e5-345d-a7e4-ad69d21a7081 | -12.86008 | -48.15099 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20d495ed-a8ea-36f5-89f0-f2dffe9b5daf | -11.59462 | -47.29498 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cdc4102-1647-3f73-aa1b-4a156e6192c4 | -9.16356 | -59.55853 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 853b75d9-6bf7-34f1-afeb-7ffac6b213ef | -12.92053 | -46.33928 | 2025-08-29 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b84f413b-22dd-3bc9-8892-304a3debc8a2 | -9.24093 | -59.78504 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45edd75a-41c7-315e-9e4b-daf5b9b1429a | -12.86126 | -48.14299 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5b446ce-1c3a-347d-af36-42ae255a24fd | -12.87188 | -48.13924 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e08a540-ed59-391b-bf4b-62a7d9651e44 | -9.78784 | -64.24301 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 469bf872-4364-3c46-97c6-f79eb1d7173c | -7.05794 | -44.35976 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb97b497-2e98-335f-a6d6-64cd9a1893d7 | -7.63345 | -42.66753 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45c714c3-0538-37d4-9bdf-f650ec624a3c | -6.20239 | -43.32485 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d7499e-9ea4-3da2-aaa0-e14925f564e2 | -9.1686 | -56.99612 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8721a44-2752-3ea4-b07d-de7ace0bd5c4 | -6.7128 | -49.65327 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3536fba4-2600-3569-9eff-ecda626b2cfb | -11.15684 | -47.14499 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dc5c597-56c0-3d51-9f44-f6d2e52ff4fa | -9.49826 | -45.38807 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef18dfd7-0fdd-32a3-adaf-085278ab7b9b | -6.13739 | -44.05413 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc487c2-6f9e-3290-9dfe-0363fd85ee6d | -5.56316 | -52.07089 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f2c6f5-5069-39c6-8b5c-1056b2f569c1 | -9.45712 | -48.27818 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README43.md)
