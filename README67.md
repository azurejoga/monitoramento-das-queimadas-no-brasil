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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 137cc075-9bd1-3d79-bf4f-bba15d784788 | -10.87496 | -55.71549 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b68b8dc-cd3b-3ec7-89c0-9713f4dcdcf3 | -11.65666 | -46.88366 | 2025-09-08 04:53:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2662f5c0-33cb-3dfa-b606-1e027ae11ca6 | -17.24176 | -46.69276 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a17e5a6-d44e-30ef-8912-94202964617f | -12.25891 | -59.32157 | 2025-09-08 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07fc5a6c-93d6-32e7-b965-420d6f5290c9 | -16.89584 | -45.76528 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 647aeee3-a5b1-3632-a013-ed3268aff52f | -9.86783 | -58.31809 | 2025-09-08 04:53:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2fbae30-2d46-3e2c-9a49-3f2dcd410b81 | -16.33275 | -52.93867 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ac7bffd-8949-34e5-acdc-2e5c7e541d18 | -15.84031 | -52.27048 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afabeaee-ec94-34dc-9953-31dfc62da11c | -12.19642 | -53.92058 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 084ab9aa-2adf-38f6-87e8-292278939178 | -16.97507 | -45.82975 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00c7709a-131c-33bb-8737-1d524d565845 | -16.91125 | -45.82237 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03581318-c6a1-3f77-9cd9-e0f340075535 | -12.89616 | -47.99804 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d2bf566-73f4-3d81-bce9-20569fe76775 | -12.89229 | -47.99386 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a3d170b-1779-3c50-810e-e9ca65e39723 | -12.6161 | -56.98029 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3650303b-0a66-30cf-b05f-62901f68e7a8 | -17.14769 | -48.67944 | 2025-09-08 04:53:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fe7df7a-0eb8-38bd-a930-8387502e3e21 | -17.61808 | -44.83314 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcb6dde9-ade5-3a2f-88b0-b0dd1da317fb | -11.83226 | -46.76131 | 2025-09-08 04:53:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 048a63d8-63f4-3266-8979-1d11046d8c56 | -12.61257 | -56.97971 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f3424f7c-6fde-3146-9ea3-3183e53433c8 | -11.36864 | -50.33687 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a95b9070-417c-3dd2-8e8c-3685ff9a1e03 | -15.75833 | -53.54657 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7086e463-a78a-3c4f-bc14-1a190a591acd | -11.90623 | -50.98108 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a4c120e-4989-3e3f-85fa-8e8a3baaf4bb | -12.52854 | -53.84103 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fdb3904-828f-3b05-9b4a-b0852f58f2a0 | -18.14075 | -43.3952 | 2025-09-08 04:53:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c9180c7c-43a4-3ead-9427-c707054d2ab3 | -11.20942 | -55.01898 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5ae1251-d4ab-398f-ad82-d594a5c45b91 | -16.34361 | -52.93654 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfc9e444-7f66-399a-8b6c-5c02b020cc6d | -16.79425 | -49.09555 | 2025-09-08 04:53:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c110cdf2-428c-3467-979c-30494cec62a4 | -12.55074 | -49.12473 | 2025-09-08 04:53:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d07124b-69cd-3606-9108-a3f8703e3145 | -15.29714 | -43.37783 | 2025-09-08 04:53:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 48adffdc-205b-376b-a00f-8937391a174a | -16.90154 | -45.76254 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd56fd8a-2910-33ac-bf3e-f37dd650a391 | -16.28224 | -48.79041 | 2025-09-08 04:53:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8e8585-360f-3dcb-8ec8-dcfebf12b079 | -14.28393 | -44.99036 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9b7d7a5-ee68-3a15-b1fe-5937188e8934 | -15.74042 | -53.59674 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24feef85-6918-3ce7-8886-660a53edb75b | -11.10339 | -52.06237 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2abc3200-1876-3a30-8cfc-751dedb703a9 | -14.21775 | -53.35361 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e324e6e-8186-386a-b335-44bd26bab1c8 | -16.89324 | -45.78956 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 891a71ca-ee5d-3dbd-8648-1f6c5188eb9e | -9.63194 | -63.0979 | 2025-09-08 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 413d9bd3-9ad3-32fb-9aae-267e7b3b506b | -12.00572 | -47.76926 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8dc7aac4-d39e-3381-8beb-056f407872ee | -13.74384 | -46.90625 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 233c2885-6be6-32a3-92da-40385bf5fbad | -13.549 | -48.11498 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbb06f02-8eac-3ae1-9886-d07bd75c5f55 | -12.8758 | -47.98475 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5330bb81-43c8-3c45-9578-8e4d9369860e | -13.65095 | -47.91654 | 2025-09-08 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1eae5c55-8031-37ce-883d-f558e296f01c | -11.23176 | -55.00795 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f60c4f4c-ae35-36af-a0ff-33386ea9f932 | -16.34017 | -52.93599 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a13d2a8-0b8b-3603-aecd-9cf8cee5da26 | -11.1124 | -52.04852 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f9fb4db-909d-3cf7-9423-b122af08392d | -15.69565 | -53.57451 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb738d90-9a9a-39f0-a082-f33079eaca8b | -16.27953 | -49.57602 | 2025-09-08 04:53:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2fab10e-7f3c-35b9-ae55-5bfcacf2869f | -11.79392 | -62.73909 | 2025-09-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 578862f1-b6eb-316f-83d9-bda65a245ff2 | -13.80828 | -46.26975 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6ff41ed7-205e-36d9-8c84-9bf17f393ede | -13.67197 | -44.22195 | 2025-09-08 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac2a1c8a-13cf-3683-80ee-da3e423a46d2 | -12.62248 | -56.98552 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3539990-d9ff-3056-bbc2-3d968a91a256 | -12.93057 | -54.76974 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fe2f8ba-79cb-33c5-97a4-74de5d57a180 | -9.37059 | -65.93731 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bed84fe0-32ba-3df0-abf3-4c0a62127a0f | -14.80864 | -48.18708 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8e396b3a-b2b3-32aa-8209-a3478b3cca0c | -15.71635 | -53.55113 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4feec42b-c5d7-36a8-9c67-c0e290f51098 | -17.62253 | -44.82851 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba6ccb59-9ac2-331c-8f46-174a1a921be0 | -17.15758 | -44.43289 | 2025-09-08 04:53:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec9ccfe3-bc85-3c24-a660-f571e16d4acf | -16.96875 | -49.31205 | 2025-09-08 04:53:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f538d677-77d5-371e-868a-0ce387709ad1 | -12.93444 | -54.76675 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31251077-fe98-3638-b4f2-ee2f773e2015 | -13.81135 | -46.28539 | 2025-09-08 04:53:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fae3fd8-8db6-3cf1-a4c0-f52fa3be814d | -11.76605 | -47.7511 | 2025-09-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cdf5858-a783-307a-84c4-dd2d92562791 | -12.94824 | -54.76538 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bdac009-318e-38b5-96a2-58031d5eeb69 | -15.84927 | -52.30828 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d645ccc1-c9d2-3390-bc82-2c8abeef6a0e | -11.03685 | -52.06026 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5ed855c-0b80-3587-962e-106d8e6b0d41 | -13.55503 | -48.10273 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b439bef-ff3d-31a0-b269-e80a4c9ae3e9 | -14.99237 | -48.01318 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 240a8af8-599e-31b8-9eda-8523e9d031ab | -16.34935 | -52.94528 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d5b5a82-6f26-33f7-9d4f-aaa2d1890e72 | -15.38454 | -46.42705 | 2025-09-08 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61bb63ce-27f7-37f3-ac92-f44a247cdd66 | -14.79168 | -48.14336 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2708fc0f-8acb-3be2-a1fe-3d690b8651f1 | -11.87397 | -51.00162 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 503da07b-f0e0-3c16-a55a-9bfe302bf0d4 | -15.83368 | -52.28664 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ef941d3-77ae-3ef7-accb-099e69e57262 | -15.00024 | -48.01097 | 2025-09-08 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7346ca3b-7982-39b1-9d11-e337fcdd8771 | -14.81033 | -48.17364 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6403fcf4-115a-3e08-95b0-62ddf63d7b0e | -13.6416 | -43.80859 | 2025-09-08 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 194b52d4-508f-3245-8df6-ecacf08593ac | -10.0884 | -59.18505 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03c6bf0e-8791-3b52-8468-b9c74f5a89ae | -9.93613 | -60.1022 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eefa4b3-0598-3a82-bafe-b59d3c528075 | -15.75327 | -53.57994 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a4482dc-1148-30af-922e-585b8dc6acd9 | -12.49538 | -48.10163 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4110e2c3-536e-3c31-89d8-e6c4e4b58b51 | -17.25684 | -46.69503 | 2025-09-08 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c426e3a1-6ec6-37be-a6f2-d566eb79b34c | -15.53881 | -49.24566 | 2025-09-08 04:53:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c395cb62-160f-3ef6-871f-1c9f050a2501 | -12.52469 | -53.84403 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e43f9630-d3f3-3f73-a68c-18c5a2f2ac86 | -11.46054 | -49.24973 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc952af9-c3ef-3569-9f79-401180387184 | -11.19855 | -55.06514 | 2025-09-08 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a02306a2-f348-3eb9-8aae-409308fc9992 | -13.66782 | -46.96585 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d152836-86d9-309a-b0f3-cd316a764d43 | -13.54845 | -48.1191 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03fa4997-bd62-37ee-9788-013d5821bc2d | -15.84006 | -52.26757 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a678487f-766a-3c6e-a5de-e67638fee276 | -14.09307 | -46.60227 | 2025-09-08 04:53:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 09f6f100-8bb0-3fc5-8e9f-a49c852aa23c | -12.94819 | -54.78715 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86c6a503-bdd1-3a1f-b2b4-2a82ca83e6aa | -11.21218 | -55.02311 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c43b197-d8a7-303a-a45f-2a797a10f022 | -12.41596 | -63.89445 | 2025-09-08 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46a4cb38-ee7c-3c62-a100-87c6640bf1d5 | -16.93742 | -45.7804 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e69cfaaa-33a5-3ea3-9906-437999a246a6 | -15.26248 | -52.38428 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 817cc7e3-22b4-3731-b2dd-85511335d1a8 | -15.53443 | -56.32281 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d82cdddf-b7cc-3c38-b6f8-0e75dd062d22 | -11.11629 | -52.02242 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ee140c3-519f-35db-9e8e-caff42615462 | -14.51596 | -48.79203 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2b249b06-ec03-3406-b519-21f3e88ab7fd | -12.83243 | -52.94347 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 058560b0-3bd9-3c69-a767-2c025abdb4b0 | -14.29159 | -44.87813 | 2025-09-08 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fa36d6-b72b-3d14-904d-58051d965de5 | -15.24803 | -52.3616 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1902244-8286-365d-98c9-376127d840e8 | -12.95389 | -54.81697 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2e16b14-b0b0-38c3-a0af-f036fb5bf0f0 | -15.25206 | -52.38261 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e616ab1-7492-32eb-a719-f978b5f73f7f | -14.87969 | -55.81927 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README68.md)
