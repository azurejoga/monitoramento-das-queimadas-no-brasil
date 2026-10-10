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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b8e0588-a399-37c6-bcc7-a269c9df261f | -4.58694 | -55.72265 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1dd3c88-186e-3f01-9967-c1e0e1a57bd2 | -5.71494 | -53.47944 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee82a25e-dfc0-34aa-af64-4a6803e594e8 | -6.41027 | -43.74619 | 2026-10-10 05:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8096f925-79ff-35d0-bf84-c7193e404aab | -4.68359 | -47.43609 | 2026-10-10 05:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 926342f1-0116-30ec-ad64-71ed951eb07a | -8.24884 | -46.43255 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0110c60a-3bf8-37b8-b904-6b7f0e0ab323 | 0.79137 | -59.20575 | 2026-10-10 05:04:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535b52f1-1240-3bc2-9dbc-51445f44e1aa | -3.14857 | -59.02977 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baa81767-a8c5-344c-ae4b-15efe89f51b8 | -2.83496 | -54.13903 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e952a2-89da-3553-9306-5ea08bfb1419 | -3.27685 | -50.39012 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3e88549-c962-3d66-ac62-0cfa5757602f | -3.07596 | -54.29032 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89674f11-4f6f-39be-929d-0b46c8f27d62 | -3.30822 | -54.00513 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9ef37325-b7c0-362d-ac73-5a3cbd159d5c | -4.12588 | -50.83076 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc010275-7aa9-3946-84cc-ccd2cf0c7f86 | -0.97403 | -52.45929 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb08a1f5-fd06-3429-9241-aefa9dc09fcf | -5.79607 | -53.80573 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e23eb06-2c84-3b3f-884b-d1a0f09f3ff6 | -3.26371 | -54.26346 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f131ff7b-09f0-304a-80b1-2fc36464fc10 | -3.30224 | -54.08541 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af346677-fec3-36c4-9837-710997675ed0 | -3.24481 | -54.6604 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e45a7a08-89b4-3a3a-a7b2-afa27c4c37e9 | -2.73878 | -54.10227 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 553d0972-5804-3304-8598-886e526ab98d | -5.78668 | -53.80072 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38cbee78-eac0-3642-89b1-6eff07ee0428 | -3.2287 | -49.43559 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39416922-a0a6-3b46-a805-0695cd6abd6f | -1.33086 | -55.44745 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c615392-3e47-33dc-b771-e6e37c856f1a | -7.20497 | -55.14057 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a185f4e-11f8-3c86-99f5-5f1f9f70ece4 | -3.54705 | -56.96506 | 2026-10-10 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eb06ade-a4bf-393c-823e-c9ef147375e4 | -4.54897 | -54.9812 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc725a5c-8002-314d-9b4b-56037a89c7e2 | -3.25837 | -54.01806 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0b82aef-1a7a-37d3-bf3b-a9856853db88 | -2.99677 | -57.74118 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee5f8e52-8dbd-3be2-a394-971c9490caa5 | -4.59093 | -55.71955 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22a57acb-c8db-31fd-937e-5f2e73758754 | -2.5641 | -56.18087 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35b25659-8635-38e9-b018-e79a0c260607 | -3.79062 | -50.80017 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6006cdb2-1b33-352d-a13c-f0762706af91 | -3.89865 | -55.88077 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1a15c30-9ab7-3a39-8fb7-c2630ee4f160 | -2.88055 | -56.66549 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7d97af-7f03-364f-b574-cad45c29eefe | -3.22506 | -54.29255 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc222e01-5441-396e-9a51-c5c08c882e70 | -4.11708 | -50.98355 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1aba80d-81e1-3513-b071-86e1db1f78e5 | -4.12824 | -54.25497 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcc75725-782f-3765-9717-731b2dd49347 | -7.17432 | -52.61656 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24ffe9c6-1d2e-3efe-9692-0a3a52d06a4e | -5.88221 | -43.40966 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddd6206-4eb1-3725-9a42-f2b2fd5e5567 | -3.27488 | -53.99947 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51036a46-be3d-3801-bf21-4b0831672293 | -2.42124 | -58.00089 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 529214c6-825a-3025-b967-14830d6fb309 | -6.45925 | -55.48878 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68d97f8-a4e9-3382-8c84-5903ecf223dd | -1.95581 | -54.389 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c81e8f96-eef4-3d58-884a-510ef798c49e | -3.43172 | -59.36167 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ad6e31-2693-353a-9b38-94bf7872dc5d | -3.84218 | -55.79606 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 544a1e69-965c-378c-81eb-02ce5b0792c8 | -3.11731 | -54.17974 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7295e8ce-45e2-3b42-bd7c-53f73a909fc4 | -3.21843 | -54.29152 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e69a8c78-1f9f-3d00-bb4f-6cdb729a684a | -6.5341 | -54.91523 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e50b7d96-c13c-3bd5-ae46-08e5af78093e | -7.10702 | -52.66698 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9684104-c641-32e1-8237-ed97ee9de69b | -1.95526 | -54.39251 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a72c124e-cd25-3f48-87c2-c3df50d70879 | -6.45541 | -55.47001 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3f9b311-003c-3e65-831c-8cf62b8ab63b | -3.90388 | -58.95255 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9538c1bf-3558-3241-95b5-7d5d5965b7ad | -3.02383 | -54.19007 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6063756-cf7d-35cd-8138-96414ca5fc9f | -2.94756 | -54.11431 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a22d657-b4d5-385a-81fa-d6b888e646d6 | -3.12227 | -54.16989 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2ea5f3a-1f1b-3ba4-80b8-16f051eeae0c | -5.78613 | -53.80417 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bee73dc6-2221-35fe-b21f-f6d4c2aaf569 | -2.73604 | -54.14082 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5eded3d-e881-3939-b63e-9b909d429919 | -3.95652 | -55.34807 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d84b1680-2641-3ea9-bec4-4ea96df926ff | -6.01503 | -52.75235 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42381738-3f04-32d8-b896-1bfcd603ba88 | -3.25595 | -54.18429 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b36bb9d-7c3f-339b-845c-5e02990a9e5b | -3.04275 | -54.15737 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 873112f2-b2d4-3fb6-a352-2dc89e5470ae | -2.56749 | -57.4203 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 251eb197-e232-3527-911d-7abe4102448c | -7.23695 | -44.18736 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0e78b60-9521-3968-bd0a-de9edd116dcb | -2.94703 | -54.18156 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae0a0a4b-58dc-3d3c-91c9-9571c360f842 | -2.23082 | -58.11143 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01f54a1-5639-34bc-bdfc-42d19058623b | -3.05507 | -54.03573 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745b434b-cd7a-36cc-a46a-1a52d1027603 | -3.90328 | -58.95613 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c177168a-0bcc-341a-a0ce-68c4a5358cc5 | -3.25877 | -50.43453 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd29259d-b859-3ac2-9dd4-f3b8ba4c2fc4 | -2.94774 | -51.97654 | 2026-10-10 05:04:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7154001-4a29-3c91-8092-6d288a9f7f4c | -6.72528 | -50.9421 | 2026-10-10 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954aac5b-564a-3430-9d0c-dd7d1571154b | -3.22413 | -49.43973 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d75c507-d59d-3000-a815-abe282ce6e83 | -3.74764 | -59.44426 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be82fdd3-9b09-338d-86aa-8749064b0bd5 | -3.2656 | -54.05805 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b65d6723-cabb-3a6e-baec-f04520d43710 | -7.03348 | -47.67282 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50b708d7-f1a1-303c-b53b-dcd9357bd105 | -3.11674 | -54.16195 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfad0c4e-8f8d-38bd-8f8b-f2b8a68d089f | -5.9269 | -51.82279 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d774e109-6bc8-3d92-83aa-81454773163a | -5.742 | -45.13182 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c50f9e9e-1135-3d07-8075-5297fd774b0e | -3.54522 | -55.52601 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d635325-97a9-3461-a906-0a60ac04273b | -3.2765 | -54.69782 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e0683ea-3100-3fa8-a8dd-da57a67cf1fb | -7.51927 | -45.30699 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 43887524-491f-34c7-a315-6a0190af95e5 | -4.51916 | -61.1334 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa8e6201-91b3-3bd2-89b0-6c36f6ec6baf | -3.85022 | -55.78973 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d316a70f-fa31-3129-909b-8ba564394b9a | -6.46039 | -55.4817 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1308e61e-79c2-3d2d-995b-de4cd01961a7 | -3.60299 | -54.58745 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb1dfa1f-d7e4-3d58-8c79-c1ad3d7832c7 | -3.58967 | -54.71446 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97d4188f-b938-35a8-9f89-071536ef7aa0 | -2.86539 | -54.20411 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3be996f-8655-38ac-8930-e49bdafb3b23 | -5.51989 | -50.02862 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f2fe4a-2de3-355c-ac0a-99dd376c0381 | -5.06594 | -60.2537 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b0773b-2a46-3132-9e9c-011e116b74d9 | -3.16914 | -58.62228 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 52892a8b-ad19-3004-a4c4-9aaf6fa762ab | -6.02808 | -55.35799 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ad6274b-1918-37bd-99fe-b4cab5e62672 | -3.90734 | -58.95679 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83858a9d-3263-31ca-afea-004308734637 | -2.84435 | -54.1228 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c34d0720-235d-34f8-89fc-ec47ee967208 | -6.09268 | -55.69666 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dcfa755-66b6-33c3-9d63-b5e5b41b25ac | -4.99003 | -56.94857 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ebd6ccb-1fe9-36ac-8fde-36498866af7a | -2.75039 | -54.11473 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 518de09d-6423-39ae-af77-68af9b65a669 | -3.57417 | -54.38327 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7975cb67-24cd-33fa-b2c8-a6da8509c849 | -1.25417 | -55.79023 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed01052c-50ea-3ea4-befe-0aa372843fc3 | -5.9911 | -55.38124 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7629b5d-2181-36af-9e3c-6d0c7b51a1c8 | -2.86484 | -54.20759 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb93aacc-5401-3045-8746-fb140038f858 | -3.49073 | -59.63406 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 066e103b-cabd-3867-b8a2-7f3498e15de7 | -6.31355 | -59.94546 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebfb210e-0f5a-3717-b433-c2e0bb91688d | -3.0433 | -54.15391 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06856d17-ada0-38d6-960e-6883b16c0ec5 | -7.23156 | -44.18262 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README105.md)
