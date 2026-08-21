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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ffdfe72-73d1-32b7-b702-077f157a95e6 | -6.6938 | -58.942 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d88c6e4b-e88b-3c1e-85ad-bd9808b14e4b | -9.0722 | -60.434 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 21564bac-c12c-30ab-91ba-093fa70a9b56 | -9.208 | -59.6548 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ae364f30-bf0b-3397-bbce-324f375bb74e | -11.1561 | -54.0028 | 2026-08-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 222efae5-5bbe-38ff-9f94-cb8f46de5d91 | -6.2341 | -55.6109 | 2026-08-21 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1d8d2b54-5165-3405-9836-a982b8f8d778 | -21.8854 | -41.3198 | 2026-08-21 14:40:00 | GOES-19 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 147.5 |
| af86a410-f70f-3521-8019-5b4c25fc0439 | -8.5175 | -55.324 | 2026-08-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 2a5d9c05-083b-3619-8954-aae83c28ffe9 | -13.7188 | -51.8675 | 2026-08-21 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 217.3 |
| d71f997b-2ac3-30ee-b1ac-0774eba0120f | -6.95 | -59.2984 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 145e2da2-b04c-31f9-812d-d1b4fcb4798b | -9.4072 | -60.3977 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 33bec490-bf6a-3b58-a2dd-2bf4430c0594 | -6.3654 | -58.3354 | 2026-08-21 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9fdb7f93-fc79-3a16-b762-2d9156b72e4c | -14.997 | -52.6775 | 2026-08-21 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| ce6b3700-f57b-3c39-9fb4-08b49b30e64c | -14.1993 | -53.054 | 2026-08-21 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1eab7e87-2293-3ac8-8863-90ac1a23a86a | -11.1747 | -54.0216 | 2026-08-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 54f69185-b5e9-3f3e-aefb-97dcf547ec04 | -13.7384 | -51.8438 | 2026-08-21 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f0500045-84f8-3cd2-8f5c-0b368f156276 | -6.6014 | -58.9844 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f43fcfb2-259a-3bc5-a3dd-1679e73bfbcb | -13.3929 | -54.3551 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 995db79b-db25-35d3-8932-14feaf3bb8ba | -13.3926 | -54.3758 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 21d75e55-99aa-32a0-aee3-cacfcce56911 | -6.5828 | -59.0044 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 745c9931-b21b-3ee3-9a59-55dd6ab8163d | -9.4061 | -60.5518 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bd27ce4d-983d-3806-a84a-afb830aaa591 | -17.6726 | -44.4776 | 2026-08-21 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 97d956bd-3235-3f60-964d-675a86be0d58 | -8.9042 | -60.5385 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 71302993-4055-3a16-9018-aec40937c09a | -11.3801 | -46.3558 | 2026-08-21 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 8d344146-feea-3d68-bcf7-93d959ac6b8f | -8.3718 | -62.697 | 2026-08-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 10c70413-4ad9-3513-86b7-26515d76868d | -8.3717 | -62.716 | 2026-08-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d65e8702-b720-33f8-9696-b53f5bcea992 | -5.6208 | -45.7027 | 2026-08-21 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ba250a27-c992-32ae-9abe-2263bc18e058 | -13.9367 | -53.859 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6aa19529-a9af-35f7-83f7-7670793f0b43 | -5.598 | -43.9978 | 2026-08-21 14:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| c7e878f1-c651-3b9e-a2ac-24c1e79527dc | -11.367 | -45.9949 | 2026-08-21 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 70e6fa18-0b5b-38c1-88cb-ce0824181f70 | -6.7647 | -59.4601 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9aa7d8a3-2d6c-3eec-9b74-0f0380d9dc97 | -3.2178 | -61.2551 | 2026-08-21 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9fde6564-1cb2-34e1-abcc-9df03f064aa2 | -14.3343 | -51.8944 | 2026-08-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| be30b2f5-7cc0-3cac-8502-8f36e7f1e05a | -6.5829 | -58.9851 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 230ad5e8-535f-391b-b767-08eb9329d261 | -5.6022 | -45.704 | 2026-08-21 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e2208c12-916e-30ee-8a48-b479c5ef4582 | -5.6024 | -45.6815 | 2026-08-21 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| f2e277f8-2e1d-316f-87d0-bd79e30ab4e0 | -9.4558 | -48.2717 | 2026-08-21 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7b344485-f74f-39e1-8d23-0d60b9aecb77 | -9.2071 | -59.771 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b1640029-b13b-38f3-84d7-6ea66d86579a | -8.9041 | -60.5577 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 72e9b252-94fb-396a-8fe7-6d9e98fde447 | -10.7504 | -50.3182 | 2026-08-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 5e964fc2-0f93-3789-bb24-8866c7ec19c3 | -8.3902 | -62.7152 | 2026-08-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 8bc0a909-47da-3217-ba8f-c5e77a19c194 | -13.937 | -53.8381 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2e9abfd8-71f4-30ee-b2de-6b7ac42be7fd | -13.6243 | -51.7732 | 2026-08-21 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ac1ddf4e-fe2d-3629-9d32-8f59a4279d4d | -9.4071 | -60.417 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 230.7 |
| 6ddc43b7-7ab9-3e63-a382-17424c672a63 | -6.871 | -45.9901 | 2026-08-21 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c90720ab-c581-3991-91cc-6fe9d135286f | -7.7702 | -61.1634 | 2026-08-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 61fa7994-9e36-3fd7-bf72-1e2c804dc3ac | -9.4257 | -60.416 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| adef5767-7dad-3a78-8e41-d26ea827268e | -15.218 | -48.2263 | 2026-08-21 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f275adb6-9e3b-3f67-a388-8b8b569e7c88 | -8.3903 | -62.6963 | 2026-08-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b70f9fd9-ec18-3bdf-b868-88a3f8c7ef8e | -13.412 | -54.3531 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 61b32fd6-d97c-3961-a0ad-a93f3716f8be | -8.8856 | -60.5394 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 5806dda1-6c7f-30b0-b74f-ae075507be77 | -14.3149 | -51.8969 | 2026-08-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| acbc7324-ea41-3915-8734-c37813c0a7ab | -9.0536 | -60.435 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 5ba30576-0c43-330f-80a2-1bed0e8d8334 | -13.738 | -51.8651 | 2026-08-21 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ffab7777-1f4b-3c38-b23b-18061710531e | -5.6168 | -43.9965 | 2026-08-21 14:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 3f1b49ce-0f01-3bd6-8f4d-3d2356f0590b | -13.2431 | -51.6295 | 2026-08-21 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ee61315b-203a-3a88-99d4-a0d63220f465 | -14.098 | -58.8611 | 2026-08-21 14:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| efb7f09c-9edd-3ae5-943e-e706fde2434d | -8.5361 | -55.3228 | 2026-08-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 6af88db3-7f61-3af4-8d62-33d9cf5acf15 | -15.1984 | -48.2296 | 2026-08-21 14:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 294.3 |
| 3fca7ab2-3203-31d5-b402-dbfeff45a842 | -6.583 | -58.9658 | 2026-08-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7ad586e3-8cc3-3454-8c92-ad022d69ebfb | -6.6729 | -56.3436 | 2026-08-21 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cdd3b5fa-079a-32f5-87c0-3fdc67cc6158 | -6.2538 | -55.4109 | 2026-08-21 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b0682d25-9ea7-3caa-abc8-718ab37d8deb | -8.0467 | -51.804 | 2026-08-21 14:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 571238e7-9d32-36c1-b3dd-53549e8a5588 | -9.406 | -60.5711 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 856b8620-4ee2-3b80-8fb7-d56475687fcb | -6.8937 | -47.4738 | 2026-08-21 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 1aec6154-fb67-3523-8e43-57f56ee633b5 | -9.4069 | -60.4362 | 2026-08-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| da788f51-23d0-372c-a5ba-36fb4b70db63 | -5.621 | -45.6802 | 2026-08-21 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 6c6840e8-247f-3430-ab5f-15a64d878157 | -8.8855 | -60.5586 | 2026-08-21 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 8b3b1fea-3aca-3e10-8428-d4a46b5b1096 | -8.1572 | -46.747 | 2026-08-21 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 77be503b-7d10-37a0-b66d-698085b04f9e | -11.3892 | -50.6972 | 2026-08-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ca9b4b1a-4d1d-3e4e-889a-7626f5ffc920 | -8.5173 | -55.3441 | 2026-08-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c0862f9c-3cf8-3449-b055-b384ada81938 | -13.4117 | -54.3737 | 2026-08-21 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1a9ad1d8-01ed-3bf8-b0a0-2073daca537b | -11.175 | -54.001 | 2026-08-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |


