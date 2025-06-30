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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d1e2375-18d4-3ab8-9636-f1e07eb4112a | -12.20127 | -49.6312 | 2025-06-30 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f0b8f36-06b5-3c2c-af1a-5a842f287d19 | -11.02766 | -56.26842 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 43f09a42-b253-3ca5-aa5b-e51ee1aca275 | -10.64868 | -44.48973 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7202a640-62d9-37ce-a13b-6fd4e3894b40 | -9.2351 | -58.74697 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7a4e435-8ba9-314c-bb45-925832a1f7f5 | -13.00535 | -53.49073 | 2025-06-30 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38270eef-8707-311f-8fbf-67635888fb81 | -10.80862 | -44.24449 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| deb65016-7706-3cf7-b83d-9e72b2d8896c | -14.02583 | -54.48887 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64250ab1-c2cf-3ff7-beda-89ed99465f98 | -10.87224 | -53.75319 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1d3d40f-366b-320d-a703-cc88595b7003 | -12.62839 | -54.22861 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b79ca1c-af51-3fdd-8ec6-1c7540b927c6 | -9.71804 | -56.18266 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8a77846-3d50-3577-b29e-af8de1a0bb7b | -10.4467 | -47.44507 | 2025-06-30 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d7e1246-c5b2-38e5-8d94-730d62d95ad7 | -10.11003 | -51.56538 | 2025-06-30 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2de7bc-fd01-3c57-9b8a-1a81964465ba | -10.5532 | -52.04038 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baf9c75b-3850-3a52-8bd4-ebccc2a9c6b2 | -14.86888 | -54.81117 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98e8adcc-2669-3a28-9984-d8ae293acf0a | -10.86264 | -53.74311 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05b57507-ae77-313d-9d56-ed01980ca130 | -10.80828 | -55.85965 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ec76030-de6a-3115-bcce-bee03a45c78e | -12.61078 | -57.87049 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f113e4b-1962-35b5-9dd1-8ff445654f13 | -9.23854 | -58.74753 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ccab7a3-62a4-361b-829a-e72429bd984a | -10.35203 | -57.50069 | 2025-06-30 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f351a066-e922-3b77-ae97-b7339a46f040 | -9.24543 | -58.74865 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a50365b-96ad-3015-a912-5b336966bfb5 | -10.3021 | -57.12668 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b153a281-678f-31b8-9bbf-bfdf0a23c7ba | -10.86082 | -53.75582 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0be2223b-4043-3952-9828-f0badba55e37 | -12.07394 | -48.45176 | 2025-06-30 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9be03b24-48c9-3599-bd24-6b94fad06c37 | -12.6218 | -54.22332 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8796012e-0689-3828-b5d0-2292bb23b715 | -10.85903 | -53.74257 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6eb4a7f4-8d9a-3136-a215-f799efe50e1e | -9.70703 | -56.18808 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a90e296-b83b-38ec-912a-4555f29d79c4 | -10.22836 | -54.29335 | 2025-06-30 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7c195df-78b6-36a4-b62d-b3b8208afa59 | -12.61799 | -54.21096 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b64ed30f-187d-3e1d-811c-c8110bb0b96e | -12.50405 | -58.3493 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d921e738-f240-3dc7-a8a2-27552acc30d8 | -10.87343 | -53.7705 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63b99976-10ba-3584-ae66-4064c79f511f | -10.80329 | -44.25092 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f89ce9a9-035a-3137-92cf-ac890bd7dc89 | -10.65603 | -44.4884 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dbdc134a-76e1-3040-9fdc-be296591327a | -9.71473 | -56.18213 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc578cec-7547-3f63-8528-4ddb72722612 | -10.62254 | -51.79477 | 2025-06-30 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34493937-25ef-389f-8c1d-c51ba4ae6a87 | -12.0941 | -54.6738 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71e42373-29cb-34e0-a8ec-8552f903edc7 | -9.24605 | -58.74485 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88aaf678-e8b5-39ac-97ab-467c6e44bc6b | -10.80532 | -44.23386 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e2755a4f-6926-3f55-9a96-abfde86a3fea | -9.70812 | -56.18109 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5133579e-f79d-34ed-9c50-5d76d3a975cf | -9.24419 | -58.75627 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd99579a-a67a-3731-bf49-9e1350639bc4 | -10.64883 | -44.49319 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 573d9f24-0606-3f84-8421-2ab89fdcad73 | -9.70481 | -56.18057 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13c8ded-0648-3d19-8233-86e4210a8aa8 | -12.45819 | -58.57102 | 2025-06-30 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4af8c80-f097-31de-bdd6-150a676d4e2a | -13.08514 | -54.85163 | 2025-06-30 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db58a449-6b40-395d-af71-e944968c1466 | -9.08686 | -59.49091 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abf5245d-4430-3786-b510-08355a6d1a58 | -9.24667 | -58.74105 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4a6c5dc-7e1b-39bb-a5b5-8b120854598f | -13.00831 | -53.4151 | 2025-06-30 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86cdc82e-ca21-34ce-96a5-0deff50800bc | -9.25889 | -57.52613 | 2025-06-30 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 034fc34a-28f7-3dcd-9914-6782968c37f0 | -12.10468 | -54.57786 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 434d782f-5109-3b2b-aaf2-88f869506af3 | -10.86142 | -53.7516 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00f2a86e-883b-33ed-b68e-5a030ade4607 | -11.0836 | -54.77787 | 2025-06-30 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de0ab377-0afa-32ab-be93-4c9661cd1ce2 | -12.61022 | -57.87402 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44966747-4823-3767-9a62-783e2989ba0e | -12.6278 | -54.23278 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 253efe9f-e4cd-388a-9b10-e5c0fc1b4ed6 | -9.7015 | -56.18005 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ee27b48-2c8f-3e22-9906-7769ab80f060 | -12.0181 | -47.77773 | 2025-06-30 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e24f0d86-bab6-3037-9b3e-7212de7c9a38 | -9.2329 | -58.73881 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 589fa03b-34df-31ee-8c22-ec855d5fff5f | -13.08456 | -54.85565 | 2025-06-30 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e924af2-ff4a-39cd-8f8e-1797c5cadd35 | -10.1215 | -57.77479 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a64bb5d0-7d9b-3915-89ae-c266d0ca5e48 | -14.03303 | -54.48993 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13dbc3c0-d18a-35b5-8efc-55840069d137 | -10.86624 | -53.74366 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ffe8bcd-7810-3192-8d65-cb0a7b85892a | -9.11174 | -59.05264 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f112c44c-cbcd-3ae2-a9ba-83dea005cac0 | -12.62957 | -54.22026 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a0b18df-7862-35aa-ab24-50d7e8d12e0b | -10.80495 | -55.85912 | 2025-06-30 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009aec2b-836a-3cf2-a5a3-490b9a0db0f8 | -12.50348 | -58.35288 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 804bd87f-c8f5-3f03-acda-f9320c496f80 | -10.85603 | -53.73777 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 762b5606-f0fa-3fff-855b-df068b1f4565 | -9.24921 | -58.76883 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84a2e1c1-c445-3077-9fd6-c617ac163d2c | -12.60747 | -57.86995 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19a08355-3691-3391-880e-06678c524277 | -9.2539 | -58.76176 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5457503a-1917-3056-808a-0875a68b0e5e | -10.29379 | -57.0503 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e8a3cdd-ac0f-319f-adbf-dc8f7cf311bb | -9.78059 | -47.80692 | 2025-06-30 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c89bb15-66f5-39c9-ac31-f94fe0c23a0d | -10.29818 | -57.04386 | 2025-06-30 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ce2474-472e-325d-a545-b7544a9e8b6b | -10.87643 | -53.77521 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05db9440-d5c5-3e76-ad08-8be45767834f | -10.12698 | -57.77995 | 2025-06-30 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b16a905-3616-37da-8d06-783d49553a0b | -9.23792 | -58.75135 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db522ff-5e52-3392-b063-61e92b4a3e42 | -9.71088 | -56.18511 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 972f8f7f-5965-3027-9b9f-3c4adc59c5de | -10.87282 | -53.77468 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20fcfa22-75c9-3ec2-a768-091148ce5757 | -9.23759 | -58.73176 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2645c8a-852f-3b91-b037-50ddad8b7c43 | -9.23634 | -58.73937 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2c123e8-4bed-3830-b954-304583b0d054 | -9.2517 | -58.75358 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5907d64-615c-3514-b046-9aa5bca0ee46 | -10.86746 | -53.73516 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58d57d77-ffbd-3c30-8c49-e6b7110ccbff | -11.21037 | -55.91845 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fcd434b-5257-3bf7-8e12-7f54038fae59 | -10.05629 | -59.36095 | 2025-06-30 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d01b5952-3a14-3390-a309-69cf72dc44db | -9.23385 | -58.7546 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c3a2f83-921f-3f97-ab05-2d77ee7d60d3 | -12.10226 | -54.66698 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ef82df-6baa-34d8-854b-c85ca152936f | -12.62121 | -54.22749 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f71d1ad-c264-3c75-9977-cec74477adac | -10.85842 | -53.74682 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a3135de-76eb-3178-b3b6-9edcbd5a4b3a | -9.24199 | -58.74808 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c79314cb-0135-3895-8b83-01e41464add6 | -10.21961 | -54.3041 | 2025-06-30 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c8327d-9d29-3840-bc5f-9401056556cf | -12.62456 | -54.21624 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| bf0b74f1-7b42-31c1-b53c-4a4042a4ef20 | -10.86385 | -53.73462 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c05448a8-9b88-3709-9c5c-0fff802f7c14 | -11.20982 | -55.92204 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c963b18-6911-3994-b47c-1b352ff7a56c | -9.88936 | -56.10968 | 2025-06-30 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f7a0d44-b9ef-3ab0-979d-518ed54d60cc | -16.29419 | -52.93027 | 2025-06-30 05:08:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79bdfb7b-9807-3867-89db-34fc6a5e0175 | -14.50891 | -58.64639 | 2025-06-30 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dad707f9-b7d7-3a1b-a6b8-db8d2e9d1f66 | -20.92807 | -49.09641 | 2025-06-30 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24342745-ece1-3167-ae7a-bfdc568e9c99 | -14.50559 | -58.64584 | 2025-06-30 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8bfb206-79e8-35c9-8883-d8dc3296a8cc | -20.93361 | -49.09703 | 2025-06-30 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 747d5b32-bbb7-3eb5-823a-a1f277b4ed04 | -15.38476 | -59.29496 | 2025-06-30 05:08:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baf0b645-9506-3f00-9ae0-f74d5c1b275d | -10.8046 | -44.2553 | 2025-06-30 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b084352f-484b-3b72-b043-200a233667b9 | -12.6319 | -54.2087 | 2025-06-30 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3bc7a0d5-9679-33af-a924-644b42068808 | -10.805 | -44.2319 | 2025-06-30 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |


[Clique aqui para ver as próximas entradas](README14.md)
