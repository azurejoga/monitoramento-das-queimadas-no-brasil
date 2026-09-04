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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef605b54-48e8-3c4b-89e3-a2cf7739ae3c | -5.84583 | -52.06736 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1777e169-e07e-3b7b-8d63-edb781726478 | -5.38552 | -42.85884 | 2026-09-04 04:38:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9128469-e823-3c36-b326-4583d4467bd6 | -5.84412 | -51.96359 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2afd16aa-ab16-3709-a3e0-1a8a3f1b169f | -5.80219 | -43.63409 | 2026-09-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28f34004-1f16-39c9-9781-2d2200e4c1d3 | -3.62595 | -54.60067 | 2026-09-04 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 994d76d0-7c48-3936-81a4-114fbedf69f3 | -8.5048 | -54.6606 | 2026-09-04 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2126509c-e316-3cd2-a6d8-7d9d8fe1be8b | -8.6101 | -67.1783 | 2026-09-04 04:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a86d0fa8-ffb9-3a43-a3c5-98b70a242475 | -5.565 | -60.1739 | 2026-09-04 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 48dc72a8-ddd9-355e-92d9-f7d552628f99 | -8.505 | -54.6404 | 2026-09-04 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| a6514cff-1ccb-310c-b4ba-7cd6e7a61e4d | -7.5476 | -61.3437 | 2026-09-04 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| b941c157-fce3-3276-8e07-d68eabe20659 | -7.566 | -61.343 | 2026-09-04 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 664b91e8-e70e-3693-94ec-37bcc71b19cc | -9.57711 | -40.34732 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2ad63eae-1568-35ae-839b-aeb5f89f9071 | -8.42533 | -54.71984 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecee2b92-618f-308d-8b15-d311919338fe | -6.69154 | -59.98153 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 764c1726-6004-36e2-b15d-8aba000ede8e | -6.52412 | -59.93918 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b2b3565-fcfb-3c17-a143-da9c5894c7e4 | -9.67849 | -50.84259 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 454da080-cf4e-36df-b5ea-519bb87f1190 | -6.67896 | -59.97903 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f65b266-49c3-3613-9e05-2c9684d7949a | -8.43564 | -54.68692 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 284371ac-f07a-3f65-90a8-0ce5672ac7c3 | -10.367 | -49.953 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fbe61ba-5cd0-35fb-ae56-ee882c70a333 | -6.68653 | -59.9378 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30325eca-7e1f-3a3f-8670-96ae767ddd9e | -10.557 | -50.01722 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf7d87c2-283e-3830-aace-7a326b196819 | -9.01412 | -40.99714 | 2026-09-04 04:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cf594773-05a8-3d68-82b9-8bc6bdd53fcc | -10.65079 | -50.38669 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 461c6399-5f3d-32a0-a0e8-7f47caa17681 | -7.24088 | -59.52989 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96a75866-e787-3e8b-90bb-6c71c1a070f6 | -13.40304 | -41.88818 | 2026-09-04 04:40:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e6845f7d-1407-35c4-aa12-4ca6466aff83 | -13.35741 | -51.74935 | 2026-09-04 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d0e800-2a96-39d1-85a4-187ba717483f | -8.62413 | -54.84821 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85d3cf87-8d38-3a9d-b40b-8dd6abd6ce6b | -10.39705 | -49.95795 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dff3ad0e-6c0a-3aea-a5ba-75305cc4289d | -13.40961 | -43.87579 | 2026-09-04 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed1cc79f-248a-368c-88c1-f0cc3e2d8c0d | -6.14977 | -59.94458 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e0fc621b-8dd0-3dc9-b1c8-4d2c9b989c67 | -10.91356 | -49.61774 | 2026-09-04 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c7d65eb-f273-3347-bfea-aad8bd148737 | -10.49727 | -51.32796 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 402bbac1-8f78-32e3-b0b3-044788c85334 | -7.55132 | -61.3377 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| feed8e68-a3e5-37dd-baa9-30766565ca4b | -7.08587 | -56.51839 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7eb2fb-41c4-3f8c-83fa-c407c2de20a4 | -10.6581 | -50.38419 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| fb58d392-117c-3f40-9e40-d06d40c25b4d | -7.24173 | -59.52872 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9be87dc1-3eac-3bed-bd22-1cb3bc71bd22 | -9.70903 | -50.82833 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce03110-6fa9-3830-8702-95aabc14d63e | -8.10967 | -54.79088 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a37fe7a4-f51f-3fab-adc3-c569da1cf510 | -6.68086 | -59.96872 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 99c0e0b3-c117-3eed-bf66-dfb4d868c352 | -10.90768 | -49.61291 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 146a36e0-0630-3b7d-81d9-01490814313c | -8.21823 | -54.91912 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffed22af-6fcb-37d2-a793-664339146457 | -11.5938 | -50.47909 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8507544-66aa-3d9e-a774-e47fbac41a7b | -8.11694 | -54.80088 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32bcb36e-c660-3cba-9f71-c4f05fab877a | -15.76897 | -43.31754 | 2026-09-04 04:40:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb011eea-7b64-3685-859c-7079a95fbc1e | -10.45392 | -45.3342 | 2026-09-04 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5347f81f-864d-3017-8c0d-e570a057f19c | -8.48676 | -54.64935 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19157bfd-db0a-3a44-886c-8a25f6840e59 | -10.6603 | -50.392 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 58d06b85-1550-37f6-b4f5-6c2a9a9dd0d9 | -7.0864 | -56.5154 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd94e540-c5d8-3b55-b6d3-47ad55aebdf9 | -9.5779 | -40.34134 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2edc2eda-dd20-338f-a5ea-1b1bee95f2da | -8.43774 | -54.70028 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 765840a5-09bc-3b16-8657-e155e977ed8f | -13.57799 | -47.887 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1fd19c7-67e9-32e2-8a24-6ddba61df6b5 | -10.26565 | -50.0354 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5206852a-e6c6-3940-b874-4347c8c9dc0f | -10.63733 | -50.38445 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 445511b8-b18f-314e-bd2c-cf29bd9b5d7a | -9.57829 | -40.33834 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a1efcd84-16c8-3809-a317-1b5043443446 | -8.49682 | -54.6426 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 67292475-e2f4-360a-b6cf-74581a7af57c | -6.94133 | -56.46226 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a3effa-15b5-3922-b54e-649359d5e9f9 | -8.2175 | -54.92325 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f1c269-4c16-3770-af39-1e85e4729428 | -9.7056 | -50.82775 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5d7920e-af7b-318e-89ec-b35f25ff1457 | -11.52269 | -49.20556 | 2026-09-04 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f17735d4-be4f-36cf-9405-d6c0b0570504 | -7.09194 | -56.51323 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a938fb61-1500-384c-a473-13fd0be3d7ea | -6.15633 | -57.76189 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c33d57cf-a0b9-3eb3-a601-ec98d6ce0ea1 | -10.62529 | -50.41598 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140aa0b1-a252-3fa4-a091-606690236ab0 | -6.76585 | -59.43567 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0226744d-a3c6-3978-900e-10137da54572 | -8.11117 | -54.78239 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ca796b17-a7f9-3156-9c40-f22ba96ec594 | -6.15699 | -57.75828 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff2e3028-ab47-320f-b80c-b3984963212a | -10.57209 | -50.00872 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b1d3c5-6f46-320f-857b-efa417598b38 | -6.67287 | -58.76722 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d88502a7-e5ca-3daf-b8f7-bdbd78b98d7c | -6.68335 | -59.99064 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 599333e6-79d6-3d2b-bdbf-cd85b4a19300 | -8.62333 | -54.84976 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54090797-14bd-3a5b-b1f5-95adce131e08 | -10.90908 | -45.351 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 470ac0bc-7fa5-3ffe-a3c5-d1417f400273 | -8.44358 | -54.69248 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c65174b-ad9a-3bba-9a6c-947f1bf8455e | -13.58306 | -47.87649 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92ccd1d1-cbff-3690-a5ca-650fb26e82c0 | -6.78673 | -58.95432 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c67ca95-72ac-3da4-8c61-4d145cc7cb61 | -10.49594 | -51.33609 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c875bd6-6366-34b7-b252-bff97514f164 | -8.11479 | -54.78741 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 61af4fc9-a673-3b66-ab7b-5f2f159d1ee8 | -6.75974 | -59.43466 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ff28b3f-b379-3600-b22f-17f8d48189f9 | -8.49108 | -54.65009 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 449e98ff-dcee-3d03-a50b-040b6de3feae | -10.56598 | -50.00406 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dd041e0-d82d-3edd-aa59-91113f0fd120 | -7.07582 | -56.51678 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7dbac3b3-2d12-3324-8f10-73f122ecf1b2 | -6.53041 | -59.94046 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f7149c-66a7-3df1-bcf8-882a7c795b4e | -10.90844 | -45.35545 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea37168f-8788-374f-b0ea-7fa0acf755a1 | -8.42983 | -54.69452 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 086983ff-d3ea-3327-95df-11ae151c5800 | -8.49539 | -54.65083 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2144bc79-987b-32c5-b689-5549d73f9758 | -10.4995 | -48.65248 | 2026-09-04 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0967bd5e-67bb-3eaf-9fd4-13c1dfca79a4 | -13.5825 | -47.88022 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa06aa28-a5bf-373e-87d1-36bce2249ce9 | -10.39314 | -49.96096 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc1a24c9-f974-3e1a-b51c-5e14c2f5b45a | -8.50113 | -54.64333 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 49c1234e-7039-3a41-bdd7-ce67ba204709 | -10.90633 | -45.35677 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 500d4df4-685c-3f8c-adbc-1387bb550764 | -13.98703 | -51.46697 | 2026-09-04 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0664da00-eb5c-3916-88ca-a38abb8a2381 | -10.52595 | -47.95821 | 2026-09-04 04:40:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 90af27a4-17e4-33bf-b61e-08c66fc5b69b | -10.62866 | -50.41654 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5730a9c6-76e8-3ad0-a638-7ca5ccc42757 | -10.64229 | -50.39645 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cea27805-a858-35a6-a3d3-644c85c04a24 | -11.94363 | -55.9151 | 2026-09-04 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddedfd8e-b3d4-30fb-99ef-e70732aba414 | -7.5836 | -57.68866 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c68c0cf9-f19c-38a6-9d15-ef08be7c5f12 | -7.08137 | -56.5146 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cb90864-b4bd-396e-9d3b-f3f1c1dd7501 | -9.71246 | -50.82891 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71f5209b-b1b4-37f5-99e0-833f1a8305a4 | -10.63893 | -50.39589 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e58fa88-0069-3304-8bc8-161774fa696b | -8.43998 | -54.6876 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b4c5b86-3714-380a-9eb1-04f49e82a007 | -9.57204 | -40.34661 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7627c7cb-7b55-3d9d-aa28-77cbc2883870 | -7.55576 | -61.35133 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README18.md)
