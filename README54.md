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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64e2faac-871c-374b-a946-bb07b9f9b981 | -6.99146 | -59.24414 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 76e0fd76-e85d-3e9c-a65c-63227ed4b09b | -6.78537 | -59.63639 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ba6dcd4-bf98-3a06-ae4e-9eecafb55dfb | -6.21614 | -57.68591 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd402ed0-14f9-3da9-874a-41978a346bf6 | -6.12218 | -57.7421 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 697fe12b-721c-3d97-9627-dbab002be8b8 | -7.20932 | -60.611 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d14b741b-d791-3b89-905d-0709a5f8ea14 | -6.96154 | -59.08334 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b63c11d-688c-3b5c-90b6-d3ccf1d4473d | -7.00457 | -59.23525 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38bfb8c4-7011-36b3-adf2-f29128b02a8e | -6.6166 | -58.38398 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11fed1be-a2c9-3607-a4d3-935296b34082 | -6.17982 | -57.70147 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d87d0964-c476-308c-afe8-7aa8acb49082 | -6.26475 | -55.41554 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cdca7cb9-5318-3005-97f8-c333f898fc8a | -6.86031 | -59.40768 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8ace90d-df17-33ec-b173-b76fab17bca5 | -12.75765 | -46.45376 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20457266-2d32-3096-974c-1c19c21d9009 | -7.00958 | -59.24725 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a026b95-bff8-3d0c-8ec1-d5594dfe3c23 | -6.20647 | -57.76936 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0afe40d1-720d-3312-8e9d-c4ac0272ae31 | -6.7888 | -59.63694 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2de75a36-6fdf-35f5-80c1-e16e41001ebf | -6.1377 | -57.77287 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e72e1ad-9953-3037-87fb-f98b566cb563 | -9.69535 | -46.04673 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a4f1acd2-43fe-36e9-a39b-30fc5a54a9eb | -6.80032 | -59.45505 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0239db1e-ae6a-3661-82c8-84192e1183bc | -8.59972 | -54.73549 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd597b2a-0e31-3e9b-91da-2539959f634f | -8.0991 | -47.4687 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e48c8d61-9bed-36fb-9d34-06834b8fb46a | -6.80853 | -59.6902 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a67396c5-fea6-38e2-914b-aca84ce836e9 | -10.90801 | -50.24819 | 2026-08-25 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7faa67b2-793d-39c5-bf38-29412f6e936f | -8.6002 | -50.01548 | 2026-08-25 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0f1a9b7-2861-300e-9a43-839a76b8ca83 | -12.14238 | -50.60451 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 284f84a8-8107-3754-99b5-07ceca17537d | -8.1757 | -54.96666 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62e8be52-dea1-3aad-9cf7-748d9f694947 | -6.54179 | -55.09425 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c12508c2-d098-3495-a1d5-5454213a827d | -6.55715 | -58.52586 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0aeadc-6200-38bc-973f-d9ed186f9b44 | -6.44229 | -54.96451 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 561745e2-be3c-39dd-869e-bd8e8f47ddbf | -6.12356 | -57.84159 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191c8aa6-7be0-3422-8732-d30857b5b657 | -6.35766 | -54.75863 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 922b1a7f-fa28-365a-90ea-2cf9b6562636 | -12.74114 | -46.4776 | 2026-08-25 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed0a9ced-9347-33e0-aec9-ae11182f93ea | -5.94109 | -57.72788 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fc4e24a-32db-3e78-b7d5-913eff5f64b4 | -6.12958 | -57.82478 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11693463-1a1d-3e80-90d2-af4606831a40 | -12.88132 | -48.48056 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c95e3d9c-1277-3942-b947-881bc91a2cbd | -6.80374 | -59.45559 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41acf11a-7577-344e-8da7-fbfbcde68947 | -8.93343 | -60.71458 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6736fec5-ffed-302e-920c-19f966f2d9a3 | -7.38473 | -55.17216 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c10c9b04-130a-3efe-b556-4dee12921a49 | -9.97074 | -53.96526 | 2026-08-25 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 469e34cb-9125-3133-9a98-4008acfd174e | -6.5673 | -58.9766 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5324397e-8de3-3b66-bb70-9341be313f41 | -6.71109 | -55.59204 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46dea542-be43-3ead-aecf-6cb895ca7c5e | -9.2106 | -50.10119 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c3f9b1-f1df-3a3d-bc52-1e79cf39ec98 | -6.25789 | -55.41444 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22a5a1fe-cb38-3140-95cc-03ae7332e936 | -6.2189 | -57.68988 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc5e7b29-163b-328f-8300-f6151a1f241c | -6.44289 | -54.96059 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d461db98-e01c-3ef8-917d-b5a837ad55e8 | -8.15926 | -46.70091 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c577320a-d675-3dc1-8f1b-3d987fc4e9fd | -9.05263 | -50.79613 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fde6d050-65ec-32b6-b9bb-77dd187b536d | -6.82447 | -59.41338 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e80d18d-804f-389e-9918-d72859e7210a | -7.0 | -59.24203 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6f012330-2a40-385d-aea3-33f8eb2fc355 | -5.94717 | -57.73236 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 335c9809-7b7d-34fc-af6a-6d709a14b349 | -6.81606 | -58.65034 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66414fb8-a58e-368c-9ee2-7613366cb4a0 | -7.49137 | -55.35029 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f206b5b3-8f58-3f6e-a7cf-999e5d9b302b | -8.21784 | -54.99607 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0782f3d-832c-382d-8ee7-96cdd8eb238c | -12.75045 | -46.45887 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1fd122ab-f9ed-3461-ad22-136adfb39ea1 | -8.59672 | -54.73067 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d06968bb-6c39-3475-8708-c2725758cb71 | -6.12681 | -57.82082 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d2fd936a-fee1-3e8b-8367-be7ed06772c6 | -10.31991 | -50.40882 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a11cb35-665b-39b4-b9d4-a97a672cff39 | -6.70214 | -56.34607 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdc476b8-f040-39bb-89ee-0f0124c83bfe | -6.00101 | -57.66994 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 699407a9-6935-3687-a9cd-57c937ceeeeb | -7.22153 | -60.62027 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e84d9cc4-878b-397d-a6f6-f914e47dc300 | -6.85466 | -59.39924 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e950a85-c7ed-3ea7-83af-26e38b1c1b63 | -6.81598 | -59.59895 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3078e59e-d002-3f3c-94ee-93b438fd7ce8 | -6.13608 | -57.85056 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94cc55c2-52fe-3eba-a732-aa9526f3ca79 | -9.69472 | -46.05183 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 571b6d1c-309f-3a0d-ab2a-050e1bf07405 | -8.54478 | -55.30484 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d616ec3c-cc1d-3122-8706-06aa5c98c9dd | -6.74839 | -59.66902 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93cfe608-c5d1-3aef-b504-a73ca9aeb134 | -7.48959 | -55.36195 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffe22b9a-2e69-3c5a-99dc-773de479cd67 | -6.53911 | -56.25949 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 796bc0d8-ac2c-31ff-bb42-fd3fd722d47a | -7.0118 | -59.25507 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47717784-0b2f-311e-ac87-70db5357a6f3 | -8.61745 | -47.1493 | 2026-08-25 05:12:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9282b215-1612-37af-bfde-647cb540ac9b | -8.1751 | -54.9707 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1379231-e09a-3a44-a976-df14684dbf5c | -8.09807 | -47.47667 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 051241c9-2acb-33b9-a900-00ff7da94182 | -9.0649 | -45.21073 | 2026-08-25 05:12:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e7355c1-d6b1-3478-bf2e-8f7144e9d366 | -11.91074 | -55.89829 | 2026-08-25 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66e4617b-6b6d-36c8-80f5-8f703d3d05ae | -5.94332 | -57.73529 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c4dfe59-2d71-3779-ae08-17cd1cbc95ef | -6.87165 | -59.40543 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc82f632-ee05-37cc-b6ce-11347746daaf | -6.51546 | -55.22018 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73d3bbc-cd98-3d65-b1b1-d8fb7d73c2e9 | -7.00724 | -59.26183 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8da7a1e3-cd7d-393b-813f-ab39bec131ea | -8.22141 | -54.99656 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c213e746-2e83-3328-9683-957e88291e26 | -6.85408 | -59.40293 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c578d83-cf6a-301a-b433-191163b3a1f4 | -6.54706 | -55.08315 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45ffa1dc-d736-331e-be45-bc5ca571eb42 | -6.64271 | -58.49966 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11f9757b-d426-3ae7-88b7-2c6587f83bab | -6.25674 | -55.42198 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f9303bd-3eb1-34ef-a1ca-9909b31098ce | -9.39366 | -60.58188 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d93ab9a5-6f26-39dc-a3f9-89aa4eac68ba | -6.35405 | -54.78249 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e248eae8-9441-3081-af88-c7c49ebd0102 | -7.49841 | -55.36229 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50593e58-cbd0-3401-84aa-7ea0971d437a | -8.21067 | -54.97047 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6576d56d-fbc5-35f0-a4a7-b2a66b2c7347 | -6.84471 | -59.46211 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c77f7e3-2522-3a9b-843c-ce5fcb4a22cf | -11.97305 | -45.90496 | 2026-08-25 05:12:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e2d6c0a8-086e-34e9-b1f5-1b68b12a35b8 | -6.86372 | -59.40823 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a45dd09-5801-3a15-8a95-ff63b7464668 | -6.72078 | -59.4465 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28a77813-86f6-39e2-a837-5d0cc279bc35 | -6.99939 | -59.23789 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| e71786e8-e8a5-30d3-8ac1-c74a7514a296 | -7.38703 | -55.18064 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1982def-b56b-3494-809c-d1e793de4c93 | -6.25731 | -55.41822 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 481ae734-1806-39a3-b909-708014de9ac0 | -8.07312 | -44.64806 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4e5f39e8-5f2f-32b5-88aa-bdf072ea7646 | -9.16586 | -59.40266 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a0a4a09-73df-30d4-9465-1dbb971599aa | -6.83173 | -52.50187 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| abbf3bfe-b5da-3dba-89ab-0044ff6e0255 | -7.49727 | -55.36998 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79569f73-28e3-3781-840b-b3ca53bd7b0d | -6.36473 | -54.75967 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cf919e0-8cc1-370c-9bfa-9190e52fbc57 | -7.51134 | -54.85994 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28d714b6-4bc1-3252-8219-58aa540424f5 | -7.21373 | -60.62317 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
