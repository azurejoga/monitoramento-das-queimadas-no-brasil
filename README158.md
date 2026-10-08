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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080914a4-9e40-343f-b6fa-b026a3f384c7 | -1.10197 | -54.17123 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da6f38b0-f0d0-381b-baf0-e84d688f3b0f | -2.50692 | -56.16805 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2754029a-2429-3bd9-95f7-9435fb3d94c8 | -3.17849 | -50.55032 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f742a26a-f476-35f6-92e5-7cdfd28f1f00 | -3.03802 | -53.94391 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 432a5e9a-ccae-38d5-a6df-195679dcac68 | -3.47688 | -54.61941 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7ce9e80-a121-3913-8524-b95805b9848b | -3.74555 | -59.44159 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a271e12-0d70-35f6-8c12-66269c8d96fc | -3.06458 | -54.21027 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d0a08eb-d5ca-37bd-b388-3cba9e64e04f | -3.65656 | -55.50289 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 512ef0cc-30b0-3dee-ade2-dff90af2d5ce | -3.04857 | -54.26629 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7b718ff-92dc-3e97-9350-414be0ab9142 | -2.9986 | -54.10535 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36c0c4e4-2059-3eac-a99e-40145ffc9b23 | -3.29027 | -54.03705 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbb2563c-0aa9-3873-811c-46caeaa6f5d7 | -3.58332 | -54.65457 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e0a4e44-5320-3739-ac9b-b01efe1df5d6 | -2.94703 | -54.10939 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5f4793-4e35-3461-9ce3-54fd3ed632c0 | -2.75448 | -56.61061 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39e57b16-e2b7-3da9-930e-bebb579aa758 | -2.96332 | -54.21024 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfe883ff-2953-3da9-a4e6-e06864371a07 | -1.4872 | -54.5373 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14239748-0bf7-339b-87dc-284b7feb225d | -3.53424 | -54.659 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7fc52da-eec4-384e-b1ef-22b0122e598d | -3.05213 | -53.94612 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4338b0a6-fdca-330b-beff-531d159f56fc | -3.30202 | -54.6923 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2041711d-bcc9-38a6-96c5-7b92dcb21df1 | -2.49749 | -56.16304 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deb804a3-d5f3-32ff-a293-ef872c68e2dc | -4.5635 | -55.0569 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84b0516e-b71c-38d3-82cd-e69380235b95 | -2.83488 | -56.68002 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1586e857-168c-3701-9e19-77c631b23e1f | -6.05411 | -59.94423 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57758079-0d64-3e39-b795-e5826b9f0187 | -4.13454 | -54.26072 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08847e71-230b-33f7-8c6b-6348fba646ee | -3.5897 | -61.63483 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c6c6767-f8b7-32d5-bc6f-d7b743f3f80e | -8.61847 | -67.02325 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 95dc2593-4164-32d1-a349-e5697f67f9b4 | -3.08662 | -54.30266 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56207d08-91b8-3dec-bdad-9ad78016b965 | -8.54256 | -67.07524 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a8af9ba-7741-3af9-8585-30080e1410c2 | -2.99427 | -54.17952 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5b19c24-5cab-335d-9f4e-091eca2010e3 | -3.77823 | -59.25953 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a3374cd-a8b5-343c-93b7-92ddbaf91371 | -5.86357 | -53.46733 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9a840285-f254-33ee-a11f-c73a14dec450 | -6.49916 | -55.95578 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 303d70fc-404e-35de-9615-313d04127cc9 | -2.77436 | -54.11121 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0957ba40-64f4-3858-afbc-40e06b887c9a | -3.02625 | -54.06604 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27821ba7-19da-3284-ab75-973f79adb39d | -3.01336 | -54.7505 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35931f98-bc38-3b7a-a446-71513ce6d854 | -4.26907 | -54.88368 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36f495ef-5ae7-3502-a43d-c0c4d19e3f05 | -3.48323 | -50.08756 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b16621c1-5313-318d-bafe-5067b208e165 | -4.42929 | -59.49112 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2ce1ce0-6018-3cfe-912d-6fee5f467757 | -4.1193 | -59.88073 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0bb84b8e-40e0-3e96-9915-d8635e4f37bc | -3.54767 | -54.65674 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be8079f9-47e4-3468-9d1a-890b153043dc | -3.3027 | -54.02689 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3bb837ee-21cb-3a0d-b9b2-d745b57b25aa | -2.8531 | -59.11046 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d56ee86-b5ac-3f25-b541-b912631ac370 | -3.13151 | -49.24028 | 2026-10-08 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97a64cd2-03e0-3fe5-9407-8dbe15f94cd8 | -2.99868 | -54.08159 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 96fd4f60-9383-34d7-93c2-7e1050b4ac88 | -3.28092 | -54.02759 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94acd79-e165-34fc-86b0-22ac93251a1f | -3.58807 | -54.57861 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37728af5-9d57-3fdb-a984-8d37a86b0ce4 | -6.23781 | -52.84981 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58702a9f-8df7-3f55-ba29-1ffe0f63b54a | -5.86137 | -57.56113 | 2026-10-08 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a29f84a5-beb7-3988-bb9b-d25b2c392c34 | -3.01567 | -54.73571 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91708c44-d3d0-305c-921e-482f9ba58adb | -2.4951 | -56.07054 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a2f695-b157-39f8-b8d1-e82ed5d85a6a | -4.06202 | -54.03273 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7d7cf42-4970-3b7f-b323-11207b227d86 | -3.55532 | -59.49466 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3e503c9-6906-39d7-996d-9bb4c8050409 | -2.57384 | -57.78878 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddeee1d5-dc76-3c92-9ee2-54ebe4c36412 | -2.96945 | -57.76273 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 739ba16d-fb38-3ce4-a692-3bb5f91b98fc | -6.05767 | -59.9448 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 332ca78e-d1f7-32c7-b26d-fb8786bb97ae | -1.83686 | -59.95925 | 2026-10-08 05:23:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5de4e89-da78-3ae1-a81f-6009ef16742a | -6.31625 | -54.80169 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9fcce0a-11e8-3384-a575-3d68b66d2c0b | -4.14439 | -54.0359 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df7367f1-bd5b-3afb-8e12-3d448cc08ca0 | -3.3056 | -54.03136 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d66c1da-05bb-368f-bcc4-cd0a741a54fc | -3.96383 | -56.11247 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05e01107-1ec1-38fd-a931-747386b07949 | -3.9646 | -56.12322 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52b82b04-eaea-3284-8f66-43bace7ece46 | -1.12115 | -54.11716 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aacfdd81-c27f-3b09-bd2c-f1bafd35a6a9 | -3.09129 | -54.29559 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37c45e16-2996-3ed8-85d6-79340cfb934a | -2.76796 | -54.10628 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ab9c6a9-0233-3cd1-8a49-9fb26751ec9c | -3.04451 | -57.48761 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3d14f77-09cd-3d38-ac93-4c0e53762d08 | -3.19517 | -50.55704 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 380d04c1-d270-318a-8a82-b4fe41462e26 | -2.55001 | -56.31977 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfdbf755-d007-3700-a7b2-bc61614845d2 | -9.077 | -65.48875 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5513663e-1798-3492-a8a5-ca4ae95f541e | -2.51134 | -56.16166 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcb1ec88-4cb9-3255-b42e-71205886c596 | -2.50575 | -56.13245 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24cbb1b9-9319-3aa7-aea9-8c85fe842da0 | -4.236 | -49.99091 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed1cffaa-3b26-383b-87dc-5b732723af91 | -3.96743 | -55.8299 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9d5535-75a4-3524-9218-0193d168fdde | -12.09942 | -57.15594 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff343bb-3fc7-3cb3-ab7d-1f400fb206c8 | -3.29519 | -54.0057 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5527f05b-66ec-305c-a0df-447eb7121b50 | -9.48234 | -64.36673 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf1e52c6-b3b4-35a3-9b3a-5d7cba97863f | -3.30503 | -53.87371 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 974b8026-503f-39bf-a12e-c6733e1e82aa | -3.62362 | -55.50523 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8b3b16-0657-30ca-a19a-ce532124c2b7 | -6.84611 | -59.29997 | 2026-10-08 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a55b8c08-436d-3d35-bc8a-928b9e7e8486 | -2.81703 | -54.09028 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47e4f001-7c9f-3aed-a1e0-f12a14649461 | -3.02905 | -54.09425 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6b2e2d4-19d5-39de-9407-840d15906f3e | -1.48379 | -54.53679 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f67df3-0ed6-38cd-b6d7-74b8fb0516d3 | -3.11095 | -54.16909 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0bf79d00-8792-3b26-8290-dc41b96c82ad | -5.67505 | -46.35091 | 2026-10-08 05:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9708560-876f-3b50-a57e-eecebc693ac1 | -3.5714 | -54.49142 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3256d095-184a-38e1-b677-222ef6d3c63d | -9.12253 | -66.00993 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 266f9561-330b-30d4-b7a3-85ea2338367b | -3.00159 | -54.08601 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b4453ffd-940c-38f7-bcca-56594c904863 | -3.84375 | -55.97237 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b3716ba-92ee-395e-91b4-73cbfa8c5352 | -2.61019 | -57.58235 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8798b0e5-1838-3768-ac92-6519119cb6e2 | -4.42553 | -55.16053 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85e45387-6bca-35a0-b8fa-020cf40a4737 | -3.51549 | -54.59858 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c09c2056-e075-329c-a44d-8841b94a04fe | -1.50962 | -54.81409 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f49cf66-a0d4-35f2-8a6b-f8dd1e54987f | -1.75197 | -56.19111 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6859d999-f7fe-3bab-89fb-2b51465b0c77 | -2.67424 | -56.4567 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c87b98fe-b12e-367a-b506-b0af6251fe64 | -2.87081 | -54.88262 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6bb0070-8a65-3e99-b655-1effe05133b2 | -4.29195 | -49.0949 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b78f57c0-1853-34de-a60b-39085a38eac0 | -3.70365 | -50.66076 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11c2214a-595a-3896-8c75-f892aeb8b813 | -3.58925 | -54.57099 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 615f71a0-e063-3bfe-875d-d3cd2dbade75 | -3.74782 | -59.29102 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b48baa-bdb2-35ec-b564-75c69e908a36 | -3.6331 | -59.54756 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74f81b5b-e558-3bbd-8955-05ef1993c775 | -3.27264 | -54.03434 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README159.md)
