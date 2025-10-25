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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2effb26-6dac-3f73-95e8-1e08d6d5d231 | -8.02691 | -54.88949 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de9fc6fc-f5f1-3917-a37c-d169d2b3ae31 | -6.91885 | -45.16698 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d4539ea-124d-328b-9601-16bc03b6f3d0 | -10.94779 | -50.29635 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57420eac-118d-396b-b1c2-ce3efeac4c40 | -10.64218 | -45.23177 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 961925dd-e45f-3e78-bfeb-def17edeec20 | -4.84168 | -50.93319 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f98054-5cc4-3239-9a7d-94a886b91d4f | -5.29253 | -48.3644 | 2025-10-25 05:10:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b962225-7103-3be8-b981-4864b0a5ca87 | -7.99513 | -49.2536 | 2025-10-25 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8fcf7bd-fd0f-3ac5-853f-2841ee0da858 | -10.40936 | -44.74638 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49d23a39-7eac-337f-b616-f2e90dfe3593 | -4.22028 | -55.74742 | 2025-10-25 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7ca7c6-56fb-370d-9c81-b55b398236f8 | -4.83014 | -50.93309 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cacfecff-0749-30f4-a8bd-82eae9a17978 | -6.41804 | -46.18713 | 2025-10-25 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62fb9a14-4583-3bc9-bc7a-641486fc322a | -3.25552 | -52.91037 | 2025-10-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f861569-5be7-3b79-8e64-c8d9e75a7252 | -12.12243 | -46.71716 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41f79922-2191-3483-beea-92f122ac540e | -15.47462 | -50.45863 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9d7f412-0876-3d95-861d-8425b7d3e2b4 | -12.08282 | -56.67773 | 2025-10-25 05:12:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89c23ebf-0723-3d17-8383-755aa604d5e0 | -11.09627 | -54.50277 | 2025-10-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ded536b-faec-3650-a8cd-dcb924a9fcad | -12.47927 | -61.05211 | 2025-10-25 05:12:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f283097c-b3ea-3812-9e24-374e0d15a030 | -15.47354 | -50.46804 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6965c7d8-8220-3b6e-9a1a-cd6f4669d354 | -13.34471 | -47.41216 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a52877c2-a49b-341d-b453-66e3b96627ef | -14.46661 | -47.92747 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6749773e-23b4-3cad-8756-9cb079fc6590 | -13.90614 | -48.42301 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 97dedc15-4c84-376f-81ee-e1063d0eabee | -15.93326 | -56.11121 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53bbda8e-3003-33a4-98a6-b8a038dd2c2c | -10.98952 | -58.46399 | 2025-10-25 05:12:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 256c137e-b039-3e81-a045-a03cf96f85f6 | -14.46016 | -47.9308 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5363842-7b27-354c-bbe6-ac22553f1472 | -12.78145 | -47.37862 | 2025-10-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab84404e-18f0-3726-838f-9b8290b4f24d | -13.03641 | -47.38572 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9cee6f3-e202-353d-8996-923c96b1609e | -14.17749 | -47.30397 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18288cec-5e27-3b66-8059-819eec634e68 | -15.9399 | -56.11666 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 12239f08-9196-3149-8e77-76431f9128ba | -13.62871 | -47.61214 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6305337b-4afb-3b6c-a11c-bcbd9c051176 | -12.90143 | -48.58756 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9182e105-46f2-3651-964f-b9ca93c77c51 | -12.83947 | -48.64924 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b59eaa5-ee98-3212-a50d-67f262b66f4e | -15.50694 | -56.03606 | 2025-10-25 05:12:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 718bccbf-b4a8-3e93-a500-c88bcd6cea19 | -14.94159 | -48.12875 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e455a190-40bc-33b3-a299-b1afa652ea83 | -10.60283 | -57.77906 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77324809-665b-3873-a9f5-30135b66c153 | -14.55922 | -54.17365 | 2025-10-25 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8b7001c-62c8-33c7-8f75-b7aabf73ce4b | -11.84671 | -49.86173 | 2025-10-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f2bffd7-0968-387d-97c3-2ef675e490e5 | -15.23745 | -47.93785 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b21283d-bbd6-3948-98a2-1e43aeb83455 | -11.10143 | -54.38665 | 2025-10-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbafbc7-422c-348b-8fa2-915931cbacd2 | -12.84544 | -48.64719 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 53f52fac-b2b3-3d2a-ba5f-5271eea6ce8a | -14.17204 | -47.31001 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e59519c-e15b-3056-b97e-776d08fb92f4 | -14.93309 | -48.5239 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc90e46e-6242-37e1-9678-699aa863415c | -14.18251 | -47.3166 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49a05c5c-b389-32a0-a3a5-b943d534fba4 | -11.10078 | -54.39122 | 2025-10-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a98b345-465e-3a30-8313-c25ce1b74c9d | -11.87893 | -56.39994 | 2025-10-25 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d4f6d49-65cb-3ff5-ba90-b8be0bad5d4b | -11.95934 | -55.25713 | 2025-10-25 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 667c8973-1142-37b7-8795-9eb5f9d9f22b | -13.06565 | -47.56581 | 2025-10-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eefee3f-5b9d-3497-a6e8-1ee405ae0383 | -14.93829 | -48.13372 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ca347eef-c935-3a7f-93a3-c909477611ba | -17.38443 | -45.50021 | 2025-10-25 05:12:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af31017e-affb-386f-a71e-f550731d6d32 | -12.17813 | -61.8401 | 2025-10-25 05:12:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aac70ca5-caf9-3cbd-b96f-9b127fb1604d | -14.4756 | -47.90058 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 143d2f36-9443-3931-86bd-0fa9829f234d | -15.24309 | -47.94263 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b37a0d72-2bf4-3310-af26-4e1ae407437a | -15.00562 | -49.98927 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9aa216c-23f8-3541-87f5-cd3206fa1f48 | -12.77589 | -47.37315 | 2025-10-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eec37901-9497-350d-9eac-f7a2ba1113dd | -12.11274 | -47.39272 | 2025-10-25 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 721c101d-13b0-3caa-a4b4-19c92a81f812 | -11.5051 | -60.73161 | 2025-10-25 05:12:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce2a76b2-df53-3042-a1e2-d6108c4d039f | -13.62788 | -47.6096 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 713f0ff8-cc51-3068-9945-8452cfe278d3 | -14.46063 | -47.92639 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 874dc1b8-f8fc-3f82-81c8-0c7478d350fc | -14.53962 | -48.03805 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b30baab9-91c7-383b-9545-35b37923caab | -14.9001 | -52.45636 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d576a3-790d-3fd4-b54c-c4aad37fabfe | -13.357 | -47.41703 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ffcde5a-39fd-3a3e-bd68-06289690d3d4 | -15.63021 | -55.84687 | 2025-10-25 05:12:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 146b0ac8-77e1-39a1-8e16-4597bcbef65f | -15.50242 | -50.44523 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e2d5a8b-5f8b-35b1-bf78-f5c31c91ba34 | -15.0911 | -56.42208 | 2025-10-25 05:12:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ceea23d-78df-3160-b0cb-becfbba3faa7 | -11.36054 | -55.12909 | 2025-10-25 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e65dafca-fc7c-3c74-9c13-5b8add3155b3 | -11.62251 | -55.00049 | 2025-10-25 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29d3c52a-7bb4-31d6-9a29-5a0bfb1ac384 | -14.86151 | -48.08478 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b0177831-c388-37df-8fa0-4352a695d59e | -13.81113 | -52.80506 | 2025-10-25 05:12:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1423ae6a-d11e-3d23-a96b-394b35030b92 | -14.53917 | -48.04198 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffe59d6b-76ed-3630-a971-0bc9e4fce982 | -14.89618 | -52.45122 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ae5171c7-4160-31cc-a774-bde45fb6cd30 | -14.93501 | -48.13356 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bda2e48-54a7-34fd-8aeb-0a51daae5b00 | -14.91532 | -52.44408 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e9f39e-ad36-3039-bbfc-3bcd15574507 | -14.53646 | -48.0397 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feeb39c1-6799-3b09-ad4a-93c672e82bbd | -13.05032 | -47.20967 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd2d9242-54be-34cf-8adc-e591437fee28 | -14.89089 | -47.86201 | 2025-10-25 05:12:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aad8015-b679-3edd-92c7-a797cec1b5b4 | -10.55166 | -56.80764 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89bd41f1-8ad3-390c-aaee-0c13c491a050 | -14.86512 | -48.0822 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 408b5067-4498-3aec-99bd-25d9212fca30 | -12.01921 | -57.90053 | 2025-10-25 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c00630d-1888-3293-897e-6057cf3bd3c1 | -11.39912 | -55.17712 | 2025-10-25 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 809e3e87-ca43-36d6-968f-5ba24d1a5b55 | -13.6547 | -48.1875 | 2025-10-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6959c07c-5578-3f61-8d01-a9b7afb346f6 | -10.98625 | -58.46342 | 2025-10-25 05:12:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2cc9bfc-5f64-3e9a-9f4a-1b513b82a19f | -14.88835 | -52.44075 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 255baa5f-5c89-3976-a305-00e580fc465a | -13.91972 | -48.4068 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ffaaa0f-0137-3d99-a8d4-9e4fdcec9fa9 | -14.45369 | -47.93433 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20979e83-aa59-3064-87da-1067e6ddebad | -10.39133 | -57.49805 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aaa95ab-1c0f-30d9-9d05-e79327d1f3a6 | -12.04604 | -54.2374 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbd39935-a63c-3913-9d4a-9096b1ffac32 | -11.78458 | -63.18091 | 2025-10-25 05:12:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2c1fb41e-813a-3ab6-b541-99b932b8fe49 | -12.89466 | -48.59647 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a09f904e-54ec-33af-a6b1-cf7aedb200b8 | -13.33844 | -47.91397 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 467bb749-5187-36e2-ad98-b11b8a203418 | -12.13319 | -46.70995 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90503315-c5e1-3818-acaa-8b0c5f404ead | -12.30851 | -45.52264 | 2025-10-25 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52a692dd-e7f5-3d00-a0ff-4873af32c334 | -15.00597 | -49.98617 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef9f59ae-7075-3b82-b7c1-aede7a484bbb | -11.32878 | -53.93697 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 521ce003-5ab1-3ed5-9f2a-6c166e285611 | -15.0007 | -49.98522 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2465225-c5d1-37c6-a1ad-757b17b15459 | -11.7191 | -59.12205 | 2025-10-25 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c05e68e-e66b-3d57-8fcf-7f3e0d686d69 | -14.86087 | -59.63562 | 2025-10-25 05:12:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 527da48d-9bac-32b6-b9cb-ee2f9e8d1131 | -14.92722 | -48.52357 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fb79b9f-7c98-3c1e-b41c-4b7523e00bb2 | -11.97758 | -58.06007 | 2025-10-25 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 098e07c4-f809-38b5-a29a-3929bbc5b226 | -12.04618 | -54.2457 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e693f8df-556e-33b3-b3c3-05ca95e9e821 | -14.20934 | -47.30141 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa29c0b1-0461-3a5f-898d-e51c73122e98 | -12.88549 | -48.59987 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README56.md)
