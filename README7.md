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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac4bd6a-ab60-3159-9b56-77d0f370b57b | -10.47065 | -47.94709 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 061c449c-14b4-3825-8fdd-e597b1deaee0 | -13.14412 | -56.80191 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0eaac439-24fc-3f19-9579-2f676fbc40d5 | -10.74511 | -49.28246 | 2025-05-25 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd9f09c3-c111-39bc-87eb-f33f92cc5556 | -11.30558 | -54.02353 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| febbfe5a-4034-3a48-bb18-1a6fc9289309 | -11.14602 | -48.11117 | 2025-05-25 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d92465f6-8653-3950-ad1c-15200dd8791d | -13.10202 | -52.28577 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6889e97f-3e8d-3f27-9871-fc0005f58f87 | -8.84579 | -49.84359 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4261b1c-b80a-3dea-9aca-11d8444dcc62 | -8.90253 | -50.0265 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aec23ff-ca92-3e49-b807-b0dbc09267fa | -12.37309 | -49.9942 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73583a1e-3b91-3f8b-9c5e-4869981d1a07 | -12.37696 | -49.99118 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b0cfd55-3af9-38e5-8565-16bc4b66ce39 | -13.09061 | -54.86939 | 2025-05-25 04:40:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fad20f7-7bdf-3786-af0f-f46cd12c30da | -11.3607 | -55.12847 | 2025-05-25 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02570ebd-8e31-3f9e-b33d-4b393b3f1b3b | -8.75682 | -48.03875 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 638e0d7b-88da-327d-9834-a6e468a14c25 | -11.99008 | -57.21029 | 2025-05-25 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60a661cc-6b3f-39cb-99e3-de0e0b3f160a | -12.27702 | -44.59742 | 2025-05-25 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a201cade-a0ea-3276-855f-a7515e1dbc59 | -10.74067 | -49.2891 | 2025-05-25 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22d5493b-c578-3491-b947-49ed1c0d5f9c | -8.71581 | -50.25978 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e15d60fc-f122-3be0-9b6c-7290c90371a1 | -7.63649 | -46.11273 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e82417ba-5ce8-3cec-9528-4269ac9ebebd | -14.56758 | -48.33031 | 2025-05-25 04:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f1af5ad-b01b-3f99-811d-7a37c9aff583 | -13.8907 | -49.64235 | 2025-05-25 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 974ff19e-2463-3600-b947-4d606ed9000e | -10.74122 | -49.28552 | 2025-05-25 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da2c9d9f-565e-3714-9622-4161a2b7fe6b | -7.65165 | -46.1048 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| beda4f87-45e1-3617-bdb4-ae9cc47e5cce | -8.05655 | -43.13995 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| c1ced9ad-d688-35b6-9d07-88b1cd78ba60 | -14.25281 | -47.14964 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd1c0e67-ae23-38d2-98bc-8f8e164d5e34 | -13.09751 | -52.29247 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd1c30d4-bb5f-32de-8783-f05e6268c7ff | -8.06064 | -43.12503 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e87bf64-816f-32b3-a822-608eee664f13 | -11.14545 | -48.11508 | 2025-05-25 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2045265-6f52-33d5-8d45-e8918bd5d4ea | -8.7534 | -48.03822 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0a8f9f-f352-3f73-acbf-9373f35b6b6e | -12.37418 | -49.98709 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 545c4288-2b3f-369b-bee2-356acd9aaa5c | -8.07266 | -43.12381 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b4251acd-1a6f-3bba-8469-7a4d139262ab | -8.06843 | -43.13538 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2f063d61-8114-38c9-a436-32c387a7f70c | -11.99447 | -57.21103 | 2025-05-25 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8747acf2-14ae-3da2-9682-527f01474069 | -12.27542 | -44.59539 | 2025-05-25 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 612c30c5-9be0-384b-82a5-1714ad7e2d0a | -11.13745 | -53.92719 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f227d816-17f4-3644-a5a0-cee2dc7c0516 | -11.29735 | -53.97956 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41413dbf-3def-3cbe-a9c0-60a7cb1d5138 | -8.64965 | -45.4366 | 2025-05-25 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85d2a6ec-e5c2-355b-8bb4-9fcf07fb380a | -11.36543 | -55.1242 | 2025-05-25 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b8f47df-ee69-35c5-a81c-5ca110e79c55 | -10.72856 | -52.46983 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31e2bb73-2722-3b38-b437-2dc9a714c6df | -10.37035 | -46.66309 | 2025-05-25 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 655cf724-355e-332f-bb74-785e7037a1ae | -10.36786 | -47.98004 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c612f92c-7915-3aca-bdd8-3cc7b3d0e0e0 | -8.06685 | -43.13221 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 64b65666-4518-37b0-9eb2-48e522ee95be | -10.36207 | -47.97124 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1693e468-656c-3c02-8d66-b149b075740c | -11.29691 | -53.98672 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d954aeb2-99bd-38a4-9aa8-e6ed4e70c714 | -7.66708 | -46.10263 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7d8ec31-6615-3c0e-9cda-92c89effea15 | -11.42492 | -54.31816 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1880ed4d-cdaa-388e-ac75-b502e911499f | -11.86695 | -52.2564 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bb60379-8c63-3dc4-9905-14d91e5a542c | -10.57506 | -48.63086 | 2025-05-25 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6ee52f3-75d5-3da3-908f-679669b5cb83 | -7.66274 | -46.10649 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a252a3eb-7d73-3e54-947f-f46beb1d8dcd | -7.93759 | -47.1892 | 2025-05-25 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8433da0-6838-30c5-a4db-fa1cdebdadbe | -13.10144 | -52.2894 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59741852-5a2f-3e26-b0b1-ba5d082673bb | -9.79741 | -48.53541 | 2025-05-25 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 468755f1-fa08-31fd-af5f-0db1b4db8c6a | -7.66403 | -46.09766 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1a23c8d-be31-31fa-884f-5db2b7a71a94 | -8.90087 | -44.78314 | 2025-05-25 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90242eb8-46b7-3e9e-be34-75c5afaca8cb | -7.94966 | -44.86413 | 2025-05-25 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 103b2a0c-ca05-300b-bd92-96ab748df348 | -11.14254 | -48.11061 | 2025-05-25 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6373451-6343-38cf-8628-cc345c2136e7 | -10.94613 | -48.61015 | 2025-05-25 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd2ade6-3713-31d3-b5be-a0d422987221 | -12.27647 | -44.60164 | 2025-05-25 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 879d604e-c596-3ea5-abd4-c9496c923c3d | -12.37364 | -49.99064 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb20fd5c-8ce3-3cf9-8460-ab10edd2c36e | -7.65294 | -46.09598 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdb86e40-0356-3c15-8612-27605791db1c | -11.13526 | -53.91804 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e9874c1-cdd7-3af5-8365-111cc10b3a7f | -12.18445 | -54.24924 | 2025-05-25 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2bf9143-f1ba-3cde-bfa2-d19fbf5168dc | -10.7012 | -48.60793 | 2025-05-25 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c42bdd5a-f926-3631-8f6a-328f3e62fad7 | -10.7391 | -53.88155 | 2025-05-25 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99f90224-1342-3986-96ec-c25e7042735d | -12.25778 | -56.5895 | 2025-05-25 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7cee2d-4efc-3e58-8318-0432b766d33a | -8.90583 | -50.02702 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fc9deef-fe64-35a1-bfce-c40ce7163f11 | -8.7323 | -47.99288 | 2025-05-25 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 514d9579-d839-3c7b-b8ab-5ecd7a374a01 | -10.36771 | -46.66496 | 2025-05-25 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5efbf9d-0dc9-3c5b-9a1f-ded061f8753a | -12.18809 | -54.24989 | 2025-05-25 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab927b80-9456-3232-96ef-a2065c119329 | -8.77764 | -47.23557 | 2025-05-25 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b710700e-f817-32c4-ac5a-0dd3d83435c8 | -12.37641 | -49.99473 | 2025-05-25 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a4f68de-b4c4-3fb4-929f-7352da3d6f6b | -10.95143 | -48.1513 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f0f220c-ee80-3dfa-94db-4c79127768f3 | -10.3748 | -47.98111 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f7a7baa-89e0-3180-92f9-121f9057b99b | -10.94854 | -48.14689 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fa297e3-9f09-3886-b764-82b71a59f303 | -11.40456 | -52.95649 | 2025-05-25 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0332017c-d8ca-39a7-8300-85e49d40dcc2 | -11.30027 | -53.9845 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5816bfed-3320-3519-a2c8-3ebc1a312f48 | -8.05368 | -43.14252 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1b4f82ad-a76f-3118-9752-672aebdca1a7 | -11.36628 | -55.11926 | 2025-05-25 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 459699ce-f378-3fc3-b587-cfaa5183ed9c | -9.93287 | -44.18118 | 2025-05-25 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e9f646a-c5b8-3745-b2aa-3547fb100ae4 | -7.66338 | -46.10211 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6456a3f-e4af-321a-8b21-0aa030e0c971 | -11.97523 | -44.1587 | 2025-05-25 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7baa915-99f4-399b-9939-fbcfcaaf5e7e | -11.91593 | -54.41298 | 2025-05-25 04:40:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6658b6f0-6ba7-3a14-83b0-f9707cdc922d | -7.65663 | -46.09655 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ba12249-a31f-35e5-861d-7a939c5e62a2 | -12.52656 | -52.45617 | 2025-05-25 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4190fa6-640c-3023-b8ec-c06bd1169ff7 | -13.14759 | -56.80661 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49b47330-a8d5-3370-8d4e-c2a4d0b0b121 | -12.75736 | -49.32053 | 2025-05-25 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbc5ed15-11fa-3778-822a-b10cc99bfe9d | -11.39829 | -52.95143 | 2025-05-25 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d6035f-1aa6-3015-8f8e-21a4bbebf55d | -10.36728 | -47.98388 | 2025-05-25 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c25c10eb-b4d7-3b1d-bec5-1ea0c24a0cc3 | -7.65358 | -46.09152 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0066d17a-891f-36b3-8157-ce24de9163f1 | -11.29663 | -53.98389 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1a820d-4d1a-3c90-b4d4-40ebd153a688 | -9.85168 | -48.56639 | 2025-05-25 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8bc12d5-8d16-3190-8bb6-2e803e37835e | -7.66033 | -46.09711 | 2025-05-25 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 204cf029-b845-35c4-84ff-f3874bdb4906 | -8.44073 | -49.62666 | 2025-05-25 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21f12105-84b4-35fa-a20c-014e462bf167 | -10.52847 | -47.58153 | 2025-05-25 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4f5b11a-09e8-3cc2-a6d3-ee9bf1657ebd | -13.15176 | -56.80739 | 2025-05-25 04:40:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b7d520e-e37a-3336-8597-7577dd09124d | -7.9411 | -47.18972 | 2025-05-25 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89b15e76-3937-35aa-b445-05bba76bd0d3 | -9.03632 | -48.94111 | 2025-05-25 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a652589-7e22-33bc-8c99-d373ab75caa7 | -12.26196 | -56.59027 | 2025-05-25 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bc989d2-786a-327e-a80f-b38b6595a4a3 | -8.06621 | -43.1367 | 2025-05-25 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ce8f2cbd-0806-39e7-a4a5-6a80dee129b9 | -11.30484 | -54.02788 | 2025-05-25 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bf91b89-0ddd-35d9-98f6-8230cda5f81e | -21.22041 | -48.61046 | 2025-05-25 04:42:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
