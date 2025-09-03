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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b80613de-7eee-3249-98c7-a8f51e36d513 | -12.61061 | -57.00518 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a97902-3d3a-31e1-b845-65dc270c66c1 | -10.24601 | -61.76022 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fab8bfc7-5c4b-3ff6-a582-4af844cdbcad | -12.64023 | -56.99445 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acb878ab-ccd0-3850-8016-fbb5933bcae6 | -11.94359 | -50.59879 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaa22cf2-d376-3660-a6e9-4707a0a2a425 | -9.62847 | -47.85889 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ae37254-f398-3081-8df8-fa5cdb78967c | -14.56079 | -53.05277 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36806f7a-6acc-3d1f-8dae-1a91a1e8fa51 | -11.44842 | -47.29844 | 2025-09-03 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0221c8e7-df23-3816-a4f6-a548b20553ce | -11.60774 | -52.07774 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4664386c-f9ab-3cda-b737-54ff00f018a3 | -12.99055 | -54.75498 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4509bbf3-e754-3a45-8f01-efa4f5984715 | -12.92078 | -48.08348 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e19d0d74-7822-3a05-9203-dbe8709a866d | -11.59296 | -52.12017 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6a60007d-53f0-3607-94a8-82ec988aa07f | -11.61658 | -52.07906 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12417bb3-94ee-3950-a386-1ebf0d989fc9 | -11.80498 | -50.64042 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7d4cb6e0-76a6-3271-bfad-d6ce2b2c8ca5 | -11.67518 | -52.17353 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec96b3e5-69c4-3013-be35-ad083aab6a55 | -10.12897 | -47.44331 | 2025-09-03 05:14:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f533e8-0ce6-3009-bd32-84efd35fa0d6 | -6.79684 | -58.99404 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38fccdf2-d8da-3007-b0f5-996ad1b094c9 | -14.57524 | -48.04867 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e827035d-a702-37e2-af65-89eb536fc0f0 | -11.62281 | -52.0666 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a94e596-b2d3-3bce-9d72-aa5969356c64 | -12.89369 | -48.05873 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c939d04a-559e-3869-aa69-39500c907b16 | -11.41916 | -55.18641 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a2b789-1554-3dfe-8183-043f3dcf8418 | -12.62884 | -57.00036 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd9ef82-5f94-34ea-b36c-f669812f14e7 | -11.00742 | -46.93149 | 2025-09-03 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83d99b38-4342-3b20-b650-30d926e34aca | -12.94528 | -56.95988 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 50c61003-0dce-3f85-be4e-d7752c2d62fa | -12.63396 | -56.98964 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9afeedee-2ce0-35de-ae6f-85e9fb1b41fb | -11.59914 | -52.10777 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4743bc50-b4a2-3249-bd7a-160b5f37cd9b | -12.94302 | -56.99805 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ec9dd5-b587-313c-a060-68e8878474e4 | -14.34777 | -52.80568 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 335c69a1-1d6f-3dad-924c-a25cd6b036c3 | -8.07567 | -47.60984 | 2025-09-03 05:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69a49a4e-47fb-3496-b3d3-1b9808c7aac9 | -14.8 | -48.20077 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db9f4c99-e9ce-3f9d-a769-3167e74fe2b9 | -8.36307 | -52.53977 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171af3a5-23ea-3feb-b20c-e748d4254d23 | -9.79464 | -56.61112 | 2025-09-03 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9812e7f8-664d-3c75-9723-4b97139dd225 | -9.09108 | -58.8881 | 2025-09-03 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c791e5c3-866a-3158-8b47-402d829f3330 | -10.88158 | -55.74716 | 2025-09-03 05:14:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59d11da8-baca-37f3-8820-8e1e02dd067e | -12.9899 | -54.75968 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea5f6e6b-174e-3e5d-8f50-11cfcac0b21b | -10.45258 | -54.78074 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bbbe572-4a61-3df6-8c6c-76a40da813b6 | -9.64614 | -47.85738 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f77c8d04-0eb5-3c5d-bd35-568968c80864 | -11.58619 | -52.13686 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c80e43d3-aaf7-3558-b8c7-674c0473e330 | -13.02024 | -56.87337 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa9f8876-3299-34f0-ab92-9aeb7b0b08a1 | -13.29066 | -46.83728 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6888262-b921-3ecd-b6ed-74d20171045b | -10.45132 | -54.78934 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| deeb488c-4258-39e1-a34e-a775c7899436 | -11.85364 | -51.52898 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 581fe63a-1ac0-35d5-a6f2-0c614e91b069 | -14.61211 | -48.10267 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d104427-90f0-3fc4-bffe-e91e53dcc94b | -9.7496 | -46.91569 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b79c361-624b-3c0c-a6e1-70300fc2cd8e | -14.34391 | -52.80092 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e39ed521-8bf9-377c-8f14-c578e76d9998 | -11.63791 | -52.0554 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26219df5-48d3-33df-a110-38b4485fd151 | -12.94529 | -56.98302 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 730da1fe-822c-3748-b3b4-9bb82173cd16 | -13.09098 | -57.12431 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ca9bc9-83c7-3caa-977c-23b4fbc75f23 | -15.01944 | -50.07184 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa9efb9-1685-33b4-9ed8-6fbd39cb614d | -9.95494 | -51.63158 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e428ecc6-441b-3100-9ff9-fb86b3be3d0b | -7.71824 | -50.29548 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9685c2a-875c-313e-87c9-27d19452bd78 | -9.66063 | -47.03375 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a3a3b91-457e-330e-94b3-785b67fac5bb | -14.97261 | -50.19885 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1bd35b41-43e2-3f81-9a2a-368b92b664cb | -6.67353 | -58.76179 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70de9c8-8caa-378e-9593-499200c1a068 | -14.7984 | -48.19887 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d21d6b26-1512-303d-b2db-134928329be6 | -10.48217 | -50.35508 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 996f7354-9368-3101-b01c-74c1cef61d95 | -9.13273 | -49.64731 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69555e56-ac51-373c-96ad-5625d2262650 | -12.49148 | -53.84033 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5f1605d-78dd-33ce-a7e5-b1974b8e9547 | -11.1912 | -55.01663 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 612d6233-d805-3777-867e-76ba1db999b8 | -14.58773 | -48.04612 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 696fe901-8599-32d1-83db-947ea11e517b | -13.09954 | -57.13713 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc7fe288-9d0b-36c1-9760-dc5bf9ceb25c | -12.94643 | -56.97549 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a07cce07-60a4-37d8-ac23-2ba8aca25287 | -9.75626 | -46.91206 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 039fd1e3-0d9b-3a47-9d8e-4eb094a7226c | -13.00709 | -48.09772 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22b1e83e-69fb-3121-b59b-3cbac55ba4c4 | -14.56785 | -53.03244 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0905687-570b-33b6-957b-3ac08396c3b9 | -14.83 | -48.36729 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d130d7c-86f7-36bb-b524-4997a218ca76 | -10.45614 | -53.62015 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc77660d-8ce8-313e-ad61-0a49ec217067 | -15.02476 | -50.07247 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a7c8cf3-740f-3de4-a58b-431de2075e11 | -10.47509 | -53.62822 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a7cab4-f812-3a81-b553-989291dcacd3 | -9.39892 | -48.04644 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c6762ab-bcd2-38d4-abe9-1d902f35ff17 | -9.9517 | -51.62223 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce5dff3c-764f-332b-bf3f-779ab820c794 | -12.91002 | -48.09406 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5bc5da6-eefe-3674-afdf-09e6c88e3d5a | -12.60719 | -57.00465 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78e609b4-2846-355e-af30-df8305b50ce4 | -11.8057 | -50.63492 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14138ef6-127c-3c75-80bd-9dd507416b86 | -13.48279 | -46.8225 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e89efe8-b315-3c79-8999-a113436281d1 | -11.64922 | -52.03905 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4be8a18-1f9d-34e3-ad9e-3e52286e4a27 | -15.03288 | -50.04909 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d02686e6-3dc5-3488-a9c7-a0ac90de01b6 | -9.5703 | -55.39362 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90bcf378-720d-3f43-bdcd-04961c23348b | -11.21044 | -55.06363 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07378dc4-fe16-3a73-9fad-e8be4beb798c | -12.92011 | -56.94041 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a707dd6-e444-3d85-ab32-4eb78c7dd4e3 | -9.13352 | -49.64149 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| de041b25-a9f2-3904-915e-ac4e15f68341 | -11.60501 | -52.13066 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98e4a4ae-b67c-3802-856e-73b1d806664e | -12.49547 | -53.84093 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 341ceb1c-9946-37e0-9e03-9e02fbe6eb11 | -11.2141 | -55.06418 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53dcb1d4-78af-33e8-82de-0830fa8c82d6 | -12.97814 | -48.10435 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad86e311-ac27-33fd-884c-f66c6d9e811d | -10.08647 | -54.76238 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a04b91e6-3e63-3f31-ad90-43566bd38e08 | -8.065 | -52.35257 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76bd0cb8-8421-3424-8e79-3e23b7daf21d | -14.4065 | -51.67686 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a43ca18-680c-3d35-ae46-afe7259443c8 | -10.24823 | -61.76967 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1388ff3d-a3a1-3a55-b8e6-e6f93c459ad9 | -14.60148 | -54.58705 | 2025-09-03 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41d15a14-85ac-35b1-a6e7-c75506dcf311 | -9.39281 | -48.04941 | 2025-09-03 05:14:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85c2ecef-9274-325c-ac6d-2dd96dd65ae9 | -12.93958 | -56.9744 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a8a452e-990a-3259-8383-872a472d571b | -12.9627 | -48.08314 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63d2fc32-4446-3df7-ab4f-cffece6c62ef | -10.48381 | -50.33249 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e949953e-4b9b-3a0e-a2d3-58db17f6425f | -14.40271 | -51.70726 | 2025-09-03 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc2ce340-aea7-3968-9c77-fda42c5d39d5 | -11.65457 | -57.35535 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b883f56-f06e-3fc2-b4b7-3a38b464252f | -6.79344 | -58.99348 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab90e01-cf54-3811-b994-a8be5e3200da | -14.78467 | -48.15947 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f451c703-0b27-36b3-b426-9da064674dd2 | -9.64043 | -47.85646 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78a8c3cf-7654-32d5-8886-fe3c8472b414 | -14.97186 | -50.20547 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7c68dd3-a77e-3a47-8d74-f8ce9ca90172 | -12.91791 | -57.00182 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README91.md)
