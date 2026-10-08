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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc2bec4c-56fa-361c-8738-e54cd8c17376 | -6.1483 | -47.930901 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9aef7e-9bd3-3cf6-adc9-c602e638206b | -2.7604 | -54.121899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7280cb25-d179-35aa-890b-f1a50b6039a3 | -3.0805 | -54.306999 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d08efcf-e7c9-3f74-ba6e-7e6455087f64 | -2.8751 | -54.128201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6993d322-231e-3788-bcd9-a410d88bef94 | -3.0188 | -53.899601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1004bf88-7dd5-3b73-a990-290cd8d16029 | -10.2656 | -47.787998 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7105bcd7-21e3-302b-83cb-b2db036dafb9 | -8.2511 | -54.7276 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6faf9398-baaa-3b7b-9bb0-360f6e958b70 | -3.2598 | -50.411201 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 550f4b05-7da4-3369-ae4b-20e7b09f6fa0 | -1.8054 | -57.112099 | 2026-10-08 00:48:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae8aadf8-c95e-3184-b907-385f989980fc | -7.2216 | -55.1768 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b715b2d-3ea2-3c38-ac46-c677f671976c | -1.5298 | -54.822201 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4c7622-85a8-3363-9377-de58aa32ffd9 | -3.0123 | -53.916599 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46db9881-f782-3f8a-a386-75ce06c65ea2 | -2.9339 | -53.934101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdbd46cb-e311-3ac0-87f9-d95ec2a7c2c2 | -3.0051 | -54.745098 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c3ae38-000a-3efb-a910-3418ceb632f2 | -10.8063 | -56.505798 | 2026-10-08 00:48:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88904e4f-d131-3f55-8ddf-6dad523e3b06 | -3.5668 | -54.362701 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 317586a0-901a-36fd-8d7d-d7dfa3d3d4e2 | -6.2254 | -52.872299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e193b65-7169-3e4f-8084-a92b0ef7deb0 | -2.5698 | -56.180698 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07ae6023-1769-3fb1-9888-82be1f5de3d3 | -0.8475 | -51.849201 | 2026-10-08 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ea819ed7-cc5a-3cd8-99e0-f77a8652e29b | -2.8763 | -54.088299 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979efbde-7a1f-3b85-86fd-3f1eafccf351 | -4.8002 | -54.676701 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4c35d5-1623-3425-b9ce-cf225d262ab0 | -11.6495 | -43.693699 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37d5baab-1c39-32f7-b481-fde0eeb931ca | -8.7207 | -45.181198 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9eddbfc1-ddc8-3a4f-a098-0f4216284501 | -15.4232 | -43.712002 | 2026-10-08 00:48:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ba23b5f2-787a-3d1b-8623-9eb42610ff3c | -3.0106 | -54.090199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a503b7b-8ffb-3ef9-9d85-9e25be57768a | -6.3343 | -55.338799 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 844954b7-59b3-39c5-8d8c-0b181122b78d | -3.1052 | -54.188801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7631ca8-fcb4-3d2e-986f-d16fb6f9ed3f | -6.5161 | -55.279499 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cccf0641-110b-3a7a-8d59-821a79b00318 | -6.1115 | -55.7225 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2252c785-c98b-3f74-a0ab-d51e1cc267b2 | -3.0152 | -54.200699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee0e010-5fb0-3d84-a5f3-6d1c11164d65 | -7.2307 | -55.124901 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6c22fa-c69c-364b-8278-e07b22089460 | -14.7515 | -47.135502 | 2026-10-08 00:48:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46ed5cf2-007e-3d27-85da-8cb074cdb24d | -2.946 | -54.168201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e514d410-a7e6-3a76-8d7b-e864ab6f50c9 | -18.104 | -42.538898 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75ec61e3-8271-38c7-aa30-3f612323e3fd | -2.9829 | -54.104301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0083d4-c761-388e-9324-c0eef32fe794 | -3.3579 | -50.4781 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15905283-ccf2-3e2f-8301-1ac1f21ad324 | -6.0507 | -51.7393 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2e1bcc-94cd-33ec-81e7-1ec3ac8faf0c | -7.3848 | -47.6157 | 2026-10-08 00:48:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0066196c-6ec9-3003-af5a-7e385eb93cee | -7.2637 | -48.0648 | 2026-10-08 00:48:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f03855d5-efd0-3adc-82c6-aad4ffc5da28 | -7.4648 | -42.852001 | 2026-10-08 00:48:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a97ed5de-3cb8-3d84-8005-25ce5bb24505 | -3.2124 | -50.562698 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69baba5-34d6-33be-bcdf-dcf8b615d0ba | -2.2498 | -51.936401 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad13960e-ef25-3bb1-99fe-b67ac2ddc685 | -5.2714 | -45.418598 | 2026-10-08 00:48:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34f41fe6-8965-3c3c-ad49-67e000f699b5 | -3.8611 | -50.423599 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18983a4b-6aa0-3dc2-a4ca-53f33f96fb1e | -2.4898 | -56.099701 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175e9f0d-d805-3c1f-9030-1c7911eb4b46 | -3.3036 | -54.064999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7419be0-716e-3dd7-9bae-f307d7606512 | -2.4954 | -56.078999 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d02da01b-d9d1-3083-84ca-784db82ec9e4 | -2.2618 | -47.012001 | 2026-10-08 00:48:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c38f0346-823a-3a06-9465-071879581419 | -6.9527 | -45.2523 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9334370f-1d5a-3849-b33f-5aa680e36834 | -7.7449 | -54.944599 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16542137-09aa-355b-aab1-10128acc1cad | -14.9245 | -48.104099 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df8c2993-52db-3e8a-a614-91c701e8388e | -3.5184 | -54.648602 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9507151b-a5ed-3b99-91d1-05988cb47ab9 | -2.8342 | -54.129299 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0dec693-4b05-3f79-9840-e2e3376cd842 | -3.5882 | -54.6842 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 496dd95c-68e8-36bc-b06e-a847d7aee57d | -3.7277 | -59.4655 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 873ea2cf-ba4f-366f-93e1-8df18d35858c | -3.0624 | -54.182301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54aad15-f120-38f4-8e1a-fddec1a440dc | -5.816 | -53.8423 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ece41c0-6f7b-329a-a4fd-26c778cb2a48 | -3.1162 | -53.784698 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e69ec64-0c1b-39d2-8e7d-e658151302a7 | -7.8789 | -54.994999 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb9b1c6-5ac4-3be8-99ec-d561e676b5af | -3.1419 | -53.717098 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed257771-0793-380c-8c5d-70d9827c10c6 | -3.0572 | -51.231602 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c081aa-1671-37de-a6fc-3026966c91de | -5.9477 | -55.353401 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3159ac9-218a-3e48-be13-c4c7af938326 | -9.8237 | -44.792 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54752f72-7c9b-3613-abb0-823e9aa716d7 | -1.5084 | -54.818699 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f36d0e4-d0ce-36e6-9455-d48b9cab69b0 | -4.5753 | -54.957001 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceca2993-f750-326f-a085-a5f04881e6ab | -6.2188 | -52.843102 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e510fa0-e927-328c-8a28-c4f98089315a | -7.3875 | -46.241299 | 2026-10-08 00:48:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99535573-2588-34b0-a90b-d0223185792e | -3.277 | -51.066601 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd93c6d5-49d8-3359-af6b-f8b57df1c7a0 | -2.9986 | -54.037498 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bee862-e92a-3ea9-8df2-e80604537beb | -3.17 | -50.468601 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a748219-af35-3bd7-86a6-e39ef44f0797 | -3.2707 | -54.0564 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9df410-2913-3545-be8b-887f87bc3122 | -3.3315 | -50.185398 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57037447-4cf8-3e08-92eb-6808d746f05c | -2.9731 | -54.106499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c8f0d5-01e2-3a56-9a1e-00736af65690 | -10.4254 | -47.284 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 326c4d71-f059-3128-bfde-c7f892874ffe | -9.9071 | -44.795101 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 478ed9ad-c252-3189-8939-f2870bb80ab6 | -3.8513 | -50.4258 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94ecbf3d-2bfc-34f8-b204-5f67dad068fc | -3.2818 | -54.014301 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b43500e-9042-3d9f-8ecd-bf6d2dc9a01e | -3.2621 | -54.0186 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce0b5083-3614-3bd5-82a0-202f1273a352 | -2.9546 | -54.2062 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddcd7afc-9697-3da7-b07d-9a12d3ddc3b8 | -8.39 | -46.288502 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf10558-3974-3cfa-98a5-bbb56db950a3 | -3.1993 | -50.5509 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7943d1-36de-3804-8691-f8e4fdd55262 | -3.2366 | -50.1768 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913f4fbe-d62f-386d-9ef6-2af6bcc729c5 | -4.6465 | -46.3377 | 2026-10-08 00:48:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8874ba-3d8d-3655-bc93-7afe2dc2b61f | -3.5417 | -59.455002 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94c655a2-dbdd-3be1-9386-f492fceeb887 | -6.2285 | -52.795101 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7c3bc88-b993-3106-a350-4113da6c16d8 | -3.0003 | -54.044998 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09adb35e-6ede-3bbf-9b78-7961b1536bba | -14.755 | -47.1507 | 2026-10-08 00:48:00 | METOP-C | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e6ae7324-edf0-3816-b99a-df493afa58e1 | -7.8999 | -54.716499 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc1f08c8-e2fc-35d2-870f-8dbf2602e0e1 | -1.4 | -54.615299 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74aa7f62-bcb6-375c-a08a-363547f8e4be | -10.4467 | -46.852299 | 2026-10-08 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f96cd3f-1138-353b-b246-1b77131e0ac0 | -1.6081 | -55.164799 | 2026-10-08 00:48:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016da988-fdec-3d06-9b0f-28cbef264c07 | -5.9969 | -40.936001 | 2026-10-08 00:48:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe2f957f-d2eb-3a66-9fd3-c2359264f836 | -6.5791 | -53.025799 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013d54e2-2c27-37de-9fd7-e48e2bae4421 | -3.4755 | -54.641201 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2359f39-e989-31ef-98b4-938bf46b0d3c | -1.4343 | -53.235298 | 2026-10-08 00:48:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa66ed49-e01c-3979-a4c9-b05c29238825 | -3.0244 | -54.150799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e12ec1-1f54-31e1-a4b2-f643f8254619 | -5.9554 | -55.341801 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31ca83ec-9057-3989-9f25-3108f9860e42 | -2.7633 | -54.089699 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f6e670-22fd-31bc-ab07-60e97959a9be | -5.234 | -56.112801 | 2026-10-08 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b93539c2-17ff-360c-a270-fed7ea5b637e | -3.0324 | -53.959202 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README39.md)
