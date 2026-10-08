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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5364c96-c6ee-3806-957b-fbc746cdb894 | -9.4936 | -64.3518 | 2026-10-08 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 718f6f92-efd0-3e9a-9031-0448cc5c1c5e | -1.4118 | -48.9318 | 2026-10-08 01:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4c87361f-de7d-37a7-9c19-6a81832dd118 | -7.1964 | -45.354 | 2026-10-08 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 34f983f6-45be-3bb9-8fe4-7619fb7b1f8a | -3.1973 | -50.5382 | 2026-10-08 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 04916f98-c9c0-3c9c-b84b-44438c07c320 | -16.8642 | -40.5709 | 2026-10-08 01:10:00 | GOES-19 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| cc53ba2e-2624-358e-b490-36ee1d16cb26 | -3.1697 | -58.6437 | 2026-10-08 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| d61a6138-a317-3b82-8d81-112e19382d45 | -9.475 | -64.3525 | 2026-10-08 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| c3ca999d-d114-354a-bf00-c60c989c21fe | -3.11 | -54.1862 | 2026-10-08 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9de28cc1-6ed8-34dc-84ac-bbbe1f94217c | -6.15 | -39.4409 | 2026-10-08 01:10:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 72.9 |
| ba2515be-440e-37eb-909b-cb8d22a0eaa2 | -3.8383 | -55.9774 | 2026-10-08 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| e86eb35a-d2e8-3235-a5a6-1dc6092997e1 | -9.0591 | -65.9396 | 2026-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1680acd5-1ea7-3afb-a6ff-e7254e8f08e5 | -3.478 | -59.5779 | 2026-10-08 01:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1f69df58-64d9-33dd-bcf8-a6a522039531 | -3.6049 | -54.5736 | 2026-10-08 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c1423ef8-79bc-36ce-9942-ffe82053cb76 | -6.2343 | -52.848 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 47cb3f9f-560a-3794-b293-5d3ebb653ef2 | -8.6291 | -67.0296 | 2026-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0909d133-c330-30c3-9653-62f7f4c37a4d | -2.7612 | -54.1142 | 2026-10-08 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| af8350cd-6ebf-31dd-852b-11dcf927e9a0 | -8.7228 | -45.1812 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 292.1 |
| d1879ff1-bcaa-3d0e-954f-77e6d5c2a325 | -11.014 | -45.4272 | 2026-10-08 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a32bf8a1-d122-3955-a071-68491019cdeb | -3.8567 | -55.9769 | 2026-10-08 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 8f325d81-a5e0-3a8d-9818-9fee04046bff | -3.073 | -54.2874 | 2026-10-08 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 331ba040-cf6a-3337-aa30-4ed9174d34b3 | -2.7796 | -54.0937 | 2026-10-08 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1658d230-6595-3490-93a7-da62e0bc65b3 | -2.5903 | -56.1642 | 2026-10-08 01:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4d44f1aa-716d-3684-88db-7395a51c4fd5 | -4.1176 | -59.8888 | 2026-10-08 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d72771c1-486e-3202-a3f3-4cef02c847a8 | -6.1689 | -39.4391 | 2026-10-08 01:10:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 86.4 |
| d58bf87e-bb75-3e96-ad37-43ff98574506 | -6.2529 | -52.847 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f8035e3d-a9a2-3fdb-9dba-0c80b3b1c5f9 | -2.7797 | -54.0736 | 2026-10-08 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 31fb3171-1f8d-30c5-9697-179122d14215 | -10.4337 | -47.2824 | 2026-10-08 01:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| e6657996-3dac-3008-ae31-2806d9805935 | -2.7981 | -54.0732 | 2026-10-08 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 417970e3-1df9-3418-be1e-708ba4c77b38 | -8.7417 | -45.1791 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e72d0218-23e0-315f-8487-481a6f240d31 | -6.3163 | -43.3614 | 2026-10-08 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d335e3c8-46fc-3f29-b3e9-3f59e02a702a | -3.2313 | -46.9596 | 2026-10-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 784f14e5-aae0-3df1-b202-885ad50a82c6 | 1.6937 | -55.6263 | 2026-10-08 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 1f00a978-1057-30fd-9f04-7467cc1830f2 | -6.6317 | -43.73 | 2026-10-08 01:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d4eb08d2-979d-3454-8b04-137e8dd4b3e4 | -8.3882 | -46.3006 | 2026-10-08 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d5c52aa8-57c9-3149-9959-e5d5d53460ce | -2.7152 | -57.472 | 2026-10-08 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c498df32-053f-38a5-ab9e-75235ca65ddf | -6.2157 | -52.8695 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b16560fe-b4d7-3322-93ba-1941c92e56b5 | -2.7613 | -54.0941 | 2026-10-08 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 1dd0c412-01a5-3fc3-a691-0c0579a5947a | -3.1101 | -54.1661 | 2026-10-08 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| afc5472f-33df-3483-83e8-e44f063f1f92 | -6.3165 | -43.3381 | 2026-10-08 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f24de5f2-5cdd-30a8-b8f7-8250d4503a20 | -9.4578 | -40.3392 | 2026-10-08 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 716c7594-587b-3f85-92a8-b7a60ca0177a | -5.6931 | -53.5073 | 2026-10-08 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| a4ea63a0-e2c8-339e-8257-f06b63ef75b1 | -4.3473 | -43.779 | 2026-10-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7a15ac81-6969-3c83-a14a-511f7bf06d27 | -3.1298 | -53.7834 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7694a924-88cc-34a7-9f5b-a1f0064fe7f1 | -2.572 | -56.1646 | 2026-10-08 01:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 7f663601-0ec6-3087-a20d-7d226c930774 | -6.2158 | -52.849 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f35cc00c-6235-3cbb-81cd-c685c46b2e01 | -2.798 | -54.0933 | 2026-10-08 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 088d4dde-fa3b-3050-a510-93d37ba4d7a4 | -4.3471 | -43.8021 | 2026-10-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| a20a63f5-66f4-39f8-9faa-1b33b6c1c634 | -5.6932 | -53.487 | 2026-10-08 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 256.3 |
| 229283c0-cdbf-30ad-b633-d3b46061bbdf | -3.1285 | -54.1657 | 2026-10-08 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| df347ba0-c380-3b43-ac26-a32c6f4af19f | -3.1115 | -53.7637 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9909f5d5-07e6-37d8-a6ba-ce50536484f2 | -12.2513 | -44.7164 | 2026-10-08 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f45701f8-997c-3506-8b6b-caccb7799692 | -3.2499 | -46.9589 | 2026-10-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| dbcee507-3b72-3ba6-8240-d9f841c9337a | -6.3351 | -43.3598 | 2026-10-08 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1eeec6c6-23e6-3e2d-8d32-69d4abd05c8c | -3.478 | -59.597 | 2026-10-08 01:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| a31ebd57-9f8b-32e5-9d10-d914d01dc8bb | -4.2954 | -49.0807 | 2026-10-08 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 12afa127-4328-34f7-82f3-de9e2dc1bc77 | -3.019 | -53.9272 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0a8f75ce-319e-36e1-bf2d-72a18ae4f0d1 | -3.328 | -50.1775 | 2026-10-08 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9577b03d-6285-333f-870f-400fb7b0a97f | -9.4749 | -64.3713 | 2026-10-08 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c072a58e-3bf9-3bb0-a767-5765ae37a45e | -3.2157 | -50.5586 | 2026-10-08 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 80e22039-a1e0-3993-b598-e5f537b9fa72 | -8.7039 | -45.1832 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a67a43de-7efe-3870-b47a-a19087cc5c7a | -10.9949 | -45.4298 | 2026-10-08 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d214762b-e3da-338b-a2cc-235b1571a4e4 | -5.731 | -41.7549 | 2026-10-08 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 23588e3a-77d3-368d-ae64-d4a40e517b06 | -2.8575 | -59.1107 | 2026-10-08 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 0e640b01-b1e5-310f-b19b-ef9066ab51f3 | -2.572 | -56.1842 | 2026-10-08 01:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| dec3ade0-575f-3612-a8c3-3c6d760a24e1 | -3.5515 | -59.4807 | 2026-10-08 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 81df5204-5346-310e-8c2a-34e0b736e256 | -3.5865 | -54.5742 | 2026-10-08 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 45106978-2033-3f9f-9241-b59fdbf3002b | -5.7376 | -45.1533 | 2026-10-08 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 33fe26f9-885e-35c8-93d6-0689d5b9bca1 | -2.4032 | -57.8848 | 2026-10-08 01:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b872c876-3722-3504-9a0f-a105027d3f7d | -5.6934 | -53.4667 | 2026-10-08 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 10c9776a-2dd8-3e7d-8668-0e1d22f89aec | -5.75 | -41.7294 | 2026-10-08 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 5ebae982-1db2-308e-8db3-3fdf0c0fbe4b | -5.7498 | -41.7534 | 2026-10-08 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| eb960f37-b092-3ac9-ac18-ced914c07b65 | -4.4507 | -47.9112 | 2026-10-08 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 5cc5b076-983f-3cfa-962c-5b171a31c3a0 | -6.3353 | -43.3365 | 2026-10-08 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 77317f5e-1307-33f7-b6c6-ac75fd286bfb | -5.7117 | -53.4862 | 2026-10-08 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 230.1 |
| 64df07ac-2a9a-3d98-b13f-47691a7929bc | -4.0628 | -59.8328 | 2026-10-08 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6bc4a097-5d7b-3562-b224-a8bfda03f016 | -6.8764 | -43.685 | 2026-10-08 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7bb969e8-18bd-3948-8bcc-1ff5b663ddf8 | -3.1114 | -53.7839 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c084418c-7d18-35c7-a2f8-a6981eda95ca | -3.0914 | -54.2669 | 2026-10-08 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b31b6475-e47c-31e6-8e48-88e0fe02b8d3 | -4.3658 | -43.8011 | 2026-10-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2595197c-fd56-3bd7-a4cd-6b0d1137a6f8 | -8.7225 | -45.204 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 46e18906-2563-332d-b8b5-9c1fcaf0f4eb | -8.7231 | -45.1583 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 94488a41-b1df-3b7d-a2c1-29da2480cb23 | -8.742 | -45.1563 | 2026-10-08 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 759c8d86-173d-31a0-bda3-cf6672f242d4 | -3.0374 | -53.9268 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| cd17d274-0ea4-37a0-91f6-8f06616a64cf | -3.1284 | -54.1857 | 2026-10-08 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 6437cfda-0be1-3a86-a0db-07e266d1fe5b | -3.1879 | -58.6433 | 2026-10-08 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ddfcfac3-e3b8-36eb-a182-52406db05ee6 | -3.0913 | -54.287 | 2026-10-08 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7f9acd99-a780-3931-9c94-556a6ff74fd4 | -9.0592 | -65.9209 | 2026-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d9f0f4d7-8a5a-302a-b697-b7246b16ba2d | -6.2527 | -52.8675 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| ece4017f-9427-3cbd-b7f2-11f4780f631b | -3.1972 | -50.5592 | 2026-10-08 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| c4bcfd5d-cebf-32fd-abee-656794d52128 | -8.537 | -66.9764 | 2026-10-08 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2ae94b55-e940-35e5-b584-84e195dcc4d3 | -12.2316 | -44.7427 | 2026-10-08 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 44a9236e-502d-329e-b671-e1bcea0afa0e | -8.0895 | -55.311 | 2026-10-08 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| eb09691f-5c26-3633-a56f-00108e9961f8 | -2.4031 | -57.9041 | 2026-10-08 01:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8be84aea-b665-304a-966f-d5e73b782c41 | -5.7 | -53.5 | 2026-10-08 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b67ade7-d3d8-3e74-b266-6a141cc9508f | -3.0 | -54.11 | 2026-10-08 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8895351d-8697-3f46-b66d-5a2f5d4d483c | -3.0 | -54.04 | 2026-10-08 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8672aa9e-a7f1-31f0-aab7-a71004640dfe | -8.73 | -45.2 | 2026-10-08 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd04ab9c-da9f-3554-b2e5-1612424c62bb | -3.02 | -54.05 | 2026-10-08 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7f26924-5909-31b5-b810-9989b02b00ba | -3.02 | -54.11 | 2026-10-08 01:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 277823ae-5e47-392f-81cf-bfcb6033cd9f | -10.4151 | -47.2623 | 2026-10-08 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |


[Clique aqui para ver as próximas entradas](README45.md)
