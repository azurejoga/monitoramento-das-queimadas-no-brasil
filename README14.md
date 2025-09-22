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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 792dcecf-a75e-3928-aee0-ca55d404a5e7 | -19.6349 | -45.37354 | 2025-09-22 03:51:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 251d9c97-8080-3584-9e15-5a6bac6d65c4 | -16.0734 | -43.47825 | 2025-09-22 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebcdcf94-f545-35e6-985d-77dabff58bdf | -17.6717 | -44.08449 | 2025-09-22 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ffe9d3-200e-3a50-a897-0d6ef22adcf1 | -18.38355 | -46.46684 | 2025-09-22 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0346a79e-0509-3e51-8cec-e0857ff4d9f5 | -14.44411 | -46.52732 | 2025-09-22 03:51:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9f332048-3f09-342b-b6e7-1db7bca8286b | -21.62935 | -43.65156 | 2025-09-22 03:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1a0eef7-e914-39bd-a269-2dae339bf996 | -20.87581 | -42.81096 | 2025-09-22 03:51:00 | NOAA-21 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57d42ad8-adf5-3141-a427-98d3a405d672 | -16.07046 | -43.47262 | 2025-09-22 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb2c490-2a37-3a5b-9c95-813697234c56 | -19.84412 | -42.21086 | 2025-09-22 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f108ddee-9672-38a4-acb2-dc6b1618559e | -19.63891 | -45.37441 | 2025-09-22 03:51:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c60cc1a2-b632-3827-9621-8f53455595a5 | -19.86716 | -46.10519 | 2025-09-22 03:51:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67da393b-8671-3e15-9213-378d8623ec33 | -18.10004 | -44.26354 | 2025-09-22 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da6d4b33-53e6-38e3-b90c-45960937602c | -14.33331 | -47.78815 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5406d863-eb60-3ed5-b65f-edd43d7dfac6 | -19.96081 | -42.10497 | 2025-09-22 03:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c50c989f-b414-3ada-b638-b31de1228ef2 | -17.63791 | -44.18185 | 2025-09-22 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cdcc657-e18c-3899-b879-342d61c908f5 | -15.53694 | -44.32178 | 2025-09-22 03:51:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8196125-fef3-30f7-a7ef-2a9d6f32840f | -19.87624 | -42.4614 | 2025-09-22 03:51:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 11f294e7-8b35-3788-8a6b-61ffaea6ff9f | -20.25931 | -44.42603 | 2025-09-22 03:51:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa4499f0-6a16-362b-9aad-7ad05c47814a | -20.14268 | -42.48428 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b68ef24-c722-34d5-8e65-549e373a7205 | -14.69369 | -48.78378 | 2025-09-22 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1b0df76-befc-3b71-808a-3f75fc223eac | -21.63436 | -47.49041 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 711f5082-48f7-3b9a-9d02-bef1ba7b09a6 | -20.14201 | -42.48821 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fe1458ba-114f-39da-b720-b212ed63017f | -19.9823 | -46.85733 | 2025-09-22 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24984c15-4153-39f7-9e14-2560e2d734db | -18.37746 | -43.69986 | 2025-09-22 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db8554e5-806b-3064-8ca1-9e2e8d2908b1 | -14.97467 | -44.43392 | 2025-09-22 03:51:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b481f06e-05ea-3f55-b678-8eca1b5d032a | -22.70514 | -43.35154 | 2025-09-22 03:51:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d888c7f-a658-3413-87b6-b44cec714645 | -15.16054 | -49.5867 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 2f818704-909d-391d-bd01-c3a22536830f | -17.4073 | -45.01684 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9507870-9a4f-3a73-8107-a3164664dc91 | -14.35619 | -47.78722 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e72d011-a1c1-3a32-a3a7-0646d2171d27 | -18.4009 | -42.86085 | 2025-09-22 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 18fd017c-b8ef-350d-ba2b-c6287e9646c1 | -17.27009 | -43.45444 | 2025-09-22 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b361a91-fab9-39bf-97ce-721d8f6c4b00 | -19.31013 | -43.75698 | 2025-09-22 03:51:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd10df2c-8085-31c3-ab94-8c782436b63f | -20.86818 | -42.81367 | 2025-09-22 03:51:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e58907ec-849b-3222-ac5c-936f07c168c0 | -22.84215 | -50.60946 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eabd697c-0bb7-3844-84c2-1797e95fbfe0 | -23.05427 | -46.8049 | 2025-09-22 03:53:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 994e6553-2b9c-387c-b1a3-6e524d592367 | -23.45365 | -47.61188 | 2025-09-22 03:53:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 581770a7-38e0-3f57-a3dd-5675f988cc0b | -20.39813 | -54.86924 | 2025-09-22 03:53:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c40623d-aa19-3f05-8a65-3326d54a3c81 | -22.80725 | -50.59291 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b74cb4cb-5612-3efe-81a5-7127f8e69999 | -22.30117 | -46.69102 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39816494-ede3-33fe-8fd8-b0fec2ea68e3 | -22.84371 | -50.60242 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9578f2a7-a642-38d4-847d-8a132bee2982 | -22.30532 | -46.69194 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7170fd2-cfa2-30d1-b74e-21f1975c900c | -20.39979 | -54.86243 | 2025-09-22 03:53:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4db2acfd-cbed-333e-a139-94f4172d6a0d | -22.82285 | -50.59711 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b50a8e9a-91db-3ab0-8bb4-a6dd599a758e | -22.30369 | -46.70022 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f992af1-b159-3d65-8d05-d2dcb2424446 | -25.42425 | -53.44844 | 2025-09-22 03:53:00 | NOAA-21 | BOA VISTA DA APARECIDA | PARANÁ | Brasil | 4103057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| ac7dbd62-f97e-3d7d-836e-bc1855135da7 | -22.80647 | -50.59639 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2d7e4909-12d5-3d88-a290-61a447c62355 | -22.84658 | -50.61435 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1ebd8451-90d2-3f48-9976-066cd8f6afe3 | -22.82206 | -50.60066 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2706b502-74c9-3cc3-9463-5a293717c145 | -22.73221 | -50.66156 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff6867ab-6aac-353b-8f7a-9e7ecc483fb4 | -20.39617 | -54.86831 | 2025-09-22 03:53:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a259ffd4-b572-3a24-8e26-fe8f47213d2a | -23.23046 | -47.63153 | 2025-09-22 03:53:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ce71e0d4-1c90-3ebd-b234-4a7ee7468581 | -22.83227 | -50.62912 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 4339cc18-5857-3c15-bec5-457275c0b929 | -22.8458 | -50.61787 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0ad2ce39-372f-3ef2-8e7f-1e76efc979b1 | -22.30285 | -46.70446 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 99256033-1610-361b-8ecd-16c68daaf51f | -22.30781 | -46.70132 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c25df37b-b6fe-3137-b717-40965907b319 | -22.81165 | -50.59789 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f2b18fb8-4afc-3092-9b1d-3babf5184dc2 | -22.81763 | -50.5958 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| eb788c41-f0e4-3856-8179-f592ab27769d | -22.84293 | -50.60596 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 699354ce-a6e1-32b5-ab1b-3d85e3341edc | -22.83695 | -50.60807 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| cbc4fbe4-2441-3620-8482-0c6a0be9659d | -22.83981 | -50.62 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dc6528e2-5610-32e2-9953-aa4ddf94f1bc | -22.83461 | -50.6186 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1c84b753-dee3-3496-af3b-bad68db86e82 | -23.43804 | -47.62223 | 2025-09-22 03:53:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5446b0dd-6066-3c23-a06c-bd79d7b37a94 | -22.30451 | -46.69608 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d8238c7-ef81-3ac5-a8b1-79d06edb7e00 | -22.83017 | -50.61377 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| aa1f5a73-86a5-3d63-8b3f-245570aa44df | -22.84503 | -50.62136 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 43ce854a-dd1a-3465-97e7-052a19f86ebe | -22.83773 | -50.60455 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| dfcf9c68-a2bd-30a5-8f8f-4447ec9a521c | -20.39788 | -54.86146 | 2025-09-22 03:53:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb153f60-c43b-3737-a1b8-048a2cb83968 | -22.30699 | -46.70547 | 2025-09-22 03:53:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 57f9041a-2320-3597-9f99-38cf6062b5a8 | -22.81684 | -50.5993 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d64232df-ff53-39c3-9972-645b7083072d | -22.83305 | -50.62561 | 2025-09-22 03:53:00 | NOAA-21 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 9aec31eb-ff71-321b-a175-2aa74be91bac | -23.44934 | -47.61094 | 2025-09-22 03:53:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2733d2f0-2d33-3934-bad3-88efa00b742b | -16.0166 | -59.4432 | 2025-09-22 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| b752f5b8-d61e-3ac0-8b56-a82fbbf1d0b6 | -16.0163 | -59.4633 | 2025-09-22 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| fd7a422d-3934-3e8a-a355-e4c7f4ac73f3 | -15.9594 | -59.3687 | 2025-09-22 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cf0ba6be-2128-37a2-a7a2-c1287d81b5f5 | -15.9969 | -59.4651 | 2025-09-22 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d3483c12-0ce3-38f0-b174-25c813a15f62 | -15.9591 | -59.3887 | 2025-09-22 04:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3b7dcce1-e0dc-33ad-8d9e-3ef7e9205d4c | -20.274 | -55.4927 | 2025-09-22 04:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 51dbd214-5a93-39fc-af00-dbb1fb65df5b | -16.0163 | -59.4633 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 0bf7b37a-a1dd-3412-b43f-877a5639ae5a | -15.8412 | -59.5199 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 217aa081-0528-3752-aca4-377426a763f3 | -15.9969 | -59.4651 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c549a477-844c-34e9-946d-1091b5fac968 | -16.0166 | -59.4432 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bbe0f6fc-81c1-32c2-b95f-204a1add0cb3 | -20.274 | -55.4927 | 2025-09-22 04:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 7bc3258f-2928-33c2-be03-7b0ec8fd246f | -20.2537 | -55.4959 | 2025-09-22 04:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9291d86b-cb05-3174-8764-044ccff0f622 | -15.7846 | -59.4053 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 91d913eb-5e96-3c54-b4a8-1b44432d7b98 | -22.4273 | -46.7907 | 2025-09-22 04:10:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 00c75752-8cca-313d-81c9-be7203694450 | -20.2735 | -55.5141 | 2025-09-22 04:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 35ede1cb-4294-3020-8e6c-95fa52139937 | -15.7652 | -59.4072 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 5fdd66f6-59e5-3851-a9c7-54d7ebcb5c96 | -16.0357 | -59.4614 | 2025-09-22 04:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 53c4be55-15dc-3e55-a1bc-7ec8b5a1e975 | -14.11791 | -44.0095 | 2025-09-22 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9870e61b-10df-37cd-8e29-42243a6b4a2d | -4.31594 | -48.09631 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4975206-f7c6-363b-b409-916b7a44208b | -3.85048 | -51.34339 | 2025-09-22 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f7d494-91e7-3168-9147-3c83a0d941c3 | -5.5779 | -42.12737 | 2025-09-22 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e96db5e6-dbe6-3f66-82bd-380b1e14baa4 | -12.33577 | -43.44686 | 2025-09-22 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48a709a6-9fba-3d23-a832-26671eb6943c | -4.31656 | -48.09255 | 2025-09-22 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 537dd0ec-9cd6-343a-a669-9ca284e3356f | -12.0774 | -44.85405 | 2025-09-22 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdeee56c-380a-33f9-93a6-526d7d1cc243 | -7.79906 | -46.18279 | 2025-09-22 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b4c43fa-2b9e-31cf-9b90-ec065af1dc9b | -5.65379 | -51.4681 | 2025-09-22 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1ecb5b2-f868-3de7-ae7a-3fbae8990a25 | -3.33209 | -50.08901 | 2025-09-22 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdc56d26-7334-37b3-9d7d-0f49732822f1 | -11.08127 | -50.75043 | 2025-09-22 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 895c8161-4ae9-3e7c-9bf1-0e78cf93e30b | -5.83242 | -49.02655 | 2025-09-22 04:17:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README15.md)
