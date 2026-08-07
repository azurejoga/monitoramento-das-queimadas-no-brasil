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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a71d559-d718-339c-92d1-96bfb9449e7d | -6.63816 | -56.41562 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acff8b05-8c36-332e-9ce5-2ede6a8f3797 | -6.54353 | -55.17953 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b24c347-c59a-37e1-bd55-b4af49ddb12d | -4.30251 | -47.57383 | 2026-08-07 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed91052e-edb4-36f9-86f4-405ec29e3eed | -6.9177 | -41.95035 | 2026-08-07 04:44:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc164f98-b82e-3b32-9f53-7a1bf4b5e857 | -6.70602 | -58.9575 | 2026-08-07 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 547c63cc-e32f-3419-b33e-e56858840926 | -6.87831 | -56.51057 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0dada12-d91a-386f-bd00-f4bd27f7cf65 | -6.72676 | -58.59098 | 2026-08-07 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 681040c1-1b3c-3e5e-8010-9a0d0947384e | -3.59641 | -49.07361 | 2026-08-07 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b975d1-f0b2-3d90-a604-efdde97a23cd | -6.64107 | -56.4285 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4b5e52-4d00-32fe-9b47-e300ba36460f | -6.5393 | -55.14915 | 2026-08-07 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3eeeb3fe-42f8-3daa-aa1a-a678b20c6733 | -6.71911 | -46.17973 | 2026-08-07 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 790790a2-6e70-361a-b404-19fbda831adf | -6.89086 | -42.43834 | 2026-08-07 04:44:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06633b63-e428-39f2-bccd-ca681328ab02 | -6.64762 | -56.42094 | 2026-08-07 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7775e237-2ac4-3837-9c0d-1b1bbda88773 | -12.58233 | -46.89287 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64691331-69fe-3984-8ef5-ba5e1d84235a | -11.13316 | -54.88771 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11c520d1-343e-3d3a-b0fc-bca214da8169 | -18.42751 | -45.49126 | 2026-08-07 04:46:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68022b4b-a77e-33dd-b330-b2ed5c9dde24 | -12.60702 | -43.40687 | 2026-08-07 04:46:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b44357d-b440-3e1a-9f8f-7b766df4cd2a | -9.17932 | -58.07228 | 2026-08-07 04:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7176f91-7836-3593-ae5b-8132ee9c2832 | -15.10939 | -53.58968 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40265e66-dbcb-33fe-962f-32e703a1f96f | -11.14828 | -44.48141 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcafbbba-c0fb-3ecc-9522-e6895e4359f7 | -13.8231 | -53.72409 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58efc559-b121-3c5d-afa4-3cbcabd146a1 | -12.58346 | -46.90939 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71eab5eb-a482-3b41-a916-923feafaa266 | -18.14441 | -47.98462 | 2026-08-07 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd5c2130-2e73-3c45-9197-d61bee7d64e9 | -11.1802 | -54.86774 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b23c478-dc54-36f0-9b0b-cbc27fe8d3e3 | -13.62704 | -54.67286 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e07ef667-aa6f-30ad-95b0-d02b080af992 | -11.13657 | -54.91716 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39a5df5d-1f5e-3e27-9bf5-7bbd6186c704 | -12.58055 | -46.90484 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64df8349-9d3f-3231-8a69-850c52e3b49d | -11.15543 | -44.48769 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 30f59235-479e-39e2-9a64-b7de19057cd3 | -12.86704 | -52.81716 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 527085d0-d66e-3ac7-9149-a28816cca6de | -12.55354 | -46.94168 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89e1365f-e4fb-347c-99dc-f85cbf9dd0a9 | -14.22756 | -48.50866 | 2026-08-07 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bad1cc6-d40f-305e-bd7b-c024506d5e04 | -11.07872 | -47.79739 | 2026-08-07 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c549718-d13a-3349-a45c-4282ead0b25b | -11.14643 | -54.91083 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95134bf9-96fe-36b2-a27e-58b03a1a22f7 | -15.86933 | -43.60257 | 2026-08-07 04:46:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3fe931a-91b0-34c6-a293-c623856ec727 | -14.21179 | -40.9876 | 2026-08-07 04:46:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5ab5f23-e30c-31d0-b32c-26e174cd84d9 | -12.55064 | -46.96128 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b588f1d-60c6-32ea-9ccd-dbf34ad9c76b | -11.13524 | -54.9003 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63262e4e-290d-38fa-b5f1-fd507272d01b | -12.4887 | -50.36839 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c9f9388-6afa-3d63-a2e3-55c9d4937b46 | -12.59518 | -46.9031 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db0d7030-f756-3f4f-9640-cae1640078f7 | -15.07735 | -53.55622 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9aec9bb0-ce1d-30bd-bfe1-d4b66e5a067f | -13.42579 | -57.04103 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5abb8a7-4d19-3558-a7d3-ef155d3fd1e0 | -11.12888 | -54.91143 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0d77e83-d21e-3e29-a6e9-9c6598708e04 | -17.53833 | -45.35433 | 2026-08-07 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06831a81-ddba-3ec8-a909-fa2c2ba058a8 | -12.57471 | -46.89575 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50c55d14-6ca2-3e14-abf1-aa42b895bbfa | -12.57995 | -46.90883 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 610a1639-ed51-3de5-88de-b2d8774134f5 | -13.77878 | -48.50205 | 2026-08-07 04:46:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87eb9eb9-ec82-3ecb-b423-c1d45dbf0e20 | -15.58313 | -54.29152 | 2026-08-07 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42c6e060-3fe4-3483-9ed6-ad64d90d9307 | -14.21431 | -53.33129 | 2026-08-07 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1c6b4b5-1801-3e54-ad2e-91583a6d47bf | -12.55642 | -46.94649 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7629390c-c4db-3b1f-85e3-b4468d6d224e | -11.17248 | -54.86233 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c40cb92c-33b4-3455-9340-d3664f4e62ee | -13.42044 | -57.02602 | 2026-08-07 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f064437b-91f2-3462-9381-76cad3034cb9 | -14.30966 | -54.73336 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b56f941e-3964-35c8-af28-1a232855898d | -14.42669 | -45.6718 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a1ea399-5ced-30f8-9e9c-136552bfcb43 | -12.55584 | -46.95037 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fa3b4c7-5f53-3c93-8b76-92a9d0803cdf | -15.08101 | -53.5569 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cec641e-7ddc-3a59-b3b7-564b2148d559 | -12.87431 | -52.81846 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8387185e-edaa-38ce-95fa-b1c57eda96a6 | -14.27012 | -45.28839 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c1cb8ad-9aeb-3c75-806c-f6bacd2ac0b4 | -14.43051 | -45.67236 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 836a21d8-09fa-3796-85a8-43d51254d619 | -16.18167 | -46.22509 | 2026-08-07 04:46:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 999529d2-7122-3296-a181-d0c2ee34a4a1 | -11.7983 | -46.3822 | 2026-08-07 04:46:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbdf22f6-108b-3fb5-b1d6-7b01f23ace4f | -14.42979 | -45.66411 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db62f0f3-045c-3b76-8170-78e83660182a | -11.14715 | -54.9068 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95adc533-75d5-3eac-bcb5-61930866037e | -14.44028 | -53.34621 | 2026-08-07 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e0a9f7b-3990-37e0-8156-360d75efe859 | -11.72693 | -56.84583 | 2026-08-07 04:46:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b05a962-f40a-3c5f-9663-ab6b426feceb | -11.46364 | -44.56416 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cab0b5c7-6f7d-3f1b-ad9f-6ce6f149ec24 | -17.53023 | -45.35305 | 2026-08-07 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08c5aac6-5335-394c-8a8c-fdc4a4f9d4f7 | -14.42465 | -45.67319 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17f4532a-4b16-3081-80ee-afcdd508e6b6 | -14.27529 | -49.71432 | 2026-08-07 04:46:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbc02ab3-e5cf-362c-a845-7b7ef391d8a9 | -9.08999 | -59.48001 | 2026-08-07 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f63a4b0-d3af-3c03-b3ed-17e15c7281a9 | -12.14133 | -48.26254 | 2026-08-07 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cfc6fd-3461-3ca1-adb3-880e1288b65f | -11.17599 | -54.86697 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f48a4bf-31b6-35e3-b67b-6752f271ba10 | -14.42356 | -45.66642 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b049293f-eda2-32eb-a17b-eaf2f1bd2285 | -18.14501 | -47.98051 | 2026-08-07 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28442faf-64ff-37f1-b3b3-186f00467e0c | -12.00593 | -49.28146 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3682c278-9fe7-3f69-85d0-8de69adfda77 | -11.14365 | -54.90198 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e74d886-cfab-377f-9f09-93b5e815b0ff | -12.51785 | -55.78635 | 2026-08-07 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 26a64c51-5f16-35fd-9d98-833b647e909b | -12.86995 | -52.8221 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81fef7c3-6591-31d9-b129-c9aa73ab0858 | -15.07927 | -53.5886 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| c8ef5dc5-5c2c-3cbe-aff3-bba2c1c6a5c4 | -17.5338 | -45.35735 | 2026-08-07 04:46:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05485e1c-c314-3232-89dd-468d6634f4fd | -14.2655 | -45.29283 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e877e711-490d-35be-9946-38f610bcccf8 | -14.27415 | -45.28613 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a96b1c4-5985-332c-b507-6c0d50fe4bce | -14.29689 | -47.17222 | 2026-08-07 04:46:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c80309dd-83d0-3d62-bcab-bc0bc17368ca | -14.27347 | -45.29117 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5d2b138-cbd0-3a47-9c4e-ffacd0ccec68 | -14.29336 | -47.17168 | 2026-08-07 04:46:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 009c17c6-4bf3-3ddf-abe5-8970d37c4332 | -16.1848 | -46.22773 | 2026-08-07 04:46:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9f9f009-e29f-36dd-8689-2049c348346d | -17.11967 | -43.30048 | 2026-08-07 04:46:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a53b7b08-be33-3333-8807-e0efb69acfb8 | -14.3506 | -54.91884 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40941eb4-50e0-3fbb-a96e-4602623d7b8a | -14.3367 | -54.92719 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13c6b9f1-dab0-38b5-baac-a993dc931f20 | -13.76967 | -47.1847 | 2026-08-07 04:46:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde6d3ea-5981-3cdd-9d26-0cfb9fb6bea2 | -11.14294 | -54.90597 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd18b563-ecc8-3b91-985e-359db1f0f862 | -14.35248 | -54.9082 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62c9971d-6817-3ffd-8263-b88793847bee | -12.56115 | -46.93874 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c226be0-d569-3109-a7d5-fb3015808b2a | -12.63322 | -46.88924 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3059916c-4772-3185-9811-d01561def7df | -14.42218 | -45.67602 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3000f066-a9cd-3256-af7b-f7af004da179 | -13.96542 | -47.36831 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aa93f9c-4903-36af-b17b-766577836b8a | -13.93751 | -47.36394 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ea95f3d-d3d8-383c-9777-e87dd3f41d8e | -9.17393 | -58.07124 | 2026-08-07 04:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6817cdcb-1f21-37d5-a142-b2ebe712e5ea | -15.09873 | -52.76141 | 2026-08-07 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3fe85e70-c88a-3a36-944c-7f84b00eda35 | -18.1515 | -47.98568 | 2026-08-07 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e018d22-216d-33f7-86b2-e7d47b4e3cd5 | -14.32841 | -54.9738 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README16.md)
