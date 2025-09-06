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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81bd2a59-a8c1-36f6-a1ec-4a8052e5ed9f | -5.44291 | -42.80696 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da300978-ae2d-34d6-b1ab-1ba96f12b1a7 | -13.66801 | -46.94935 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fac5d39f-6377-3d97-be5b-1c0a47549924 | -5.94573 | -42.96457 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1be0d553-dbab-316d-9235-b8c3c6a14ec0 | -8.7752 | -49.63734 | 2025-09-06 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02388be8-e06d-3031-9993-f7596b9b93a6 | -6.49455 | -44.21035 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0de417f7-9e1b-3bc0-9cd5-59b7b385ccf2 | -13.00252 | -54.83472 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3d94657-5fc5-3aad-b173-f30e8bd08b53 | -9.31321 | -45.40235 | 2025-09-06 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ae4455-20ac-3c6f-a829-d1217d35f6c7 | -15.18455 | -48.03698 | 2025-09-06 04:17:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b27bb02-0b47-338f-b5aa-d188b9e564e6 | -7.36382 | -44.3196 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084ccf31-04a9-30b0-9188-b90a19bdb803 | -4.80119 | -47.26052 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95b90819-ae13-3e1f-b3bb-b1827cbf5b88 | -8.45009 | -45.0369 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 31161cb4-add3-3e33-b51c-f9d80f0d1243 | -10.65159 | -44.8388 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 390b39aa-8c3c-3a91-ac0d-1d546872772a | -3.69605 | -49.57298 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2952bd7-7345-3b9c-a5e8-368651c83e0d | -12.99686 | -54.83363 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3d3ead6-1dee-39d4-8123-d29a4837516c | -6.23332 | -43.28406 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a2c4dfe-a4ea-3202-a516-6b16af0f1a9e | -5.42028 | -43.187 | 2025-09-06 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 247cb26d-325f-3515-8b87-86ee07be0fbb | -7.67835 | -50.29971 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3260ec5a-51e9-390b-832a-978096cf36ef | -9.01195 | -49.8016 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce9e2cf-30e2-3e7e-bf63-1bc6101e395a | -13.00203 | -48.05158 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a050defa-bad0-3ea5-9025-938cc695c2a4 | -6.2422 | -43.29259 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4f56c80-dc5f-3c4c-8b7c-6ade0b18396e | -7.08107 | -43.86609 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6ae97f-e9ee-30a5-86ec-36dfbe98e005 | -12.95563 | -54.79264 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eb878f0-f0da-3c9d-b322-7ae7b2ed452c | -5.79219 | -45.62236 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e460529-1546-3208-971f-d5558859e2f5 | -15.29407 | -46.98608 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4596576-9a1a-3f4d-a2f0-2e4307a80d86 | -13.00485 | -54.82298 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e34b3ba7-7d66-3124-a9d0-113289f47f07 | -5.93141 | -43.01207 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0bd7fa51-9586-3a9e-a40b-f7f2926b6ab9 | -5.94914 | -53.80001 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e8cb654-0979-3718-86d5-d61cc638c610 | -5.72916 | -43.90361 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 089bf21a-7b25-3cb0-93c8-893ae08044ec | -12.98073 | -54.82618 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07fe6947-1c69-36e0-821c-91c57a048b2e | -12.51056 | -53.84903 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bae0229-8fe8-3de9-b2f4-1fa16b603076 | -5.9531 | -53.78917 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248f559f-7e57-3784-9db4-9e8225c644d5 | -6.15599 | -43.17593 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd522e84-bf76-399d-bba7-4cd8153d0713 | -6.28403 | -53.44373 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a00f437-b497-31fa-b848-8d4e3cfcb156 | -13.65918 | -46.9594 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44074f46-0b5c-3f6f-8d33-177fd7fc9493 | -3.75087 | -44.37334 | 2025-09-06 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30b34203-b00a-394c-81d5-4778e01d732e | -4.50634 | -42.89022 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 884327d4-0bbe-372d-9b75-8c8ad99dcfa0 | -5.55141 | -43.06546 | 2025-09-06 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fef5adec-fc50-383c-987f-f118cb6f6994 | -5.86497 | -52.17025 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da60c3a5-1e1c-310b-8481-367dbeaa191b | -9.70436 | -49.49297 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9524b43-5c9a-33e1-a6ff-ef2351ac392f | -9.84481 | -48.84124 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88918a29-c5fa-3444-9a0a-7eaa753eeeaf | -14.58799 | -48.08942 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f085fd9-80f4-320e-959d-ded9800fde39 | -5.94715 | -53.78805 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3252415d-e476-3c33-b772-d4503eaf7094 | -8.49469 | -45.06295 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77f34328-d6b3-32f4-b238-091bee168a2c | -3.75488 | -49.05431 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c00f69b-2051-3b2a-8b5e-4d7de032a514 | -5.87318 | -46.04671 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4909d79f-ab06-3f3c-a842-0ec26e14b5f0 | -15.84329 | -52.28553 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4acc3b6b-233a-3ac8-8aa6-836465f6e054 | -8.34142 | -47.49078 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acf55497-37ed-3557-912a-ac2938bef63d | -6.15157 | -43.18235 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7346b306-a1e9-3bba-9ca5-156b6f52d1b5 | -2.8561 | -49.50672 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8d9e2fa-c5e4-3dd4-82bd-35d03cd2bd4a | -12.89712 | -48.01235 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23fc3712-fb4f-3239-9c3e-237731546b0b | -13.47358 | -46.83718 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57cb2cb8-c800-32fe-a943-0e936c63f166 | -5.72803 | -43.91069 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 968d814f-384f-3576-9867-848971c03b2c | -9.17587 | -46.02928 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78cdba3c-4085-3c1b-8bfc-bd4c9770f2ac | -5.65694 | -43.61438 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0f727c6-c64f-3144-9c58-408ef7320961 | -15.36747 | -46.41515 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4e95544-9fb3-32c2-bef5-058ca8a91fee | -6.23852 | -41.82718 | 2025-09-06 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae3e7736-41c5-37f7-9bbf-20d8747e8ca6 | -6.26371 | -53.45683 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a9d178b-a69c-3840-acd7-9250542075b4 | -8.0259 | -44.76748 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71beb3a7-c507-3bb2-8276-e79ee00387dd | -2.65484 | -48.7969 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2af4d266-f841-3b39-9233-3fbd72fdcc91 | -5.4957 | -42.15335 | 2025-09-06 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2419ad34-cf44-33ab-bfbd-d25e3736368b | -10.15289 | -46.2327 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6b8771d-236a-3d2a-8114-7052ff3135ba | -16.29509 | -45.68606 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a3e056a-4671-36de-92d6-d67f7eed1ca1 | -7.98698 | -44.50739 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24a3b753-c2bc-34cc-95d8-2bc75452bf9b | -7.32702 | -48.50395 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4cfd160-366b-3de8-9f8f-79727f75c5ae | -3.75024 | -44.37257 | 2025-09-06 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7328178-289c-3351-8394-0903f016534f | -8.0177 | -45.43546 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fde45f54-0abb-367d-85c2-3fd61496a749 | -14.57936 | -48.00946 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd83cbf7-ca83-34da-b1ea-9981aa28ee98 | -10.6067 | -44.33447 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 46995d3e-ee4d-38de-a014-5ce68da6bbde | -9.82541 | -46.53285 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd3736fa-240f-3273-9972-eaffad04b50c | -8.06137 | -52.38759 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55f4d9db-6627-328a-9400-3ef6259321fa | -6.37925 | -43.02599 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e36016d-50d3-3a6a-acb1-2e3ab84808c1 | -10.61059 | -44.3315 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bbad98cc-084b-3a2e-a1e9-065c0796d4be | -6.22529 | -45.12597 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 617dfc4e-7d25-3d33-83dd-6c99053f8480 | -6.5385 | -49.5069 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d6aa320-ab16-3d03-9b1f-6b3ac07f7a12 | -5.92715 | -43.71808 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bffa759e-afd8-3a9d-9140-f2888af2c281 | -7.21137 | -43.98374 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98773676-141f-36c9-81d1-cfca5bc67e51 | -6.20623 | -43.36879 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7a3018e-01cc-3300-bafa-3a5af4161fb7 | -5.5135 | -42.66183 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e8e5cccd-2443-3aa9-a1b1-1dceb9318f42 | -9.84139 | -48.83713 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c04b0bb5-c907-3e85-a95e-97a767abec48 | -14.56855 | -48.02927 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae7bc67c-c0bd-3d85-a242-48f95c1e88a0 | -12.62094 | -56.98507 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 270efa37-145f-3062-a483-fda50d302ec5 | -6.59271 | -44.55401 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e4ab9c7-48fa-38a1-920d-e258e67729ed | -9.71485 | -48.99023 | 2025-09-06 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8468f98-ab5d-3f9a-98d8-0d357f9acf8a | -5.92808 | -43.01154 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90b53f05-2ad2-3d87-b2f0-2d18eab1ff7f | -14.18623 | -53.06305 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b97f8e93-a8fa-3bd8-a424-74d50d6f7bea | -5.92553 | -52.00034 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dbf7788-1bd3-3094-8d8a-d3cfa6c55906 | -14.37284 | -51.91646 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f46534b-ef0a-30dc-ba39-5e11cb855fa1 | -7.69064 | -50.28349 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 244e0e3d-6d0a-3b73-9257-2d5525df37d2 | -5.62104 | -42.87746 | 2025-09-06 04:17:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38b2f557-2c99-3e2c-a3c5-e951a1428aaa | -6.80824 | -52.81258 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00a07dad-7e5c-332b-8d96-870443480401 | -6.20215 | -45.49753 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c44efc3b-535e-3731-97fa-e0831173b53f | -13.55614 | -48.11559 | 2025-09-06 04:17:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c3f8c3e-e08c-388c-9dec-bead35f12acb | -6.18737 | -43.35868 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e85ab9b0-3baa-301d-828b-19846404cbcf | -9.78032 | -46.91345 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6165e65f-d45b-3f0c-9261-7673bd612042 | -7.41641 | -44.94741 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 830c8ef6-bc7a-322a-b655-f5c246a6f64a | -5.73303 | -45.36161 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ed06a25-d74b-39d2-8ea9-22343b7d1543 | -5.87155 | -52.16428 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39b2d821-7aeb-3458-b0f1-bfadaffc8478 | -10.60506 | -44.32338 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 000b7016-54b7-3344-8ff1-8a648605a0e5 | -3.38287 | -47.61191 | 2025-09-06 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e1d46ad-aef7-3bcc-973d-f6f267eeca68 | -7.41358 | -44.94321 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README40.md)
