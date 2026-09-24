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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b489115-076c-3809-9205-475805a2ef11 | -11.41195 | -47.35864 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a75f1443-136c-3781-9805-46f52d8519be | -10.08562 | -46.01434 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9004d19b-8286-3aab-a6ba-6b88709c0c20 | -11.40348 | -47.36156 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af528715-40fc-3420-b01b-b950366ae061 | -11.69367 | -43.43923 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 148090b6-f54d-3ec3-865d-b1173440190c | -11.68336 | -41.4551 | 2026-09-24 04:10:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5381eb54-cbe5-348b-97e3-1c5e531d328a | -13.95617 | -42.51297 | 2026-09-24 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a477a3c-cf06-37af-a7cb-e50a13ffa5f3 | -12.42126 | -46.96275 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28537c69-e132-3b83-9bba-a0a4f4776004 | -13.07267 | -43.28199 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5041350-6351-3622-b93a-8d57618babb5 | -10.43365 | -46.26991 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 960e9278-77e7-33ee-8ae7-2f4183ad7560 | -10.20321 | -44.16094 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f52772d-29ae-359e-80ce-ce8bc12f2a88 | -12.05998 | -50.30238 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ea94611-1431-31d1-8d84-242cd11622a4 | -12.16817 | -47.37441 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 015fead8-5a9a-3750-8d16-f00c970404e7 | -10.71703 | -48.73491 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e20a0ce-4003-3ff4-b302-a7fb188877c0 | -11.91784 | -50.73578 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 384d647d-68f6-3aa8-a3fb-f5e1c095928b | -14.70506 | -45.58824 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1d6988f-f30d-3b68-953c-330c3e39f857 | -14.56065 | -54.11475 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9464a431-41db-3482-a712-717214043c0b | -10.28096 | -49.96778 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d44ee6fb-546b-3370-b501-75ea33258d6b | -11.36594 | -43.38209 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba92edc3-7af6-3508-bac8-e5a4376ac25e | -10.21629 | -44.14431 | 2026-09-24 04:10:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 954ff951-ed98-3b22-9214-905d34be7b21 | -10.4381 | -46.26597 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b69ea8af-a6d1-392b-95e0-e1919d89e23f | -11.45643 | -47.40161 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6aaab92a-4783-3b58-ac14-4cf1c5ca00db | -11.34606 | -43.4005 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a230276-afe9-32a6-a49e-a699e93cdbac | -10.08803 | -46.04456 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6226b795-ff72-3681-a530-e721f52c58de | -13.92153 | -46.9094 | 2026-09-24 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aac5a151-70fa-32e2-9e74-8c1f1167790e | -11.93257 | -38.29065 | 2026-09-24 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e8c8af2b-e37b-315a-a153-e5b140f005cc | -12.15852 | -50.7698 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcecaf23-3143-305f-99bb-23793ab064c3 | -10.11529 | -50.19904 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5b7e3e9-809a-3c55-8f84-841b4eb0e3da | -12.92776 | -50.91111 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9e8549e-b7bd-37a5-b370-30e6ae060a04 | -10.07984 | -46.02668 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89191ad0-8565-34bb-8d40-52354285df5a | -11.6616 | -43.49183 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fd1b0e8b-a3ef-31a6-a1a6-ec8f4f4c3e38 | -14.57022 | -54.13633 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3b5c25a-4f9d-3a36-993f-86282efd6585 | -11.58426 | -47.73826 | 2026-09-24 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 811b0ca6-0847-3074-88a8-922b9fcb642d | -10.24195 | -49.98421 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8264ef8-71af-372d-bc07-743b9b6f34a0 | -11.26349 | -45.37955 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 742db681-340d-3852-a924-bdf38cc9c475 | -11.48848 | -47.33997 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1849c9a-26d7-3ad8-ac30-25c4f5a2f654 | -12.14342 | -50.71796 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1bfb94d-f461-31f6-b54a-559a7180ea91 | -13.99311 | -44.06878 | 2026-09-24 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7884f998-6ace-3c27-b8e1-865fbf4f4288 | -10.4222 | -49.36875 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 836ca5fe-737a-33cc-9e46-58bcecb3ea06 | -12.41162 | -46.95164 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21940e0a-ff1d-3362-962e-e976aaba6684 | -9.98949 | -50.238 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc454500-4f79-31b1-b227-d7aa65ade7ed | -12.35051 | -48.19796 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a651cc68-b05e-3aaf-92ba-15a5c957bc43 | -10.61514 | -54.00046 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e0e975a-c502-3518-82c6-ec2407efcdcb | -12.42313 | -46.96101 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b086b1-fda4-35b0-92f0-47a0243c594a | -16.40055 | -43.32939 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3734c61-6cd1-39d9-818a-b6b810182e67 | -11.73669 | -41.30635 | 2026-09-24 04:10:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acb4efb6-b26d-337d-9836-c4469124c3ff | -10.28004 | -49.97277 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83ac6a7-fa77-36a0-9314-f1d92fdf1827 | -10.62299 | -53.99239 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7f8d042-d9d0-33c7-960e-200edeb182c3 | -10.62027 | -54.0062 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6db1807f-7930-3a1d-9b3e-3125a51f124c | -10.44716 | -45.1078 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9c9c343-774b-34de-b2e3-eda9300f36c1 | -14.57107 | -54.1322 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 991d5207-2bdf-3eb9-be97-88fa26fbfb2f | -8.60469 | -54.6034 | 2026-09-24 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f8d537-dbfd-369c-96e9-d6f0320f080e | -13.4604 | -46.28283 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2191cada-c986-368f-b0a0-564b11545a31 | -11.29316 | -51.317 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68f7e220-33cf-351c-b17d-1297fe0f703e | -10.14263 | -45.78698 | 2026-09-24 04:10:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39fcabc4-96bc-39f2-be1f-c8b503e35558 | -10.27537 | -49.97192 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d78363-ff63-3834-8d64-3b9d0edb1e3e | -10.21233 | -44.14738 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9240b656-5a78-3ea8-bc60-95dcfa753bc1 | -15.09859 | -41.95526 | 2026-09-24 04:10:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc1ef5ad-fb23-35a7-8446-f0cd883cd38d | -11.20467 | -54.12968 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f33bc6a-2ad9-317a-a9cb-246a0116e5d1 | -10.93939 | -43.83935 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae779b49-52e7-3aaf-8b77-db0f96cd158d | -11.48591 | -47.35457 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b9642c8e-d0ff-3c4b-bb07-3ae1500002b8 | -9.98425 | -50.24052 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d76a95e-6582-3291-ba8d-52da3c48c383 | -11.90031 | -45.77063 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8291ee1f-8c3d-3a1e-8925-ab5e81670e42 | -11.86305 | -49.95153 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e62858b-7dd8-3a96-9dca-53fd5d5fa324 | -13.84601 | -48.57916 | 2026-09-24 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1451c8cb-bf80-3597-bb60-d3eb9fff4eba | -12.92649 | -50.91992 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 518d9772-2d3a-3206-9f73-70945835556a | -12.14334 | -45.62045 | 2026-09-24 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd9f7318-1735-35e6-b635-539371bf8efa | -12.41984 | -46.94835 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7064cf0-9ba9-329d-ae54-61765581d242 | -11.28758 | -51.31901 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e5012e09-59ca-3722-b790-e049df3551b4 | -12.12158 | -47.37899 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e97b5055-ce79-3ea1-ac4a-b6b31cbcab74 | -10.7178 | -48.73059 | 2026-09-24 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9aa78c9-9e24-3955-9940-385ecf12a101 | -11.63399 | -50.61495 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1598d935-9a59-3948-b631-c2f0d2b76c23 | -11.69559 | -43.47202 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d7aa52e-3854-3cf6-a979-d3834f211dfc | -11.95893 | -50.7545 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01b4741e-010a-3204-9740-ecb7d074a654 | -11.39768 | -47.39502 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1e365faa-2eb8-3b74-ad72-a564e6bec8c5 | -11.13265 | -48.30885 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fa851e1-7811-359d-96ce-c088d2d90ff3 | -15.24074 | -43.2692 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e737276-d572-3f9f-a916-af4ec5b1eda6 | -12.15189 | -50.75217 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29ccab75-fd86-342a-804e-7b42b0870b4e | -10.08944 | -46.05844 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c50143f1-c014-3399-ad64-0c712a97b8ad | -12.04599 | -50.29302 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83dad4c-0271-3151-ada1-7e0b63e0e5af | -12.04412 | -50.28409 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72034d14-f877-3554-9fbb-6c0f6fdad37f | -12.1402 | -47.36222 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50cf2b97-d139-3b1b-9a82-46675cf49708 | -10.07228 | -46.00422 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76ebf246-ab88-34e4-b0c6-b4680349505b | -11.9236 | -50.73138 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f66089bb-12c1-3e4e-971c-115ca6ee2ff0 | -10.08729 | -46.04893 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 23fd9c80-7ea4-3de1-ab1f-8e505ccc4950 | -15.27266 | -44.11047 | 2026-09-24 04:10:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 91be2766-af84-3978-80a4-c8bd3cc7ed37 | -12.81537 | -44.84998 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1b8890-893d-3995-b806-14be6f345fef | -11.23389 | -51.38318 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34085193-fb8d-39c5-b21e-9f67082538cb | -14.06064 | -42.51894 | 2026-09-24 04:10:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8324b1dd-ff7a-36ff-a352-db9eb2dea121 | -12.35115 | -48.19439 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc4e4b6a-4c87-33e8-9c36-70f4981da5e7 | -12.33762 | -44.20844 | 2026-09-24 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 756c8663-4881-36e4-abd6-3ebe384ac284 | -12.19761 | -47.02091 | 2026-09-24 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 367a330c-bde9-34d4-b638-df12d25a3ef2 | -11.22774 | -51.36032 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d01a0033-b539-3139-88a5-07c98a13279d | -11.16566 | -42.83941 | 2026-09-24 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59ac0ee3-9f0e-32aa-892c-a792334bc1b7 | -11.62638 | -50.60266 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b248ba1-0e4e-3296-a322-3993446e7a2e | -11.69036 | -43.43869 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8113bc6c-7f12-35bf-b8f5-680858697cbf | -11.22831 | -51.35733 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8a286793-85b2-321e-9530-d579f37b36f2 | -12.15672 | -50.72589 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3995e2a-3eb0-35d7-876e-7a2dce7ef2d6 | -10.08077 | -46.0209 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f927fcda-738c-34c8-b08d-5bd79f34dc9b | -12.14201 | -45.6284 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce42c382-2e57-3acd-be96-79bcd12a9d65 | -15.23743 | -43.26865 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README40.md)
