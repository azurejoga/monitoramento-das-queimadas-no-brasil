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
| f55cd6ed-09ec-33d7-b880-7d6b7e788be6 | -5.18641 | -46.15614 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2c1433f-7c5e-332a-8c0b-e242c4aac8be | -5.12912 | -46.09233 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55506027-819d-3c03-913c-2446d014c0e1 | -5.12575 | -46.09181 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd57bfeb-6b2f-3114-8b4b-ca316b29a623 | -5.03688 | -45.87395 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d4665ae-b29a-324a-8713-31f00341bdd0 | -1.73648 | -46.71756 | 2024-11-01 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9876cc41-89c3-38e6-9f23-f4f0287c7c2e | -1.62973 | -46.07644 | 2024-11-01 04:29:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0412ac96-52fd-3ab4-99c4-89b7f7d957f6 | -1.55001 | -46.25841 | 2024-11-01 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e89c623-d037-31d3-92f5-869d17b836d5 | -1.54946 | -46.26186 | 2024-11-01 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a87a1ab7-cc91-378c-87cb-d827ba5156f3 | -2.0758 | -47.12857 | 2024-11-01 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fb2c07a4-bce0-3c1a-a060-948b4929d3ad | -2.07526 | -47.132 | 2024-11-01 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 22d4eba7-a7ce-3a5d-ae89-011b3295f8e3 | -2.00978 | -46.3833 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41747c70-3022-3b2f-8dc6-a998a12d874e | -1.96869 | -46.42653 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d2a6d2b-cdf3-3a49-ac0f-2f1df699a4df | -1.96539 | -46.42601 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83198a1a-94d3-3c37-afe5-aae9a2b970d7 | -1.96208 | -46.4255 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 476ca993-fdda-3480-a31a-59dfe7536120 | -1.87718 | -47.05541 | 2024-11-01 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6801f1a1-4d58-33c8-b668-c87e05fcf269 | -1.16992 | -46.21365 | 2024-11-01 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a901d5e6-11e8-39a5-90a2-019125fbb948 | -2.5161 | -47.35632 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec92fdd-f491-3b23-a48a-27f40b50adeb | -2.49166 | -46.27831 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4607c4-421e-31c4-a16c-8fb7a9de0ed2 | -2.49112 | -46.28177 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043b03c2-712d-3a95-afd5-fcaeabef9037 | -2.48889 | -46.27433 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 288e8739-760e-31ad-be25-e600e272c8c7 | -2.4813 | -47.27302 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a12e81b-dd75-34ab-9abb-4525a146c34e | -2.44726 | -46.9303 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2f051a-68ef-3e44-b626-9f6644622e1c | -2.43892 | -46.89436 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9df4354-aa79-3cc8-8d07-b73ecf5499fc | -2.43838 | -46.89778 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a271805c-1e78-30c8-a00a-c2571e0b2246 | -2.43616 | -46.89041 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d688510f-48f6-3123-8dc9-49de1276e0da | -2.43454 | -46.9007 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36631da4-7a12-32d0-b66a-0a59c1b81b39 | -2.42789 | -46.70631 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6972f93b-0f8b-388b-8b16-f63edbee9621 | -2.42735 | -46.70975 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d990c5-4c6e-34b5-985e-d625437dcea1 | -2.42513 | -46.70237 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4427301a-9cb4-3900-8835-86a74955fb2f | -2.42459 | -46.7058 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f73f192f-248e-3695-8c21-be1105de84b2 | -2.42405 | -46.70924 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41a2c3f-f445-3bbf-b759-2dde8f5a8799 | -2.42351 | -46.71267 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e798e6bb-848e-3de1-9d3b-ef5e9801d582 | -2.42236 | -46.69843 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f26e3f-4c46-33c2-ba67-123e42cb3ac6 | -2.42182 | -46.70186 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b01af45f-46e0-3ec0-a306-f6df65b0348c | -2.42074 | -46.70872 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d72c7b97-699b-3655-8572-53b49ff1d396 | -2.42021 | -46.71216 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4df26f1d-7da5-3c7b-bc3c-ef1182585de2 | -2.41906 | -46.69791 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad88a26-4693-3bc0-ab58-262b882b30f4 | -2.41852 | -46.70135 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 291521ba-d258-3adf-9e28-81a882b81036 | -2.41744 | -46.70821 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f6eafe-f386-356e-a209-3b7280dae082 | -2.4169 | -46.71165 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81e35a37-aeef-3fb4-966f-9b4231668b55 | -2.41576 | -46.6974 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 433931d6-3700-3a34-8cf9-2b89a6a6892e | -2.41475 | -46.72538 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44481a20-475c-3788-a2b2-6703e78cea8e | -2.41414 | -46.7077 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b598777-1d0f-3e0d-9263-cf10565fdea1 | -2.41245 | -46.69689 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9a32fe-616e-381a-b7d6-43071bb968c1 | -2.41144 | -46.72486 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57827613-f4c2-30b6-8b3a-d48fd39bdca5 | -2.4109 | -46.7283 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5adfbd98-8caa-3f9c-838d-6ede334e6ad2 | -2.40915 | -46.69637 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e82c603d-0284-375f-982f-6c371c808f74 | -2.40861 | -46.69981 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f241387-6cc9-3921-922a-ba597123ca46 | -2.40837 | -46.4636 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d5313c9-c7f6-3758-ae45-cfcf44796e15 | -2.40783 | -46.46705 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b4b5d86-523e-3f20-b2df-38f863b75566 | -2.4076 | -46.72779 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b5a48a-82cf-3e4c-8579-ed6504ee4904 | -2.40545 | -46.74152 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d7998c-7013-3b15-a6a1-2a661c5ef855 | -2.4043 | -46.72728 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac616e76-940c-3e84-b7be-d522590aa80d | -2.40214 | -46.74101 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f13a8cb-7b75-36f4-ad7d-b2d3eb715be0 | -2.401 | -46.72676 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76e7b96f-b84d-3aaa-bf59-d9068b7e8705 | -2.40046 | -46.7302 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0fc6667-3689-33d5-b272-b401f8cf9193 | -2.40021 | -46.49412 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a74265ca-8dda-3be3-8fd0-bfd2f1f3d1ad | -2.3969 | -46.49361 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf57d531-dca3-3b43-8923-5af7f25e492d | -2.39662 | -46.73312 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb077b20-a01b-3967-9a9c-4123381d4ebe | -2.39001 | -46.73209 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca9642bc-6b84-37d1-8f4a-1f04b32127db | -2.38671 | -46.73158 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73a4cf4d-139e-32a5-bbfa-5df0aa93d23b | -2.38448 | -46.7242 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7da9e210-3ffe-350e-b686-f28c58e982e1 | -2.38395 | -46.72763 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3058f21-e7ce-37ed-a09e-b2167a8a3688 | -2.37805 | -46.56788 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa4d32e-d133-3ad8-9b2e-69424200cb8d | -2.37474 | -46.56737 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3da49c3c-63fa-3669-95f3-a416c6e73d3f | -2.37249 | -46.75751 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d95016a0-b2e6-3f20-88ef-522e6e5f317a | -2.37144 | -46.56685 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b461fba9-8a9f-3847-9354-e650ea8d363d | -2.36919 | -46.757 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6701cde-f327-3189-b69c-203df8e43c36 | -2.36813 | -46.56634 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f902ad8c-c024-3ffa-96a9-5c6862a27459 | -2.3644 | -46.41755 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983addae-8930-3b9a-8811-e8c1ad0cea58 | -2.36416 | -46.52695 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a0f33d8-9c49-33f2-a89c-acc0fbf8d485 | -2.30069 | -46.82325 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 100f4401-72f7-3192-8def-f6732d2738cc | -2.30015 | -46.82669 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a5fbb11-d3e0-33e5-a6fb-1cd290040c69 | -2.29739 | -46.82274 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 141496c9-811c-3641-8726-5244ed3d8c36 | -2.29685 | -46.82618 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eae060ac-0a7d-3a16-9ec5-8c6d0705a4ab | -2.29631 | -46.82961 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 028ce0ac-95e5-3e72-800d-5e672e4dcd59 | -2.29355 | -46.82566 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed74581d-8f12-3adc-872f-70089fd7a088 | -2.27529 | -46.7912 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7c13149-9463-3254-9ea1-f372320a499d | -2.27475 | -46.79463 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16fce213-b693-37ac-97a7-5a7015efac1a | -2.27421 | -46.79806 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56360f9e-c172-314e-be98-8915aaab98c1 | -2.27367 | -46.80149 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e395138-d51d-39a0-b2d5-8780891d8cf5 | -2.27246 | -46.76616 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 798faeb4-910b-3330-9fab-a0aefd33448e | -2.27199 | -46.79069 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa8f9cbe-e7aa-38d5-b2b3-b028484e331e | -2.27037 | -46.80098 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 392aa90f-54ed-3689-9049-c9d56949a0bb | -2.26983 | -46.80441 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9f757b-9894-36f4-b68f-d3b13bde18b3 | -2.26875 | -46.81127 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80ce9f09-00b7-3dea-80ed-afcbae91b354 | -2.26869 | -46.79018 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85582083-7e7c-324a-a465-d6d47c6d4c33 | -2.26599 | -46.80733 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42b3124b-c0d9-3e95-897c-66eb606f19ab | -2.25885 | -46.80973 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab1b19c8-896c-3f5a-a6c4-8128341135b4 | -2.25609 | -46.80579 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 595dcfc2-cc78-3989-b479-5e9f7690f5ec | -2.25279 | -46.80528 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20362adb-65a6-3cf6-af85-bb76f7047987 | -2.22704 | -46.79417 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 812a5609-1875-3a02-96f1-2d88426e978e | -2.2265 | -46.7976 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f201a867-d292-3e31-aef0-48c7afb59311 | -2.22374 | -46.79366 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4cdb1fe-2def-3d84-9df5-a9b86d0ef069 | -2.2232 | -46.79709 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c04dc7d-f67b-3704-a3a9-da582f4bb5fb | -2.85755 | -46.65366 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19d1a2ba-af98-330b-9d44-660bee0007b1 | -2.82879 | -46.62097 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db02132f-4a70-3735-ac1e-739b4d321b5f | -2.8128 | -46.61496 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba30887a-e81a-3ed1-950f-b434af5e3a7b | -2.80259 | -46.63413 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a771e5d5-7c1a-3dda-862e-1b3e86af54aa | -2.72701 | -45.98943 | 2024-11-01 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
