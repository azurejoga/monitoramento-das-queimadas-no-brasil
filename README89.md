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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c755ccf-f6c9-39cd-8e7d-9481e18ace27 | -6.75424 | -59.11331 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93ce6857-e0ea-369c-9d88-17c7149b82ce | -6.3336 | -59.95163 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a1865f3-4b35-356e-a57c-ce465a1eb199 | -4.34794 | -55.64967 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ed35ae-c34a-35b6-b10b-182fb7b35637 | -3.07351 | -61.28238 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8cabeeb-a57e-3d45-8356-d86e37143d5d | -11.95115 | -46.52091 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb341dbf-68fc-35f4-affa-f5ae64d35b5f | -4.25754 | -60.00932 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b791f47-7c38-3ae3-9406-6f7dea843844 | -3.05116 | -54.41557 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67651546-d3aa-3863-b1d3-0b5ffe86beee | -11.9882 | -58.07363 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a6f6c2d-3bb4-32a9-af90-bdc279beef85 | -6.73952 | -55.09658 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29239dce-d5a3-3692-ad35-edc412876d10 | -13.86203 | -48.58181 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7713301-21f3-3663-b87c-1030a8e6fded | -3.46489 | -58.32903 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a577310-b2ee-314a-854c-156717ed18be | -2.53996 | -48.15921 | 2026-09-22 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6bac39c-825b-3680-ae4f-99e428689553 | -8.15222 | -54.80202 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e8b218-08b9-31f4-8f14-fe192f29e637 | -2.91349 | -54.18843 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef443135-23f2-33a2-aa44-0053cab4aed7 | -11.95831 | -46.51563 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b13dc3a-9834-3a99-aac7-ecec62aa6e89 | -4.3491 | -55.66438 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91abc4a7-15e7-310d-8dae-e2506cc72960 | -4.41163 | -55.24139 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2fb434-aaab-3416-ba13-e4cc4038d5ea | -13.3693 | -51.30798 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cd08443-87cc-327b-b4e8-531941bf272d | -4.28399 | -48.6215 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f22bb8f3-7582-3bac-818c-cca5f0e2e141 | -6.64095 | -59.92244 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ebd11be3-0bff-3470-bb07-b06255762733 | -9.11199 | -65.382 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50757e0-2d0f-3c8c-a792-97fccb47a411 | -8.67399 | -70.02739 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba488dc-a6b7-3541-af9b-9173d20c1002 | -11.81043 | -58.17631 | 2026-09-22 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8557ff3e-939d-3ed2-80c1-eec89c285edc | -3.68938 | -60.5677 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bed6d13-fcb6-3ef4-8a3a-8d800f7f8d3a | -9.56801 | -66.03574 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b073e7f-bfb8-3df4-9187-9dd717d7ff36 | -6.45664 | -59.99045 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75d5ed21-2dcb-3b56-b46c-ac22db0b0fa4 | -6.52131 | -58.30914 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 890fce18-3200-3cfd-ab49-e5c2aff4be3f | -2.96626 | -57.62617 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aeb32a7-29ed-3e5d-a07d-217c00658982 | -4.55955 | -54.93832 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 03a6d9d0-a300-394a-afbc-d8ab36da11b5 | -6.04719 | -57.8233 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 819102fa-fe1f-3d48-8db6-dd533a541663 | -12.83811 | -50.97737 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41c65a10-2cc4-3ffc-be33-2f6f267ac4f8 | -1.21293 | -55.62605 | 2026-09-22 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5aa9699-47d2-31b0-8120-f72e149b4843 | -6.16088 | -57.72696 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af9f3cc3-a2c1-3d23-8646-2266f316366d | -6.65113 | -47.43358 | 2026-09-22 05:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8340575-0eda-38a3-a470-02eab85764c8 | -5.80738 | -57.742 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 558c45ec-d0ef-339d-a214-7d9b3c802707 | -3.48738 | -59.5652 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12435c16-59ce-3e06-bc90-f332fc2b1ae2 | -9.10832 | -67.82363 | 2026-09-22 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00722fd4-ae75-30b5-98b3-23d398b92038 | -6.04264 | -53.2768 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e42bc9c0-3a2b-33d7-84bf-4636e8c26ada | -11.88446 | -46.85448 | 2026-09-22 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c68e6d8-35d9-31c5-b24c-5da3b176f214 | -3.75571 | -59.42606 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe7630b-95d3-3caa-9de5-31a866cafe45 | -12.79303 | -54.03899 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ff7795f-6739-303d-8aca-99e83733784e | -11.01379 | -54.15 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2be2052e-b4cf-3f9f-8f5f-12a38e1c8987 | -12.35412 | -50.22962 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05192039-7548-33c5-ae09-953c005f5ce9 | -3.20564 | -53.95471 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 978db618-ddab-30e9-bb8c-090cde8ac4b0 | -5.83843 | -53.53129 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 187f3007-e143-357f-8312-73ba32c4be9f | -3.48963 | -59.57384 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3db6d417-e359-3145-b8c6-469201844bab | -14.76277 | -48.44573 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed509b7-cd88-3061-9e2a-7dc2a6a6f8f6 | -6.35014 | -57.77481 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bea31a4e-5518-3c43-8756-b0f73c6d995c | -7.32066 | -46.76693 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 894fb1b5-9275-3fca-bd42-956d4afb42a6 | -9.75776 | -65.06053 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03416e01-42ec-3566-83ee-11dcb37a213c | -2.95773 | -57.72275 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 462238ef-2f1d-31c0-8e92-8c346f499d50 | -5.41851 | -60.21327 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81466092-62d8-36c9-8100-ea94ce045543 | -4.51956 | -55.75963 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8439ba3a-6025-336e-af34-06b6de346ff3 | -6.4291 | -55.61406 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1b0f6fd-8f1d-34c7-8bc6-5f6aa8719de2 | -1.77067 | -54.79011 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d52e9330-bca9-3d33-b987-bfdd7446c402 | -9.55721 | -66.03949 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dec55a1-2745-361b-bed2-1a6e63ef21f1 | -11.23864 | -54.10861 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27482361-f366-3bb5-b5e4-58119e69ff10 | -5.94126 | -57.70293 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9caaec4-d075-3362-a6ac-8bed1f882599 | -5.87317 | -51.94546 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ab2a1a-494e-3ed2-b137-34ba66ca7a18 | -3.52253 | -59.94128 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd484196-52a5-3efd-97d8-4754e619c6bc | -6.00899 | -47.90022 | 2026-09-22 05:23:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d21ba37-fed0-36cc-85e7-3b3b0c007ff7 | -3.38742 | -61.29239 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6e37306-e38c-395b-974d-ab0381cf4f37 | -8.3359 | -47.5333 | 2026-09-22 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8422445-fc61-32d8-8bd4-5afefbee9d92 | -6.1914 | -57.77111 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a051a4-1771-3b3f-b89e-405d0bccfdd2 | -3.00862 | -54.17845 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52faa9e8-43c0-32c4-a9d4-c72e21d1e1c9 | -12.84872 | -54.04713 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee0d45a-b317-3d18-9754-8c5cfbc54705 | -3.48753 | -54.68548 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e65498-bdc7-3ace-a3fd-31cd915cb514 | -6.6515 | -59.92415 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| a6bbcc1c-e9a7-3392-b1d4-837a7e810fd7 | -11.94522 | -46.51559 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a80e3f24-f7f4-35aa-9ae6-475810688f4e | -8.17131 | -54.82164 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d087bbcf-441b-35fb-908d-8cac8129f359 | -3.06512 | -59.28081 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddfa1fbd-d349-3e22-a6b1-39044dc6b67d | -7.6114 | -55.35781 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd7dc84-6553-3661-acd1-8db3ab81fc57 | -3.80801 | -55.66398 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8818d8c3-69b0-3c8a-918d-236737747012 | -6.4637 | -59.99164 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 476d54f0-19ff-3b5d-8ffc-f2890928cef2 | -3.50796 | -55.48713 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b98209e-36b2-3211-89f8-b033f23e8aec | -8.78729 | -44.28023 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d15919d1-08a7-3fff-a124-0c4d2887ca4b | -9.19005 | -65.85141 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03255900-62e7-3865-ae8e-2b4a544cf795 | -6.78703 | -48.67605 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f6785d4-9aec-3de1-a7b2-a44ae9857f17 | -5.01215 | -56.08984 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1d49a4-5ef4-3cb5-89d1-1c26251a1e81 | -2.87256 | -57.79325 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe7b5cd9-56fa-37ad-94f9-45baacd97e69 | -7.3867 | -51.77421 | 2026-09-22 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b03d8abf-2f64-336b-8255-321e2c83530d | -6.23734 | -51.00909 | 2026-09-22 05:23:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 865bebfd-4d24-3b76-a767-b6c95adb2c46 | -11.50531 | -51.51451 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40263cd7-68cc-3c0b-8513-cf1d73163fef | -3.37659 | -52.79292 | 2026-09-22 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d55a04f-9150-3cac-8db3-f55eaf83f205 | -3.77053 | -51.35121 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e383a41-75c8-3b48-bd85-62fb83c15326 | -11.04991 | -54.14532 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9cce568-620b-327e-b29b-777cbd871e6e | -15.36196 | -48.10882 | 2026-09-22 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9aa48d9-d9fa-3fdf-b377-4f7153674e7c | -7.32299 | -46.76908 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3eb20bfa-48b6-32d9-9aa7-a83af35f51a6 | -4.07169 | -56.22681 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259144fa-eb8a-3503-94d4-89f27586896c | -12.14086 | -47.39217 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf9f1c25-70e4-333b-b3dd-7bdad3f23d89 | -13.51156 | -51.52015 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| dcf644ef-efae-3e04-9682-02b2c49c43e9 | -5.98623 | -57.69936 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc191a07-c526-34f6-ba78-265006065d44 | -5.46683 | -60.21534 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f1b72d8-e74d-3209-8756-339d84c6036c | -15.36147 | -48.11331 | 2026-09-22 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08fd49aa-23e0-386d-b172-74a14d80fdf6 | -6.62401 | -59.9156 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 382eb2c4-b220-38bd-aee9-684c5de98250 | -2.53477 | -57.55104 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ccff81b-7872-33b6-9ed1-c4daabb7b650 | -4.50794 | -54.98455 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8dcc31db-76b9-3135-8b43-1d9d484ef8da | -3.66561 | -54.26672 | 2026-09-22 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 877a5855-5c00-3faf-9360-3754133f4ff4 | -4.96225 | -55.82816 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fb47946-4a9d-3ba5-b0b5-73a897be01e1 | -3.47625 | -59.58832 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README90.md)
