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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d3ae260-166f-35df-a38f-b337bec7d09e | -3.3359 | -58.1191 | 2026-09-21 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 895372dd-0623-3e11-afb0-fd63eba8a1d4 | -10.2982 | -50.2158 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| eb0f03fe-cae2-360f-aad9-bdbe4858aee8 | -5.6406 | -43.4153 | 2026-09-21 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 50a779b1-a95e-37d1-8d34-f3bd89fe41ae | -2.9158 | -57.7789 | 2026-09-21 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 84f84fc3-9b67-3021-9f40-78723b1abcf0 | -6.3013 | -59.9771 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f526081c-557e-3ff4-92e5-3eb2341d04e2 | -4.2239 | -48.6127 | 2026-09-21 15:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 23c8ee3a-ce12-31bf-ac93-ad4d3b953e4f | -3.3824 | -50.4276 | 2026-09-21 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 562e7268-849a-38e1-92af-1cedb0edf5ff | -12.5231 | -50.0051 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| ebdd6acd-ea6e-3acc-8d02-3ec7c4e8109c | 1.261 | -50.872 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2e8f8ca6-7dcc-3c13-a504-1dea62be161e | -6.8264 | -55.5222 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 29f33928-c5b6-33e4-8f82-54ee681522d6 | -6.3918 | -45.2175 | 2026-09-21 15:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 381d6a08-2e31-3152-a071-b7255f353019 | -8.2975 | -46.0178 | 2026-09-21 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| baac3195-17ee-31b2-b823-14ce16593dd6 | -6.3195 | -60.0147 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f9c3a5d1-c18c-389d-80cb-06cc6c469052 | -5.8274 | -47.7898 | 2026-09-21 15:10:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 88bfe9ac-1959-3a6b-93e3-193e0973f7a8 | -10.3729 | -50.2722 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 0e32a9a3-23aa-3c11-a8d8-19b11727dbee | -8.0894 | -55.331 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0c3150bb-ff16-3ac8-8b65-194e84c2ad15 | -4.0944 | -52.1252 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 69cd576d-1986-3489-945d-f447bac44eeb | -6.1466 | -47.5065 | 2026-09-21 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6d665541-eb08-3437-9b62-bda309d98ae7 | -8.0706 | -55.3522 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 4e67b8a6-1b32-36a9-a285-feea8155c193 | -2.9157 | -57.7983 | 2026-09-21 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| e45ae5fd-28c3-3f2b-a97a-d2771d194fdd | -7.2117 | -56.0193 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 59be94e7-a124-3525-bfd4-eb2fa4fcea4f | -6.8263 | -55.5421 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 018c817b-12aa-36f1-8744-fc24ee52bf5d | -6.3012 | -59.9962 | 2026-09-21 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ad0f64ab-de07-3da0-843d-36ae50d50ff6 | -10.473 | -51.2808 | 2026-09-21 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 7650310b-ad16-3e24-86c8-db7810b4f96c | -3.4555 | -50.5927 | 2026-09-21 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4fccbc0e-4edb-37f8-a50b-244a5f5c96fd | -10.0898 | -50.2795 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 9b03f773-2119-3243-97b2-14f173ae0bdf | -9.8686 | -48.447 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 98dd725e-667d-3f2f-a54a-cd27be7060de | -12.5043 | -49.9858 | 2026-09-21 15:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 719a085c-1069-352e-b865-95b6a3f30462 | -9.8683 | -48.4689 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b7a06002-a939-3d89-9ccd-a23268a9b89a | -2.9997 | -60.8047 | 2026-09-21 15:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 530629a6-193f-3007-b944-19952028d505 | -10.5906 | -53.9918 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| fee5edfb-cbef-355f-8433-5607c1faafb6 | -0.803 | -48.6825 | 2026-09-21 15:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a76fc7e3-cdab-3abb-858f-2be0c9d5ef77 | -9.5593 | -66.0545 | 2026-09-21 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 49ae18f2-2035-359e-8998-f9608997ab9b | -2.8608 | -57.7994 | 2026-09-21 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| d546e1a4-61e5-3734-8f57-107f718e749f | -11.8014 | -49.8129 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| aeff4c17-6def-3afa-8575-06408ff96e70 | -10.0526 | -50.2406 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| a5bff602-5255-336f-a579-e5c796a4d114 | 1.2608 | -50.9968 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4a13ef7f-334f-3da7-b52a-5ed64fbb1149 | -3.753 | -59.419 | 2026-09-21 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| af9d2a05-97ae-37d0-8e2a-d4c79514955f | -6.2585 | -41.6617 | 2026-09-21 15:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 0c16eadf-f6dd-3fe0-b7b4-decdf99f430b | -8.0708 | -55.3321 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e7bd480e-3886-3768-bd5f-f8e104f041c0 | -12.8711 | -50.9505 | 2026-09-21 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2c64ea35-4200-3345-89e4-4bd3c6ff17a3 | -8.2388 | -55.2616 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 60dc880a-61ba-3ba3-ac34-7caa11e61644 | -11.8168 | -50.0482 | 2026-09-21 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b1a8cdc6-1f75-3be0-bd55-a86503202f25 | -10.4725 | -51.3231 | 2026-09-21 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e56a7a7d-8dd5-39c3-92c0-fd49606e3165 | -10.8743 | -50.9439 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 934b0b29-ef49-3d36-b243-a5f55d87e11b | -8.5984 | -54.6139 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e1fdb1a7-cba2-308e-839f-41f33658929f | -10.6944 | -50.26 | 2026-09-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e46ddb8e-573f-3e46-8e5e-3b55b595e786 | -10.9098 | -54.0866 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9936e359-1e1b-3653-8296-57ef8b3d8fb6 | -8.4922 | -47.0257 | 2026-09-21 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 527d741d-aa54-3965-b5b1-7e99e1da2c9f | -3.4003 | -61.2898 | 2026-09-21 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7fa1717f-b4df-3027-93a5-2effa073ddee | -6.8448 | -55.5411 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 6ccf3236-df21-397d-829e-fbb9d1f97fdd | -9.831 | -48.4292 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 2376a880-85bb-34c2-aa28-59a20394d420 | -2.9709 | -57.7197 | 2026-09-21 15:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2a9fd7b4-a7b8-31ce-9c65-5f66ca04cd19 | -11.0412 | -54.1362 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 248.5 |
| 178860b2-436e-3668-bfae-7c3219d56146 | -10.3919 | -50.2702 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 04b8834e-60b7-3008-bec4-903ef8131d2e | -10.3732 | -50.2508 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 802ccb83-1878-3ad0-bfa5-151e5d81fe1b | -10.8746 | -50.9227 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4f786cc2-80bb-36d4-995c-2500962a859d | -7.8243 | -61.409 | 2026-09-21 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d0b82e4c-2255-3070-9c30-97328f380a5a | -10.7115 | -60.7312 | 2026-09-21 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2e6ca8a2-43c3-319c-b0ed-d266fd3dba1f | -10.6694 | -50.7103 | 2026-09-21 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b185739c-b8c4-3f7f-aaea-741852a4bec6 | -7.2333 | -55.6004 | 2026-09-21 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| d4a8a561-1a31-3b9e-983a-8ff7874fb394 | -10.6571 | -50.2212 | 2026-09-21 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5f9ffd1b-7707-393c-b079-2e80bf92ba77 | -12.3206 | -50.7394 | 2026-09-21 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a33e8734-4445-30d0-bf16-4f79c4d29ed3 | -9.257 | -46.1873 | 2026-09-21 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b2557683-811a-3f1d-9225-36b8174b055e | -12.1853 | -50.8623 | 2026-09-21 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 213da153-52c4-3918-b2e8-01ef90ef0aa8 | -11.0601 | -54.1345 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 163712bd-4969-3b9c-9eb2-dda3979d642b | -3.4599 | -59.5209 | 2026-09-21 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| bc1a8f9e-2080-3d0a-ba6e-5c7e9f772739 | -9.8307 | -48.451 | 2026-09-21 15:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 378d5497-d726-3a7e-b8bd-5847ad5a96e1 | -5.6221 | -43.3934 | 2026-09-21 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 062592fc-d39d-3e65-b6a5-aaf2b5f979aa | -3.6449 | -58.8647 | 2026-09-21 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| c5c71829-79a2-38b7-a4c2-f4c85233275c | -10.4919 | -51.279 | 2026-09-21 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| d48d5f1f-9d64-38fa-b5ec-33088b7ccbd0 | -4.0943 | -52.1458 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 6283be29-fa45-3cd6-b537-4d90241753a5 | -5.2546 | -55.9303 | 2026-09-21 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 44231d9b-e5ac-3e55-8a4d-72b2606df028 | -5.9985 | -45.2476 | 2026-09-21 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 8ad32fef-0e28-328d-8c30-1b330adc9877 | -5.804 | -53.5223 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d6c8eeb2-42f8-3295-a533-7990685ef728 | 1.132 | -50.9151 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 90.2 |
| cdaa0216-c37f-3cd9-9097-487db0ef26cb | -13.2794 | -51.7524 | 2026-09-21 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 6fe807d0-65f4-3816-92f9-e063b5f32e3e | -5.7304 | -53.465 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fd1a7a87-a933-38b7-b81c-d293e0101f18 | -10.2635 | -49.984 | 2026-09-21 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 281fe9db-1fcc-309d-8bc4-80a5f1f26af6 | -6.0033 | -44.7247 | 2026-09-21 15:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 12594d5d-9286-3d1c-8887-989fdc6fb6f5 | -7.3291 | -55.1955 | 2026-09-21 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| df6b57e0-cc8c-3c25-9a0e-7b53428ec950 | -10.8911 | -54.0677 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 06ad3e19-2132-3fc0-9755-7550dc4be4fd | -6.183 | -47.6133 | 2026-09-21 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6b409801-2588-3dfc-a3da-bc891fba2f30 | 1.2239 | -50.9972 | 2026-09-21 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2713d972-1bee-3636-9488-ba248ce2b7c1 | -1.0243 | -48.83 | 2026-09-21 15:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b57c3a18-c53d-34f0-a7cd-6763065a4a7c | -13.4887 | -51.8539 | 2026-09-21 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8ff3e8da-b480-3f85-915c-11fef62d931d | -10.8921 | -53.9857 | 2026-09-21 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 16f4c2d1-cb8b-34c2-9c25-0422389f4309 | -9.61 | -43.94 | 2026-09-21 15:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3571a640-c230-3232-8e4f-b28f2f342ccb | -10.72 | -50.78 | 2026-09-21 15:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57d5be91-0dea-34cd-bccf-c12cbde10dbe | -9.15 | -50.02 | 2026-09-21 15:15:00 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc889d0b-d3fb-3bbd-8baf-a640c62445e9 | -10.85 | -50.16 | 2026-09-21 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eec8c579-7157-3539-bb88-f465b3ee5ed6 | -12.43 | -47.08 | 2026-09-21 15:15:00 | MSG-03 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7cb3e03-ba4e-3866-9edc-9b3a97a55eb6 | -10.75 | -50.79 | 2026-09-21 15:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a23a489-29af-377b-80b8-4664462dfa84 | -7.16566 | -37.71192 | 2026-09-21 15:16:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d2403896-b56c-372a-838f-3c4cbf57b895 | -5.67688 | -38.8878 | 2026-09-21 15:16:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5741b73c-b17d-3092-bd8e-ae83b0f565ae | -6.93276 | -38.72437 | 2026-09-21 15:16:00 | NOAA-20 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 91818fee-7b33-3423-b109-7c3c37f5b47e | -7.39664 | -38.72384 | 2026-09-21 15:16:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| cd091677-20bf-3b34-9274-40a32e911f13 | -7.81882 | -38.84919 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 47df3019-dd09-36ef-960d-c6cd2fbc282e | -8.53238 | -36.63396 | 2026-09-21 15:16:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7a5b670d-3b7e-34ac-af79-519a9d8395f4 | -7.8219 | -38.84864 | 2026-09-21 15:16:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |


[Clique aqui para ver as próximas entradas](README139.md)
