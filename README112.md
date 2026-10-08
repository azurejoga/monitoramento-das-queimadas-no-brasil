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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c0338bc-06cc-3374-9580-c4b28f2ce965 | -3.04199 | -53.89705 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d416feba-1cd7-33be-937b-a81080ec8ae3 | -2.86838 | -54.16123 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6d480b04-93e4-34d0-9a5a-d3f4a8dcd949 | -3.99267 | -56.2594 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a27450c9-ea24-354f-a8ed-fda8427db8d8 | -3.02565 | -54.0712 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87e5cf06-28b0-333a-80ec-26f9c9f454d2 | -3.28065 | -54.02416 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5170e03-688d-3f68-a1b1-2d14c95d63a0 | -3.01385 | -54.14578 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd432ae6-23bb-3887-a0b7-88e999c306dc | -3.51457 | -54.66031 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a323fbba-f972-3d35-86cb-87ad14a063bc | -2.90097 | -54.07592 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91bc0977-63b8-3f21-bfc3-f519cc10080a | -7.10278 | -42.53143 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd839ff4-8c5e-3932-bad2-a48446dec63f | -5.7534 | -42.05493 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 941f223d-0139-3af7-a240-500789b8ff47 | -11.64884 | -43.6921 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7387a6ce-5963-36da-abb4-6147601e1c92 | -6.63112 | -43.73067 | 2026-10-08 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 3583f2df-8c70-3729-a992-d0ff0ca67ed6 | -3.32075 | -58.22887 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de117569-8e2b-3424-80b2-4b0dc1211103 | -3.00729 | -54.23533 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a28e828f-d560-3979-b9a1-3e87e6233131 | -11.34806 | -46.96481 | 2026-10-08 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57e00450-dcc4-3c47-88d3-f3a8f30ac766 | -3.00722 | -54.06834 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 710c1b00-0840-3d38-8586-df184e4ce4c4 | -3.85193 | -55.9876 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2678cf4c-9edb-3e7d-9ba3-7257726eb65e | -4.93312 | -55.81264 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 814f80b0-6459-3fd6-8ee0-e9f1a216cf06 | -5.83745 | -52.05894 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea17d3b7-ba53-39c7-9d1e-548bab7f62c7 | -7.08153 | -46.28881 | 2026-10-08 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce8deb1e-0242-3689-881e-bdc25bf9ca08 | -4.30546 | -50.782 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddab79af-894a-3aa2-99dd-c97a40097b45 | -3.03248 | -54.23298 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eac55d71-6a54-3d9c-a5a8-3b907abf23d8 | -2.94132 | -54.05983 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43475d17-4475-33ce-b8d7-ccf11d999d9d | -3.29307 | -54.0159 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c03ca64-2c39-391a-9409-669efee3bccd | -3.42735 | -50.4372 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7c7fa98-a2b8-3c1c-8664-543a59952dbd | -6.86995 | -59.3466 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| acf0c9a3-bad9-3e2d-971e-bc7eaae9c202 | -3.07478 | -53.95034 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 73b35461-a0bf-3fd0-b078-0ddaa56c37ec | -2.99865 | -54.09837 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c0e1a8f5-326a-39d3-abf9-dff4b30649a0 | -3.01434 | -54.11875 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a9ee0b9e-58f9-3ab0-a191-b8cb9f3081b1 | -8.72691 | -45.16 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d739258a-bc08-30ad-ace6-42e2b7e8a328 | -4.78118 | -55.727 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe206508-c454-31cf-814a-186eb59099a8 | -3.29 | -54.01242 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 262b2493-8e77-3fd2-87b6-da167f6335c5 | -3.27388 | -54.06736 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7481ef80-fd1e-308e-b592-ae27a464d90e | -3.7412 | -51.21479 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b007267e-33f9-3af1-bcc0-637b195118e9 | -6.32106 | -43.35503 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 86d20df4-40b8-3646-9d01-b59d35e762fb | -3.08755 | -54.24611 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5987206b-f382-30a3-8955-a60703fe73c8 | -3.00074 | -54.08523 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7302b3dc-ff5f-3865-82bd-6dac14b79887 | -2.39741 | -57.89249 | 2026-10-08 04:46:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 249038c2-0255-3be6-a642-ecfe558ec269 | -3.47578 | -50.08235 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba9b9b38-89bd-3ca1-b7d2-d6a848a13b4e | -3.05322 | -53.92062 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a8770b5-025e-31da-8e93-2bce7ea2e2e5 | -2.7825 | -56.50581 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fe43e9b-0def-3241-94b2-4bebd093769d | -2.49427 | -56.3456 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2d1d3cd-e991-3b2b-83f4-0c2321610f76 | -5.99053 | -55.37125 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7b94c4ba-92b0-3cd6-ba31-80c28837dd50 | -6.92323 | -43.66925 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 647b3ee2-6427-3756-921c-6e89376389da | -3.27945 | -54.05342 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29e4f874-6a03-32e2-bd5d-6320c1ed14d6 | -5.22174 | -60.04626 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a98edac-839b-351d-980b-f8585919bac3 | -4.44555 | -54.9781 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b7a3ff-7198-3006-b8c0-7bb1cd98a776 | -2.4889 | -56.16737 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c5ead02-4eb1-3195-805c-af9b10e7262f | -3.26557 | -54.0484 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3bfdb8f7-025b-3540-a74a-313bf4a9f8ba | -3.66762 | -54.50714 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 236ef209-7601-3443-b8ac-1ae4a1e8afab | -3.86712 | -55.99756 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b05833fe-88dd-301c-bb23-736fd38eb20f | -3.71522 | -59.33944 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef5178f-12b9-3dbe-bb8a-50e70894f648 | -6.94361 | -45.27753 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b501af8d-71b8-371d-9d0f-5a340f702fe0 | -4.93711 | -55.81328 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5f28653-8250-34f4-9e25-b7d74ce98d81 | -3.54483 | -54.499 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0db61182-ab7b-3dcf-a8a3-2bdeebffa0d8 | -11.73864 | -43.6458 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 495bb93a-2a6c-3514-9382-3b8814039b38 | -3.11568 | -53.79006 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3217458f-cbc3-3bb8-beac-d3fb8ac97486 | -3.16738 | -58.63072 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e60557b-7637-39f6-8e8e-047b099c92b1 | -3.266 | -54.02185 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 06f40e2e-7150-34ed-8bbb-4bb1e60bec0f | -10.34454 | -47.75446 | 2026-10-08 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1c75230-1044-39af-b7af-d086c344cc9c | -4.42729 | -55.16074 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e953c671-3c72-31fb-a2a0-93c523080402 | -5.68929 | -53.47549 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6ed1575-85c9-3b19-854a-91136fcbbcb1 | -11.20376 | -49.42982 | 2026-10-08 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 167e4cd4-bc05-34d4-8412-f263ad99e34b | -11.1099 | -47.70431 | 2026-10-08 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 855d2639-0db7-3113-a09e-565a20e00d5e | -4.65931 | -56.216 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37f0954a-d8fc-34a0-beba-889fcaec697a | -3.85892 | -55.99624 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36d3440-e933-33e2-a5d4-1d29b3325ba2 | -3.84084 | -55.97832 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f6ec976-1a7c-3d8c-982d-11fa5ae19204 | -3.02285 | -53.94669 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32af3769-1fea-3592-b233-602b646e0c84 | -5.81936 | -53.83621 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43c8b551-73c4-3e3e-8d70-acc2b2da089a | -11.2693 | -45.19449 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6711cd23-0c08-3d17-88f2-46642eddfa1b | -3.07288 | -59.27772 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03fb52e0-2ce8-31ae-a273-4be6636e5c06 | -4.12231 | -53.8066 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d95390ad-0ae2-375a-a1d2-966dd9b99bf4 | -3.04649 | -54.1553 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bf0c913-34a2-3147-aeb6-ba2e04e5f9c1 | -4.26716 | -54.88186 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a46792dc-9d8d-367c-ad0f-5faab93d98c4 | -7.87689 | -54.98198 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b5a7354-3837-393f-a136-178cff76c3c5 | -3.85171 | -51.93748 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b31bae28-c4af-392a-b74b-9058c6b1194a | -3.54675 | -54.65374 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a181bec-65a1-37ab-a010-4ceb27b5d719 | -5.70644 | -53.5018 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 04a322e3-ba6b-3400-a85d-fc94f5767d36 | -2.87655 | -54.88665 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 30e173e3-0085-3290-a8a5-ee982949c34e | -2.86946 | -54.2021 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 499b8233-7c9c-3c81-a5a6-8e104adf372b | -2.48368 | -56.11819 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1fda35e-f931-3dfb-b1d1-e1f884072a2f | -3.04566 | -53.16449 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bea21b1-50c0-316a-a6e9-c1035bd15a89 | -3.01031 | -54.24037 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c772b821-14f6-3ee2-8a11-6ad14313e726 | -2.7728 | -54.07922 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad05ff77-6f82-3327-ac3b-ccada2cbeba8 | -4.07189 | -54.05048 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0ea06b3-f767-311c-af4f-e2a4bb410a8c | -5.67921 | -53.4938 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d63478c-c5f8-3c63-8b68-52d641b1467a | -6.02214 | -52.75982 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b5cae2a-4aa6-3ab6-ac9b-059b97017867 | -5.81702 | -53.83156 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fae693a3-8b12-3ae8-9554-4f5674d304f8 | -6.1197 | -51.95358 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0920595-1a2c-387f-b944-2f6b0ce2509d | -7.21234 | -44.33033 | 2026-10-08 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 114e79e0-cffa-34be-8f8f-943af2bafa17 | -3.66039 | -54.27884 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e388f11-31ab-3e2f-838b-7bfcc13c27ad | -2.72012 | -57.46968 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ad1ec2f-615d-35f9-86ea-24dc7d6d7afc | -8.72506 | -45.17326 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0210cc6b-3b0c-3477-af24-9e719e90c171 | -10.42015 | -47.2804 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d9742fbb-2047-313a-8a76-64d098509465 | -3.59142 | -54.66565 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d5bd9724-57d1-39e4-a619-7e648de7b5c6 | -3.47202 | -59.57477 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9414a1a9-0176-383a-92f3-6050d61ec474 | -3.85227 | -51.93393 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87dc0feb-9715-3598-8883-f405241bd252 | -5.96532 | -55.35759 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b1be5f3a-0baa-3c8c-b840-56478549ea0e | -3.26532 | -54.02615 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9f3e112c-4a9a-375d-ac72-85d277ddec6c | -3.69959 | -54.19362 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README113.md)
