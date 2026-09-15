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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c26f1d5-2093-377b-921a-141acd03debd | -13.7722 | -48.8087 | 2026-09-15 14:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 20785a33-1fa0-333a-b8b1-5630bf542e89 | -6.6953 | -58.6903 | 2026-09-15 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c8228ac0-5e44-303a-9d62-77bd5f8c1192 | -13.414 | -57.0225 | 2026-09-15 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| e773d4d8-5741-3a86-89e2-ad5c44fc1d8e | -10.6522 | -50.5845 | 2026-09-15 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 9344a9cd-85c0-3d48-a622-2391dd97a89c | -6.7463 | -59.4416 | 2026-09-15 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 4c321e43-73b1-3779-a7c0-4ee217a68851 | -15.539 | -53.8502 | 2026-09-15 14:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 562d080f-e176-3769-abdc-7eaa3b46f615 | -2.7768 | -49.4553 | 2026-09-15 14:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 18b2b865-62e9-33df-97a9-7ef758f81d9f | -8.8361 | -62.489 | 2026-09-15 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 466277a0-6400-3c20-99d6-55c9e2ad23c2 | -13.4085 | -54.6009 | 2026-09-15 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 37fdfedc-96ec-3bfc-9611-d6de811e5f34 | -12.126 | -44.2225 | 2026-09-15 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 75c91721-ce6b-35ea-aecf-bb7784343251 | -13.3059 | -51.3022 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ae023c91-f67f-34c6-b34e-9f233af42e40 | -12.6821 | -54.7174 | 2026-09-15 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 92b5987b-176d-3b5e-9a46-2e2d25261762 | -11.3114 | -47.062 | 2026-09-15 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d499eeb6-a8cb-3d96-98ae-aca5688cb859 | -7.1711 | -44.2367 | 2026-09-15 14:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 6d4d6d1c-abce-31b2-9c35-cb7f4c34ed35 | -14.0133 | -53.8709 | 2026-09-15 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cc7273fa-c300-3853-b503-0d2e00237e92 | -9.7358 | -47.0958 | 2026-09-15 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 75396b42-5a4d-3898-b64a-37ae3340352e | -12.6636 | -54.6782 | 2026-09-15 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8abfb167-d2e0-35e2-9fe3-d88e759428b6 | -10.6525 | -50.5631 | 2026-09-15 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e9c20999-9123-3b9c-9913-84455ae324eb | -12.3273 | -47.9735 | 2026-09-15 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 645cd11c-5c76-3e23-8847-fd743c9bc62a | -10.792 | -46.2071 | 2026-09-15 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5133091a-c394-34ea-9621-481978dd7b89 | -14.013 | -53.8917 | 2026-09-15 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 3d9e18b6-5687-3524-b6ae-a80b3ffaa2e9 | -13.5722 | -51.4391 | 2026-09-15 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| cf39e8fb-3649-3efe-9387-274f4312636e | -8.7892 | -45.8773 | 2026-09-15 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 23be0819-bd2d-3673-9312-1d9a21d749d9 | -13.3202 | -51.5986 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 789a1ef4-a684-337e-b091-d2f92d4a7251 | -13.3199 | -51.62 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 903cbf3b-314c-3293-9d2d-75487915967c | -7.1525 | -44.2154 | 2026-09-15 14:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a0b6de81-739c-3778-934f-116a24321418 | -15.5397 | -53.8081 | 2026-09-15 14:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 12cac030-fa46-3852-8ba4-22d937faf61a | -13.2996 | -51.6862 | 2026-09-15 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b67242c6-5404-3bf3-b7ae-fb2c69e9521e | -6.8944 | -47.4079 | 2026-09-15 14:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8886fa10-e3f7-32ef-af8a-850ef587c010 | -7.0823 | -42.1107 | 2026-09-15 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 178.9 |
| 9e992ee2-d207-3f84-a725-27965bdf35df | -2.7767 | -49.4765 | 2026-09-15 14:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b8c222a4-470f-3e72-b6f8-01fcda137a17 | -12.6826 | -54.6763 | 2026-09-15 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bbb89a4a-7639-302b-bfe0-532293bd68e2 | -8.638 | -44.4567 | 2026-09-15 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 427.0 |
| 5de9783e-b651-3ac0-b602-ede3eba8d750 | -6.8408 | -43.5021 | 2026-09-15 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 96e16a6d-e13e-32c9-a11c-ae77c141cbe7 | -4.6589 | -42.0726 | 2026-09-15 14:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 4a7b1f90-82f8-3697-afd3-a61163cd2de8 | -13.553 | -51.4416 | 2026-09-15 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| d0f04abb-426b-3072-bed7-cde2dfc3bde6 | -6.7464 | -59.4223 | 2026-09-15 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6d260357-4cbb-3e85-b3c1-cd70d2d3a028 | -6.6952 | -58.7097 | 2026-09-15 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f4e2466d-6a3b-3d0b-851c-c2d7321062fc | -8.638 | -44.4567 | 2026-09-15 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 187.2 |
| e56e0015-3fe8-33ed-be76-06177a8d2ae9 | -9.3765 | -50.0925 | 2026-09-15 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b7d02686-b6be-34f8-b996-af8e4a79b239 | -10.792 | -46.2071 | 2026-09-15 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1f6bff48-a2d0-3edd-8b51-656b73ba6625 | -8.7892 | -45.8773 | 2026-09-15 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 8cf375be-ff5a-313b-a015-64996553f6ad | -3.5727 | -58.5389 | 2026-09-15 15:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 35e49c62-8dc6-3956-8606-0d2ac2a599c5 | -6.1362 | -59.8871 | 2026-09-15 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f9026cc7-9288-35a2-be5d-5ca5a6aa9a62 | -14.0133 | -53.8709 | 2026-09-15 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 08da0cf6-970f-388a-b0f0-060a26433ee4 | -13.414 | -57.0225 | 2026-09-15 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| cb34b8d7-2d0b-3bea-afac-45872a032151 | -9.1742 | -56.9358 | 2026-09-15 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 65aad0c2-f991-3a02-ad5a-787a60002b71 | -13.7002 | -51.8274 | 2026-09-15 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 4efbf95c-67e7-3c6f-b221-ac133104d1c0 | -13.2235 | -51.6531 | 2026-09-15 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| d2676a38-1fc9-36e7-adaa-cc5670b9b75c | -5.2023 | -49.3348 | 2026-09-15 15:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 115a0a63-1300-3160-aeb4-e15145d6a9d9 | -10.312 | -45.2907 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d22934c8-a92c-3f07-bdb6-4d5844f8fb88 | -15.2827 | -42.783 | 2026-09-15 15:00:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f94cbb38-a427-35f7-9a3f-71ba51a548f9 | -13.7722 | -48.8087 | 2026-09-15 15:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8a4b7ab2-cb78-381c-918d-80f001b0ac3e | -9.7358 | -47.0958 | 2026-09-15 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 1d35834e-07be-3dc1-bcc9-dc29ae600117 | -10.0194 | -45.8055 | 2026-09-15 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| c9603c03-4c7a-34f8-8516-168c3975d516 | -6.0255 | -59.9484 | 2026-09-15 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 10684bef-80e6-3b07-865d-6b127d9126d3 | -2.7768 | -49.4553 | 2026-09-15 15:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 1641efbd-771a-3e86-bd84-cc092d88f93e | -13.5719 | -51.4605 | 2026-09-15 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c9b3c188-286c-3c60-9b4b-93a1e5ac09df | -9.7687 | -46.1067 | 2026-09-15 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1a774fd0-21c0-3ee8-98ed-ee132bbf2119 | -6.8408 | -43.5021 | 2026-09-15 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e7cdd1e5-7cc3-31e6-9065-71948d9a9c72 | -6.7648 | -59.4408 | 2026-09-15 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 560117ca-6049-31a7-8001-919b094e0f2a | -13.7006 | -51.8061 | 2026-09-15 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 55889095-0270-3675-bae8-9aa1d4f2accb | -12.1265 | -44.199 | 2026-09-15 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| cfe5e054-639a-3919-9d01-fd51fc30f9e9 | -6.6767 | -58.7105 | 2026-09-15 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ecaf4564-cab2-34dc-94bc-acfd34d925ac | -8.8459 | -45.8713 | 2026-09-15 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ca0b7b67-7862-36fe-b28d-f06b33432eaa | -9.1337 | -65.844 | 2026-09-15 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a3f37023-78f1-340f-9256-727116a735d6 | -3.1174 | -57.6779 | 2026-09-15 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c90e4bc3-f1da-3d57-baa6-48339abc46ce | -7.1711 | -44.2367 | 2026-09-15 15:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a5bfe8f6-9d91-310e-be8c-2e08e35e45ca | -2.4815 | -49.3996 | 2026-09-15 15:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4e9312b3-14d9-3c70-8752-739ea5c15766 | -8.7889 | -45.8999 | 2026-09-15 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.9 |
| ca282981-975f-394e-b4a2-23bdf5dc1161 | -7.0823 | -42.1107 | 2026-09-15 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 763617c8-eafc-342c-9682-6b79f918bbda | -12.6821 | -54.7174 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9a24e702-3253-3903-8eb4-978e8a394aea | -13.2996 | -51.6862 | 2026-09-15 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a2d5895a-401a-3017-90d6-e7bca5b9327d | -3.3676 | -59.8285 | 2026-09-15 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1a48f9e0-1778-35b7-b501-0be74f65b8b1 | -9.1708 | -50.0049 | 2026-09-15 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a541f0c5-16ae-334e-8375-7db676bfd24b | -2.9395 | -50.3994 | 2026-09-15 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 28a0aaa7-b0d7-3515-a742-f45b694b4282 | -6.0991 | -59.9459 | 2026-09-15 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c3ea095f-db7c-3995-b09b-0368e9206473 | -12.6824 | -54.6968 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b22c2247-3b9c-3b8d-8932-8bc8b661a5a6 | -10.2929 | -45.2932 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ad34d115-b31c-325c-95dd-4673fe490b58 | -12.5333 | -47.1414 | 2026-09-15 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9f4e8ebc-6229-399a-91e8-65efaf2f68b1 | -13.4468 | -54.5968 | 2026-09-15 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 11b8294e-637c-3ac0-bbfb-851ae870d7ec | -12.0471 | -49.9344 | 2026-09-15 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 037c8ef0-c622-3c57-8700-c47191d8f1ef | -13.2239 | -51.6318 | 2026-09-15 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| cee90060-79fa-39d3-8069-a22b770438c4 | -6.641 | -58.4987 | 2026-09-15 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8d1d2e7a-4ca7-32f8-871c-ca122780fab7 | -13.4085 | -54.6009 | 2026-09-15 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1549be96-ceff-3450-a79b-025a939b674a | -7.5608 | -62.33 | 2026-09-15 15:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 4118ca54-c70b-3cd2-abd2-9dcc329a3699 | -13.553 | -51.4416 | 2026-09-15 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 1b6d60ce-6e5a-3fad-a854-5df8c250031e | -10.6958 | -47.5175 | 2026-09-15 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 2c5d9351-7970-383d-8688-2b641cbecd20 | -8.8078 | -45.8979 | 2026-09-15 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 77dead06-2cc6-3b57-85cd-59e4eb60b3c3 | -13.3946 | -57.0444 | 2026-09-15 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 79e89c4d-14f8-3a7f-9adb-e71a7eda82b5 | -10.9595 | -50.2529 | 2026-09-15 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| b371aa7b-ff1f-34eb-9872-0017604d974d | -4.6776 | -42.0713 | 2026-09-15 15:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 181.6 |
| 414df25e-1093-3ee0-b1b7-3cd2dc8f338c | -13.3949 | -57.0242 | 2026-09-15 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| ae54c6d5-4a37-3bbb-8954-fbcd185a7c9a | -10.6827 | -54.1679 | 2026-09-15 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1fe4e310-f874-3f00-b9ab-bb36f4390dec | -12.126 | -44.2225 | 2026-09-15 15:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 9518a6a9-5f22-3855-828d-7a084a47d84a | -13.5722 | -51.4391 | 2026-09-15 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cf23b53e-03bf-3fca-be2b-a4e7bf44962e | -10.6829 | -54.1475 | 2026-09-15 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| bb6728e8-fe64-3e35-b640-abde86e03a59 | -10.3113 | -45.3366 | 2026-09-15 15:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 173b7bab-9f41-3658-87fc-d72ee74b6f5b | -13.9941 | -53.8731 | 2026-09-15 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 11ab2cf4-310b-3e07-b826-c80f47f0d8ff | -12.6826 | -54.6763 | 2026-09-15 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |


[Clique aqui para ver as próximas entradas](README84.md)
