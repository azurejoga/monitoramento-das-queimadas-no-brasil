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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60bca4e7-57ff-3811-a27f-5b1cefd79d63 | -14.19968 | -48.0777 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 447f1be2-d049-35bf-9d75-f6ea6129142c | -9.88252 | -46.56285 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| b7a397f4-b6c1-3de1-8a87-eeb7415c02bd | -12.96777 | -48.05442 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0edc1c3e-96ed-3bd1-8f45-02753492a76b | -10.97751 | -46.83084 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f59be6ac-4286-3f60-9d5f-779dcd0d682f | -12.46345 | -48.09166 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 884de0a9-837b-3be9-bb52-d0cc16bc9e99 | -13.8702 | -47.99411 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 507f528b-9431-3af3-ab13-8fa2721028fb | -8.73981 | -46.68799 | 2025-09-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 858f35a1-bebc-36a1-82f1-36438a0da5c6 | -9.8838 | -46.55394 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6e2c0717-2375-3af5-9048-6542c2c1988a | -9.43951 | -46.75019 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c2fda036-084d-346b-b48f-ed889306245d | -10.66213 | -51.59076 | 2025-09-04 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 217.8 |
| 34f833bc-0ae7-3b3b-8c37-4b03359606a4 | -9.5337 | -46.29744 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bf3718c9-3065-3fcc-b15a-c808867de42b | -11.04896 | -45.14907 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c7c465cb-c673-3288-9f17-184957d88116 | -12.65492 | -45.31241 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 6aed1533-98d0-332a-84be-b1ad265c3cc9 | -12.90506 | -48.03869 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 46bb71b6-9724-3f61-b8b2-7c2eeca76c16 | -10.511 | -50.43083 | 2025-09-04 12:17:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| d5d4a960-f123-3275-acd8-bbc1cba45ec8 | -10.85618 | -47.28241 | 2025-09-04 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 66fd0511-4f9f-3fdf-a4f4-4811a49ff971 | -11.62825 | -46.66633 | 2025-09-04 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 66ab7d65-f1e8-33fa-8b37-79c69a2b0a1f | -15.04622 | -50.07274 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9aa566a4-3395-3149-bf66-07e89d2a343f | -9.70388 | -51.01192 | 2025-09-04 12:17:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7a714673-5221-3651-9aaa-532919af26c8 | -12.11676 | -45.21098 | 2025-09-04 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c1eb0a2d-ab6b-34f6-950e-115c17611d1c | -15.02523 | -48.10843 | 2025-09-04 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4b46aa2d-db9c-3e28-b23c-7e927950d220 | -9.40037 | -48.02966 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3aa6bcea-7a6c-3964-9162-ef4c7c29feaf | -9.72818 | -48.30682 | 2025-09-04 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 19527ba5-02bb-3ddd-8a77-935eb359a675 | -11.84836 | -51.44903 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 47738d83-1c39-3f3d-8536-b8a5661a4be5 | -10.03675 | -48.15675 | 2025-09-04 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3bc56384-66b0-3414-89de-fc838ebbe57b | -10.46677 | -50.39225 | 2025-09-04 12:17:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 74411770-3429-3c23-8412-2cf1f3027210 | -10.99574 | -45.92585 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e6f5f495-53e8-317d-b08f-bedac52e928c | -9.71273 | -49.02301 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0350173d-d727-3ce3-b331-1ad8b83a27a7 | -9.66384 | -42.15486 | 2025-09-04 12:17:00 | TERRA_M-T | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 65e11d73-f4c3-3a60-ac0e-4f96cf523b0f | -9.8292 | -47.8125 | 2025-09-04 12:17:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 09cf46ec-67ea-3c5a-a432-ee7e37f91838 | -13.86133 | -47.9928 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 23a5c5cc-569f-3dc8-a331-6b03033435da | -12.29828 | -50.00623 | 2025-09-04 12:17:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ff8f2600-3743-3d57-951b-d537bc8fda29 | -8.91924 | -45.87825 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 85a271c6-0afb-3a71-a935-d9acba36e5a3 | -8.18769 | -47.4327 | 2025-09-04 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f1ed6e8a-8401-3fd3-927b-88872104354a | -8.73463 | -47.54012 | 2025-09-04 12:17:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 984e872b-3b74-36b7-bbd8-95dbf0c8ca9f | -14.19835 | -48.0868 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d7b0974-0cd9-3d9d-8c1b-a5ca7ab4f10d | -11.63081 | -46.64835 | 2025-09-04 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| b7ce39a9-4cae-35c2-a233-b91818402a66 | -10.1469 | -46.00091 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fad6ecf7-15c7-379c-8349-082d5725f7a8 | -12.81082 | -47.66927 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 64519919-1a6a-3dd2-a604-18e1403471ee | -14.81775 | -48.20446 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51346732-1e77-3457-9b18-9b9387f43205 | -9.70173 | -51.02571 | 2025-09-04 12:17:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| c3412a64-b791-31a1-939e-e76350f6467c | -13.70875 | -46.87753 | 2025-09-04 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2dc30ac4-396f-308c-aa7c-0f3382c7671a | -11.09774 | -45.12256 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dff572f8-815e-3b16-8ba4-441e1ecb7fd1 | -12.92905 | -48.06118 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| af931cc0-d14e-3acc-9847-95e27e88c749 | -15.19458 | -48.21199 | 2025-09-04 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66fa8c45-9fc3-3ec8-bc12-66d4360fdb07 | -14.98981 | -50.06332 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dbca9a62-0df3-33bc-b966-d1c9ddca5d71 | -10.45466 | -50.40287 | 2025-09-04 12:17:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f2eb8ef3-4fb3-321b-a072-225b72e8a420 | -15.18703 | -48.01499 | 2025-09-04 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c7f4313c-2a6d-3ebc-9f8c-375c4023a611 | -13.41176 | -45.90137 | 2025-09-04 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f7830b8d-4185-3f6b-bc1d-f9fbd399a1a0 | -9.7143 | -49.0127 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a91cdd78-09ed-3953-8aec-09716eb91cb7 | -11.95312 | -50.585 | 2025-09-04 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d1daa0bc-7b60-3c07-a91f-59447589f5cb | -10.15551 | -46.25897 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 18dcaba2-cc04-39ed-8bf3-0698addfd053 | -14.03851 | -41.43023 | 2025-09-04 12:17:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 509ff816-314b-3403-8517-bce2025ac0bc | -13.86266 | -47.98368 | 2025-09-04 12:17:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 6f3539e9-1c74-360d-a446-680d43f0c422 | -8.47387 | -45.055 | 2025-09-04 12:17:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 20f47f08-a54d-39e1-84dd-21464a16bd6a | -10.99433 | -49.76019 | 2025-09-04 12:17:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 73abef7a-ab72-30d1-b75b-54a4e8ebdad5 | -12.87971 | -48.02563 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea8fb392-6d8a-350e-9cf1-a485677fc2ec | -12.12883 | -45.92374 | 2025-09-04 12:17:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 06d11947-4705-3e2e-927b-3a02b980dfdc | -8.74109 | -46.6791 | 2025-09-04 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5a5953fc-048a-3637-97ab-6343d24da61e | -9.44192 | -46.79599 | 2025-09-04 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3320bfb4-9ee7-303a-a3bd-1111dcf0d9b1 | -13.71245 | -46.9156 | 2025-09-04 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 081a6d53-a393-3481-890a-3e40e8827925 | -14.60231 | -48.03244 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 389972d7-7197-3cfb-a68a-dcf52cd74a01 | -14.5323 | -48.07804 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d30bd55d-d2f5-3e67-8ab0-1c0ae28bb6ad | -11.80497 | -44.25948 | 2025-09-04 12:17:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c10f5a04-a39e-39de-85b7-d9b5941b7d52 | -11.62953 | -46.65734 | 2025-09-04 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d9c05e49-31c1-3171-92ae-f936be704a6f | -13.63854 | -43.81054 | 2025-09-04 12:17:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a4217fd9-ebe9-3458-b2d2-2599ec620edb | -11.85057 | -51.43509 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 19762c45-b5de-3f91-ae54-61ba5145fd1f | -14.32417 | -43.32689 | 2025-09-04 12:17:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| e6c3c031-540d-3f59-9152-0eb8537b41ac | -15.01503 | -50.0248 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 205f18d7-56d3-32df-8308-86840d077744 | -11.8592 | -51.4505 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 47e9eaf2-0e41-3c0a-938c-499eef8caff7 | -11.35943 | -46.8651 | 2025-09-04 12:17:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7f713381-450b-3b93-91c0-324eae756ac0 | -10.98635 | -46.83212 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a4f5f3b-9239-323f-aa05-33397876c307 | -10.10364 | -46.24242 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 22c08b9e-90bb-3cf1-9380-0e7867336922 | -10.62585 | -46.25611 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f5ecb94c-423b-335b-ab4e-80e3d4cea8ac | -10.75148 | -46.35062 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 38897ffd-b9e0-32ac-9295-48d665013fa7 | -10.48966 | -46.76634 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e39ccf5c-96d0-3593-941b-0a956a208c89 | -10.14156 | -46.29347 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| fdfbe30c-dc0f-3b56-a20c-93218baa6255 | -10.91771 | -50.59571 | 2025-09-04 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c50cda53-83d3-3fa5-8f13-2ea6f2e072e4 | -15.55227 | -48.41271 | 2025-09-04 12:17:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 30c3f011-8a9d-338b-ae3b-e16fe59f77ad | -12.96643 | -48.06354 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f8f1e39e-a33d-3f1c-90ea-8e2a9fbb5423 | -14.38882 | -53.07039 | 2025-09-04 12:17:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ef5a7b21-6b95-3fa8-841f-1bc98e0f0c90 | -9.6985 | -48.98919 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15c7aad0-c0c5-3593-b23c-04dafcd48cd3 | -12.50323 | -48.07598 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d66dd3d3-d7b7-3ed5-8dd2-74e883f60eef | -10.74261 | -46.34938 | 2025-09-04 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85fee4e9-79e6-39a1-8961-f374a59f3a05 | -9.87496 | -46.55268 | 2025-09-04 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| e28e955c-b46b-32bc-94c8-8c4d26494a49 | -14.98817 | -50.07389 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| adf7bc53-cf60-3922-b6bb-ddf144eef577 | -10.14563 | -46.00994 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| b1461778-0c22-3278-aead-76ab8b50ecfa | -11.8832 | -51.53094 | 2025-09-04 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 65caa4e4-014d-3331-afc0-d3041cf34dfb | -14.5691 | -48.07412 | 2025-09-04 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 61cfac49-0305-37c5-a2a5-838860ffaa15 | -15.19588 | -48.01633 | 2025-09-04 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8c860ff0-aba8-312c-914d-a43a4a124169 | -13.57426 | -48.12666 | 2025-09-04 12:17:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ca7297bb-9ed9-3c48-8a64-7d4024fa61d8 | -12.05788 | -43.50433 | 2025-09-04 12:17:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| cdefd0ff-242e-38db-bbf0-00e458201993 | -9.70639 | -49.00099 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 137f9e6b-078e-36f8-ab86-c0aa5e85676a | -15.05728 | -50.06327 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1598eec4-295c-37d4-b771-c8c53f604f50 | -15.06357 | -50.05939 | 2025-09-04 12:17:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6eb34ae7-319d-3235-b7cf-6084b6018343 | -12.28894 | -45.29737 | 2025-09-04 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cc1849b-f2c2-34bb-8f42-1f44fbf0be2b | -13.56401 | -48.13457 | 2025-09-04 12:17:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| b2ae1220-fc30-3054-b3eb-890d6db4ad76 | -13.64157 | -43.80452 | 2025-09-04 12:17:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 39577c79-4245-3594-a254-78ffb6189edd | -9.71266 | -48.95977 | 2025-09-04 12:17:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1c2964cd-849d-3623-9b5f-a5e726f94556 | -12.51489 | -48.05882 | 2025-09-04 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README101.md)
