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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 790d3872-f20b-3895-93e1-ce0e9da6cf6e | -9.12167 | -49.92158 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53b85782-f7c1-39e8-8e2d-2e9f5a8227ca | -7.18794 | -46.54396 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd9fa50c-8069-33d8-99e3-630752822949 | -10.32315 | -47.78741 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f621c185-b599-3101-8a42-a30289d48518 | -9.76196 | -44.81627 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9cff45a-3d0e-356e-a005-d777b52b7a8f | -11.20386 | -45.20225 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0bc1c39-254d-3201-9f3b-8b6e0c2d5289 | -6.70356 | -55.05388 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbfe50e0-4592-347a-b8bd-9718667de86e | -8.6386 | -45.2933 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c906f61-168c-3d96-8cee-48242e33555a | -8.16615 | -47.14484 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f14abe4-a265-31fa-a235-fd14d9e88a50 | -9.78896 | -44.81155 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f6c9fd1-aa3e-31d7-92cf-df93841c4954 | -11.41961 | -43.4054 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3e091ad0-b2ec-3190-b996-bdb934b05f8e | -8.37579 | -50.73206 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41bba033-abfe-34ec-9254-760818b93d3d | -11.18141 | -45.11462 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cd8ced3-e01f-36a5-b18d-e6af123ad2cc | -8.21227 | -45.48895 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050ed3f8-a211-36f2-b0d3-98414f0f1f32 | -9.81277 | -44.81928 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d160251b-13ef-33c2-bcef-5e57bcf5f35a | -11.41197 | -43.40429 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e3ba61f-9891-38ac-a8ef-07acc1136664 | -10.84001 | -48.71308 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0bf8295-d148-3211-a9bc-8c05567e5cb7 | -13.38193 | -46.80902 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f12296dd-abe9-3691-8849-41142d6c1d9a | -12.55156 | -47.18209 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 797618ea-6111-39a7-ae88-157e320a00f3 | -12.70255 | -54.06919 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ea47aa6-52d4-39bf-a200-5dcba3b816c9 | -12.4907 | -49.1159 | 2026-10-01 04:34:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d10694b-dfd9-33a2-a69d-edd34928aa24 | -10.60395 | -48.04887 | 2026-10-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d320f50-cc0f-3071-a264-8581815e357a | -12.08854 | -50.70094 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c1dfff4-d0fc-31d7-9928-49d8588f6ccc | -7.49611 | -45.79322 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7366b6bf-f8d5-382e-859d-c94d142795cc | -11.19176 | -45.16444 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 421c09e3-8e5f-38d7-9bd2-7e949615dc41 | -9.2052 | -45.82261 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 043ed65d-9c62-3043-a6da-fe83535648f8 | -11.45192 | -43.42479 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cc79202-b8a8-3956-8ef3-40aeb6a654f8 | -12.39242 | -54.10141 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48e682b9-51a2-3d8a-a800-2c23db19e80a | -9.87073 | -44.94278 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d551acb-54bb-3f39-9e02-d2769ef067d0 | -11.11702 | -43.28088 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 38daf247-3306-3eae-9d05-312f258eb496 | -8.2635 | -54.74415 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bffcd3b-333a-30cd-ac7a-17d6a76fc3d1 | -11.17264 | -54.11345 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0175f625-a3fc-37b2-b8ee-eb52ea37300d | -7.70208 | -54.79829 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7c15390-8be5-3c68-b1d1-b4daa81c558b | -11.26025 | -43.52227 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6711290-33c1-301c-a32e-f95e64e0eae5 | -13.38529 | -46.83214 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c3dee3-fa35-3c8c-a4ec-a65f95dbcf3d | -10.77405 | -54.75808 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a0b26e8-df76-3e59-a838-1a0e9ee08074 | -6.14339 | -53.05851 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b6ce2c-81c4-3f0e-aa66-9e4e3ae67f7c | -11.19161 | -44.85238 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27c30b84-225a-32cd-95ab-28c3293e73f4 | -13.10092 | -47.44525 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05ab4980-b7a8-334e-b52c-a1d60c80deb7 | -10.77218 | -50.52531 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 328481c3-63fb-3d07-8798-fce9589d9f5b | -6.33253 | -51.12169 | 2026-10-01 04:34:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d74ab69b-11c7-3fc6-8d6c-0c8413582477 | -9.12454 | -49.92623 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3641c78c-2d34-36a5-9a4a-8c8b6970a049 | -9.16237 | -45.59793 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb0ebe44-abd4-3b27-a31e-0dfa6b3b5c5f | -8.61951 | -45.37275 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e059847-4045-37e4-8de8-056332d462f5 | -11.21446 | -45.15573 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 160895c6-76c7-3e6e-a025-8695ca95e848 | -13.39202 | -46.83311 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f0ddbec-2f9e-396e-84cb-434127346b81 | -8.96268 | -44.17802 | 2026-10-01 04:34:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92a45824-c00e-3865-b11e-54a617be6b87 | -7.88937 | -54.72392 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 405c8fbb-1729-3d17-ad57-59dbf592ff8c | -8.46449 | -48.47824 | 2026-10-01 04:34:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97983ec8-33bc-31e1-8567-c460956f28eb | -7.19731 | -46.549 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8cf6664-edb7-3666-8129-d7f2519d4572 | -11.65643 | -43.53249 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9deb198c-7078-3167-9697-c0a03b596619 | -11.83502 | -44.75304 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4791604-810e-3b30-ad8b-83364783b962 | -10.72674 | -45.32493 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 812c441a-ee25-318d-987a-444cae7909a4 | -11.26206 | -54.82167 | 2026-10-01 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c9c0922-6244-3e83-90c5-88dd039490ec | -10.7222 | -45.30829 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0f0dcc-0ca6-30f0-b7bb-ccf400edaea4 | -12.74011 | -46.99337 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cb4d39b-6bb0-3abf-b919-d2d856646448 | -11.39675 | -51.025 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e3700af-8502-30ff-a802-c8fa8ea0a56f | -9.2799 | -46.45902 | 2026-10-01 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db21629e-b444-30f9-880e-d654fddf1c60 | -13.53593 | -49.19428 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f77df63-2b94-3645-a158-5a090877db46 | -8.05742 | -55.34056 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a46bf013-fb59-3569-9ae1-2408fe4d23ad | -8.79706 | -48.00195 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 871e03c7-e88a-310f-a8f4-a70bf31e82d3 | -8.83724 | -49.69057 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad3be2d-38ea-397f-8662-cdd648d93132 | -11.40812 | -43.48616 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba27b917-8b9e-353f-97a2-239ed39028e2 | -7.80662 | -49.84874 | 2026-10-01 04:34:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1a67e94-76ac-3758-b819-e82cd5502b20 | -6.36929 | -55.14044 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78a08618-f410-3c70-b804-cfed70beba78 | -13.3836 | -46.82064 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b55812a-2435-3a5f-8e31-053e2941f2f7 | -13.54796 | -49.17705 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f20445fd-5745-31f9-82fa-46b9048d3e65 | -10.84238 | -48.6985 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31fc5357-1c75-3e40-83f2-6cdeb90bac39 | -11.84126 | -50.95105 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a145851-8984-3eed-84e5-927cfc5d6c92 | -13.54045 | -49.18756 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceddbdb2-6789-373e-a68f-365a97ac7a88 | -7.34054 | -55.5984 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b743f47d-a500-31e4-9ff2-cab241e841f5 | -11.19188 | -45.11619 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86ee7079-94ae-334c-912d-284066e18045 | -8.19657 | -45.50128 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae104964-3cf9-337a-af1c-e8e627886850 | -13.17714 | -48.50909 | 2026-10-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa974512-fd9f-3915-83c9-c22759eaacf9 | -6.51167 | -55.37195 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a7921ce-6b45-37ba-8aec-cd16f2fb3973 | -6.36875 | -55.1435 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6913841c-81cd-3b6e-b5be-34b4d1c130d4 | -11.45436 | -43.43484 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 582ff929-2464-322e-a8e6-1c4d04f3bfa9 | -7.54482 | -55.04136 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3a5be1c-ea1a-3942-ae6e-1d907681e6ad | -8.38242 | -46.2921 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88f09ff5-311c-322a-87db-68b866f529af | -12.18044 | -47.38414 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c45cf2ba-87db-3660-bfed-d49d49b5d7a8 | -7.54758 | -55.02793 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd151665-2c6d-3bfb-9485-1cc4fc9fd16d | -6.3475 | -55.32408 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2a1c395-7d76-3ed1-b6cc-8f45120f6f5d | -9.78198 | -44.81048 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63b4a4f3-aa89-3beb-8d12-151b2eae753b | -18.50829 | -45.14245 | 2026-10-01 04:36:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db694faa-96e6-391d-8ec9-d068c7126892 | -19.04118 | -45.66636 | 2026-10-01 04:36:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d653c33b-d054-3642-8a13-85b407e578b8 | -13.66133 | -53.94608 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef15bff2-76f5-39a0-ac15-58a81f3eef5f | -19.34048 | -41.45022 | 2026-10-01 04:36:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e6e58d7d-2811-337f-884d-1f410429920e | -14.86488 | -51.85575 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e93e3b1f-7acf-3388-8ce1-94bc0f895d9c | -19.25944 | -43.75241 | 2026-10-01 04:36:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83180bd4-e9dd-3c05-962f-188edc7288fb | -15.23126 | -46.15716 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ccbe96-f7c4-3e2f-92c5-0c70c5f9223c | -14.43483 | -51.25838 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6350ef9d-4a9d-3e7e-aa8d-8d8afa5d301a | -17.92082 | -45.04221 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17800781-2c23-360d-8145-2046844a766a | -15.65252 | -44.71653 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28439f9-abfe-3e99-88e9-9399b837242c | -17.08347 | -46.82273 | 2026-10-01 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0270c63b-c5b8-3cad-b824-1bf5d4c9b36b | -15.95465 | -45.97175 | 2026-10-01 04:36:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4eb4b7cd-d588-3f61-9220-f75ef6a881a8 | -17.64567 | -39.66486 | 2026-10-01 04:36:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fdbd2a68-afb0-3720-9e95-cecce96de105 | -15.22835 | -46.15274 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 886f372c-a0fc-3999-9f22-94a8692737e1 | -13.67042 | -53.94374 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66c8df91-2661-373d-a0d7-df3b9804ee97 | -16.43096 | -47.18928 | 2026-10-01 04:36:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1803b334-79de-3d6a-bb13-e0bf3eaf21ff | -20.53862 | -45.76785 | 2026-10-01 04:36:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c189f1-db34-388a-af4c-6ee805117019 | -18.89856 | -43.79168 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README67.md)
