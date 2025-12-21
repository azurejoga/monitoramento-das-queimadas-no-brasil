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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bd06dcf-481e-34d7-9481-08b14949d7c2 | -21.13934 | -40.95993 | 2025-12-21 04:06:00 | NOAA-21 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 05196058-b84b-3ed9-be58-43282c828ecc | -20.35843 | -40.37229 | 2025-12-21 04:06:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c736f74-2711-3976-aa5a-e8b3c5e53000 | -29.32318 | -50.20377 | 2025-12-21 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64613da1-9c95-3956-bfa4-1d7012e301c6 | -25.47117 | -51.28925 | 2025-12-21 04:08:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5db003ae-bcbe-3db7-bf92-50972145f42e | -25.46946 | -51.28674 | 2025-12-21 04:08:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fa350e88-5f4b-34c7-8d57-12a0bc86a3cd | -9.7255 | -60.1877 | 2025-12-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e501f661-41c7-3cde-80b9-85a018fd9148 | -9.7254 | -60.2071 | 2025-12-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8b6533f2-7a9f-39fa-a3cf-6aac95f0725e | -9.7254 | -60.2071 | 2025-12-21 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 29c6f54f-fc0c-3516-aa88-d13a6ed1f97e | -1.45908 | -53.3875 | 2025-12-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56876181-548e-309c-b107-7b3214e37ccc | -4.81287 | -42.21025 | 2025-12-21 04:29:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3e618ea-179d-36cd-9d48-7b8c0a3133ac | -5.06595 | -40.83934 | 2025-12-21 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7979c0e-51c1-3c37-8a0a-ba4052b2001c | -5.06541 | -40.84296 | 2025-12-21 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 213b31f3-ec8c-3d7a-af1a-39397bac96f3 | -5.2935 | -40.61394 | 2025-12-21 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 207470b7-a575-3141-89cb-f02075206f63 | -4.81246 | -42.21261 | 2025-12-21 04:29:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 992f174a-48b7-34cd-90cf-3d44308d1dcc | -5.98162 | -39.38318 | 2025-12-21 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 29337a25-0e71-3553-abf6-a1f7a9d709d9 | -5.54432 | -39.54031 | 2025-12-21 04:29:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28509202-2e45-3dfd-b7c4-71e928361b4b | -4.88787 | -40.4469 | 2025-12-21 04:29:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a2fed78-ffb5-37b4-9263-8cf7679326dc | -4.8873 | -40.45076 | 2025-12-21 04:29:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0bbc0dfc-30fb-3106-bcb9-a421a287cf03 | -4.71401 | -41.77023 | 2025-12-21 04:29:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 81619886-3185-3254-ac30-36090df68b61 | -4.8122 | -42.21476 | 2025-12-21 04:29:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6eb2fb2e-1967-3682-be1f-dfe2f973754a | -5.98236 | -39.38145 | 2025-12-21 04:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 65fb9433-a4ff-303d-9aee-70e135ee26f2 | -9.7254 | -60.2071 | 2025-12-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a15340b8-1b15-3e11-a554-1dd5c7dbb5d0 | -11.7595 | -43.32674 | 2025-12-21 04:31:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 912958fc-d2fe-37ce-8ac6-5d33331e226f | -7.47452 | -35.24795 | 2025-12-21 04:31:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53b1a6cb-aef4-3ef5-b488-62a9857d0ffd | -6.30675 | -41.88251 | 2025-12-21 04:31:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a29c50d2-2f49-3c54-a741-a6a07eea7d88 | -12.2681 | -44.61207 | 2025-12-21 04:31:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7a5db40-42fb-3676-ae39-51e2f0b9b221 | -9.57161 | -44.60484 | 2025-12-21 04:31:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e1198a4-fdd4-3c3c-af9f-67a9402a21c0 | -12.21632 | -42.4471 | 2025-12-21 04:31:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 76d8e799-9394-3017-acc3-95507e22c293 | -10.36938 | -45.16171 | 2025-12-21 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 873f354f-f92f-33d2-b09d-9a8cf5f110d7 | -9.26588 | -44.31298 | 2025-12-21 04:31:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17dd51ad-81f0-3572-8a81-c7a6c2fca73c | -7.48073 | -35.24883 | 2025-12-21 04:31:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84162957-3280-37f0-bb14-0265e78c7b04 | -11.76102 | -43.32385 | 2025-12-21 04:31:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3145ba74-ddde-3714-9c4a-884abc550829 | -9.0458 | -40.43192 | 2025-12-21 04:31:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 974ccae7-4fef-3d57-b1cb-2608f479c9e3 | -11.83935 | -38.19997 | 2025-12-21 04:31:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e051c076-02f3-35ac-8723-9c69598566e2 | -10.3688 | -45.16554 | 2025-12-21 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e81b2279-366d-3ad5-88a5-037cd44c7dcf | -12.72647 | -41.80718 | 2025-12-21 04:31:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed190560-60b2-3064-b4bc-077343872362 | -10.41144 | -38.03403 | 2025-12-21 04:31:00 | NPP-375D | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16f2714c-5131-3901-a426-e393f9f6add8 | -9.51613 | -43.24237 | 2025-12-21 04:31:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dbb0535e-1c29-3220-847a-0462fd967c4a | -11.76021 | -43.3219 | 2025-12-21 04:31:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ba39cf5-064b-3594-8e94-63cd1cb6fc8e | -11.84477 | -38.20079 | 2025-12-21 04:31:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ee42105-d426-349b-805b-c575e83a1cea | -11.75564 | -43.32617 | 2025-12-21 04:31:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36a824a9-8d42-36b8-bbe2-59a7f308aa0d | -10.49136 | -44.92623 | 2025-12-21 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d1c993-bcf3-3262-89e8-42a8f53f12d9 | -9.24876 | -60.33685 | 2025-12-21 04:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd0257e2-df40-3fe9-ae9b-a2d3a3d7ada4 | -10.41727 | -38.03137 | 2025-12-21 04:31:00 | NPP-375D | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 035c864a-3f48-3d3e-8e23-333ed2fd7ced | -12.22044 | -42.44753 | 2025-12-21 04:31:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1798367b-bfc5-3300-a4d5-4a019643132b | -11.75649 | -43.32812 | 2025-12-21 04:31:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5690b42-9817-3c17-adee-41dc13d10e5e | -10.41189 | -38.03057 | 2025-12-21 04:31:00 | NPP-375D | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da4d9686-8961-3f89-9c12-62bb7d128e57 | -10.41682 | -38.03481 | 2025-12-21 04:31:00 | NPP-375D | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc11efad-e12b-3faa-9934-44c85275faea | -14.43612 | -43.98332 | 2025-12-21 04:33:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6afda201-28e1-3184-b84c-da179136f965 | -13.3401 | -53.19362 | 2025-12-21 04:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5dde8707-3537-35e1-9f4e-68674844f774 | -13.3435 | -53.19801 | 2025-12-21 04:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 524d14b0-58ff-304d-b244-fb4800d3ac80 | -13.34415 | -53.1944 | 2025-12-21 04:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 513eaa56-ef37-33b2-b0e7-243ceb8f9535 | -21.14092 | -40.96546 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0eadb214-696a-35aa-8f7f-e19d549968fc | -17.34122 | -42.45905 | 2025-12-21 04:33:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da22af55-dea9-324e-b72d-5339e6856c11 | -21.13651 | -40.95841 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7d3708cc-ad52-3e38-a583-f09e316f3a55 | -14.43995 | -43.98389 | 2025-12-21 04:33:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8d3ae8e-bd46-344e-b152-6aeca6c72bad | -21.13581 | -40.96486 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 697145ac-ee2d-39d4-8820-61534990047d | -17.34112 | -42.46148 | 2025-12-21 04:33:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b7c6188-b783-3800-8595-b42ef16972ef | -21.14127 | -40.96226 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0b569d33-8621-3ab0-a26e-b2a78972f7ec | -17.74957 | -46.49015 | 2025-12-21 04:33:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0955cb97-0f41-3b2a-801b-e554fe291688 | -21.13893 | -40.96021 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c0f9432d-b1ec-3691-b368-60aed1df7ded | -21.13616 | -40.96167 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f326d468-023d-3e4d-aa3a-baf6d595cd09 | -21.1386 | -40.96345 | 2025-12-21 04:33:00 | NPP-375D | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 39a68755-482a-3d78-84ab-8e38b35dde7d | -13.7227 | -44.3754 | 2025-12-21 04:33:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccf68a9c-9676-31ab-a99f-cf5e6a39064a | -21.34561 | -49.21965 | 2025-12-21 04:36:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fae8224a-a91c-30d4-ad7b-d533dcb71b57 | -25.46927 | -51.28982 | 2025-12-21 04:36:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6fd8dc1a-e514-3b9b-942f-7b4a471efcc5 | -20.63684 | -51.67901 | 2025-12-21 04:36:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 95eaf917-2140-38b3-b471-d09ab033d7ed | -30.17219 | -51.11261 | 2025-12-21 04:38:00 | NPP-375D | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 8663dcfa-8dba-356b-b7a1-97c9658551f8 | -29.22689 | -50.88502 | 2025-12-21 04:38:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 543fa083-7b92-3e89-a384-5dd9cfa9d7c6 | -9.7254 | -60.2071 | 2025-12-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1cf5b058-e25c-3df5-810d-6e0d751dee15 | -9.7254 | -60.2071 | 2025-12-21 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fccc90f7-a89c-3746-be04-e188664127a5 | 0.46858 | -60.41873 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbc02792-ca32-3bc2-a765-5b8e471d6374 | 3.5023 | -60.89628 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd90b8e1-071e-348a-8b82-209d5662806d | 0.46017 | -60.41741 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4fe8f88-f8d3-3a79-a721-eedfbcbfb5e1 | 3.31577 | -60.67339 | 2025-12-21 04:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df89097f-3dba-35fa-a653-3e652b661f77 | 3.50749 | -60.89127 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f72329f-9bd2-33eb-9ec4-ffe21c87ced8 | -1.28802 | -53.05094 | 2025-12-21 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962ca109-9f9c-3614-9c4a-9284c9ff7a48 | 3.49651 | -60.89722 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f93ade3-117d-3470-aaa1-2eaf79bfaf0b | 3.50688 | -60.88718 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20fa2d4d-7c49-3cbb-a88a-ed8ad375f97c | 3.37775 | -60.13426 | 2025-12-21 04:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d98a0809-2926-3b9b-a7cb-b2e6b737aa12 | 2.72456 | -60.39848 | 2025-12-21 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a52119bb-9f1b-3285-a531-0501a8877acc | 0.46319 | -60.41954 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9e692b9-71f1-308c-9562-cfab4c825ac0 | 3.50169 | -60.89218 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27b9f7a2-bf4f-3854-b0c3-1d7494a8b02a | 0.46265 | -60.41615 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 746c7182-a177-3842-b5e2-5cc2458871f7 | 3.50049 | -60.88407 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4a564c0-d7c1-35d6-a313-293c120d8cce | 0.46659 | -60.42339 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06952e46-6b88-3395-8b3d-b28c3a4fd2ba | 2.72399 | -60.39481 | 2025-12-21 04:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a72a637f-046f-33d6-be49-ba9aedfc3d8b | 0.46069 | -60.4208 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c0e69d-981d-33b6-a23a-03a1131fbb6f | 0.46555 | -60.41655 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fb44ac5-7a1f-3679-ba92-3e819ea0ad65 | 3.50109 | -60.8881 | 2025-12-21 04:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81c524cb-d179-34ac-9dd3-4893e01d19fe | 0.46606 | -60.41996 | 2025-12-21 04:50:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23d46f3a-ea04-3f27-a547-d66fc2ecaa19 | 3.37829 | -60.13789 | 2025-12-21 04:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 130b2df4-af85-3fd8-a3d2-f9a6e5ac8220 | -13.34228 | -53.19471 | 2025-12-21 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 627a64bb-598b-3b01-b59b-205d7bd0e209 | -9.56585 | -44.59792 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0389147-9854-35a8-aadd-edf00828e793 | -9.56985 | -44.608 | 2025-12-21 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1edf0939-4b09-33ee-b15c-fba9bd58a859 | -4.81157 | -42.21183 | 2025-12-21 04:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9fc9d437-2ecb-39c0-9afc-3797d6264e87 | -13.34563 | -53.19524 | 2025-12-21 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0fb3d25-2b20-3c0b-889b-4361a33d6917 | -1.45881 | -53.38871 | 2025-12-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13913cb-c5c7-37c5-9db9-424c70adc737 | -14.43596 | -43.98475 | 2025-12-21 04:53:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f33b9ce-a1cb-3e1b-87d5-0ff41b2f1bc6 | -4.811 | -42.21576 | 2025-12-21 04:53:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README5.md)
