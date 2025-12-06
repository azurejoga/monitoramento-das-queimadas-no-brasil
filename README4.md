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
| dbbbd67f-114e-37e6-af55-2328f8e33d2d | -2.58797 | -45.54747 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c846c88-8959-3cfa-b8e9-9f1cc8714eb6 | -1.80603 | -45.94368 | 2025-12-06 04:10:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18c92653-3c3e-3b56-beb7-2a56aa9fd910 | -1.47869 | -45.58108 | 2025-12-06 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ae87a66-0c9c-397a-ae54-2d9cf15ba90c | 3.51023 | -51.25328 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8586a723-ad1e-3cb7-8fcf-d683d6aecebb | -2.35164 | -45.75284 | 2025-12-06 04:10:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7171ee22-79a0-31a8-8bcd-6aa85814f949 | 3.50458 | -51.25951 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a455898d-4c9b-3ab6-b91b-9eba06c48302 | -4.54479 | -38.33336 | 2025-12-06 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e36b71b-2bc6-33ac-8b2c-646463a92d5d | -2.77737 | -45.50866 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c51e16a-2ae1-300e-82ce-addd4bbb2521 | -3.23707 | -43.34956 | 2025-12-06 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9001c18-07c0-3135-920a-dbf3e6d829a9 | -2.27961 | -47.94092 | 2025-12-06 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f650557a-4c2b-32a3-9a75-6bfd00c4ac64 | -2.23144 | -45.59608 | 2025-12-06 04:10:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 240d62b4-d6ba-3278-82ea-16ebfd0169e6 | -1.4822 | -45.58532 | 2025-12-06 04:10:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70066804-efd2-38b4-963c-27e9a4f60d46 | 3.50534 | -51.26476 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82e5c38a-8328-3b79-90a2-3ae8e61144ac | 3.50381 | -51.25425 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08583cf6-f808-3c35-8b48-2cede4756936 | 3.41305 | -51.26589 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 216dee19-f3bc-303a-bda7-181d66550b47 | -3.17672 | -39.56108 | 2025-12-06 04:10:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 938fc29b-eaee-3418-bdfb-68e0d64db722 | 1.69627 | -50.8504 | 2025-12-06 04:10:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a63c9ba-3cfa-3041-85fa-7890b0e94f58 | -2.10988 | -53.58107 | 2025-12-06 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ceb6eb-abac-38e6-9f86-2137c8bbd3b7 | -2.02669 | -46.49809 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6a76b4a-7395-3346-9641-47f860b6336b | -5.36464 | -36.84206 | 2025-12-06 04:10:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d4930e0-bb0c-32d2-8cac-2352ae8d490f | -2.43861 | -47.1937 | 2025-12-06 04:10:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35b45637-2979-39ad-b496-f92d4e181c78 | -2.2965 | -45.78856 | 2025-12-06 04:10:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9330e34a-74b6-3677-b55c-d44d63ca297f | -2.02123 | -46.27051 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a2f337c-59a6-3333-b0cc-1319d1ce6ae5 | -2.68216 | -45.97227 | 2025-12-06 04:10:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1055924c-24a9-3583-8443-3f4ff8e805d2 | -2.99487 | -45.58579 | 2025-12-06 04:10:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb27ab3d-4f09-3f38-9752-105b3c7c18ba | -4.07248 | -43.83154 | 2025-12-06 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c5fe6be-8c04-3598-9945-e72937d9c139 | -2.16845 | -47.87471 | 2025-12-06 04:10:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 461f9cd3-0e05-3540-a9a0-7a5639c4c53a | 0.43227 | -50.92653 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 363c3737-2f76-3e2b-b61e-eb02242467b7 | -1.85542 | -45.58598 | 2025-12-06 04:10:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97b0c10f-e8ad-3981-9ec8-93fcc5d471a6 | 0.43136 | -50.92834 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9151d657-373a-3cb2-b314-14d5faff9949 | 0.44265 | -50.92182 | 2025-12-06 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0062cee-1166-3028-9739-195e0c6bc2b6 | -2.02546 | -46.27116 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2659508a-0db3-33f4-b0a7-ac5cbd1fe2a0 | -2.41142 | -46.47475 | 2025-12-06 04:10:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b07b45b-7da8-36e4-8bc2-f8f91d11038c | -2.7686 | -45.51247 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a2bf0ed-a243-379d-86f8-2e1862036b3a | -3.87777 | -41.5905 | 2025-12-06 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0f1723b7-b337-3bb3-b274-84835b04a004 | 3.48944 | -51.2457 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c71eeaee-46de-3a40-9153-9dc918f6370e | -2.77258 | -45.51311 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e43d418-eef6-30f4-a6c6-f04e276e3482 | -2.76778 | -45.51758 | 2025-12-06 04:10:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2aec1dda-5ea7-3096-9a15-30462f5582a4 | -3.47321 | -43.88342 | 2025-12-06 04:10:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3c34c2f-d663-3008-8253-98804c2f5ea4 | -4.16478 | -39.25172 | 2025-12-06 04:10:00 | NPP-375D | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f28456a-cfb3-372b-b773-549eebb37b09 | -2.23199 | -45.59259 | 2025-12-06 04:10:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbcd0c6f-d8a9-3825-ad5e-f550b27dd004 | -3.97694 | -40.92278 | 2025-12-06 04:10:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f761c885-9ebd-3aa2-9cf1-112f1bed129b | 3.42511 | -51.25869 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d735e96a-3fa1-3927-b1c5-118cfdfcdbe1 | -2.02239 | -46.49745 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10ea4b54-051f-3fd0-aafc-12342fe4b2b6 | -4.54417 | -38.33738 | 2025-12-06 04:10:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d9563ff0-4e30-3512-a29d-ada36722c2c8 | -3.59479 | -40.90123 | 2025-12-06 04:10:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 48203a67-c521-3db0-a46a-40b0c45e0728 | -3.87665 | -41.57608 | 2025-12-06 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a39f7b7e-76a4-300d-ab00-76aadaf04155 | -1.17562 | -46.13673 | 2025-12-06 04:10:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e332f86e-a6c7-3194-abd8-dfce7fd0c36c | 3.46846 | -51.24148 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7ae2887-0a49-33d4-a4f4-f3f2732d177c | 3.51177 | -51.2638 | 2025-12-06 04:10:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39354e57-00f0-3955-b1e7-a1e26cde7e1b | -1.76684 | -46.45968 | 2025-12-06 04:10:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b56df7-237a-369d-8b4f-dc7de27f81b6 | -3.66269 | -43.55393 | 2025-12-06 04:10:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1cb07e4-0758-37d9-81b7-c8d1e90fbebf | -5.36413 | -36.84505 | 2025-12-06 04:10:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 324fb4c5-3c28-346f-81b6-236aa877e3a2 | -1.85946 | -45.58667 | 2025-12-06 04:10:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 675dd1d0-dc39-3ca1-9127-7b7cb2aff172 | -4.49916 | -40.50823 | 2025-12-06 04:10:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5d4f9e14-c89b-3b54-a1f3-c1fc90050b1f | -4.78173 | -44.56418 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d6f36c4-e97d-3f8d-95f8-dec5ca1a8943 | -6.57637 | -39.67429 | 2025-12-06 04:12:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 98277249-9ee9-3ff5-9f2b-e356002b1216 | -5.67424 | -39.60016 | 2025-12-06 04:12:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b949760d-758e-3093-a564-bbd44b75a2c5 | -5.7676 | -42.60192 | 2025-12-06 04:12:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76a88636-9be3-314c-b3c6-a71d7775d050 | -5.90307 | -37.82964 | 2025-12-06 04:12:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36d3401f-5a5c-3eeb-b2d1-9ffa78ad0974 | -4.907 | -44.50523 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20866e44-b3d6-3d23-8c24-e95fca828630 | -5.85847 | -39.94209 | 2025-12-06 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2f3e0ac-1518-36c4-ac80-6d68f77c4374 | -10.26141 | -37.8644 | 2025-12-06 04:12:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a118b625-4a40-3fce-9aed-f89a143888c8 | -6.57865 | -39.54401 | 2025-12-06 04:12:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f5f6097-b500-3c5e-be53-2b79b34f1a46 | -5.85508 | -39.9416 | 2025-12-06 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 754ef1cd-fc1c-3101-9009-b1e2eacb03b9 | -5.35194 | -42.11318 | 2025-12-06 04:12:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32077f23-f5f6-3e90-97d6-1f1721143d0b | -5.35472 | -42.11721 | 2025-12-06 04:12:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 218d8c21-9e15-3e69-b44c-9932ac71f9df | -5.85455 | -39.94204 | 2025-12-06 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8db377dd-9265-3713-913b-a39633f858f7 | -10.26089 | -37.86085 | 2025-12-06 04:12:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2321caad-78a4-3391-8d69-34dfc0272ff5 | -4.73538 | -44.43464 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01f55258-9a13-3551-899e-b362cb26b137 | -5.65448 | -37.79498 | 2025-12-06 04:12:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce9cf4af-ee2e-36f6-a06a-f439aeb30743 | -4.73607 | -44.43043 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fb6632d-4376-31e2-ba48-c8d3759071bf | -4.67513 | -44.50928 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a49e17fd-c511-3d3b-9a7e-4e66c6e723df | -5.90374 | -37.82526 | 2025-12-06 04:12:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fc9578d-11c1-3841-bd7a-55cc94f6d4b2 | -4.90623 | -44.50755 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38e868e0-01be-30c4-bac1-02fef2b190d4 | -5.22144 | -39.25373 | 2025-12-06 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bc1ca77-f57b-3a20-a85b-d1adafa01327 | -5.22431 | -39.25805 | 2025-12-06 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa788dbe-1dad-3077-a98a-5c134ccfe934 | -6.5307 | -39.7663 | 2025-12-06 04:12:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 753740c3-23eb-34b5-83ac-503f722929ae | -10.26482 | -37.86142 | 2025-12-06 04:12:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b7a77b39-67ab-3f49-8e46-399b399e04a0 | -4.67445 | -44.51353 | 2025-12-06 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3a89a1b-d20d-383c-9c12-8ebbb5100291 | -6.75871 | -39.80447 | 2025-12-06 04:12:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4edc2a2e-4225-3a06-9cd5-cd7f6f42cdde | -5.22086 | -39.2575 | 2025-12-06 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3baadb9c-86e7-3845-9924-c322767a2a22 | -6.53143 | -39.76693 | 2025-12-06 04:12:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d12961f4-2018-3e65-af5c-6ff13796759f | -5.85452 | -39.94523 | 2025-12-06 04:12:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0da0b8ae-eacc-30d7-b46a-de6e860c8ea7 | -6.5821 | -39.54457 | 2025-12-06 04:12:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a226b903-46c3-399e-b649-bba9125007fe | -11.65474 | -48.07935 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 325456dd-c071-36d2-80ae-0f704a3b6362 | -11.6513 | -48.07488 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5acb78aa-c4df-3881-830c-e45b6e4652cd | -11.63906 | -48.07263 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 307cd3ff-e79c-3de9-a4a0-6b78a8f8e457 | -11.63433 | -48.07558 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9374cd5a-dcd2-37f4-ba7b-c5834d338358 | -11.63971 | -48.06894 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48899161-18ce-37a0-ae5c-be0a1a2d0df0 | -10.457 | -47.32594 | 2025-12-06 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7e800d2-3bdd-300d-a79e-4bedb7d78c43 | -10.46097 | -47.32658 | 2025-12-06 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d23f5d0f-6ca9-362d-9ab2-f6ca49301120 | -10.45879 | -47.31557 | 2025-12-06 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8e019f9-ab3e-31a9-a5e6-a114507d2e78 | -10.45789 | -47.32074 | 2025-12-06 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 450dd8d4-ac5d-337f-b57c-c5ce14390588 | -11.63841 | -48.07632 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90916f81-72b4-3bc8-8def-d74b0dcc47bd | -10.46187 | -47.32141 | 2025-12-06 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a2759c7-3884-3aac-be07-1e715b0e69c1 | -11.63368 | -48.07929 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff988364-082f-3e9d-bb5d-1f8bef612154 | -11.65087 | -48.10158 | 2025-12-06 04:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b80e7092-92ee-3ef3-824d-0efcae51d05e | -20.33301 | -50.19307 | 2025-12-06 04:16:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c202720d-8d2d-38dd-bcbc-6720ed2d805d | -19.6404 | -56.83413 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |


[Clique aqui para ver as próximas entradas](README5.md)
