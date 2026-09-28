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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5957e26f-3d6e-3d86-b73c-7b08aaa23782 | -10.80231 | -48.72209 | 2026-09-28 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93d3dc0c-f203-303e-8ca2-4b8e7df7dd53 | -8.13872 | -44.44727 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f1badbb-1ec4-34f5-9b7b-d9c925f68a9f | -8.02614 | -54.88729 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee7842fc-f83d-37dc-b27e-2a95b31150e6 | -11.69937 | -50.60171 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9397ed0a-c9d8-3f99-a5b1-a7f6b67558c7 | -11.13229 | -50.06311 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 99f28448-0403-3487-890a-763faa164e77 | -12.86787 | -44.80582 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c4b0306-1e91-342f-8d5d-5a56ca11625d | -11.68836 | -44.53494 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8c9706a-e772-3e12-acf0-2bcefd1070ff | -6.67947 | -55.05013 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb062207-20e0-3e8a-83ae-9927fdfdcd24 | -10.70681 | -50.47208 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ec74d56-aa49-3af2-a10e-67acdb17eaef | -11.84215 | -50.49877 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c03f3b70-9adb-3646-8394-540e2486bf59 | -11.4438 | -44.9165 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc8d0c38-1f20-35af-9970-2f43efdceff0 | -12.62687 | -47.2723 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 490d3058-44c1-378e-8f36-69eedc4bbc65 | -9.273 | -48.67075 | 2026-09-28 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75f20d60-a079-3140-9af1-5ead5c50725a | -8.05229 | -48.46891 | 2026-09-28 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6156e99-4100-3bbf-b890-611a6f35a9c5 | -11.35903 | -47.43511 | 2026-09-28 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c478c818-bb45-366e-ad90-a367cc664be8 | -11.47516 | -46.848 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fecd3c02-f289-31a7-938a-b95f6a7cf5a0 | -11.10909 | -51.33727 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 13e8162b-ad7d-360d-9749-f5b0f127e9bc | -11.17292 | -45.1398 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50ff07f8-925f-3b5c-b7f8-bc2f59c5932b | -8.33328 | -45.4129 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77917da1-af2c-36f8-9aa8-2e51d8bc025f | -8.36186 | -45.46784 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11191ae5-687b-36e2-9054-6486df284d25 | -13.1049 | -47.40615 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48eb97d9-065a-3f3c-a426-8dee2560cd1d | -12.6247 | -47.31132 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2fa18ee3-a9eb-3136-a955-5f14d6f6c8e5 | -12.83877 | -43.39897 | 2026-09-28 04:34:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 029bbfc2-8698-3738-988b-e2d01f85efea | -7.38231 | -47.01897 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010eab8f-3437-3ce4-be35-0b7577da8609 | -8.00119 | -39.70225 | 2026-09-28 04:34:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b65abb8-669d-36a7-a463-e43034178a96 | -12.25896 | -53.99522 | 2026-09-28 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52fc1781-bf8e-3ccd-b8de-3990bb9688bb | -8.36191 | -45.44258 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 451747e4-6d3c-3c1a-b54d-451fbd6bee0e | -7.69447 | -54.7642 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f720f79-807f-3e60-a49b-fd4150590b2a | -9.14156 | -47.98249 | 2026-09-28 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 586bf3a0-92ce-3e9b-a4c9-4ccb56261501 | -6.70112 | -45.58903 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 965b7f36-8953-3da6-9395-bc6186aaa78d | -10.70975 | -44.42863 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ad478c2-6e5a-3ab6-8363-a69ac061a454 | -9.7939 | -44.82931 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15833931-e28d-3dcc-b349-7a8ec1ded6dc | -6.69242 | -45.976 | 2026-09-28 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3f728b2-f57c-3711-9cae-5acb2a4e6e32 | -9.44582 | -47.70524 | 2026-09-28 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05aeb27-f273-382b-bf32-b3c249d6ea13 | -11.33914 | -54.11032 | 2026-09-28 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12828029-25fe-3194-a477-17d04455787a | -7.68988 | -44.8733 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 00cbba1c-8726-318b-9597-f9cf23b903f8 | -12.6223 | -47.27947 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca4d670c-ca73-3baa-92d5-dcf284bc7293 | -7.26582 | -45.34363 | 2026-09-28 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d1e2af8-54f9-3927-99f8-72f20940882c | -10.25066 | -44.61216 | 2026-09-28 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6ff7f34-206f-39c7-8aac-4a81e71731cd | -9.13892 | -45.62291 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57c3799f-34ce-3910-a8bd-1c3433229f46 | -11.69622 | -44.53609 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39be9b7a-f8b4-3d54-8912-1904a233d17f | -6.66166 | -55.10044 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecb13f7b-66a8-3ba9-8e24-cbe1fb226d29 | -9.77498 | -48.2187 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0c4b177-3d77-3023-8ea5-25675518c939 | -12.15375 | -50.35874 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bd7993e8-46fc-335f-9997-ed6d25345aa5 | -6.69069 | -45.65885 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39999b60-6d19-36bf-b9e7-d186594ad3fa | -7.3466 | -42.0759 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 600385cc-ceca-3961-afba-27b87e415e48 | -8.3604 | -46.79466 | 2026-09-28 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52e36d8c-45c2-36f5-9f5e-d026f832c958 | -8.59982 | -54.65046 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08717354-608e-39b7-aa43-1cafe21ab822 | -12.15042 | -50.35819 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b4189975-5189-380c-b57d-6d9ad245a2c8 | -11.85945 | -47.08889 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ced1e255-290f-36ce-9eb2-92e155c09b5d | -7.49241 | -46.08514 | 2026-09-28 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91ecfba0-8ef2-37ca-a4f0-84e80b731a71 | -11.78468 | -48.3252 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec9713df-45e6-3bdb-9dbf-000dbef7e91b | -12.68954 | -47.32535 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18d9aac6-0bea-31f6-96f2-8f83efc1bb7e | -9.98711 | -50.13994 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d30d586-de40-3569-b7de-6f8b0ace4835 | -11.18214 | -44.80305 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bd260e6-0a6c-384a-b138-0415d14b1a64 | -7.87083 | -61.18813 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0cfa659-bf45-30e3-9c24-31e0faf602e4 | -12.168 | -50.39779 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7de98bec-7acb-3fc2-ace6-ab5c64572144 | -9.3249 | -45.38118 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f491b3d4-6de2-37df-af34-d24efe8cd588 | -9.19544 | -45.85043 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 200d5500-62aa-3feb-bd46-8fc8c448e41b | -10.57353 | -51.28132 | 2026-09-28 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1445f146-576d-30a6-96ff-27ba5b8bd823 | -11.33853 | -54.11382 | 2026-09-28 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 221b3379-e833-3f8d-9f02-f1e3992b5e04 | -11.11033 | -51.3296 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78b7fda9-e625-3025-93cc-babba6ec845f | -6.66545 | -55.10594 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df3ec6f6-28fb-3f42-b1a6-6c5700264a85 | -11.07779 | -51.39922 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 593f547b-b948-3fcd-b5a0-dd39af36fcb4 | -9.09181 | -49.8814 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78b3030a-fe4b-3722-b92f-cf948dbe1dcd | -11.37652 | -47.43436 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb907c6e-8e05-31ec-9564-2a77c29533d4 | -11.78692 | -48.33284 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a5570e4-1099-388c-9ab5-b0254a7dad2f | -8.43793 | -44.8703 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd45ace7-f713-37da-af46-fa59524d8c8b | -11.90973 | -47.00549 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be4401b1-ee42-397d-b224-75abfeddf50c | -11.69799 | -44.55193 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eea7160-8fc8-3653-b8af-4fab52f299b6 | -7.35154 | -42.07233 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8efee656-3561-34b7-9ca1-9698eefdc232 | -8.94557 | -45.90112 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 317d481f-ec8c-3970-b949-eaddde520eff | -6.65709 | -55.09962 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88a27514-cf78-381b-a067-3cdf1980b18f | -12.73956 | -47.29273 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9df3a206-65ee-389e-9050-4d6cb827279d | -10.11046 | -50.19339 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab43e64c-ff44-3d79-b597-c1d4672506d4 | -6.69882 | -45.65215 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b14fef60-9694-35c8-91d7-8fa5e54efae8 | -10.22725 | -49.99923 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 620756b7-08d0-3ec7-9e4a-3e031c565335 | -11.29936 | -49.93364 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5731f59-f2f7-313b-b5e5-6d763bf3bbc7 | -8.73398 | -47.97955 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05fe3981-3013-3cfc-8af3-1fc15bdc9e91 | -7.8601 | -61.1876 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8968e023-6146-3a43-ac67-1b0e36c14fdf | -10.26222 | -44.61348 | 2026-09-28 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6317487e-4918-339a-ac30-1506993bfe7e | -10.57601 | -51.28162 | 2026-09-28 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 401aa1da-acf3-3526-8190-cb97154bd034 | -7.69008 | -54.76341 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aec6ff1-35ec-3e91-9c35-66e822341e6b | -6.72501 | -45.59664 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 545b4ccf-6a7a-3d61-90f9-8df568559cda | -7.38566 | -47.01948 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 482e9d3b-af65-32a9-9696-ed96ebd5f03b | -12.63834 | -47.26621 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76f5619f-4640-3fd7-84f8-6445c53f5a00 | -10.89256 | -50.68221 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 323ebe26-2345-39b1-a8b7-7720586bc908 | -7.82644 | -55.13037 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff3f509d-5364-3f86-b6d2-c8a09de405ae | -6.18953 | -44.1177 | 2026-09-28 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 691275ca-6a94-3dfc-a03a-28548c0e354f | -10.16607 | -46.57797 | 2026-09-28 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 795cfc67-65a2-35ac-83fd-08c56b2eed30 | -11.13342 | -50.05601 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a811a0a0-e2d0-36b1-83da-48cd8be2a394 | -6.30513 | -56.0358 | 2026-09-28 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a5f8fb5-f56e-3de9-aa10-c03597941b3c | -12.16743 | -50.40137 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 65a05cf2-cb81-3164-8812-1a49d8263b58 | -12.17295 | -50.40963 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0984f51-6d6d-379d-b9b8-fcd3eacfa50f | -8.25652 | -54.78745 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eda07b4-438c-38f8-add7-3a0c15af459c | -12.68897 | -47.32918 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49914405-44ed-3675-a619-73fbd79ffa06 | -9.98768 | -50.13634 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e4840e88-dbe6-3d22-bcec-9a7b1679bf52 | -11.6957 | -50.64582 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae2cdde7-687c-31e3-82d8-2956f731bd94 | -7.05828 | -55.4794 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3366c5d4-621b-33d9-8c10-b674733e554f | -6.735 | -55.08559 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
