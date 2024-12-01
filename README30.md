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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67ec28d8-3d9e-37b1-aeca-2b91b3f88c73 | -2.95255 | -51.78829 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad9cbc05-f237-3d1b-ac15-767a8d36e50b | -3.18436 | -45.35241 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3200d26c-0d06-32f1-a1ae-cd34a2cdd321 | -3.22973 | -51.50321 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 37ee7fda-d416-3864-9aa5-bb7874027f0e | -1.27253 | -54.55652 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bd760bd-829f-3e39-85db-d7050ef04381 | -3.03672 | -51.78381 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9603fbc-56d8-3791-a08f-4729a49dd381 | -3.81993 | -46.59327 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0bba1b8-1762-3f40-8359-fcd19538e094 | -4.50155 | -45.73972 | 2024-12-01 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ec3e91-0610-36c4-b365-7c874cda9cf1 | -3.09071 | -50.35335 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6a30d51-8582-3731-822b-7403a3c1025d | -2.2876 | -45.60362 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| fa841ab8-a47d-30ae-98f1-dd6378a66363 | -1.72159 | -45.76344 | 2024-12-01 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8637cc4d-ed1d-371f-9bc5-7aeaabfd55bf | -3.77884 | -46.69615 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab9911e3-26ed-30e9-aa58-5c2fc3e16dc9 | -3.6809 | -44.70274 | 2024-12-01 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3b84691-5dae-3b9b-b881-a13134163e7f | -1.27665 | -54.55315 | 2024-12-01 04:21:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0faa9142-11cf-37d9-8a2a-66817e653466 | -1.4997 | -54.95425 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81141847-3c80-3dbc-bd1c-bd008fe6244c | -2.96334 | -53.72765 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419bb984-60cd-3d5e-8610-0beeba20be26 | -1.69837 | -52.63687 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fae73db-b1c8-32b5-9336-94e5e5c44001 | 1.67546 | -50.6636 | 2024-12-01 04:21:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8fda5c0-59de-3bc3-80da-9e1ba9eeea2d | -1.97693 | -46.46402 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f5dab25-2b9d-300d-a799-4f245e4a5edc | -3.13705 | -45.9811 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cad21cbe-cab6-33e8-abee-34e1fd1f22dc | -2.99375 | -45.57333 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31dc4b4d-8dd9-30fc-9a99-d41751aa6f16 | 0.93757 | -50.74333 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aaf3f86b-76c4-31b7-9d33-27365dbaa936 | -3.93816 | -46.70478 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 720039cd-68de-3919-94fa-50016699fbe6 | -1.71653 | -52.62363 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e9a8b55-0280-3f8d-8b21-482d023dcded | -2.59005 | -46.94305 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc05e133-3db6-3cac-99dd-32c7ad561160 | -2.6528 | -51.87285 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 79ac0167-1c23-3d28-b4d3-38e99931d6fa | -1.73573 | -46.66153 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d7d0a9c-9841-3510-b883-b6fd6bf7273e | -3.06787 | -53.81421 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0788705-e205-3ac2-bc18-0ee62a50d845 | -4.02458 | -46.67531 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 244a1506-da4e-3224-9700-9d7aee87c247 | -3.28504 | -50.16479 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ac33ee3-da53-337f-a457-c46b90fe3b1e | -3.65006 | -50.217 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32ded8d7-af45-3717-b3d6-b5fb23671ca1 | -1.71602 | -52.62676 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ef3f55f-a9ce-30d3-8fa5-370797c4d6f0 | -3.14613 | -49.40876 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 441a18ac-cb93-311f-a89e-738bc7c94f29 | -3.27274 | -50.21269 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd363666-51d4-3470-b376-17273e13d0b2 | -2.12167 | -45.96471 | 2024-12-01 04:21:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b6b14e9-d3f7-3769-90ad-51bf21a6ff73 | -3.26372 | -46.44654 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 812d34b5-f36e-34c3-a282-b9f804c1b18c | -3.10864 | -53.80901 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9aa703b3-0cbe-3e11-b37a-518fc74bfc00 | -1.44795 | -47.11297 | 2024-12-01 04:21:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e96e68b2-c6db-32f4-bcfa-57bfb52abba9 | -1.0489 | -51.75988 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f8ddde2-8866-385d-bf90-59060c966098 | -2.12113 | -46.56457 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0709905e-cb6d-3655-affd-48a0126b2b02 | -1.23223 | -51.80435 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f96a832-87bb-3b65-9a63-0cfb2fdd0e1e | -4.68119 | -44.06989 | 2024-12-01 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d9b013-75d2-3866-bdee-28fbda47d051 | -2.58717 | -53.98272 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78ad54ab-c856-3781-a938-4ef33ce66a7f | -2.62546 | -54.22397 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56ed667d-b2f4-39ea-b63e-86d031859c3d | -4.00574 | -44.75732 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c22ead-0a49-359f-824e-6b2e34ba675e | -3.30213 | -50.27589 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1854c6b6-e28b-32b1-bd5d-1c0a1feba6a4 | -4.53062 | -45.74434 | 2024-12-01 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a72c28-0fc4-36de-8181-cae81f45ff04 | -1.51712 | -45.90305 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a8678a3-2507-38a2-8449-8fcec6b845b2 | -3.98063 | -46.7509 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3f3c100-6a1e-3fbf-860d-83a8102a72a3 | -2.50517 | -46.2028 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3fd90dc-a4b3-3462-aedc-7aba21f21121 | -1.56235 | -46.77129 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ebb3f94-d897-3464-886f-836898e329f3 | -3.0882 | -51.06989 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 882a3c79-4ee8-3d3b-8eb0-b57501adaf18 | -2.71333 | -46.1316 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3648385e-3ef3-308a-b394-6db2f26c6d19 | -4.49778 | -43.60724 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c418eb23-e859-3369-829d-b238aade1367 | 1.18331 | -50.87416 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 566ca065-80b9-3155-886f-7777e4ee8c70 | -1.92115 | -52.6588 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 242d4ac8-d8ff-3d38-846e-bdbe6bd183e2 | -2.80583 | -53.04775 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0e095b5-88be-3171-b6dc-a50bdd5ef1f6 | -1.50069 | -54.95475 | 2024-12-01 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ae15404-6525-304d-a7fd-54e159b78e09 | -1.56558 | -53.83536 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 005d1875-8e0f-361a-99e5-5ff0bddd704b | -2.63354 | -46.87589 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5766129-6960-3d6f-9e31-f68297e08635 | -2.99263 | -45.58049 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b561a7-f9f9-362c-aba3-daaa3057eab3 | -3.8563 | -46.53691 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 041d9a25-edb0-3edd-ba8e-b33a2b4e0339 | -1.70707 | -52.44033 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc3206bc-9dd6-35c4-a8df-94169995066b | -2.97234 | -48.03813 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e42725-074e-3615-8bde-6a311459c759 | -4.5475 | -43.30882 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5735db2b-1cf8-385f-9c31-f26f720260fe | -3.85888 | -47.0602 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282c51b5-4504-3a39-9184-58ef3f9fddf1 | -1.89508 | -53.01852 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43262699-0dd7-3947-868f-0750fd5f0144 | -3.32948 | -50.18855 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b6df31f-cbdd-3125-a6e7-ce1bc7683db0 | -4.05693 | -46.82109 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a683cd7d-14a0-3713-8baa-24799695e2b4 | -2.47473 | -54.01313 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956ccfa5-2d2b-377d-a322-98a2668da8c4 | -2.83887 | -46.86222 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0999c4e3-7f7a-361b-8f78-4e8404bb555c | -3.14952 | -53.83498 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bce4cc51-6c6d-37a8-b272-b4a582fb78f5 | -3.82684 | -46.59443 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 991f5054-db81-338d-b69a-9ed9a5156822 | -2.11309 | -46.54731 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5455a35-3e8f-3580-aad9-09e07e2aae51 | -2.78478 | -49.82838 | 2024-12-01 04:21:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1081aebb-a247-3b2f-968c-73cc9a9ee6ed | -4.05631 | -46.82496 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0221cb2f-baf9-379a-9102-7d6696ab0e02 | -3.89119 | -45.01216 | 2024-12-01 04:21:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bebd7b2b-623c-39e1-9a68-272cf6ce1ff6 | -2.97045 | -53.44992 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8557cf-4485-3796-92c9-a883f6a373a5 | 1.25353 | -50.69362 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55ab4e5d-2191-3e13-9595-f7c2eacf3796 | -2.98927 | -45.57997 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| bde1b612-cb45-396c-b872-f94b99a6b432 | -2.63113 | -54.22505 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcb12822-f3a1-35f5-90b1-e4f43b251c48 | -2.65419 | -51.87518 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| da683dcb-3b06-3e2f-99a5-333addfb9eb1 | -2.78414 | -49.83226 | 2024-12-01 04:21:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e76bdc5-cc13-31ab-8915-69a329e9368f | -0.76413 | -52.41643 | 2024-12-01 04:21:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ae6c173-53cd-3616-b958-832553b918a2 | -1.89562 | -53.0152 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c62adc0-9fc1-337e-9078-f6c0c31eada6 | -1.28352 | -51.65536 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1369208-f526-3594-8269-6b6333900964 | -1.50419 | -47.47327 | 2024-12-01 04:21:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53716d58-f4ce-384f-b468-40298a6b1deb | -3.30805 | -51.1065 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f30f06d-f25c-3c35-867f-7bb0c958748f | -2.6785 | -46.10717 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22db3bde-8847-3f39-a71e-f71d5a3fbfc3 | -1.11089 | -52.30443 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b8aea0-06ce-35ab-9dc7-6393da4e49bc | -1.09228 | -53.64148 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b76b24c-904f-3a6f-99e3-0fc2b5fe9372 | -2.8793 | -50.73697 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0eefd00-b129-38d9-9247-2e59ad3c40ba | -4.55529 | -43.30277 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 209e2ad2-433d-366b-88b8-12980eff07f4 | -3.99563 | -46.50066 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5475cb56-4e0e-3592-a474-6646528e56b4 | -2.92898 | -51.44715 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fc0948ce-812b-358b-ac6c-1af1a8515026 | -3.1148 | -53.80602 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f12436af-dd63-31bd-be93-e5d6c36cbd1a | -3.32587 | -50.18373 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4943a01-5aa0-3e01-b976-dac316055cb3 | -2.46133 | -46.56799 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b126d7f5-e7b1-30fc-9cf0-2f63dfe7db8e | -2.09306 | -46.28031 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d6e7b62-564f-3d21-b59a-74d0ad4f75fa | -1.57831 | -53.86457 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4ddbcad-50bb-3023-a3b0-dcea387000a7 | -3.06907 | -53.80693 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README31.md)
