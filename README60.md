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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 224ca6e6-0454-312c-ba56-3fb09e9ca51f | -21.00822 | -41.28306 | 2024-09-27 03:49:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 957cb360-c8e3-36c2-bfa4-b6c40f9b480b | -21.00489 | -41.28227 | 2024-09-27 03:49:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b52f6e43-29d6-3eb7-a3d7-33622b277250 | -21.00428 | -41.28602 | 2024-09-27 03:49:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ecda98bf-2035-3f81-860c-bfcaf74beadc | -21.28377 | -41.09707 | 2024-09-27 03:49:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aaf6ff56-a20e-313b-a7c2-e96412bf6685 | -22.87723 | -42.48163 | 2024-09-27 03:49:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1c7d8ca-63cf-3c1b-bbdb-df9d83163845 | -16.54065 | -41.44108 | 2024-09-27 03:49:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2272f13e-07fd-33e2-b7c1-b4f5b9fbcde9 | -17.99775 | -42.30835 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 52603645-9599-3829-8533-5e992a02c5b4 | -17.99421 | -42.30761 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8f062ff-f8f5-3953-99ef-1fc368329d1f | -17.98147 | -42.29637 | 2024-09-27 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c1b71bf-7d8d-3e48-826c-f237cdfed88c | -17.92212 | -42.13514 | 2024-09-27 03:49:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4af2e2e0-e361-3b6f-99e2-6de8297b4614 | -17.9207 | -42.14344 | 2024-09-27 03:49:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e247262-8b9f-36fe-bad0-b4ac57f9e7e2 | -17.77943 | -42.80837 | 2024-09-27 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a3d45e-07ae-309b-8e6e-23ce784ee13a | -16.87426 | -42.14356 | 2024-09-27 03:49:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9175029-7f90-3175-bbfd-cd9ed5174b25 | -16.87351 | -42.14782 | 2024-09-27 03:49:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b110b84-2ddb-3fda-bce7-9e419e1e92db | -18.90643 | -42.00576 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce74010a-ad5a-3bd9-a16b-48a3eb9509e1 | -19.00468 | -42.59387 | 2024-09-27 03:49:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f2e606da-0cba-3b76-baa0-c731474b4004 | -18.78928 | -42.79142 | 2024-09-27 03:49:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| df582d53-c644-3586-8aab-8f7350ed657a | -18.70585 | -42.09473 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c8ca6730-a43f-3183-990b-479fe76636cf | -18.70514 | -42.09895 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| fc8a225e-fc14-3ad1-9cee-d4230bf78d1b | -18.70443 | -42.10315 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ca5e97e2-17a1-3222-af40-0d32450690b7 | -18.70377 | -42.08574 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c5088bcd-6369-32f7-8854-0073fd0752cc | -18.70372 | -42.10733 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 12bf7a03-c1a3-3fb1-9d7c-aa747f20a95a | -18.70308 | -42.08983 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a216e3fb-650d-31ee-a2b4-aa7a63222a1b | -18.70094 | -42.10245 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 403f8886-9bfc-3458-aecf-d74a79aaf843 | -18.69957 | -42.08925 | 2024-09-27 03:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2c9520f8-54fd-3ed7-95ec-ba057b06e867 | -18.5444 | -42.56435 | 2024-09-27 03:49:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8483cf5-1aa3-39cf-b5e4-de23c39790ab | -18.54209 | -42.56602 | 2024-09-27 03:49:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3dc61051-bb0b-3110-b201-a3e1c6cf9b8c | -18.50023 | -42.21442 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4b5147bd-a486-3a3d-8f49-5d45ded56429 | -18.49953 | -42.21845 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3c465a30-d850-3a53-8ee5-856843e6972c | -18.49461 | -42.20493 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6e5fddbb-53a4-34d0-a12a-a734e8001885 | -18.49452 | -42.20626 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2ad7b16f-e79c-357f-824d-44df190ec914 | -18.49112 | -42.20413 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7a03ddad-6419-32de-a3ce-2e00bd13a554 | -18.49102 | -42.20549 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1320e2c5-77e1-3857-a6fe-7cdaa02a95ca | -18.49041 | -42.20819 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 54648af2-6037-3d47-935f-8ab62f5a81cb | -18.48752 | -42.20474 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8aee8474-d4e8-3a87-94e7-c60f91adef9a | -18.4868 | -42.20894 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 65936dc2-b675-3def-b2d0-0494a8c55432 | -18.48396 | -42.20429 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3351fb9f-ed79-3b5c-bafe-7db6a2c364e1 | -18.48324 | -42.20855 | 2024-09-27 03:49:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 529c249d-7a6b-3ad0-904a-fa90c84efe6e | -18.33553 | -42.61761 | 2024-09-27 03:49:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76799806-ed1b-33ca-a3ae-31862a33884c | -18.33385 | -42.16861 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| df7c6ce8-ec37-3022-9dea-c2b7cc24c459 | -18.33194 | -42.61688 | 2024-09-27 03:49:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 94c6d6b7-2464-352a-b073-aec5cdcfecfa | -18.31401 | -42.61342 | 2024-09-27 03:49:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3f8fd07-428c-3b18-b3f2-800540d85c5f | -18.31309 | -42.61019 | 2024-09-27 03:49:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 331d203d-7fff-337e-887c-1eb703dadc0e | -18.29376 | -42.74878 | 2024-09-27 03:49:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| af8186ec-5200-3e3a-823b-841cf55e1e62 | -18.2928 | -42.75004 | 2024-09-27 03:49:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 450e91cb-bfd1-3257-a504-30cc70c9a01c | -18.2746 | -42.13362 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfc696b1-739a-32ed-8d76-19884e72578b | -18.26879 | -42.67322 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93c68955-f78d-3eae-b0fd-bf7d55c32e0c | -18.26806 | -42.67741 | 2024-09-27 03:49:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecd23fc7-c79e-3fbb-a686-98d13a1bcb24 | -19.42189 | -42.63834 | 2024-09-27 03:49:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16733e3c-6788-32d0-a7cc-26349ae4f49e | -19.41836 | -42.63756 | 2024-09-27 03:49:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0fc657a8-898d-3f91-a048-825b0893bb72 | -19.40173 | -42.98557 | 2024-09-27 03:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee290e11-a8b8-3771-bf0c-c8f35b12937c | -19.39815 | -42.98473 | 2024-09-27 03:49:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c59bc4ff-7fd2-3c9f-90de-a04c13b8cf0b | -19.39724 | -42.57389 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 78c4dfa6-8a74-3ad4-a2dc-37ccc3cc18c4 | -19.39438 | -42.56923 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| c426cb67-efaf-3143-a0f0-3c47e84882d6 | -19.39368 | -42.5733 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| f49cdf41-b1ba-3b76-920a-0f16abf60d1b | -19.39081 | -42.56876 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b866399f-7829-3607-be7f-99ba508928f2 | -19.39011 | -42.57282 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d589f371-3970-3b8b-b78f-62334d391e2a | -19.38874 | -42.58078 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ae19dfc5-6aaa-3081-8918-50654126dde9 | -19.38807 | -42.58464 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9bfcffa6-e328-3331-9aee-0b38f47f0a4b | -19.38739 | -42.58856 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9ed1a45f-dfbe-3f39-8dba-d71d4d2b62d3 | -19.38725 | -42.5682 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 8aa21d2e-e054-3ff5-9484-baa7ed43f2bd | -19.38656 | -42.57222 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 1881c922-4e57-3278-8d6f-6b679d685383 | -19.38589 | -42.57612 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| b1153cba-d328-3f43-bb38-1e2654e199ec | -19.38522 | -42.57996 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0677bc0c-a8b1-35d1-8c12-0a6231b8ee48 | -19.38455 | -42.58379 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 28348264-dd3b-3466-b3e8-1c2975a0e6b8 | -19.38388 | -42.58768 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6d035fe7-4816-3ac4-b0d9-a53e21baa7da | -19.38318 | -42.59174 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2ce65d38-fce5-36d1-9fdc-102bfedf50ab | -19.38304 | -42.5714 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| b971c375-f582-3626-86af-46fd5bca19b0 | -19.38239 | -42.57518 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| c77e7e15-4cfe-33f2-877d-310e1ff7bef6 | -19.3809 | -42.56266 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4cacc2bd-ca51-3984-b3cb-17176cb1df71 | -19.38037 | -42.58678 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f0cb4057-fb6a-321b-bb3c-b3c2ad47531d | -19.3802 | -42.56666 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 404c6d7b-c5a1-308b-9fcb-3dcdcca01eb7 | -19.37967 | -42.59086 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 040e0702-2056-39d5-80c6-a367ff79beee | -19.37952 | -42.57058 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 096b6131-9aae-3bf7-b545-8169f0470fb5 | -19.37737 | -42.56193 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b77e6a02-46f0-307d-a102-f06c42c36272 | -19.37668 | -42.56586 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 648a08ea-1122-3bee-8d5c-712fc1c1960d | -19.37601 | -42.56972 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ded1795e-c6fd-3e20-8151-67772924c4da | -19.37535 | -42.57354 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 731b2cab-a2c5-3a67-9d24-db923bf023af | -19.37454 | -42.55714 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cff3ebe1-18fc-37e4-9e11-6477147b4ceb | -19.37384 | -42.56116 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| af3d8dad-b8ff-3308-a51b-e6657c81d66b | -19.37317 | -42.56505 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8b55dd84-736b-3b9d-a0b0-faf28030af76 | -19.37251 | -42.56886 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f40a990-2dc7-32b0-a3bc-bd49c69bf806 | -19.37183 | -42.57272 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f566a5e6-c815-3412-904e-58429760d9e0 | -19.37115 | -42.57669 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| cbeba368-85e1-3e9d-9cf3-3d11d59f581c | -19.37044 | -42.58078 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 0cf42cb4-9f86-3a0f-a74e-8501c9b5a3cc | -19.36972 | -42.58494 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8dd58fbc-1f8d-300a-b34f-9bb6380b418b | -19.36897 | -42.56819 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| bd204f5e-d3a7-3744-a1db-cc6f9035d7f9 | -19.36828 | -42.57214 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 93a61bcb-8c0c-3037-beca-f9ca063872ed | -19.36757 | -42.57624 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| abb9895a-e400-33db-bb96-020abb4d2890 | -19.36685 | -42.58038 | 2024-09-27 03:49:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c895d302-f6aa-3676-a2e1-cb7facc84174 | -19.27461 | -42.72991 | 2024-09-27 03:49:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cf6df5f9-7635-3b53-ae6a-f50af523d51d | -19.27316 | -42.72696 | 2024-09-27 03:49:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6ced5c8-7773-3aed-a472-98210ede3627 | -19.27243 | -42.73122 | 2024-09-27 03:49:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4eb870de-4467-3547-aa5d-874fab8a0413 | -19.2229 | -42.34072 | 2024-09-27 03:49:00 | NOAA-20 | NAQUE | MINAS GERAIS | Brasil | 3144359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8118c8c1-3c79-3f1d-8308-491b49bf7b65 | -20.97789 | -42.40394 | 2024-09-27 03:49:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 08600816-c3ac-3fc9-ad2f-479309b79fe9 | -20.97722 | -42.40786 | 2024-09-27 03:49:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4b57d942-caff-3391-a491-a3e5be4c0f76 | -20.84725 | -42.63214 | 2024-09-27 03:49:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f216ddb-1c52-31bf-97c0-89ea6c088e31 | -20.84375 | -42.63148 | 2024-09-27 03:49:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f273ee0f-61bf-3e32-9900-f942d8896cb8 | -20.7492 | -42.77842 | 2024-09-27 03:49:00 | NOAA-20 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6af60e3b-8f20-3069-ae30-6665dacef97a | -20.63282 | -42.2698 | 2024-09-27 03:49:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README61.md)
