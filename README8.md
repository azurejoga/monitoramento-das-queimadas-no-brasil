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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03c80b39-bfc0-3bd4-9835-a5545c3b3c7b | -8.9858 | -65.438202 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0ade758-07e2-38f2-b38f-8509d3ad2af8 | -20.823999 | -57.313301 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb2b75d-1653-3567-8a70-06058b11eceb | -14.9461 | -52.603298 | 2026-08-28 01:36:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65b22abf-970a-3b22-8e0b-12ec99a77659 | -10.5089 | -64.512802 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0ddf08-22ae-39a0-9da5-d41023a35765 | 4.1339 | -61.2612 | 2026-08-28 01:36:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| eb7ee0e1-9177-3e48-9e60-9e378886cf52 | -16.1595 | -58.594398 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c332363-fd88-359c-b639-ad3e70a8846b | -21.0394 | -57.835899 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a706626b-fa33-3854-8ed0-43b3e9bd3c28 | -14.17 | -52.800701 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 644b1bda-261f-3fb5-adb5-40609ed08979 | -8.6009 | -54.793598 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f2a550-2a99-3b34-b56e-9b1ce6bd13b7 | -14.8594 | -52.627701 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48c33ec0-629c-3b61-be8f-89897445895a | -14.1651 | -52.821701 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46ffc5ab-5be4-3b4e-8107-97abb1f8f6ba | -22.089001 | -55.970699 | 2026-08-28 01:36:00 | METOP-C | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b1eba718-ead9-3dd6-a4f8-1baaf2884e1a | -14.1699 | -52.839901 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a16aba0-4810-374b-8567-90742c45a8db | -10.7957 | -54.013901 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9dc622-1a29-3363-9916-b5c16228a5ff | -6.1581 | -57.7771 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be50a222-0c9e-3795-9568-ec7c24e9c60f | -11.7146 | -54.537201 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d72e4df2-f1ab-3d30-88bc-b6e1e89c5cca | -14.8546 | -52.609402 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de5b4697-4781-3d2f-a9a7-ad42f7b366dc | -8.6293 | -66.531303 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd3cf3a5-7cba-3e6e-9d70-1469078c177f | -21.0315 | -57.846298 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef114be7-eae4-3d85-aa9b-1bb084d0645f | -10.757 | -54.024101 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec6195e4-25b0-3706-9640-276621e4c546 | -11.2767 | -53.997398 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47620339-0747-32b5-bbc6-6a404486c1c0 | -8.9939 | -65.428101 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77c86dab-a6ed-3183-a456-a52f11cfa47e | -9.2063 | -65.788696 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3eff2be6-6f83-37f4-9014-4a0731b9800e | -9.6186 | -55.109699 | 2026-08-28 01:36:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6abfed51-ea56-3b34-ae25-0928352810b1 | -6.1679 | -57.774799 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e472f1f7-c69a-3ff4-9452-be91355ddcc2 | -6.1636 | -57.7999 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e31d4bb-d369-3670-a82e-26b82c6bddf3 | -10.3942 | -61.2523 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b77904b-62aa-3594-be19-63fc258b8bf1 | -13.4513 | -54.0103 | 2026-08-28 01:36:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16534a76-5811-3cc5-9611-13e4c6bf1e5f | -3.4575 | -59.514099 | 2026-08-28 01:36:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3290662-79b2-33fc-88fa-2e277eebbd28 | -11.5164 | -58.505901 | 2026-08-28 01:36:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 812fbe77-4a12-3936-9498-24beb2eabf38 | -8.5968 | -54.777 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0357ffb-0d0d-32f8-bc9d-cee0ff179ec6 | -22.0912 | -55.979801 | 2026-08-28 01:36:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 65ab4313-846b-3b54-a72b-39ead31486b0 | -10.3877 | -61.2239 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1014a3b-3aea-3ee2-8830-c200d61128f2 | -5.7664 | -57.561699 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad078f69-c99b-38a8-8797-da4c2ebb46ef | -21.0413 | -57.8438 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6dd52975-af2b-30c1-bac9-89865a4d59f8 | -8.8748 | -66.907501 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62bcc56b-b544-356a-80dc-74f34c20cff8 | -8.5926 | -54.760399 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bf2897f-2ef6-3c4f-a340-e09b0057b79b | -6.5333 | -55.2551 | 2026-08-28 01:36:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746824c1-7848-3c9d-b9ad-aec6167aa237 | -6.1707 | -57.786201 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c70081-e922-3fed-bd1a-da0a417fe16f | -11.238 | -54.007599 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c78a79c4-c9ef-3f5f-bb9b-ba0db71a7cd0 | -6.7641 | -55.690701 | 2026-08-28 01:36:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c46a66ef-2497-368b-b17c-94d1dd515719 | -11.7185 | -54.552601 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70b3acaa-22c3-3081-a2c2-75341abb84ae | -10.7517 | -54.0438 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a51a9144-2fbf-384b-98de-b0c0b09bba91 | -11.2283 | -54.010101 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e05af23b-25f9-33ba-8ab4-4a026137960a | -10.5039 | -64.490196 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd7ba29-f755-38cc-8edc-45cfbbdc138a | -16.1497 | -58.596802 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20d19828-403b-3b9e-8da7-ae2fbc63feab | -9.8493 | -65.019203 | 2026-08-28 01:36:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 633faaf5-6be7-3bbf-a38a-092b1ee02a9a | -8.6051 | -70.205803 | 2026-08-28 01:36:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9137e89c-ad66-3b6a-a799-71a8c771d424 | -9.9594 | -53.930901 | 2026-08-28 01:36:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5c65ad2-e132-3c1f-822d-7b97440688dc | -9.5428 | -66.774399 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f440351-e6bd-3274-b420-be135373445a | -8.9876 | -65.446198 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf925bd3-229d-3095-bd35-abfc11902308 | -10.3926 | -61.245201 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a04b085-cb44-3c4c-a142-c4308549d8ff | -11.7282 | -54.549999 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c05f5a4-64c1-3747-b68b-751b82f6ef6b | -14.1796 | -52.8372 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5407b1-e753-3a62-b341-6cf59c96c331 | -20.826 | -57.321499 | 2026-08-28 01:36:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f3367e97-7f12-39f1-bb34-63387fc3eb00 | -9.9691 | -53.928398 | 2026-08-28 01:36:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd13ac43-84d1-3dbb-af98-2d00224d9b53 | -11.7204 | -54.519299 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19e37ca3-a3fd-3ff3-be56-63d3bf4b7d69 | -10.3909 | -61.238098 | 2026-08-28 01:36:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9018f619-47f7-3876-ba75-b81b1ae69d03 | -10.5072 | -64.505302 | 2026-08-28 01:36:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ddc00d3b-147e-3ba0-b384-7f11a45e76bd | -11.734 | -54.532101 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48211ade-fade-3e42-922a-8c4f065f74d8 | -14.8642 | -52.606701 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f8d8073-defb-3e26-abe5-e211a477d285 | -14.1603 | -52.803398 | 2026-08-28 01:36:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb82e642-7138-3a70-bd93-cc9ec2f3d628 | -6.1512 | -57.790798 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bedfb56-693e-3a1b-bdf3-0bf621eabf49 | -11.267 | -54.0 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7dbf115-bba6-3efa-9f03-429d0dd94a48 | -8.8707 | -66.888702 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc207d2f-a03f-31fe-92e9-2abfad4f7c3f | -11.5185 | -58.514702 | 2026-08-28 01:36:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d696b47-295d-3af7-a354-3573fd201d1d | -12.9163 | -59.882702 | 2026-08-28 01:36:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e7d078a-5e9a-3325-8e2b-166d29e3254d | -11.224 | -53.993099 | 2026-08-28 01:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c761e64-9b75-3440-b7b3-8f16cdbf32a5 | -8.5829 | -54.762901 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3ccb6bd-f9b3-300a-94ef-2ccd3ae1b90f | -28.667299 | -49.893101 | 2026-08-28 01:36:00 | METOP-C | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c60b3585-f273-3f0f-b9e7-93055f553c1d | -11.2757 | -54.033798 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5d654f-0b68-3154-bd97-2ec44e15e955 | -14.8593 | -52.588299 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2e25bec-660c-378c-bf7c-c6bab5899632 | -16.161301 | -58.602299 | 2026-08-28 01:36:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9699936-2262-3016-8237-22ebbeca86db | -6.1609 | -57.788502 | 2026-08-28 01:36:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee2518a-cd77-3fe5-82af-113ae3998a79 | -14.8497 | -52.591 | 2026-08-28 01:36:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf38214e-6bc5-3eaf-a946-995069db043b | -8.9974 | -65.444 | 2026-08-28 01:36:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0464ac68-6cd5-3357-a4ec-c99030ad2e3a | -11.6707 | -50.461899 | 2026-08-28 01:36:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbd9945-668b-3e74-afd8-52834c9ad6af | -7.5152 | -61.387199 | 2026-08-28 01:36:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86d7bf09-a3e3-3524-82d2-8396a1c01ada | -11.7301 | -54.516701 | 2026-08-28 01:36:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c50dc6d0-9fe9-33fb-83c4-217b478ec536 | -8.5871 | -54.779499 | 2026-08-28 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4f70a9a-182c-37d1-abe0-16a60b8c7bc0 | -14.1649 | -52.8058 | 2026-08-28 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 2c77b284-feba-3e9f-8a10-efaedc612eb4 | -21.5304 | -48.3869 | 2026-08-28 01:40:00 | GOES-19 | DOBRADA | SÃO PAULO | Brasil | 3514007 | 35 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a20791f8-db32-3541-aacc-04b2177d845f | -10.3894 | -61.2502 | 2026-08-28 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 222.1 |
| fd35f83e-e06a-3486-9402-2870e35976e7 | -7.2659 | -45.8668 | 2026-08-28 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 381.9 |
| bb63b430-fe51-394b-b71b-f525d57d3677 | -7.2657 | -45.8893 | 2026-08-28 01:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| cf6f395f-e072-38cd-9c5f-94c4456e4e31 | -14.1841 | -52.8034 | 2026-08-28 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 336509f6-2c33-3213-95ca-608d1519f463 | -9.621 | -55.1266 | 2026-08-28 01:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 62cd4d31-8512-3c64-8c42-c597ef3b745c | -10.7596 | -54.0384 | 2026-08-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 039d702e-6750-30bc-b672-e498cfaa18bf | -7.2471 | -45.8685 | 2026-08-28 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 418.9 |
| 624a3f63-2964-3be4-8318-f7ee56e4a88b | -11.2882 | -54.0111 | 2026-08-28 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 237.8 |
| 9960045b-d965-3fae-8300-40da7272c604 | -7.2661 | -45.8443 | 2026-08-28 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 1d4de1f9-96ff-354e-980a-705cd4de1952 | -8.5969 | -54.7755 | 2026-08-28 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 5ab4c6dc-3b2e-380b-8027-910d4695d271 | -11.5659 | -45.5338 | 2026-08-28 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 8e98776f-f684-3aba-a0ac-5f70ba354693 | -7.2469 | -45.891 | 2026-08-28 01:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| d6536d3a-8479-38bd-94ea-e7a0ab2f477d | -8.6156 | -54.7743 | 2026-08-28 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6a976457-2dd8-3517-926c-a56ad23741d5 | -6.1472 | -57.7995 | 2026-08-28 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ca30aced-d94a-3f12-b71e-a3627c7ae3d0 | -10.4082 | -61.23 | 2026-08-28 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b0a3769e-ffaa-3175-a9ed-6e255c429391 | -8.6154 | -54.7945 | 2026-08-28 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 64cbe156-85ba-31c0-98c4-1aa886a5bbc6 | -10.4081 | -61.2492 | 2026-08-28 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d38ae011-947c-3a57-ad68-cde970ba257d | -21.5518 | -48.3585 | 2026-08-28 01:40:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |


[Clique aqui para ver as próximas entradas](README9.md)
