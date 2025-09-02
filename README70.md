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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891a5237-be47-3c2f-9e71-bc29e5689f50 | -9.35063 | -65.44696 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da3bde85-1b57-3694-a8ff-58bebbabfca3 | -9.6015 | -47.15511 | 2025-09-02 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8666f671-8705-3ddd-a0a5-e7eaaaa48120 | -11.92463 | -50.61537 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dbab972-f304-3ee4-a727-b8c40e35cb89 | -8.72894 | -62.42339 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e48920d-a44d-31cc-8b85-00a588b51cd0 | -7.53624 | -63.85191 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d862b6d-d5dd-3014-92db-8d23bab20823 | -8.55425 | -63.0116 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e640afb1-fa30-3a8a-a1c3-64e595b1194f | -8.75941 | -62.42453 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 815cd1f5-74d1-3150-b22b-09c7558668df | -11.92966 | -50.61154 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57bd1b2e-c328-3019-a022-271b58efa39e | -12.91521 | -56.94356 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66617358-2148-3a30-af99-0804dca456a3 | -13.89494 | -48.09243 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ae475d-cf8e-38c8-af49-7c3dce9f3948 | -9.73199 | -48.98703 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| dfb1448b-d232-397f-8fb1-70cc1bad7828 | -11.04479 | -45.14344 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf81e7d9-cadd-33f1-b743-8d07e857d633 | -13.54311 | -46.98681 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0c0b070-b8dd-38ee-82ab-c7156b24641c | -8.76465 | -61.44082 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67ca4aa5-4c19-36d9-a94f-9c1c24e36462 | -10.04713 | -48.14801 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab4d6a53-8759-3e1f-a287-8b0ca875af2c | -12.93951 | -56.96198 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cef41c48-0d4e-3b96-a51a-d5d1995a538f | -14.26077 | -45.24664 | 2025-09-02 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52a1ab0e-98cc-3bd0-939d-a49b222ec0c2 | -8.85105 | -52.01528 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e3ceb37-eeb4-33fc-a108-bb29fcd14e94 | -10.4543 | -49.05911 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 620e6c10-2c99-34c1-9070-91769b003ce9 | -11.40008 | -54.69654 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fda39b3d-fbf8-3da4-97f2-1204c7f8e46b | -9.92374 | -51.63058 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ead2dfb3-da8a-3cfa-815d-79fb5bea3f7b | -13.5361 | -46.9936 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2460e28-7117-33c9-aa34-e8e9a569dbe1 | -14.78551 | -48.20415 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18954e90-cb88-3233-9161-78eb925fac04 | -12.4267 | -63.90758 | 2025-09-02 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa408b80-601f-37bd-8363-05b999036a00 | -12.75342 | -44.41072 | 2025-09-02 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df4ecfa8-8c9b-3e8e-8588-e06efb1f15f8 | -14.60194 | -48.03925 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e3f4290-3033-33d2-9b06-8eef39c4b411 | -11.43312 | -55.18209 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3342e76-4af7-3c7a-a20f-35c5b68607ff | -9.50471 | -57.79792 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 928b1b81-0eb5-3ca6-b198-651ed164ab21 | -9.48645 | -46.50814 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df8f4651-b10a-31be-8f9e-31eeb1c22fe9 | -7.78808 | -61.57042 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86337399-fb0b-3a85-8f9d-0aa27ab62a84 | -9.50805 | -57.79846 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0124d053-83e4-3c50-b8a6-6650971dd411 | -12.86711 | -48.0432 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4aef39a7-36b8-3537-bbfe-476db9681736 | -11.43584 | -46.812 | 2025-09-02 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 875ee523-2804-3d2c-b791-0981061eed2f | -9.48126 | -46.5034 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77b85375-98f7-3392-80c0-8173b6d3f70b | -14.60429 | -48.06827 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 187348fe-0a78-3e9c-a5a8-7a440168845a | -12.92794 | -56.97097 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2df385b5-85a1-38fc-8c12-3465cd752f94 | -7.57595 | -63.04728 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e346d86-8e59-3611-b3d1-4fe614f9e71a | -9.34156 | -55.22297 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea25ba10-b895-3711-bf52-296eb7dcae1f | -11.06415 | -45.39599 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3203369f-510c-3cd3-ba3e-39dc6a72a598 | -11.66785 | -52.17883 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8f46a0ab-5f5e-3226-ae9a-b28740ae6050 | -12.93067 | -56.95331 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 615a6792-b301-360c-83be-b8b445d82576 | -10.76239 | -59.8412 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 511bb107-8b5c-3435-bef7-108c7fa45dcc | -10.75255 | -49.57087 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b57bd0c8-233f-3980-b0cc-23e8f3376c3e | -11.66698 | -52.21433 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7bd1dd45-e994-361d-87d9-01fffa733b13 | -11.76032 | -47.82847 | 2025-09-02 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6a2f5e2-7ff1-32d2-b7f5-10667954a950 | -10.27752 | -54.26208 | 2025-09-02 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f93f961c-cef0-35a6-b054-06cda036b374 | -7.69559 | -61.09782 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4237cf96-102d-31e0-80c7-9889a4690bc6 | -10.26081 | -47.52961 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c044b32e-b47d-3797-ac80-53fc1d061c94 | -8.65518 | -62.60552 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 103f94d4-808b-31e4-8d4d-1d0a448c9013 | -13.09346 | -57.1318 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36984dd6-f66b-3780-b6b0-f00037037264 | -13.70225 | -46.93354 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ffd582c-1e23-306a-a1f4-d44106c2b0a6 | -11.82448 | -51.54665 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35f581eb-858c-3128-b65b-019a77875638 | -13.54288 | -46.98598 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 477cbd02-7e41-3bbf-8159-cf959cc1b0c9 | -10.43983 | -54.77213 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba777f6-e97b-3c93-8a66-247a1dea6ee4 | -7.70353 | -61.09914 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7123ecd-8185-39fd-a276-5280ede7773b | -11.65491 | -52.18401 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 46ec39c8-b994-3262-ad7c-c82f606f3700 | -9.83778 | -48.61 | 2025-09-02 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa89d464-e584-3cda-bcec-1d83e0aeabe8 | -12.94668 | -48.08624 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a04a03b1-be25-343b-9d8b-c8e49c7d3726 | -14.58842 | -48.05571 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862a6809-ed93-3c0b-84dd-c54e00e3fb2c | -11.82083 | -51.54216 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97f25813-ce0e-3e4b-baae-edc09f9f9f44 | -12.93787 | -56.97256 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71d0bd2d-511d-3047-91da-3027a91e0cd2 | -11.66132 | -52.16709 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ead5895d-83e6-353f-baca-31a15d18606f | -9.3749 | -63.5027 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6353c0c2-86e1-3142-81f6-8619c5675ecd | -8.68548 | -62.40037 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17fef70f-aa89-3e5c-8cc7-640b2e894c2a | -13.49124 | -46.92205 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e1e41f5f-1d4b-3a0e-b7d1-8251864de23b | -7.54787 | -61.33233 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d391a458-aede-3bd8-9796-d5aef2b4eee7 | -12.59057 | -48.20519 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fea07ef1-7e41-373e-b84e-d17bd145234f | -13.71418 | -46.93278 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f886d85e-4b6d-3904-9fe6-619568f17c74 | -12.9119 | -56.94302 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a7a3ab-1b51-33ba-a694-36f586d02097 | -12.57698 | -44.78772 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eb9b762-83a1-38ab-901f-e5f4b3616b5e | -10.05923 | -48.09515 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1f6382d4-b18b-31b1-84d0-27ea40c97bc0 | -7.54502 | -61.32453 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a52181e-f181-3a46-bed3-c032a41aef9a | -9.6074 | -47.15231 | 2025-09-02 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77774524-918f-36e8-aad3-9c286e1477d6 | -11.66795 | -52.2074 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bd4558e4-f075-3247-857f-1f2b306243c7 | -11.00975 | -46.83382 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 228b8914-93d4-3663-b6f9-9a6727fb8fc9 | -11.66239 | -52.18877 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 229fd45f-8f0c-3dfe-a81d-9da66d772939 | -12.92238 | -56.94109 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78eb54ce-7196-3f38-98e8-de169d848a21 | -10.3633 | -59.1783 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264aaea0-a1d8-3bf9-b205-c48bfa73bfa5 | -11.10484 | -44.62345 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 68045440-0c5d-3342-8295-c9e640220aec | -11.86245 | -46.7109 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57ff9cad-5429-3ee6-9fa6-b58c12ef64fd | -10.75847 | -59.83963 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2735f307-3ac7-3ed1-a7ce-858fc05d0c59 | -9.259 | -56.90008 | 2025-09-02 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2f4d966-8577-336e-9749-f6e9147942e5 | -11.65387 | -57.35583 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02911bc2-1121-30d9-b455-013ca0ddd8b1 | -14.49941 | -45.95057 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebad1a4b-69b5-3274-8317-00898b6b1ab2 | -8.65671 | -62.6088 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 616895ad-1a8c-31be-b04c-42acdb34276d | -11.66191 | -52.19226 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6cd28149-a441-3e9c-8a4b-153747b8035c | -14.59583 | -48.04 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 791f567c-2d4e-3423-9cfa-e734855985dc | -12.92411 | -56.99569 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef0264fb-17ad-31ee-84b3-dde37fd0c30c | -11.65237 | -52.17284 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79d349d5-2b0a-32ac-bddb-51cd5418a710 | -12.92132 | -56.9699 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0da13285-8052-3652-a542-f38e4c5543d3 | -7.08164 | -63.071 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8264eb4f-e32a-3f4e-b70f-f4b05d7bc053 | -11.43026 | -55.17782 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 490775a3-ed11-30ce-9bcb-d9ab133ddf91 | -10.36715 | -52.28586 | 2025-09-02 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21458f35-a963-319d-a79a-803b1ab9f0f8 | -12.8765 | -48.05559 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4b0d4833-d6b0-3a64-8492-886c2d12bb80 | -13.31085 | -46.84917 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d8a6ac5-771f-3ed8-992a-961a0f6bbaea | -12.94097 | -48.08846 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 729f44ad-93b1-3955-8f83-1ddcd0abf423 | -12.87902 | -48.05944 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bd09727-6fb7-3001-8e66-dbc3d57f1553 | -10.66904 | -47.33234 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa3c7899-b52d-3255-9edf-cfb1f40bc521 | -9.46442 | -60.31713 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3418585-97ea-30f5-a9e0-ad87f861a4ae | -8.66167 | -62.83549 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README71.md)
