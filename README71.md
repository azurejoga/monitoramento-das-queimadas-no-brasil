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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfb56304-4fbf-39d6-b017-9caa1a90937a | -8.87953 | -62.45598 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60d4431c-4e7c-347e-a6d5-27d5ec95449f | -8.90669 | -60.71994 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e8ad8ea-7aa1-343e-9fd6-567e8aa779d0 | -10.52683 | -46.78552 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49b60bd4-543b-37e5-830b-b04817bb76a8 | -14.24089 | -53.04572 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4693ddcb-ece6-36f6-ae26-457bfde4325c | -13.43877 | -46.99405 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c676e063-a6e2-377d-9cec-363e37766fa3 | -10.53801 | -46.79473 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b7052e35-22c3-36bf-aa69-396cbdf0e5c6 | -13.52367 | -46.90355 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fdf13dc-b7f9-37d6-a230-744aae448ba6 | -7.43552 | -60.62024 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d982e69-aab5-3977-957c-90b7e3cad7bb | -10.52274 | -57.98041 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cbd14d7-b690-3d2f-96b3-39d28eb06ce0 | -9.79438 | -64.25977 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3477b09a-998f-3cd6-83bc-a5fe88c89fa2 | -15.06737 | -48.69773 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51d9f8fe-8534-36ec-82ce-e42b851e5205 | -11.11803 | -51.87303 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e17c0171-3c1f-385c-aa0c-b0d5cb342a64 | -13.44092 | -47.01025 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74d160fe-d362-377f-ba69-8885c3f73fa2 | -8.86038 | -62.43877 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 91c61ca4-d4eb-3239-8b9e-1b819235719f | -11.14207 | -46.33518 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b9b366c-e3f9-3119-ab7e-8453ed8e1d43 | -15.03196 | -48.68568 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a331da7-f1a9-369c-b811-e467731b8edf | -8.86111 | -62.4568 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d56ee213-4e1d-38f3-95d3-5da6bcaa3215 | -9.20168 | -59.51717 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2787411-7cba-3701-9c05-6922e6ee45ca | -9.31276 | -48.26348 | 2025-08-26 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07aa7d5b-2e1b-39b9-91f6-9d693465ecb1 | -13.41027 | -46.88161 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4e726ab-37d2-339b-bfbb-4a6347e742ed | -9.22633 | -60.92395 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae62340f-4c75-3b09-8b34-98dc994c4f1c | -13.41949 | -46.90882 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b44234ab-8093-3c6c-9b6a-6f1d88c86baf | -13.65951 | -46.88552 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 981c9842-6038-3981-8a3f-4aa6997b33ec | -8.88217 | -62.47425 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 924d8959-f0a0-335a-911d-c6bd5acf9476 | -13.50639 | -50.81221 | 2025-08-26 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5f324ba-78aa-3469-bbc5-f527538530d0 | -9.07964 | -65.71759 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f72e087-4949-30a7-8da8-dd5c81327537 | -11.05473 | -52.01742 | 2025-08-26 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838aec60-c6bc-3e42-9b63-c83e0506c6a1 | -13.8219 | -45.89216 | 2025-08-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f55dee6c-ddc0-3add-a986-6f91f4df0a76 | -13.05688 | -46.30754 | 2025-08-26 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc1085df-69e8-3a96-9019-240cf9332d7c | -12.3734 | -46.55758 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11ea2ae6-077e-3e8a-aa6e-2d264c386445 | -14.39605 | -51.94025 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753faa1d-8940-3c3d-9f76-2c1b6ad4815f | -8.1089 | -62.88366 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc04c4b2-4b99-3010-b9d5-37ee8cb6f700 | -13.44669 | -46.86708 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e77a91-9e7c-3680-bc07-cf409f9c1109 | -9.17793 | -59.46175 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 843d5380-6ca4-3c9b-a22c-f4848a0a73cb | -11.69301 | -60.17244 | 2025-08-26 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e6d514c-235d-38e1-81b4-d4f7b266f13c | -14.72416 | -45.37108 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3946821f-e949-3577-a94b-2c3adce35cdc | -8.86274 | -62.44823 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe5db2b1-2ddf-30bf-9117-930708d1d423 | -9.16671 | -59.52574 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42a440aa-02b3-3707-844a-375767763124 | -13.52689 | -46.91158 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcbd8dbe-76cd-3410-bd65-e6d1b1ddcf9a | -11.55145 | -52.11882 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d9f5834-ddd4-30b7-b2c4-ddc4c8b9f75e | -13.47934 | -47.01022 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 27f166a8-ecf2-3aed-ac14-d03231f5e9a6 | -13.4968 | -46.87914 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea383e4-2faf-395b-b443-c445b6cdb2eb | -11.1601 | -44.75877 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 75e2d3e0-67b5-3d88-895a-a865dcf625b9 | -9.16685 | -59.55344 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aebc5858-b867-357c-8797-13cfc77da06c | -7.44026 | -60.62469 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a9de7e9-18ad-3ccc-8be2-e1cbc9a4f460 | -11.57463 | -52.12256 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 84d8eb19-0b5a-39b8-9c89-6635e457f746 | -13.38857 | -51.78809 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c13c2e3-caae-31cf-bd22-d65b9f737922 | -10.77755 | -47.06742 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60140261-6fc9-3937-8f68-bd72b35ce7d6 | -9.27562 | -56.90422 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4dd5295-fe2e-390c-97bd-7ba436f21e27 | -7.65204 | -61.46473 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e390efb7-582e-358a-b8ba-f52d6fb8f994 | -11.54482 | -52.11775 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4004daff-c671-31c6-9f5c-cd6ede71c7d9 | -9.23894 | -60.82402 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26352483-dbcf-341e-a781-511100b86a5e | -13.58581 | -48.19296 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0369fa88-767a-34af-8822-808761c7525e | -9.17376 | -59.50639 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7eb98e85-1310-37c6-bd2c-d52976da5cae | -13.61025 | -48.1609 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6077c2b-7223-3179-bab4-cf9188beaf50 | -10.53853 | -46.79107 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 12816968-b815-3e98-959f-3fffc9bead79 | -13.52739 | -46.90786 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 487c6bf2-e9fb-319e-ba37-1a50ed22d6b1 | -11.56966 | -52.11096 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b3fb3747-ceb6-351e-821f-060af2a97303 | -7.39084 | -64.34632 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c80380ae-d4ba-3d15-a4e7-bb7c48545912 | -9.27501 | -56.90779 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b46b506-f456-37d8-95cc-ca42785c6a9e | -8.98446 | -65.41754 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 304fb465-dc1e-3ca8-8bf7-19e373320d93 | -11.63312 | -44.86264 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a9a9f48-d92a-34a8-b769-75a9a436d4c9 | -8.5752 | -62.63232 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8b9831b-a2af-32cc-ba20-81d389cf5d39 | -9.16306 | -59.53758 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93536ffa-25f7-3d27-8255-40a0bdf04eb5 | -6.91022 | -59.35997 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db387e1a-597a-31e2-9e79-eb03e259a26c | -9.19989 | -60.91883 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a9c9892-335b-3c6c-ab18-b5d8fdb31237 | -7.38173 | -64.35717 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7c77494-4434-3292-904a-d9f540f6d8e5 | -13.44509 | -47.01104 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de72118-f95b-3f54-a31e-31bfb5bcea39 | -12.72877 | -48.14367 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3e62ee8f-bee0-3126-88ce-25c0c956ef73 | -10.13404 | -48.33523 | 2025-08-26 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e9fc44a-03dc-3f4b-852a-958b61194de4 | -11.03095 | -49.14582 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f946b73-f036-31d1-8dbc-ef0d2a399684 | -13.0112 | -56.88816 | 2025-08-26 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd68b75e-6ffe-3983-bd60-c68a521866d5 | -9.26286 | -56.90577 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f398112a-8c7b-334c-af19-6771583f654b | -11.52792 | -50.45321 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e06be2b-cc27-3bd0-b842-bed8ca01970d | -13.51628 | -46.89451 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1ee8644-77a6-3e4f-a4c6-4bd1d9d8a6f0 | -9.18103 | -59.50079 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0a7f3d3-f5b5-3af3-8927-d33c7be91773 | -13.45093 | -46.86757 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f786a8f-616b-322c-b3c6-5c4e02bea778 | -13.82593 | -46.69614 | 2025-08-26 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573248c8-be0d-3e9b-b225-9c5648ab7197 | -11.63244 | -44.86779 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa06c253-4c41-3e33-9b59-552682a81e60 | -7.65628 | -61.47337 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f19467f9-3dcc-3f3a-be27-2b3f5b4b6e4b | -8.3063 | -55.10386 | 2025-08-26 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55a9913e-d622-387c-8fc4-a1c75f4dfb66 | -7.38173 | -64.34722 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 74da8e30-b256-341b-9627-443506c283ea | -9.17312 | -59.46089 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8f432cf5-dafb-302a-99ef-80f0c905a719 | -9.16215 | -59.51535 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d258f71-32c3-3680-97a4-22da9ae60787 | -11.53102 | -52.11912 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b513cd02-7f61-3686-bb05-c280af2778b1 | -9.0844 | -62.67339 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c0f6a06-ea5a-3148-85d0-355ce20f4ecf | -6.76682 | -59.67585 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ff74c511-9a7c-3856-9dd1-634c4f57af70 | -9.24864 | -65.62852 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91a3c9db-c98b-3444-b4ea-a50181d0a176 | -11.10065 | -44.76006 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81d00137-99ea-36d6-a7f3-7d2a0fa6c8e1 | -14.84569 | -47.15442 | 2025-08-26 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bcd98b14-8a6b-393c-8c1d-47ab3864f565 | -8.5346 | -55.26514 | 2025-08-26 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f513176e-d9d1-3690-9b28-ea84a3a00174 | -10.3908 | -57.69684 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12c2f997-90df-35da-9b02-ba7c0e807e42 | -11.19316 | -55.0419 | 2025-08-26 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ce89585-f1c1-3474-828b-7a35eaeeffe1 | -9.47223 | -57.82768 | 2025-08-26 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be6bab8a-6021-3652-8495-6e35f396d253 | -8.98468 | -60.49622 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33082ff2-8e27-3aea-b041-c482f816b9a2 | -9.56977 | -55.37288 | 2025-08-26 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98695f9a-fccb-3814-8ecd-5aa4b6a0506c | -14.80301 | -48.96784 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d788b95b-6373-386c-8853-311175b22829 | -9.57561 | -48.63425 | 2025-08-26 04:46:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1faec52c-fbf8-3eb0-ae6e-ab03cbd735f7 | -12.74907 | -48.09251 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61569420-ee75-307c-811c-686d74cdfbcc | -9.1543 | -60.7855 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README72.md)
