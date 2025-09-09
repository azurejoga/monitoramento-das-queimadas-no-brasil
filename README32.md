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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a3f522e-52e8-3551-8134-1ccd498cb214 | -9.43108 | -46.72724 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4228a34c-e056-3d87-b262-2821fd1c09ff | -13.72999 | -46.8872 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0871533-318f-308f-b66c-bfcd65d0bf32 | -10.27921 | -48.80769 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6d5951e-f35b-3b20-baf2-f72ddf725d32 | -12.1573 | -43.70811 | 2025-09-09 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a2d5c5a-8e12-308f-89c4-9d8d5d53b6d5 | -14.28823 | -45.02346 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26c61bda-47f6-305c-8b4b-ade10b36792c | -9.24195 | -57.06562 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0210441-1197-3a66-b562-3840555339f5 | -8.04325 | -48.63787 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac1f6dfb-9332-326a-8803-09b11aa95a12 | -13.04615 | -48.02856 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d1a457f-01a3-30b0-9ac8-a834ee35433e | -11.94221 | -50.96976 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 58ea447f-4efe-38f3-bebe-6d2fd2030171 | -9.95019 | -49.77109 | 2025-09-09 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea3ba99-b1bd-303f-975b-f4925af3c418 | -13.83663 | -46.23125 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc07b962-4471-3f02-ba6c-42f3c8876f70 | -11.34945 | -50.43283 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b65c67b1-de9d-32ad-959e-e9eb39a50a2d | -11.15094 | -45.26556 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cf6462e-88fe-3b88-b37a-c4389a9f68d8 | -8.128 | -44.86873 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3d9f6b7-a9b8-3eeb-b42f-5be65fb01803 | -8.49794 | -51.32594 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48a3e8b4-9883-3435-a636-1e1670cc0596 | -6.87901 | -47.90702 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| edd26a4b-c77f-3cc8-ac48-77d88353b723 | -12.19287 | -53.91337 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0488de09-fee0-338f-a4f5-d5b773199fce | -12.8196 | -47.98676 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a750f5e4-b53f-33fd-b9d1-666e550409cb | -15.02631 | -42.14696 | 2025-09-09 04:34:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 67c98d18-93fe-3489-b0ea-272e32271483 | -12.95684 | -54.75926 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 089b9976-5217-3807-976b-86d910b25771 | -8.03828 | -48.62644 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37333e99-41d5-36d2-a3cc-f76458f4a1bd | -11.83954 | -46.75929 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0f87473-4178-3d11-9c14-d6355b016a60 | -9.46525 | -60.50613 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 170d6142-3b7c-3062-8283-022ef6e314e7 | -13.33438 | -43.25032 | 2025-09-09 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 49d6724d-5003-38c9-8acf-a71d54a5b27f | -11.36996 | -50.44724 | 2025-09-09 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a5c8fd-593c-3f1f-a250-83f32bda81ea | -12.94812 | -54.76139 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0612f0f-a0b1-378e-95c5-c7b5f2312697 | -10.16883 | -46.21364 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b51a456-f6cb-3613-babb-76ea8a34ca5d | -9.85497 | -47.79217 | 2025-09-09 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03be64b7-f88b-33d8-9f6f-6cd5d1193f31 | -7.14767 | -46.06131 | 2025-09-09 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06c6f045-d87b-3f49-9312-de364611fa7f | -11.17315 | -48.37299 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ee15a45-2cf6-3abc-9b27-ad73fa342b08 | -8.04136 | -43.81277 | 2025-09-09 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02a64942-adb9-3436-8f61-da7f09d80236 | -8.09155 | -54.75736 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fa69740-8462-37e2-ae19-b6a227e3433a | -12.19203 | -53.91837 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d49c4e06-d8b7-36ad-a6d6-39ed92a0b014 | -11.44114 | -43.60764 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6c159a-aeb5-31f5-88ae-eb19b7dadf41 | -7.71975 | -45.1553 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5bfd26c-00b8-388f-8179-267e077307d6 | -9.35159 | -46.50682 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be86a36b-54af-3ee5-966d-91a728777a69 | -7.74696 | -50.31274 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11eb6220-c23e-32f0-ae27-bc3549389f70 | -8.08643 | -54.76091 | 2025-09-09 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 411cb6f4-4501-3a69-8467-14dd6b601473 | -12.1863 | -53.88154 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54f7f19e-6022-3921-9d5e-40836a561c2b | -13.2777 | -43.74438 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78f06b42-9417-38f8-9113-fddce144a4a4 | -9.80661 | -46.04298 | 2025-09-09 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 590abc58-7c79-3538-809f-e0b25cfb15ef | -7.75184 | -50.73802 | 2025-09-09 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dad03eab-47b3-3b01-8b71-f9bcd429cc73 | -8.82038 | -47.84325 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 039f0087-c583-36d7-b304-011475ff817a | -13.5515 | -48.20072 | 2025-09-09 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1833c1e-ecbc-3c9b-a44c-fee9979d105d | -10.1747 | -46.22262 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0652a216-1191-30b0-b625-45b1c736354a | -9.01411 | -49.7944 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af58899a-8f3d-3abd-9eb8-a8148ac2b11e | -8.40303 | -49.09837 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ce27fcb-dccd-3b0c-bb98-703bf07fd663 | -11.44292 | -49.26416 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1aaf864-6e22-37c6-b6cc-04888d5736b1 | -12.46576 | -48.03256 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c19f239-9168-30f6-9d8d-9d92727d04da | -8.40413 | -49.09138 | 2025-09-09 04:34:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f77dcaad-31a3-316d-919d-a4d322cb5bcf | -10.90125 | -55.70545 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 19fdfcfc-1163-3725-9b5d-ceb0cca62b81 | -11.66009 | -46.8892 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e0e1536-49b7-3f4c-a06d-ec44a0f99bd4 | -11.95117 | -50.97886 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f62c021-2be5-32d0-9c1b-b26b5b73d642 | -7.7282 | -44.73977 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad573264-2f18-3b0e-b8db-363269b1d7f6 | -9.14972 | -45.57024 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97873aca-e403-381e-ae27-c358050f1bac | -11.26425 | -59.18562 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ca5560-5a0f-3dd8-8508-40fe532700d7 | -11.39285 | -43.54303 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bc92bf6-d710-3063-8c16-08157c413718 | -12.6085 | -56.97376 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c01cdefb-f62a-3d75-a626-6fe66cb49031 | -13.81116 | -46.27724 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee31adbf-0c3b-3e7b-bc0a-f983b23323c0 | -11.68556 | -47.16299 | 2025-09-09 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec36d2a1-35aa-3140-b775-1c4990ff6bc1 | -12.95345 | -54.75489 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dd00286f-e4c4-3805-8df1-70e582347e4f | -12.63204 | -56.97803 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c29420a8-962d-3064-90cc-a2f8eed168a0 | -14.3585 | -47.31885 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0adafba6-7f82-3e06-9f32-847b30547fee | -9.55991 | -48.66404 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1e4a956-ccba-315c-98c8-8bd4ceabeca7 | -9.27868 | -56.89427 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89266904-3ecf-3762-9696-112903f51740 | -11.82567 | -46.78105 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c781ecdd-a881-3cd4-bf98-5b3a9bc86b61 | -11.85738 | -47.53717 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 020a7f22-5368-3b04-8c72-5433397844eb | -12.60947 | -56.96866 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25f2aa2d-9c66-3bb1-95f2-ff5f1163abb2 | -9.04365 | -49.80281 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 402b2859-7878-3c0a-9c47-34e1cc5701a6 | -10.88792 | -55.70289 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 569dbd53-5ec4-3db1-85bd-c5e88f54b629 | -11.42922 | -43.60192 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c59ed101-dd4d-394d-9788-04bbb049d327 | -10.29463 | -48.81728 | 2025-09-09 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff136a50-1507-3881-830f-dc4cc4f8883f | -6.86527 | -47.90842 | 2025-09-09 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb3b0dd8-4a21-3320-bf6d-2ca193eeba44 | -12.81262 | -56.51778 | 2025-09-09 04:34:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9e2ffcd-4609-3aa7-acb2-f777bedb8dad | -8.03661 | -48.61553 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb7cbb7a-90aa-3705-b299-fc38d6a6075b | -11.30891 | -46.50571 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7efc0931-a0f9-3157-b89b-88bf868562f3 | -13.82827 | -46.236 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1af6175d-abb7-3945-85a6-422f8bd8b602 | -12.94837 | -54.80687 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09eb4fa8-ab96-351e-9698-fdd8675b9fcb | -12.53314 | -45.25924 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67f25f2f-c83f-304b-9532-4cba20100689 | -11.12235 | -52.03509 | 2025-09-09 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70915817-4ff5-380f-a55c-74f8c1c765bd | -12.52935 | -45.25869 | 2025-09-09 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb1dc433-7e1b-36cd-b373-5db1c22dec6e | -8.05826 | -48.65438 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61f4b403-1307-31fb-8a34-2ed9b7b5bcf0 | -11.37365 | -43.52844 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec016ab4-015e-3ebe-8132-36e492895cd3 | -11.41833 | -43.58857 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 518934fc-cb4f-3939-8f52-8c67d3b8ec0a | -13.94922 | -48.2403 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b29a735-4a60-3cfb-b775-fdd70126731b | -9.25036 | -57.07632 | 2025-09-09 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1b1dd4d-aa0e-3fb4-9432-a915c894fffe | -13.87919 | -44.45723 | 2025-09-09 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed1e2cbe-e122-332e-a826-5f82d523c0bc | -11.98423 | -51.01105 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f479d9db-0c35-3e5a-b00b-d2b3b988abdb | -12.03139 | -51.09108 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fea82d5-4683-394e-be8d-4b6e5c223839 | -11.55503 | -49.04536 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8354895f-aae4-3015-959b-1fe3817f2237 | -12.15558 | -49.0778 | 2025-09-09 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d3e62a4-0ce2-3421-b5dc-d5632c394cf1 | -10.56907 | -51.99752 | 2025-09-09 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a543898-2fdc-3b5e-89a3-bd751a9068be | -8.33975 | -45.05571 | 2025-09-09 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5e1a566-315c-3298-a447-0da29bcdfa58 | -11.32938 | -46.53741 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72fe3405-d8da-3152-95ec-ace7b99088a4 | -9.89285 | -46.47805 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a709b16b-bf66-314b-b968-5f57c3c39a2e | -11.43647 | -43.61086 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbc56594-09fa-3c01-9580-fe96cf8b3330 | -13.02761 | -48.02625 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25d0ab21-f25e-3531-9aff-52a23c73e38e | -11.65544 | -46.87284 | 2025-09-09 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63f5e3f4-7a6c-3c2e-990d-36f218608d2a | -11.81624 | -51.41702 | 2025-09-09 04:34:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c50074e8-8080-3683-9100-7c87807c0a2c | -12.85045 | -47.97658 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
