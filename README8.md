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
| b3d38346-5078-31e0-b950-88a28e3b2b71 | -14.7655 | -52.6446 | 2024-12-13 02:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8d0fe516-7489-32f5-a866-20763f064f0a | -5.211 | -43.2833 | 2024-12-13 02:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 0cfc77d0-a78e-3eb2-88ed-006b4d0d1841 | -11.1959 | -53.8348 | 2024-12-13 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 826b7812-f334-36bc-9cfb-15c61f2d20bf | -3.2685 | -46.9362 | 2024-12-13 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b04edf11-7558-3dea-a27f-2559cf4d2928 | -6.9349 | -43.4934 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ec11b264-7dc1-3b2e-aace-95e18aeae077 | -6.9161 | -43.4952 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f361ee88-b6bf-3d2b-95f9-2a24e8d9d64a | -11.2151 | -53.8125 | 2024-12-13 02:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 71c1b27e-92ce-3403-a0ed-a255691a7676 | -6.9344 | -43.5401 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 240.4 |
| 87f6d070-a290-34e7-84a7-44e9fecd8713 | -1.62 | -46.6747 | 2024-12-13 02:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 32ebfbd3-544d-3c14-b792-f70836cd02b3 | -2.5108 | -51.8023 | 2024-12-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 67e096a8-93e5-3d1e-9a20-61b28ee13829 | -13.0644 | -52.0326 | 2024-12-13 02:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| db3fab5a-bb9a-3489-9d25-be33a0fde4b8 | -6.9158 | -43.5185 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 368.5 |
| 1e54ce9d-bfce-3459-b9c8-4ac28efcdb63 | -6.9156 | -43.5418 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 04e08e8b-9144-3a05-816c-6c6c16ef0607 | -2.4923 | -51.8027 | 2024-12-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 016a26cb-77a4-38f5-a08c-2279cc1b04b2 | -6.9346 | -43.5168 | 2024-12-13 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 408.3 |
| 55998f0b-c441-396c-ade7-46d4b97cbe93 | -2.5108 | -51.7817 | 2024-12-13 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ee010e92-1641-35b7-8e92-34ade2bc9686 | -2.4923 | -51.8233 | 2024-12-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7e0ac795-8c44-3df4-aa05-fec15c475a49 | -14.7848 | -52.642 | 2024-12-13 02:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 62f78f9a-8b30-3e6c-bb33-ed3166e68c96 | -11.2151 | -53.8125 | 2024-12-13 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d03aa9f2-daef-39e6-8547-ee32a2c37560 | -6.9346 | -43.5168 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 404.0 |
| b8789f94-46b9-31f7-8d63-28fcf1009f9f | -11.1962 | -53.8142 | 2024-12-13 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c644ca48-cdd2-35c0-8d86-14287920930a | -2.5108 | -51.8023 | 2024-12-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| bc6d06ee-c799-3c5b-abeb-8f729d985abc | -5.211 | -43.2833 | 2024-12-13 02:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 83ee5982-da98-37c9-b9b4-f712bfbb9eda | -6.9158 | -43.5185 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 325.6 |
| d1b6a308-f352-3ed0-9408-dba13d7a6b47 | -13.0644 | -52.0326 | 2024-12-13 02:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 66db1dc7-20a7-3e3f-8d42-2522ac7546b2 | -1.62 | -46.6747 | 2024-12-13 02:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2865e18b-42f0-30e3-9b4d-0c0fedb65109 | -6.9156 | -43.5418 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 5f5a2ad4-2c83-3b21-8e14-d33e1e237c68 | -3.2685 | -46.9362 | 2024-12-13 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6f07de61-7990-3874-950b-c7b73bf3b4dd | -2.5108 | -51.7817 | 2024-12-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 03319e16-380e-37f7-b72b-93943f28ef95 | -5.2108 | -43.3067 | 2024-12-13 02:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| b67d0fe8-b3b8-3869-8bb8-c68a9e202826 | -13.6933 | -54.7555 | 2024-12-13 02:40:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2094ebd9-d556-386f-a3b6-d4960bd498aa | -6.9161 | -43.4952 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 098435ac-c6d5-37bc-b1a7-a318a936f841 | -6.9349 | -43.4934 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ff057682-64bc-3ad3-901e-5c7f8ffbde47 | -11.1959 | -53.8348 | 2024-12-13 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 59b6cd7e-fc0a-30fb-95f4-ea38658e3f0a | -14.7655 | -52.6446 | 2024-12-13 02:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0dd75616-2336-3289-a61e-023bcd533fc4 | -3.2686 | -46.9142 | 2024-12-13 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 58a25830-f330-32b7-8e75-7a5ee705bcd9 | -2.5107 | -51.8228 | 2024-12-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c2e1b68a-e417-33e6-b13a-a124da39e9d1 | -6.9344 | -43.5401 | 2024-12-13 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 3d234cac-a04a-3589-87de-3a1718f0ff93 | -2.4923 | -51.8027 | 2024-12-13 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| b310a007-bed1-3b7f-ab99-a771d3be063d | -11.2148 | -53.833 | 2024-12-13 02:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 66dab68c-0140-3916-b888-7dfdd0ab8aa2 | -13.6933 | -54.7555 | 2024-12-13 02:50:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ea7397b8-e97c-328a-b6aa-d2b34cc2d3a6 | -6.9158 | -43.5185 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 335.7 |
| 57fc4825-5b51-3f00-be3b-1923989b12ba | -6.9346 | -43.5168 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 342.6 |
| 8b802b5a-9a92-37a9-a3e0-87bca15558e4 | -6.9156 | -43.5418 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 223.1 |
| fb0a60cb-7f7c-3b56-844e-cdb5a535c804 | -2.4923 | -51.8233 | 2024-12-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7f084079-b470-3046-bba5-9f165350c5a6 | -3.2685 | -46.9362 | 2024-12-13 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ccbbfabf-d4ec-35f6-8a97-a4519c12cc96 | -11.2148 | -53.833 | 2024-12-13 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 12c61b27-27a8-3dad-9aa7-a23f7c331175 | -6.9344 | -43.5401 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 218.0 |
| f097428b-9398-380f-9abc-217ca6ec14b4 | -5.211 | -43.2833 | 2024-12-13 02:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d350b12c-ac9e-30df-bcee-ebaa0571134d | -11.2151 | -53.8125 | 2024-12-13 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f388baa0-f9e1-38f5-ae29-030274fdb331 | -14.7655 | -52.6446 | 2024-12-13 02:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9bc13598-ad7d-3772-a62a-319f82c28a3c | -2.4923 | -51.8027 | 2024-12-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| cb7da73a-d0ca-34b9-874d-f41f57d4f477 | -5.2108 | -43.3067 | 2024-12-13 02:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 4c3bf768-1b8d-30d6-b56c-afdc0480cb2c | -13.0644 | -52.0326 | 2024-12-13 02:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 920d9ddf-7438-3925-aeb6-720257e9db9e | -3.2686 | -46.9142 | 2024-12-13 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 681a8fde-2049-3716-8e2f-a1f0cbfc407d | -2.5108 | -51.8023 | 2024-12-13 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 626e8eba-0936-3504-8079-ffe74ebeb8e5 | -6.9349 | -43.4934 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f1119020-5468-3c9d-a20f-aeda0240173c | -11.1962 | -53.8142 | 2024-12-13 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 364ebcf7-d6aa-37e6-a0dc-8768ed1c88c8 | -1.62 | -46.6747 | 2024-12-13 02:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c7008d69-1526-3a0e-876d-652a3bfea28f | -11.1959 | -53.8348 | 2024-12-13 02:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c2647af1-3d3f-3829-b352-257896df375d | -6.9161 | -43.4952 | 2024-12-13 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fc312ff4-0672-3cd0-bc1b-b5f765c0a6d9 | -14.7848 | -52.642 | 2024-12-13 02:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 75dec4da-ba2b-3573-9881-e2cea3d603c1 | -11.2148 | -53.833 | 2024-12-13 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 48185524-8ad4-38a7-8bb0-99c19722ec3c | -6.9349 | -43.4934 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9574f415-6d42-3cab-80d1-02ba200a68d7 | -6.9346 | -43.5168 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 311.9 |
| 98c6b4b0-e30e-328f-a306-700002638dfc | -3.2686 | -46.9142 | 2024-12-13 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 0cafe6b4-d96a-3a1c-87b5-4170b9523a73 | -5.2108 | -43.3067 | 2024-12-13 03:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 24c1d5f3-704e-3b1f-a6a5-a963628460b6 | -2.5108 | -51.8023 | 2024-12-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| bfe61ffb-a905-365e-b0e0-af2737dcdde8 | -6.5631 | -51.1126 | 2024-12-13 03:00:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| beb33177-3cb8-364d-be76-5efac9f80b89 | -11.1959 | -53.8348 | 2024-12-13 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a2f6c74b-9e1f-39fe-9f38-e22c2edfec6d | -1.62 | -46.6747 | 2024-12-13 03:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 193b3a4c-1873-3ca1-87ba-4ddcf0b4fc6c | -6.9156 | -43.5418 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 8f06240c-d82f-3c75-988c-d1f209b36af7 | -13.0644 | -52.0326 | 2024-12-13 03:00:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1256af9f-87a2-3d67-9274-67fc36b3c7e4 | -13.6933 | -54.7555 | 2024-12-13 03:00:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 90512ff5-61ea-300e-8ead-b96593c14a5b | -14.7655 | -52.6446 | 2024-12-13 03:00:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 0e5716c9-0c90-3c22-8d3c-ce856c2ef3d1 | -5.211 | -43.2833 | 2024-12-13 03:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| b9ba725a-4980-3a51-896b-a609e3e50636 | -6.9158 | -43.5185 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 313.2 |
| 30204102-b33b-310d-ac47-c5dc2ac58682 | -2.4923 | -51.8027 | 2024-12-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| cf229532-2456-3c3d-aa73-597e9a517242 | -6.9161 | -43.4952 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 166b230a-ce42-38cb-92dc-be76dbe20715 | -11.2151 | -53.8125 | 2024-12-13 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a1f0cb40-d707-38f3-976f-7a91e140ad54 | -11.1962 | -53.8142 | 2024-12-13 03:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c0d70ba1-34bc-3624-8aa7-b8f55aa552e1 | -2.4923 | -51.8233 | 2024-12-13 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7b2162a9-33e4-3000-a70a-516ccc2062dd | -6.9344 | -43.5401 | 2024-12-13 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 8ea41aac-c9d8-34ea-806e-5adc4b81d5e7 | -6.92 | -43.52 | 2024-12-13 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee728595-8938-3d59-93da-3dcbca299ea9 | -6.9 | -43.51 | 2024-12-13 03:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a029410-ca62-3053-9bb5-23317ff8350c | -6.93 | -43.56 | 2024-12-13 03:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3a567f9e-e694-3857-86b6-8b23d57f0e9f | -9.97824 | -36.18083 | 2024-12-13 03:02:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51421d01-16b9-3163-9c3b-2a7e86ffb6a6 | -7.75435 | -35.14406 | 2024-12-13 03:02:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd133c8a-b7b4-3fe9-b38a-b587398c7faf | -7.34638 | -34.85707 | 2024-12-13 03:02:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 06470b33-a42e-3779-9fea-11b3f51c4130 | -9.97272 | -36.17973 | 2024-12-13 03:02:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31ee89bf-9382-3ef7-bd00-fd9f1d69aa8e | -7.3523 | -34.85458 | 2024-12-13 03:02:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 47eb1e37-4fdc-32b3-a7aa-5ec234ac2088 | -7.85616 | -35.2086 | 2024-12-13 03:02:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed7e7fba-63b7-3616-b6b2-619c85231477 | -7.34697 | -34.85378 | 2024-12-13 03:02:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1c215086-e7f5-3a4b-b1e5-32bd97d9a6ae | -7.35289 | -34.85125 | 2024-12-13 03:02:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9baa75aa-26b6-3107-83f1-d81bbb68b866 | -7.74898 | -35.14311 | 2024-12-13 03:02:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9a7eb89-e5af-38ab-a477-d38ab520a8d3 | -6.56022 | -39.44253 | 2024-12-13 03:02:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e9c0582-c7aa-39d2-8674-4549cd6f00b7 | -7.85833 | -35.20992 | 2024-12-13 03:02:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 14cd135c-9c3e-3d6a-beff-c751795bd426 | -6.56743 | -39.44335 | 2024-12-13 03:02:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 631fbcec-5649-3a21-bc80-d96c3b1ff468 | -4.72082 | -37.36158 | 2024-12-13 03:02:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bdeaa0c-fdf6-34b0-b133-d0a976fdb7cf | -5.45054 | -36.87246 | 2024-12-13 03:02:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README9.md)
