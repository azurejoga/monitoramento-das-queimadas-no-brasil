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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae8157f0-a99d-300e-bf97-f29a6c792086 | -8.5823 | -54.745499 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8481b9d3-30d0-30e9-8978-6a4a517ef259 | -8.5387 | -54.872101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2d5b733-e3f6-39ad-9e8d-4833d55ccee8 | -13.5655 | -51.672798 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e5037ea-7c95-3288-b94c-b352f2a832a7 | -9.2085 | -59.778099 | 2026-08-20 01:02:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b16bc53-ca93-3dcf-b361-b0578604de43 | -8.5658 | -54.763802 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71545561-8ac8-32c4-a23b-0451c63c322b | -8.5348 | -54.763401 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd89f9b-6a85-36ac-b4d0-5b430bf60a4a | -2.6455 | -47.983398 | 2026-08-20 01:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99ee1367-7908-3db8-a67a-488a9a0f2ee6 | -12.2533 | -43.1544 | 2026-08-20 01:02:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e3d35d45-cc33-3c97-ac70-f22b76e09ab4 | -10.2477 | -54.3643 | 2026-08-20 01:02:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f423376-a9c8-383b-9474-0827529c7a7d | -8.5764 | -54.673901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50748cc4-bc7e-329a-a8f8-5fe23c4db629 | -8.5645 | -55.308701 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c382563-faa3-3d6b-9098-685b8703c6b7 | -8.2809 | -62.884602 | 2026-08-20 01:02:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7420cc-b477-3a1d-afd7-f892eada39b1 | -14.5265 | -53.3255 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb413a62-f0a0-37d3-a8c9-182e900a2fca | -8.6616 | -54.640301 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a96b2a5-dac0-35fc-9480-2cde1433c39b | -9.1119 | -61.605 | 2026-08-20 01:02:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2cd00e9-d8be-35e7-8c97-a502289ad349 | -11.8095 | -44.802299 | 2026-08-20 01:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 900253ca-d267-33d7-963c-cf1ecb85fa77 | -6.4361 | -52.712101 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df452e0a-a3d6-378a-b135-22d357ca3029 | -5.4198 | -49.226299 | 2026-08-20 01:02:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c0a45f-8e50-3647-91d9-9d91d792300b | -8.5563 | -55.317902 | 2026-08-20 01:02:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f518ee1-9492-3605-96e7-98e47136d178 | -7.7579 | -49.2145 | 2026-08-20 01:02:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| dbcba388-cd37-3504-b89d-62f90af8787b | -7.7651 | -49.201599 | 2026-08-20 01:02:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8f92519d-892b-3f8e-b95d-cd87db749ec6 | -14.1799 | -53.0639 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a729ded-b3c9-3026-aa26-b061c81bc8c0 | -6.428 | -52.721699 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc23f8d-1ffc-3758-9ead-d7030e251ec1 | -8.578 | -54.680901 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 346e774d-466c-3310-b0ba-b47472a6f4a2 | -4.1227 | -49.445499 | 2026-08-20 01:02:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f739971-e32b-309c-8de7-2b1df7cf8843 | -6.4284 | -52.767899 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673f47f5-650f-3217-b5c6-d1dcaa182ce7 | -16.506201 | -55.174801 | 2026-08-20 01:02:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c2242e0-d507-303f-9273-94070fb8bcbc | -12.4817 | -54.737801 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65d3c3ee-d30a-3617-9b87-309b7d10b2f8 | -12.7925 | -48.415001 | 2026-08-20 01:02:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8733243-9b4e-3aaf-9284-5226314277f4 | -7.3619 | -45.8354 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dd2343e-457c-382c-88ca-a6f9ff923b79 | -14.2155 | -52.900501 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 571ccf4b-5576-3fc4-9fb9-027923d341a8 | -11.3121 | -45.195801 | 2026-08-20 01:02:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04625e60-6fef-3933-b74d-268561c16a5b | -5.7999 | -55.701199 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc0073e-f7d5-3c9b-8d87-642ccd4faff0 | -14.1548 | -52.9515 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd1b87b1-6d23-396e-b9d9-6cd558612883 | -10.1051 | -54.279301 | 2026-08-20 01:02:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33d1f115-970c-3b64-b2d8-57195dde4c16 | -6.918 | -59.348 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f770ed9-e2b6-3d89-928b-f8b942766b56 | -6.6844 | -56.152802 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ec25e3-5662-3f39-8b7d-d77917966997 | -8.5478 | -54.775101 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e0967f-e757-3d54-8300-6b8ca4f61ea5 | -12.009 | -53.445202 | 2026-08-20 01:02:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8b4c315-e205-3f99-b0ad-af0a1da4306c | -9.4544 | -51.6208 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e512865-056f-351f-a5f5-ef79c052caf1 | -2.5643 | -47.252998 | 2026-08-20 01:02:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9e46f4-7174-3388-a612-faabe2e7c621 | -2.574 | -47.250702 | 2026-08-20 01:02:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c07d9acc-35e0-3cb9-8029-0557a567935d | -2.1693 | -47.487999 | 2026-08-20 01:02:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 879934f1-cf99-3fdc-96bc-40c4648b9e4c | -9.1086 | -61.589199 | 2026-08-20 01:02:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 528f105d-daf8-3902-a9d8-23fe48ff1c22 | -18.5602 | -48.287601 | 2026-08-20 01:02:00 | METOP-C | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8632662d-067b-3f6f-843f-77a94471cdd8 | -6.8672 | -59.020901 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5270799d-56ab-3075-b8bf-0eafcc4444cd | -20.8953 | -50.503502 | 2026-08-20 01:02:00 | METOP-C | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b89870a5-a173-3209-926f-9f48ceba5216 | -11.8192 | -44.799702 | 2026-08-20 01:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f76b03bb-e106-34be-9b45-d87cb8353ab8 | -13.5753 | -51.670502 | 2026-08-20 01:02:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf42cdd8-e51e-39a3-ac0d-2da750503276 | -8.5854 | -54.759399 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc9fd29-3ea8-39c2-bbc1-d1fb8b786caa | -10.7976 | -50.3064 | 2026-08-20 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdd9a2d8-c709-3012-8591-22d032a2ae45 | -9.4236 | -60.413601 | 2026-08-20 01:02:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 895e4d82-9a59-308d-aeb5-cfde415b111c | -6.8097 | -58.9921 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bab7585-ad5b-3430-a21b-e3e008dc59ba | -7.9568 | -44.647701 | 2026-08-20 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1e4c999-39f7-3090-918a-f225d59e0aba | -6.9538 | -52.808399 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfbf8654-921b-3191-a37f-cb136d1308ea | -11.8049 | -44.784401 | 2026-08-20 01:02:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c13c3ee-bea5-3223-9a85-b1c621fafb8b | -8.574 | -54.754601 | 2026-08-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f558f3d-ddc0-35c0-b5dc-7ed3ec567789 | -6.4378 | -52.719501 | 2026-08-20 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07926a2d-f034-3b60-b762-c986c0da0a3e | -7.3477 | -45.819801 | 2026-08-20 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17d5b06c-8bff-306a-a7dc-86926bb6af62 | -7.6017 | -45.152802 | 2026-08-20 01:02:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0ed29ee-2296-3e8f-a56a-490fd6c40055 | -4.9028 | -46.824799 | 2026-08-20 01:02:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 433fa1e0-c0c6-306a-bebd-286ea3ab0d10 | -1.8397 | -54.4772 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc1a2bdb-3bc1-36e2-a71b-a385fe08d369 | -14.1701 | -53.0662 | 2026-08-20 01:02:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66d43a9e-4431-3a71-b80d-ef5424fc8ca0 | -12.4703 | -54.7327 | 2026-08-20 01:02:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89187cc9-1d2f-36f7-8386-a481929109ba | -6.8316 | -56.442501 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37104d53-d186-3f23-a52d-f232ae0f4e4b | -7.7626 | -49.191002 | 2026-08-20 01:02:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 362b192b-4532-349e-97e2-5d072b0629db | -6.6968 | -58.944901 | 2026-08-20 01:02:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 634a63e3-2301-3d17-87f2-68fb0b0e1bdf | -11.2251 | -55.056301 | 2026-08-20 01:02:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a4be3a1-7ae4-3b8f-88b2-420a9c8c3ba8 | -6.8806 | -56.431702 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36012b0b-28b0-3808-9c3f-93f13c9c30ea | -6.6015 | -58.9651 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a68c83dc-6348-33f7-aea6-47c0c3528850 | -23.0831 | -49.1746 | 2026-08-20 01:10:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f2ff26c5-693c-35fe-b42d-293c80a0ffd4 | -6.3863 | -54.9451 | 2026-08-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 83d99511-3abe-3e15-a0f0-c1821ecdc03b | -11.2189 | -55.0585 | 2026-08-20 01:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ea00475c-b994-3e6d-b813-25a972ae1e82 | -6.7123 | -58.9412 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d3492262-86e8-3f03-bb1e-8fc56dbbaa1e | -11.1939 | -53.9993 | 2026-08-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a783f795-c9ee-373d-bc47-c1d53d2cc415 | -17.3372 | -43.6139 | 2026-08-20 01:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 83db2b86-717c-36e9-9446-c3bb87eced12 | -9.4071 | -60.417 | 2026-08-20 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| ec83972b-898c-36f5-9474-36f992d5d650 | -6.4391 | -52.7343 | 2026-08-20 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 76bf484b-3cf2-30ff-8944-263d4534ccea | -7.3413 | -45.8377 | 2026-08-20 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 91ed2d5f-85af-3b05-bc4e-bd663680f9c2 | -17.3365 | -43.6383 | 2026-08-20 01:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 88df1fec-a8a7-37b5-92a7-adfad84a20f8 | -11.1936 | -54.0199 | 2026-08-20 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 96cfb0e3-f799-3d69-a583-3760064c683a | -2.5629 | -47.2445 | 2026-08-20 01:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2bb1c3d4-2234-30e0-a08c-2009639901ed | -6.583 | -58.9658 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4912a6cd-5db4-3720-ad53-6da59ed816b3 | -9.207 | -59.7903 | 2026-08-20 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0351c831-fab9-34fd-ba02-d4b3475e9af2 | -11.8275 | -44.8044 | 2026-08-20 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| dffbe051-82d1-38f4-8184-e4d7d0cad785 | -8.654 | -54.6505 | 2026-08-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 20780cab-b276-33a6-8843-cc311b655f77 | -7.3415 | -45.8152 | 2026-08-20 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 270.7 |
| 978b31b1-8a88-3504-af54-dd664e4f7f58 | -7.9751 | -44.6648 | 2026-08-20 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d773085a-8e32-337d-9c63-04c78cc186c9 | -9.2258 | -59.77 | 2026-08-20 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 51211ef3-40bc-3e2a-b548-e76cd5d9c530 | -17.3172 | -43.6186 | 2026-08-20 01:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1feba0ae-4404-3fb5-8e07-e2a3721a9156 | -7.6115 | -45.1799 | 2026-08-20 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fab39f5d-c1f2-3d51-9a1e-890ad8b55129 | -5.8087 | -55.7293 | 2026-08-20 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 019295e7-3f07-3fce-97bb-48c14ddf19fb | -5.7904 | -55.7103 | 2026-08-20 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| bad1be4c-7217-384d-81dc-71716124ac67 | -11.8083 | -44.8072 | 2026-08-20 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| da10536e-e179-3bd7-ae4e-33d54898d168 | -6.6938 | -58.942 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 14e2fa39-5700-3e50-812c-536bcb6009b5 | -8.6727 | -54.6492 | 2026-08-20 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 0e97d8bb-f13f-36bb-b394-5e9c84771cae | -6.7114 | -59.0958 | 2026-08-20 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e2668122-ec79-313c-a8b2-914e51708b61 | -7.3603 | -45.8136 | 2026-08-20 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 315.6 |
| bb9f4fd8-0dd1-3d3f-b857-980fceb94702 | -9.2071 | -59.771 | 2026-08-20 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c600a57c-09bb-396f-ae56-4f0a44e957f7 | -9.2256 | -59.7894 | 2026-08-20 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |


[Clique aqui para ver as próximas entradas](README18.md)
