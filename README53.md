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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f057628-01a4-37b3-938a-a5454ae23b84 | -11.7809 | -46.3687 | 2025-10-11 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 236.7 |
| a850f12e-b2f7-3972-bd1f-f2a0ab70ae6a | -8.1807 | -43.321 | 2025-10-11 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.6 |
| 0ded8f30-15df-35b5-bdda-c02648f53cee | -13.2833 | -47.1203 | 2025-10-11 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| b97ef96e-8423-32fe-865d-546cc3844a69 | -9.2285 | -46.9063 | 2025-10-11 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c8b426d7-8185-396a-8dc2-ea52c696bae4 | -11.7422 | -46.3967 | 2025-10-11 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ad47b301-39ff-37fc-aa34-0202547f4e6e | -15.0021 | -45.5725 | 2025-10-11 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 1b89bc21-2292-322a-b891-9a97469f6e76 | -18.0803 | -57.5141 | 2025-10-11 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 827581c7-f996-3b0b-b299-f9ca46beb024 | -9.4137 | -45.7861 | 2025-10-11 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 9eba441a-9056-3859-9d68-28aaaee19d29 | -11.4531 | -50.2195 | 2025-10-11 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6b46cba8-bed7-3f1f-82e8-d84297a7d6fb | -10.6703 | -46.6954 | 2025-10-11 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 6bde7c6e-927f-3c04-ab71-a6aacab6cf7c | -8.5275 | -44.2379 | 2025-10-11 14:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| fa06f386-587a-3e99-b6b1-556e6219ab3c | -15.6538 | -44.4838 | 2025-10-11 14:00:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 6624c95f-5cf5-383d-be07-d41e66f15f34 | -1.1716 | -49.1055 | 2025-10-11 14:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| d88bd717-aad8-30b5-8c29-6a320d0bb911 | -11.7614 | -46.3941 | 2025-10-11 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 301da19f-50ad-30dd-a18d-ce1d54397325 | -8.8595 | -44.846 | 2025-10-11 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f9acf4e2-3b56-3fb7-ac76-fef959654e2b | -10.0731 | -67.5478 | 2025-10-11 14:00:00 | GOES-19 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 98565e3e-b151-3512-8d94-1e269822b87c | -9.5176 | -47.8709 | 2025-10-11 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a66829b3-82cf-3841-9d5c-7ed845ae0bff | -10.1714 | -44.5496 | 2025-10-11 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 666ed4f3-03a7-349a-877f-111489e9918d | -11.942 | -44.8335 | 2025-10-11 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b12b9702-267f-3120-8c43-c185eac62cb4 | -13.3026 | -47.1174 | 2025-10-11 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 16b0ea0b-5271-31d3-b743-e6709a84ba3a | -8.9833 | -45.4714 | 2025-10-11 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 53cd4240-fab0-3603-bcc9-b48f1619faa5 | -7.7919 | -44.246 | 2025-10-11 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| baa377d1-5947-3add-8ade-c410183941a0 | -10.9106 | -47.1353 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2e2622b0-2690-30b9-be59-bf733b6eecd7 | -10.8922 | -47.093 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| df192202-2ae2-35ad-83e8-ec25b83f5f67 | -8.2263 | -44.178 | 2025-10-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5ababbf5-0d68-307d-ae80-b7e5daffd0fd | -10.9109 | -47.1129 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| dc7e68c2-48b6-390f-99b4-9663166d2d3c | -18.0598 | -57.5577 | 2025-10-11 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 9a1ddd59-48d8-3193-842e-922934a7b5af | -7.7922 | -44.2229 | 2025-10-11 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6cec9813-ea03-3949-b097-d0c860f31d7d | -18.0796 | -57.5553 | 2025-10-11 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 66340209-49ba-3edf-b5f6-c058c65375af | -10.9364 | -47.9309 | 2025-10-11 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f9581245-972d-3729-b117-e086ab6e937c | -13.8117 | -45.7826 | 2025-10-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d949f520-00fd-3c9d-803c-bb7197329109 | -9.4137 | -45.7861 | 2025-10-11 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 351.4 |
| 97bef31e-cfa7-3451-a4ba-0833e7410677 | -8.1804 | -43.3445 | 2025-10-11 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| c56bff3a-4ccb-3b66-ab6f-0dd7413ebb5d | -10.8729 | -47.1177 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 10a43740-1227-375a-a83c-dba4ab386606 | -8.1618 | -43.323 | 2025-10-11 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 92acbc53-187d-35fa-9e4c-86c0b8fae718 | -10.8216 | -47.9888 | 2025-10-11 14:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| f7780914-5785-3f30-a157-d42044638cc5 | -13.8004 | -45.3917 | 2025-10-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| d0d3c799-8670-34ff-8238-434f1c164acc | -12.7299 | -45.8422 | 2025-10-11 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| c6243599-3e96-3219-a003-6c424f017cdf | -9.3951 | -45.7655 | 2025-10-11 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9e149986-2552-3bd5-9e9f-2297de65cfe8 | -10.1898 | -44.5934 | 2025-10-11 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5e40d993-cdcb-3fe3-a2ec-1f5f13acd5a3 | -18.0601 | -57.5371 | 2025-10-11 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 429cf291-b8cb-33b8-bd58-03b74808f771 | -9.3944 | -45.8109 | 2025-10-11 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 37dba273-38ef-39a7-b408-cb7570cea765 | -9.0022 | -45.4693 | 2025-10-11 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 391e89a5-d8fd-3e09-8200-933b709f9936 | -13.2829 | -47.1429 | 2025-10-11 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ef04bb46-42c7-3115-89ff-39c22ed30b5e | -10.0747 | -45.9121 | 2025-10-11 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| e3ced815-88a6-3ce9-9619-04b8618228e6 | -4.9071 | -41.5057 | 2025-10-11 14:10:00 | GOES-19 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 270fe5a0-3666-38f2-ad2c-14a41fe67fca | -10.8538 | -47.1201 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e7f09616-afd5-330b-98c0-1498ac659007 | -18.0803 | -57.5141 | 2025-10-11 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 4803adc4-3aef-3e68-b2c1-1794a83d5265 | -12.7676 | -45.8822 | 2025-10-11 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 431f8c2e-1602-300c-a63c-34340c053d81 | -13.2833 | -47.1203 | 2025-10-11 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 185.0 |
| bc30f819-18f3-36dd-ba99-b94e14e0968b | -9.3947 | -45.7882 | 2025-10-11 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 26fbd870-fe7b-37fc-b639-acdb5a10ff4a | -14.573 | -45.5809 | 2025-10-11 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 592ba81f-3764-30c0-9311-777a910c34ea | -8.2266 | -44.1548 | 2025-10-11 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| cd6fa46f-6a1f-3844-804b-7a3e3b245229 | -12.7488 | -45.8622 | 2025-10-11 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f6725d03-23be-39f9-9e4b-4f0a9279c1bb | -11.8728 | -45.4896 | 2025-10-11 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 69600c49-4370-3405-8128-77623bdf1de2 | -10.1714 | -44.5496 | 2025-10-11 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3af8d892-c8cd-33ba-9721-1383b2f37e61 | -15.6538 | -44.4838 | 2025-10-11 14:10:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 4b602383-4f48-3a07-9b90-11b8061f3f3d | -10.2085 | -44.6141 | 2025-10-11 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d14da1f2-ca18-3d90-a94e-9970343e48f8 | -10.8732 | -47.0953 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 1c167adf-c3ab-3482-a751-d87a9310f87e | -13.3026 | -47.1174 | 2025-10-11 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| fab451a6-3d15-3547-9767-c1b1c851eee6 | -18.0799 | -57.5347 | 2025-10-11 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 297.9 |
| 829a2570-c0a1-386d-9eb0-e6194eb4b901 | -10.9293 | -47.1553 | 2025-10-11 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 510.9 |
| 56b4b863-3e91-3d7f-8a75-03f3c730ed9d | -10.0027 | -46.9543 | 2025-10-11 14:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f6a2e2e5-2288-3875-ae31-2ba2c1f938df | -8.5055 | -45.9519 | 2025-10-11 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 77228634-1b7e-30d0-8d15-0da4ab1e5808 | -11.7219 | -44.285 | 2025-10-11 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 5f458e99-7685-3d53-bbc1-1d3a6e6d59c0 | -9.3947 | -45.7882 | 2025-10-11 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| fdecd14d-cde6-3f20-ab09-ae6b3741cf1d | -8.9833 | -45.4714 | 2025-10-11 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 4a4c5017-eeee-33cd-b628-3a89821da904 | -10.0937 | -45.9098 | 2025-10-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 217.3 |
| c1ce7b4a-b47a-393c-a608-becbc338f2eb | -9.5562 | -66.7442 | 2025-10-11 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d5974f50-7cd4-32cb-a7a8-315532673768 | -8.5029 | -46.1545 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 1e648094-f7a1-3de9-b13f-91fa7afc2cad | -10.8729 | -47.1177 | 2025-10-11 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f39b53ad-eca7-3529-8934-2fac6bb94a90 | -8.1882 | -44.2052 | 2025-10-11 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 67a4862e-753d-3dbc-b518-b77441452ce2 | -9.3944 | -45.8109 | 2025-10-11 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9cb2df8b-2e2d-3586-bf13-7ef3e6c35cc2 | -7.6804 | -42.5728 | 2025-10-11 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 30c0f584-8270-303c-a720-5513cb64f197 | -12.9192 | -47.04 | 2025-10-11 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f3f331c5-f6ce-3e16-8f71-ccf6b609dc56 | -8.4838 | -46.1789 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 50683d0c-9762-37af-9703-8b514fa45ce8 | -12.0118 | -45.2161 | 2025-10-11 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| fedd60f6-37ba-3616-a75c-0a32004da224 | -10.1714 | -44.5496 | 2025-10-11 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 9b20e1fd-02e2-30e5-9d07-9b84fbf81dd3 | -6.1749 | -38.8848 | 2025-10-11 14:20:00 | GOES-19 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 169.2 |
| aaa95415-e262-3d49-be1a-389d6fd20fec | -8.4841 | -46.1564 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b653d015-3d22-3fc6-95fe-a9ffb08b7052 | -12.9921 | -45.2252 | 2025-10-11 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 23e0f444-2375-3413-812f-2286e102fb54 | -8.5016 | -46.2669 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 21aec224-b91c-345f-aa33-71cf2b483930 | -18.04 | -57.5602 | 2025-10-11 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| ef2a38c0-67e0-3b85-ba6c-61eadc96868f | -13.2833 | -47.1203 | 2025-10-11 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| baa4db85-5a96-310e-a45a-878c136da5cd | -9.4137 | -45.7861 | 2025-10-11 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 844f605a-1af9-387f-ad7e-419eb8c0675d | -8.5018 | -46.2444 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 5108b27e-28e1-3e2f-a618-904298026366 | -9.0022 | -45.4693 | 2025-10-11 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 4f864c41-af31-3c30-8444-fe0836b0a693 | -10.9041 | -47.5588 | 2025-10-11 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c6cafb2f-6420-3a90-b0c5-49f592041760 | -9.1024 | -45.0477 | 2025-10-11 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 38004bb5-3e25-3468-8927-068ee1bf54f6 | -18.0598 | -57.5577 | 2025-10-11 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| ade47a6c-1b00-3373-b705-68bf4cdab802 | -8.4833 | -46.2239 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| ebef2c77-570f-3dec-8432-d4edacf43929 | -10.0934 | -45.9325 | 2025-10-11 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 4d90fe67-96c0-3efc-83df-65b36e3a006f | -13.8004 | -45.3917 | 2025-10-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 401.3 |
| 329c3447-2180-3d5d-9941-cfd21725c248 | -7.7956 | -42.4179 | 2025-10-11 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 0979dd1e-401e-3f56-ba39-1d4ed6067982 | -13.2829 | -47.1429 | 2025-10-11 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| d5110842-5069-3781-bf79-c511eec83ed2 | -12.7299 | -45.8422 | 2025-10-11 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8bbc053a-f7b1-3a1f-b377-b84749206643 | -8.5027 | -46.177 | 2025-10-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 98b363a6-5f2a-37b6-8596-71cc29003a6a | -15.6538 | -44.4838 | 2025-10-11 14:20:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 502.2 |
| eb8659bd-d535-3b93-9810-aeb245a23734 | -12.8999 | -47.0429 | 2025-10-11 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 26c0095c-eeb0-37b9-a506-0f67662c5391 | -18.0799 | -57.5347 | 2025-10-11 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |


[Clique aqui para ver as próximas entradas](README54.md)
