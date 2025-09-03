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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 883a59ff-d586-3dce-9d5a-93809e0abe96 | -6.22515 | -43.4041 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9b36388-e535-3084-bd7e-48da6707d170 | -11.60451 | -52.13427 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c30c8965-9e75-3f77-aa70-817cd3f6e999 | -7.9389 | -46.54338 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79998d23-d448-3921-9cbc-f5df0f81eba5 | -6.26408 | -42.63314 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ea792d0-23aa-34af-a2c4-5ba4da3449fd | -11.64898 | -52.04435 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a399b62-943d-387e-b3cb-3ae483ad6915 | -6.82251 | -52.835 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f70bed2-d2ee-3bc3-b5d1-52a4932e76f7 | -9.14369 | -49.64488 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5443dec9-9f6f-39d6-bae9-8723bfcaf2dc | -11.62093 | -52.07221 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d08052f4-e23d-36b5-a6ef-4153d69e1d0b | -6.77816 | -52.80935 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fd844d2-83f2-3705-b7cc-422b44bdac54 | -4.24475 | -55.53281 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 396ac8a2-6caa-3ca4-9b59-7c5f8236dd5a | -6.85102 | -45.55141 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ca4ba7a-0ab3-3c0a-8604-d32a38082e1d | -5.31926 | -55.88044 | 2025-09-03 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 363b59d8-5879-3239-b705-e648ebcbcf54 | -9.63502 | -47.04353 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d919532-c900-39a1-91d5-066dca1a3cfa | -6.12244 | -44.13559 | 2025-09-03 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 401e4172-691a-3515-b64c-0853ca253f96 | -6.25775 | -42.64111 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9dd4e71e-d230-3bba-86d7-a6639a81e2ce | -7.25189 | -57.54965 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8fbc143-4165-3613-b55a-2a26d1ea019b | -11.06491 | -52.08359 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c937af85-f036-3ae5-97f1-d4069a1eafca | -10.14569 | -46.29681 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0698dd1-1cd9-36ed-83a3-692a66f0cf2d | -7.70087 | -50.3091 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7d9adc6-cd08-3861-817b-97d9ff46eafc | -6.45449 | -44.68105 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72f246ae-bc14-3566-9710-42bc243d67cd | -9.76472 | -46.91901 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 70935114-c215-3960-875e-2b005c17d3ec | -10.25959 | -51.11306 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9547a61-1af0-360f-b673-f7c7b5469849 | -7.69938 | -48.74872 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b32d0ced-ea2c-3b15-a844-0ca5b7c8076f | -11.48896 | -43.21747 | 2025-09-03 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 823db0bf-9754-3881-9ec5-3e278ebbb8e8 | -8.8912 | -45.78941 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e2ee6eb-3569-3739-8468-abd71e883f6c | -6.79361 | -44.09141 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1af5b296-b1f8-3d62-b10c-2461a768a702 | -5.82999 | -46.35772 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b55ba7d3-eb7e-3b81-9e9e-d14d857974b6 | -8.8769 | -45.82843 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb2e48f3-b540-3b70-8079-dfcc424ad1d2 | -6.25806 | -42.60133 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb4d01df-70d6-3d7a-98ca-53286a6bb3ea | -6.99624 | -43.25604 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b68f8e42-f2bb-3fb3-b4d7-67172bfc54f8 | -8.45537 | -47.35125 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf0717a-b401-3bd4-a859-d6a6fc120e77 | -6.24316 | -44.84349 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6552ddf-8222-3de0-8dd6-c321ef783e1a | -8.36854 | -48.31203 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b5a70fe-13d3-3dd0-b68a-32b5f11d3ac5 | -7.79853 | -45.44905 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a2c0f1f-ed78-39ba-92e6-2d57288638f3 | -6.27593 | -44.51337 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4eed1b6f-1c91-3fc2-b43e-35d92c7d6c1c | -6.26295 | -43.51337 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fef879b-8461-3469-9410-aa7e9bc1cbb0 | -7.93154 | -46.47045 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e83882f-f0c4-3218-925d-c2a0d87f317f | -6.84104 | -52.84906 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52979db4-1d06-3987-9512-f8327cc0c4a2 | -11.64019 | -52.05732 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ab485f8-8acf-3612-9e99-5995c77bf8c9 | -8.46238 | -45.06656 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e4c7c6d-9415-39dd-910d-6b59d5b8aa96 | -6.28101 | -43.5925 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f761135b-75eb-3287-b7db-c58eafd6b050 | -8.04907 | -52.35283 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 498e1401-fabf-374c-a882-fadaefeff630 | -5.42732 | -47.11409 | 2025-09-03 04:46:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9afe542d-be2b-3807-9739-31a7d41084b4 | -8.85924 | -45.83022 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b7c43f6-a0b3-31da-8791-fda3601d2ed6 | -8.30826 | -55.09596 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b64cec31-adf4-3520-92aa-affc9a661199 | -8.71394 | -50.39862 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5afd8d15-b92e-3516-a25d-b9a64991243d | -4.13769 | -54.89776 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 645661c8-7005-31f8-b0fe-2526f446a384 | -5.54489 | -51.33727 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a66f314d-f509-3fcf-b1ba-f80b0781a1bd | -6.50396 | -43.57384 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad1531ab-4472-318b-94bf-f09f09f22372 | -7.71682 | -50.24933 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c3f6996c-78f7-3158-911d-5b180b55f660 | -5.56115 | -43.08192 | 2025-09-03 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7056a095-a32a-3a68-8d27-68288550cbc1 | -9.6649 | -47.03347 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb1a47f2-3069-34d5-9696-9e071f12ccaf | -6.69225 | -44.18087 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35af27fd-40b3-3415-a8ca-9aa83b478748 | -6.02698 | -46.00469 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01d01da2-760f-3e07-99bc-f6fbdded5a49 | -5.84811 | -43.01348 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 03777075-74d6-38ac-85c4-5ee365f5795c | -8.34871 | -52.52348 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e69daa8-6bd6-3447-ad8e-ff55e81f647b | -9.95359 | -51.64077 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3fa885-7a31-34a2-b80f-149b4d896e55 | -7.53227 | -47.44062 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42f825ca-a684-3424-9d0c-58d66abe8a13 | -9.91607 | -51.62059 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e116cd-3ee6-3d65-8678-c01c1f5b8183 | -11.07413 | -52.00268 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38a1d381-e458-3993-8746-59b306919b4f | -6.67588 | -45.92266 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7238e46-b2c9-3aa1-a06e-32f8c4858ad2 | -10.28072 | -46.50126 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca80f0e7-148b-348d-af43-261c949e11c0 | -10.4502 | -53.61658 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d7be86db-f7c0-35b3-a08b-db47430b738c | -4.67413 | -50.83971 | 2025-09-03 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 649e48bc-96cd-3ad0-a4d6-e7a4464c471c | -7.70124 | -50.26168 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 740a04c8-0d35-3a4f-bbc1-203aafefdaf2 | -10.45402 | -54.78239 | 2025-09-03 04:46:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a563e915-eb4d-39e7-b6fb-a4f5319cf71e | -6.95339 | -42.9703 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89d9279d-1d35-314b-9db9-211dba5c6dd2 | -11.60062 | -52.11569 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9237f9b7-3ac4-337a-aa78-091e2dd209e5 | -9.19915 | -45.19393 | 2025-09-03 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8519302d-3b62-361e-a3c0-6831d630b2e2 | -8.06659 | -45.36141 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c5ed05d-8680-3756-b403-fdeb068c261b | -7.70624 | -48.75263 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 999b31e1-721c-3991-9a67-3c4185719c78 | -10.13886 | -46.25212 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21da034d-97a1-3e98-8eae-883626a07ef6 | -5.90902 | -57.73956 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3a80b62e-cb76-3e5f-b511-fe6b3f2d5698 | -7.59189 | -49.66256 | 2025-09-03 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea783f75-eb95-3070-b7db-b99735431bf9 | -9.94307 | -51.62125 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4d10b7-7004-3630-b0cc-dfe1d72daffb | -7.0034 | -43.23244 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1cb4fe5d-9bc2-3237-afd1-12824c83c7ee | -6.8226 | -52.81269 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 108160ee-2684-3806-8d1d-936f0d9dbb99 | -11.58686 | -52.11708 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5e07962e-59ea-3194-84d9-0c23735641ec | -5.87012 | -51.71522 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c39fbe-41ea-351a-91b4-d770cc68f9f6 | -10.94556 | -50.7819 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f1568a0-60f3-3b31-ac44-c08b64fedd68 | -6.80226 | -52.83173 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19f8fc77-7fc7-35e0-9d88-82c3c53884ca | -11.63964 | -52.06083 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ba6bb37-d0b5-3512-88c8-c7e94cd17fd5 | -8.88876 | -45.79947 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e631deb8-baf6-30e1-848b-3e54bb8d7144 | -6.46209 | -49.5261 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fecd4b04-9073-3d5a-9382-06b0e0a3edda | -5.43345 | -51.43964 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7d65507-b8f1-329c-97bb-555357f75d9d | -10.11886 | -46.23848 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dfb53e4-6b96-3436-90dc-562837233478 | -11.42561 | -46.90082 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 472eae56-5ecc-3f70-bff2-60ac519473eb | -7.90536 | -46.45232 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6e721d0-9e09-3bf2-bdff-978e25b66530 | -6.45331 | -42.38872 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27df4442-38fb-3f7f-b95a-04fd32a2c70b | -8.9129 | -45.12346 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6ef8c28-172a-31f7-ab7c-51e992d0b25c | -5.90824 | -57.71673 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6927e61e-ab94-30f7-ae7c-1f1f275db33e | -7.91251 | -46.43147 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0672499-a365-3aeb-bac8-6416c6f7dec7 | -11.59677 | -52.11867 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cab3a162-0d92-3e07-9555-1ca0b4a185d5 | -11.6716 | -52.16344 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdc99db9-cd3c-36b4-906c-12a653034f30 | -11.59367 | -51.94194 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a945ac5-1a27-3a6b-86cd-aa6d22fb9c4a | -11.58522 | -52.1276 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f2378a0a-bdbd-3fa6-86b9-3e62be59c2b1 | -11.81004 | -50.63044 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1b09cc5-700e-31f9-a862-ded926c7a141 | -11.58464 | -52.10955 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5b325e8-1521-3757-9287-417424303edd | -6.5875 | -44.05948 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16d98139-d1af-360a-9ab4-f3140495094f | -7.70643 | -48.74981 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README60.md)
