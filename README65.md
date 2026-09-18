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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d35c54a-b701-3f6c-895e-2135d5a4129c | -10.57282 | -48.56385 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ddd20a95-9115-3eb3-b363-05ada37be47a | -6.43793 | -44.95455 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28158dfb-46ea-325a-af49-9967a4c28cf7 | -9.86387 | -48.6305 | 2026-09-18 04:57:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4038da8-e613-30fe-bf81-cc0de20120c8 | -9.38803 | -46.84618 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8a163fe-da79-30ee-a56a-6f995dc94b64 | -7.37475 | -44.5223 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96912ee8-a1e3-356b-9b14-4ca579ede6df | -10.6122 | -46.55753 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2df97097-aff5-3790-8004-370cf44e479a | -5.13091 | -56.20224 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52da0e53-b1e8-3998-817a-24fe2f238913 | -9.8351 | -49.2253 | 2026-09-18 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35dc8c41-2bde-36f9-8ab2-02d48a44c5f0 | -7.05947 | -47.48363 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf34ad9a-6518-383c-80db-4eb62c89ec90 | -12.21055 | -53.21877 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bab09d2-062e-3720-bfa3-570bf2e4d5f8 | -11.10482 | -47.09821 | 2026-09-18 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 557b8061-2ea3-31d1-92bd-2d3d21ab84c9 | -12.78287 | -47.5657 | 2026-09-18 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35b2dc72-c0f9-38c7-8cc3-4196000395be | -10.13049 | -56.76504 | 2026-09-18 04:57:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6e1a465-b3dd-3d34-ba0a-ea52c7f405c6 | -10.11627 | -46.30347 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd80a84e-84bd-3cec-b031-159b4a0e738c | -7.3923 | -44.4966 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16f55a11-aa75-3aa9-8ab4-02f332b1ad3b | -9.77083 | -46.59596 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b8b5d14-8251-345d-a7b3-d9b7799c8178 | -9.19205 | -46.7652 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39e70575-1fc3-3316-97a3-bb359fd0bbd2 | -13.47505 | -46.89925 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d3dceed-1923-3f39-8758-4251ae7b7915 | -5.74001 | -52.2442 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dce131b5-bee2-3b79-892e-8a5886e02b23 | -4.71232 | -55.75348 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ef931b6-1bd6-3126-9ca7-b0b745b9904e | -12.99993 | -46.92721 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02e8efe2-dcf7-3c7a-85e5-4b59104f490c | -11.27906 | -43.5049 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b179a9e-d1be-345e-ab28-3b8ea3dd2729 | -9.84344 | -48.39071 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0b81d66-6a8b-3c11-b2bc-acffac53e048 | -12.16845 | -46.97558 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 980779ae-1c1a-308a-9eaf-ee73a31776a1 | -8.49212 | -57.62655 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c514cba1-0140-3e33-b68a-821f050b3ee1 | -7.11303 | -55.12627 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85ed45ad-a4fe-367e-bc7b-069afd041011 | -10.59087 | -48.69569 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c9dab47-f851-30aa-9507-3646c78a5707 | -10.65526 | -50.25056 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 51f83f37-f6d7-32b2-aec2-2847e79b8ebc | -9.71302 | -54.81842 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 234498a6-61c7-3a82-9520-204d632246f6 | -5.86175 | -52.05036 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d9859c8-07f2-3ac8-8b05-61eea25f24c9 | -6.33821 | -45.69817 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8068b4e5-9232-3ea0-a2a6-276a0380ae7d | -12.26559 | -50.75457 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e5ba6dc-8182-3447-b669-0c08edd91e0b | -8.71228 | -44.87757 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d53e76-7964-387c-8503-2f34b46ba8b8 | -12.39348 | -48.47041 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a0cdd98-78ca-3dad-b243-4d361b8d4e34 | -9.76003 | -46.0878 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 079c204a-94b3-348d-9488-842a1adfe2fb | -9.94995 | -45.69053 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 43423434-9a0c-3ba6-927a-611c95fced73 | -6.31968 | -55.27862 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423f068f-d202-32e2-948b-3646d18f2667 | -11.28827 | -43.34965 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 899fd3ef-38dc-3e14-be06-0166b8dc8fea | -10.66325 | -50.26709 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad28a838-c7f2-3149-9b29-bfe9a2162f0b | -6.32885 | -52.72874 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b37d015d-497c-3cb8-a611-6d7c9b577428 | -4.51498 | -56.08624 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75257368-46b0-3da1-a508-bc7e928d0130 | -8.65793 | -47.46931 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2b271cb-80a8-35b5-9540-6c5be17dacee | -6.91175 | -41.72071 | 2026-09-18 04:57:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e124d5c5-49e1-3baf-aa6f-dd24c0c28e72 | -8.90879 | -45.01494 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9c6e0cf-f1d9-30bd-bd70-d278e69bfeb1 | -10.50665 | -46.27717 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a2befe-6f51-3ab1-9ea5-f58d26668d6c | -7.39166 | -44.50115 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 539369a7-c1cc-3ea7-8e41-ca313a80bb68 | -4.5156 | -56.08256 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1438afd6-0c8e-3bcc-8b08-ceeda0f40bd9 | -9.90931 | -46.55227 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d58f0640-82dc-3f68-8bcf-4930fb57da9f | -9.19321 | -46.75737 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2716f8ba-d51e-3dcd-b1ea-272b4fd15af2 | -9.61668 | -46.74971 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75a310ca-2fee-3d9b-b65f-3f1d8b5cddf3 | -8.11709 | -45.62298 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09401df0-3caa-3d0c-94e0-6a5d70e0fc84 | -9.84169 | -49.18133 | 2026-09-18 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc65604-d308-348f-8f48-2dc848289acc | -12.17273 | -46.98728 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7756d88-7d03-3680-a3b5-a33254ffca57 | -9.75894 | -46.09553 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fe203d2-c5dd-3ffb-ae44-2358cdf89495 | -7.62012 | -46.17228 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99124e4e-0fea-3984-b722-db9915d5d879 | -9.59501 | -45.85829 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2097f3c8-e0b4-3740-a84f-95f1972f64bd | -10.89447 | -53.99458 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ef7de4-6f28-3a81-9bdd-9ef407d81fd3 | -7.66637 | -46.08598 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aecd817c-21fb-36a2-80d2-c906354c7e1c | -8.94873 | -51.46647 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 317f7889-2fed-3ef5-b14a-8487d24e42be | -11.89158 | -47.61892 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b778379-dca6-3f2a-bd82-f6cf5621b113 | -12.55749 | -47.08266 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c97dd0c-781e-3151-8a2a-f10f5d7fff54 | -6.01554 | -51.76688 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd19442-48f9-3412-9683-ff27d7e745ee | -9.39205 | -46.84673 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e292575f-00f6-3a38-b7cc-e40f75ee97d9 | -10.61672 | -46.06826 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 943731ea-0bbe-3b41-b172-12342cf984d3 | -6.02887 | -51.8123 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa915586-63b2-38cd-bccc-f2b4b3b7f731 | -8.46464 | -44.52049 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae2661a9-5e25-3356-bf56-d08f0906c0ee | -5.75327 | -51.92415 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5dd924c-11fd-3738-8c83-33c2ddf19b57 | -9.55948 | -45.41576 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e08c1e-6c66-3896-a8f1-05fecc4a5bd9 | -9.85705 | -48.37495 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 164aaeac-cba2-39c7-afa5-bf7bd6e0e2a7 | -11.89281 | -43.82092 | 2026-09-18 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf639d8-db0f-3938-894b-529f429ab950 | -9.59387 | -45.86634 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f27418c0-90b8-3d13-be38-dfa8e3e33c6c | -10.68151 | -50.26229 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d754c375-cdf2-3cd4-9807-8af3820235fb | -9.18217 | -46.74876 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd07170d-6458-3974-983e-96a9d4cf5b6f | -4.51434 | -56.0901 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6cec647-ee8a-3e05-afcf-29e74ef921d7 | -10.68208 | -50.25857 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7659bfb-a96d-354e-bb54-a6c428b7db29 | -10.66719 | -50.46878 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 905c7173-3fbe-37f8-a427-9b1d6a18be5f | -12.31647 | -50.83027 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dd82450-954d-3219-ad05-6b7575f7b7fb | -10.91352 | -53.98621 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09fa67cb-7724-383c-94ca-58af3ae323c8 | -10.54526 | -44.84808 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a02e49c0-64d8-3795-a074-4caedb6d5576 | -10.08174 | -45.57804 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20f5930a-fa0c-372a-8dd3-08bb936d6d8c | -11.32526 | -43.35112 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5446fe5d-6b88-3ab5-8c1e-798c3142bc94 | -6.65697 | -43.63728 | 2026-09-18 04:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebfbdde4-1a50-386c-b977-1399e46bd42e | -9.78168 | -48.36113 | 2026-09-18 04:57:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c305f646-a1b4-3f05-9495-2f28eb9e9519 | -8.71681 | -44.8782 | 2026-09-18 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 228a610c-9de1-35c8-aa3f-0b162e350039 | -11.5345 | -46.88481 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3320a2f7-af67-300d-9e19-ea3590bb8b6b | -11.52427 | -46.88354 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0b0af77-fc65-3565-b7e3-d4543f5342fc | -11.87747 | -47.57518 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf5e5119-ffb0-319a-a737-0d0fd59098e7 | -8.77598 | -46.89973 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a35a55-c753-3bb9-bedd-295f40179675 | -9.94758 | -45.4501 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b5eab89-0925-37bf-92fe-09bcad631b76 | -7.34819 | -51.76427 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e9647e-2cea-345c-b1a9-b373be310f11 | -7.19806 | -44.10436 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3517461-e450-3e1f-b785-30f9e41af87d | -7.49858 | -55.01523 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7848f255-1ff7-3bf1-8595-71014c1948c1 | -10.67409 | -50.28786 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3a7d573-4c54-346a-9f85-b54b1d1656f7 | -7.45221 | -46.15902 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af7134f9-a7f2-39a5-be07-9187c15afda2 | -10.65012 | -50.23828 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b3f254d-450b-3a67-8c78-e6f927a34744 | -11.5182 | -46.86707 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a80112a5-c806-3e13-84f2-6a861ccb6a2a | -12.31987 | -50.83081 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 988fe051-4fbf-3480-ae14-9c46938d7c39 | -9.71868 | -54.80672 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e922567f-c77f-3bdd-92f8-095a11e1cb5f | -9.96028 | -45.45631 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a9fa52c-49a0-35a2-8b0b-b6fe99178fcb | -9.95048 | -45.32956 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
