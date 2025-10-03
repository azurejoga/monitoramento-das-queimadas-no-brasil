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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 823250a6-5932-3021-a8ea-ea491adc99c3 | -15.58876 | -46.91131 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39e81887-12ba-3c30-bba2-504493b880c8 | -12.29686 | -45.37465 | 2025-10-03 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05528599-b9d2-3cba-b831-9025c2840cc2 | -14.98382 | -49.96348 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e06d1c5-67f2-3234-ad67-8ea9377df8a3 | -14.3035 | -45.88378 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 248701fa-ef25-3f31-907e-8366676bd186 | -11.10254 | -47.81672 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 395dc7f5-74fd-3166-8640-b85510475acf | -13.12544 | -47.8699 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd42a83e-ca23-3ed7-8c03-66aad90fe75b | -14.87669 | -48.30319 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 12c87474-a72a-398d-9e34-10ed756c4bc2 | -12.63532 | -46.97211 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 768275a1-73e8-3930-ae59-2a547c6cd739 | -9.94459 | -43.75406 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1c3e86c9-9369-38cf-a114-7c227b8e7e6e | -15.21866 | -47.1877 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a7f3c460-2a50-36de-90f5-57aa1c84fe36 | -13.7744 | -47.57496 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49205fdb-c642-3725-ad24-75fcd7f3f73a | -10.75655 | -45.34728 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef76601d-3c87-3b35-a99d-ec0e56b8f473 | -14.29513 | -45.97961 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53e49c50-d4cc-3864-a819-90de53fff620 | -11.45036 | -42.23045 | 2025-10-03 03:45:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5efc29c6-32ac-303c-8765-a1fe185dbeb2 | -14.65863 | -48.25847 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84edaf80-e26f-34e5-b5f4-97a650ce3cce | -13.29495 | -46.9836 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 666aedea-3fb7-3108-8799-a7b541765887 | -15.31234 | -46.28279 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31285e5a-b8a0-38ba-822f-c880be449a7d | -11.42364 | -42.11292 | 2025-10-03 03:45:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2d0265f2-0c15-3f52-b786-001d5b9a9b7b | -8.71095 | -47.98176 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c4a5b90-8a30-3f81-9f71-aa6160a29034 | -11.85575 | -44.97061 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64358aa2-a0d2-38eb-945e-20e8fda2c6c6 | -14.90905 | -46.96585 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6d4b94b-2cde-3538-9556-942876421c5a | -10.90845 | -47.04291 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a160b0f-7293-3b1d-9de3-3e435a226690 | -15.17159 | -43.6236 | 2025-10-03 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cdb308e-2355-3959-be17-049b89f15b61 | -14.89903 | -47.8246 | 2025-10-03 03:45:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9505e0b6-534a-3a7c-972c-c4ed5731b75f | -15.19495 | -46.40551 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6816fc09-4285-3133-82c5-94005f8ca3ea | -14.31681 | -45.86996 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf09ff3-c040-369a-a12a-17b7c438b587 | -12.6362 | -46.96763 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 17f08aab-3b72-3678-b37e-b6d2fc2ba3f5 | -14.59099 | -48.34758 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f989037-e220-381e-b782-fe797f3eaea7 | -13.74322 | -48.01744 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 701f5276-b054-350a-9c2e-7162672c6e02 | -13.27328 | -47.24302 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4a92287-195a-3f9b-a6df-8e27eda2bf99 | -15.94884 | -43.34125 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc073209-2362-3d32-a761-befb96c21e46 | -14.93286 | -46.90274 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2b08188d-23c3-3adf-a6fa-46b45305e577 | -11.83067 | -45.02202 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42f1ad28-e79d-32c6-afe9-793cbe105feb | -14.9197 | -48.30236 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f643955f-d03b-353c-afd8-aad11f7bd324 | -8.79657 | -46.66727 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2a5c514c-9222-3aac-9f92-eb7f9c1212b8 | -13.63744 | -48.67426 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6362fabb-8c2e-3b09-9292-d2d22997f8ea | -11.59912 | -47.65181 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1411c0b3-d1b7-331d-8d78-d596327df1ca | -15.32816 | -47.32701 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d09632d-e3c8-3d0d-81cb-2a15779c582f | -14.64575 | -44.74169 | 2025-10-03 03:45:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c12c01-bcd5-3efc-af47-755eab5c69d5 | -12.63704 | -46.96333 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 378c9603-9c5e-395a-a6b6-c11d6e9d3f7f | -11.1251 | -43.39639 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 58b8aa14-07a6-3324-9b27-e37da124b721 | -13.75988 | -48.08499 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 144c97fd-99f2-33bf-9406-53ba4b97c9d8 | -13.97716 | -48.17173 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 84d150dd-2f42-3b1e-a33d-c18618b11d3b | -10.88642 | -46.71668 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94f34bb3-a471-3a62-bc9a-5d4bce9de8cd | -14.68633 | -48.09377 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea342ebc-f968-3b91-b26f-ebbed13a859e | -11.55363 | -47.66164 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 18ce66ad-52c6-37c0-b297-92847d0ca7d5 | -13.76293 | -48.07029 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed367445-9360-3be9-b5c5-0efeaeb1b2e8 | -14.90497 | -48.29312 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ef54215-e0bd-392b-941d-cea48d3e539f | -8.45355 | -46.83968 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f62fb5ad-ce71-3166-aff3-28ae7318cbf4 | -12.90035 | -46.89517 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e583ae8-813f-3b8e-b150-c865925930cc | -13.95787 | -48.09667 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 954a0de7-f5f3-3673-998f-7c76def2c396 | -12.82965 | -46.90906 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6342d1c5-63be-30e7-8b54-6e3d55cf8dc8 | -13.77259 | -47.58382 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eb33385b-e302-367a-9b18-b16921c38e4b | -11.87256 | -44.98849 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc9436d5-4e81-305a-aaa6-c37b92269f93 | -12.86418 | -46.99965 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41502c1d-d1c6-3455-909d-597f887c36ac | -9.90573 | -43.72329 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 389c39e6-308a-3498-a2bb-0fb89e6b8103 | -14.41306 | -47.86799 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6de6fb1-6183-3564-b25c-c9a168aea096 | -12.37046 | -46.51689 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f25428a-a498-3207-8b90-591910458b44 | -12.91217 | -47.15769 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45717d6d-b464-3f50-9898-ffc8a0cf20cd | -8.89815 | -45.02978 | 2025-10-03 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 717807d6-7fbc-3e1d-9193-7c6466d01ccf | -8.7099 | -47.98716 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 271f77ca-2d72-3814-88f0-9ee71ead68d5 | -13.96654 | -48.16352 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96b8c826-ad2b-3069-b41b-8a0b08fd0207 | -15.32312 | -46.38904 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bad82278-2760-33a5-a5df-32903d6d723e | -14.86972 | -48.33594 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0bf02e6-511b-3c07-87f6-33d82ce39edd | -15.36625 | -43.66891 | 2025-10-03 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5f0958c-593e-335d-ab55-08ce15d7e1d9 | -13.68349 | -48.6348 | 2025-10-03 03:45:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a05153e-0018-3eed-a229-a3b85a68048a | -8.80248 | -46.66836 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| be28b67c-41ff-3882-b8d6-7edbd027a60d | -14.98244 | -49.96998 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79eeef04-a9c8-38b4-8682-9ca4e43d4d3a | -13.77137 | -47.53143 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5319ebf-0473-3965-bff9-e5f04903a6aa | -11.08489 | -47.87301 | 2025-10-03 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47b6a326-9f27-369e-adb0-acad914454df | -13.7404 | -48.00162 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9209e711-2ca4-375d-86ee-09bdbb51082a | -11.10407 | -47.84068 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 783798f9-e8f5-3151-81a5-fb12a5f6dec9 | -15.30414 | -46.28699 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb26eaa4-272b-3b47-ae59-f769e1a0cd27 | -13.22647 | -46.43564 | 2025-10-03 03:45:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ca4f99a-7264-3e1d-97af-7132f5f8072c | -13.37647 | -47.28123 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bff177f-6ff7-334d-9400-ab71495631eb | -14.74312 | -48.10897 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1e31d35-1f17-39b2-93d9-d0e78d52ce54 | -13.14504 | -47.89476 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56b641f9-a659-31c9-ab0d-3ae9280e031c | -13.35985 | -47.33392 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad946a06-8ab9-3b4e-adea-8ff35873b8b2 | -9.90266 | -43.71372 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a07557fe-ec67-38d0-96cb-9f5542044e75 | -12.75675 | -44.91387 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b523202a-3728-3df9-a827-db65490dff3e | -13.26846 | -47.26773 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e617c1ad-bfec-301c-b2ce-bf36ec1929a7 | -10.87229 | -46.67521 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a8b2091-8840-33c6-9522-6a39c98363d7 | -14.95032 | -47.52121 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 47f389b1-2a55-3981-9d40-d712a79f193f | -13.13383 | -47.88938 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dd1e254e-3263-3ebd-ba84-8a577753ba66 | -15.21212 | -47.64485 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03677a99-1c7a-3d3a-8d06-388a88057932 | -13.7458 | -48.01437 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7449c308-1c3f-31ab-a323-1c4186c3c14f | -8.81303 | -46.66637 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc7aa2b7-b73c-310d-ae42-ee5d551e5f2b | -9.91437 | -43.73022 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| c12a04a9-d2df-3580-97d9-016cca620e21 | -12.87629 | -44.62709 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29ec16cc-f712-342a-a22d-f23310a78731 | -15.59514 | -46.90701 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c27e593-7f58-3a8a-a66b-55b7a1e74a34 | -13.30937 | -47.5806 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60e37397-f1e3-3bd8-b622-110001815d47 | -12.92886 | -48.43832 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dffb31a9-de77-3bcf-b995-15da3923d100 | -13.14503 | -47.83307 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 29175d69-fc9a-3a39-912a-e6b686958ac3 | -11.85246 | -44.96035 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2895b8de-ec22-3a7c-8412-0e27af317855 | -14.70006 | -43.88337 | 2025-10-03 03:45:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 651ed2f7-5b70-3c6c-9da1-723c3e068895 | -14.93134 | -46.91037 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f772a894-2875-3762-aaa2-116ecadead96 | -13.79131 | -47.57968 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fab4aee-95e6-3115-996c-e29e34c1e542 | -13.23435 | -48.49841 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fd1c2f3-9079-3a38-9258-a1e89850af5d | -11.43317 | -43.49704 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aadec49-d6df-3e10-8067-03f98de0ae0c | -14.38038 | -45.95113 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
