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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce56a1a5-d419-3adc-85ce-a3b7c30f8c42 | -4.17787 | -51.23779 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5b161e-6d52-3bbf-95c6-dafbe8ba07db | -3.14888 | -53.83435 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0ea88c-776e-3c9e-b084-422d5455064f | -3.18186 | -53.25286 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 631bb128-4bbc-3cc2-88ca-e012e96572a9 | -2.46059 | -53.96416 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d0e550c-8d1f-3074-a85e-0de4fb02becc | -2.88935 | -53.98682 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6dffdf3b-9e96-323a-8de8-0f24d769d9aa | -1.39337 | -51.59726 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce5eb610-35e3-3e6c-8f34-f472e07f26ce | -2.87088 | -54.03012 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11da33aa-1ba4-3b32-a1fd-2ad0b93ccba3 | -3.97109 | -49.91027 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6f2459f-4d4b-379b-a7b1-a561e1f698db | -3.95016 | -49.95676 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1795ba9d-d711-3324-852f-22adc5b9494d | -2.76583 | -51.6857 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fbe0e08-2f8d-3675-894c-e6dab176e1ee | -2.8351 | -54.10836 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c04e78c6-4f1f-3069-ab45-4038bf0e5fc4 | -3.47354 | -50.53386 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c360b7f-2280-3637-9818-141e8c82cb92 | -1.40918 | -46.59566 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fdaaea3-86b1-3660-8fa1-9059214f0245 | -1.64342 | -52.74794 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4641e5-fa99-3388-a561-1ac1d4af46db | -3.75101 | -49.93308 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c862c822-48e8-3f65-9ae7-c0e1661acb60 | -1.00359 | -51.72378 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a748c7f-ebce-3e86-a7fb-b97f37e220fb | -1.32293 | -55.66979 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5cb720a-0079-3cd3-99b0-6eb10b3dca83 | -3.08672 | -51.07391 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c311cac-a82b-340e-9da6-1493e9de9adf | -4.05579 | -46.82263 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| daca1dff-e6e2-3a16-80b3-73b72191551a | -2.27926 | -50.57282 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d118d861-dbf7-311d-8fa6-2c8443bb0fea | -2.88577 | -54.00933 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55aa1d2d-d18b-3858-bae0-7e885435b1a3 | -3.31377 | -50.02414 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57162a24-9aec-303b-b5ef-32720329c10a | -5.79748 | -47.07567 | 2024-12-01 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae7931a-abc0-3e08-9ab0-51db6edd0cd9 | -1.6282 | -47.32417 | 2024-12-01 04:44:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafc8df4-b35e-37ab-975f-97784f7970bb | -3.17248 | -46.31533 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad8c9f94-f137-38d1-ba8c-66e6281a297e | -1.95033 | -53.34732 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c755acdf-8c7c-35ba-8ce9-55d695c3b82c | -3.80505 | -51.00767 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21d49ed8-651d-3da5-8dee-8c59ff8f47b0 | -4.55577 | -45.71596 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c0137774-036c-35d4-bc30-ece5dde4f23e | -3.58149 | -54.52453 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40da0dfe-2fa1-3872-97dc-b29c261c89d1 | -1.30292 | -55.74072 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94918f0-0c4a-3359-a37f-fc999343cdb9 | -3.33826 | -53.37237 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53c19b1e-f525-3337-ad55-1719fc8c5338 | -2.65226 | -51.87347 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4981651c-c246-30d9-9fd6-a089f350059a | -3.66716 | -52.29818 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c259d591-2d83-3f83-9ee1-d16bfea999f2 | -1.39395 | -51.5936 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6147599c-d8b2-31ba-b73c-2d561367a4c1 | -1.43186 | -55.19457 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75d5a154-9f8a-35e6-8fc5-5ef8855104a4 | -3.97304 | -47.2449 | 2024-12-01 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c15fa74-b2d4-3d33-9b50-7fb7e9602f77 | -2.58144 | -51.72425 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd422f45-8a4e-318a-80da-800a57fc006f | -2.54793 | -45.61283 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c058940d-a35d-3a39-bc18-57f3ddba5ffa | -3.65615 | -50.23342 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a28164c5-2bcd-3814-a9ec-000151163730 | -1.03249 | -53.54868 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fea1021-1bb3-347f-84f8-67d31c98eed9 | -2.59845 | -46.56706 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b36a5b80-e193-3369-88a2-57e305b1730f | -3.1987 | -53.42526 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74f017d3-8382-3b20-998d-13f5ca54d5d5 | -2.46184 | -46.57914 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdbcb13e-062c-32e1-871b-431aa1eba84c | -2.89186 | -54.16301 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5e446dc-5113-345f-9564-02afb732ae10 | -1.28069 | -51.73481 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b1650cf-bdec-37f5-be4d-7e27626b1603 | -3.66776 | -52.29445 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c0d9186-c12d-31d0-b96c-0656741cd65c | -1.56237 | -53.51864 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6ae0492-4a65-3dc3-b2e9-18b10db05198 | -3.59646 | -49.99073 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 588b7d29-4974-31ac-9498-c44f497d046b | -1.06918 | -53.38649 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 357515b1-b546-3232-89ab-b39512c7e400 | -2.12054 | -46.57801 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcf20fc1-ae68-3568-903d-d4e370811657 | -3.10915 | -54.03679 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd08a5a1-07fa-3b0b-9ffb-80330cdedc1e | -3.49344 | -53.80253 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b32ec455-c685-3502-be11-93a72c0e2474 | -2.46901 | -53.69516 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b6fe1b3-f2ff-322e-8a86-276392ef29fd | -3.50684 | -53.82584 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1a873c-414f-3a25-93ec-94f03de56064 | -3.40957 | -50.66132 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4efa3754-0eea-364f-b076-42dda926d93c | -3.31014 | -53.86887 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f46a8071-5b13-3d51-84db-2447b82cdf4b | -2.92546 | -54.26831 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6b5729d-bb8d-3a92-9341-1eff442a63ce | -1.27062 | -51.82091 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8ad83b3-5dd1-3ca0-b9ec-1440012fabab | -2.47795 | -46.5727 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1450ef0-75e9-3e27-9500-2dddf2286aab | -2.95554 | -53.89118 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e40add71-bc82-301d-8ac9-07cff9a240e4 | -2.39443 | -50.48801 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 707479e5-643b-31b0-aa0e-d91a242f47e3 | -2.95345 | -53.70283 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b4cf97a-cdc1-3de3-8ac8-daedc96c4771 | -3.62142 | -42.74119 | 2024-12-01 04:44:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c651107a-07d8-37dc-9c53-3f4182d8c735 | -1.48479 | -55.38327 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40bac29f-4f07-3908-8ddd-0d8f15f5294d | -2.59297 | -53.981 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c478500d-40e7-3afd-8943-c21be745be04 | -1.26402 | -51.75121 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 077243e1-8b90-3bc3-8e0a-08bd49da8d3b | -3.01427 | -51.79151 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2e8963e-5b01-3505-9033-6ca1082b30a8 | -1.26746 | -51.75175 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8093a5eb-f0b6-395d-8a5d-d778f088195b | -1.66045 | -53.22335 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b646ea33-3721-36e4-8634-a4be83dd3336 | -3.1419 | -45.98856 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52fb72f4-189a-38b9-8a66-b90b2a16c3b7 | 0.89484 | -59.54475 | 2024-12-01 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ac0e99-aee9-3cff-8669-c5aa08c0265d | -1.9063 | -52.87033 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fefcf67-b34e-30ff-9d7f-ce62320ddb1e | -3.47022 | -50.53334 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d3be31-ed0a-3071-b072-8bb992d5d32d | -3.29727 | -53.83095 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a363aa23-11f0-3b11-9bc7-ce1b87df303e | -1.56676 | -53.51498 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39943268-0355-3621-b5c0-83c0600c99d7 | -4.90076 | -47.14515 | 2024-12-01 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 953fdff0-df16-3107-b3cf-dbfb5f86a8e4 | -1.3272 | -55.67045 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80f37f23-4b9d-3526-b4a8-7569f1bb6b69 | -2.88881 | -47.4452 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f682bc5-27b0-3f32-b551-33dfdf1efc8c | -3.75524 | -50.05777 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e18b7403-e214-318f-972d-3ae4c7f6903e | -2.37747 | -50.40388 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91221a48-b73f-3863-91fd-e72bd11e4399 | -3.26277 | -53.63275 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f22308c7-1330-3754-8585-92032c238f81 | -3.63825 | -54.44209 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 94c43a90-0a7c-3841-a527-2fc119db642a | -1.93251 | -53.96198 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 406aa5dd-d428-3af8-ab3f-50f927535596 | -2.25536 | -51.09136 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54a5c652-609a-35e2-af1f-24ed5565f152 | -3.24168 | -50.54666 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d3644ea-551c-3a50-b3bb-a9c9682be097 | -3.30643 | -53.86828 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5e67a4f3-9170-38d4-9b56-ef84381cb57f | -3.3585 | -50.51541 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52a0df05-839f-3f9a-83a9-8b19b1b00ed5 | -1.45765 | -54.86894 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65a3faf5-c72f-3f7e-8ea5-9e8f4ee9eeac | -2.82801 | -54.0326 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631309f9-bd4a-3c88-9411-685312d04c22 | -2.24366 | -45.43295 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7e2eb6-b773-3611-805f-c492c78152db | -3.24226 | -53.9285 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a0d381e-ee8e-352f-bfc8-e03853982af4 | -3.74805 | -50.06019 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c49a1f0-79fc-35cd-b229-ab8dfe988eb8 | -1.3243 | -51.68102 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b0784fd-8ffc-3f62-ab7e-b28c495467da | -3.28252 | -50.43636 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c80ce67-5ef8-338f-b2d1-c95312e7352e | -2.44988 | -53.62536 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6a34485-a117-3b07-9265-5aa9e02745c2 | -4.18555 | -50.67728 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1186c2f-9888-36b9-8e39-159ad018b940 | -2.75234 | -51.66137 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b9ce5da-8a42-3d26-aba6-3a3d16185b0b | -1.56129 | -46.76733 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2ebe784-e8f2-30b8-bdf7-0247d23b5b4d | -3.10163 | -53.75001 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a2f736e-2385-3da1-aea5-194f68660134 | -3.48686 | -53.80915 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README67.md)
