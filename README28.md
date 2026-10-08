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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e50d6a4-17fa-3f19-af16-3caf82b632e1 | -3.0111 | -54.137798 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78c0190-0dd7-3c23-8a1e-f07bc0969088 | -10.8835 | -49.1553 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1a5695d-af82-31ec-a0f7-1383d0215121 | -5.6855 | -53.490799 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17d3d4c5-e86e-35be-a6e8-b730822e8cfb | -3.1733 | -50.438099 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7966fd5-a358-3118-813a-d950465bd722 | -3.2786 | -51.073502 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7b64c3-c6ed-3faa-b3e1-e4ff9c516a68 | 0.7688 | -51.3675 | 2026-10-08 00:48:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da3cc85f-365f-374c-bdec-835500cf7788 | -3.5525 | -59.5033 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e76369f-313b-3a57-bc22-5a9971bcf586 | -4.1075 | -54.023399 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 194bb108-2bfa-3792-95fc-33cb86104e36 | -11.627 | -43.686298 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2675664e-b57a-3a2a-a6ad-fdca7c9b427c | -4.0752 | -51.0387 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32746bf1-3851-30d3-863d-8c36cd5758fa | -6.155 | -52.652302 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c2e6417-35f6-3d6e-bf8e-a9edee7c933b | -5.7432 | -45.153198 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73ca5c21-b37e-3e7b-a9d9-2b320be9ec0a | -4.1043 | -54.418499 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f88abf6-eb18-302a-b5bd-89eea0dbfd43 | -3.1782 | -50.459301 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243ebe36-3c83-3c40-b903-f157a3a0db73 | -22.017599 | -49.5784 | 2026-10-08 00:48:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff99bf17-e084-36d6-af5f-d77cd30d39fa | 1.6963 | -55.625599 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9da42d5-e457-32b4-88cb-c7389dfad9e7 | -10.3093 | -46.6231 | 2026-10-08 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52ef06b5-208b-3fec-ae4d-b8f6b224843c | -3.3408 | -52.5116 | 2026-10-08 00:48:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1955970-27f3-3ac1-9b72-0f262f378e62 | -7.2155 | -45.357899 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a36da735-ae7e-3bf3-97a4-08f186c4c21b | -3.1212 | -53.8069 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72aecee5-6580-3ce9-9856-15ff79696a8b | -2.9454 | -54.120499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 150d6040-6d00-3e91-a888-46fa21cf28f2 | -5.8952 | -53.5084 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0c4d6b-462a-3f84-8894-11c51887cce0 | -3.4848 | -50.090401 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b69b800-8fb5-3b92-899c-3e7f314d8b12 | -3.3677 | -50.475899 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98f8a537-0afb-3579-8138-aec6e929598a | -1.52 | -54.824402 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5805a33-a91f-36db-97fc-d17516b2c50f | -3.0949 | -54.279598 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f4a25b-ec1a-3508-91fc-01b420e738fd | -3.2839 | -54.069401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1bb1cdb-48c1-3134-bd7f-ef0c7d35b155 | -2.9748 | -54.113998 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca53b71-698e-38d5-8153-5f5c7469c518 | -2.9817 | -54.144299 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3707cfd-a495-388a-b4ee-bef91ce3ea62 | -2.9425 | -54.153 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a63d70f-c48c-3191-a831-35bd0f7a6828 | -5.8538 | -53.461601 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f64638c-e2bd-3266-8733-28c0b91b9528 | -3.0672 | -54.2938 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae2c6a34-114d-3cdd-b2da-5c9690a49d1b | -14.9228 | -48.096901 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9384eee4-8c94-3ccd-bf61-d077524f9ac4 | -6.7262 | -55.115898 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7016ba8c-9762-3bf4-8b7b-a7f56b169bd5 | -3.1342 | -49.246399 | 2026-10-08 00:48:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d0a90c-900e-3a11-a893-b79306321e74 | -11.6239 | -43.673801 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2202e5-043d-3270-a9aa-f33ea1087a20 | -2.9921 | -54.189899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2787955d-350d-36d4-967f-ce0b98d6e2af | -3.1338 | -54.360199 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eec5a55-1907-38d4-ad0d-a95297dc289f | -2.999 | -54.763401 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 315a780a-86ee-3bb2-a4b4-7478518cc19d | -2.5677 | -56.171299 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d31fa1a-849d-3447-9fd7-99a98762c81a | -2.7482 | -48.430698 | 2026-10-08 00:48:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 657d760d-2167-3431-8a81-0201fa60bcb3 | -5.2443 | -50.919399 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c232c5a0-3ff1-3210-a066-91f9f5528485 | -3.1583 | -50.597 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 202aaebc-8b5d-3367-bc94-0e6c63e227aa | -22.0273 | -49.576099 | 2026-10-08 00:48:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97c1e235-abe9-32b4-afbd-8755fc063bda | -3.2382 | -50.183998 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee23561b-95f9-3896-a064-c01b16465cd1 | -6.1009 | -49.403599 | 2026-10-08 00:48:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f226bc0b-6fc5-3ae6-be7e-514309496227 | -1.532 | -54.561798 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2237fd72-a38d-312d-914f-55216f5f0f72 | -11.344 | -51.883701 | 2026-10-08 00:48:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc6bf939-8da3-30ad-9c84-6a83f3aac8ee | -3.006 | -54.115101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd03eb5-082f-344e-9664-bb4ca536a929 | -14.9148 | -48.106499 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d9010be4-d1b7-3531-a995-1ae5da8076eb | -3.0504 | -54.265202 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be10155-b014-34bc-be09-25647d2e77c1 | -4.5185 | -54.9785 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e7bd99-e5a8-326d-8e39-7190d8edb8d1 | -13.7795 | -52.8009 | 2026-10-08 00:48:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99f77924-cd5f-3fb2-84eb-19239740f16a | -13.1699 | -54.331902 | 2026-10-08 00:48:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6403665e-42eb-3a87-9102-4e211e2f5f73 | -3.0868 | -54.289501 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e380cc12-fb9e-3d93-8076-6471c574923c | -3.1987 | -53.875301 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74a78f71-f4b0-310a-b44e-1789196b482e | -2.965 | -54.1161 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4e3ad9b-0824-33b6-bf6f-e1e7567f84f5 | -3.1115 | -54.171398 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 298316c0-aa75-34bf-80a4-c0b29b06fe0f | -1.0523 | -53.592899 | 2026-10-08 00:48:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715f060d-742c-34bd-92eb-190d283bf953 | -10.3113 | -46.631802 | 2026-10-08 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b43cd67c-14fc-329d-96a9-49e5e4167083 | -2.9948 | -51.0504 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd5899a-ddcc-300b-923a-ef46c5f057a0 | -8.3802 | -46.290901 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ac87c1-fc87-3431-93e7-9a6f1aec9b39 | -6.2223 | -55.6674 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb64af0f-c48a-314f-befe-80d4de01977f | -6.1026 | -49.4109 | 2026-10-08 00:48:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e573dd-3834-35d0-bb28-a289b96ddbdd | -3.5258 | -59.4753 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e038c5c-48cf-3659-9121-b9989a2cd741 | -3.5202 | -54.6567 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25f79776-4394-3d67-a9b8-c2ff19932181 | -3.2752 | -50.031601 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b36491-7dd9-3ef5-b866-cf04b7a4de84 | -2.8722 | -54.884899 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56dd31aa-7c71-32f3-b663-a9d0fdd971cb | -2.9639 | -54.1562 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 012237fc-cd6a-36c2-bf4e-1538d23df100 | -11.7747 | -46.7864 | 2026-10-08 00:48:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cd1ab71-f790-3f56-914c-5f60ddb7983d | -2.9443 | -54.160599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d5719e4-e95d-3b97-8971-ff6400a359ef | -19.9958 | -49.089199 | 2026-10-08 00:48:00 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d30ea7c-f649-32a7-9936-8dfe40dec55d | -3.3002 | -54.0499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 425e22bb-2ce3-3059-a54c-65c4558b6bc8 | -11.3424 | -51.876202 | 2026-10-08 00:48:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8791a12-af92-3588-9d0f-090f2ecbfe55 | -3.1688 | -53.835201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80c6fb44-65f8-3d57-97a8-0eb5900719e8 | 1.7446 | -55.5951 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86a4006e-baac-31ff-a964-15bf5ed5d905 | -3.2938 | -54.0672 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d16c2d-f3e0-36fb-a3a9-a6c9adf8cd4b | -17.628099 | -46.664299 | 2026-10-08 00:48:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d2223b7-fe06-3b29-9ca5-fafe1d76162f | -3.0833 | -54.274101 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a74fda3f-c28c-39a5-879b-ef1979861fbf | -2.8703 | -54.876801 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbce6b8-b7e9-3855-9790-ae6bcb58e9a3 | -3.103 | -53.772202 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e194725-2a54-38de-a48c-20c789e5e6d2 | -6.1749 | -39.465599 | 2026-10-08 00:48:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c50d6b61-7079-3c37-a38a-1983830bbfb7 | -6.1778 | -53.438 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5550b58e-5987-3353-b3f2-c24fab8fb9af | -1.1452 | -54.222698 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c306c3-e534-3582-8d28-bc07e5e6b3a3 | -3.2891 | -54.092201 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347c3af6-1818-3c27-ace0-ae132ca074e9 | -3.0406 | -54.267399 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9099aeaf-e82c-3ca6-9e9b-c1cb2a764e46 | -5.289 | -60.084702 | 2026-10-08 00:48:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa1aa725-94cb-30aa-8eef-d9c6bab03e92 | -3.2892 | -51.567501 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97cd7637-b578-324a-87fa-fee77a344869 | -11.4597 | -43.390598 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff2f28c7-bb7f-3dbc-b751-7d3bed56e458 | -3.0101 | -54.042801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa97bf4-c3b8-3ddd-af3e-96f3ee4f93c6 | -16.840099 | -41.033401 | 2026-10-08 00:48:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24865195-de6e-3437-9749-f78ccb3a4039 | -3.0192 | -54.127998 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df5e17a1-6d3d-3bdf-8fbf-485a2863dba8 | -17.764299 | -42.4291 | 2026-10-08 00:48:00 | METOP-C | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff23e28d-aa42-3dbc-a7fa-6bc5751b1304 | -5.5227 | -50.0247 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d43e72-4aad-370d-a18b-361823d33d3a | -3.0089 | -53.901798 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee69dd1-e114-38e3-a507-26ed474c02cb | -3.0405 | -53.9496 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d361bb-b24c-30ea-8359-fcbf96f926b6 | -3.0216 | -54.0481 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23ef69e-96c1-3f8c-a4b6-3036d35e7fa5 | -3.2753 | -54.031601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 204b55b1-3da8-3fc1-9a82-2d5ba236857c | -3.4794 | -59.587399 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37effb0f-86b8-3007-84bf-5c92ad0b95ad | -3.0013 | -54.1399 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README29.md)
