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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaf0ef4a-a289-355f-baa1-6f1df73bb55b | -15.8464 | -42.0336 | 2026-10-10 00:09:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27ec2f22-e16a-3ece-8001-ef87104b3dc5 | -13.2489 | -43.994801 | 2026-10-10 00:09:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c527743e-30af-3ab1-846a-4c2caa66c18e | -11.9493 | -43.4977 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6536bc8a-8065-3230-9f32-6f22d57ba6ab | -16.628901 | -40.590099 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65a3bdb6-da66-3569-b709-e764cd2d133d | -11.6041 | -43.751801 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aef764cb-67d3-329a-b20c-e8ef4b01e16e | -5.7418 | -43.267601 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65535442-4b57-3414-b185-f47c3e5f9568 | -11.0769 | -44.111198 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37618a49-8656-3a00-9869-757bfe02e4e4 | -9.0112 | -44.357498 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65f81fe0-31ba-337f-b332-4de5c62ad950 | -13.409 | -43.732601 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb9efc72-cc70-3247-99a0-febb681e770b | -14.444 | -40.7388 | 2026-10-10 00:09:00 | METOP-C | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cecdcb46-a84c-3be6-8437-0198d7d839fa | -15.0515 | -41.805401 | 2026-10-10 00:09:00 | METOP-C | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cab66a95-7093-314c-8b75-64083ee556ee | -13.3434 | -43.908901 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34559695-98d2-314e-acbb-d0ca593cd3df | -11.8243 | -43.584 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ca9790e-415f-343d-b714-ba61988fa66e | -5.2142 | -50.6717 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77369215-286a-3778-9401-dd75eb573bad | -8.1965 | -45.750301 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d51eb837-5bdb-3b68-8799-80cad70ba93b | -12.2799 | -47.038502 | 2026-10-10 00:09:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9444df-7af3-350d-ba00-ded493c1fdf4 | -13.161 | -43.278301 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 233fd913-ecfa-3ee8-92df-86d8812ec894 | -14.0034 | -43.250401 | 2026-10-10 00:09:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ce504d7c-86f6-3ac6-ae7d-9aac23fd542b | -13.9015 | -47.843601 | 2026-10-10 00:09:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2fcad5-4c7d-3207-899f-73944b3e05ac | -12.0097 | -43.445099 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fffef71-b507-3fab-bddf-a046b00e4bc3 | -7.4761 | -42.837101 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 880d311b-9e43-3a7a-aa89-12016ef679d9 | -9.0133 | -44.367199 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a88d67f-a708-38d9-9a08-b13ac464b4c3 | -16.184401 | -39.340401 | 2026-10-10 00:09:00 | METOP-C | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 604bc241-e689-333e-8d57-21439daea0a2 | -12.0546 | -43.415798 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f502cdc5-a1a2-3dcb-becc-c0aacd6955e5 | -7.2271 | -44.1693 | 2026-10-10 00:09:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9b130ca8-33b4-34a5-aca8-512f1a1f60b6 | -7.0525 | -40.9575 | 2026-10-10 00:09:00 | METOP-C | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46f5700b-4f33-3ce1-9d1b-5ebcf0fcb8d4 | -12.0634 | -47.374802 | 2026-10-10 00:09:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9ac03e8-a6df-3c71-af34-8da6b8c6790a | -3.6809 | -47.8186 | 2026-10-10 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50118578-43cf-37aa-829d-65a903d700fe | -4.438 | -47.913898 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff70a9c6-d7a3-3115-b804-0a05bef2ce9f | -16.661301 | -40.549702 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a72685d-375e-39a7-a937-d038a60e00ec | -14.3232 | -44.666401 | 2026-10-10 00:09:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e128e810-812c-3bf0-9afe-c709a7ca1b6f | -7.1099 | -42.5336 | 2026-10-10 00:09:00 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eff473cb-de1d-3e24-bd07-e46368d76e80 | -15.3893 | -41.902599 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58e7040f-c3ab-3957-a81c-e73add48fcb9 | -6.8718 | -45.9137 | 2026-10-10 00:09:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aaf8cae8-5470-37dc-98af-1944334ba1ae | -14.8062 | -42.3433 | 2026-10-10 00:09:00 | METOP-C | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8b6f5e1a-ea4e-3e79-9288-02a533c40feb | -6.1499 | -42.840302 | 2026-10-10 00:09:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31e570b5-bf7d-37b4-9f12-e1049d8f5536 | -11.9569 | -43.486099 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da5e5205-f2b9-3681-af71-7497bd40d9eb | -14.4402 | -43.935398 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9d35f5-7947-3796-bdcc-0a1b702ffe1b | -11.9745 | -43.472401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59ce4997-bb6e-35cb-80fb-92d467946345 | -11.1207 | -43.261299 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5faaf1f0-88b4-3c71-a721-8d4f64640e62 | -8.3246 | -45.017101 | 2026-10-10 00:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2344ddf1-0421-3836-8bc3-5b026a32bb8c | -13.677 | -44.291 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5a4a79e-0f16-3f61-8a20-b02e851f3f7a | -11.0727 | -44.091301 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1eee999f-fe46-31f3-823e-1f4a073dc08b | -6.7626 | -48.669102 | 2026-10-10 00:09:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc01c8c-b0d0-3339-949d-60040c3c6be8 | -3.2525 | -50.381001 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5aeec1-d572-3199-be01-310804236399 | -3.2185 | -50.1828 | 2026-10-10 00:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8788ffd3-daf6-3858-a013-82224243d80c | -4.3829 | -41.8162 | 2026-10-10 00:09:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a53229e5-5ebb-3b90-80fb-94b946641209 | -4.4251 | -47.5322 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b0b46d4-51b4-3ce2-bf8d-dd4243c4f3d3 | -14.8505 | -50.283699 | 2026-10-10 00:09:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 340df6d3-9bb0-314f-938f-e302187b66b4 | -17.284901 | -41.2258 | 2026-10-10 00:09:00 | METOP-C | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97a8bc44-fe08-37a5-a0d1-d779bbf742b7 | -10.8867 | -44.806999 | 2026-10-10 00:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5791d0b-c107-30a0-93ee-403be620c634 | -3.6711 | -47.820702 | 2026-10-10 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce7e079-b0fe-3de5-958a-bf0f7732f9a8 | -7.2389 | -44.175999 | 2026-10-10 00:09:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97d0c6d7-11c9-352b-8adb-8f80c641d5a2 | -6.9061 | -45.882999 | 2026-10-10 00:09:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b09561e1-2442-3837-bf7b-3efe6c836533 | -11.5625 | -43.700199 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8876cfcd-7eb5-3709-b8bb-15b6038b98ec | -9.0056 | -44.378899 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd070834-efa0-3510-ba60-3f07849107b5 | -13.2412 | -42.254002 | 2026-10-10 00:09:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 681f44cf-2bec-3413-be04-26f1a7d9edb9 | -3.2159 | -49.440899 | 2026-10-10 00:09:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d75bdf13-a0b3-38fe-b145-e35bf027ec96 | -4.4006 | -43.116798 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 228036c4-2268-3de6-8b80-980088677bba | -8.9634 | -45.945702 | 2026-10-10 00:09:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 32372359-b902-3779-8c08-f5af7acbb3d9 | -6.8755 | -43.694099 | 2026-10-10 00:09:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c22a64e2-92f0-387f-b381-9f4cd78253e7 | -12.9909 | -43.344601 | 2026-10-10 00:09:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97d2738b-3450-34a9-8e11-6456e8c3bbf5 | -11.5979 | -43.722801 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2936c26-6d1e-378a-a20c-190a93963ceb | -7.5074 | -48.013 | 2026-10-10 00:09:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 292c8502-3257-336e-97db-8f7bd175ec3f | -7.5227 | -45.3307 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d983cc4-e579-379a-9804-9e861ae6ba6b | -5.6988 | -41.756302 | 2026-10-10 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 92f809c8-1a5c-3047-93cd-ea2f1ab4d658 | -15.3734 | -41.924198 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a290f80-d521-3419-9654-cb216bd4bbcd | -14.4446 | -43.957298 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a538bea-3b46-3d4f-bbf4-64378daac1b0 | -5.6798 | -49.023201 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02258a4-cf81-387a-826c-8972474653b7 | -15.3887 | -41.9482 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07a4bd63-e8b1-310f-b378-ef6fcf7d2d47 | -6.5619 | -51.113499 | 2026-10-10 00:09:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72d0d648-3cce-31a1-81db-0b1998759cda | -4.9039 | -43.338902 | 2026-10-10 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaf40bc9-ae79-31c8-928d-9369f5e30ba5 | -13.3554 | -43.9174 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e82e0098-472e-3713-93dc-375c7aac835a | -15.3789 | -41.950401 | 2026-10-10 00:09:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 79050561-358c-386a-ae31-a766adaa3081 | -14.8558 | -50.3134 | 2026-10-10 00:09:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4107b1ea-5545-3854-b531-2dc79ed54243 | -5.7472 | -45.132301 | 2026-10-10 00:09:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 117d3db5-001f-3f68-ac8f-00af9ace1282 | -4.3098 | -44.993599 | 2026-10-10 00:09:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8ec183c-8344-33ec-9ea8-3f4cc8a29f55 | -7.0658 | -41.606201 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6964cb28-42e2-3755-b6cd-747a9a5c92e1 | -3.6839 | -47.8321 | 2026-10-10 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 076ec513-fea6-333b-b8c0-97315a40562e | -16.119801 | -46.8899 | 2026-10-10 00:09:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66e1a79a-dbcc-3972-8d77-2e4e62bb9eb9 | -3.3715 | -44.480099 | 2026-10-10 00:09:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6c656b-d49c-3971-9624-0e95bf4a5a78 | -8.1916 | -45.775398 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2d6f4ca-a079-3a65-b1c4-6d8ddec4e767 | -9.9009 | -44.8797 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74094b09-147a-32e3-9abb-fa6235054d20 | -7.0836 | -43.474998 | 2026-10-10 00:09:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07a2387d-d02b-34b1-9858-bd3d4d89ee9f | -5.4269 | -39.270302 | 2026-10-10 00:09:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 615fdacb-a1f7-3a46-90be-be601a834d90 | -6.0135 | -40.9669 | 2026-10-10 00:09:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72db76f4-afe2-3b11-910d-c7f518c38692 | -12.8673 | -39.928699 | 2026-10-10 00:09:00 | METOP-C | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6702b42d-544a-3cd3-8de3-4dd66b00e11b | -7.0978 | -41.747898 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1030da9f-80bc-3871-92a0-0d069294bc4c | -4.923 | -45.072201 | 2026-10-10 00:09:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ad30e2a-194c-3039-aa74-15125addebbf | -11.7429 | -46.786701 | 2026-10-10 00:09:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c310b324-4a4d-3cbd-ae51-cd3bb8920c65 | -6.9037 | -45.871799 | 2026-10-10 00:09:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c193c972-03fa-3120-b275-f71d3e609ab1 | -7.4859 | -42.8349 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9fad99e5-9fce-309c-8eec-5696aaa6ce16 | -11.9667 | -43.484001 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc1664f3-db19-3a63-807e-6b7b97a77254 | -14.437 | -43.970299 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb2059e-b33e-3905-bfb6-9eaac37067b3 | -4.9881 | -45.7785 | 2026-10-10 00:09:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5d56baf-439a-39eb-b8f8-55f88ccd4e70 | -6.8266 | -39.567501 | 2026-10-10 00:09:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ec3509b1-792d-322b-80d5-271fd7dcc6b9 | -3.6741 | -47.834202 | 2026-10-10 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30a6ae96-057c-3f5b-a2ef-b3c28b817661 | -9.0014 | -44.3596 | 2026-10-10 00:09:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| acd0dd44-114c-3152-b35c-b47c75ac9c05 | -14.0329 | -47.002499 | 2026-10-10 00:09:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 80513f97-9a88-3e70-9459-322f43690ef8 | -5.2251 | -45.368198 | 2026-10-10 00:09:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
