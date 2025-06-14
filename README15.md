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
| 0ed1639d-ba9b-3bb4-84dc-77a0641ece2e | -12.62284 | -57.89434 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5cac2a09-ee6c-3695-8213-f57fa914220a | -14.03245 | -55.12191 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f9038be-172b-3889-8b34-f3d76f326612 | -10.91703 | -56.83673 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f3ffd64-13c7-3902-b5cd-eb28f201e5d5 | -10.09134 | -52.74259 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eee15300-cd9d-392b-9b10-ee31bfc5d2d4 | -9.40021 | -48.41281 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e197597-8828-30fc-97b6-3d1e5fdb12a7 | -10.96218 | -49.56815 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7281569-8c56-3006-a496-c2b1bf77fe2e | -11.72924 | -48.87352 | 2025-06-14 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1858a96a-2d03-3db5-8f37-d8f5f023f76e | -13.89156 | -54.63632 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f64f8e7-1694-316d-aba2-27e1106b7217 | -11.00537 | -55.0886 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dffe51e4-a2b7-3484-89ea-a03031e32ca3 | -12.76585 | -44.41182 | 2025-06-14 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 416cef48-893d-39e3-a3d5-3e6cf9deadfc | -14.21226 | -57.40027 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10d60f8b-2854-317f-94be-19ab9bbc55ef | -11.79709 | -43.78973 | 2025-06-14 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 762550c8-7acf-3507-aea5-fb2900e61d3d | -13.89648 | -54.6114 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 798fbd3f-a394-3406-aa78-01b7a2834445 | -11.99844 | -51.61432 | 2025-06-14 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abdf513a-7e56-36c0-aaf5-43e41f4cd45e | -11.01124 | -55.08991 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e64315e-8e53-3530-afd2-bfade6fe6dd4 | -8.80692 | -49.8306 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d7f42dc-2857-3687-924d-3ff68dec47c0 | -13.89371 | -54.62545 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e2eaa59-4eb1-3d20-84b3-ac48f010d6c2 | -11.1377 | -53.91919 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f4e9321-007a-3590-9eef-1182fd894d2e | -11.79921 | -57.35057 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7465629-f25d-3d02-82ad-a7c131d5c24c | -14.07074 | -53.39762 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52f7c62d-898e-3acc-bf8d-157a7f93b10f | -15.39143 | -47.8646 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5031935-4861-3d7c-91d2-ae0b3aac4633 | -15.99218 | -49.82127 | 2025-06-14 04:14:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd3d315c-cde8-3b5e-a3b8-dff76f274e7a | -14.21028 | -57.40517 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa92511c-9e4f-32ba-9079-a26e50d313a0 | -9.56559 | -46.74464 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ca3b73d-c794-301b-b022-87788fd15ddf | -13.22698 | -49.83622 | 2025-06-14 04:14:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f9068ec-c627-3cf5-adcc-40146a9821b3 | -10.85127 | -53.78276 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d8827c-9817-3225-ab3b-4594791807db | -14.69148 | -53.37091 | 2025-06-14 04:14:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b04fd5-64c4-34c9-9763-7e19165f9660 | -13.9667 | -54.43721 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e1df77b-8ec2-3c9a-95b0-21040a9f6184 | -10.84912 | -53.78935 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52755ae-a60b-3d14-89ec-1d4523bd4644 | -13.88967 | -54.61727 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77db8d49-7583-3282-8082-7652570e7827 | -10.70554 | -46.55635 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46c7da12-9651-34d6-8aff-6c6294ac3602 | -13.03314 | -44.11444 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfb9d756-680d-3524-9703-c766115c5f0c | -10.36337 | -57.23027 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a9afcaa-e966-39e5-bcd6-56063e5e0aac | -9.40378 | -50.4179 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3091eedb-27d6-3e8a-88b8-80edf107a6c8 | -11.91222 | -57.472 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88f54c3b-597d-33e5-afe0-405bdd9bcaf5 | -13.95777 | -54.44236 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41cd7cf9-0d42-3adc-9136-0888ab627938 | -9.56031 | -50.77908 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a139ad73-3ed7-31fd-b227-23862459ed5b | -13.49992 | -53.4857 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 164eb4c9-8828-3462-8abf-7a0f7859469f | -10.85587 | -46.70222 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e5e1255-4011-336f-82c4-3246394b4bf8 | -12.27007 | -44.60527 | 2025-06-14 04:14:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d37a72a8-0f22-305f-96a0-a93fb9d82a5c | -10.87384 | -54.31277 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98d32620-f480-3792-8bc0-6e92d45185ea | -12.21101 | -49.64286 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d4669fe-081b-3403-962b-eaff151d1bab | -14.50971 | -48.22409 | 2025-06-14 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7613e93c-ad28-3fec-9b68-88c000945566 | -10.86558 | -54.29515 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1578060b-8ca7-30b5-9085-bcdf691aed6d | -12.27696 | -57.2764 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 036d908b-08cd-3cb9-8588-1ba5c2d2e54d | -11.87707 | -54.67978 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4827599d-0bc4-38f8-b1e0-956790d03314 | -14.20875 | -57.41642 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b22bb806-5fdf-39bd-82f0-246d873065b3 | -11.13881 | -53.91496 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4429170-1a48-3a27-9855-75d2390b0dba | -9.38408 | -57.52158 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcdd1825-948f-32fb-a7b8-fcab82be26e2 | -14.54712 | -47.02899 | 2025-06-14 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e11c31b-c3c9-366f-ae9c-fa3db84844eb | -11.89271 | -47.45982 | 2025-06-14 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3ee0ea3-be8f-3075-93b3-9708d35d03b7 | -14.67214 | -53.39117 | 2025-06-14 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 33254177-0e80-375b-9dab-4edd2b59d22a | -11.88272 | -54.68097 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666c3f42-159e-3ef1-a248-e6864ae04092 | -9.04029 | -47.02118 | 2025-06-14 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c349fd0b-7ed6-335c-ab31-437c0e31320e | -9.12164 | -46.93507 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c271c62d-74bf-355d-949a-c3d31ae46d77 | -12.27939 | -57.27427 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2db03cce-4833-3a4b-9873-5d3a56bce99f | -10.35899 | -57.22553 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa9f863-9768-3ff7-b7c6-7ebb56ce665e | -14.07192 | -53.39165 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7d34c21-051d-3c9f-8ed1-6ead606efd7b | -10.91551 | -54.77682 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5561eba4-c17a-34b8-8520-01b1480fa73b | -11.83946 | -43.80005 | 2025-06-14 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c85ccf4c-df7a-3d9b-b721-a3628e3ec91c | -10.56237 | -52.01214 | 2025-06-14 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b8fac40-1599-3f3a-bbdb-cdd0a97a2613 | -12.61476 | -57.89923 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbea0d0c-bb6c-381c-bf6e-4492db3c21df | -8.92459 | -49.85441 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ebcb541-1395-3c80-93a0-ce1dbad4cbf3 | -11.12673 | -53.94737 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be4d8e5-44a7-3ebb-ac30-9d0113f4d24e | -13.0062 | -42.6701 | 2025-06-14 04:14:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b780ecba-72f1-398a-abe4-f92c576c462a | -9.71163 | -48.61929 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9185f8a-280f-300e-bc95-a51ecadec000 | -15.39492 | -47.88644 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25127379-f86d-3704-a883-6d28e793b6d8 | -10.93547 | -56.84677 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dcd4e628-6eda-3ae9-ae5d-f473e4c59073 | -12.61921 | -57.88554 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6892d753-5c3f-3586-b2f6-a45b1dbe48f9 | -14.20912 | -57.4107 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 77c90a72-083a-3875-b217-a1ccd5c74901 | -13.90373 | -48.7364 | 2025-06-14 04:14:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0801269d-7bee-384e-b6d5-2666e2ee2a9b | -10.07013 | -52.74181 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88b32c6f-7d4d-3ea2-9843-0fc8353f05f5 | -14.02282 | -55.12386 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67da6873-aab1-3aa4-8bf2-b958cc310d73 | -13.89717 | -54.60794 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7d8ab398-6b80-38b3-872a-129b94ab7d48 | -15.39495 | -47.86521 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f637dc05-68cb-3bf9-b0cc-287831b4758f | -11.91348 | -57.4661 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc7027e3-1c85-3efa-9422-4000a55afa75 | -13.96714 | -54.45164 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0727110-18e3-39ca-aae4-7548d313edfd | -10.65375 | -44.49297 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 07c3ed3a-14cd-3403-9a37-7fce2966567b | -10.92895 | -56.84527 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 117e3f10-251a-3f04-832b-4f389a9eecd5 | -11.91789 | -51.10573 | 2025-06-14 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e55bd8b1-4232-32a5-85bc-4dec47badc4b | -13.62687 | -47.74187 | 2025-06-14 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f78dfcd-bfa6-3cf6-bf37-df0ca204335c | -10.87458 | -54.30894 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2460c35-9540-3e31-9f5d-c4dcf3979a05 | -10.9378 | -56.83527 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9dfbff4b-3462-3801-84b1-2e7d98d40c64 | -10.06077 | -49.71106 | 2025-06-14 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16e275e1-f532-3cef-a871-e5715063091a | -9.46194 | -57.84842 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02488e5d-41c5-3d2d-9022-b2cb7f6b7550 | -9.40825 | -50.41868 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b3c27f5-24ca-3c3a-b748-65545907c70f | -11.00877 | -55.09088 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38d56f97-a7e5-37c3-822c-5a325b958f8f | -12.10793 | -48.87191 | 2025-06-14 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0cfa26e8-3851-35d0-aa3a-e6f7866f8834 | -15.39098 | -47.86539 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7b333ca-ab5f-3e2e-a971-9089f6ef3e7a | -11.0121 | -55.08545 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da92552e-ac5f-3cc7-a334-aa55cf5e86db | -13.22828 | -49.82902 | 2025-06-14 04:14:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2018031a-c375-3a9a-be8a-d1acd979d430 | -12.72624 | -46.44837 | 2025-06-14 04:14:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2839875d-5a94-37e5-a350-18502e70f7e5 | -12.21378 | -49.65091 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1212b37-6832-3086-a3c3-b434f35c5db2 | -10.91633 | -54.77263 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b5c114d-24ec-3d4d-8a9b-5389f31d389f | -13.90051 | -54.61966 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2dd2f24a-9645-3ad9-8ff5-a224137606a9 | -9.40329 | -48.41846 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce24c90d-0aec-393b-924e-8c7a639d7f91 | -10.75192 | -54.78327 | 2025-06-14 04:14:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40001f33-23e0-3fc3-8cdf-ada42a2cadbf | -14.07133 | -53.39463 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9123af9d-069e-3e17-be79-50dfd5c019b6 | -10.86266 | -54.29573 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015175c8-3832-3b68-b62b-c9c8d05dbb9b | -16.19777 | -46.47028 | 2025-06-14 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README16.md)
