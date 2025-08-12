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
| 735f656e-6b91-3e6b-a325-d00b44a6b98f | -9.07117 | -45.06258 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd53ed23-577d-3544-a0e9-d06307b2784f | -10.35483 | -50.83301 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 584132d7-139c-35d5-9c53-4ea312dc9bb9 | -9.21157 | -48.52309 | 2025-08-12 04:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4a4741c-0780-3610-94d2-cdf036dc6f21 | -12.99347 | -44.88478 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 801ef475-cc3b-387c-b9ef-e896ed59eeb8 | -11.80978 | -44.93657 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 075f4288-0871-36a7-8e30-a4a126db8618 | -7.55621 | -47.04539 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a12bff25-9e00-31ca-a8da-7696aab55e24 | -12.55735 | -47.01263 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 7882059c-249f-37b9-8265-39c77f8ad3d4 | -11.71839 | -47.77429 | 2025-08-12 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38eb8764-09c4-39f2-9202-60d02c3554db | -10.35613 | -50.82611 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ee0a32f-2666-31db-a211-7ef5fab44c0a | -10.6295 | -44.75177 | 2025-08-12 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d5682cd-a949-35e7-8885-4f5a956eab3b | -11.46386 | -50.14967 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 572af753-33d5-3472-8853-dd9c57fafb1a | -10.31008 | -54.15946 | 2025-08-12 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 912c759c-defb-30f8-a2aa-e2d9ef081a46 | -13.87889 | -45.57622 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa650878-a6e8-3d8d-a3d7-d1f29219759d | -12.49678 | -46.34413 | 2025-08-12 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56187300-7cea-3e28-954b-873369478f81 | -9.71696 | -49.48375 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| deceeb61-77fa-35a2-91fd-a823d1a30992 | -9.62983 | -40.58904 | 2025-08-12 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 32374381-5f8a-3a35-996d-eca5d4a17ca4 | -8.1554 | -49.14608 | 2025-08-12 04:08:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 518f9b76-45ed-393f-98d4-26eb2ae22a2b | -14.12713 | -44.8881 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb0e5bfa-c7f8-33ae-a3a2-fe497567943a | -12.56147 | -46.98911 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 871a3e3a-7549-3b10-9bd9-0a1225a32bf7 | -13.62151 | -46.92315 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60766ae0-87b3-325b-b1dd-7a1233cb381a | -11.91384 | -44.85696 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 654e5acd-a2ea-3bb9-b2d6-d3c419ec831d | -7.87102 | -41.59982 | 2025-08-12 04:08:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d53f8f0d-77e2-3bc3-ae3e-8f393293a52a | -9.7182 | -49.48186 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56d05861-2d89-3ce9-b278-c6ecca560e23 | -12.66767 | -46.98299 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da07d018-6da6-371c-b5c9-bca9cb359ca3 | -14.11881 | -45.38417 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff769c0a-38ce-3421-9eab-e5347e4fb48c | -12.44696 | -48.72301 | 2025-08-12 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92db1242-c56c-312d-acb4-6f7772983c5e | -9.07084 | -45.06171 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f26424a-3a07-3d71-81d9-9746481dd25c | -12.56787 | -47.01889 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf419c2-7512-3803-8749-9b4858cdb8e2 | -13.34071 | -50.24254 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 24e47189-68d8-3ad2-b8a2-c507025329f7 | -13.62812 | -46.92886 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 446a68f7-9cea-3849-be4e-bb2eeaff998d | -12.65676 | -44.52371 | 2025-08-12 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d79ca26-2dfa-34f4-9527-6a3b0a1d88ae | -11.73122 | -50.11214 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0784f0de-b616-394f-be7a-2ab9d7523993 | -11.45778 | -47.32611 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58df5c3e-ddde-39c7-882f-9bc5e04ddba4 | -12.76953 | -45.45592 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48eafc9d-19cf-3ce2-996a-f6c841bf0fdb | -13.88009 | -45.57734 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f7ad772-0891-3ab7-9337-bba3bc8c2eba | -11.65992 | -50.13413 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a92d7270-5a10-3102-9dcd-94629aa23984 | -8.52246 | -43.31728 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8defa227-84f8-3661-a4f7-1aa0cde69917 | -14.03401 | -47.41743 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8769aaf4-ae3a-33e1-b8d1-6044068e8991 | -13.33528 | -50.24647 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 201e7161-2380-39f0-83bd-8a45913a8021 | -12.56037 | -47.01755 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1cae8a0-a404-329d-bceb-d0687a34b1f0 | -11.25516 | -41.47334 | 2025-08-12 04:08:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10004a11-3b55-3255-b284-c7a5e681fa73 | -11.70998 | -50.12333 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cefc3d4-1676-3e24-b6a7-c6bb9fc5b064 | -8.57411 | -54.69733 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0060121e-5c21-30da-85d7-3311a1f1d6fa | -14.1054 | -45.40148 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f544722-d5c9-3e51-9276-a6e7f5a8f738 | -8.56323 | -54.71833 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| aed80d55-624d-390e-8076-f437ebe6ee5b | -13.37691 | -44.30061 | 2025-08-12 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ecc6d79-19ea-3d7a-b665-1ae5bc951652 | -12.56815 | -46.99514 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d1bc09df-7c56-3db2-b113-b0151313a0e9 | -11.67385 | -50.13681 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aba8238-4991-3737-a476-ab9c30a2d6c7 | -9.77262 | -48.75434 | 2025-08-12 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3abb3b2e-cc4e-396c-8971-0e7d11e13e51 | -10.76354 | -44.18962 | 2025-08-12 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 107c8ee1-e74b-39d0-83ff-e7da18433b19 | -11.72255 | -48.34623 | 2025-08-12 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a9bda25-330d-3315-8712-d2d2d2578dbb | -11.68413 | -51.59087 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3756a15-fb28-31ee-9445-e2cd98e6897d | -13.12029 | -46.87265 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d25d140d-17f9-3e9a-b70a-e4ca05fe611c | -11.4676 | -50.15556 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26f1bc5e-b184-30a5-ab61-c9e01ed7707f | -10.35594 | -50.82712 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cb14b1e-8b58-3dce-b72e-cb4f3bf1bc66 | -9.06537 | -45.05349 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3fbe0f43-b891-311e-8632-c8765e247700 | -10.36342 | -46.64277 | 2025-08-12 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86cdecfc-c514-3fda-ac56-acc06b539592 | -9.07051 | -45.06668 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f19f3ed-47bd-3478-955e-445c3dce36e8 | -8.21282 | -45.05326 | 2025-08-12 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 947f3421-ea91-34db-96c1-1abdb304574f | -10.34722 | -50.81842 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91bb1c52-ed56-39fe-b073-aa9df58bd767 | -9.06828 | -45.05799 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0239892-deda-39e7-9f34-6640130b62e1 | -11.70534 | -50.12244 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d51d9b1-623a-3f80-845f-c82e904f7c36 | -11.21532 | -46.26824 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70050269-dc27-30cd-b3b3-e0264b49f84a | -11.54574 | -47.3084 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdd3219a-821b-3a2d-b003-244cfeb20f97 | -12.77712 | -45.45324 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17c62385-ecbc-3523-8d2a-2f5d2a92fda2 | -12.77018 | -45.45202 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2103a11f-7028-370f-b929-7b359a384487 | -13.87728 | -45.57286 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3032f9f0-3edf-3dd5-b921-3b55ba35b6c8 | -11.74378 | -44.97274 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57c980e0-510d-393d-8e55-fe035419128c | -12.14051 | -44.92856 | 2025-08-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44fbd614-dc11-38e8-8466-d497bc93e1e1 | -11.67595 | -50.13582 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e03ccb64-d2d6-3165-9b2d-e1923f0b492a | -12.57743 | -47.09777 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6784356-a92d-34b3-830b-88c2c5ce9c4e | -14.64001 | -45.85695 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ba429a34-be8b-3096-9901-760f4e36e5f6 | -13.87664 | -45.57674 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c02839d2-d382-3915-a95f-a32814c1c5d4 | -8.55862 | -54.71672 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e3ab49c-f88e-3714-a29e-9f5afdc6b916 | -13.02594 | -46.67572 | 2025-08-12 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3de424f-7006-354d-a6fb-76bf39a48cfa | -11.8104 | -44.93276 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a34f5288-482c-3ce5-8267-06d3dd21439b | -8.12872 | -47.44125 | 2025-08-12 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8fc0d62-e798-360b-9030-32fffc97a9be | -8.51911 | -43.31674 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9e0ab80c-a9b1-3e63-8ac0-97d234782c9f | -10.34598 | -50.82524 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd369afc-2e7f-3434-847a-10bedf4016b0 | -8.51691 | -43.30905 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f19eb9c-eaf0-34d9-aeca-d24b716244f6 | -12.50114 | -46.34042 | 2025-08-12 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01576006-7a06-3fdc-ae99-0a2a72b5c45d | -11.69266 | -51.60199 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4977efcb-fbf4-3298-805c-6e19c4468592 | -9.21592 | -48.52386 | 2025-08-12 04:08:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 628b6a49-5871-38db-8005-d4f238ebbc1e | -11.84912 | -49.007 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 797bd09b-232d-3b2f-b7c9-c4239306ce40 | -12.57827 | -47.02589 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0684c44d-ec93-346b-8683-d3a6b0038e74 | -13.32372 | -43.57389 | 2025-08-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52ae0554-51b8-3093-86c8-a0093b5a8bf8 | -10.34512 | -50.83008 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82c848b1-88d6-3f1c-8327-d299857aac6b | -13.7743 | -43.21602 | 2025-08-12 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 495ca88f-4073-3bbd-915e-cd2d17669146 | -8.5698 | -54.71957 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b473008d-c54e-3fca-bbc2-b42598b8c69c | -13.62893 | -46.92409 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9176b2f-7e51-3deb-882d-f808fc00eff3 | -11.4482 | -50.16999 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 774afcae-4574-320c-9a92-57c2a223f597 | -10.75692 | -48.79082 | 2025-08-12 04:08:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 383a12a4-5454-33e1-9987-a36b84537637 | -8.57303 | -54.70292 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8416dd9a-5a45-3308-89ce-b29ff471881a | -11.68405 | -50.13365 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b6ad3c-8708-3692-99c2-ff240c4749e1 | -11.6881 | -51.59798 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f57d3bd0-bbcc-33a9-a91b-1828bacd671b | -9.20168 | -44.53374 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0030ac0-318d-3bb7-a762-37108794ed22 | -10.35703 | -50.82128 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f9258e1-8924-3e50-bf80-bc81e0438dc4 | -8.51576 | -43.3162 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 818913a8-6c36-39d5-b66b-cf702804f312 | -8.52083 | -43.30603 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dba699d-18a5-3652-aade-5255697a7e3c | -7.56027 | -47.04606 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
