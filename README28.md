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
| 46496ca1-e016-3316-b0eb-e9347d200da5 | -11.40504 | -45.14322 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0b99571-ef22-33b3-8632-d27df73af41d | -11.40224 | -45.13227 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57193a21-ff0f-3dbc-a206-8f4a009a2e84 | -11.40133 | -45.13732 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 828bc91a-da30-3091-8147-a1b544fcad87 | -11.40042 | -45.14238 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d45680a-73c1-3d46-84b3-e2e405316fb8 | -11.39861 | -45.15245 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb3e46f2-ba18-3f66-bf38-02112c2d3b75 | -11.39771 | -45.15742 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55314633-0f88-3e5b-9237-069e1c335f2b | -11.39672 | -45.13643 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5473a223-23e7-3273-8bd5-643f845892cf | -11.3958 | -45.14154 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28e367b8-af70-312b-9905-2e0253f18cc0 | -11.39488 | -45.14663 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceef4a6d-9f7a-3bca-b633-927c4f0126b7 | -11.3354 | -45.03312 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 091d661d-0063-3503-98cf-e1abb2ee3db3 | -11.33532 | -45.03002 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f0d0ee4-adc1-3cdd-b129-df2b3aa9353e | -11.33448 | -45.03831 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d2d8a28-14b0-33c1-98cb-31851a17b842 | -11.33435 | -45.03522 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a64e15ac-db47-3aaf-b227-f34db2c2ed79 | -11.33072 | -45.03278 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9f8f07-ea74-344d-87ff-13364c138a2c | -11.09943 | -45.08665 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2496958-f3c2-3bd6-aedd-ada5ab69b270 | -11.05463 | -45.37012 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be92dd80-5b42-34c9-8d49-742b7d583fc9 | -11.05389 | -45.36834 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea5bd2ed-1b4a-3e58-a1a4-ebca92a3210a | -11.04993 | -45.36916 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d50460-2012-3561-b192-394889eabf13 | -10.92916 | -44.77167 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14fd7e1c-2c09-3a78-9919-ff301010ac32 | -10.92465 | -44.77064 | 2024-10-29 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8af76b1-49a1-3dbc-a035-9c36ddd75d44 | -10.9122 | -45.1761 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16980fc2-2022-3e0f-914a-c385715d16c1 | -10.90753 | -45.17527 | 2024-10-29 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86a10a7-2ce4-3e5a-aeb5-5f1a7b2c7d1f | -13.36951 | -45.11232 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d169ed9-fdb6-3b8d-ac37-80a3cdc58916 | -13.36869 | -45.11686 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9433d8a-5909-3106-9f55-e26897350360 | -13.36671 | -45.10239 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f307a179-bc5b-30a5-a688-78b4ebe43472 | -13.36589 | -45.10692 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80b16535-5815-3606-87f1-b8e10ea3ca19 | -13.36507 | -45.11145 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdf14041-15cc-3e40-ab6e-df27ff1d7e1a | -13.36424 | -45.11599 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 225d32d8-49fc-36b4-b7fd-e9926c932f6c | -13.36227 | -45.10152 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e84eabd9-b72a-35df-993e-401c9fedd77c | -13.36144 | -45.10605 | 2024-10-29 03:47:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f6890e5-ca1e-380c-8720-e52d62deea82 | -3.47954 | -45.49453 | 2024-10-29 03:47:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72375b09-22f9-32ff-a82e-e7b32bf22986 | -2.24423 | -45.6149 | 2024-10-29 03:47:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f178ff7b-6075-3a07-abad-5597654f799d | -2.24363 | -45.61858 | 2024-10-29 03:47:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75658e16-01f5-3afc-add3-b53bea64b03b | -5.11454 | -45.14693 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc26bae1-b57d-3f96-8b49-d244ab1cde5a | -5.10937 | -45.14614 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc767f7c-a77e-3dd7-bf1b-eb9c32932957 | -5.09655 | -45.28438 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a00e51e-c675-3403-8d06-9b51727ca5b7 | -5.05011 | -45.52602 | 2024-10-29 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0b4e784-87e9-373f-809f-c0c7e3d1aa52 | -4.94152 | -45.43584 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8290fe1-bc10-3489-8025-591d929e81ba | -4.93622 | -45.43514 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e6335e47-8a12-3fa2-a674-4ba6b3f3a109 | -4.93568 | -45.4383 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 862e7c07-2a4b-37f5-abdd-fdc861e04d6f | -4.93033 | -45.4379 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5eaf2583-69a4-3143-9b89-266034fc357e | -4.86176 | -45.77203 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ffb22b0-4d06-36a7-a9b6-71eb360f7d50 | -4.85632 | -45.77139 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91713c47-ed6b-331b-850a-382b5622c5e0 | -4.69952 | -45.88624 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 858dc3ba-fa73-3ce0-95d5-e884e0086e39 | -4.69891 | -45.88991 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91ecdff0-db43-3456-a8e4-23e76e30bd4d | -4.69351 | -45.88862 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 841d4719-afff-3062-b2ec-18819f232ddd | -4.67846 | -45.8121 | 2024-10-29 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71f19a0b-1c13-3140-a751-581d7ecfdb60 | -4.67783 | -45.81582 | 2024-10-29 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45f1dc09-a733-39b1-8452-2e5452c2b2c3 | -4.47655 | -45.9348 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33660c39-7738-35be-ab9c-d29255ee6c9c | -4.47623 | -45.9352 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e99e0fc3-7ddf-3d0e-872e-24a7cf01c507 | -4.47594 | -45.93829 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f3ba11c-24df-34f6-aadd-f2c086f05fa3 | -4.47564 | -45.93872 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4aef928-b362-3e9f-b02e-53609aa4b434 | -4.46346 | -45.91043 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c50a7840-20e9-3da9-be0f-643375b4badc | -4.45793 | -45.9098 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c40182f-1933-3612-bcf1-f4d81ecdca7d | -4.27137 | -46.10629 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcf33e3d-9fe4-3f8d-b48b-85331d391f9b | -4.27072 | -46.11007 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d94fe38-3a59-31a9-b870-688e838b2f67 | -4.27009 | -46.11375 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea1710ab-367a-3e7a-85df-9841947aa312 | -4.26581 | -46.10528 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e49ee8a-edb9-3513-b98f-6e7bd8faa642 | -4.2646 | -46.11232 | 2024-10-29 03:47:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c587806-2d1b-326f-9988-06bfe7985a9e | -3.84183 | -45.94078 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09401bb9-825f-3338-ba7f-91cd48f708ca | -3.84123 | -45.94444 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 147265e2-72bd-30e5-91c7-009874ba8f94 | -3.84103 | -45.93987 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f66dedf7-7555-314c-9831-93ccee08758f | -3.84062 | -45.94811 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10aa53f4-faca-3afb-ae1b-516163e8f440 | -3.84041 | -45.94348 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c2e53d9-f0fe-389f-8c6a-4ad1eae262f7 | -3.83978 | -45.94715 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d0d220c-8d8c-31af-8901-9e4d5d257e7c | -3.83628 | -45.93987 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5a5eb7e-24d9-3309-83ea-bb7289d39206 | -3.83568 | -45.94352 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e92943f-3b22-3ca2-9191-ccfdfb2fa5b8 | -3.83508 | -45.94717 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97acfc9b-6390-339d-ad88-18efd3408c08 | -3.83486 | -45.94258 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a871e858-a4fd-35f2-b64e-b55f7adf8c2e | -3.83423 | -45.94624 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e14dcaa-4cfc-307e-ac46-a589856f0da2 | -3.78466 | -45.84054 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5faf19-b2b4-391f-ad5a-6fb2b994eb8d | -3.77653 | -45.95586 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 519c7a70-d458-3576-8e2e-90906becd4b2 | -3.77592 | -45.95953 | 2024-10-29 03:47:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f07de3b4-f0c6-3093-ba47-e0f8cc5b6489 | -5.09709 | -45.28118 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9821baa3-f52a-3946-b49d-9cc22210e8b4 | -5.04953 | -45.52945 | 2024-10-29 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e80e20a6-4ba4-3700-b98c-23045b221489 | -4.94204 | -45.43277 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38a1bfa4-c70a-34a4-b5ca-572712fb4cc5 | -4.94097 | -45.43907 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61168c99-70aa-3da4-8028-82630230bd68 | -4.93674 | -45.4321 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac40b309-a4b9-37e7-96ab-7ecaccfc92d5 | -4.93144 | -45.43143 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a4829548-2910-3aec-8149-e4e3f6c4039a | -4.93089 | -45.43465 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d78816df-a260-30d1-92a3-8b102d627945 | -4.92979 | -45.44105 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0991cb1-e0fa-3e8f-9488-35437391f8b4 | -4.92925 | -45.44418 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65ca9e9b-517d-3076-be4f-1023b7b44fd3 | -4.92616 | -45.43059 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dea8051-7dd3-3c16-8c55-5fd4f9e2af2f | -4.92559 | -45.43395 | 2024-10-29 03:47:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3972eab4-616a-30de-a8df-b32d72ee7b1e | -5.44607 | -46.35728 | 2024-10-29 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 435f53dd-39da-3f9b-b0fb-9c284a009aad | -5.44052 | -46.35627 | 2024-10-29 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a8d472f-7b54-37d0-899c-d09648247081 | -5.41478 | -45.65899 | 2024-10-29 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 629e3fca-dc62-3829-acb5-5e3472f09a93 | -5.1821 | -46.21329 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b183209-36d1-31c4-b0da-0e8663955a6e | -5.18152 | -46.21667 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f0e6bcc-0c6b-3423-9265-1b60efb3991f | -5.1814 | -46.21539 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4632c683-5e1b-3bf1-b40c-4d5cbf752188 | -5.10029 | -45.96215 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 720195a3-9f4b-32a6-95ef-70d855a46a77 | -5.09969 | -45.96567 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aab0fc1-b348-32a4-a4e3-cfff2dfb3ec5 | -5.0991 | -45.96915 | 2024-10-29 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22a9924f-a532-3ece-a572-dde7fab6bb92 | -5.97182 | -46.29852 | 2024-10-29 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad165d6-3ca7-37d1-85e7-8fe2862c32c9 | -5.18757 | -45.19622 | 2024-10-29 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d15671a1-b698-3ece-bd07-9cecf9f3efba | -6.94878 | -46.10628 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3010d12f-d269-3cf8-bcdf-f11421014d21 | -6.94816 | -46.10971 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c99fe187-2642-3ad7-92fb-6b8a429ba78d | -6.94754 | -46.11317 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6779c9b6-411f-39ab-94b1-cbba08c6b2cf | -6.94471 | -46.31498 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 241b46df-82d6-3d5e-8c0a-df186701f7e7 | -6.87073 | -45.90834 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
